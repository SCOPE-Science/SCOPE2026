#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
// Independent biadjacency representation: one row mask per vertex in the first shore.
const int sz[]={3,4,5,5,6,6,6,6,6};
const int rows[9][6]={
 {7,7,7,0,0,0},
 {7,11,13,14,0,0},
 {7,7,25,26,28,0},
 {7,11,21,26,28,0},
 {7,7,11,52,56,56},
 {7,7,25,42,52,56},
 {7,11,21,42,52,56},
 {7,11,21,44,50,56},
 {7,11,28,44,49,50}
};
const char* names[]={"EFz_","G?zTb_","I?BeeOwM?","I?BedPWM?","K??FFBOJ?wB_","K??FEbGL@WB_","K??FEagT@WB_","K??FEQoT@WB_","K??EUIo[@WB_"};
struct Labels {vector<int> p,dep;int maxdep;};
Labels classify(const vector<vector<int>>& neighbors,int mode){
 int n=neighbors.size(),states=1;vector<int> powers(n);
 for(int j=0;j<n;j++){powers[j]=states;states*=3;}
 vector<int> output(states);
 for(int code=0;code<states;code++){
   array<int,12> digits{};
   for(int j=0;j<n;j++)digits[j]=(code/powers[j])%3;
   int newCode=0;
   for(int j=0;j<n;j++){
     int val=digits[j];
     if(mode==0){
       int target=(val+1)%3;
       for(int k:neighbors[j])if(digits[k]==target){val=target;break;}
     }else if(val==1)val=2;
     else if(val==2)val=0;
     else {val=0;for(int k:neighbors[j])if(digits[k]==1){val=1;break;}}
     newCode+=val*powers[j];
   }
   output[code]=newCode;
 }
 Labels res;res.p.assign(states,0);res.dep.assign(states,-1);res.maxdep=0;
 vector<int> seen(states,-1),pos(states,-1);
 for(int start=0;start<states;start++){
   if(res.p[start])continue;
   vector<int> walk;int cur=start;
   while(res.p[cur]==0&&seen[cur]!=start){
     seen[cur]=start;pos[cur]=walk.size();walk.push_back(cur);cur=output[cur];
   }
   int split=walk.size();
   if(res.p[cur]==0){
      assert(seen[cur]==start);split=pos[cur];int period=walk.size()-split;
      for(int j=split;j<(int)walk.size();j++){res.p[walk[j]]=period;res.dep[walk[j]]=0;}
   }
   for(int j=split-1;j>=0;j--){int s=walk[j],next=output[s];res.p[s]=res.p[next];res.dep[s]=res.dep[next]+1;}
 }
 for(int i=0;i<states;i++){assert(res.p[i]>0&&res.dep[i]>=0);res.maxdep=max(res.maxdep,res.dep[i]);}
 return res;
}
int main(){
 for(int g=0;g<9;g++){
   int m=sz[g];vector<vector<int>> nb(2*m);
   for(int i=0;i<m;i++)for(int j=0;j<m;j++)if((rows[g][i]>>j)&1){nb[i].push_back(m+j);nb[m+j].push_back(i);}
   for(auto &n:nb)assert(n.size()==3);
   auto a=classify(nb,0),b=classify(nb,1);
   map<pair<int,int>,long> joint;
   for(size_t s=0;s<a.p.size();s++)joint[{a.p[s],b.p[s]}]++;
   cout<<"order="<<2*m<<" code="<<names[g]<<" maxCCA="<<a.maxdep<<" maxGHM="<<b.maxdep<<" joint:";
   for(auto [pair,num]:joint)cout<<" "<<pair.first<<"/"<<pair.second<<"="<<num;
   cout<<"\n";
 }
}
