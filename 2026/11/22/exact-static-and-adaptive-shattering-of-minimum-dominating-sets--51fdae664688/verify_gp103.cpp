// Independent finite verifier using the generalized Petersen GP(10,3) model.
// Standard C++17, no external dependencies.
#include <array>
#include <algorithm>
#include <vector>
#include <unordered_map>
#include <cstdio>
#include <cstdint>
#include <cassert>
using namespace std;
int main(){
  const int n=20; const uint32_t ALL=(1u<<n)-1;
  array<uint32_t,n> N{};
  for(int i=0;i<n;i++)N[i]=1u<<i;
  auto edge=[&](int x,int y){N[x]|=1u<<y;N[y]|=1u<<x;};
  for(int i=0;i<10;i++) {edge(i,(i+1)%10);edge(i,10+i);edge(10+i,10+(i+3)%10);}
  for(int i=0;i<n;i++)assert(__builtin_popcount(N[i])==4);
  vector<uint32_t> C;
  int gamma=-1;
  for(int k=0;k<=6;k++){
    for(uint32_t m=0;m<=ALL;m++){
      if(__builtin_popcount(m)!=k)continue;
      uint32_t covered=0,m2=m;
      while(m2){int b=__builtin_ctz(m2);covered|=N[b];m2&=m2-1;}
      if(covered==ALL)C.push_back(m);
    }
    if(!C.empty()){gamma=k;break;}
  }
  assert(gamma==6&&C.size()==130);
  array<vector<uint32_t>,6> F;
  F[0].push_back(0);
  for(int k=1;k<=5;k++){
    for(uint32_t m=1;m<=ALL;m++){
      if(__builtin_popcount(m)!=k)continue;
      int positions[6],len=0;
      uint32_t x=m;
      while(x){positions[len++]=__builtin_ctz(x);x&=x-1;}
      bool seen[32]={false};int cnt=0;
      for(uint32_t s:C){int t=0;
        for(int j=0;j<k;j++)t|=((s>>positions[j])&1u)<<j;
        if(!seen[t]){seen[t]=true;cnt++;}
        if(cnt==(1<<k))break;
      }
      if(cnt==(1<<k))F[k].push_back(m);
    }
  }
  array<int,6> expected{1,20,190,560,360,0};
  for(int k=0;k<6;k++)assert(F[k].size()==(size_t)expected[k]);
  array<int,5> r{};
  for(int k=1;k<=4;k++){
    unordered_map<uint32_t,int> row;
    for(int i=0;i<(int)F[k-1].size();i++)row[F[k-1][i]]=i;
    int len=(F[k-1].size()+63)/64;
    vector<vector<uint64_t>> piv(F[k-1].size());
    for(uint32_t f:F[k]){
      vector<uint64_t> w(len);
      uint32_t m=f;
      while(m){int p=__builtin_ctz(m);m&=m-1;int j=row.at(f & ~(1u<<p));w[j>>6]^=1ull<<(j&63);}
      while(true){int hi=-1;
        for(int b=len-1;b>=0;b--)if(w[b]){hi=b*64+63-__builtin_clzll(w[b]);break;}
        if(hi<0)break;
        if(piv[hi].empty()){piv[hi]=w;r[k]++;break;}
        for(int b=0;b<len;b++)w[b]^=piv[hi][b];
      }
    }
  }
  assert(r[1]==1&&r[2]==19&&r[3]==141&&r[4]==300);
  for(int i=0;i<20;i++){
    int positive=0;for(uint32_t s:C)positive += !!(s&(1u<<i));
    assert(positive==39);
  }
  printf("GP(10,3): gamma=%d concepts=%zu shattering=[",gamma,C.size());
  for(int k=0;k<6;k++)printf("%s%zu",k?",":"",F[k].size());
  printf("] ranks=[%d,%d,%d,%d] reduced_Betti=(30,119,60) positive_branch=39\n",r[1],r[2],r[3],r[4]);
  return 0;
}
