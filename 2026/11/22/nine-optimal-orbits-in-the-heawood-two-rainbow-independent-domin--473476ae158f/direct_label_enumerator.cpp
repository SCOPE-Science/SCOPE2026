// Independent exhaustive check: direct three-label assignments on the
// 14-vertex Fano incidence graph, with no component decomposition.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
using namespace std;
int main(){
    array<uint16_t,14> adj{};
    for(int i=0;i<7;++i)
        for(int d: {0,1,3}){
            int p=(i+d)%7, l=i+7;
            adj[p]|=uint16_t(1u<<l);
            adj[l]|=uint16_t(1u<<p);
        }
    for(int i=0;i<14;++i) assert(__builtin_popcount((unsigned)adj[i])==3);
    const int total=4782969; // 3^14
    array<int64_t,15> count{};
    array<int64_t,7> optimal_zero_point{};
    for(int code=0;code<total;++code){
        int n=code;
        array<int,14> f{};
        uint16_t one=0,two=0;
        int nonzero=0;
        for(int v=0;v<14;++v){
            f[v]=n%3;n/=3;
            if(f[v]==1){one|=uint16_t(1u<<v);++nonzero;}
            if(f[v]==2){two|=uint16_t(1u<<v);++nonzero;}
        }
        bool ok=true;
        for(int v=0;v<14&&ok;++v){
            if(f[v]==0){
                if(!(adj[v]&one) || !(adj[v]&two))ok=false;
            } else if(adj[v]&(f[v]==1?one:two))ok=false;
        }
        if(ok){
            ++count[nonzero];
            if(nonzero==8){
                int zp=0;
                for(int i=0;i<7;i++)if(!f[i])++zp;
                ++optimal_zero_point[zp];
            }
        }
    }
    const array<int64_t,15> expected{0,0,0,0,0,0,0,0,868,168,42,28,0,0,2};
    assert(count==expected);
    const array<int64_t,7> e_z{70,84,168,224,168,84,70};
    assert(optimal_zero_point==e_z);
    cout<<"WEIGHTS";
    for(int i=0;i<=14;++i)if(count[i])cout<<" "<<i<<":"<<count[i];
    cout<<"\nOPTIMUM_ZERO_POINT_COUNTS";
    for(int i=0;i<7;++i)cout<<" "<<i<<":"<<optimal_zero_point[i];
    cout<<"\nTERNARY_CERTIFICATE_OK\n";
}
