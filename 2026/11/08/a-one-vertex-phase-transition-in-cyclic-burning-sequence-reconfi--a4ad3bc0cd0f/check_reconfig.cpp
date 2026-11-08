// Direct exhaustive test of burning-sequence slide-reconfiguration theorem.
// All vertices are ordered ignition sequences; slides preserve time labels.
#include <cassert>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>
using namespace std;
long long fact(int k){long long v=1;for(int i=2;i<=k;i++)v*=i;return v;}
int main(){
for(int k=2;k<=5;k++)for(int deficit=0;deficit<=1;deficit++){
 int n=k*k-deficit;
 vector<vector<uint64_t>> B(k,vector<uint64_t>(n));
 for(int i=0;i<k;i++)for(int x=0;x<n;x++)for(int v=0;v<n;v++){
  int d=abs(x-v);d=min(d,n-d);
  if(d<=k-1-i) B[i][x]|=(uint64_t(1)<<v);
 }
 uint64_t full=(uint64_t(1)<<n)-1;
 vector<int> src(k);
 vector<vector<int>> states;
 auto enc=[&](const vector<int>& v)->uint64_t{uint64_t z=0;for(int i=0;i<k;i++)z=z*n+v[i];return z;};
 auto legal=[&](const vector<int>& v)->bool{
  for(int i=0;i<k;i++)for(int j=i+1;j<k;j++){
   int d=abs(v[i]-v[j]);d=min(d,n-d);
   if(d<j-i)return false;
  }
  uint64_t hit=0;for(int i=0;i<k;i++)hit|=B[i][v[i]];
  return hit==full;
 };
 auto rec=[&](auto&&rec,int i)->void{
  if(i==k){if(legal(src))states.push_back(src);return;}
  for(int v=0;v<n;v++){
   bool ok=true;
   for(int j=0;j<i;j++){
    int d=abs(v-src[j]);d=min(d,n-d);if(d<i-j){ok=false;break;}
   }
   if(!ok)continue;
   src[i]=v;rec(rec,i+1);
  }
 };
 rec(rec,0);
 unordered_map<uint64_t,int> ids;ids.reserve(states.size()*2);
 for(int id=0;id<(int)states.size();id++)ids[enc(states[id])]=id;
 vector<vector<int>> adj(states.size());
 for(int a=0;a<(int)states.size();a++)for(int i=0;i<k;i++)for(int s:{-1,1}){
  auto v=states[a];v[i]=(v[i]+s+n)%n;
  auto it=ids.find(enc(v));if(it!=ids.end())adj[a].push_back(it->second);
 }
 vector<int> seen(states.size(),0);int comps=0,lo=100000000,hi=0;long long twiceedges=0;
 for(int a=0;a<(int)states.size();a++){
  twiceedges+=adj[a].size();
  if(deficit==0)assert(adj[a].size()==0);
  else assert(adj[a].size()==2);
  if(seen[a])continue;
  comps++;int sz=0;
  queue<int> q;q.push(a);seen[a]=1;
  while(!q.empty()){int x=q.front();q.pop();sz++;
   for(int y:adj[x])if(!seen[y]){seen[y]=1;q.push(y);}
  }
  lo=min(lo,sz);hi=max(hi,sz);
 }
 long long expected=deficit? (long long)n*fact(k) : (long long)n*fact(k-1);
 int expcomp=deficit?fact(k-1):expected;
 int expsize=deficit?k*n:1;
 cout<<"C"<<n<<" k="<<k<<" states="<<states.size()<<" edges="<<twiceedges/2<<" components="<<comps<<" component_sizes="<<lo<<","<<hi<<"\n";
 assert((long long)states.size()==expected);
 assert(comps==expcomp&&lo==expsize&&hi==expsize);
 }
 cout<<"PASS exhaustive sequence reconfiguration\n";
}
