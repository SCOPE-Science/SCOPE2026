// Independent bit-parallel implementation of cyclic Rule 110.
// Compile: c++ -O2 -std=c++17 verify_direct.cpp -o verify_direct && ./verify_direct
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
static unsigned step(unsigned x, unsigned n){
 unsigned mask=(1u<<n)-1u;
 unsigned left=((x<<1)&mask)|(x>>(n-1));
 unsigned right=(x>>1)|((x&1u)<<(n-1));
 return ((~x & right) | (x & ~(left & right)))&mask;
}
static long long lucas(unsigned m){
 long long a=2,b=1;
 if(m==0)return a;
 for(unsigned i=1;i<m;i++){long long c=a+b;a=b;b=c;}
 return b;
}
int main(){
 for(unsigned n=1;n<=20;n++){
  long long observed[6]={};
  unsigned count=1u<<n;
  for(unsigned x=0;x<count;x++){
   unsigned y=x;
   for(unsigned t=1;t<=5;t++){
    y=step(y,n);
    if(y==x)observed[t]++;
   }
  }
  long long expect[6]={};
  expect[1]=1;
  expect[2]=1+4*(n%4==0);
  expect[3]=1+9*(n%9==0);
  expect[4]=expect[2];
  if(n%5==0){
   unsigned m=n/5;
   long long sig=(m%2)?-1:1;
   expect[5]=1+5*( (1ll<<m)+2*sig*lucas(m) );
  } else expect[5]=1;
  for(unsigned t=1;t<=5;t++)
   if(observed[t]!=expect[t]){
    cerr<<"FAIL n="<<n<<" time="<<t<<" observed="<<observed[t]<<" predicted="<<expect[t]<<"\n";
    return 1;
   }
  cout<<"n="<<n<<" fix_t1="<<observed[1]<<" fix_t2="<<observed[2]
      <<" fix_t3="<<observed[3]<<" fix_t4="<<observed[4]
      <<" fix_t5="<<observed[5]<<"\n";
 }
 cout<<"ALL_EXHAUSTIVE_CHECKS_PASS n=1..20\n";
 return 0;
}
