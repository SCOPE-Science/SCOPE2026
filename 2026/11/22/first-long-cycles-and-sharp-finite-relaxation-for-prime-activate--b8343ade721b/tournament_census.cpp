#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
#include <array>
#include <cstring>
#include <algorithm>
using namespace std;
// Tournament encoding: bits indexed by pairs (i,j), 0<=i<j<n, in lexicographic order.
// 1: arc i->j; 0: arc j->i. States are bit masks of active vertices.
int main(int argc, char** argv){
 int n=argc>1?atoi(argv[1]):7; if(n<1||n>7){fprintf(stderr,"require 1<=n<=7\n");return 2;}
 int e=n*(n-1)/2, N=1<<n;
 uint64_t G=1ULL<<e;
 uint64_t count_max[130]={0}, count_any[130]={0}, count_orbits[130]={0};
 uint64_t witness[130];for(int i=0;i<130;i++)witness[i]=UINT64_MAX;
 uint8_t wstate[130]={0};
 uint64_t by_t[130]={0}; int maximum_depth=0;
 vector<uint8_t> f(N), indeg(N), visited(N), depth(N), q(N);
 for(uint64_t code=0;code<G;code++){
   uint32_t pred[8]={0};int bit=0;
   for(int i=0;i<n;i++)for(int j=i+1;j<n;j++,bit++){
     if(code&(1ULL<<bit)) pred[j]|=1u<<i; else pred[i]|=1u<<j;
   }
   memset(indeg.data(),0,N);
   for(int s=0;s<N;s++){
     unsigned t=0;
     for(int j=0;j<n;j++){
       int d=__builtin_popcount(pred[j]&(uint32_t)s);
       t|=(unsigned)(d==2 || d==3 || d==5) << j;
     }
     f[s]=t;indeg[t]++;
   }
   int head=0,tail=0;
   for(int s=0;s<N;s++)if(indeg[s]==0)q[tail++]=s;
   while(head<tail){
     int s=q[head++];
     if(--indeg[f[s]]==0)q[tail++]=f[s];
   }
   // Remaining vertices are exactly periodic states.
   memset(visited.data(),0,N);
   int maxp=0;
   for(int s=0;s<N;s++){
     if(!indeg[s]||visited[s])continue;
     int length=0,h=s;
     do {visited[h]=1;h=f[h];length++;} while(h!=s);
     count_orbits[length]++;
     if(witness[length]==UINT64_MAX){witness[length]=code;wstate[length]=s;}
     count_any[length]++;maxp=max(maxp,length);
   }
   count_max[maxp]++;
   // Distances to periodic sets: reverse of peel order (depth measured at each s).
   memset(depth.data(),0,N);
   for(int t=tail-1;t>=0;t--){int s=q[t];depth[s]=depth[f[s]]+1;maximum_depth=max(maximum_depth,(int)depth[s]);by_t[depth[s]]++;}
 }
 printf("n=%d graphs=%llu max_possible_depth=%d\n",n,(unsigned long long)G,maximum_depth);
 printf("max_period_graph_counts:");for(int p=1;p<=N;p++)if(count_max[p])printf(" %d:%llu",p,(unsigned long long)count_max[p]);puts("");
 printf("cycles_detected_over_all_graphs:");for(int p=1;p<=N;p++)if(count_any[p])printf(" %d:%llu",p,(unsigned long long)count_any[p]);puts("");
 printf("orbits_over_all_graphs:");for(int p=1;p<=N;p++)if(count_orbits[p])printf(" %d:%llu",p,(unsigned long long)count_orbits[p]);puts("");
 printf("first_witness_graph_and_state:");for(int p=1;p<=N;p++)if(count_any[p])printf(" %d:%llu/%u",p,(unsigned long long)witness[p],wstate[p]);puts("");
 printf("transient_counts_positive:");for(int t=1;t<=maximum_depth;t++)if(by_t[t])printf(" %d:%llu",t,(unsigned long long)by_t[t]);puts("");
}
