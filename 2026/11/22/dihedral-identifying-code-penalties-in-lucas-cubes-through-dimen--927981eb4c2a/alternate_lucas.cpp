// Independent signature-based enumerator for finite Lucas-cube identifying codes.
// Requires only C++17 and standard library. Compile: g++ -O3 -std=c++17 alternate_lucas.cpp -o alt && ./alt
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;

vector<string> words(int n){
 vector<string> out;
 for(int z=0;z<(1<<n);++z){
  string s(n,'0');for(int j=0;j<n;++j)if((z>>j)&1)s[j]='1';
  bool allowed=true;
  for(int j=0;j<n;++j)if(s[j]=='1'&&s[(j+1)%n]=='1')allowed=false;
  if(allowed)out.push_back(s);
 }
 return out;
}
vector<uint32_t> signatures(const vector<string>& w){
 vector<uint32_t> out(w.size());
 for(size_t i=0;i<w.size();i++)for(size_t j=0;j<w.size();j++){
  int diff=0;for(size_t t=0;t<w[i].size();t++)diff+=w[i][t]!=w[j][t];
  if(diff<=1)out[i]|=uint32_t(1)<<j;
 }
 return out;
}
bool valid(uint32_t bits,const vector<uint32_t>& balls){
 uint32_t seen[40];int len=0;
 for(uint32_t b:balls){
  uint32_t signature=b&bits;
  if(signature==0)return false;
  for(int i=0;i<len;i++)if(seen[i]==signature)return false;
  seen[len++]=signature;
 }
 return true;
}
// Generate fixed-popcount masks recursively, unlike the Gosper-order primary enumerator.
void enumeration(int m,int k,int start,uint32_t chosen,const vector<uint32_t>& balls,vector<uint32_t>& solutions){
 if(k==0){if(valid(chosen,balls))solutions.push_back(chosen);return;}
 for(int i=start;i<=m-k;i++)enumeration(m,k-1,i+1,chosen|(uint32_t(1)<<i),balls,solutions);
}
vector<vector<int>> group_action(const vector<string>& w){
 const int m=w.size(),n=w[0].size();vector<vector<int>> out;
 for(int shift=0;shift<n;shift++)for(int reflect=0;reflect<2;reflect++){
  vector<int> p;
  for(const string& x:w){
   string z(n,'0');
   for(int t=0;t<n;t++)z[t]=x[(shift+(reflect?n-t:t))%n];
   auto i=find(w.begin(),w.end(),z);
   assert(i!=w.end());p.push_back(i-w.begin());
  }out.push_back(p);
 }return out;
}
uint32_t transport(uint32_t bits,const vector<int>& p){
 uint32_t out=0;
 for(size_t i=0;i<p.size();++i)if((bits>>i)&1)out|=uint32_t(1)<<p[i];
 return out;
}
int main(){
 const int optimal[]={0,0,2,3,4,5,7,11};
 const int counts[]={0,0,1,4,13,21,18,259};
 const int symmetric_min[]={0,0,2,3,4,5,8,14};
 const int symmetric_counts[]={0,0,1,1,1,1,1,3};
 const vector<map<int,int>> expected={{},{},{ {1,1} },{{1,1},{3,1}},{{1,1},{4,1},{8,1}},{{1,1},{5,2},{10,1}},{{6,1},{12,1}},{{7,9},{14,14}}};
 for(int n=2;n<=7;++n){
  auto w=words(n);auto balls=signatures(w);int m=w.size();
  vector<uint32_t> small,solutions;
  enumeration(m,optimal[n]-1,0,0,balls,small);
  if(!small.empty()){cerr<<"Lower bound failed n="<<n<<'\n';return 1;}
  enumeration(m,optimal[n],0,0,balls,solutions);
  if((int)solutions.size()!=counts[n]){cerr<<"Count failed n="<<n<<" count="<<solutions.size()<<'\n';return 1;}
  auto actions=group_action(w);
  set<uint32_t> todo(solutions.begin(),solutions.end());map<int,int> hist;
  while(!todo.empty()){
   uint32_t seed=*todo.begin();set<uint32_t> orb;
   for(const auto& p:actions)orb.insert(transport(seed,p));
   hist[(int)orb.size()]++;
   for(uint32_t x:orb)if(!todo.erase(x)){cerr<<"Orbit closure failure";return 1;}
  }
  if(hist!=expected[n]){cerr<<"Orbit counts failed n="<<n<<'\n';return 1;}
  set<uint32_t> vertex_unseen;
  for(int i=0;i<m;i++)vertex_unseen.insert(i);
  vector<uint32_t> blocks;
  while(!vertex_unseen.empty()){
   int x=*vertex_unseen.begin();uint32_t O=0;
   for(const auto& p:actions)O|=uint32_t(1)<<p[x];
   blocks.push_back(O);
   for(int i=0;i<m;i++)if((O>>i)&1)vertex_unseen.erase(i);
  }
  int minimum=999,number=0;
  for(int z=0;z<(1<<blocks.size());z++){
   uint32_t code=0;for(size_t i=0;i<blocks.size();i++)if((z>>i)&1)code|=blocks[i];
   if(!valid(code,balls))continue;
   int sz=__builtin_popcount(code);
   if(sz<minimum){minimum=sz;number=1;}else if(sz==minimum)number++;
  }
  if(minimum!=symmetric_min[n]||number!=symmetric_counts[n]){
   cerr<<"Invariant failure n="<<n<<'\n';return 1;
  }
  cout<<"dimension="<<n<<" min="<<optimal[n]<<" codes="<<counts[n]<<" invariant_min="<<minimum<<" invariant_codes="<<number<<'\n';
 }
 cout<<"ALTERNATE_OK\n";
}
