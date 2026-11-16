#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
struct E {long long a,b;};
E operator+(E x,E y){return {x.a+y.a,x.b+y.b};}
E operator*(E x,E y){return {x.a*y.a-x.b*y.b,x.a*y.b+x.b*y.a-x.b*y.b};}
long long norm2(E x){return x.a*x.a-x.a*x.b+x.b*x.b;}
constexpr E root[3]={{1,0},{0,1},{-1,-1}};
E circperm(const array<int,8>& e){
  E dp[256]{};dp[0]={1,0};
  for(int m=1;m<256;m++){
    int i=__builtin_popcount((unsigned)m)-1;E s{0,0};
    for(int j=0;j<8;j++)if((m>>j)&1)
      s=s+dp[m^(1<<j)]*root[e[(j-i+8)%8]];
    dp[m]=s;
  }
  return dp[255];
}
int main(){
  map<long long,int> distribution; long long least=LLONG_MAX;
  int count=0;E witness{0,0};
  for(int z=0;z<6561;z++){
    int u=z;array<int,8> e{};
    for(int j=0;j<8;j++){e[j]=u%3;u/=3;}
    E v=circperm(e);long long q=norm2(v);
    distribution[q]++;
    if(q<least){least=q;count=1;witness=v;}
    else if(q==least) count++;
  }
  assert(distribution.size()==59);
  assert(distribution.at(1296)==48);
  assert(least==1296&&count==48);
  array<int,8> e={1,1,0,1,1,0,0,0};
  E evalue=circperm(e);
  assert(norm2(evalue)==1296);
  cout<<"CIRCULANT_EISENSTEIN_PASS min_norm_squared="<<least
      <<" minimizers="<<count<<" distinct_levels="<<distribution.size()
      <<" witness="<<evalue.a<<","<<evalue.b<<"\n";
}
