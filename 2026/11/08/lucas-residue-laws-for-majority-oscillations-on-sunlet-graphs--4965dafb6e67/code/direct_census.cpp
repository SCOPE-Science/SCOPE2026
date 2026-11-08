#include <cstdint>
#include <iostream>
#include <stdexcept>
using u64=std::uint64_t;
static u64 step(u64 state,int n){
  u64 mask=(1ULL<<n)-1ULL;
  u64 a=state&mask, b=(state>>n)&mask;
  u64 left=((a<<1)|(a>>(n-1)))&mask;
  u64 right=((a>>1)|(a<<(n-1)))&mask;
  u64 next=(left&right)|(left&b)|(right&b);
  return next|(a<<n);
}
static u64 lucas(int n){
  u64 a=2,b=1;
  for(int j=0;j<n;j++){u64 c=a+b;a=b;b=c;}
  return a;
}
static int epsilon(int n){int a[]={2,1,-1,-2,-1,1};return a[n%6];}
static int delta(int n){return n%3==0?2:-1;}
static u64 expectedP(int n){
  if(n%2) return lucas(2*n)+delta(n);
  if(n%6==0) return lucas(2*n)+6+4*lucas(n);
  return lucas(2*n)+3-2*lucas(n);
}
int main(){
  for(int n=3;n<=11;n++){
    const u64 all=(1ULL<<(2*n)); const u64 mask=(1ULL<<n)-1;
    u64 F=0,P=0,Q=0;
    for(u64 state=0;state<all;state++){
      u64 first=step(state,n);
      if(first==state)F++;
      if(step(first,n)==state){
        P++;
        if(((first^state)&mask)==mask && (((first^state)>>n)&mask)==mask)Q++;
      }
    }
    u64 f=lucas(n)+epsilon(n), p=expectedP(n),q=lucas(n)+delta(n);
    if(F!=f||P!=p||Q!=q||(P-F)%2||Q%2)
      throw std::runtime_error("finite periodic state census mismatch");
    std::cout<<"n="<<n<<" states="<<all<<" fixed="<<F
             <<" periodic="<<P<<" pure_period_two_states="<<Q
             <<" primitive_two_cycles="<<(P-F)/2<<" OK\n";
  }
}
