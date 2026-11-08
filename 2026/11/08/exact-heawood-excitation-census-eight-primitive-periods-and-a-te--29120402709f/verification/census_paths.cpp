// Independent complete-state enumeration by memoized trajectories.
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
constexpr int V=14;
constexpr int S=4782969;
constexpr int lines[7][3]={
 {0,1,2}, {0,3,4}, {0,5,6}, {1,3,5},
 {1,4,6}, {2,3,6}, {2,4,5}
};
uint32_t nextState(uint32_t x,const array<array<int,3>,V>& adj,const array<int,V>& power){
 int a[V]; uint32_t t=x;
 for(int i=0;i<V;i++){a[i]=t%3;t/=3;}
 uint32_t y=0;
 for(int i=0;i<V;i++){
   int z=0;
   if(a[i]==1)z=2;
   if(a[i]==0){for(int j:adj[i])if(a[j]==1){z=1;break;}}
   y+=z*power[i];
 }
 return y;
}
int main(){
 array<array<int,3>,V> adj{};
 array<int,V> deg{};
 for(int j=0;j<7;j++)for(int k=0;k<3;k++){
   int v=lines[j][k];adj[v][deg[v]++]=7+j;adj[7+j][deg[7+j]++]=v;
 }
 for(int i=0;i<V;i++)if(deg[i]!=3)return 2;
 array<int,V> power{};power[0]=1;for(int i=1;i<V;i++)power[i]=3*power[i-1];
 vector<int32_t> entry(S,-1),period(S,-1);
 vector<int32_t> tag(S,0),at(S,0);
 vector<int> path;path.reserve(128);
 for(int seed=0;seed<S;seed++){
   if(entry[seed]>=0)continue;
   path.clear();int node=seed, stamp=seed+1;
   while(entry[node]<0 && tag[node]!=stamp){
     tag[node]=stamp;at[node]=(int)path.size();path.push_back(node);
     node=nextState(node,adj,power);
   }
   if(entry[node]<0){
     int start=at[node];int p=(int)path.size()-start;
     for(int i=start;i<(int)path.size();i++){entry[path[i]]=0;period[path[i]]=p;}
     path.resize(start);
   }
   for(int i=(int)path.size()-1;i>=0;i--){int y=path[i];int nxt=nextState(y,adj,power);entry[y]=1+entry[nxt];period[y]=period[nxt];}
 }
 map<pair<int,int>,uint64_t> count;
 for(int i=0;i<S;i++){if(entry[i]<0 || period[i]<1)return 4;count[{entry[i],period[i]}]++;}
 int maxT=0;for(auto [key,n]:count)maxT=max(maxT,key.first);
 cout<<"S "<<S<<" maxT "<<maxT<<" classes "<<count.size()<<"\n";
 for(auto [key,n]:count)cout<<key.first<<","<<key.second<<","<<n<<"\n";
}
