// Exact certification of the ranks of all 6-by-6 minors of the order-12 Fourier matrix.
// Standard C++17. Usage: ./verify_rank12 rank_orbits.csv
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
using i64=long long;
constexpr int N=12, K=6, P[2]={1000033,1001017}, Z[2]={385966,72098};
bool isprime(int n){for(int d=2;d*d<=n;d++)if(n%d==0)return false;return n>1;}
i64 power(i64 a,int n,int p){i64 result=1;while(n){if(n&1)result=result*a%p;a=a*a%p;n/=2;}return result;}
int shift(int mask,int s){int out=0;for(int i=0;i<N;i++)if(mask&(1<<i))out|=1<<((i+s)%N);return out;}
array<int,K> indices(int mask){array<int,K> out{};int a=0;for(int i=0;i<N;i++)if(mask&(1<<i))out[a++]=i;assert(a==K);return out;}
int rank_mod(const array<int,K>& r,const array<int,K>& c,int p,int z){
 int roots[N];roots[0]=1;for(int t=1;t<N;t++)roots[t]=(i64)roots[t-1]*z%p;
 int a[K][K];for(int i=0;i<K;i++)for(int j=0;j<K;j++)a[i][j]=roots[r[i]*c[j]%N];
 int rank=0;
 for(int j=0;j<K;j++){
  int pivot=rank;while(pivot<K&&!a[pivot][j])pivot++;
  if(pivot==K)continue;
  for(int h=0;h<K;h++)swap(a[rank][h],a[pivot][h]);
  int inv=power(a[rank][j],p-2,p);
  for(int i=rank+1;i<K;i++){
   i64 fac=(i64)a[i][j]*inv%p;
   for(int h=j;h<K;h++)a[i][h]=((i64)a[i][h]-fac*a[rank][h]%p+p)%p;
  }
  ++rank;
 }
 return rank;
}
int main(int argc,char**argv){
 assert(argc==2);
 for(int t=0;t<2;t++){
  assert(isprime(P[t]));
  assert(power(Z[t],12,P[t])==1 && power(Z[t],6,P[t])!=1);
  assert(power(Z[t],4,P[t])!=1 && power(Z[t],3,P[t])!=1);
 }
 assert((i64)P[0]*P[1]>2176782336LL); // 6^(2*6), upper bound on every 12th-cyclotomic norm
 set<int> visited;map<int,vector<int>> orbit;
 for(int m=0;m<1<<N;m++)if(__builtin_popcount((unsigned)m)==K&&!visited.count(m)){
  int representative=1<<N;set<int> members;
  for(int t=0;t<N;t++){int u=shift(m,t);members.insert(u);representative=min(representative,u);visited.insert(u);}
  orbit[representative]=vector<int>(members.begin(),members.end());
 }
 assert(visited.size()==924 && orbit.size()==80);
 ofstream csv(argv[1]);assert(csv.good());csv<<"rows,cols,rank,row_size,col_size\n";
 i64 counts[7]={};int pairs=0;
 for(const auto& [rmask,rv]:orbit){auto r=indices(rmask);
  for(const auto& [cmask,cv]:orbit){auto c=indices(cmask);
   int ra=rank_mod(r,c,P[0],Z[0]);int rb=rank_mod(r,c,P[1],Z[1]);
   assert(ra==rb && ra>=3 && ra<=6);
   counts[ra]+=(i64)rv.size()*cv.size();pairs++;
   csv<<rmask<<","<<cmask<<","<<ra<<","<<rv.size()<<","<<cv.size()<<"\n";
  }
 }
 assert(pairs==6400 && counts[3]==76 && counts[4]==5376 && counts[5]==150564 && counts[6]==697760);
 i64 total=0;for(int i=0;i<7;i++)total+=counts[i];assert(total==853776);
 cout<<"80 translation orbits; 6400 orbit-pair exact ranks; 924 row sets\n";
 for(int i=0;i<7;i++)cout<<"rank "<<i<<": "<<counts[i]<<"\n";
 cout<<"CRT norm bound: "<<2176782336LL<<" < "<<(i64)P[0]*P[1]<<"\n";
 cout<<"VERIFY_OK\n";
}
