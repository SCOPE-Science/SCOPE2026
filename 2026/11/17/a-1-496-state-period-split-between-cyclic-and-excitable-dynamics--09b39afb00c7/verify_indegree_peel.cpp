// Exact paired cyclic-contact and Greenberg-Hastings dynamics on the Frucht graph.
// Standard C++17, no external libraries. Uses explicit edges and indegree pruning.
#include <array>
#include <cassert>
#include <cstdio>
#include <deque>
#include <map>
#include <utility>
#include <vector>
using namespace std;
constexpr int V=12, N=531441;
const pair<int,int> edges[18]={
{0,1},{0,6},{0,7},{1,2},{1,7},{2,3},
{2,8},{3,4},{3,9},{4,5},{4,9},{5,6},
{5,10},{6,10},{7,11},{8,9},{8,11},{10,11}};
array<array<int,3>,V> nb;
array<int,13> powers;
void setup(){
 array<int,V> deg{};
 for(auto [a,b]:edges){assert(a!=b); assert(deg[a]<3 && deg[b]<3);nb[a][deg[a]++]=b;nb[b][deg[b]++]=a;}
 for(int i=0;i<V;i++)assert(deg[i]==3);
 // Independently confirm that the standard LCF labeling and the edge-list
 // labeling describe the same graph, using this explicit vertex permutation.
 const int lcf[V]={-5,-2,-4,2,5,-2,2,5,-2,-5,4,2};
 const int perm[V]={4,3,2,1,7,0,6,5,10,11,8,9};
 bool edge_matrix[V][V]={};
 for(auto [a,b]:edges)edge_matrix[a][b]=edge_matrix[b][a]=true;
 bool lcf_matrix[V][V]={};
 for(int i=0;i<V;i++){
  int j=(i+1)%V, k=(i+lcf[i]+V*10)%V;
  lcf_matrix[perm[i]][perm[j]]=lcf_matrix[perm[j]][perm[i]]=true;
  lcf_matrix[perm[i]][perm[k]]=lcf_matrix[perm[k]][perm[i]]=true;
 }
 for(int i=0;i<V;i++)for(int j=0;j<V;j++)assert(edge_matrix[i][j]==lcf_matrix[i][j]);
 powers[0]=1;for(int i=1;i<=V;i++)powers[i]=3*powers[i-1];
}
struct result {
 vector<int> period, depth, next;
 map<int,int> orbit_counts;
 int maxdepth=0, maxpop=0;
};
result evaluate(bool ghm){
 result r;r.period.assign(N,0);r.depth.assign(N,0);r.next.resize(N);
 for(int state=0;state<N;state++){
  int digit[V];int copy=state;
  for(int i=0;i<V;i++){digit[i]=copy%3;copy/=3;}
  int y=0;
  for(int i=0;i<V;i++){
    int here=digit[i], out=here;
    if(ghm){
      if(here==1) out=2;
      else if(here==2)out=0;
      else if(digit[nb[i][0]]==1||digit[nb[i][1]]==1||digit[nb[i][2]]==1)out=1;
    }else{
      const int target=(here+1)%3;
      if(digit[nb[i][0]]==target||digit[nb[i][1]]==target||digit[nb[i][2]]==target)out=target;
    }
    y+=out*powers[i];
  }
  assert(y>=0&&y<N);r.next[state]=y;
 }
 vector<int> indegree(N,0);
 for(int k:r.next)indegree[k]++;
 deque<int> peel;for(int v=0;v<N;v++)if(indegree[v]==0)peel.push_back(v);
 vector<int> deleted;deleted.reserve(N);
 while(!peel.empty()){
  int v=peel.front();peel.pop_front();deleted.push_back(v);
  if(--indegree[r.next[v]]==0)peel.push_back(r.next[v]);
 }
 int cyclepop=0;
 for(int s=0;s<N;s++){
  if(indegree[s]==0 || r.period[s]!=0)continue;
  vector<int> cycle;int t=s;
  do { assert(indegree[t]!=0 && r.period[t]==0);cycle.push_back(t);r.period[t]=-1;t=r.next[t]; }while(t!=s);
  int p=(int)cycle.size();r.orbit_counts[p]++;
  for(int v:cycle)r.period[v]=p;
  cyclepop+=p;
 }
 assert(cyclepop+deleted.size()==N);
 for(auto it=deleted.rbegin();it!=deleted.rend();++it){
   int v=*it, t=r.next[v];assert(r.period[t]>0);
   r.period[v]=r.period[t];r.depth[v]=r.depth[t]+1;
   if(r.depth[v]>r.maxdepth){r.maxdepth=r.depth[v];r.maxpop=1;}
   else if(r.depth[v]==r.maxdepth)r.maxpop++;
 }
 return r;
}
int main(){setup();auto c=evaluate(false),g=evaluate(true);
 map<pair<int,int>,int> joint;
 for(int v=0;v<N;v++) {assert(c.period[v]>0&&g.period[v]>0);joint[{c.period[v],g.period[v]}]++;}
 const map<pair<int,int>,int> expected={
 {{1,1},52563},{{3,3},282990},{{4,4},62952},{{5,5},90432},
 {{6,6},24636},{{7,7},12840},{{8,8},3532},{{8,4},1496}};
 assert(joint==expected);
 assert(c.maxdepth==19 && c.maxpop==9 && g.maxdepth==21 && g.maxpop==3);
 const map<int,int> expected_c={{1,3},{3,1912},{4,66},{5,60},{6,20},{7,84},{8,36}};
 const map<int,int> expected_g={{1,1},{3,1912},{4,22},{5,10},{6,2},{7,28},{8,4}};
 assert(c.orbit_counts==expected_c&&g.orbit_counts==expected_g);
 printf("joint_period_matrix:");for(auto [p,k]:joint)printf(" (%d,%d):%d",p.first,p.second,k);puts("");
 printf("cca_orbits:");for(auto [p,k]:c.orbit_counts)printf(" %d:%d",p,k);puts("");
 printf("ghm_orbits:");for(auto [p,k]:g.orbit_counts)printf(" %d:%d",p,k);puts("");
 int first=-1, exceptional_periodic_cca=0, exceptional_periodic_ghm=0;
 for(int v=0;v<N;v++)if(c.period[v]==8&&g.period[v]==4){
  if(first<0)first=v;
  exceptional_periodic_cca+=(c.depth[v]==0);
  exceptional_periodic_ghm+=(g.depth[v]==0);
 }
 assert(first>=0);
 printf("first_mismatch_state=%d CCA=(entry:%d,period:%d) GHM=(entry:%d,period:%d)\n",
 first,c.depth[first],c.period[first],g.depth[first],g.period[first]);
 printf("exceptional_immediate_CCA=%d exceptional_immediate_GHM=%d\n",
 exceptional_periodic_cca,exceptional_periodic_ghm);
 printf("max_entries: CCA=%d states=%d; GHM=%d states=%d\n",c.maxdepth,c.maxpop,g.maxdepth,g.maxpop);
 puts("DUAL_FRUCHT_PEEL_VERIFY_OK");
}
