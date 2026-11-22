#include <iostream>
#include <vector>
#include <numeric>
using namespace std;
using ll=long long;
static bool theory(int n, int pat, int support) {
  // Pattern represented in left-to-right order as low-to-high bits.
  bool b=(pat==1||pat==3||pat==4||pat==6);
  if(!b){for(int j=0;j+2<n;j++)if(((support>>j)&7)==7)return false;return true;}
  if(pat==1||pat==6){
    bool first=false;
    for(int j=0;j<n;j++)if((support>>j)&1){
      if(first && j+1<n && ((support>>(j+1))&1))return false;
      first=true;
    }
  } else {
    bool later=false;
    for(int j=n-1;j>=0;j--)if((support>>j)&1){
      if(later && j-1>=0 && ((support>>(j-1))&1))return false;
      later=true;
    }
  }
  return true;
}
static ll choose(int n,int k){if(k<0||k>n||n<0)return 0;ll ans=1;for(int i=1;i<=k;i++)ans=ans*(n-i+1)/i;return ans;}
int main(){
 for(int n=0;n<=11;n++){
  int bound=1<<n;
  for(int p=0;p<8;p++){
   vector<int> concepts;
   for(int w=0;w<bound;w++){
    bool ok=true;
    for(int j=0;j+2<n;j++)if(((w>>j)&7)==p){ok=false;break;}
    if(ok)concepts.push_back(w);
   }
   vector<ll> freq(n+1,0);
   for(int mask=0;mask<bound;mask++){
    vector<unsigned char> seen(bound,0);
    int count=0;
    for(int w:concepts){int tr=w&mask;if(!seen[tr]){seen[tr]=1;count++;}}
    int pc=__builtin_popcount((unsigned)mask);
    bool actual=count==(1<<pc);
    if(actual!=theory(n,p,mask)){cerr<<"support FAIL n="<<n<<" pat="<<p<<" mask="<<mask<<"\n";return 1;}
    if(actual)freq[pc]++;
   }
   bool b=(p==1||p==3||p==4||p==6);
   if(b){for(int k=0;k<=n;k++){
    ll wanted=(k==0?1:(k==1?n:choose(n-k+2,k)));
    if(freq[k]!=wanted){cerr<<"coefficient FAIL";return 1;}
   }}
   bool extremal=accumulate(freq.begin(),freq.end(),0LL)==(ll)concepts.size();
   if(extremal!=(n<=3 || p!=2 && p!=5)){cerr<<"extremality FAIL";return 1;}
  }
  cout<<"n="<<n<<": eight patterns, all supports, traces and extremality PASS\n";
 }
 cout<<"CPP_CHECK_PASS\n";
}
