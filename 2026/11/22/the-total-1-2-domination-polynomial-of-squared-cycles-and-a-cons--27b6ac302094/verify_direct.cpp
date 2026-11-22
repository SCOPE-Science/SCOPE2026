// Independent adjacency-based exhaustive verification (standard C++17).
#include <cstdint>
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;
int main(){
  for(int n=5;n<=21;++n){
    vector<unsigned> neigh(n);
    for(int v=0;v<n;++v)
      for(int j=0;j<n;++j)
        if(j!=v){int d=(j-v+n)%n;if(d==1||d==2||d==n-1||d==n-2)neigh[v] |= 1u<<j;}
    vector<unsigned long long> count(n+1);
    for(unsigned m=0;m<(1u<<n);++m){
      bool feasible=true;
      for(int v=0;v<n;++v){
        int c=__builtin_popcount(m & neigh[v]);
        if(c<1||c>2){feasible=false;break;}
      }
      if(feasible) ++count[__builtin_popcount(m)];
    }
    int k=0;while(!count[k])++k;
    int q=n/7,r=n%7,expect=2*q+(r==0?0:(r<=2?1:2));
    assert(k==expect);
    if(r==0)assert(count[k]==7);
    if(r==1)assert(count[k]==(unsigned)((2*q-1)*n));
    if(r==2)assert(count[k]==(unsigned)n);
    if(r==6)assert(count[k]==2u*n);
    unsigned long long total=0;for(auto v:count)total+=v;
    cout<<n<<" "<<k<<" "<<count[k]<<" "<<total<<"\n";
  }
  cout<<"PASS independently enumerated every subset n=5..21\n";
}
