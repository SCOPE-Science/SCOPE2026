#include <cstdint>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>
using namespace std;
static constexpr unsigned V=12, N=1u<<(2*V);
static constexpr unsigned edges[][2]={{0,1},{0,4},{0,6},{0,9},{1,2},{1,5},{1,7},{2,3},{2,6},{2,8},{3,4},{3,7},{3,9},{4,5},{4,8},{5,10},{5,11},{6,10},{6,11},{7,8},{7,11},{8,10},{9,10},{9,11}};
unsigned nb[V]={};
unsigned nxtstate(unsigned s){
    unsigned exc=0;
    for(unsigned i=0;i<V;i++) if(((s>>(2*i))&3)==1) exc|=1u<<i;
    unsigned out=0;
    for(unsigned i=0;i<V;i++) {
        unsigned x=(s>>(2*i))&3;
        unsigned y=x==0 ? ((nb[i]&exc)?1:0) : ((x+1)&3);
        out |= y<<(2*i);
    }
    return out;
}
int main(){
    for(auto &e:edges){nb[e[0]]|=1u<<e[1];nb[e[1]]|=1u<<e[0];}
    for(unsigned i=0;i<V;i++) assert(__builtin_popcount(nb[i])==4);
    vector<uint32_t> nxt(N), indeg(N), queue(N);
    for(uint32_t s=0;s<N;s++) {uint32_t t=nxtstate(s);nxt[s]=t;indeg[t]++;}
    uint32_t tail=0;
    for(uint32_t s=0;s<N;s++) if(indeg[s]==0) queue[tail++]=s;
    uint32_t head=0;
    while(head<tail){uint32_t s=queue[head++];uint32_t t=nxt[s];if(--indeg[t]==0)queue[tail++]=t;}
    vector<uint16_t> period(N,0), depth(N,0);
    map<unsigned,uint64_t> cycs;
    for(uint32_t s=0;s<N;s++) if(indeg[s]&&period[s]==0){
       uint32_t t=s;unsigned p=0;do{p++;t=nxt[t];}while(t!=s);
       t=s;do{period[t]=p;t=nxt[t];}while(t!=s);
       cycs[p]++;
    }
    for(int64_t i=int64_t(tail)-1;i>=0;i--){uint32_t s=queue[i], t=nxt[s]; period[s]=period[t]; depth[s]=depth[t]+1;}
    map<pair<int,int>,uint64_t> census;map<int,uint64_t> depths, periods;
    uint32_t maxdepth=0;uint64_t maxcount=0;
    for(uint32_t s=0;s<N;s++) {auto d=depth[s], p=period[s]; assert(p>0);census[{d,p}]++;periods[p]++;depths[d]++;if(d>maxdepth){maxdepth=d;maxcount=1;}else if(d==maxdepth)maxcount++;}
    printf("graph=Chvatal vertices=%u edges=24 q=4 threshold=1 total=%u\n",V,N);
    printf("cycle_orbits");for(auto [p,c]:cycs)printf(" %d:%llu",p,(unsigned long long)c);puts("");
    printf("max_first_entry=%u count=%llu\n",maxdepth,(unsigned long long)maxcount);
    printf("period_basin");for(auto [p,c]:periods)printf(" %d:%llu",p,(unsigned long long)c);puts("");
    printf("depth_census");for(auto [d,c]:depths)printf(" %d:%llu",d,(unsigned long long)c);puts("");
    printf("joint_census");for(auto [dp,c]:census)printf(" (%d,%d):%llu",dp.first,dp.second,(unsigned long long)c);puts("");
    printf("sum=%llu recurrent=%llu joint_classes=%zu\n",(unsigned long long)N,(unsigned long long)(N-tail),census.size());
    printf("maximal_states");for(uint32_t s=0;s<N;s++)if(depth[s]==maxdepth)printf(" %u",s);puts("");
}
