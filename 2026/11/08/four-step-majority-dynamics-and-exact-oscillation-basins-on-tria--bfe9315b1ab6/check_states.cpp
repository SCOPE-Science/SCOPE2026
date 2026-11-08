// Exact state-space verifier for synchronous neighbour-majority dynamics on K1 join r K3.
// Usage: c++ -std=c++17 -O3 check_states.cpp -o check_states && ./check_states
#include <cstdint>
#include <iostream>
#include <vector>
#include <array>
#include <cstdlib>
using namespace std;

uint32_t advance_state(uint32_t x,int r,const vector<uint32_t>& nbr) {
  const int n=1+3*r;
  uint32_t y=0;
  for(int v=0;v<n;v++) {
    int degree=__builtin_popcount(nbr[v]);
    int active=__builtin_popcount(x&nbr[v]);
    if(2*active>degree || (2*active==degree && ((x>>v)&1u)))y|=(1u<<v);
  }
  return y;
}

int main(){
  for(int r=1;r<=7;r++){
    const int n=1+3*r; const uint32_t size=1u<<n;
    vector<uint32_t> nbr(n,0);
    for(int i=1;i<n;i++){nbr[0]|=1u<<i;nbr[i]|=1u;}
    for(int k=0;k<r;k++)for(int a=0;a<3;a++)for(int b=0;b<3;b++)if(a!=b)
      nbr[1+3*k+a]|=1u<<(1+3*k+b);
    uint64_t C[5][3]={{0}};
    for(uint32_t x=0;x<size;x++){
      array<uint32_t,7> orbit; orbit[0]=x;
      for(int t=0;t<=5;t++)orbit[t+1]=advance_state(orbit[t],r,nbr);
      int e=-1,period=0;
      for(int t=0;t<=4;t++){
        if(orbit[t+1]==orbit[t]){e=t;period=1;break;}
        if(orbit[t+2]==orbit[t]){e=t;period=2;break;}
      }
      if(e<0){cerr<<"FAIL: entry exceeds four, r="<<r<<" x="<<x<<"\n";return 1;}
      C[e][period]++;
    }
    uint64_t sum=0,fixed=0,primitive_cycles=0,basin2=0;int maxdepth=0;
    for(int t=0;t<=4;t++)for(int p=1;p<=2;p++){
      sum+=C[t][p]; if(C[t][p])maxdepth=t;
      if(p==1&&t==0)fixed=C[t][p];
      if(p==2){basin2+=C[t][p];if(t==0)primitive_cycles=C[t][p]/2;}
    }
    if(sum!=size || C[0][2]%2){cerr<<"FAIL: normalization\n";return 2;}
    cout<<"r="<<r<<" size="<<size<<" fixed="<<fixed<<" cycles2="<<primitive_cycles<<" basin2="<<basin2
        <<" maximum_entry="<<maxdepth<<" depth_period_counts=";
    for(int t=0;t<=4;t++){if(t)cout<<";";cout<<t<<":"<<C[t][1]<<","<<C[t][2];}cout<<"\n";
  }
  cout<<"STATE_ENUMERATION_PASS\n";
}
