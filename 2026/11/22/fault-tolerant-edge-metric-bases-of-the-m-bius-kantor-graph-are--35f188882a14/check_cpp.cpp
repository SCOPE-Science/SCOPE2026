// Independent, dependency-free C++17 exhaustive verifier for GP(8,3).
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
using P=pair<int,int>;
int main(){
 constexpr int N=16, INF=1000;
 vector<P> edges;
 auto add=[&](int a,int b){if(a>b)swap(a,b);edges.push_back({a,b});};
 for(int i=0;i<8;i++){
  add(i,(i+1)%8);add(i,8+i);add(8+i,8+(i+3)%8);
 }
 sort(edges.begin(),edges.end());assert(edges.size()==24);
 array<vector<int>,N> adj;
 for(auto [a,b]:edges){adj[a].push_back(b);adj[b].push_back(a);}
 array<array<int,N>,N> dist;
 for(int a=0;a<N;a++){
  dist[a].fill(INF);dist[a][a]=0;queue<int> q;q.push(a);
  while(!q.empty()){
   int x=q.front();q.pop();for(int y:adj[x]) if(dist[a][y]==INF){dist[a][y]=dist[a][x]+1;q.push(y);}
  }
 }
 array<array<int,24>,N> signature;
 for(int v=0;v<N;v++) for(int e=0;e<24;e++) signature[v][e]=min(dist[v][edges[e].first],dist[v][edges[e].second]);
 vector<unsigned> witness;
 for(int a=0;a<24;a++)for(int b=a+1;b<24;b++){
  unsigned bits=0;for(int v=0;v<N;v++)if(signature[v][a]!=signature[v][b])bits|=(1u<<v);
  witness.push_back(bits);
 }
 assert(witness.size()==276);
 vector<unsigned> ft5;
 int count4=0,regular4=0;
 for(unsigned S=0;S<(1u<<N);S++){
  int n=__builtin_popcount(S);if(n!=4 && n!=5)continue;
  int minw=N;
  for(unsigned w:witness)minw=min(minw,__builtin_popcount(w&S));
  if(n==4){if(minw>=1)regular4++;if(minw>=2)count4++;}
  else if(minw>=2)ft5.push_back(S);
 }
 assert(regular4==368 && count4==0 && ft5.size()==16);
 vector<unsigned> spheres;
 for(int a=0;a<N;a++){
  unsigned S=0;for(int v=0;v<N;v++)if(dist[a][v]==3)S|=1u<<v;
  assert(__builtin_popcount(S)==5);spheres.push_back(S);
 }
 sort(ft5.begin(),ft5.end());sort(spheres.begin(),spheres.end());
 assert(ft5==spheres);
 array<int,6> ints{};
 array<int,6> edgecounts{};
 for(int a=0;a<16;a++)for(int b=a+1;b<16;b++){
  int overlap=__builtin_popcount(ft5[a]&ft5[b]);ints[overlap]++;
  for(int k=1;k<=5;k++)if(5-overlap<=k)edgecounts[k]++;
 }
 assert(ints[0]==64&&ints[2]==8&&ints[3]==48);
 assert(edgecounts[1]==0&&edgecounts[2]==48&&edgecounts[3]==56&&edgecounts[4]==56&&edgecounts[5]==120);
 cout<<"C++ PASS: ordinary=368, FT4=0, FT5=16, sphere3 classification, intersections and exchange edge counts\n";
 return 0;
}
