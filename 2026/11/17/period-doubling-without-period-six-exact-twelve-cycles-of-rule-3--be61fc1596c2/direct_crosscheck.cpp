// Independent all-pair graph traversal, physical-ring reconstruction and evolution.
// C++17; g++ -O2 -std=c++17 direct_crosscheck.cpp -o crosscheck && ./crosscheck
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;
static vector<uint8_t> evolve(const vector<uint8_t>& x){
 int n=x.size();vector<uint8_t> y(n);
 for(int j=0;j<n;++j)y[j]=x[(j+n-1)%n]^(x[j]|x[(j+1)%n]);
 return y;
}
static int least_time(vector<uint8_t> x,int p){const vector<uint8_t> initial=x;
 for(int t=1;t<=p;t++){x=evolve(x);if(x==initial)return t;}
 throw runtime_error("temporal recurrence invalid");
}
static int least_space(const vector<uint8_t>&x){int n=x.size();for(int d=1;d<=n;++d){if(n%d)continue;bool ok=true;for(int j=0;j<n;++j)if(x[j]!=x[(j+d)%n]){ok=false;break;}if(ok)return d;}throw runtime_error("space");}
static void audit(int p){
 const uint32_t Q=1u<<p,N=Q*Q,mask=Q-1;
 auto step=[&](uint32_t s){uint32_t a=s>>p,b=s&mask, shifted=(a>>1)|((a&1)<<(p-1));
  uint32_t before=shifted;
  for(int t=0;t<p;t++){uint32_t ct=(a>>t)&1,rt=(b>>t)&1,nt=(a>>((t+1)%p))&1;
    uint32_t lt=nt^(ct|rt);if(lt)before|=(1u<<t);else before&=~(1u<<t);
  }
  return (before<<p)|a;
 };
 vector<uint8_t> status(N,0);vector<uint32_t> path;path.reserve(10000);
 map<pair<int,int>,int> classes;
 uint64_t processed=0,periodic=0;
 for(uint32_t s=0;s<N;++s){
  if(status[s])continue;
  path.clear();uint32_t k=s;
  while(!status[k]){status[k]=1;path.push_back(k);k=step(k);}
  if(status[k]==1){vector<uint32_t> cyc;uint32_t v=k;
   do{cyc.push_back(v);v=step(v);}while(v!=k);
   int n=cyc.size();vector<uint8_t> x(n);
   for(int j=0;j<n;++j)x[j]=(cyc[(n-j)%n]>>p)&1u;
   int t=least_time(x,p),sp=least_space(x);
   if(sp!=n)throw runtime_error("spatial primitive mismatch");
   // Check that all time slices and all sites of the reconstructed cylinder match.
   vector<uint8_t> curr=x;
   for(int z=0;z<p;++z){for(int j=0;j<n;++j){uint32_t word=cyc[(n-j)%n]>>p;
     if(curr[j]!=((word>>z)&1u))throw runtime_error("spacetime mismatch");}
    curr=evolve(curr);
   }
   if(curr!=x)throw runtime_error("return mismatch");
   classes[{n,t}]++;periodic+=n;
  }
  for(uint32_t v:path)status[v]=2;
  processed+=path.size();
 }
 if(processed!=N)throw runtime_error("not exhaustive");
 cout<<"height="<<p<<" processed="<<processed<<" cyclic_pairs="<<periodic<<"\n";
 for(auto [key,count]:classes)cout<<"space="<<key.first<<" time="<<key.second<<" component_count="<<count<<"\n";
}
int main(){audit(6);audit(12);}
