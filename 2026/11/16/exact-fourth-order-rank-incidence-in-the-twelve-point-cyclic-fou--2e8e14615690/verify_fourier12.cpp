// Exact census of rank of every 4-by-4 submatrix of the order-12 DFT.
// Build: c++ -O2 -std=c++17 verify_fourier12.cpp -o check12 && ./check12
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int P=65557, ROOT=10574;
static int mpow(int b,int e){int64_t r=1,x=b;while(e){if(e&1)r=r*x%P;x=x*x%P;e>>=1;}return (int)r;}
static bool prime(int n){for(int d=2;d*d<=n;d++)if(n%d==0)return false;return n>1;}
int main(){
 assert(prime(P) && P>65536 && (P-1)%12==0);
 assert(mpow(ROOT,12)==1 && mpow(ROOT,6)==P-1 && mpow(ROOT,4)!=1);
 array<int,12> powers{}; powers[0]=1;
 for(int i=1;i<12;i++)powers[i]=(int)((int64_t)powers[i-1]*ROOT%P);
 vector<array<int,4>> ss;
 for(int a=0;a<12;a++)for(int b=a+1;b<12;b++)for(int c=b+1;c<12;c++)for(int d=c+1;d<12;d++)ss.push_back({a,b,c,d});
 assert(ss.size()==495);
 array<long long,5> rank_count{};int fullspark=0;
 for(auto rows:ss){int nonsingular=0;
  for(auto cols:ss){int x[4][4];
   for(int i=0;i<4;i++)for(int j=0;j<4;j++)x[i][j]=powers[(rows[i]*cols[j])%12];
   int rank=0;
   for(int j=0;j<4;j++){
    int pivot=rank;while(pivot<4 && x[pivot][j]==0)pivot++;
    if(pivot==4)continue;
    for(int k=j;k<4;k++)swap(x[pivot][k],x[rank][k]);
    int inv=mpow(x[rank][j],P-2);
    for(int i=rank+1;i<4;i++)if(x[i][j]){
      int z=(int)((int64_t)x[i][j]*inv%P);
      for(int k=j;k<4;k++)x[i][k]=(int)((x[i][k]-(int64_t)z*x[rank][k]%P+P)%P);
    }
    rank++;if(rank==4)break;
   }
   assert(rank>=2 && rank<=4);
   rank_count[rank]++;
   if(rank==4)nonsingular++;
  }
  if(nonsingular==495)fullspark++;
 }
 assert(rank_count[1]==0 && rank_count[2]==1224 && rank_count[3]==39384 && rank_count[4]==204417);
 assert(fullspark==24);
 assert(rank_count[2]+rank_count[3]+rank_count[4]==245025);
 cout<<"EXACT_Z12_TOTALS rank2="<<rank_count[2]<<" rank3="<<rank_count[3]<<" rank4="<<rank_count[4]<<"\n";
 cout<<"FULL_SPARK_ROWS "<<fullspark<<"\nEXACT_Z12_CHECK_PASS\n";
}
