// Reproduces the finite checks for minimum paired dominating sets of KG(n,2).
// Compile: c++ -O2 -std=c++17 verify_min_paired_kg2.cpp -o verify && ./verify
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
struct Instance {
  int n,N; vector<pair<int,int>> edges; vector<uint32_t> adj;
  vector<int8_t> memo;
  explicit Instance(int n):n(n){
    for(int i=0;i<n;++i) for(int j=i+1;j<n;++j)edges.emplace_back(i,j);
    N=edges.size();assert(N<=28);
    adj.resize(N); for(int i=0;i<N;++i)for(int j=0;j<N;++j){auto [a,b]=edges[i];auto [c,d]=edges[j];if(a!=c&&a!=d&&b!=c&&b!=d)adj[i]|=1U<<j;}
    if(N<=21){memo.resize(1U<<N,-1);memo[0]=1;}
  }
  bool matching(uint32_t mask){
    if(!mask)return true;
    if(__builtin_popcount(mask)&1)return false;
    if(N<=21&&memo[mask]!=-1)return memo[mask];
    int i=__builtin_ctz(mask);uint32_t rem=mask^(1U<<i);uint32_t partners=rem&adj[i];
    while(partners){uint32_t b=partners&(-partners);partners-=b;if(matching(rem^b)){if(N<=21)memo[mask]=1;return true;}}
    if(N<=21)memo[mask]=0;
    return false;
  }
  bool dominates(uint32_t mask){
    for(int i=0;i<N;++i)if(!(mask&(1U<<i))&&!(mask&adj[i]))return false;
    return true;
  }
  bool paired(uint32_t mask){return dominates(mask)&&matching(mask);}
  bool expected4(uint32_t mask){
    if(__builtin_popcount(mask)!=4)return false;
    // H contains three pairwise disjoint edges, and the fourth may meet zero,
    // one, or two of those three; the non-paired case K3 + K2 is excluded.
    vector<int> ids;for(int i=0;i<N;++i)if(mask>>i&1)ids.push_back(i);
    for(int omit=0;omit<4;++omit){
      int x[3],k=0;for(int j=0;j<4;++j)if(j!=omit)x[k++]=ids[j];
      if((adj[x[0]]&(1U<<x[1]))&&(adj[x[0]]&(1U<<x[2]))&&(adj[x[1]]&(1U<<x[2])))return true;
    }
    return false;
  }
  bool tree_complement_of6(uint32_t mask){
    if(n!=5||__builtin_popcount(mask)!=6)return false;
    int par[5]={0,1,2,3,4};
    auto root=[&](int a){while(par[a]!=a)a=par[a];return a;};
    int count=0;
    for(int i=0;i<N;++i)if(!(mask>>i&1)){
      auto [a,b]=edges[i];++count;
      int x=root(a),y=root(b);if(x==y)return false;par[x]=y;
    }
    if(count!=4)return false;
    for(int i=0;i<5;++i)if(root(i)!=root(0))return false;
    return true;
  }
};
int main(){
  const map<int,long long> expected={{4,1},{5,125},{6,180},{7,1575},{8,7665}};
  unsigned long long examined=0,paired=0;
  for(int n=4;n<=7;++n){
    Instance G(n);
    unsigned long long total=0,optimal=0,trees=0;
    int optimum=(n<=5?6:4);
    for(uint32_t mask=1;mask<(1U<<G.N);++mask){
      ++total;
      if(!G.paired(mask))continue;
      ++paired;
      if(__builtin_popcount(mask)==optimum){
        ++optimal;
        if(n>=6&& !G.expected4(mask)){cerr<<"4-vertex family mismatch n="<<n<<"\n";return 1;}
        if(n==5){if(!G.tree_complement_of6(mask)){cerr<<"tree mismatch\n";return 2;}++trees;}
      }
      if(__builtin_popcount(mask)<optimum){cerr<<"smaller paired set found n="<<n<<"\n";return 3;}
    }
    if(optimal!=expected.at(n)||(n==5&&trees!=125)){cerr<<"coefficient failure "<<n<<" "<<optimal<<"\n";return 4;}
    examined+=total;
    cout<<"n="<<n<<" subsets="<<total<<" optimal="<<optimal<<"\n";
  }
  Instance G(8);unsigned long long fours=0,choices=0;
  // Independently enumerate 4-edge combinations of the 28 auxiliary edges.
  for(int a=0;a<G.N;++a)for(int b=a+1;b<G.N;++b)
    for(int c=b+1;c<G.N;++c)for(int d=c+1;d<G.N;++d){
      ++choices;
      uint32_t mask=(1U<<a)|(1U<<b)|(1U<<c)|(1U<<d);
      bool P=G.paired(mask);if(P!=G.expected4(mask)){cerr<<"n8 structural mismatch\n";return 5;}
      fours+=P;
    }
  if(fours!=expected.at(8)){cerr<<"n8 expected="<<expected.at(8)<<" got="<<fours<<"\n";return 6;}
  cout<<"n=8 four_subsets="<<choices<<" optimal="<<fours<<"\n";
  cout<<"VERIFY_OK full_orders=4..7 full_subsets="<<examined<<" paired_sets="<<paired
     <<" n8_four_subsets="<<choices<<" minimum_counts=1,125,180,1575,7665"
     <<" tree_bijection_n5=PASS three_families=PASS"<<"\n";
}
