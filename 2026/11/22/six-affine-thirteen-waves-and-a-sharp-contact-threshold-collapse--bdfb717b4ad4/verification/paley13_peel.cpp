// Exhaustive finite functional-graph classification for a quadratic-residue circulant.
// Standalone C++17, no external libraries.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <tuple>
#include <vector>
using namespace std;
int main() {
 constexpr int n=13;
 constexpr array<int,6> residues={1,3,4,9,10,12};
 int powers[n+1]; powers[0]=1; for(int i=1;i<=n;i++) powers[i]=3*powers[i-1];
 const int total=powers[n];
 for(int threshold: {2,3}){
  vector<int> nxt(total);
  // Independent transition implementation: test each vertex's six modular offsets.
  for(int s=0;s<total;s++){
   array<unsigned char,n> color{};
   int x=s;for(int i=0;i<n;i++){color[i]=x%3; x/=3;}
   int z=0;
   for(int i=0;i<n;i++){
    int out;
    if(color[i])out=(color[i]==1?2:0);
    else {int k=0;for(int offset:residues)k+=color[(i+offset)%n]==1;out=(k>=threshold?1:0);}
    z+=out*powers[i];
   }
   nxt[s]=z;
  }
  vector<int> incoming(total,0);
  for(int x:nxt)incoming[x]++;
  queue<int> zero;
  for(int i=0;i<total;i++)if(!incoming[i])zero.push(i);
  vector<int> removed;removed.reserve(total);
  while(!zero.empty()){
   int x=zero.front();zero.pop();removed.push_back(x);int y=nxt[x];if(--incoming[y]==0)zero.push(y);
  }
  vector<int> label(total,-1), depth(total,0), plen(total,0), basins, basin_period;
  map<int,int> per_cycles;
  for(int i=0;i<total;i++) if(incoming[i] && label[i]<0){
   int id=basins.size(), x=i,len=0;
   do {label[x]=id;len++;x=nxt[x];}while(x!=i);
   basins.push_back(len);basin_period.push_back(len);per_cycles[len]++;
   x=i;do {plen[x]=len;x=nxt[x];}while(x!=i);
  }
  for(auto it=removed.rbegin();it!=removed.rend();it++){
   int x=*it, y=nxt[x];label[x]=label[y];depth[x]=depth[y]+1;plen[x]=plen[y];basins[label[x]]++;
  }
  map<pair<int,int>,long long> histogram;map<int,map<int,int>> basin_sizes;
  int max_depth=0,witness=-1;
  for(int i=0;i<total;i++){
   histogram[{depth[i],plen[i]}]++;
   if(depth[i]>max_depth){max_depth=depth[i];witness=i;}
  }
  for(int id=0;id<(int)basins.size();id++){
   basin_sizes[basin_period[id]][basins[id]]++;
  }
  cout<<"threshold "<<threshold<<" total "<<total<<" max_depth "<<max_depth<<" witness "<<witness<<"\n";
  cout<<"cycles";for(auto [p,c]:per_cycles)cout<<" "<<p<<":"<<c;cout<<"\n";
  cout<<"histogram";for(auto [dp,c]:histogram)cout<<" "<<dp.first<<","<<dp.second<<":"<<c;cout<<"\n";
  for(auto [p,h]:basin_sizes){cout<<"basins "<<p;for(auto [s,c]:h)cout<<" "<<s<<":"<<c;cout<<"\n";}
 }
}
