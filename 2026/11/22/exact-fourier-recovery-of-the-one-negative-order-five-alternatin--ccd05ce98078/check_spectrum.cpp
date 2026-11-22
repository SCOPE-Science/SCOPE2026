// Exact signed incidence spectrum of 5-by-5 alternating-sign matrices with exactly one -1.
// Build: g++ -std=c++17 -O3 check_spectrum.cpp -o check_spectrum
// Run: ./check_spectrum  (about 160 MiB RAM; all arithmetic is exact integer)
#include <cstdint>
#include <cstdlib>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <array>
#include <algorithm>
#include <numeric>
#include <cassert>
#include <iostream>
#include <string>

constexpr int N = 5, D = 25, Q = 1<<D;
using Row = std::array<int8_t,N>;
std::vector<Row> admissible_rows;
std::vector<uint32_t> masks;
int all_count=0;

void rows(int j,int sum,Row row){
 if(j==N){if(sum==1)admissible_rows.push_back(row);return;}
 for(int x=-1;x<=1;++x)if(sum+x==0 || sum+x==1){row[j]=x;rows(j+1,sum+x,row);}
}
void visit(int depth,std::array<int,N> cols,int neg,uint32_t mask){
 if(depth==N){
  if(std::all_of(cols.begin(),cols.end(),[](int a){return a==1;})){
   ++all_count;
   if(neg==1) masks.push_back(mask);
  }
  return;
 }
 for(const Row& r:admissible_rows){
  std::array<int,N> nc=cols;int nn=neg;uint32_t mm=mask;bool ok=true;
  for(int j=0;j<N;++j){
   nc[j]+=r[j];if(nc[j]<0||nc[j]>1){ok=false;break;}
   if(r[j]<0)++nn;
   if(r[j]!=0)mm|=(uint32_t(1)<<(depth*N+j));
  }
  if(ok && nn<=1)visit(depth+1,nc,nn,mm);
  // Count all ASMs separately, without pruning by negative count.
 }
}
void visit_all(int depth,std::array<int,N> cols){
 if(depth==N){if(std::all_of(cols.begin(),cols.end(),[](int a){return a==1;}))++all_count;return;}
 for(const Row& r:admissible_rows){
  std::array<int,N> nc=cols;bool ok=true;
  for(int j=0;j<N;++j){nc[j]+=r[j];if(nc[j]<0||nc[j]>1){ok=false;break;}}
  if(ok)visit_all(depth+1,nc);
 }
}
void fwht(std::vector<int32_t>& a){
 for(int bit=0;bit<D;++bit){
  const int h=1<<bit;
  for(int block=0;block<Q;block+=2*h){
   for(int j=0;j<h;++j){int32_t u=a[block+j],v=a[block+j+h];a[block+j]=u+v;a[block+j+h]=u-v;}
  }
 }
}
int main(){
 rows(0,0,Row{});
 visit_all(0,{});
 if(all_count!=429){std::cerr<<"FAILED full ASM total "<<all_count<<"\n";return 2;}
 all_count=0;visit(0,{},0,0);
 if(all_count!=320 || masks.size()!=200){std::cerr<<"FAILED one-minus enumeration "<<all_count<<" "<<masks.size()<<"\n";return 3;}
 std::sort(masks.begin(),masks.end());
 if(std::unique(masks.begin(),masks.end())!=masks.end()){std::cerr<<"duplicate occupancy mask\n";return 4;}
 std::vector<int32_t> a(Q,0);
 for(uint32_t m:masks)a[m]++;
 fwht(a);
 int64_t zeros=0,negatives=0;int gap=1000;
 std::map<int,int64_t> spectrum;
 for(int32_t v:a){
  spectrum[v]++;
  if(v==0)++zeros;
  else{gap=std::min(gap,std::abs((int)v));if(v<0)++negatives;}
 }
 int z1=0,z2=0,z3=0;
 std::vector<std::pair<int,int>> zero_pairs;
 for(int i=0;i<Q;i++)if(a[i]==0){
  const int k=__builtin_popcount((uint32_t)i);
  if(k==1)++z1; if(k==2){++z2;int p=__builtin_ctz((uint32_t)i);int q=__builtin_ctz((uint32_t)i & ((uint32_t)i-1));zero_pairs.push_back({p,q});}
  if(k==3)++z3;
 }
 const std::map<int,int64_t> expected_positive = {
 {4,4012544},{8,3500288},{12,2669056},{16,1877504},{20,1107456},
 {24,577280},{28,329728},{32,205056},{36,129024},{40,85760},
 {44,55808},{48,41216},{52,20480},{56,11264},{60,9216},
 {64,12288},{68,11776},{72,7168},{76,4096},{80,768},
 {92,2048},{96,3072},{100,3072},{108,1024},
 {136,1024},{140,512},{168,1024},{200,256}};
 const std::set<std::pair<int,int>> expected_pairs={{6,12},{6,13},{6,17},{7,16},{7,18},{8,11},{8,12},{8,17},{11,18},{12,16},{12,18},{13,16}};
 const bool pairs_ok=std::set<std::pair<int,int>>(zero_pairs.begin(),zero_pairs.end())==expected_pairs;
 bool hist_ok=(spectrum[0]==4194816);
 for(auto [v,c]:expected_positive)hist_ok=hist_ok&&spectrum[v]==c&&spectrum[-v]==c;
 for(auto [v,c]:spectrum)if(v!=0&&expected_positive.find(std::abs(v))==expected_positive.end())hist_ok=false;
 if(!pairs_ok||!hist_ok||zeros!=4194816||negatives!=14679808||gap!=4||z1!=0||z2!=12||z3!=200){
  std::cerr<<"FAILED Fourier histogram or low-degree counts\n";return 5;
 }
 // The unique Fourier projection onto the convolution range has spectrum 1_{W!=0}.
 for(auto& v:a)v=(v!=0)?1:0;
 fwht(a);
 int64_t absolute_sum=0;
 for(int32_t v:a)absolute_sum+=std::abs((int64_t)v);
 if(absolute_sum!=2222212096LL){std::cerr<<"FAILED range projection sum "<<absolute_sum<<"\n";return 6;}
 std::cout<<"ONE_MINUS_ASM5_WALSH_PASS\n";
 std::cout<<"ASM_total=429; one_minus=200; dimension=25; zero_modes="<<zeros
          <<"; rank="<<Q-zeros<<"; negative_modes="<<negatives
          <<"; least_nonzero="<<gap<<"; zero_weights_1_2_3="<<z1<<","<<z2<<","<<z3<<"\n";
 std::cout<<"range_projection_abs_sum="<<absolute_sum<<"; norm=2170129/32768\n";
 std::cout<<"zero_pairs_0based=";
 for(auto [p,q]:zero_pairs)std::cout<<"("<<p<<","<<q<<")";
 std::cout<<"\n";
}
