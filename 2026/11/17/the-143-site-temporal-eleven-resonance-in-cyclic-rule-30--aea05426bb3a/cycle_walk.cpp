// Exact functional-graph enumeration for temporal-period-eleven Rule 30 profiles.
// Compile: g++ -O2 -std=c++17 cycle_walk.cpp -o cycle_walk
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <cassert>
using namespace std;
constexpr int K=11;
constexpr uint32_t MASK=(1u<<K)-1,N=1u<<(2*K);
uint32_t next_pair(uint32_t s){
  uint32_t a=s&MASK, b=s>>K;
  uint32_t shift=(a>>1)|((a&1u)<<(K-1));
  return (shift^(a|b))|(a<<K);
}
string minimum_rotation(const string&s){
  string best=s;
  for(size_t j=1;j<s.size();++j){string z=s.substr(j)+s.substr(0,j);if(z<best)best=z;}
  return best;
}
string time_zero_word(const vector<uint32_t>& states){
 string x;for(int j=int(states.size())-1;j>=0;j--)x+=char('0'+(states[j]&1));
 return minimum_rotation(x);
}
string next_word(const string&x){
 string y=x;int n=x.size();
 for(int i=0;i<n;i++){
  int a=x[(i+n-1)%n]-'0',b=x[i]-'0',c=x[(i+1)%n]-'0';
  y[i]=char('0'+(a^(b|c)));
 }
 return y;
}
void verify_witness(const string &x){
 assert(x.find('1')!=string::npos);
 auto y=x;
 for(int t=1;t<=K;t++){y=next_word(y);if(t<K)assert(y!=x);}
 assert(y==x);
 for(size_t d=1;d<x.size();++d)if(x.size()%d==0){bool smaller=true;
   for(size_t i=0;i<x.size();i++)if(x[i]!=x[i%d]){smaller=false;break;}
   assert(!smaller);
 }
}
int main(){
 vector<uint8_t> mark(N,0);
 vector<uint32_t> trail;trail.reserve(1024);
 map<int,int> counts;map<int,string>witnesses;
 uint64_t scanned=0;
 for(uint32_t s=0;s<N;s++){
  if(mark[s])continue;
  trail.clear();uint32_t u=s;
  while(mark[u]==0){mark[u]=1;trail.push_back(u);u=next_pair(u);}
  if(mark[u]==1){
   vector<uint32_t>cyc;uint32_t v=u;
   do{cyc.push_back(v);v=next_pair(v);}while(v!=u);
   int len=cyc.size();counts[len]++;
   if(len==143||len==275){string word=time_zero_word(cyc);verify_witness(word);witnesses[len]=word;}
  }
  for(uint32_t v:trail){mark[v]=2;scanned++;}
 }
 assert(scanned==N);
 assert((counts==map<int,int>{{1,1},{2,1},{143,1},{275,1}}));
 cout<<"states_checked="<<scanned<<"\n";
 for(auto [len,n]:counts)cout<<"spatial_cycle_length="<<len<<" multiplicity="<<n<<"\n";
 for(auto [len,word]:witnesses){cout<<"witness_"<<len<<"="<<word<<"\n";}
 cout<<"direct_rule30_returns_and_minimal_periods=PASS\n";
}
