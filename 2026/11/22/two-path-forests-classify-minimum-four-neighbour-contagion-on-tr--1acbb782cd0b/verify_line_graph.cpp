// Exhaustive fixed-size bootstrap seeds on triangular graphs; independent-neighbor implementation.
// Compile: c++ -O2 -std=c++17 verify_line_graph.cpp -o verify_line_graph
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <array>
using namespace std;
int main(){
 for(int n=5;n<=10;n++){
  vector<pair<int,int>> es;
  for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)es.push_back({u,v});
  int m=es.size();
  vector<vector<int>> nbr(m);
  for(int i=0;i<m;i++)for(int j=0;j<m;j++)if(i!=j){
   auto [a,b]=es[i];auto [c,d]=es[j];
   if(a==c||a==d||b==c||b==d)nbr[i].push_back(j);
  }
  long long total=0,paths=0,twop3=0, t3=0,t4=0,other=0;
  for(int a=0;a<m;a++)for(int b=a+1;b<m;b++)for(int c=b+1;c<m;c++)for(int d=c+1;d<m;d++){
   vector<uint8_t> active(m,0);active[a]=active[b]=active[c]=active[d]=1;
   int time=0;
   while(true){
    vector<int> added;
    for(int j=0;j<m;j++)if(!active[j]){
     int count=0;for(int h:nbr[j])count+=active[h];
     if(count>=4)added.push_back(j);
    }
    if(added.empty())break;
    for(int j:added)active[j]=1;
    time++;
   }
   if(count(active.begin(),active.end(),uint8_t(1))!=m)continue;
   total++;
   int deg[16]={};for(int j:{a,b,c,d}){deg[es[j].first]++;deg[es[j].second]++;}
   vector<int> ds(deg,deg+n);sort(ds.begin(),ds.end(),greater<int>());
   // Degree sequences alone do not distinguish a five-vertex path from triangle plus edge.
   if(ds[0]==2 && ds[1]==2 && ds[2]==2 && ds[3]==1 && ds[4]==1){
    // Four initial edges with five supported vertices must be a tree or triangle plus edge.
    vector<int> seen(n,0), stack;
    for(int v=0;v<n;v++)if(deg[v]){stack.push_back(v);break;}
    while(!stack.empty()){
     int u=stack.back();stack.pop_back();if(seen[u])continue;seen[u]=1;
     for(int j:{a,b,c,d}){
      auto [x,y]=es[j];if(x==u)stack.push_back(y);if(y==u)stack.push_back(x);
     }
    }
    int visited=0;for(int v=0;v<n;v++)visited+=seen[v];
    if(visited==5)paths++;else other++;
   }else if(ds[0]==2 && ds[1]==2 && ds[2]==1 && ds[3]==1 && ds[4]==1 && ds[5]==1){
    // Two components of 3 vertices each.
    twop3++;
   }else other++;
   t3+=(time==3);t4+=(time==4);
   if(time!=3 && time!=4)other++;
  }
  auto C=[](int N,int K)->long long {if(N<K)return 0;long long v=1;for(int j=1;j<=K;j++)v=v*(N-j+1)/j;return v;};
  long long ep=60*C(n,5), ed=90*C(n,6);
  assert(total==ep+ed && paths==ep && twop3==ed && other==0);
  assert(t3==((n==5)?ep:((n==6)?ed:0)));
  assert(t4==total-t3);
  cout<<"n="<<n<<" percolating4="<<total<<" P5="<<paths<<" 2P3="<<twop3<<" time3="<<t3<<" time4="<<t4<<" PASS\n";
 }
}
