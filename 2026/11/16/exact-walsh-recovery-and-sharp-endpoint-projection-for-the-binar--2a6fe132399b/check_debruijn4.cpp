// Exact census of rooted binary order-four de Bruijn words and their Boolean Fourier projection.
// C++17: g++ -std=c++17 -O2 -Wall -Wextra check_debruijn4.cpp -o check && ./check
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
static constexpr int N=16, Q=1<<N;
static uint16_t rotate_word(uint16_t w,int r){
  if(!r)return w;
  return uint16_t((unsigned(w)<<r)|(unsigned(w)>>(N-r)));
}
static bool debruijn(uint16_t w){
  uint32_t seen=0;
  for(int i=0;i<N;i++){
    int pattern=0;
    for(int j=0;j<4;j++)pattern|=((w>>((i+j)%N))&1)<<j;
    if(seen&(1u<<pattern))return false;
    seen|=1u<<pattern;
  }
  return seen==65535u;
}
static void fwht(vector<int64_t>& a){
  for(int len=1;len<Q;len*=2){
    for(int i=0;i<Q;i+=2*len){
      for(int j=0;j<len;j++){
        int64_t x=a[i+j],y=a[i+j+len];
        a[i+j]=x+y;
        a[i+j+len]=x-y;
      }
    }
  }
}
static void demand(bool yes,const char* name){
  if(!yes){cerr<<"FAILED "<<name<<"\n";exit(2);}
}
int main(){
  // Direct independent exhaustive test of every word.
  set<uint16_t> brute;
  for(int w=0;w<Q;w++)if(debruijn(uint16_t(w)))brute.insert(uint16_t(w));
  demand(brute.size()==256,"rooted-word cardinality");
  // Independent state-transition enumeration of all de Bruijn necklaces.
  // State bit 0 is the oldest bit. Feedback is b0 xor g(b1,b2,b3).
  set<uint16_t> feedback_words;
  int valid_rules=0;
  for(int rule=0;rule<256;rule++){
    int state=0;
    uint32_t visited=0;
    uint16_t word=0;
    bool repeated=false;
    for(int i=0;i<N;i++){
      if(visited&(1u<<state)){repeated=true;break;}
      visited|=1u<<state;
      word|=uint16_t(state&1)<<i;
      int fresh=(state&1)^((rule>>(state>>1))&1);
      state=(state>>1)|(fresh<<3);
    }
    if(!repeated && state==0 && visited==65535u){
      valid_rules++;
      for(int r=0;r<N;r++)feedback_words.insert(rotate_word(word,r));
    }
  }
  demand(valid_rules==16,"feedback-rule cardinality");
  demand(feedback_words==brute,"independent enumeration equality");
  vector<int64_t> W(Q,0);
  for(uint16_t w:brute)W[w]=1;
  fwht(W);
  // Direct signed enumeration at EVERY one of the 2^16 frequencies.
  for(int u=0;u<Q;u++){
    int64_t count=0;
    for(uint16_t w:feedback_words)
      count+=__builtin_parity(unsigned(u)&w)?-1:1;
    demand(count==W[u],"independent full Fourier transform");
  }
  map<int64_t,int64_t> freq;
  int64_t weighted_energy=0;
  int zero=0,odd_zero=0,min_abs=Q;
  for(int u=0;u<Q;u++){
    freq[W[u]]++;
    weighted_energy+=W[u]*W[u];
    if(!W[u]){zero++;if(__builtin_parity(unsigned(u)))odd_zero++;}
    else min_abs=min<int64_t>(min_abs,abs(W[u]));
    demand(W[u]%16==0,"sixteen-fold divisibility");
  }
  demand(weighted_energy==int64_t(Q)*256,"Fourier Parseval");
  demand(zero==42022 && odd_zero==32768,"nullity and complement symmetry");
  demand(min_abs==16 && W[0]==256,"sharp nonzero spectral gap");
  const map<int64_t,int64_t> required={
    {-96,64},{-80,32},{-64,96},{-48,1088},{-32,2640},
    {-16,7872},{0,42022},{16,7744},{32,2576},
    {48,1184},{64,216},{256,2}};
  demand(freq==required,"complete signed Walsh histogram");
  // Complete pair-character classification, including 48 local zeros.
  const array<int,9> lag={0,0,0,0,-96,16,-16,-48,32};
  int zero_pairs=0;
  for(int i=0;i<N;i++)for(int j=i+1;j<N;j++){
    int d=min(j-i,N-(j-i));
    int64_t coeff=W[(1<<i)|(1<<j)];
    demand(coeff==lag[d],"position-independent two-point law");
    if(!coeff)zero_pairs++;
  }
  demand(zero_pairs==48,"exact pair-character zeros");
  // The inverse Walsh transform of the Fourier support is the canonical
  // translation-invariant range projection kernel. Its L1 norm is sharp
  // among all bounded projections by averaging over group translations.
  vector<int64_t> K(Q,0);
  for(int u=0;u<Q;u++)K[u]=bool(W[u]);
  fwht(K);
  int64_t abs_sum=0;
  for(int u=0;u<Q;u++)abs_sum+=abs(K[u]);
  demand(K[0]==23514,"range rank and kernel origin");
  demand(abs_sum==2520272,"projection norm numerator");
  demand(accumulate(K.begin(),K.end(),int64_t(0))==Q,"kernel sum");
  cout<<"DEBRUIJN4_FOURIER_PASS rooted="<<brute.size()
      <<" feedback_rules="<<valid_rules
      <<" zeros="<<zero
      <<" rank="<<(Q-zero)
      <<" gap="<<min_abs
      <<" odd_zeros="<<odd_zero
      <<" pair_zeros="<<zero_pairs
      <<" projection_abs_sum="<<abs_sum
      <<" projection_denominator="<<Q<<"\n";
}
