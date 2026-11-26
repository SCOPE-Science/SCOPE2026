// Exact finite-field point-count verifier for a complete-intersection curve.
// Build: g++ -std=c++17 -O2 verify_counts.cpp -o verify_counts && ./verify_counts
#include <array>
#include <cassert>
#include <iostream>
#include <vector>
using namespace std;
int mul(int a,int b,int n,int mod){int p=0,mask=(1<<n)-1;while(b){if(b&1)p^=a;b>>=1;a<<=1;if(a&(1<<n))a^=mod;}return p&mask;}
int main(){
 // These moduli are irreducible over F2 in degrees 1 through 6.
 const int mods[7]={0,3,7,11,19,37,67};
 const int expect[7]={0,5,5,5,29,5,125};
 for(int n=1;n<=6;++n){
   int q=1<<n, mod=mods[n], cnt=0;
   auto oncurve=[&](array<int,4>a)->bool{
     array<int,5> v={a[0],a[1],a[2],a[3],a[0]^a[1]^a[2]^a[3]};
     int e2=0,e3=0;
     for(int i=0;i<5;++i)for(int j=i+1;j<5;++j){
       e2^=mul(v[i],v[j],n,mod);
       for(int k=j+1;k<5;++k)e3^=mul(mul(v[i],v[j],n,mod),v[k],n,mod);
     }
     return e2==0&&e3==0;
   };
   // Every projective point has a unique first-nonzero-coordinate-is-1 representative.
   for(int b=0;b<q;++b)for(int c=0;c<q;++c)for(int d=0;d<q;++d)cnt+=oncurve({1,b,c,d});
   for(int c=0;c<q;++c)for(int d=0;d<q;++d)cnt+=oncurve({0,1,c,d});
   for(int d=0;d<q;++d)cnt+=oncurve({0,0,1,d});
   cnt+=oncurve({0,0,0,1});
   cout << "extension=" << n << " points=" << cnt << " expected=" << expect[n] << '\n';
   if(cnt!=expect[n])return 2;
 }
 cout<<"VERIFY_OK\n";
}
