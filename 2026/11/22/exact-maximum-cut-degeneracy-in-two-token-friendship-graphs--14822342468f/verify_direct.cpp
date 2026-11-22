#include <algorithm>
#include <cstdint>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;
int main(){
 for(int q=1;q<=3;q++){
  int n=2*q+1;
  vector<pair<int,int>> g;
  for(int i=0;i<q;i++){
   int a=2*i+1,b=a+1; g.push_back({0,a});g.push_back({0,b});g.push_back({a,b});
  }
  vector<pair<int,int>> states;
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)states.push_back({a,b});
  vector<tuple<int,int,int>> edges;
  for(int i=0;i<(int)states.size();i++)for(int j=i+1;j<(int)states.size();j++){
   int p=(1<<states[i].first)|(1<<states[i].second),r=(1<<states[j].first)|(1<<states[j].second);
   int d=p^r;
   if(__builtin_popcount((unsigned)d)!=2)continue;
   int a=__builtin_ctz((unsigned)d),b=__builtin_ctz((unsigned)(d^(1<<a)));
   if(find(g.begin(),g.end(),make_pair(a,b))!=g.end() ||find(g.begin(),g.end(),make_pair(b,a))!=g.end())edges.push_back({i,j,1});
  }
  int nn=states.size();
  uint64_t best=0,count=0;
  // One state fixed to 0, count unordered cuts
  for(uint64_t bits=0;bits<(1ULL<<(nn-1));bits++){
   int val=0;
   for(auto [u,v,w]:edges){int bu=u?((bits>>(u-1))&1):0,bv=v?((bits>>(v-1))&1):0; val+=w*(bu^bv);}
   if(val>best){best=val;count=1;}else if(val==best){count++;}
  }
  cout<<"DIRECT_MAXCUT_CENSUS q="<<q<<" vertices="<<nn<<" edges="<<edges.size()<<" max="<<best<<" cuts="<<count<<"\n";
  const uint64_t answer[]={0,3,97,17239};
  if(best!=uint64_t(2*q*(2*q-1))||count!=answer[q])return 1;
 }
 cout<<"DIRECT_MAXCUT_CENSUS_PASS\n";
}
