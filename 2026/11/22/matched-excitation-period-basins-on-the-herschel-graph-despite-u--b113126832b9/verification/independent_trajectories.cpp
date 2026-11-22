// Independent exhaustive orbit finder for the two Herschel-graph excitation rules.
// Each of the 3^11 starting states is analyzed by Floyd cycle detection.
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <tuple>
#include <vector>
using namespace std;
constexpr int V=11;
constexpr int S=177147;
const vector<vector<int>> edges = {
 {1,3,4},{0,2,5,6},{1,3,7},{0,2,8,9},{0,5,9},
 {1,4,10},{1,7,10},{2,6,8},{3,7,10},{3,4,10},{5,6,8,9}
};
array<int,V> decode(int code){
 array<int,V> x{};
 for(int i=0;i<V;++i){x[i]=code%3;code/=3;}
 return x;
}
int encode(const array<int,V>& x){
 int r=0,p=1;
 for(int i=0;i<V;++i){r+=p*x[i];p*=3;}
 return r;
}
int advance(int code,bool gh){
 auto x=decode(code);array<int,V> y{};
 for(int i=0;i<V;++i){
  int c=x[i];
  if(gh){
    if(c>0)y[i]=(c+1)%3;
    else {
      int excited=0;for(auto j:edges[i])if(x[j]==1)excited=1;
      y[i]=excited;
    }
  } else {
    int target=(c+1)%3;int seen=0;
    for(auto j:edges[i]) if(x[j]==target) seen=1;
    y[i]=seen?target:c;
  }
 }
 return encode(y);
}
struct Output{int depth,period;};
Output orbit(int s,bool gh){
 auto f=[&](int v){return advance(v,gh);};
 int slow=f(s),fast=f(f(s));
 while(slow!=fast){slow=f(slow);fast=f(f(fast));}
 int start=0;slow=s;
 while(slow!=fast){slow=f(slow);fast=f(fast);++start;}
 int len=1;fast=f(slow);
 while(slow!=fast){fast=f(fast);++len;}
 return {start,len};
}
int main(){
 int ed=0;
 for(int i=0;i<V;++i)for(int j:edges[i]){
  assert(j>=0&&j<V);
  assert(find(edges[j].begin(),edges[j].end(),i)!=edges[j].end());
  ++ed;
 }
 assert(ed==36);
 map<tuple<int,int>,int> cHist,hHist;
 map<int,int> basins,cRecur,hRecur;
 int maxC=0,maxH=0,mismatch=0,shared3=0,shared4=0;
 for(int s=0;s<S;++s){
  auto c=orbit(s,false),h=orbit(s,true);
  cHist[{c.depth,c.period}]++;
  hHist[{h.depth,h.period}]++;
  basins[h.period]++;
  maxC=max(maxC,c.depth);maxH=max(maxH,h.depth);
  mismatch+=(c.period!=h.period);
  if(c.depth==0)cRecur[c.period]++;
  if(h.depth==0){
    hRecur[h.period]++;
    if(c.depth==0 && c.period==h.period){
      assert(advance(s,false)==advance(s,true));
      if(h.period==3)shared3++;
      if(h.period==4)shared4++;
    } else if(h.period!=1)assert(false);
  }
 }
 assert(mismatch==0 && maxC==8 && maxH==10);
 assert(basins[1]==17397 && basins[3]==23346 && basins[4]==136404);
 assert(cRecur[1]==3 && cRecur[3]==3060 && cRecur[4]==4752);
 assert(hRecur[1]==1 && hRecur[3]==3060 && hRecur[4]==1200);
 assert(shared3==3060 && shared4==1200);
 assert(hHist[make_tuple(10,3)]==36 && cHist[make_tuple(8,3)]==108);
 cout<<"STATES "<<S<<" MISMATCH "<<mismatch<<" ENTRY_MAX_CCA "<<maxC<<" ENTRY_MAX_GHM "<<maxH<<"\n";
 cout<<"BASIN "<<basins[1]<<" "<<basins[3]<<" "<<basins[4]<<"\n";
 cout<<"RECURRENT_CCA "<<cRecur[1]<<" "<<cRecur[3]<<" "<<cRecur[4]<<"\n";
 cout<<"RECURRENT_GHM "<<hRecur[1]<<" "<<hRecur[3]<<" "<<hRecur[4]<<"\n";
 for(auto [t,count]:cHist)cout<<"CCA "<<get<0>(t)<<" "<<get<1>(t)<<" "<<count<<"\n";
 for(auto [t,count]:hHist)cout<<"GHM "<<get<0>(t)<<" "<<get<1>(t)<<" "<<count<<"\n";
 cout<<"HERSCHEL_FLOYD_OK\n";
}
