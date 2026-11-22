// Standalone finite cross-check of an Italian domination weight transform.
// Compile: c++ -O3 -std=c++17 verify_all_small.cpp -o verify_all_small
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
using U = unsigned long long;

vector<U> direct(int n, const vector<unsigned>& adj) {
  vector<U> out(4*n+1,0);
  int total=1; for(int i=0;i<2*n;i++) total*=3;
  int f[10];
  for(int z=0;z<total;z++) {
    int t=z, weight=0;
    for(int j=0;j<2*n;j++){f[j]=t%3;t/=3;weight+=f[j];}
    bool ok=true;
    for(int v=0;v<n && ok;v++){
      if(f[n+v]==0 && f[v]<2) {ok=false;break;}
      if(f[v]==0) {
        int sum=f[n+v];
        for(int u=0;u<n;u++) if(adj[v]>>u&1)sum+=f[u];
        if(sum<2)ok=false;
      }
    }
    if(ok)out[weight]++;
  }
  return out;
}
vector<U> formula(int n, const vector<unsigned>& adj) {
  vector<U> ans(4*n+1,0);
  for(unsigned p=0;p<(1u<<n);p++) {
    int a=__builtin_popcount(p), b=0;
    for(int v=0;v<n;v++)if(!(p>>v&1) && (adj[v]&p))b++;
    vector<U> coefficients(2*n+1,0);coefficients[0]=1;
    int degree=0;
    for(int i=0;i<a;i++){
      for(int k=degree+2;k>=0;k--){
        U z=0;
        if(k<=degree)z+=2*coefficients[k];
        if(k>=1 && k-1<=degree)z+=2*coefficients[k-1];
        if(k>=2 && k-2<=degree)z+=coefficients[k-2];
        coefficients[k]=z;
      }
      degree+=2;
    }
    for(int i=0;i<b;i++){
      for(int k=degree+1;k>=1;k--){
        coefficients[k]+=coefficients[k-1];
      }
      degree++;
    }
    for(int k=0;k<=degree;k++)ans[2*n-b+k]+=coefficients[k];
  }
  return ans;
}
int gam(int n,const vector<unsigned>& adj){
  int best=n;
  for(unsigned p=0;p<(1u<<n);p++){
    bool ok=true;
    for(int v=0;v<n;v++)if(!(p>>v&1) && !(adj[v]&p)){ok=false;break;}
    if(ok)best=min(best,__builtin_popcount(p));
  }
  return best;
}
int main(){
  unsigned long long ngraphs=0, tested=0;
  for(int n=1;n<=5;n++) {
    int ne=n*(n-1)/2;
    for(unsigned e=0;e<(1u<<ne);e++){
      vector<unsigned> adj(n,0);
      int b=0;
      for(int u=0;u<n;u++)for(int v=u+1;v<n;v++,b++)if(e>>b&1){adj[u]|=1u<<v;adj[v]|=1u<<u;}
      auto x=direct(n,adj),y=formula(n,adj);
      if(x!=y){cerr<<"COUNTEREXAMPLE n="<<n<<" edge-mask="<<e<<"\n";return 1;}
      int minw=0;while(minw<(int)x.size()&&!x[minw])minw++;
      if(minw!=n+gam(n,adj)){cerr<<"MINIMUM_FAIL n="<<n<<" mask="<<e<<"\n";return 2;}
      U minimum=0;
      int maxbd=n-gam(n,adj);
      for(unsigned p=0;p<(1u<<n);p++){
        int boundary=0;
        for(int v=0;v<n;v++)if(!(p>>v&1)&&(adj[v]&p))boundary++;
        if(boundary==maxbd)minimum+=(U)1<<__builtin_popcount(p);
      }
      if(minimum!=x[minw]){cerr<<"MIN_COUNT_FAIL\n";return 3;}
      ngraphs++;tested+=x.size();
    }
    cout<<"ALL_LABELLED_GRAPHS_ORDER_"<<n<<" PASS\n";
  }
  cout<<"VERIFY_OK graphs="<<ngraphs<<" coefficient_comparisons="<<tested<<"\n";
}
