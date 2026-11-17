// Finite exhaustive cross-check for immediate period-three states on gear graphs.
// No symbolic transfer or characteristic polynomial is used here.
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

static vector<uint8_t> step(const vector<uint8_t>& x, const vector<vector<int>>& N) {
  vector<uint8_t> y(x.size(), 0);
  for (size_t i=0;i<x.size();i++) {
    if (x[i]==1) y[i]=2;
    else if (x[i]==2) y[i]=0;
    else {for(int j:N[i]) if(x[j]==1){y[i]=1;break;}}
  }
  return y;
}
static void edge(vector<vector<int>>& adj,int a,int b) {adj[a].push_back(b);adj[b].push_back(a);}
static uint64_t gear_count(int n) {
  int N=2*n+1;
  vector<vector<int>> adj(N);
  for(int i=0;i<n;i++) {
    edge(adj,0,1+i);
    edge(adj,1+i,1+n+i);
    edge(adj,1+n+i,1+(i+1)%n);
  }
  uint64_t total=1;
  for(int i=0;i<N;i++) total*=3;
  uint64_t count=0, fixed=0, rotcheck=0;
  for(uint64_t id=0;id<total;id++){
    vector<uint8_t> x(N);
    uint64_t q=id;
    for(int i=0;i<N;i++){x[i]=q%3;q/=3;}
    auto y=step(x,adj),z=step(y,adj),w=step(z,adj);
    if(w==x){
      if(y==x) fixed++;
      else {
        count++;
        bool allrotate=true;
        for(int i=0;i<N;i++) if(y[i]!=(x[i]+1)%3) allrotate=false;
        if(allrotate) rotcheck++;
      }
    }
  }
  cout<<"n="<<n<<" states="<<total<<" fixed="<<fixed<<" P3="<<count<<" fully_rotating="<<rotcheck<<"\n";
  assert(fixed==1 && count==rotcheck);
  return count;
}
int main(){
  const vector<uint64_t> expected={36,84,300,954};
  for(int n=3;n<=6;n++) assert(gear_count(n)==expected[n-3]);
  cout<<"EXHAUSTIVE_PASS\n";
}
