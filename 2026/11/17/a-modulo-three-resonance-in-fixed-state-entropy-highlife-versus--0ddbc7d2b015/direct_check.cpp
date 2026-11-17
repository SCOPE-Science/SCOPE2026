// Exhaustive direct Moore-neighborhood update on labelled three-row tori.
// Build: g++ -O3 -std=c++17 direct_check.cpp -o direct_check
// Run: ./direct_check
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
using namespace std;
int main() {
    const int expected_h[8]={0,0,0,127,37,91,2539,1009};
    const int expected_l[8]={0,0,0,127,39,121,2595,1177};
    for(int n=3;n<=7;n++) {
        uint64_t count_l=0,count_h=0;
        const uint64_t configurations=1ULL<<(3*n);
        for(uint64_t x=0;x<configurations;x++) {
            int cols[7],wt[7];
            for(int j=0;j<n;j++){
                cols[j]=(x>>(3*j))&7;
                wt[j]=__builtin_popcount((unsigned)cols[j]);
            }
            bool life=true,highlife=true;
            for(int j=0;j<n;j++){
                int three=wt[(j+n-1)%n]+wt[j]+wt[(j+1)%n];
                for(int r=0;r<3;r++){
                    int bit=(cols[j]>>r)&1;
                    int k=three-bit;
                    bool s=(k==2 || k==3), b3=(k==3), b36=(k==3 || k==6);
                    if(bit){ if(!s){life=false;highlife=false;} }
                    else {if(b3)life=false;if(b36)highlife=false;}
                }
                if(!life&&!highlife)break;
            }
            count_l+=life; count_h+=highlife;
        }
        assert(count_h==expected_h[n] && count_l==expected_l[n]);
        cout<<n<<" "<<count_h<<" "<<count_l<<"\n";
    }
    cout<<"PASS exhaustive independent direct update through circumference 7\n";
}
