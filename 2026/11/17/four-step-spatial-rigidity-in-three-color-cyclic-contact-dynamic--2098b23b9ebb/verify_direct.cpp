// Independent exhaustive evolution of the original spatial update on labelled 2-by-n rings.
// Build: g++ -std=c++17 -O3 verify_direct.cpp -o verify_direct
// Run: ./verify_direct
#include <cstdio>
#include <vector>
#include <array>
#include <cassert>
using namespace std;
static void advance(const vector<unsigned char>& x,vector<unsigned char>& y,int n){
   for(int p=0;p<2*n;p++){
      int r=p/n,j=p%n;
      unsigned char next=(x[p]+1)%3;
      bool yes=false;
      for(int delta=-1;delta<=1;delta++)for(int rr=0;rr<2;rr++){
         if(delta==0 && rr==r)continue;
         if(x[rr*n+(j+delta+n)%n]==next)yes=true;
      }
      y[p]=yes?next:x[p];
   }
}
int main(){
for(int n=3;n<=7;n++){
   long long configs=1,period1=0,period4=0;
   for(int k=0;k<2*n;k++)configs*=3;
   vector<unsigned char> original(2*n),current(2*n),updated(2*n);
   for(long long code=0;code<configs;code++){
      long long z=code;
      for(int p=0;p<2*n;p++){original[p]=z%3;z/=3;}
      current=original;
      for(int j=1;j<=4;j++){
         advance(current,updated,n);current.swap(updated);
         if(j==1 && current==original)period1++;
         if(j==4 && current==original)period4++;
      }
   }
   assert(period1==3);
   assert(period4==(n%4==0?27:3));
   printf("n=%d states=%lld fix1=%lld fix4=%lld least4=%lld\n",n,configs,period1,period4,period4-period1);
}
}
