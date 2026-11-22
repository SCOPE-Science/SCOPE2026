// Independent exhaustive witness for the first two period-seven orders.
// Enumerates all supports of label-2 vertices with possible optimum weight.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <vector>
using namespace std;
using U=uint64_t;
struct Exhaust {
 int n,N,limit,best; vector<U> nb; map<pair<int,int>,int> counts;
 Exhaust(int n0): n(n0),N(2*n0),limit(8*n0/7),best(2*n0+1),nb(N,0){
  for(int i=0;i<N;i++)nb[i] |= U(1)<<i;
  auto add=[&](int x,int y){nb[x] |= U(1)<<y;nb[y]|= U(1)<<x;};
  for(int i=0;i<n;i++){
   add(i,(i+1)%n);add(i,n+i);add(n+i,n+(i+2)%n);
  }
 }
 void explore(int from,int left,U twos,U covered){
  if(left==0){
   int k=__builtin_popcountll(twos),one=N-__builtin_popcountll(covered),w=2*k+one;
   if(w<best){best=w;counts.clear();}
   if(w==best)counts[{k,one}]++;
   return;
  }
  for(int t=from;t<=N-left;t++)explore(t+1,left-1,twos|(U(1)<<t),covered|nb[t]);
 }
 void check(){
  for(int k=0;k<=limit/2;k++)explore(0,k,0,0);
  int cnt=0;for(auto z:counts)cnt+=z.second;
  if(best!=limit || cnt!=7 || counts.size()!=1 || counts.begin()->first!=make_pair(3*n/7,2*n/7))
      throw runtime_error("minimum Roman count mismatch");
  cout<<"PASS n="<<n<<" minimum_weight="<<best<<" optimal_functions="<<cnt<<" twos="<<3*n/7<<" ones="<<2*n/7<<"\n";
 }
};
int main(){Exhaust(7).check(); Exhaust(14).check();}
