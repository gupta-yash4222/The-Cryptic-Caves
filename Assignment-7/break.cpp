#include<bits/stdc++.h>
using namespace std;
#define ll long long int 


int state[5][5][64], tempstate[5][5][64];

string hex_to_bin(char ch){
    int n;
    switch(ch){
        case '0' : n = 1; break; 
        case '1' : n = 2; break;
        case '2' : n = 3; break;
        case '3' : n = 4; break;
        case '4' : n = 5; break;
        case '5' : n = 6; break;
        case '6' : n = 7; break;
        case '7' : n = 8; break;
        case '8' : n = 9; break;
        case '9' : n = 10; break;
        case 'A' : n = 11; break;
        case 'B' : n = 12; break;
        case 'C' : n = 13; break;
        case 'D' : n = 14; break;
        case 'E' : n = 15; break;
        case 'F' : n = 16; break;
    }
    n--;
    string s;
    
    for(int i=0; i<4; i++){ s = s + char(n%2 + 48); n = n/2; }
    return s;
}

int main(){

	#ifndef ONLINE_JUDGE
	//freopen("D:\\CP_codes\\input.txt", "r", stdin);
	freopen("C:\\Users\\Yash Gupta\\Desktop\\CS641A\\SHA\\output.txt", "w", stdout);
	#endif

    cout<<"SHA ko todo\n\n\n";

    int b = 1600;
    int l = 512;
    int c = 1024;
    int r = 40;
    int rounds = 24;
    int i, j, k;

    char hexa[16] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};

    string digest = "606260E00000000080098001696566E1EE6FE9ED696566E18E0D890D696566E10E04090C000000008E0D890D696566E16E6669EC00000000606260E000000000";

    //int state[5][5][64], tempstate[5][5][64];
    for(i=0;i<5;i++) for(j=0;j<5;j++) for(k=0;k<64;k++) state[i][j][k] = tempstate[i][j][k] = 0;

    string s;

    
    //for(i=0;i<16;i++) cout<<hex_to_bin(hexa[i])<<"\n";

    //cout<<hex_to_bin(digest[0]);

    for(k=0;k<l;k+=4){
        s = hex_to_bin(digest[k/4]);
        //cout<<s<<"\n";
        for(j=0;j<4;j++) state[k/(64*5)][(k/64)%5][k%64 + j] = s[j]-'0';
    }

    
    k = 0;
    while(k < l){
        int index = 0;
        for(j = 3; j >= 0; --j)
            index = index*2 + state[k/(64*5)][(k/64)%5][k%64 + j];
        cout<<hexa[index];
        k += 4;
        if(k == 256)
            cout<<"\n";
    }
    cout<<"\n\n\n";

    

    for(k=0; k<64; k++){
        for(j=4; j>=0; j--){
             for(i=0; i<5; i++) cout<<state[i][j][k]<<" ";
             cout<<"\n";
        }
        cout<<"\n";
    }

    cout<<"\n\n\n";
   

    int n, current_round = 0, flag = 0;
    int column_parity[5];
    int A[5][5][64];  for(i=0;i<5;i++) for(j=0;j<5;j++) for(k=0;k<64;k++) A[i][j][k] = 0;
    int val[2][64]; for(i=0;i<2;i++) for(j=0;j<64;j++) val[i][j] = 0;

    

    for(k=0; k<64; k++){
        cout<<"\n---------------"<<k<<"-----------------\n";
        for(n=0; n<4; n++){
            A[0][0][k] = n&1; A[0][1][k] = n/2;
            //cout<<A[0][0][k]<<" "<<A[0][1][k]<<"\n";
            current_round = 0; flag = 0;

            for( ; current_round < rounds; current_round++){

                // theta
                //cout<<"theta\n";
                for(i=0; i<5; i++){
                    column_parity[i] = 0;
                    for(j=0; j<5; j++) column_parity[i] ^= A[i][j][k];
                }
                for(i=0; i<5; i++){
                    for(j=0; j<5; j++){
                         A[i][j][k] ^= column_parity[(i+4)%5] ^ column_parity[(i+1)%5];
                         tempstate[i][j][k] = A[i][j][k];
                    }
                }

                // pi

                for(i=0; i<5; i++){
                    for(j=0; j<5; j++) A[j][((2 * i) + (3 * j)) % 5][k] = tempstate[i][j][k];
                }

                for(i=0; i<5; i++) for(j=0; j<5; j++) tempstate[i][j][k] = A[i][j][k];

                // chi

                for(i=0; i<5; i++){
                    for(j=0; j<5; j++) A[i][j][k] = tempstate[i][j][k] ^ ((tempstate[i][(j+1)%5][k]^1) & tempstate[i][(j+2)%5][k]);
                }

            }

            for(i=0; i<2; i++){
                for(j=0; j<5; j++){
                    if(i==1 && j>2) break;
                    if(state[i][j][k] != A[i][j][k]){ flag++; break; }
                }
                if(flag) break;
            }

            if(flag){
                for(j=4; j>=0; j--){
                    for(i=0; i<5; i++) cout<<A[i][j][k]<<" ";
                    cout<<"\n"; 
                }
                cout<<"\n"; 
            }

            if(flag){
                for(i=0; i<5; i++) for(j=0; j<5; j++)  A[i][j][k] = 0;
                continue;
            }
            
            if(flag==0){
                /*
                for(j=4; j>=0; j--){
                    for(i=0; i<5; i++) cout<<A[i][j][k]<<" ";
                    cout<<"\n"; 
                }
                */
                cout<<"out - "<<(n&1)<<" "<<n/2<<"\n"; 
                cout<<"\n";
                val[0][k] = n&1; val[1][k] = n/2;
                break; 
            }

        }
    }

/*
    for(j=0; j<2; j++){
        for(k=0; k<64; k++) cout<<A[0][j][k];
        cout<<"\n"; 
    }
*/

    for(i=0;i<2;i++){
        for(j=0;j<64;j++) cout<<val[i][j];
        cout<<"\n";
    }

    cout<<"reached!!";
    
}