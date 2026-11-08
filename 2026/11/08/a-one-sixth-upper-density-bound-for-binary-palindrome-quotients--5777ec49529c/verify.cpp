// Reproducible arithmetic certificate for binary palindromic quotient density bounds.
// Compile: c++ -O3 -std=c++17 verify.cpp -o verify && ./verify
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
unsigned reverse_bits(unsigned x, unsigned k) {
 unsigned y=0; for(unsigned i=0;i<k;++i){ y=(y<<1)|(x&1u); x>>=1; } return y;
}
unsigned inverse_2power(unsigned x,unsigned mask){
 unsigned y=x; for(unsigned i=0;i<6;++i) y=(y*(2u-x*y))&mask;
 return y;
}
int main(){
 for(unsigned k=3;k<=14;++k){
  unsigned H=1u<<(k-1), Q=2u*H, mask=Q-1;
  vector<unsigned> reversed(Q),inverse(Q), rows(H);
  for(unsigned x=0;x<Q;++x) reversed[x]=reverse_bits(x,k);
  for(unsigned b=H;b<Q;++b){
   inverse[b]=inverse_2power(reversed[b],mask);
   if(((reversed[b]*inverse[b])&mask)!=1u){cerr<<"inverse certificate failed";return 2;}
  }
  for(unsigned t=H;t<Q;++t){
   vector<uint8_t> possible(Q,0);
   for(unsigned b=H;b<Q;++b){
    unsigned lo=t*b,hi=(t+1u)*(b+1u), inv=inverse[b];
    for(unsigned shift=0;shift<=1;++shift){
     unsigned step=H<<shift;
     unsigned a0=max(H,lo/step),a1=min(Q-1,(hi-1)/step);
     for(unsigned a=a0;a<=a1;++a){
      if(max(lo,a*step)<min(hi,(a+1u)*step)){
       unsigned r=(reversed[a]*inv)&mask;
       possible[r]=1;
      }
     }
    }
   }
   for(unsigned r=1;r<Q;r+=2) if(!possible[r]) ++rows[t-H];
  }
  uint64_t T=0;for(auto x:rows)T+=x;
  uint64_t prefix=0, best_num=0,best_den=1;unsigned best_q=0;
  for(unsigned q=0;q<=H;++q){
   uint64_t num=T+prefix,den=uint64_t(Q)*(H+q);
   if(q==0||num*best_den<best_num*den){best_num=num;best_den=den;best_q=q;}
   if(q<H)prefix+=rows[q];
  }
  if(k==14 && !(T==45362298ull && best_q==6493u && best_num==80469557ull && best_den==240599040ull)){cerr<<"width14 density certificate failed"; return 3;}
  auto g=gcd(best_num,best_den);
  cout << "k="<<k<<" T="<<T<<" best_q="<<best_q<<" min="<<best_num/g<<"/"<<best_den/g<<" decimal="<<double(best_num)/best_den<<"\n";
 }
}
