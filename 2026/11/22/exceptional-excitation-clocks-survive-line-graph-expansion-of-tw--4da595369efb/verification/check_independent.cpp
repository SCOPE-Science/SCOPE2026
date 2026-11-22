// Exact finite-state checker for three-state excitable dynamics on two edge-adjacency graphs.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 if(argc!=2) return 2;
 int k=atoi(argv[1]); if(k!=1 && k!=2) return 2;
 array<pair<int,int>,15> edges;
 for(int i=0;i<5;i++){edges[i]={i,(i+1)%5}; edges[i+5]={i,i+5};edges[i+10]={i+5,(i+k)%5+5};}
 array<vector<int>,15> neighbors;
 for(int i=0;i<15;i++)for(int j=0;j<15;j++)if(i!=j){
   auto [a,b]=edges[i];auto [c,d]=edges[j];
   if(a==c||a==d||b==c||b==d) neighbors[i].push_back(j);
 }
 for(auto v:neighbors)assert(v.size()==4);
 constexpr int N=14348907;array<int,15> pow3;pow3[0]=1;for(int i=1;i<15;i++)pow3[i]=pow3[i-1]*3;
 vector<int> successor(N);vector<uint32_t> in_degree(N,0);
 // Independent implementation with explicit arrays and per-vertex successor tests.
 for(int x=0;x<N;x++){
  int digits[15]={};int t=x;
  for(int i=0;i<15;i++){digits[i]=t%3;t/=3;}
  int y=0;
  for(int i=0;i<15;i++){
   int v=digits[i];
   if(v==0){for(int j:neighbors[i]) if(digits[j]==1){v=1;break;}}
   else if(v==1)v=2;
   else v=0;
   y+=pow3[i]*v;
  }
  successor[x]=y; in_degree[y]++;
 }
 // Prune the finite functional digraph. The surviving vertices are precisely recurrent ones.
 vector<int> q;q.reserve(N);
 for(int i=0;i<N;i++)if(in_degree[i]==0)q.push_back(i);
 for(size_t start=0;start<q.size();start++){
  int v=q[start],w=successor[v];
  if(!--in_degree[w])q.push_back(w);
 }
 vector<uint8_t> d(N,0),p(N,0);
 map<int,uint64_t> cycles;
 for(int i=0;i<N;i++)if(in_degree[i] && p[i]==0){
  int len=1;for(int t=successor[i];t!=i;t=successor[t]) len++;
  for(int t=i;;t=successor[t]){p[t]=len;if(successor[t]==i)break;}
  cycles[len]++;
 }
 for(auto it=q.rbegin();it!=q.rend();++it){int v=*it,w=successor[v];p[v]=p[w];d[v]=d[w]+1;}
 map<pair<int,int>,uint64_t> hist;int maxd=0;
 for(int i=0;i<N;i++){assert(p[i]!=0);hist[{p[i],d[i]}]++;maxd=max(maxd,(int)d[i]);}
 cout<<"P "<<k<<" N "<<N<<" PRUNED "<<q.size()<<" MAXD "<<maxd<<'\n';
 cout<<"CYCLES\n";for(auto [len,n]:cycles)cout<<len<<' '<<n<<'\n';
 cout<<"PERIOD_ENTRY\n";for(auto [pd,n]:hist)cout<<pd.first<<' '<<pd.second<<' '<<n<<'\n';
}
