// Exact low-degree Walsh cancellation census for convex-polygon noncrossing perfect matchings.
// Compile: c++ -std=c++17 -O2 noncrossing_walsh_checker.cpp -o check && ./check
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;

struct Census {
 int n,N,m,maxdegree;
 vector<pair<int,int>> edges;
 int index[16][16]{};
 vector<vector<int>> perms;
 long long zero_by_degree[5]{};
 long long zero_stars=0,zero_brooms=0,zero_other=0;
 long long representatives=0, zero_orbits=0;
 vector<pair<int,vector<pair<int,int>>>> zero_reps;
 Census(int n_):n(n_),N(2*n_),maxdegree(n_/2) {
  if(n_<2||n_>8||n_%2)throw runtime_error("n must be even between 2 and 8");
  for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)if((b-a)%2==1){
   index[a][b]=index[b][a]=edges.size()+1;
   edges.emplace_back(a,b);
  }
  m=edges.size();
  assert(m==n*n&&m<=64);
  for(int sign: {1,-1})for(int shift=0;shift<N;shift++) {
   vector<int> p(m);
   for(int i=0;i<m;i++){
    int a=(sign*edges[i].first+shift+N)%N;
    int b=(sign*edges[i].second+shift+N)%N;
    p[i]=index[a][b]-1;
    assert(p[i]>=0);
   }
   perms.push_back(p);
  }
 }
 uint64_t change(const vector<int>& chosen,const vector<int>&p)const {
  uint64_t z=0;
  for(int a:chosen)z|=uint64_t(1)<<p[a];
  return z;
 }
 long long value(uint64_t S)const{
  long long dp[17][17]{};
  for(int a=0;a<=N;a++)dp[a][a]=1;
  for(int len=2;len<=N;len+=2)for(int a=0;a+len<=N;a++){
   int b=a+len;
   for(int j=a+1;j<b;j+=2){
    int i=index[a][j]-1;
    assert(i>=0);
    int sign=((S>>i)&1)?-1:1;
    dp[a][b]+=sign*dp[a+1][j]*dp[j+1][b];
   }
  }
  return dp[0][N];
 }
 void visit(const vector<int>&chosen) {
  uint64_t S=0;
  for(int i:chosen)S|=uint64_t(1)<<i;
  uint64_t mn=S;
  set<uint64_t> orbit;
  for(const auto&p:perms){uint64_t t=change(chosen,p);mn=min(mn,t);orbit.insert(t);}
  if(S!=mn)return;
  representatives++;
  if(value(S)!=0)return;
  int d=chosen.size();
  zero_by_degree[d]+=orbit.size();
  if(d==maxdegree){
   zero_orbits++;
   map<int,int> degrees;
   vector<pair<int,int>> ex;
   for(int i:chosen){auto e=edges[i]; degrees[e.first]++;degrees[e.second]++;ex.push_back(e);}
   vector<int> shape;
   for(auto kv:degrees)shape.push_back(kv.second);
   sort(shape.rbegin(),shape.rend());
   if(d==4 && shape==vector<int>({4,1,1,1,1}))zero_stars+=orbit.size();
   else if(d==4 && shape==vector<int>({3,2,1,1,1}))zero_brooms+=orbit.size();
   else if(d==4)zero_other+=orbit.size();
   zero_reps.push_back({orbit.size(),ex});
  }
 }
 void enum_choose(int start,int rem,vector<int>&chosen){
  if(!rem){visit(chosen);return;}
  for(int j=start;j<=m-rem;j++){
   chosen.push_back(j);
   enum_choose(j+1,rem-1,chosen);
   chosen.pop_back();
  }
 }
 void run(){
  for(int d=1;d<=maxdegree;d++){
   vector<int> chosen;
   enum_choose(0,d,chosen);
  }
  cout<<"n="<<n<<" Catalan="<<value(0)<<" edges="<<m;
  for(int d=1;d<=maxdegree;d++)cout<<" zeros_degree_"<<d<<"="<<zero_by_degree[d];
  cout<<"\n";
  if(n==8){
   cout<<"star="<<zero_stars<<" broom="<<zero_brooms<<" other="<<zero_other
       <<" zero_orbits="<<zero_orbits<<"\n";
   assert(value(0)==1430);
   assert(zero_by_degree[1]==0&&zero_by_degree[2]==0&&zero_by_degree[3]==0);
   assert(zero_by_degree[4]==544);
   assert(zero_stars==256&&zero_brooms==288&&zero_other==0&&zero_orbits==17);
   for(auto [sz,es]:zero_reps){
    cout<<"orbit="<<sz;
    for(auto [a,b]:es)cout<<" ("<<a<<","<<b<<")";
    cout<<"\n";
   }
  }
  if(n==4)assert(value(0)==14&&zero_by_degree[1]==0&&zero_by_degree[2]==32);
  if(n==6)assert(value(0)==132&&zero_by_degree[1]==0&&zero_by_degree[2]==0&&zero_by_degree[3]==216);
 }
};
int main(){
 try {for(int n: {4,6,8})Census(n).run();cout<<"NONCROSSING_MATCHINGS_WALSH_EXACT_PASS\n";}
 catch(const exception&e){cerr<<e.what()<<"\n";return 1;}
}
