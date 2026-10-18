// Exact finite discrete-Morse certificate for total cut complexes of squared cycles.
// Compile: g++ -std=c++17 -O3 verify_squared_cycle.cpp -o verify_squared_cycle
// Run: ./verify_squared_cycle 4 8
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <stdexcept>
using namespace std;
static bool allowed(uint32_t mask,int n){
 uint32_t t=mask;
 while(t){
  int i=__builtin_ctz(t);t&=t-1;
  uint32_t v=t;
  while(v){int j=__builtin_ctz(v);v&=v-1;
    int d=j-i;if(d<=2||n-d<=2)return false;
  }
 }
 return true;
}
static void check(int k){
 const int n=3*k+3;
 if(n>27)throw runtime_error("n exceeds 27-bit bound");
 const uint32_t N=1u<<n, universe=N-1;
 vector<uint8_t> live(N,0);
 uint64_t facets=0;
 uint32_t comb=(1u<<k)-1;
 while(comb<N){
  if(allowed(comb,n)){
   ++facets;
   uint32_t f=universe^comb;
   for(uint32_t s=f;;s=(s-1)&f){
    live[s]=1;
    if(s==0)break;
   }
  }
  uint32_t c=comb&-comb, r=comb+c;
  if(!r)break;
  comb=(((r^comb)>>2)/c)|r;
 }
 uint64_t faces=0;int64_t euler=0;
 for(uint32_t mask=0;mask<N;++mask)if(live[mask]){
  ++faces;
  euler+= (__builtin_popcount(mask)%2==0 ? -1 : 1);
 }
 cout<<"k="<<k<<" n="<<n<<" facets="<<facets<<" faces="<<faces
     <<" reduced_euler="<<euler<<"\n"<<flush;
 uint64_t pairs=0;
 for(int vertex=0;vertex<n;++vertex){
  uint32_t bit=1u<<vertex, matched=0;
  // Exhaust all candidate lower faces not containing this vertex.
  for(uint32_t a=0;a<N;++a){
   if(!(a&bit)&&live[a]&&live[a|bit]){
    live[a]=live[a|bit]=0;
    ++matched;
   }
  }
  pairs+=matched;
  cout<<" "<<matched<<flush;
 }
 cout<<"\n";
 uint64_t critical=0;uint32_t critical_mask=0;
 for(uint32_t a=0;a<N;++a)if(live[a]){
  ++critical;critical_mask=a;
 }
 cout<<"critical_count="<<critical<<" critical_mask="<<critical_mask
     <<" critical_dimension="<<__builtin_popcount(critical_mask)-1
     <<" matched_pairs="<<pairs<<"\n"<<flush;
 const uint32_t expected=(1u<<1)|(1u<<2)|(1u<<4)|(1u<<6)|(1u<<8)|(1u<<10)|(1u<<12)|(1u<<14);
 if(critical!=1||critical_mask!=expected||faces!=2*pairs+critical
  ||facets!= (uint64_t)n*(k+2)*(k+1)/6 // n/k * C(k+2,3) = n*(k+2)*(k+1)/6
  ||euler!=(-1))throw runtime_error("Certificate mismatch");
}
int main(int argc,char**argv){
 int low=4,high=8;
 if(argc>1)low=atoi(argv[1]);
 if(argc>2)high=atoi(argv[2]);
 if(low<4||high>8||low>high)throw runtime_error("4<=low<=high<=8 required");
 for(int k=low;k<=high;++k)check(k);
 cout<<"VERIFY_OK"<<endl;
}
