// Standalone exhaustive certificate for distance-equalizer sets of GP(10,2).
// Build with: c++ -O2 -std=c++17 verify_direct.cpp -o verify_direct
// Run with: ./verify_direct
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int main() {
  constexpr int N=20;
  array<vector<int>,N> a;
  auto edge=[&](int u,int v){a[u].push_back(v);a[v].push_back(u);};
  for(int i=0;i<10;++i){ edge(i,(i+1)%10);edge(i,10+i);edge(10+i,10+(i+2)%10); }
  array<array<int,N>,N> d;
  for(int s=0;s<N;++s){ d[s].fill(-1);queue<int> q;q.push(s);d[s][s]=0;
    while(!q.empty()){int v=q.front();q.pop();for(int w:a[v])if(d[s][w]<0){d[s][w]=d[s][v]+1;q.push(w);}}
  }
  array<int,6> distances{};
  vector<pair<int,int>> pairs;
  for(int i=0;i<N;++i)for(int j=i+1;j<N;++j) {
    ++distances[d[i][j]];pairs.emplace_back(i,j);
    int k=0;for(int w=0;w<N;++w)k+=(d[w][i]==d[w][j]);
    assert(k==(d[i][j]==5?0:4));
  }
  assert((distances==array<int,6>{0,30,60,60,30,10}));
  // Permutation for the ten antipodal pairs, checked using graph distances.
  array<int,N> antipode{};
  for(int i=0;i<10;++i){antipode[i]=(i+5)%10;antipode[10+i]=10+(i+5)%10;}
  for(int v=0;v<N;++v){assert(d[v][antipode[v]]==5);for(int x=0;x<N;++x)assert(d[x][v]+d[x][antipode[v]]==5);}
  for(auto [u,v]:pairs)if(d[u][v]!=5){
    int eqmask=0;for(int x=0;x<N;++x)if(d[x][u]==d[x][v])eqmask|=(1<<x);
    assert(__builtin_popcount((unsigned)eqmask)==4);
    for(int x=0;x<N;++x)if(eqmask>>x&1)assert(eqmask>>antipode[x]&1);
  }
  array<long long,21> polynomial{};
  long long mismatch=0,total=0;
  // Truly exhaustive 2^20 subsets, checking the original definition without
  // relying on the antipodal characterization.
  for(int s=0;s<(1<<N);++s){
    bool feasible=true;
    for(auto [u,v]:pairs)if(!(s>>u&1)&&!(s>>v&1)){
      bool found=false;
      for(int w=0;w<N;++w)if((s>>w&1)&&d[w][u]==d[w][v]){found=true;break;}
      if(!found){feasible=false;break;}
    }
    bool transversal=true;
    for(int i=0;i<5;++i){
      if(!(s>>i&1)&&!(s>>(i+5)&1))transversal=false;
      if(!(s>>(10+i)&1)&&!(s>>(15+i)&1))transversal=false;
    }
    if(transversal!=feasible)++mismatch;
    if(feasible){++total;++polynomial[__builtin_popcount((unsigned)s)];}
  }
  assert(mismatch==0);assert(total==59049); // 3^10
  for(int k=0;k<=20;++k){
    long long expected=0;
    // Each pair contributes either singleton (2 choices) or both endpoints.
    if(k>=10){
      long long choose=1;int both=k-10;
      for(int i=0;i<both;++i)choose=choose*(10-i)/(i+1);
      expected=choose*(1LL<<(20-k));
    }
    assert(polynomial[k]==expected);
  }
  cout<<"DISTANCE_PAIR_COUNTS";for(int r=1;r<=5;++r)cout<<" "<<distances[r];cout<<"\n";
  cout<<"EQUALIZER_COUNTS";for(int k=0;k<=20;++k)if(polynomial[k])cout<<" "<<k<<":"<<polynomial[k];cout<<"\n";
  cout<<"FULL_TOTAL "<<total<<"\nPASS\n";
}
