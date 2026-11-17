// Exact finite transfer-graph certificate for synchronous elementary Rule 54.
// C++17; no third-party dependencies.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

struct Check {
 int t, K, mask, N, edges=0;
 vector<vector<int>> adj, radj;
 vector<int> used, order, group;
 Check(int T):t(T),K(1<<T),mask(K-1),N(K*K),adj(N),radj(N),used(N),group(N,-1) {
  for (int a=0;a<K;a++) for(int b=0;b<K;b++) for(int c=0;c<K;c++){
   // The bits of the temporal history are indexed by time mod t.
   // Rule 54: 001,010,100,101 -> 1; all other triples -> 0.
   int updated=((a & (~b))|((~a) & (b^c))) & mask;
   int next=(b>>1)|((b&1)<<(t-1));
   if(updated==next){int v=a*K+b,w=b*K+c;adj[v].push_back(w);radj[w].push_back(v);edges++;}
  }
 }
 void dfs1(int v){used[v]=1;for(int w:adj[v])if(!used[w])dfs1(w);order.push_back(v);}
 void dfs2(int v,int id,vector<int>&vtx){group[v]=id;vtx.push_back(v);for(int w:radj[v])if(group[w]==-1)dfs2(w,id,vtx);}
 vector<pair<int,string>> run(){
  for(int v=0;v<N;v++)if(!used[v])dfs1(v);
  int id=0;vector<pair<int,string>> cycles;
  reverse(order.begin(),order.end());
  for(int v:order){if(group[v]!=-1)continue;vector<int> cc;dfs2(v,id,cc);
   bool recurrent=cc.size()>1;
   if(cc.size()==1) for(int w:adj[cc[0]])if(w==cc[0])recurrent=true;
   if(recurrent){
    // Every induced recurrent component must be one isolated directed cycle.
    for(int x:cc){int in=0,out=0;for(int y:adj[x])if(group[y]==id)out++;for(int y:radj[x])if(group[y]==id)in++;assert(in==1&&out==1);}
    int cur=*min_element(cc.begin(),cc.end()); string word;
    for(size_t k=0;k<cc.size();k++){
     word+=char('0'+(cur/K&1));
     for(int y:adj[cur])if(group[y]==id){cur=y;break;}
    }
    assert(cur==*min_element(cc.begin(),cc.end()));
    cycles.push_back({int(cc.size()),word});
   }
   id++;
  }
  sort(cycles.begin(),cycles.end());
  cout << "t="<<t<<" vertices="<<N<<" edges="<<edges<<" recurrent_components="<<cycles.size()<<"\n";
  for(auto [length,word]:cycles) cout << "cycle="<<length<<" spatial_word="<<word<<"\n";
  return cycles;
 }
};
int main(){
 for(int t : {1,2,3,6}){
  auto c=Check(t).run();
  map<int,int> distribution;
  for(auto [size,word]:c)distribution[size]++;
  if(t==1||t==3)assert((distribution==map<int,int>{{1,1}}));
  if(t==2)assert((distribution==map<int,int>{{1,1},{4,1}}));
  if(t==6)assert((distribution==map<int,int>{{1,1},{4,1},{8,3}}));
 }
 cout<<"PASS finite complete graph certificates; for every n>=3: primitive6_states=24*[8 divides n], orbits=4*[8 divides n]\n";
}
