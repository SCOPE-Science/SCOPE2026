// Exhaustive independent checker for all 36 incidence-edge subsets of size at most seven.
// The graph is the standard affine plane AG(2,3), with 9 points and 12 lines.
#include <array>
#include <vector>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <cstdint>
#include <queue>
using namespace std;
struct Edge {int p,l;};
vector<Edge> edges;
array<array<int,3>,12> lines;
vector<uint64_t> minima;
array<long long,8> totals{};
void visit(int start,int need,uint64_t mask){
 if(!need){
  unsigned cp=0,cl=0;
  for(int i=0;i<(int)edges.size();++i) if(mask>>i&1){cp|=1u<<edges[i].p;cl|=1u<<edges[i].l;}
  for(const auto &e:edges)if(!(cp>>e.p&1) && !(cl>>e.l&1)) return;
  int k=__builtin_popcountll(mask); ++totals[k];
  if(k==7) minima.push_back(mask);
  return;
 }
 for(int i=start;i+need<=36;i++)visit(i+1,need-1,mask|(1ULL<<i));
}
int main(){
 int z=0;
 for(int c=0;c<3;c++){lines[z++]={3*c,3*c+1,3*c+2};}
 for(int m=0;m<3;m++)for(int b=0;b<3;b++){
  array<int,3> tmp{};
  for(int x=0;x<3;x++)tmp[x]=3*x+(m*x+b)%3;
  lines[z++]=tmp;
 }
 assert(z==12);
 for(int p=0;p<9;p++)for(int l=0;l<12;l++)if(find(lines[l].begin(),lines[l].end(),p)!=lines[l].end())edges.push_back({p,l});
 assert(edges.size()==36);
 for(int k=1;k<=7;k++)visit(0,k,0);
 for(int k=1;k<=7;k++)cout<<"EDGE_DOMINATING_SIZE "<<k<<" "<<totals[k]<<"\n";
 assert(totals[7]==72);for(int k=1;k<7;k++) assert(totals[k]==0);
 // Full exchange graph of minima: adjacent iff exactly four edges are replaced.
 int n=minima.size();
 vector<vector<int>> adj(n);
 int maxshared=0,shared3=0;
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
  int common=__builtin_popcountll(minima[i]&minima[j]);
  maxshared=max(maxshared,common);
  if(common==3){shared3++;adj[i].push_back(j);adj[j].push_back(i);}
 }
 assert(maxshared==3);
 for(const auto &x:adj)assert(x.size()==8);
 int diameter=0;
 for(int i=0;i<n;i++){
  vector<int> d(n,-1);queue<int> q;q.push(i);d[i]=0;
  while(!q.empty()){int u=q.front();q.pop();for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;q.push(v);}}
  assert(*min_element(d.begin(),d.end())==0);
  diameter=max(diameter,*max_element(d.begin(),d.end()));
 }
 cout<<"OPTIMUM_INTERSECTION_MAX "<<maxshared<<"\n";
 cout<<"FOUR_EDGE_EXCHANGE_GRAPH "<<n<<" "<<shared3<<" 8 "<<diameter<<"\n";
 assert(shared3==288 && diameter==4);
 cout<<"CERTIFICATE_OK\n";
}
