// Exact identifying-code census in Fibonacci cubes, dimensions 1--7.
// C++17; no external dependencies. Compile: g++ -std=c++17 -O3 fib_identifying_verify.cpp -o verify
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;
using U=uint64_t;
struct Graph {
 int n,v; vector<int> words,reflection; vector<U> nb,rows;
 explicit Graph(int d):n(d){
  for(int w=0;w<(1<<n);++w)if(!(w&(w<<1)))words.push_back(w);
  v=(int)words.size(); if(v>63)throw runtime_error("graph too large");
  nb.resize(v);reflection.resize(v);
  for(int i=0;i<v;++i){
   for(int j=0;j<v;++j)if(__builtin_popcount((unsigned)(words[i]^words[j]))<=1)nb[i]|=U(1)<<j;
   int w=0;for(int j=0;j<n;++j)if((words[i]>>j)&1)w|=1<<(n-1-j);
   auto x=find(words.begin(),words.end(),w);if(x==words.end())throw runtime_error("missing reflection");
   reflection[i]=int(x-words.begin());
  }
  for(U r:nb)rows.push_back(r);
  for(int i=0;i<v;++i)for(int j=0;j<i;++j)rows.push_back(nb[i]^nb[j]);
  sort(rows.begin(),rows.end(),[](U a,U b){
   int aa=__builtin_popcountll(a),bb=__builtin_popcountll(b);
   return aa==bb?a<b:aa<bb;
  });rows.erase(unique(rows.begin(),rows.end()),rows.end());
 }
 bool valid(U s)const{
  U seen[64];
  for(int i=0;i<v;++i){
   U x=s&nb[i];if(!x)return false;
   for(int j=0;j<i;++j)if(x==seen[j])return false;
   seen[i]=x;
  }return true;
 }
 U reverse_set(U s)const{
  U t=0;for(int i=0;i<v;++i)if(s>>i&1)t|=U(1)<<reflection[i];return t;
 }
};
struct Result{int best=100,reversible_best=100;U witness=0, rev_witness=0;uint64_t count=0,rev_count=0,at_best_invariant=0;};
Result exhaustive(const Graph &g){
 Result z;
 for(U s=0;s<(U(1)<<g.v);++s){
  int k=__builtin_popcountll(s);
  bool r=g.reverse_set(s)==s;
  if(k>z.best&&(!r||k>z.reversible_best))continue;
  if(!g.valid(s))continue;
  if(k<z.best){z.best=k;z.count=0;z.witness=s;z.at_best_invariant=0;}
  if(k==z.best){z.count++;if(r)z.at_best_invariant++;}
  if(r){if(k<z.reversible_best){z.reversible_best=k;z.rev_count=0;z.rev_witness=s;}
    if(k==z.reversible_best)z.rev_count++;}
 }
 return z;
}
struct Hitting {
 const Graph &g;int K;uint64_t calls=0;unordered_set<U> solutions;
 Hitting(const Graph &gr,int k):g(gr),K(k){}
 int lb(U s)const{
  int z=0;U used=0;
  for(U r:g.rows)if(!(r&s)&&!(r&used)){++z;used|=r;}
  return z;
 }
 void dfs(U s,int k){
  ++calls;if(k>K)return;
  U pivot=0;int n=100;bool has_unmet=false;
  for(U r:g.rows){if(r&s)continue;has_unmet=true;
   int c=__builtin_popcountll(r);
   if(c<n){n=c;pivot=r;if(c<=1)break;}
  }
  if(!has_unmet){solutions.insert(s);return;}
  if(!pivot||k==K)return;
  if(k+lb(s)>K)return;
  vector<pair<int,int>> options;
  for(int i=0;i<g.v;++i)if(pivot>>i&1){
   int score=0;for(U r:g.rows)if(!(r&s)&&(r>>i&1))++score;
   options.push_back({-score,i});
  }
  sort(options.begin(),options.end());
  for(auto [score,i]:options)dfs(s|(U(1)<<i),k+1);
 }
};
Result n7_result(const Graph &g){
 if(find(g.rows.begin(),g.rows.end(),0)!=g.rows.end())throw runtime_error("unexpected twins");
 Hitting lower(g,11);lower.dfs(0,0);
 if(!lower.solutions.empty())throw runtime_error("unexpected order-seven 11-sensor code");
 Hitting equal(g,12);equal.dfs(0,0);
 Result z;z.best=12;z.count=equal.solutions.size();z.reversible_best=100;
 for(U s:equal.solutions){if(!g.valid(s)||__builtin_popcountll(s)!=12)throw runtime_error("invalid solution");
  if(!z.witness)z.witness=s;
  if(g.reverse_set(s)==s)z.at_best_invariant++;
 }
 vector<U> orb;vector<int> used(g.v);
 for(int i=0;i<g.v;++i)if(!used[i]){int j=g.reflection[i];used[i]=used[j]=1;orb.push_back((U(1)<<i)|(U(1)<<j));}
 // An independent exhaustive enumeration of all reversal-invariant selections.
 for(U a=0;a<(U(1)<<orb.size());++a){
  U s=0;for(int j=0;j<(int)orb.size();++j)if(a>>j&1)s|=orb[j];
  int k=__builtin_popcountll(s);if(k>z.reversible_best||!g.valid(s))continue;
  if(k<z.reversible_best){z.reversible_best=k;z.rev_count=0;z.rev_witness=s;}
  if(k==z.reversible_best)z.rev_count++;
 }
 cerr<<"n7_lower_nodes="<<lower.calls<<" n7_equality_nodes="<<equal.calls<<" n7_reverse_orbits="<<orb.size()<<'\n';
 return z;
}
void expect(bool q,const char*s){if(!q)throw runtime_error(s);}
int main(){
 const int min_expected[]={-1,-1,2,3,4,5,8,12};
 const int total_expected[]={0,0,1,6,14,2,18,13};
 const int revmin_expected[]={-1,-1,2,3,4,6,8,12};
 const int revcnt_expected[]={0,0,1,2,2,8,2,5};
 const int inv_expected[]={0,0,1,2,2,0,2,5};
 for(int n=1;n<=7;++n){
  Graph g(n);
  Result r=n==7?n7_result(g):exhaustive(g);
  if(n==1){expect(g.nb[0]==g.nb[1],"Gamma1 twins");cout<<"n=1 vertices=2 not_identifiable\n";continue;}
  expect(r.best==min_expected[n],"minimum incorrect");
  expect(r.count==total_expected[n],"total count incorrect");
  expect(r.reversible_best==revmin_expected[n],"reversal minimum incorrect");
  expect(r.rev_count==revcnt_expected[n],"reversal total count incorrect");
  expect(r.at_best_invariant==inv_expected[n],"invariant optimum count incorrect");
  expect(g.valid(r.witness)&&g.valid(r.rev_witness),"witness invalid");
  cout<<"n="<<n<<" vertices="<<g.v<<" min="<<r.best<<" optima="<<r.count
      <<" reversible_min="<<r.reversible_best<<" reversible_count="<<r.rev_count
      <<" invariant_optima="<<r.at_best_invariant<<" reversal_orbits="<<(r.count+r.at_best_invariant)/2<<'\n';
 }
 cout<<"VERIFY_OK\n";
}
