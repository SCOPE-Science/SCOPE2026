// Independent exact certificate for a sixteen-site quantum-walk trapping census.
// Build: g++ -O2 -std=c++17 check_krylov.cpp -o check_krylov
// Run: ./check_krylov
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;
using ll=long long;
constexpr ll primes[2]={1000000007LL,1000000009LL};
ll power(ll x,ll k,ll p){ll r=1;while(k){if(k&1)r=r*x%p;x=x*x%p;k>>=1;}return r;}
int mod_rank(const vector<vector<int>>& matrix,ll p){
 const int m=(int)matrix.size(),n=(int)matrix[0].size();
 vector<vector<ll>> a(m,vector<ll>(n));
 for(int i=0;i<m;i++)for(int j=0;j<n;j++)a[i][j]=(matrix[i][j]%p+p)%p;
 int r=0;
 for(int j=0;j<n&&r<m;j++){
  int q=r;while(q<m&&!a[q][j])q++;
  if(q==m)continue;
  swap(a[q],a[r]);
  ll inv=power(a[r][j],p-2,p);
  for(int i=r+1;i<m;i++)if(a[i][j]){
    ll ratio=a[i][j]*inv%p;
    for(int k=j;k<n;k++)a[i][k]=(a[i][k]-ratio*a[r][k]%p+p)%p;
  }
  r++;
 }
 return r;
}
int main(){
 for(int type=0;type<2;type++){
  int a[16][16]={},a2[16][16]={};
  for(int u=0;u<16;u++)for(int v=0;v<16;v++)if(u!=v){
   const int x=u/4,y=u%4,X=v/4,Y=v%4;
   if(type==0)a[u][v]=(x==X||y==Y);
   else {const int dx=(X-x+4)%4,dy=(Y-y+4)%4;
     a[u][v]=(dx==1&&dy==0)||(dx==3&&dy==0)||
              (dx==0&&dy==1)||(dx==0&&dy==3)||
              (dx==1&&dy==1)||(dx==3&&dy==3);
   }
  }
  for(int u=0;u<16;u++)for(int v=0;v<16;v++){
    for(int w=0;w<16;w++)a2[u][v]+=a[u][w]*a[w][v];
    if(a2[u][v]!=(u==v?6:2))throw runtime_error("SRG test failed");
  }
  map<int,int> dark_counts;
  for(int mask=0;mask<(1<<16);mask++)if(__builtin_popcount((unsigned)mask)==9){
    vector<int> t;for(int u=0;u<16;u++)if(mask&(1<<u))t.push_back(u);
    vector<vector<int>> mat(16,vector<int>(27));
    for(int u=0;u<16;u++)for(int j=0;j<9;j++){
      mat[u][3*j]=(u==t[j]);
      mat[u][3*j+1]=a[u][t[j]];
      mat[u][3*j+2]=a2[u][t[j]];
    }
    int r1=mod_rank(mat,primes[0]),r2=mod_rank(mat,primes[1]);
    int exact_rank=max(r1,r2);
    // Every minor of size <=16 has absolute determinant <10^16:
    // columns e_v, A e_v, A^2 e_v have norms 1,sqrt(6),sqrt(96).
    // 10^16 < primes[0]*primes[1], so max modular rank is exact.
    dark_counts[16-exact_rank]++;
  }
  const char* name=type==0?"ROOK":"SHRIKHANDE";
  cout<<name;for(auto [dark,count]:dark_counts)cout<<" dark="<<dark<<":"<<count;cout<<"\n";
  if(type==0 && dark_counts!=map<int,int>{{0,3936},{1,6736},{2,768}})return 2;
  if(type==1 && dark_counts!=map<int,int>{{0,7200},{1,4144},{2,96}})return 3;
 }
 cout<<"KRYLOV_OK cases=22880 primes=1000000007,1000000009\n";
}
