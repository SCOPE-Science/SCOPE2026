// Exhaustive parity and weight check, using Gray-code updates rather than elimination.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;
void check(int m,int n,int target_min, uint64_t target_count){
    int N=m*n;assert(N<=24);
    vector<uint32_t> update(N);
    for(int i=0;i<m;i++)for(int j=0;j<n;j++){
        int u=i*n+j; uint32_t e=0;
        e^=1u<<(((i+1)%m)*n+j);e^=1u<<(((i+m-1)%m)*n+j);
        e^=1u<<(i*n+(j+1)%n);e^=1u<<(i*n+(j+n-1)%n);
        update[u]=e;
    }
    uint32_t syndrome=0, selected=0;
    uint64_t solutions=0, at_min=0;
    int best=N+1;
    const uint64_t limit=1ull<<N;
    for(uint64_t k=0;k<limit;k++){
        if(syndrome==((1u<<N)-1u)){
            ++solutions;int w=__builtin_popcount(selected);
            if(w<best){best=w;at_min=1;}else if(w==best)++at_min;
        }
        if(k+1<limit){int z=__builtin_ctzll(k+1);syndrome^=update[z];selected^=(1u<<z);}
    }
    assert((best==N+1?-1:best)==target_min);
    assert(at_min==target_count);
    cout<<m<<"x"<<n<<" min="<<(best==N+1?-1:best)<<" minima="<<at_min<<" total="<<solutions<<" PASS\n";
}
int main(){
    check(3,3,-1,0);check(3,4,6,4);check(3,5,-1,0);
    check(4,4,4,16);check(4,5,10,4);check(4,6,12,16);
    check(5,4,10,4);check(6,4,12,16);
}
