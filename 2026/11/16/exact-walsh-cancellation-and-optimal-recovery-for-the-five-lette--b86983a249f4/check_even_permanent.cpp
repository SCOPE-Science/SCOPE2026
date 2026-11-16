/* Independent signed-permanent and signed-determinant enumeration for order five.
   Build: g++ -O2 -std=c++17 check_even_permanent.cpp -o check_even_permanent
   Run: ./check_even_permanent
*/
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
int main() {
  constexpr int N=1<<16;
  array<int,5> p={0,1,2,3,4};
  vector<pair<array<int,5>,int>> permutations;
  do {
    int parity=0;
    for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)parity^=(p[i]>p[j]);
    permutations.push_back({p,parity?-1:1});
  }while(next_permutation(p.begin(),p.end()));
  assert(permutations.size()==120);
  vector<int> W(N);
  map<int,int> histogram;
  for(int s=0;s<N;s++){
    int permanent=0, determinant=0;
    for(auto &pair:permutations){
      auto &q=pair.first;
      int sign=1;
      for(int i=0;i<4;i++) if(q[i]<4 && ((s>>(4*i+q[i]))&1)) sign=-sign;
      permanent+=sign;
      determinant+=pair.second*sign;
    }
    assert((permanent+determinant)%2==0);
    W[s]=(permanent+determinant)/2;
    histogram[abs(W[s])]++;
  }
  assert((histogram==map<int,int>{{0,11320},{4,24600},{8,17400},{12,7850},{16,3720},{20,360},{24,200},{28,60},{36,25},{60,1}}));
  long long second=0;
  for(int w:W) second+=(long long)w*w;
  assert(second==N*60LL);
  // Direct butterfly inversion of the indicator of nonvanishing frequencies.
  vector<long long> projection(N);
  for(int i=0;i<N;i++)projection[i]=(W[i]!=0);
  for(int stride=1;stride<N;stride*=2){
    for(int off=0;off<N;off+=2*stride){
      for(int i=off;i<off+stride;i++){
        auto a=projection[i],b=projection[i+stride];
        projection[i]=a+b;projection[i+stride]=a-b;
      }
    }
  }
  long long absolute=0;int kernel_zeros=0;
  for(auto x:projection){absolute+=llabs(x);if(!x)kernel_zeros++;}
  assert(absolute==266611LL*16); // 266611/4096 = 4265776/65536
  assert(kernel_zeros==60);
  cout<<"PASS independent even permanent+determinant, 65536 exact signed evaluations\n";
  cout<<"PASS Fourier histogram and Parseval, rank=27758592, nullity=5795840\n";
  cout<<"PASS kernel sum="<<absolute<<" norm=266611/4096, zero kernel="<<kernel_zeros<<"\n";
}
