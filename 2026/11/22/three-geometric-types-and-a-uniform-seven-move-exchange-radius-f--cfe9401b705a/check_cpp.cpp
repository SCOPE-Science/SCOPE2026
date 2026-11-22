// Exhaustive bitset verification for the generalized Petersen graph GP(8,3).
// Compile: c++ -std=c++17 -O2 -Wall -Wextra check_cpp.cpp -o check_cpp && ./check_cpp
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
static constexpr int N=16, TOTAL=1<<N;
int main(){
  array<vector<int>,N> adj{};
  auto edge=[&](int a,int b){adj[a].push_back(b);adj[b].push_back(a);};
  for(int i=0;i<8;i++){
    edge(i,(i+1)%8);edge(i,i+8);edge(i+8,8+(i+3)%8);
  }
  array<array<int,N>,N> d{};
  for(int s=0;s<N;s++){
    d[s].fill(99);d[s][s]=0;
    vector<int> q{s};
    for(size_t j=0;j<q.size();j++)for(int v:adj[q[j]])if(d[s][v]==99){d[s][v]=d[s][q[j]]+1;q.push_back(v);}
    assert(q.size()==N);
  }
  array<array<unsigned,N>,N> sep{};
  for(int a=0;a<N;a++)for(int b=a+1;b<N;b++){
    unsigned m=0;
    for(int t=0;t<N;t++)if(d[a][t]!=d[b][t])m|=1u<<t;
    sep[a][b]=m;
  }
  vector<unsigned char> good(TOTAL,0); map<int,int> counts,minimal,ftcounts; int pure2=0,pure1=0;
  for(int s=0;s<TOTAL;s++){
    bool ok=true,ft=true;
    for(int a=0;a<N;a++){
      for(int b=a+1;b<N;b++){
        int pop=__builtin_popcount(unsigned(s)&sep[a][b]);
        if(pop==0 || (((((s>>a)&1)^((s>>b)&1)) != 0) && pop==1))ok=false;
        if(pop<2)ft=false;
      }
    }
    if(__builtin_popcount(unsigned(s))==1 || __builtin_popcount(unsigned(s))==2){
      bool pure=true;
      for(int a=0;a<N;a++)if(s>>a&1)for(int b=0;b<N;b++)if(!(s>>b&1)){
        unsigned m=sep[a<b?a:b][a<b?b:a]&unsigned(s)&~(1u<<a);
        if(!m)pure=false;
      }
      if(pure){if(__builtin_popcount(unsigned(s))==1)pure1++;else pure2++;}
    }
    if(ok){good[s]=1;counts[__builtin_popcount(unsigned(s))]++;}
    if(ft)ftcounts[__builtin_popcount(unsigned(s))]++;
  }
  for(int s=0;s<TOTAL;s++)if(good[s]){
    bool essential=true;
    for(int j=0;j<N;j++)if((s>>j)&1)if(good[s^(1<<j)])essential=false;
    if(essential)minimal[__builtin_popcount(unsigned(s))]++;
  }
  assert((counts==map<int,int>{{5,192},{6,2712},{7,8288},{8,11966},{9,11328},{10,8008},{11,4368},{12,1820},{13,560},{14,120},{15,16},{16,1}}));
  assert((minimal==map<int,int>{{5,192},{6,1080},{7,192},{8,2}}));
  assert(ftcounts.begin()->first==6 && ftcounts[6]==336);
  assert(pure1==0 && pure2==8);
  cout<<"PASS GP(8,3): all 65536 subsets; min WTR=5 (192), min FTR=6 (336), minimal WTR spectrum:";
  for(auto [k,v]:minimal)cout<<" "<<k<<":"<<v;
  cout<<"; pure two-set WTR count="<<pure2<<"\n";
}
