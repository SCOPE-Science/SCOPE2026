// Independent exhaustive verification: all 2^18 states for each 9_3 Levi graph.
// C++17; g++ -O2 -std=c++17 check_full_states.cpp -o check && ./check
#include <array>
#include <vector>
#include <map>
#include <queue>
#include <iostream>
#include <cassert>
#include <algorithm>
#include <numeric>
using namespace std;
using Tri=array<int,3>;
using Blocks=array<Tri,9>;
static const array<Blocks,3> reps={{
 Blocks{{Tri{0,1,2},Tri{0,3,4},Tri{0,5,6},Tri{1,3,7},Tri{1,6,8},Tri{2,4,6},Tri{2,7,8},Tri{3,5,8},Tri{4,5,7}}},
 Blocks{{Tri{0,1,2},Tri{0,3,4},Tri{0,5,6},Tri{1,4,8},Tri{1,6,7},Tri{2,3,7},Tri{2,6,8},Tri{3,5,8},Tri{4,5,7}}},
 Blocks{{Tri{0,1,2},Tri{0,3,4},Tri{0,5,6},Tri{1,3,8},Tri{1,5,7},Tri{2,4,7},Tri{2,6,8},Tri{3,6,7},Tri{4,5,8}}}
}};
int main(){
 constexpr int n=18,N=1<<18;
 const array<int,3> expectedFixed={98,96,92};
 const array<int,3> expectedCycles={4753,4560,4186};
 const array<int,3> expectedDepth={4,4,3};
 for(int ci=0;ci<3;ci++){
  array<unsigned,18> neigh{};
  for(int j=0;j<9;j++)for(int v:reps[ci][j]){neigh[v]|=1u<<(9+j);neigh[9+j]|=1u<<v;}
  for(auto m:neigh)assert(__builtin_popcount(m)==3);
  vector<int> dest(N),indeg(N,0),first(N,-1),orbit(N,-1),decomp;
  for(int s=0;s<N;s++){
   int t=0;
   for(int v=0;v<n;v++)if(__builtin_popcount((unsigned)s&neigh[v])>=2)t|=1<<v;
   dest[s]=t;indeg[t]++;
  }
  queue<int> q;
  for(int s=0;s<N;s++)if(indeg[s]==0)q.push(s);
  while(!q.empty()){
   int s=q.front();q.pop();decomp.push_back(s);
   if(--indeg[dest[s]]==0)q.push(dest[s]);
  }
  vector<int> periods;
  for(int s=0;s<N;s++)if(indeg[s]>0&&orbit[s]<0){
   int t=s,id=(int)periods.size(),p=0;
   do{assert(orbit[t]<0);orbit[t]=id;first[t]=0;t=dest[t];p++;}while(t!=s);
   assert(p==1||p==2);periods.push_back(p);
  }
  for(auto it=decomp.rbegin();it!=decomp.rend();++it){
   int s=*it;first[s]=first[dest[s]]+1;orbit[s]=orbit[dest[s]];
  }
  vector<int> basin(periods.size(),0);
  map<int,int> depths;
  for(int s=0;s<N;s++){
   assert(0<=orbit[s] && orbit[s]<(int)periods.size());
   assert(first[s]>=0);basin[orbit[s]]++;depths[first[s]]++;
  }
  int fixed=0,two=0;
  map<pair<int,int>,int> spectrum;
  for(size_t j=0;j<periods.size();j++){
   spectrum[{periods[j],basin[j]}]++;
   if(periods[j]==1)fixed++;else two++;
  }
  assert(fixed==expectedFixed[ci]);assert(two==expectedCycles[ci]);
  assert(depths.rbegin()->first==expectedDepth[ci]);
  assert(accumulate(basin.begin(),basin.end(),0)==N);
  cout<<"class="<<ci<<" fixed="<<fixed<<" two="<<two<<" maxdepth="<<depths.rbegin()->first<<"\n";
  cout<<"entry";for(auto [d,k]:depths)cout<<" "<<d<<":"<<k;cout<<"\n";
  cout<<"basin-spectrum";for(auto [z,k]:spectrum)cout<<" ("<<z.first<<","<<z.second<<")="<<k;cout<<"\n";
 }
 cout<<"PASS all 786432 states\n";
}
