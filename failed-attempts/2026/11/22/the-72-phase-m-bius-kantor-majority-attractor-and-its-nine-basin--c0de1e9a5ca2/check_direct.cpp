// Exhaustive finite-state census for strict majority on the Möbius–Kantor graph.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra check_direct.cpp -o check_direct
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
int main(){
 constexpr int N=16, M=1<<N;
 array<int,N> masks{};
 auto edge=[&](int i,int j){assert(i!=j); masks[i]|=1<<j; masks[j]|=1<<i;};
 for(int i=0;i<8;i++){
   edge(i,(i+1)%8);
   edge(i,i+8);
   edge(i+8,8+(i+3)%8);
 }
 for(auto m:masks) assert(__builtin_popcount((unsigned)m)==3);
 vector<int> f(M), indegree(M), root(M,-1), entry(M,-1), order;
 for(int x=0;x<M;x++){
   int y=0;
   for(int i=0;i<N;i++) if(__builtin_popcount((unsigned)(x&masks[i]))>=2) y|=1<<i;
   f[x]=y;
   indegree[y]++;
 }
 queue<int> Q;
 for(int x=0;x<M;x++) if(!indegree[x]) Q.push(x);
 while(!Q.empty()){
   int x=Q.front();Q.pop();order.push_back(x);
   if(--indegree[f[x]]==0) Q.push(f[x]);
 }
 vector<int> orbit_len;
 for(int x=0;x<M;x++) if(indegree[x]>0 && root[x]==-1){
   int oid=(int)orbit_len.size(),y=x,len=0;
   do {root[y]=oid;entry[y]=0;len++;y=f[y];} while(y!=x);
   assert(len==1 || len==2);
   orbit_len.push_back(len);
 }
 for(auto it=order.rbegin();it!=order.rend();++it){
   int x=*it;
   root[x]=root[f[x]];
   entry[x]=entry[f[x]]+1;
 }
 vector<int> basin(orbit_len.size());
 map<int,int> entry_count;
 for(int x=0;x<M;x++) {
   assert(root[x]>=0 && entry[x]>=0);
   basin[root[x]]++;
   entry_count[entry[x]]++;
   auto iterate=[&](int z,int t){for(int j=0;j<t;j++)z=f[z];return z;};
   assert(iterate(x,3)==iterate(x,5));
 }
 assert(entry_count==(map<int,int>{{0,5184},{1,15552},{2,22528},{3,22272}}));
 map<pair<int,int>,int> hist;
 for(size_t i=0;i<orbit_len.size();i++) hist[{orbit_len[i],basin[i]}]++;
 const map<pair<int,int>,int> target={
  {{1,1},22},{{1,4},48},{{1,4761},2},
  {{2,2},231},{{2,4},1056},{{2,8},1128},
  {{2,138},44},{{2,276},96},{{2,9522},1}};
 assert(hist==target);
 assert((int)orbit_len.size()==2628);
 assert((int)order.size()==M-5184);
 assert(*max_element(entry.begin(),entry.end())==3);
 cout << "DIRECT_CENSUS_OK\n";
 for(const auto& kv:hist)cout<<"period="<<kv.first.first<<" basin="<<kv.first.second<<" multiplicity="<<kv.second<<"\n";
 for(const auto& kv:entry_count)cout<<"entry="<<kv.first<<" states="<<kv.second<<"\n";
}
