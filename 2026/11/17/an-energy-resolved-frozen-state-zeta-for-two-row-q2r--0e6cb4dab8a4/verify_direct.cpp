// Direct phase-by-phase exhaustive check of 2-by-n Q2R, independent of the transfer construction.
#include <bits/stdc++.h>
using namespace std;
static int bit(uint32_t x,int r,int c,int n) {return (x>>(r*n+c))&1U;}
static uint32_t step(uint32_t x,int n){
    for(int phase=0;phase<2;++phase){
       // Checkerboard colors are (row+column) modulo two.
       for(int r=0;r<2;++r) for(int c=0;c<n;++c) if(((r+c)&1)==phase){
         int up=bit(x,1-r,c,n);
         int k=2*up+bit(x,r,(c+n-1)%n,n)+bit(x,r,(c+1)%n,n);
         if(k==2)x^=(1U<<(r*n+c));
       }
    }
    return x;
}
static int energy(uint32_t x,int n){
    int e=0;
    for(int c=0;c<n;++c){
       e+=2*(bit(x,0,c,n)!=bit(x,1,c,n));
       for(int r=0;r<2;++r)e+=(bit(x,r,c,n)!=bit(x,r,(c+1)%n,n));
    }
    return e;
}
int main(){
 for(int n: {4,6,8,10}){
   uint64_t fixed=0; vector<uint64_t> hist(4*n+1,0);
   for(uint32_t x=0; x<(1U<<(2*n)); ++x){
     if(step(x,n)==x){++fixed;++hist[energy(x,n)];}
   }
   for(int k=0;k<=4*n;++k)if(hist[k]!=hist[4*n-k]){cerr<<"energy-palindrome FAIL n="<<n<<"\n"; return 1;}
   cout<<"n="<<n<<" fixed="<<fixed<<" energy-hist=";
   for(int k=0;k<=4*n;++k)if(hist[k])cout<<k<<":"<<hist[k]<<",";
   cout<<" palindrome=PASS\n";
 }
 cout<<"ALL PASS\n";
}
