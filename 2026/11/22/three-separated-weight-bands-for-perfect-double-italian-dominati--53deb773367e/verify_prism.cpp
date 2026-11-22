// Exact direct-neighborhood verification for two-clique prisms.
// Build: g++ -std=c++17 -O3 verify_prism.cpp -o verify_prism
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
using U64=uint64_t;
U64 choose(int n,int k){if(k<0||k>n)return 0; U64 p=1;for(int i=1;i<=k;i++)p=p*(n-i+1)/i;return p;}
map<int,U64> formula(int n){
 map<int,U64> p;
 auto add=[&](int d,U64 a){p[d]+=a;};
 add(6,choose(n,3)*choose(n,3)+U64(n)*n*n);
 add(7,U64(n)*n*(n-1)); add(8,choose(n,2));
 for(int k=0;k<=n;k++)add(2*n+1+k,2*U64(n)*choose(n,k));
 add(2*n+2,U64(n)*(n+1));add(2*n+3,2*n);add(3*n,2);
 for(int k=0;k<=2*n;k++)add(4*n+k,choose(2*n,k));
 return p;
}
int main(){
 for(int n=2;n<=6;n++){
  U64 cap=U64(1)<<(4*n);map<int,U64> coeff;
  vector<int> f(2*n);
  for(U64 x=0;x<cap;x++){
   U64 t=x;int weight=0;
   for(int v=0;v<2*n;v++){f[v]=int(t&3); t>>=2;weight+=f[v];}
   bool admissible=true;
   // Evaluate every closed neighborhood using graph edges, without layer-sum formulas.
   for(int v=0;v<2*n && admissible;v++){
    if(f[v]>=2)continue;
    int total=f[v];
    for(int u=0;u<2*n;u++)if(u!=v && ((u/n==v/n)||(u%n==v%n)))total+=f[u];
    if(total<3 || total>4)admissible=false;
   }
   if(admissible)coeff[weight]++;
  }
  if(n>=4){
   auto want=formula(n);
   for(auto const &z:want)assert(coeff[z.first]==z.second);
   for(auto const &z:coeff)assert(z.second==want[z.first]);
   assert(coeff.begin()->first==6);
  }
  if(n==2){assert(coeff.begin()->first==4 && coeff.begin()->second==3);}
  if(n==3){assert(coeff.begin()->first==5 && coeff.begin()->second==6);}
  cout<<"n="<<n<<" admissible=";
  U64 all=0;for(auto x:coeff)all+=x.second;cout<<all;
  cout<<" min_weight="<<coeff.begin()->first<<" minimizers="<<coeff.begin()->second;
  if(n>=4){cout<<" three_band_polynomial=PASS";}
  cout<<'\n';
 }
 cout<<"DIRECT_NEIGHBORHOOD_CERTIFICATE_OK\n";
}
