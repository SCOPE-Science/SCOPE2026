// Exhaustive exact edge-domination census of the Fano incidence graph.
// Build: c++ -O2 -std=c++17 verify_binary.cpp -o verify_binary
// Run: ./verify_binary
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
  vector<pair<int,int>> e;
  for(int a=1;a<8;a++) for(int x=1;x<8;x++)
    if(__builtin_parity((unsigned)(a & x))==0) e.push_back({a,x});
  assert(e.size()==21);
  constexpr int m=21, lim=1<<m;
  const unsigned full=(1u<<m)-1;
  array<unsigned,m> B{};
  for(int i=0;i<m;i++) for(int j=0;j<m;j++)
    if(e[i].first==e[j].first || e[i].second==e[j].second) B[i] |= 1u<<j;
  vector<unsigned> dominated(lim,0);
  array<uint64_t,22> all{}, minimal{}, maximal_matching{};
  vector<unsigned> opt;
  for(int S=1;S<lim;S++) {
    unsigned b=(unsigned)S & -(unsigned)S;
    int i=__builtin_ctz(b);
    dominated[S]=dominated[S^(int)b] | B[i];
    if(dominated[S]!=full) continue;
    int k=__builtin_popcount((unsigned)S);
    all[k]++;
    bool essential=true, is_matching=true;
    for(int a=0;a<m;a++) if((S>>a)&1) {
      if(dominated[S^(1<<a)]==full) essential=false;
      for(int c=a+1;c<m;c++) if((S>>c)&1)
        if(e[a].first==e[c].first || e[a].second==e[c].second)
          is_matching=false;
    }
    if(essential) minimal[k]++;
    if(is_matching) maximal_matching[k]++;
    if(k==5) opt.push_back((unsigned)S);
  }
  assert(opt.size()==42);
  assert(minimal[5]==42 && minimal[6]==1246 && minimal[7]==24);
  for(int k=0;k<=m;k++) if(k!=5 && k!=6 && k!=7) assert(minimal[k]==0);
  assert(maximal_matching[5]==42 && maximal_matching[6]==168 && maximal_matching[7]==24);
  for(int k=0;k<=m;k++) if(k!=5 && k!=6 && k!=7) assert(maximal_matching[k]==0);
  const array<uint64_t,22> expected_all={
    0,0,0,0,0,42,1918,15186,58044,137522,226422,276192,
    259518,192318,113802,53928,20328,5985,1330,210,21,1
  };
  assert(all==expected_all);
  array<int,6> diff{};
  vector<vector<int>> A(42);
  for(int i=0;i<42;i++) for(int j=i+1;j<42;j++) {
    int r=__builtin_popcount(opt[i]^opt[j])/2;
    assert(r>=2 && r<=5);
    diff[r]++;
    if(r==2) { A[i].push_back(j); A[j].push_back(i); }
  }
  assert(diff[2]==84 && diff[3]==84 && diff[4]==525 && diff[5]==168);
  for(int i=0;i<42;i++) {
    assert(A[i].size()==4);
    array<int,6> profile{};
    vector<int>d(42,-1); queue<int>Q;d[i]=0;Q.push(i);
    while(!Q.empty()) {
      int u=Q.front();Q.pop();
      for(int v:A[u]) if(d[v]<0){d[v]=d[u]+1;Q.push(v);}
    }
    for(int x:d){assert(x>=0&&x<=5);profile[x]++;}
    assert((profile==array<int,6>{1,4,8,16,12,1}));
  }
  cout<<"ALL_EDGE_DOMINATION_COUNTS";
  for(int k=0;k<=m;k++)if(all[k])cout<<" ("<<k<<","<<all[k]<<")";
  cout<<"\nINCLUSION_MINIMAL_COUNTS (5,42) (6,1246) (7,24)";
  cout<<"\nMAXIMAL_MATCHING_COUNTS (5,42) (6,168) (7,24)";
  cout<<"\nOPTIMUM_EXCHANGE 42 vertices 84 edges degree 4 diameter 5";
  cout<<"\nDISTANCE_PROFILE (1,4,8,16,12,1)\nVERIFY_BINARY_OK\n";
}
