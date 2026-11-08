// Exhaustive ternary-word check of a 3-state antiferromagnetic Potts model on L(K_6).
// Compile: c++ -O3 -std=c++17 verify_ternary.cpp -o verify_ternary && ./verify_ternary
#include <array>
#include <cstdlib>
#include <iostream>
#include <string>
using namespace std;
constexpr int M=15,N=6, TOTAL=14348907;
constexpr int expectedE[16]={24,20,16,12,12,12,12,14,16,18,24,30,36,44,52,60};
constexpr long long expectedG[16]={1760,4680,2520,300,5580,19530,6180,15480,3420,120,900,1080,120,180,30,1};
int main(){int U[M],V[M],j=0;for(int u=0;u<N;u++)for(int v=u+1;v<N;v++){U[j]=u;V[j++]=v;}
 array<int,16> best;array<long long,16> ways{};array<string,16> witness{};best.fill(1000);
 for(int z=0;z<TOTAL;z++){
  int d[N][3]{};int k=z,occ=0;string ss(M,'0');
  for(int e=0;e<M;e++){int c=k%3;k/=3;ss[e]=char('0'+c);d[U[e]][c]++;d[V[e]][c]++;occ+=(c==0);}
  int E=0;for(int u=0;u<N;u++)for(int c=0;c<3;c++)E+=d[u][c]*(d[u][c]-1)/2;
  if(E<best[occ]){best[occ]=E;ways[occ]=1;witness[occ]=ss;}
  else if(E==best[occ])ways[occ]++;
 }
 long long totalWays=0;for(int i=0;i<=15;i++){
  cout<<i<<" "<<best[i]<<" "<<ways[i]<<" "<<witness[i]<<"\n";
  if(best[i]!=expectedE[i]||ways[i]!=expectedG[i]){cerr<<"MISMATCH\n";return 1;}
  totalWays+=ways[i];
 }
 cout<<"VERIFY_TERNARY_OK\n";
}
