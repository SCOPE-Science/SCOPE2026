// Finite-certificate independent verifier for acyclic four-edge-colouring sectors.
// Build the Fano incidences as seven cyclic triples. Enumerate proper colourings
// by assigning permutations of the four colours at each point, and test all
// six bichromatic subgraphs separately at the leaves.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
constexpr int K=4;
array<array<int,3>,7> perPoint{};
array<array<int,3>,7> linePoints{};
int occupancy[7]={};
int cell[7][7];
vector<uint64_t> accepted;
long long proper_count=0;
int eu[21],ev[21];
uint64_t encode(){uint64_t x=0;int i=0;for(int p=0;p<7;p++)for(int j=0;j<3;j++)x|=(uint64_t)cell[p][perPoint[p][j]]<<(2*i++);return x;}
int get(uint64_t z,int e){return (z>>(2*e))&3;}
uint64_t put(uint64_t z,int e,int c){return (z&~(3ULL<<(2*e)))|((uint64_t)c<<(2*e));}
uint64_t normalize(uint64_t z){
 int rel[4]={-1,-1,-1,-1};for(int j=0;j<3;j++)rel[get(z,j)]=j;
 for(int c=0;c<4;c++)if(rel[c]==-1)rel[c]=3;
 uint64_t t=0;for(int e=0;e<21;e++)t=put(t,e,rel[get(z,e)]);return t;
}
bool forest_pair(uint64_t z,int ca,int cb){
 int parent[14];iota(parent,parent+14,0);
 auto root=[&](int x){while(parent[x]!=x){parent[x]=parent[parent[x]];x=parent[x];}return x;};
 for(int e=0;e<21;e++){
  int c=get(z,e);if(c!=ca&&c!=cb)continue;
  int x=root(eu[e]),y=root(ev[e]);if(x==y)return false;parent[x]=y;
 }
 return true;
}
bool admissible(uint64_t z){
 int forbidden[14]={};
 for(int e=0;e<21;e++){
  int col=get(z,e),bit=1<<col;
  if((forbidden[eu[e]]&bit)||(forbidden[ev[e]]&bit))return false;
  forbidden[eu[e]]|=bit;forbidden[ev[e]]|=bit;
 }
 for(int a=0;a<4;a++)for(int b=a+1;b<4;b++)if(!forest_pair(z,a,b))return false;
 return true;
}
void enumeration(int point){
 if(point==7){
  proper_count++;uint64_t code=encode();if(admissible(code))accepted.push_back(code);return;
 }
 int colors[4]={0,1,2,3};
 do{
  // Assign first three colours to the lines through this point.
  bool ok=true;
  for(int j=0;j<3;j++)if(occupancy[perPoint[point][j]]&(1<<colors[j]))ok=false;
  if(!ok)continue;
  for(int j=0;j<3;j++){
   int l=perPoint[point][j];cell[point][l]=colors[j];occupancy[l]|=1<<colors[j];
  }
  enumeration(point+1);
  for(int j=0;j<3;j++)occupancy[perPoint[point][j]]^=1<<colors[j];
 }while(next_permutation(colors,colors+4));
}
int main(){
 for(int i=0;i<7;i++)for(int j=0;j<7;j++)cell[i][j]=-1;
 int t=0;
 for(int l=0;l<7;l++){
  linePoints[l]={l,(l+1)%7,(l+3)%7};
 }
 for(int p=0;p<7;p++)perPoint[p]={-1,-1,-1};
 int sizes[7]={};
 for(int l=0;l<7;l++)for(int p:linePoints[l])perPoint[p][sizes[p]++]=l;
 for(int p=0;p<7;p++){
  sort(perPoint[p].begin(),perPoint[p].end());
  for(int j=0;j<3;j++){int l=perPoint[p][j];eu[t]=p;ev[t]=7+l;t++;}
 }
 // Canonical orientation of names on first point: 0,1,2, with 3 missing.
 for(int j=0;j<3;j++){int l=perPoint[0][j];cell[0][l]=j;occupancy[l]|=1<<j;}
 enumeration(1);
 cout<<"canonical="<<accepted.size()<<" named="<<accepted.size()*24<<" proper_canonical="<<proper_count<<"\n";
 unordered_map<uint64_t,int> index;index.reserve(accepted.size()*2);
 for(int i=0;i<(int)accepted.size();i++){
  if(index.count(accepted[i])){cerr<<"Duplicate canonical state\n";return 1;}
  index[accepted[i]]=i;
 }
 vector<vector<int>> edges(accepted.size());
 long long directed=0;int loops=0;
 for(int i=0;i<(int)accepted.size();i++){
  uint64_t z=accepted[i];
  for(int e=0;e<21;e++)for(int nc=0;nc<4;nc++)if(nc!=get(z,e)){
   uint64_t w=put(z,e,nc);if(!admissible(w))continue;
   w=normalize(w);
   auto it=index.find(w);if(it==index.end()){cerr<<"Closedness fail\n";return 2;}
   edges[i].push_back(it->second);directed++;
   if(it->second==i)loops++;
  }
  sort(edges[i].begin(),edges[i].end());edges[i].erase(unique(edges[i].begin(),edges[i].end()),edges[i].end());
 }
 vector<bool> visited(accepted.size());unordered_map<int,int> compFreq,degreeFreq;
 for(const auto &x:edges)degreeFreq[x.size()]++;
 for(int i=0;i<(int)accepted.size();i++)if(!visited[i]){
  vector<int> q(1,i);visited[i]=true;
  for(size_t j=0;j<q.size();j++)for(int v:edges[q[j]])if(!visited[v]){visited[v]=true;q.push_back(v);}
  compFreq[q.size()]++;
 }
 cout<<"arcs="<<directed<<" loops="<<loops<<" edges="<<directed/2<<"\n";
 vector<pair<int,int>> counts(compFreq.begin(),compFreq.end());sort(counts.begin(),counts.end());
 cout<<"components:";for(auto [sz,n]:counts)cout<<" "<<sz<<"x"<<n;cout<<"\n";
 cout<<"degrees:";vector<pair<int,int>> ds(degreeFreq.begin(),degreeFreq.end());sort(ds.begin(),ds.end());for(auto [d,n]:ds)cout<<" "<<d<<":"<<n;cout<<"\n";
 if(accepted.size()!=119784||loops||directed!=599760||compFreq[1]!=392||compFreq[14]!=112||compFreq[42]!=24||compFreq[40040]!=1||compFreq[76776]!=1){cerr<<"CERTIFICATE MISMATCH\n";return 3;}
 cout<<"PASS\n";
}
