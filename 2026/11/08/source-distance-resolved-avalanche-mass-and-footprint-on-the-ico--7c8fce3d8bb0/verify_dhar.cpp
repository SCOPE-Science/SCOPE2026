// Independent graph realization and Dhar burning-addition replay.
#include <array>
#include <iostream>
#include <map>
#include <utility>
#include <cstdint>
using namespace std;
array<array<int,5>,12> adj;
array<int,12> degree{};
array<int,12> h{};
array<map<pair<int,int>,uint64_t>,3> hist;
uint64_t recurrence=0;
void edge(int a,int b){adj[a][degree[a]++]=b;adj[b][degree[b]++]=a;}
// Use a distinct icosahedral realization: two staggered pentagonal rings plus poles.
void make_graph(){
 for(int i=0;i<5;i++){
  int a=1+i,b=6+i;
  edge(0,a);edge(11,b);
  edge(a,1+(i+1)%5);edge(b,6+(i+1)%5);
  edge(a,b);edge(a,6+(i+4)%5);
 }
 for(int v=0;v<12;v++)if(degree[v]!=5)throw 1;
}
struct Avalanche {int t=0;int mask=0;int topple[12]{};};
Avalanche relax(array<int,12> &x){
 Avalanche a;
 for(;;){
  int v=11;
  while(v>0 && x[v]<5)--v;
  if(v==0)break;
  if(++a.t>200)throw 2;
  a.topple[v]++;
  a.mask|=1<<(v-1);
  x[v]-=5;
  for(int w:adj[v])if(w)++x[w];
 }
 return a;
}
bool is_rec(){
 auto b=h;
 for(int k=0;k<5;k++)++b[adj[0][k]];
 Avalanche t=relax(b);
 for(int i=1;i<12;i++)if(t.topple[i]!=1 || b[i]!=h[i])return false;
 return true;
}
int main(){
 make_graph();
 constexpr uint64_t n=48828125ULL;
 constexpr int src[3]={1,6,11};
 for(uint64_t k=0;k<n;k++){
  if(is_rec()){
   ++recurrence;
   for(int j=0;j<3;j++){
    auto x=h;++x[src[j]];
    Avalanche r=relax(x);
    hist[j][{r.t,__builtin_popcount((unsigned)r.mask)}]++;
   }
  }
  for(int v=1;v<12;v++)if(++h[v]<5)break;else h[v]=0;
 }
 cout<<"recurrent "<<recurrence<<"\n";
 for(int j=0;j<3;j++){
  cout<<"distance "<<j+1<<" terms "<<hist[j].size()<<"\n";
  for(auto [ts,c]:hist[j])cout<<ts.first<<","<<ts.second<<":"<<c<<" ";
  cout<<"\n";
 }
}
