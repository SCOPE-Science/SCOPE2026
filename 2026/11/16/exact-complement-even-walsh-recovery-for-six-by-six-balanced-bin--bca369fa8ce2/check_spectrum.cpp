// Exact finite verification for binary 6x6 tables of row and column sum 3.
// Compile: g++ -O3 -std=c++17 check_spectrum.cpp -o check_spectrum
#include <algorithm>
#include <array>
#include <cassert>
#include <climits>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
constexpr int N = 6, D = 25, LENGTH = 1 << D;
int main() {
  vector<int32_t> a(LENGTH, 0);
  vector<int> row_masks;
  for (int x=0; x<(1<<N); ++x)
    if (__builtin_popcount((unsigned)x)==3) row_masks.push_back(x);
  array<int,N> left{3,3,3,3,3,3};
  int64_t tables=0;
  auto enumerate = [&](auto &&self, int r, uint32_t signature)->void {
    if(r==N){
      for(int v:left) if(v!=0) return;
      ++a[signature]; ++tables; return;
    }
    for(int row:row_masks){
      bool admissible=true;
      for(int c=0;c<N;c++) if(((row>>c)&1) && !left[c]){admissible=false;break;}
      if(!admissible) continue;
      for(int c=0;c<N;c++) left[c]-=(row>>c)&1;
      uint32_t next=signature;
      if(r>0) for(int c=1;c<N;c++) if((row>>c)&1)
        next|=uint32_t(1) << (5*(r-1)+c-1);
      self(self,r+1,next);
      for(int c=0;c<N;c++) left[c]+=(row>>c)&1;
    }
  };
  enumerate(enumerate,0,0);
  assert(tables==297200);
  for(int k=0;k<D;k++){
    int step=1<<k;
    for(int start=0;start<LENGTH;start+=2*step)
      for(int i=0;i<step;i++){
        int32_t p=a[start+i],q=a[start+i+step];
        a[start+i]=p+q; a[start+i+step]=p-q;
      }
  }
  int64_t zeros=0,zero_even=0,zero_odd=0,nonzero_even=0,wrong_residue=0;
  int minabs=INT_MAX; int64_t sumsq=0;
  uint32_t first_min=0;
  for(int u=0;u<LENGTH;u++){
    int v=a[u]; sumsq+=(int64_t)v*v;
    bool odd=__builtin_parity((unsigned)u);
    if(v==0){++zeros;if(odd)++zero_odd;else ++zero_even;}
    else {if(!odd)++nonzero_even;if(abs(v)<minabs){minabs=abs(v);first_min=u;}}
    if(!odd && ((v%32)+32)%32!=16) ++wrong_residue;
    if(odd && v) {cerr<<"Nonzero odd character"<<endl;return 2;}
  }
  assert(zeros==(1LL<<24) && zero_even==0 && zero_odd==(1LL<<24));
  assert(nonzero_even==(1LL<<24) && wrong_residue==0 && minabs==16);
  assert(sumsq==(1LL<<D)*tables);
  cout<<"tables="<<tables<<" characters="<<LENGTH<<" zeros="<<zeros
      <<" all_even_residue=16_mod_32 min_nonzero="<<minabs
      <<" first_min_frequency="<<first_min
      <<" parseval="<<sumsq<<" PASS\n";
}
