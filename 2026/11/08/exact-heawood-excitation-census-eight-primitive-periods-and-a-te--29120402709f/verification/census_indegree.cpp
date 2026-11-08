#include <bits/stdc++.h>
using namespace std;
int main(){
 constexpr int N=14, S=4782969; //3^14
 array<array<int,3>,N> nb{};
 for(int j=0;j<7;j++){
  for(int k=0;k<3;k++){
    int i=(j+(k==0?0:k==1?1:3))%7;
    nb[j+7][k]=i;
  }
 }
 array<int,N> deg{};
 for(int j=0;j<7;j++)for(int k=0;k<3;k++){
  int i=nb[j+7][k];nb[i][deg[i]++]=j+7;
 }
 vector<int> pw(N+1);pw[0]=1;for(int i=1;i<=N;i++)pw[i]=3*pw[i-1];
 vector<uint32_t> nxt(S),indeg(S,0);
 array<int,N> a{};
 for(int x=0;x<S;x++){
  int y=x;for(int i=0;i<N;i++){a[i]=y%3;y/=3;}
  int z=0;
  for(int i=0;i<N;i++){
    int b=(a[i]==1?2:(a[i]==2?0:((a[nb[i][0]]==1||a[nb[i][1]]==1||a[nb[i][2]]==1)?1:0)));
    z+=b*pw[i];
  }
  nxt[x]=z;indeg[z]++;
 }
 vector<uint32_t> peel;peel.reserve(S);
 for(uint32_t x=0;x<S;x++)if(!indeg[x])peel.push_back(x);
 for(size_t i=0;i<peel.size();i++){
  uint32_t y=nxt[peel[i]];if(!--indeg[y])peel.push_back(y);
 }
 vector<int32_t> tim(S,-1),per(S,-1);
 map<int,int> orbitCounts;
 for(uint32_t x=0;x<S;x++)if(indeg[x] && tim[x]<0){
  vector<uint32_t> v;uint32_t y=x;
  do{v.push_back(y);y=nxt[y];}while(y!=x);
  int p=v.size();orbitCounts[p]++;
  for(uint32_t z:v){tim[z]=0;per[z]=p;}
 }
 for(int i=(int)peel.size()-1;i>=0;i--){uint32_t x=peel[i];tim[x]=tim[nxt[x]]+1;per[x]=per[nxt[x]];}
 map<pair<int,int>,int64_t> counts;
 int maxt=0,maxp=0;int64_t states=0;
 for(uint32_t x=0;x<S;x++){counts[{tim[x],per[x]}]++;maxt=max(maxt,(int)tim[x]);maxp=max(maxp,(int)per[x]);states++;}
 cout<<"states "<<states<<" maxT "<<maxt<<" maxP "<<maxp<<" periodic_states "<<S-peel.size()<<"\n";
 cout<<"orbits";for(auto [p,n]:orbitCounts)cout<<" "<<p<<":"<<n;cout<<"\n";
 map<int,uint32_t> leastRep;uint32_t longestWitness=S;for(uint32_t x=0;x<S;x++){if(tim[x]==0 && !leastRep.count(per[x]))leastRep[per[x]]=x;if(tim[x]==maxt && longestWitness==S)longestWitness=x;}
 cout<<"least_period_reps";for(auto [p,x]:leastRep)cout<<" "<<p<<":"<<x;cout<<"\n";cout<<"max_transient_rep "<<longestWitness<<"\n";
 for(auto [key,num]:counts)cout<<"T="<<key.first<<" P="<<key.second<<" count="<<num<<"\n";
}
