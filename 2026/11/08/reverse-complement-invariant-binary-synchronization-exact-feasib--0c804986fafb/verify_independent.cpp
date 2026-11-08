// Independent integer-bit implementation of the small-length strand-pair census.
// All-length claims use a mathematical proof; this is a finite consistency check.
#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <cstdint>
#include <stdexcept>
using namespace std;
uint32_t reversal_complement(uint32_t x,int n){
    uint32_t out=0;
    for(int i=0;i<n;i++) out=(out<<1)|((1^((x>>i)&1)));
    return out;
}
bool overlap(uint32_t a,uint32_t b,int n){
    for(int t=1;t<n;t++) {
        uint32_t mask=(1u<<t)-1;
        if((a>>(n-t))==(b&mask)) return true;
    }
    return false;
}
bool good(uint32_t w,int n){
    uint32_t v=reversal_complement(w,n);
    return !overlap(w,w,n)&&!overlap(v,v,n)&&!overlap(w,v,n)&&!overlap(v,w,n);
}
int main(){
    const int expected[]={0,1,2,0,2,0,4,0,8,4};
    for(int n=1;n<=9;n++){
        set<pair<uint32_t,uint32_t>> orbits;
        for(uint32_t w=0;w<(1u<<n);w++){
            if(!good(w,n))continue;
            auto v=reversal_complement(w,n);
            orbits.insert(minmax(w,v));
        }
        if((int)orbits.size()!=expected[n]){
            cerr<<"wrong "<<n<<" "<<orbits.size()<<"\n";return 1;
        }
        cout<<n<<":"<<orbits.size()<<" ";
    }
    cout<<"\nINDEPENDENT_INTEGER_OK\n";
}
