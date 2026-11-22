// Finite exhaustive certificate for minimum resolving bases and exchanges of the Coxeter graph.
// Public mathematics only. Build: c++ -O3 -std=c++17 cox_metric_a.cpp -o a && ./a
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <stdexcept>
#include <unordered_map>
#include <vector>
#include <map>
using namespace std;
constexpr int N=28;
using Four=array<int,4>;
int main(){
 vector<vector<int>> graph(N);
 auto join=[&](int a,int b){graph[a].push_back(b);graph[b].push_back(a);};
 for(int L=0;L<3;L++){
  int st=L+1;
  for(int i=0;i<7;i++) join(7*L+i,7*L+(i+st)%7);
 }
 for(int i=0;i<7;i++) for(int L=0;L<3;L++) join(21+i,7*L+i);
 int edgeCount=0;
 for(auto &ng:graph){sort(ng.begin(),ng.end());if(ng.size()!=3||unique(ng.begin(),ng.end())!=ng.end())throw runtime_error("not cubic simple");edgeCount+=ng.size();}
 if(edgeCount!=84)throw runtime_error("bad edge count");
 array<array<int,N>,N> dist{};
 for(int x=0;x<N;x++){
  dist[x].fill(-1);queue<int>q;q.push(x);dist[x][x]=0;
  while(!q.empty()) {int v=q.front();q.pop();for(int w:graph[v])if(dist[x][w]<0){dist[x][w]=dist[x][v]+1;q.push(w);}}
  if(count_if(dist[x].begin(),dist[x].end(),[](int z){return z<0;}) || *max_element(dist[x].begin(),dist[x].end())!=4)throw runtime_error("distance failure");
 }
 vector<Four>bases;
 array<int,5> pass{};
 for(int a=0;a<N;a++) for(int b=a+1;b<N;b++) for(int c=b+1;c<N;c++) for(int d=c+1;d<N;d++){
  Four S{a,b,c,d};
  bool ok=true;
  for(int u=0;u<N&&ok;u++) for(int v=u+1;v<N;v++){
   if(dist[u][a]==dist[v][a]&&dist[u][b]==dist[v][b]&&dist[u][c]==dist[v][c]&&dist[u][d]==dist[v][d]){ok=false;break;}
  }
  if(ok)bases.push_back(S);
 }
 // There are no resolving 3-sets, since every resolving subset of size <=3
 // would extend to a 4-set in at least N-3 ways. Count explicitly as a check.
 int small=0;
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++){
  bool ok=true;
  for(int u=0;u<N&&ok;u++)for(int v=u+1;v<N;v++)
   if(dist[u][a]==dist[v][a]&&dist[u][b]==dist[v][b]&&dist[u][c]==dist[v][c]){ok=false;break;}
  small+=ok;
 }
 if(small!=0)throw runtime_error("resolving triple");
 unordered_map<uint32_t,int>index;index.reserve(bases.size()*2);
 auto mask=[](Four s){return (uint32_t(1)<<s[0])|(uint32_t(1)<<s[1])|(uint32_t(1)<<s[2])|(uint32_t(1)<<s[3]);};
 for(size_t i=0;i<bases.size();i++)index[mask(bases[i])]=int(i);
 vector<vector<int>> adj(bases.size());
 for(int i=0;i<(int)bases.size();i++){
  uint32_t m=mask(bases[i]);
  for(int del:bases[i]) for(int add=0;add<N;add++)if(!(m&(uint32_t(1)<<add))){
   uint32_t m2=(m^(uint32_t(1)<<del))|(uint32_t(1)<<add);
   auto it=index.find(m2);if(it!=index.end())adj[i].push_back(it->second);
  }
  sort(adj[i].begin(),adj[i].end());
  if(unique(adj[i].begin(),adj[i].end())!=adj[i].end())throw runtime_error("duplicate neighbors");
 }
 long long oriented=0;map<int,int>degreeHist;
 for(auto& nbr:adj){oriented+=nbr.size();degreeHist[(int)nbr.size()]++;}
 vector<int>dists(bases.size()),queue_(bases.size());
 long long geodesic=0, detours=0;map<int,long long>distanceHist,detourHist;
 map<int,int>eccHist;
 // Full pairwise BFS, with no symmetry assumptions.
 for(int root=0;root<(int)bases.size();root++){
  fill(dists.begin(),dists.end(),-1);
  int head=0,tail=0;queue_[tail++]=root;dists[root]=0;
  while(head<tail){int u=queue_[head++];for(int v:adj[u])if(dists[v]<0){dists[v]=dists[u]+1;queue_[tail++]=v;}}
  if(tail!=(int)bases.size())throw runtime_error("disconnected");
  eccHist[*max_element(dists.begin(),dists.end())]++;
  for(int j=root+1;j<(int)bases.size();j++){
   int common=__builtin_popcount(mask(bases[root])&mask(bases[j]));
   int johnson=4-common, delta=dists[j]-johnson;
   if(delta==0)geodesic++;
   else if(delta==1){detours++;detourHist[dists[j]]++;}
   else throw runtime_error("distance not Johnson or Johnson+1");
   distanceHist[dists[j]]++;
  }
 }
 cout<<"nodes="<<N<<" edges="<<edgeCount/2<<" diameter=4\n";
 cout<<"resolving_triples="<<small<<" resolving_4sets="<<bases.size()<<"\n";
 cout<<"exchange_edges="<<oriented/2<<" degree_hist=";
 for(auto [k,v]:degreeHist)cout<<k<<":"<<v<<",";
 cout<<"\necc_hist=";for(auto[k,v]:eccHist)cout<<k<<":"<<v<<",";
 cout<<"\ndistance_hist_unordered=";for(auto[k,v]:distanceHist)cout<<k<<":"<<v<<",";
 cout<<"\nJohnson_exact_pairs="<<geodesic<<" Johnson_plus_one_pairs="<<detours<<"\n";
 cout<<"detour_by_graph_distance=";for(auto[k,v]:detourHist)cout<<k<<":"<<v<<",";
 cout<<"\n";
 if(bases.size()!=7728||oriented/2!=155904||eccHist[4]!=1680||eccHist[5]!=6048||detours!=449820)throw runtime_error("unexpected certificate statistics");
}
