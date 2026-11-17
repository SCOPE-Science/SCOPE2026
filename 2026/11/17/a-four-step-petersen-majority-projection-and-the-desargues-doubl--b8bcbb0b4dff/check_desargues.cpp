#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <tuple>
#include <vector>
using namespace std;
int main(){
  constexpr int N=20,S=1<<20;
  array<array<int,3>,N> nb{}; array<int,N> deg{};
  auto edge=[&](int a,int b){ nb[a][deg[a]++]=b;nb[b][deg[b]++]=a; };
  for(int i=0;i<10;i++){edge(i,(i+1)%10);edge(10+i,10+(i+3)%10);edge(i,10+i);}
  for(int i=0;i<N;i++)if(deg[i]!=3)return 1;
  vector<int> go(S),indeg(S,0);
  for(int s=0;s<S;s++){
    int out=0;
    for(int i=0;i<N;i++){
      int ones=((s>>nb[i][0])&1)+((s>>nb[i][1])&1)+((s>>nb[i][2])&1);
      if(ones>=2)out|=1<<i;
    }
    go[s]=out;indeg[out]++;
  }
  queue<int> q;vector<int> peel;peel.reserve(S);
  for(int s=0;s<S;s++)if(indeg[s]==0)q.push(s);
  while(!q.empty()){
    int s=q.front();q.pop();peel.push_back(s);
    if(--indeg[go[s]]==0)q.push(go[s]);
  }
  vector<int> orbit(S,-1),depth(S,-1),period(S,-1);vector<int> orbit_size;
  int fixed=0,two=0;
  for(int s=0;s<S;s++)if(indeg[s]>0 && orbit[s]==-1){
    int id=(int)orbit_size.size(),v=s,p=0;
    do{orbit[v]=id;depth[v]=0;p++;v=go[v];}while(v!=s);
    if(p==1)fixed++;else if(p==2)two++;else return 2;
    orbit_size.push_back(0);
    v=s;do{period[v]=p;v=go[v];}while(v!=s);
  }
  for(auto it=peel.rbegin();it!=peel.rend();it++){
    int s=*it,v=go[s];orbit[s]=orbit[v];depth[s]=depth[v]+1;period[s]=period[v];
  }
  map<pair<int,int>,int> joint;
  for(int s=0;s<S;s++){
    if(orbit[s]<0 || depth[s]>4)return 3;
    orbit_size[orbit[s]]++;
    joint[{depth[s],period[s]}]++;
  }
  map<pair<int,int>,int> basins;
  for(int s=0;s<S;s++)if(depth[s]==0){
    if(s<go[s] && period[s]==2)continue;
    basins[{period[s],orbit_size[orbit[s]]}]++;
  }
  // Each period-two cycle is counted once, fixed cycle once.
  cout<<"vertices="<<N<<" configurations="<<S<<" fixed="<<fixed<<" two_cycles="<<two<<"\n";
  cout<<"entry_period:";
  for(auto const &[key,count]:joint)cout<<" ("<<key.first<<","<<key.second<<")="<<count;
  cout<<"\n";
  cout<<"basins:";
  for(auto const &[key,count]:basins)cout<<" ("<<key.first<<","<<key.second<<")="<<count;
  cout<<"\n";
  if(fixed!=124 || two!=7626 || joint[{4,1}]!=47040 || joint[{4,2}]!=184320) return 4;
  if(basins != map<pair<int,int>,int>{{{1,1},72},{{1,100},50},{{1,51076},2},{{2,2},2556},{{2,20},3600},{{2,200},1225},{{2,452},144},{{2,4520},100},{{2,102152},1}})return 5;
  cout<<"all_checks_passed\n";
}
