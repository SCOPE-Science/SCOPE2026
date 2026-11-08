// Exact enumeration of universal cycles for the cyclic no-11 language.
// Compile: g++ -std=c++17 -O2 count_cycles.cpp -o count_cycles
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <numeric>
#include <cassert>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using boost::multiprecision::cpp_int;
using ll=long long;

bool prime(int v) {
 if(v<2) return false;
 for(int d=2; (ll)d*d<=v; ++d) if(v%d==0) return false;
 return true;
}
ll modpow(ll a,ll b,ll p){ll v=1;for(;b;b>>=1,a=a*a%p)if(b&1)v=v*a%p;return v;}
ll detmod(const vector<vector<int>>& lap,int p) {
 const int m=(int)lap.size()-1;
 vector<vector<ll>> a(m,vector<ll>(m));
 for(int i=1;i<=m;++i) for(int j=1;j<=m;++j) a[i-1][j-1]=(((ll)lap[i][j]%p+p)%p);
 ll det=1;
 for(int k=0;k<m;++k){
  int pivot=k;while(pivot<m&&a[pivot][k]==0)++pivot;
  if(pivot==m)return 0;
  if(pivot!=k){swap(a[pivot],a[k]);det=(p-det)%p;}
  ll z=a[k][k];det=det*z%p;
  ll iz=modpow(z,p-2,p);
  for(int i=k+1;i<m;++i){
   if(a[i][k]==0)continue;
   ll f=a[i][k]*iz%p; a[i][k]=0;
   for(int j=k+1;j<m;++j){
    ll diff=(a[i][j]-f*a[k][j])%p;
    if(diff<0)diff+=p;
    a[i][j]=diff;
   }
  }
 }
 return det;
}

cpp_int count(int n,int &branches,int &windows) {
 if(n==2){branches=1;windows=3;return 1;}
 const int len=n-1, mask=(1<<len)-1, hi=1<<(len-1);
 vector<int> B;
 for(int v=0;v<=mask;++v)
  if(!(v&hi)&&!(v&1)&&!(v&(v>>1))) B.push_back(v);
 branches=(int)B.size();
 map<int,int> idx;
 for(int i=0;i<branches;++i)idx[B[i]]=i;
 assert(B[0]==0);
 vector<vector<int>> lap(branches,vector<int>(branches,0));
 for(int i=0;i<branches;++i) for(int bit=0;bit<=1;++bit){
  int curr=((B[i]<<1)|bit)&mask;
  int steps=0;
  while((curr&hi)||(curr&1)){
   curr=(curr<<1)&mask;
   assert(++steps<=len);
  }
  assert(idx.find(curr)!=idx.end());
  ++lap[i][i];--lap[i][idx[curr]];
 }
 windows=0;
 for(int w=0;w<(1<<n);++w) if(!(w&(w>>1)) && !((w&1)&&(w&(1<<(n-1))))) ++windows;
 // Each non-root branch has two outgoing edges; tree count at most 2^(branches-1).
 cpp_int limit=cpp_int(1) << (branches-1);
 cpp_int x=0,product=1;
 int p=2147483647;
 while(product<=limit){
  while(!prime(p))p-=2;
  ll r=detmod(lap,p);
  ll xm=(x%p).convert_to<ll>(), pm=(product%p).convert_to<ll>();
  ll t=(r-xm+p)%p *modpow(pm,p-2,p)%p;
  x+=product*t;
  product*=p;
  p-=2;
 }
 assert(x>=0&&x<=limit);
 return x;
}
int main(int argc,char**argv){
 int top=argc>1?stoi(argv[1]):15;
 for(int n=2;n<=top;++n){
  int branches,windows;
  cpp_int ans=count(n,branches,windows);
  cout<<n<<","<<windows<<","<<branches<<","<<ans<<"\n";
 }
}
