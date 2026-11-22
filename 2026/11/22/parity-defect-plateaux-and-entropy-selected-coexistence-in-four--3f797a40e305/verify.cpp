#include <bits/stdc++.h>
using namespace std;
using ll=long long;
ll lucas(int n){ll a=2,b=1;if(n==0)return a;for(int i=2;i<=n;i++){ll c=a+b;a=b;b=c;}return b;}
ll indC(int n,int z){ll c=0; for(int mask=0;mask<(1<<n);++mask){bool ok=true;int k=0;for(int i=0;i<n;i++)if(mask>>i&1){++k;if(mask>>((i+1)%n)&1){ok=false;break;}}if(ok){ll w=1;for(int j=0;j<k;j++)w*=z;c+=w;}}return c;}
int main(){
 for(int n=6;n<=9;n++){
  ll N=1;for(int i=0;i<n+2;i++)N*=4;
  vector<int> v(n+2);vector<int> minp(n+3,100000000);vector<ll> count(n+3);
  for(ll raw=0;raw<N;raw++){
   ll x=raw;int k=0;for(int i=0;i<n+2;i++){v[i]=x%4;x/=4;k+=(v[i]==0);}
   int p=0;for(int i=0;i<n;i++){p+=(v[i]==v[(i+1)%n]);p+=(v[i]==v[n]);p+=(v[i]==v[n+1]);}
   if(p<minp[k]){minp[k]=p;count[k]=1;} else if(p==minp[k])count[k]++;
  }
  auto check=[&](int h,ll expectedE,ll expectedDeg,string tag){ll E=LLONG_MAX,deg=0;for(int k=0;k<=n+2;k++){ll val=minp[k]-(ll)h*k;if(val<E){E=val;deg=count[k];}else if(val==E)deg+=count[k];}if(E!=expectedE||deg!=expectedDeg){cerr<<"FAIL n="<<n<<" h="<<h<<" tag="<<tag<<" observed="<<E<<","<<deg<<" expected="<<expectedE<<","<<expectedDeg<<"\n";exit(1);}cout<<"CHECK n="<<n<<" h="<<h<<" energy="<<E<<" degeneracy="<<deg<<" PASS\n";};
  ll i1=indC(n,1),i2=indC(n,2);if(i1!=lucas(n)||i2!=((1LL<<n)+(n%2?-1:1)))return 2;
  ll d2=3*i2+6*i1;
  if(n%2==0){
   check(0,0,4*((1LL<<n)+2)+24,"zero");
   check(1,-n/2,6*(1LL<<(n/2))+12,"low");
   check(2,-n,d2,"first-boundary");
  } else {
   int r=(n-1)/2; ll pow=1LL<<r;
   check(0,0,4*((1LL<<n)-2),"zero");
   check(1,-r, n*(6*pow+6),"parity-boundary");
   // rational h=3/2 checked with doubled integer field manually
   {ll E=LLONG_MAX,deg=0;for(int k=0;k<=n+2;k++){ll val=2LL*minp[k]-3LL*k;if(val<E){E=val;deg=count[k];}else if(val==E)deg+=count[k];}if(E!=2-3LL*(r+1)||deg!=n*(3*pow+6)){cerr<<"FAIL odd intermediate";return 1;}cout<<"CHECK n="<<n<<" h=3/2 energy2="<<E<<" degeneracy="<<deg<<" PASS\n";}
   check(2,-n,d2,"second-boundary");
  }
  auto halfcheck=[&](int twiceh,ll expectedDoubleEnergy,ll expectedDeg,string tag){
   ll E=LLONG_MAX,deg=0;
   for(int k=0;k<=n+2;k++){
    ll val=2LL*minp[k]-(ll)twiceh*k;
    if(val<E){E=val;deg=count[k];}else if(val==E)deg+=count[k];
   }
   if(E!=expectedDoubleEnergy||deg!=expectedDeg){cerr<<"FAIL half n="<<n<<" h2="<<twiceh<<" got="<<E<<","<<deg<<" expected="<<expectedDoubleEnergy<<","<<expectedDeg<<"\n";exit(1);}
   cout<<"CHECK n="<<n<<" twice_field="<<twiceh<<" twice_energy="<<E<<" degeneracy="<<deg<<" PASS\n";
  };
  if(n%2==0){halfcheck(1,-n/2,6*(1LL<<(n/2))+12,"low-half");}
  else{halfcheck(1,-(n-1)/2,3LL*n*(1LL<<((n-1)/2)),"low-half");}
  halfcheck(5,2LL*n-5LL*n,9,"middle-half");
  halfcheck(2*n-1,2LL*n-(2LL*n-1)*n,9,"late-half");
  halfcheck(2*n+1,6LL*n-(2LL*n+1)*(n+2),1,"after-half");
  check(3,n-3LL*n,9,"middle");
  check(n,n-1LL*n*n,16,"saturation-boundary");
  check(n+1,3LL*n-1LL*(n+2)*(n+1),1,"saturation");
 }
 cout<<"ALL_ENUMERATION_CHECKS_PASSED\n";
}
