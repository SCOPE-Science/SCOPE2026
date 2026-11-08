// Separate direct-bond calculation: enumerate ternary spins; count all 60 physical bonds of L(K6).
// Compile: c++ -O3 -std=c++17 verify_adjacency.cpp -o verify_adjacency && ./verify_adjacency
#include <array>
#include <iostream>
using namespace std;
constexpr int M=15, TOTAL=14348907;
constexpr int expE[16]={24,20,16,12,12,12,12,14,16,18,24,30,36,44,52,60};
constexpr long long expG[16]={1760,4680,2520,300,5580,19530,6180,15480,3420,120,900,1080,120,180,30,1};
int main(){int a[M],b[M],n=0;for(int i=0;i<6;i++)for(int j=i+1;j<6;j++){a[n]=i;b[n++]=j;}
 int U[60],V[60],m=0;
 for(int e=0;e<M;e++)for(int f=e+1;f<M;f++)if(a[e]==a[f]||a[e]==b[f]||b[e]==a[f]||b[e]==b[f]){U[m]=e;V[m++]=f;}
 if(m!=60)return 2;
 array<int,16> minE;array<long long,16> deg{};minE.fill(1000);
 for(int i=0;i<TOTAL;i++){
  int z=i,s[M],occ=0;for(int e=0;e<M;e++){s[e]=z%3;z/=3;occ+=(s[e]==0);}
  int energy=0;for(int p=0;p<m;p++)energy+=(s[U[p]]==s[V[p]]);
  if(energy<minE[occ]){minE[occ]=energy;deg[occ]=1;}
  else if(energy==minE[occ])deg[occ]++;
 }
 for(int i=0;i<=15;i++)if(minE[i]!=expE[i]||deg[i]!=expG[i]){cerr<<"MISMATCH "<<i<<"\n";return 1;}
 cout<<"VERIFY_ADJACENCY_OK 60 bonds "<<TOTAL<<" configurations\n";
}
