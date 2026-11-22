// Exact finite census of global-maximum-overlap GREEDY on distinct binary 4-mers.
// Compile: c++ -std=c++17 -O3 verify_binary_four.cpp -o verify_binary_four
// Run: ./verify_binary_four
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
static constexpr int K=4, N=16, TOTAL=(1<<N);
static int ov[N][N];
static unordered_map<string,int> memo;
static uint64_t states=0,hits=0;
static string word(int i){string s(4,'0'); for(int b=0;b<4;b++)s[3-b]=char('0'+((i>>b)&1));return s;}
static int strOverlap(const string&a,const string&b){
 for(int t=(int)min(a.size(),b.size());t>0;--t)
  if(a.compare(a.size()-t,t,b,0,t)==0)return t;
 return 0;
}
// One byte records first input 4-mer (high nibble), last input 4-mer (low nibble).
static int minimumGreedyCompression(const vector<uint8_t>&s){
 if(s.size()==1)return 0;
 string ky(s.begin(),s.end());
 auto it=memo.find(ky);
 if(it!=memo.end()){++hits;return it->second;}
 ++states;
 int mx=0;
 for(size_t i=0;i<s.size();i++)for(size_t j=0;j<s.size();j++)
   if(i!=j)mx=max(mx,ov[s[i]&15][s[j]>>4]);
 int result=INT32_MAX;
 set<string> visitedSuccessors;
 for(size_t i=0;i<s.size();i++)for(size_t j=0;j<s.size();j++)if(i!=j){
  if(ov[s[i]&15][s[j]>>4]!=mx)continue;
  vector<uint8_t> t;
  for(size_t z=0;z<s.size();z++)if(z!=i&&z!=j)t.push_back(s[z]);
  t.push_back(uint8_t((s[i]&0xf0)|(s[j]&0x0f)));
  sort(t.begin(),t.end());
  if(!visitedSuccessors.insert(string(t.begin(),t.end())).second)continue;
  result=min(result,mx+minimumGreedyCompression(t));
 }
 assert(result!=INT32_MAX);
 memo.emplace(move(ky),result);
 return result;
}
// Direct subset-optimum Hamiltonian-path DP: maximum overlap compression.
static vector<array<int,N>> optimalDp(){
 vector<array<int,N>> dp(TOTAL);
 for(auto &a:dp)a.fill(-10000);
 for(int i=0;i<N;i++)dp[1<<i][i]=0;
 for(int mask=1;mask<TOTAL;mask++)for(int j=0;j<N;j++)if(mask&(1<<j)){
  int prior=mask^(1<<j);
  if(!prior)continue;
  for(int i=0;i<N;i++)if(prior&(1<<i))
   dp[mask][j]=max(dp[mask][j],dp[prior][i]+ov[i][j]);
 }
 return dp;
}
static int reverse4(int x){int y=0;for(int j=0;j<4;j++)if(x&(1<<j))y|=1<<(3-j);return y;}
static array<int,4> orbitMasks(int mask){
 array<int,4> a={mask,0,0,0};
 for(int i=0;i<N;i++)if(mask&(1<<i)){
  a[1]|=(1<<(i^15)); a[2]|=(1<<reverse4(i));a[3]|=(1<<(reverse4(i)^15));
 }
 return a;
}
struct P{uint8_t code; string s;};
static string greedyWitness(vector<P>nodes){
 if(nodes.size()==1)return nodes[0].s;
 vector<uint8_t> codes;for(auto &p:nodes)codes.push_back(p.code);
 int best=minimumGreedyCompression(codes), mx=0;
 for(size_t i=0;i<nodes.size();i++)for(size_t j=0;j<nodes.size();j++)if(i!=j){
  int actual=strOverlap(nodes[i].s,nodes[j].s);
  int endpoints=ov[nodes[i].code&15][nodes[j].code>>4];
  if(actual!=endpoints){cerr<<"Endpoint invariant failed on witness\n";abort();}
  mx=max(mx,actual);
 }
 for(size_t i=0;i<nodes.size();i++)for(size_t j=0;j<nodes.size();j++)if(i!=j){
  if(strOverlap(nodes[i].s,nodes[j].s)!=mx)continue;
  vector<P> t;
  for(size_t z=0;z<nodes.size();z++)if(z!=i&&z!=j)t.push_back(nodes[z]);
  t.push_back({uint8_t((nodes[i].code&0xf0)|(nodes[j].code&0x0f)),nodes[i].s+nodes[j].s.substr(mx)});
  sort(t.begin(),t.end(),[](const P&a,const P&b){return a.code<b.code;});
  vector<uint8_t> nxt;for(auto&p:t)nxt.push_back(p.code);
  if(mx+minimumGreedyCompression(nxt)==best)return greedyWitness(t);
 }
 abort();
}
// Separate literal-string exhaustive GREEDY calculation on the sharp witness input.
static unordered_map<string,int> directMemo;
static int directWorst(vector<string>s){
 if(s.size()==1)return (int)s[0].size();
 string ky;for(auto&w:s){ky+=w;ky+='|';}
 auto it=directMemo.find(ky);if(it!=directMemo.end())return it->second;
 int mx=0;
 for(size_t i=0;i<s.size();i++)for(size_t j=0;j<s.size();j++)if(i!=j)
  mx=max(mx,strOverlap(s[i],s[j]));
 int worst=0;
 for(size_t i=0;i<s.size();i++)for(size_t j=0;j<s.size();j++)if(i!=j){
  if(strOverlap(s[i],s[j])!=mx)continue;
  vector<string> t;
  for(size_t z=0;z<s.size();z++)if(z!=i&&z!=j)t.push_back(s[z]);
  t.push_back(s[i]+s[j].substr(mx));sort(t.begin(),t.end());
  worst=max(worst,directWorst(t));
 }
 directMemo.emplace(move(ky),worst);return worst;
}
int main(){
 for(int i=0;i<N;i++)for(int j=0;j<N;j++){
  ov[i][j]=0;
  for(int t=1;t<K;t++)if(word(i).substr(K-t)==word(j).substr(0,t))ov[i][j]=t;
 }
 const auto dp=optimalDp();
 int canonicalCount=0,allCount=0,maximumNum=0,maximumDen=1;
 vector<int> maxMasks;
 for(int mask=1;mask<TOTAL;mask++){
  auto orbit=orbitMasks(mask);
  if(*min_element(orbit.begin(),orbit.end())!=mask)continue;
  ++canonicalCount;
  vector<uint8_t>s;for(int i=0;i<N;i++)if(mask&(1<<i))s.push_back(uint8_t((i<<4)|i));
  int count=s.size();int optCompression=-1;
  for(int i=0;i<N;i++)if(mask&(1<<i))optCompression=max(optCompression,dp[mask][i]);
  int optimum=K*count-optCompression;
  int greedy=K*count-minimumGreedyCompression(s);
  if((long long)greedy*maximumDen>(long long)maximumNum*optimum){
    maximumNum=greedy;maximumDen=optimum;maxMasks.clear();
  }
  if((long long)greedy*maximumDen==(long long)maximumNum*optimum)
    maxMasks.push_back(mask);
  // Reclaim transient memoization periodically, without changing mathematical states.
  if(canonicalCount%100==0){memo.clear();memo.rehash(0);}
 }
 set<int> allMaxMasks;
 for(int mask:maxMasks){auto orbit=orbitMasks(mask);allMaxMasks.insert(orbit.begin(),orbit.end());}
 cout<<"nonempty_binary_four_mer_sets="<<TOTAL-1<<"\n";
 cout<<"reversal_complement_orbits="<<canonicalCount<<"\n";
 cout<<"maximum_ratio="<<maximumNum<<"/"<<maximumDen<<"\n";
 cout<<"maximizing_canonical_masks:";for(int mask:maxMasks)cout<<" "<<mask;cout<<"\n";
 cout<<"maximizing_labeled_masks:";for(int mask:allMaxMasks)cout<<" "<<mask;cout<<"\n";
 cout<<"states_calculated="<<states<<" memo_hits="<<hits<<"\n";
 assert(canonicalCount==16959);
 assert(maximumNum==17 && maximumDen==11);
 assert(maxMasks.size()==1 && maxMasks[0]==1343);
 assert(allMaxMasks.size()==4);
 vector<P> nodes;vector<string> directInput;
 for(int i=0;i<N;i++)if(1343&(1<<i)){
  nodes.push_back({uint8_t((i<<4)|i),word(i)});
  directInput.push_back(word(i));
 }
 string greedyOut=greedyWitness(nodes);
 int independentWorst=directWorst(directInput);
 assert(greedyOut.size()==17 && independentWorst==17);
 for(auto&w:directInput)assert(greedyOut.find(w)!=string::npos);
 string optimalOut;
 for(int x=0;x<(1<<11);x++){
  string t(11,'0');for(int b=0;b<11;b++)t[10-b]=char('0'+((x>>b)&1));
  bool ok=true;for(auto&w:directInput)if(t.find(w)==string::npos)ok=false;
  if(ok){optimalOut=t;break;}
 }
 assert(optimalOut.size()==11); // 8 distinct four-mers need at least 8+3 symbols
 cout<<"sharp_input:";for(auto&w:directInput)cout<<" "<<w;cout<<"\n";
 cout<<"legal_greedy_witness="<<greedyOut<<"\n";
 cout<<"shortest_witness="<<optimalOut<<"\n";
 cout<<"independent_literal_states="<<directMemo.size()<<"\n";
 cout<<"PASS\n";
}
