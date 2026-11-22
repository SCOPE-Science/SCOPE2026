// Independent finite-state classifier using Hamiltonian LCF graph and path tracing.
#include <cstdio>
#include <cstdint>
#include <vector>
#include <map>
#include <algorithm>
#include <numeric>
using namespace std;
constexpr int N=1<<24, V=12;
int neighbors[V][3], degrees[V]{};
void add(int a,int b){
 for(int i=0;i<degrees[a];i++)if(neighbors[a][i]==b)return;
 neighbors[a][degrees[a]++]=b;neighbors[b][degrees[b]++]=a;
}
void setup(){
 int shifts[V]={-5,-2,-4,2,5,-2,2,5,-2,-5,4,2};
 for(int v=0;v<V;v++) add(v,(v+1)%V);
 for(int v=0;v<V;v++) add(v,(v+shifts[v]+V)%V);
 for(int v=0;v<V;v++)if(degrees[v]!=3){fprintf(stderr,"bad cubic degree\n");exit(2);}
}
uint32_t evolve(uint32_t n){
 unsigned char x[V];
 for(int i=0;i<V;i++)x[i]=(n>>(2*i))%4;
 uint32_t out=0;
 for(int i=0;i<V;i++){
   unsigned char cur=x[i];
   if(cur==0){
      for(int t=0;t<3;t++) if(x[neighbors[i][t]]==1){cur=1;break;}
   }else{cur=(cur+1)%4;}
   out|=uint32_t(cur)<<(2*i);
 }
 return out;
}
int main(){
 setup();
 vector<uint32_t> mark(N,0);vector<uint16_t> dist(N,0),period(N,0),orbitID(N,0); vector<int> op(1,0);
 vector<uint32_t> path;path.reserve(256);
 map<int,uint64_t> cycles;
 for(uint32_t s=0;s<N;s++){
   if(mark[s]==1)continue;
   uint32_t p=s;path.clear();
   while(mark[p]==0){mark[p]=s+2;path.push_back(p);p=evolve(p);}
   if(mark[p]==s+2){
      auto it=find(path.begin(),path.end(),p);
      if(it==path.end()){fprintf(stderr,"cycle detection failed\n");return 3;}
      int k=int(path.end()-it);cycles[k]++;op.push_back(k);
      for(;it!=path.end();it++){period[*it]=k;dist[*it]=0;orbitID[*it]=op.size()-1;mark[*it]=1;}
      while(!path.empty()&&mark[path.back()]==1)path.pop_back();
   }
   for(auto it=path.rbegin();it!=path.rend();it++){
      uint32_t next=evolve(*it);period[*it]=period[next];dist[*it]=dist[next]+1;orbitID[*it]=orbitID[next];mark[*it]=1;
   }
 }
 vector<uint64_t> bc(op.size());
 map<pair<int,int>,uint64_t> hist;
 int maxentry=0;map<int,uint64_t> last;
 for(int i=0;i<N;i++){
  hist[{dist[i],period[i]}]++;bc[orbitID[i]]++;
  if(dist[i]>maxentry){maxentry=dist[i];last.clear();}
  if(dist[i]==maxentry)last[period[i]]++;
 }
 printf("N %d maxentry %d\nORBITCOUNTS\n",N,maxentry);
 for(auto [p,c]:cycles)printf("%d %llu\n",p,(unsigned long long)c);
 printf("MAX_STATES\n");for(auto [p,c]:last)printf("%d %llu\n",p,(unsigned long long)c);
 map<int,vector<uint64_t>> lists;for(int j=1;j<(int)op.size();j++)lists[op[j]].push_back(bc[j]);printf("BASIN_SIZES_BY_PERIOD\n");
 for(auto &[p,v]:lists){sort(v.begin(),v.end());printf("%d count=%zu min=%llu max=%llu sum=%llu\n",p,v.size(),(unsigned long long)v.front(),(unsigned long long)v.back(),(unsigned long long)accumulate(v.begin(),v.end(),0ULL));if(p!=4){printf("VALUES");for(auto k:v)printf(" %llu",(unsigned long long)k);printf("\n");}}
 printf("HIST\n");for(auto [key,c]:hist)printf("%d %d %llu\n",key.first,key.second,(unsigned long long)c);
}
