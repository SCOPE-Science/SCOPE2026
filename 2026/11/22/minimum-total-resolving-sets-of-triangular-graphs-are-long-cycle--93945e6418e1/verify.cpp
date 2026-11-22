// Independent finite checks for third-party distance resolution on triangular graphs.
// A vertex of J(n,2) is an unordered pair of elements of {0,...,n-1}.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>
#include <utility>
using namespace std;
using U=uint64_t;
static int dis(pair<int,int> a,pair<int,int> b){
  if(a==b)return 0;
  int overlap=(a.first==b.first)+(a.first==b.second)+(a.second==b.first)+(a.second==b.second);
  return 2-overlap;
}
static bool root_test(int n,vector<pair<int,int>> const& ed,U S){
  vector<int> adj(n,0),comp(n,-1),cnt;
  for(size_t k=0;k<ed.size();k++)if(S&(U(1)<<k)){
    auto [a,b]=ed[k];adj[a]|=1<<b;adj[b]|=1<<a;
  }
  for(int a=0;a<n;a++)for(int b=0;b<n;b++)if(a!=b)for(int c=b+1;c<n;c++)if(c!=a){
    int outside=(1<<n)-1-(1<<a)-(1<<b)-(1<<c);
    if(!((adj[b]|adj[c])&outside))return false;
  }
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++)if(c!=a)for(int d=c+1;d<n;d++)if(d!=a){
    int x=(1<<a)|(1<<b)|(1<<c)|(1<<d), ext=((1<<n)-1)^x;
    for(int t=0;t<n;t++)if((x>>t)&1)if(adj[t]&ext)goto next_four;
    return false;
    next_four:;
  }
  return true;
}
static bool full_witness_test(U S,vector<U> const& witness){
  for(U w:witness) if(!(S&w))return false;
  return true;
}
static U cycle_mask(int n,vector<pair<int,int>> const& edges,vector<int> const& cc){
  U ans=0;
  for(int i=0;i<(int)cc.size();i++){
    int a=cc[i],b=cc[(i+1)%cc.size()];
    if(a>b)swap(a,b);
    for(size_t k=0;k<edges.size();k++)if(edges[k]==make_pair(a,b)){ans|=U(1)<<k;break;}
  }
  return ans;
}
static uint64_t predict_count(int n){
  // labelled (n-1)-vertex set: a permutation, divided by cycle rotations/reversals
  vector<uint64_t> f(n,0);f[0]=1;
  for(int j=1;j<n;j++){
    uint64_t val=0;
    // decomposing a 2-regular graph by the cycle containing its least vertex
    for(int ell=5;ell<=j;ell++){
      uint64_t choose=1;
      for(int t=1;t<ell;t++)choose=choose*(j-t)/t; // C(j-1,ell-1)
      uint64_t per=1;for(int t=2;t<ell;t++)per*=t;
      val+=choose*(per/2)*f[j-ell];
    }
    f[j]=val;
  }
  return (uint64_t)n*f[n-1];
}
int main(){
  for(int n=4;n<=8;n++){
    vector<pair<int,int>> E;
    for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)E.emplace_back(a,b);
    const int m=E.size();vector<U> W;
    for(int a=0;a<m;a++)for(int b=a+1;b<m;b++){
      U mask=0;
      for(int w=0;w<m;w++)if(w!=a&&w!=b&&dis(E[w],E[a])!=dis(E[w],E[b]))mask|=U(1)<<w;
      W.push_back(mask);
    }
    int maxK=(n==4?m:n==5?5:n-1);
    uint64_t optimumCount=0,lowerCount=0;U example=0;
    for(int k=0;k<=maxK;k++){
      uint64_t good=0;U limit=U(1)<<m;
      if(k==0) {if(full_witness_test(0,W))good++;}
      else{
        U S=(U(1)<<k)-1;
        while(S<limit){
          if(full_witness_test(S,W)) {good++;if(!example)example=S;}
          U c=S&-S, r=S+c;
          if(!r||r>=limit)break;
          S=(((r^S)>>2)/c)|r;
        }
      }
      if(k<maxK)lowerCount+=good;
      else optimumCount=good;
      cout<<"n="<<n<<" k="<<k<<" count="<<good<<"\n";
    }
    if(n==4)assert(optimumCount==0);
    if(n==5)assert(lowerCount==0&&optimumCount==132);
    if(n>=6)assert(lowerCount==0&&optimumCount==predict_count(n));
    if(n>=6){
      vector<int> cycle(n-1);iota(cycle.begin(),cycle.end(),0);
      U mask=cycle_mask(n,E,cycle);
      assert(full_witness_test(mask,W));
    }
    // Independent structural neighborhood / four-cut formulation, tested on random sets.
    mt19937_64 gen(4917+n);
    for(int i=0;i<20000;i++){
      U S=gen() & ((U(1)<<m)-1);
      assert(root_test(n,E,S)==full_witness_test(S,W));
    }
    cout<<"PASS_N_"<<n<<"\n";
  }
  cout<<"TRIANGULAR_TOTAL_METRIC_VERIFY_OK\n";
}
