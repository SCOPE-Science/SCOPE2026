#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>
using namespace std;
// The nine canonical representatives of all connected simple cubic bipartite graphs with <= 12 vertices.
const string codes[]={"EFz_","G?zTb_","I?BeeOwM?","I?BedPWM?","K??FFBOJ?wB_","K??FEbGL@WB_","K??FEagT@WB_","K??FEQoT@WB_","K??EUIo[@WB_"};
vector<unsigned> decode(const string& s){
 int n=int(s[0])-63;vector<unsigned> adj(n);
 int k=0,bit=5;
 for(int j=1;j<n;j++) for(int i=0;i<j;i++) {
   int on=(int(s[1+k])-63)>>bit&1;
   if(on){adj[i]|=1u<<j; adj[j]|=1u<<i;}
   if(--bit<0){bit=5;k++;}
 }
 for(int i=0;i<n;i++)assert(__builtin_popcount(adj[i])==3);
 return adj;
}
struct MapInfo{vector<int> successor;vector<int> period;vector<int> depth;};
MapInfo analyze(const vector<unsigned>& adj,int mode){
 const int n=adj.size();int smax=1;vector<int> pw(n);
 for(int v=0;v<n;v++){pw[v]=smax;smax*=3;}
 MapInfo t;t.successor.resize(smax);t.period.assign(smax,-1);t.depth.assign(smax,-1);
 vector<int> indeg(smax,0);
 for(int x=0;x<smax;x++){
   int digits[12],s=x,y=0;
   for(int v=0;v<n;v++){digits[v]=s%3;s/=3;}
   for(int v=0;v<n;v++){
     int c=digits[v],z=c;
     if(mode==0){
       int target=(c+1)%3;
       unsigned bits=adj[v];while(bits){int w=__builtin_ctz(bits);bits&=bits-1;if(digits[w]==target){z=target;break;}}
     } else if(c==1) z=2;
     else if(c==2) z=0;
     else {unsigned bits=adj[v];while(bits){int w=__builtin_ctz(bits);bits&=bits-1;if(digits[w]==1){z=1;break;}}}
     y+=z*pw[v];
   }
   t.successor[x]=y;indeg[y]++;
 }
 vector<int> removed;removed.reserve(smax);
 for(int x=0;x<smax;x++)if(indeg[x]==0)removed.push_back(x);
 for(size_t i=0;i<removed.size();i++){
   int y=t.successor[removed[i]];if(--indeg[y]==0)removed.push_back(y);
 }
 for(int x=0;x<smax;x++)if(indeg[x]&&t.period[x]==-1){
   int y=x,k=0;do{k++;y=t.successor[y];}while(y!=x);
   do{t.period[y]=k;t.depth[y]=0;y=t.successor[y];}while(y!=x);
 }
 for(int i=(int)removed.size()-1;i>=0;i--){int x=removed[i],y=t.successor[x];t.period[x]=t.period[y];t.depth[x]=t.depth[y]+1;}
 for(int x=0;x<smax;x++)assert(t.period[x]>0&&t.depth[x]>=0);
 return t;
}
int main(){
 for(int g=0;g<9;g++){
   auto adj=decode(codes[g]);auto ca=analyze(adj,0),gh=analyze(adj,1);
   map<pair<int,int>,long> joint;int maxc=0,maxh=0;
   for(int s=0;s<(int)ca.period.size();s++){
     joint[{ca.period[s],gh.period[s]}]++;
     maxc=max(maxc,ca.depth[s]);maxh=max(maxh,gh.depth[s]);
   }
   cout<<"order="<<adj.size()<<" code="<<codes[g]<<" maxCCA="<<maxc<<" maxGHM="<<maxh<<" joint:";
   for(auto [pair,num]:joint)cout<<" "<<pair.first<<"/"<<pair.second<<"="<<num;
   cout<<"\n";
 }
}
