#include <cstdint>
#include <cstdio>
#include <cassert>
using namespace std;
static constexpr unsigned V=12, N=1u<<24;
static constexpr int E[24][2]={{0,1},{0,4},{0,6},{0,9},{1,2},{1,5},{1,7},{2,3},{2,6},{2,8},{3,4},{3,7},{3,9},{4,5},{4,8},{5,10},{5,11},{6,10},{6,11},{7,8},{7,11},{8,10},{9,10},{9,11}};
int main(){
    uint16_t nbr[12]={};
    for(auto e:E){nbr[e[0]]|=1u<<e[1];nbr[e[1]]|=1u<<e[0];}
    uint64_t total=0;
    for(uint32_t s=0;s<N;s++){
        uint16_t c[4]={};
        for(int i=0;i<12;i++)c[(s>>(2*i))&3] |= 1u<<i;
        bool valid=true;
        for(int i=0;i<12;i++){
            int a=(s>>(2*i))&3;
            if((nbr[i]&c[(a+1)&3])==0){valid=false;break;}
        }
        total+=valid;
    }
    assert(total==118408);
    printf("successor_supported_four_colorings=%llu\n",(unsigned long long)total);
    printf("primitive_four_orbits=%llu\n",(unsigned long long)(total/4));
}
