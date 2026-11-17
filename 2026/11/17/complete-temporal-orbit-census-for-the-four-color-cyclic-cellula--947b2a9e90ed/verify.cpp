// Independent exhaustive checks of exact finite-cycle periodic-point counts.
// g++ -std=c++17 -O3 verify.cpp -o verify && ./verify
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
static unsigned step(unsigned x, int n) {
 unsigned out=0;
 for(int i=0;i<n;i++){
  unsigned c=(x>>(2*i))&3, l=(x>>(2*((i+n-1)%n)))&3,
           r=(x>>(2*((i+1)%n)))&3, next=(c+1)&3;
  unsigned v=(l==next || r==next)?next:c;
  out |= v<<(2*i);
 }
 return out;
}
static uint64_t choose(int n,int k){
 uint64_t p=1;
 for(int j=1;j<=k;j++) p=p*(n-j+1)/j;
 return p;
}
static int gcd0(int a,int b){while(b){int c=a%b;a=b;b=c;}return a;}
static uint64_t theorem(int n,int t){
 int d=gcd0(n,t), v=n/d,w=t/d;
 uint64_t z=1ULL<<(n+1);
 for(int k=1;k<=d;k++)if((v*k)%4==0 && (w*k)%4==0)z+=8*choose(d,k);
 return z;
}
int main(){
 for(int n=3;n<=10;n++){
  uint64_t size=1ULL<<(2*n);vector<uint64_t> hits(n+1,0);
  uint64_t period=0,truth_period=0;
  for(uint64_t x=0;x<size;x++){
   int plus=0,minus=0,stationary=0;
   for(int i=0;i<n;i++){
    int a=(x>>(2*i))&3,b=(x>>(2*((i+1)%n)))&3;
    int d=(b-a+4)%4;
    plus+=d==1;minus+=d==3;stationary+=d==2;
   }
   bool wave=(stationary==0&&(plus==0||minus==0));
   bool frozen=(plus==0&&minus==0);
   bool classified=frozen || (wave&&(plus>0||minus>0));
   truth_period+=classified;
   unsigned y=(unsigned)x;
   if(classified){ /* check first periodic return by n */ }
   for(int t=1;t<=n;t++){
    y=step(y,n);
    if(y==x)hits[t]++;
   }
   bool periodic=(y==x);
   period+=periodic;
   if(periodic != classified){cerr<<"classification fail n="<<n<<" x="<<x<<"\n";return 1;}
  }
  if(period!=truth_period){cerr<<"sector count fail\n";return 1;}
  for(int t=1;t<=n;t++)if(hits[t]!=theorem(n,t)){
   cerr<<"count fail n="<<n<<" t="<<t<<" observed="<<hits[t]<<" expected="<<theorem(n,t)<<"\n";
   return 1;
  }
  cout<<"n="<<n<<" tested="<<size<<" recurrent="<<period<<" fixed="<<hits[1]<<" nth-return="<<hits[n]<<" all t=1..n PASS\n";
 }
}
