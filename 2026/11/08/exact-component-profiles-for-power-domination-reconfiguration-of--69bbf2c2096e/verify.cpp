// Standalone reproducibility checks for triangular-graph power domination and TAR connectivity.
// Compile: c++ -std=c++17 -O2 verify.cpp -o verify && ./verify
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>
#include <numeric>
#include <stdexcept>
using namespace std;
static int pc(uint64_t x) {return __builtin_popcountll(x);}
struct Instance {
 int n,m;vector<pair<int,int>> e;vector<uint64_t> nbr;
 explicit Instance(int n):n(n){
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)e.push_back({a,b});
  m=int(e.size());nbr.assign(m,0);
  for(int i=0;i<m;i++)for(int j=0;j<m;j++)if(i!=j){auto [a,b]=e[i];auto[c,d]=e[j];if(a==c||a==d||b==c||b==d)nbr[i]|=(1ull<<j);}
 }
 int isolated(uint64_t mask) const {
  uint64_t supp=0;
  for(int i=0;i<m;i++)if(mask>>i&1){auto[a,b]=e[i];supp|=(1ull<<a)|(1ull<<b);}
  return n-pc(supp);
 }
 bool criterion(uint64_t mask) const {return mask && isolated(mask)<=2;}
 bool direct(uint64_t mask)const{
  if(!mask)return false;
  uint64_t obs=mask,all=(1ull<<m)-1;
  for(int i=0;i<m;i++)if(mask>>i&1)obs|=nbr[i];
  while(obs!=all){uint64_t add=0;
   for(int i=0;i<m;i++)if(obs>>i&1){uint64_t u=nbr[i]&~obs;if(u&&!(u&(u-1)))add|=u;}
   if(!add)break;obs|=add;
  }
  return obs==all;
 }
 bool minimal(uint64_t mask)const{
  if(!criterion(mask))return false;
  for(int i=0;i<m;i++)if(mask>>i&1)if(criterion(mask^(1ull<<i)))return false;
  return true;
 }
 bool structural(uint64_t mask)const{
  if(!criterion(mask))return false;
  int iso=isolated(mask),d[20]={};
  for(int i=0;i<m;i++)if(mask>>i&1){auto[a,b]=e[i];d[a]++;d[b]++;}
  if(iso==1){for(int i=0;i<n;i++)if(d[i]>1)return false;return true;}
  if(iso!=2)return false;
  for(int i=0;i<m;i++)if(mask>>i&1){auto[a,b]=e[i];if(d[a]>1&&d[b]>1)return false;}
  return true;
 }
};
static void generate(const Instance &g,int k,int first,uint64_t mask,vector<vector<uint32_t>>&v){
 if(k==0){if(g.criterion(mask))v[pc(mask)].push_back((uint32_t)mask);return;}
 for(int i=first;i<=g.m-k;i++)generate(g,k-1,i+1,mask|(1ull<<i),v);
}
static pair<long long,long long> components(const Instance &g,const vector<vector<uint32_t>>&v,int k){
 unordered_set<uint32_t> unseen;size_t cap=0;for(int j=0;j<=k;j++)cap+=v[j].size();unseen.reserve(cap*2);
 for(int j=0;j<=k;j++)for(uint32_t mask:v[j])unseen.insert(mask);
 long long comps=0,isolated=0;
 vector<uint32_t> queue;queue.reserve(cap);
 while(!unseen.empty()){
  uint32_t x=*unseen.begin();unseen.erase(x);queue.clear();queue.push_back(x);size_t head=0;
  while(head<queue.size()){
   uint32_t cur=queue[head++];
   for(int i=0;i<g.m;i++){
    uint32_t y=cur^(1u<<i);
    auto it=unseen.find(y);if(it!=unseen.end()){unseen.erase(it);queue.push_back(y);}
   }
  }
  ++comps;if(queue.size()==1)++isolated;
 }
 return {comps,isolated};
}
int main(){
 long long directly=0,tar=0,minimalsets=0;
 for(int n=4;n<=8;n++){
  Instance g(n);int q=(n-1)/2,largest=n-3,top=n-2;
  vector<vector<uint32_t>>v(top+1);
  for(int j=0;j<=top;j++)generate(g,j,0,0,v);
  long long mincounts[20]={};
  for(int j=0;j<=top;j++)for(auto s:v[j]){
   if(g.minimal(s)!=g.structural(s))throw runtime_error("minimal structural mismatch");
   if(g.minimal(s)){mincounts[j]++;minimalsets++;}
   if(n<=6 || (n==7 && j<=5) || (n==8 && j<=4)){
    if(g.criterion(s)!=g.direct(s))throw runtime_error("direct PDS mismatch");
    directly++;
   }
  }
  // Every subset, feasible or not, is checked independently for the smaller orders.
  if(n<=6){
   for(uint64_t mask=0;mask<(1ull<<g.m);mask++){
    if(g.criterion(mask)!=g.direct(mask))throw runtime_error("exhaustive PDS mismatch");
   }
  }
  // For n=7, verify the criterion on all 2^21 subsets directly.
  if(n==7){for(uint64_t mask=0;mask<(1ull<<g.m);mask++){
   if(g.criterion(mask)!=g.direct(mask))throw runtime_error("n=7 PDS mismatch");
  }}
  long long known[9]={}; // independent enumerator: root partitions by recursive star-cover enumeration
  vector<int> freevertex(n);iota(freevertex.begin(),freevertex.end(),0);
  // Enumerate minimal sets independently by assigning root non-isolated component edges.
  // First family is encoded as a set partition into blocks of size >=2 with a designated star center.
  auto rooted=[&](auto&& self,int remaining,uint64_t mask)->void{
   if(remaining==0){known[pc(mask)]++;return;}
   int a=__builtin_ctz((unsigned)remaining),tail=remaining^(1<<a);
   for(int sub=tail;sub;sub=(sub-1)&tail){
    int block=sub|(1<<a);if(pc(block)<2)continue;
    vector<int> w;for(int u=0;u<n;u++)if(block>>u&1)w.push_back(u);
    int choices=pc(block)==2?1:int(w.size());
    for(int j=0;j<choices;j++){
     int center=w[j];uint64_t part=0;
     for(int u:w)if(u!=center){for(int i=0;i<g.m;i++){
      auto[x,y]=g.e[i];if((x==center&&y==u)||(x==u&&y==center)){part|=1ull<<i;break;}
     }}
     self(self,remaining^block,mask|part);
    }
   }
  };
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++){
    int rem=((1<<n)-1)^(1<<a)^(1<<b);
    rooted(rooted,rem,0);
  }
  if(n%2){
   // Count perfect matchings on n-1 roots after choosing the unique isolated root.
   for(int excluded=0;excluded<n;excluded++){
    auto matching=[&](auto&& self,int remaining)->void{
     if(!remaining){known[(n-1)/2]++;return;}
     int a=__builtin_ctz((unsigned)remaining),tail=remaining^(1<<a);
     for(int b=0;b<n;b++)if(tail>>b&1)self(self,tail^(1<<b));
    };
    matching(matching,((1<<n)-1)^(1<<excluded));
   }
  }
  for(int j=q;j<=largest;j++)if(known[j]!=mincounts[j])throw runtime_error("partition count mismatch");
  for(int k=q;k<=top;k++){
   auto [cc,iso]=components(g,v,k);
   long long expected=k==q?known[k]:(k<=largest?known[k]+1:1);
   long long expectediso=k==q?known[k]:(k<=largest?known[k]:0);
   if(cc!=expected||iso!=expectediso)throw runtime_error("component formula mismatch");
   cout<<"n="<<n<<" k="<<k<<" components="<<cc<<" isolated="<<iso<<" ";tar++;
  }
  cout<<"minimal=";for(int k=q;k<=largest;k++)cout<<k<<":"<<known[k]<<",";cout<<"\n";
 }
 cout<<"VERIFY_OK orders=4..8 budget_component_cases="<<tar<<" exact_minimal_sets="<<minimalsets<<" direct_PDS_checked="<<directly<<" full_direct_orders=4..7 matching_partition_counts=PASS components=PASS\n";
}
