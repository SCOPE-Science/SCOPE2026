// Direct complete-state test, independent of the eight-symbol transfer computation.
#include <iostream>
#include <cstdint>
#include <vector>
using namespace std;
uint32_t evolve(uint32_t state,int n){
 uint32_t output=0;
 for(int c=0;c<n;c++)for(int r=0;r<3;r++){
  int here=(state>>(3*c+r))&1;
  int north=(state>>(3*c+(r+1)%3))&1;
  int east=(state>>(3*((c+1)%n)+r))&1;
  if(here+north+east>=2) output|=uint32_t(1)<<(3*c+r);
 }
 return output;
}
int main(){
 for(int n=3;n<=7;n++){
  uint64_t fixed=0,uniform=0,mixed=0;
  for(uint32_t s=0;s<(uint32_t(1)<<(3*n));s++){
   if(evolve(s,n)!=s) continue;
   fixed++;
   bool all_uniform=true,all_mixed=true;
   for(int c=0;c<n;c++){
    int v=(s>>(3*c))&7;
    if(v!=0&&v!=7)all_uniform=false;
    if(v==0||v==7)all_mixed=false;
   }
   if(all_uniform)uniform++;
   else if(all_mixed)mixed++;
   else {cerr<<"FAIL mixed-class state "<<s<<" length "<<n<<"\n";return 1;}
  }
  uint64_t want=uint64_t(1)<<n;
  uint64_t sum=0,binom=1;
  for(int j=0;j<=n;j++){
   if(j%6==0)sum+=binom;
   binom=binom*(n-j)/(j+1); // only called before a final unused iteration
  }
  uint64_t want_mixed=6*sum;
  if(uniform!=want||mixed!=want_mixed){cerr<<"FAIL count length "<<n<<"\n";return 2;}
  cout<<"n="<<n<<" fixed="<<fixed<<" uniform="<<uniform<<" mixed="<<mixed<<"\n";
 }
 cout<<"PASS direct complete-state enumeration for n=3,...,7\n";
}
