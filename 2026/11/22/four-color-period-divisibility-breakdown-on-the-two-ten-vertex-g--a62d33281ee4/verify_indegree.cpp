// Separate finite-state classifier for four-color graph dynamics.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
using namespace std;
constexpr int N=10, SIZE=1<<20;
using Graph=array<vector<int>,N>;
static Graph graph(int type){
 Graph g{};
 if(type==1){ // Cartesian C5 x K2, (rail,position) coordinate encoding
  for(int z=0;z<2;z++)for(int i=0;i<5;i++){
   int v=5*z+i;
   g[v]={5*z+(i+4)%5,5*z+(i+1)%5,5*(1-z)+i};
  }
 }else{ // Petersen = disjointness graph on the ten two-element subsets of five symbols
  array<pair<int,int>,N> subset{};int j=0;
  for(int a=0;a<5;a++)for(int b=a+1;b<5;b++)subset[j++]={a,b};
  for(int x=0;x<N;x++)for(int y=0;y<N;y++)if(x!=y){
   auto [a,b]=subset[x];auto [c,d]=subset[y];
   if(a!=c&&a!=d&&b!=c&&b!=d)g[x].push_back(y);
  }
 }
 for(int i=0;i<N;i++){
  sort(g[i].begin(),g[i].end());
  if(g[i].size()!=3){cerr<<"noncubic";exit(2);}
  for(int j:g[i])if(find(g[j].begin(),g[j].end(),i)==g[j].end()){cerr<<"not undirected";exit(2);}
 }
 return g;
}
static int next_state(int s,const Graph&g,int model){
 array<int,N> x{};
 int v=s;for(int i=0;i<N;i++){x[i]=v%4;v/=4;}
 int out=0,mult=1;
 for(int i=0;i<N;i++){
  int col=x[i];
  int y=col;
  if(model==1){
   if(col>0)y=(col+1)%4;
   else{for(int w:g[i]) if(x[w]==1){y=1;break;}}
  }else{
   int wanted=(col+1)%4;
   for(int w:g[i])if(x[w]==wanted){y=wanted;break;}
  }
  out+=y*mult;mult*=4;
 }
 return out;
}
struct Cl {vector<uint8_t> period,entry;map<int,long long> pcount;int maxentry=0;};
static Cl classify(const Graph&g,int model){
 vector<int> nxt(SIZE);vector<int> indeg(SIZE,0);
 for(int s=0;s<SIZE;s++){int t=next_state(s,g,model);nxt[s]=t;indeg[t]++;}
 vector<int> removed;removed.reserve(SIZE);
 vector<int> queue;queue.reserve(SIZE);
 for(int s=0;s<SIZE;s++)if(indeg[s]==0)queue.push_back(s);
 for(size_t i=0;i<queue.size();i++){
  int s=queue[i];removed.push_back(s);
  int t=nxt[s];if(--indeg[t]==0)queue.push_back(t);
 }
 Cl res;res.period.assign(SIZE,0);res.entry.assign(SIZE,0);
 for(int s=0;s<SIZE;s++)if(indeg[s]>0&&res.period[s]==0){
  int t=s,len=0;
  do{++len;t=nxt[t];}while(t!=s);
  t=s;do{res.period[t]=len;t=nxt[t];}while(t!=s);
 }
 for(auto it=removed.rbegin();it!=removed.rend();it++){
  int v=*it,to=nxt[v];res.period[v]=res.period[to];res.entry[v]=res.entry[to]+1;
 }
 for(int s=0;s<SIZE;s++){
  if(res.period[s]==0){cerr<<"unclassified";exit(3);}
  res.maxentry=max(res.maxentry,(int)res.entry[s]);
  res.pcount[res.period[s]]++;
 }
 return res;
}
int main(){
 for(int type:{1,2}){
  auto G=graph(type);
  Cl c=classify(G,0),h=classify(G,1);
  map<pair<int,int>,long long> cells;long long bad=0;
  map<pair<int,int>,int> witnesses;
  for(int s=0;s<SIZE;s++){
   auto key=make_pair((int)c.period[s],(int)h.period[s]);
   cells[key]++;if(key.first!=key.second)bad++;
   if(!witnesses.count(key))witnesses[key]=s;
  }
  cout<<"GP(5,"<<type<<") "<<SIZE<<" states, CCA max entry "<<c.maxentry<<", GHM max entry "<<h.maxentry<<"\n";
  cout<<"joint";
  for(auto [key,n]:cells)cout<<" ("<<key.first<<","<<key.second<<")="<<n;
  cout<<"\nmismatch="<<bad<<"\n";
  cout<<"witnesses";for(auto [key,s]:witnesses)cout<<" ("<<key.first<<","<<key.second<<")="<<s;
  cout<<"\n";
 }
 cout<<"INDEPENDENT_INDEGREE_OK\n";
}
