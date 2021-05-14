def coppersmith_howgrave_univariate(pol, N, beta, m, t, X):
    
    delta = pol.degree()
    n = delta * m + t

    polZ = pol.change_ring(ZZ)
    x = polZ.parent().gen()

    # compute polynomials
    g = []
    for i in range(m):
        for j in range(delta):
            g.append((x * X)**j * N**(m - i) * polZ(x * X)**i)
    for i in range(t):
        g.append((x * X)**i * polZ(x * X)**m)

    # construct lattice B
    B = Matrix(ZZ, n)

    for i in range(n):
        for j in range(i+1):
            B[i, j] = g[i][j]

    # LLL
    B = B.LLL()

    # transform shortest vector in polynomial
    new_pol = 0
    for i in range(n):
        new_pol += x**i * B[0, i] / X**i

    # factor polynomial
    potential_roots = new_pol.roots()
    
    # test roots
    roots = []
    for root in potential_roots:
        if root[0].is_integer():
            result = polZ(ZZ(root[0]))
            if gcd(N, result) >= N^beta:
                roots.append(ZZ(root[0]))

    return roots

e = 5



N = 84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093
C = 23701787746829110396789094907319830305538180376427283226295906585301889543996533410539381779684366880970896279018807100530176651625086988655210858554133345906272561027798171440923147960165094891980452757852685707020289384698322665347609905744582248157246932007978339129630067022987966706955482598869800151693

# RSA known parameters
ZmodN = Zmod(N);

def break_RSA(p_str, max_len):
    global e, C, ZmodN

    p_binary_str = ''.join(['{0:08b}'.format(ord(x)) for x in p_str])

    for length in range(0, max_len+1, 4):          # size of the root

        # Problem to equation (default)
        P.<x> = PolynomialRing(ZmodN) #, implementation='NTL')
        pol = ((int(p_binary_str, 2)<<length) + x)^e - C
        delta = pol.degree()

        # Tweak those
        beta = 1                                
        epsilon = beta / 7                      
        m = ceil(beta**2 / (delta * epsilon))     
        t = floor(delta * m * ((1/beta) - 1))    
        X = ceil(N**((beta**2/delta) - epsilon))  

        roots = coppersmith_howgrave_univariate(pol, N, beta, m, t, X)

        if roots:
            print("Root is :", ' {0:b}'.format(roots[0]))
            return

    print('No solution found\n')


print("start from here")

break_RSA("You see a Gold-Bug in one corner. It is the key to a treasure found by ", 300)