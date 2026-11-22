// Reproducible exact-integer check of excedance-position Fourier spectra.
// Compile: g++ -std=c++17 -O2 verify.cpp -o verify && ./verify
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <cmath>
#include <limits>
#include <numeric>
#include <vector>
using namespace std;
using i64=long long;
using i128=__int128_t;
const i64 UNSET = numeric_limits<i64>::min();
vector<vector<i64>> memo(19);
int removebit(int mask,int k){return (mask & ((1<<k)-1))|((mask>>(k+1))<<k);}
i64 word_count(int length,int mask){
 if(!length)return 1;
 i64 &v=memo[length][mask];
 if(v!=UNSET)return v;
 if(!(mask&1))return v=word_count(length-1,mask>>1);
 if(mask&(1<<(length-1)))return v=word_count(length-1,mask&((1<<(length-1))-1));
 for(int i=0;i<length-1;i++){
   if((mask&(1<<i)) && !(mask&(1<<(i+1)))){
     int swap_mask=mask^(3<<i);
     return v=word_count(length,swap_mask)+word_count(length-1,removebit(mask,i+1))
               +word_count(length-1,removebit(mask,i));
   }
 }
 assert(false);return 0;
}
vector<i64> via_words(int n){
 int L=n-1;vector<i64> a(1<<L);
 for(int mask=0;mask<(1<<L);mask++)a[mask]=word_count(L,mask);
 for(int i=0;i<L;i++)for(int start=0;start<(1<<L);start+=2<<i)
   for(int j=0;j<(1<<i);j++){
     i64 x=a[start+j],y=a[start+j+(1<<i)];
     a[start+j]=x+y;
     a[start+j+(1<<i)]=x-y;
   }
 return a;
}
i64 via_rooks(int n,int mask){
 i128 fact[20]={1};for(int j=1;j<=n;j++)fact[j]=fact[j-1]*j;
 i128 coef[20]={1};int k=0;
 for(int i=n-2;i>=0;i--)if(mask&(1<<i)){
  int allowed=n-i-1;
  for(int j=k+1;j>=1;j--)coef[j]+=(allowed-j+1)*coef[j-1];
  k++;
 }
 i128 ans=0,power=1;
 for(int j=0;j<=k;j++){
  ans+=power*coef[j]*fact[n-j];power*=-2;
 }
 assert(ans>=-(i128)fact[n] && ans<=fact[n]);
 return (i64)ans;
}
int reverse_bits(int x,int L){int y=0;for(int i=0;i<L;i++)if(x&(1<<i))y|=1<<(L-1-i);return y;}
int main(){
 for(int L=0;L<=18;L++)memo[L].assign(1<<L,UNSET);
 const vector<int> wanted_zeros19={850,1353,4388,5716,8348,9570,10824,11300,
  18768,21013,37072,37408,43424,44162,58384,66772,72336,76544,
  131225,150144,156673,172328,175543,243413};
 const vector<int> wanted_nullity={0,0,1,0,2,2,4,0,8,4,18,0,32,14,76,0,130,24,288,24};
 for(int n=1;n<=19;n++){
  int L=n-1;
  auto F=via_words(n);
  int z=0;int positives=0, negatives=0; i64 smallest=std::numeric_limits<i64>::max();int smallest_mask=-1; vector<int> zeros;
  for(int mask=0;mask<(1<<L);mask++){
    if(F[mask]==0){z++;zeros.push_back(mask);}else { if(F[mask]>0)positives++;else negatives++; i64 av=F[mask]>0?F[mask]:-F[mask]; if(av<smallest){smallest=av;smallest_mask=mask;}}
    assert(F[mask]==via_rooks(n,mask));
    // Duality of excedance words: f(w)=f(reverse complement w).
    int dual=((1<<L)-1)^reverse_bits(mask,L);
    assert(word_count(L,mask)==word_count(L,dual));
    // Fourier consequence: F(S)=(-1)^|S| F(reverse S).
    assert(F[mask]==((__builtin_popcount((unsigned)mask)%2)?-F[reverse_bits(mask,L)]:F[reverse_bits(mask,L)]));
  }
  assert(z==wanted_nullity[n]);
  if(n==19)assert(zeros==wanted_zeros19);
  if(n==3||n==7||n==11||n==15)assert(z==0);
  if(n==19){assert(z==24);assert(positives==131048);assert(negatives==131072);assert(smallest==3403284480LL);assert(smallest_mask==59359);}
  if(n<=8){
    vector<i64> direct(1<<L);vector<int> p(n);iota(p.begin(),p.end(),1);
    do {int word=0;for(int i=0;i<n-1;i++)if(p[i]>i+1)word|=1<<i;direct[word]++;}while(next_permutation(p.begin(),p.end()));
    for(int mask=0;mask<(1<<L);mask++)assert(direct[mask]==word_count(L,mask));
  }
  cout <<"n="<<n<<" dimension="<<L<<" nullity="<<z<<" rank="<<(1<<L)-z<<"\n";
 }
 cout<<"PASS: all exact Walsh coefficients by two independent methods for 1<=n<=19.\n";
}
