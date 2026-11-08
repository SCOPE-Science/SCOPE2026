// Exact independent dynamic-programming enumeration of unique shortest absent binary subsequences.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main() {
  constexpr int MAXN = 22;
  long long expected[MAXN+1][MAXN+1] = {};
  expected[1][0] = 2;
  for (int n=2;n<=MAXN;n++) for(int k=0;k<=MAXN;k++) {
    expected[n][k]=expected[n-1][k];
    if(k>0 && n>=2) expected[n][k]+=expected[n-2][k-1];
    if(k>0 && n>=3) expected[n][k]+=expected[n-3][k-1];
  }
  for (int n=1;n<=MAXN;n++) {
    long long got[MAXN+1] = {};
    for(uint32_t word=0;word<(1u<<n);word++) {
      int first[2] = {n,n};
      int shortest[MAXN+2] = {};
      int number[MAXN+2] = {};
      shortest[n] = 1;
      number[n] = 2; // The empty suffix misses both single letters.
      for(int i=n-1;i>=0;i--) {
        first[(word>>i)&1u] = i;
        int cost[2];
        for(int b=0;b<2;b++)
          cost[b] = first[b]==n ? 1 : 1+shortest[first[b]+1];
        shortest[i] = min(cost[0],cost[1]);
        number[i] = 0;
        for(int b=0;b<2;b++) if(cost[b]==shortest[i])
          number[i] += (first[b]==n ? 1 : number[first[b]+1]);
      }
      if(number[0]==1) got[shortest[0]-1]++;
    }
    long long total=0;
    for(int k=0;k<=MAXN;k++) {
      if(got[k]!=expected[n][k]) {
        cerr<<"DISAGREEMENT n="<<n<<" k="<<k<<" got="<<got[k]
            <<" expect="<<expected[n][k]<<"\n";
        return 1;
      }
      total += got[k];
    }
    cout<<n<<" "<<total<<"\n";
  }
  cout<<"DYNAMIC_CENSUS_VERIFY_OK\n";
}
