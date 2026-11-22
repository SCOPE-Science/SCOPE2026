// Self-contained independent C++17 verification of four-star-color reconfiguration.
// Compiled with: g++ -O3 -std=c++17 star_cpp.cpp -o star_cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;
struct Graph {int n; vector<pair<int,int>> edges;};
Graph make_graph(string name){
  Graph g; auto &E=g.edges;
  if(name=="Heawood"){
    g.n=14;for(int i=0;i<7;i++)for(int d:{0,1,3})E.push_back({i,7+(i+d)%7});
  }else if(name=="Mobius-Kantor"){
    g.n=16;for(int i=0;i<8;i++){
      E.push_back({i,(i+1)%8});E.push_back({i,i+8});E.push_back({i+8,8+(i+3)%8});
    }
  }else if(name=="Pappus"){
    g.n=18;for(int x=0;x<3;x++)for(int y=0;y<3;y++){
      int p=3*x+y;E.push_back({p,9+x});E.push_back({p,12+y});E.push_back({p,15+(x+y)%3});
    }
  }else if(name=="Desargues"){
    g.n=20;vector<int> a,b;
    for(int m=0;m<32;m++){
      if(__builtin_popcount((unsigned)m)==2)a.push_back(m);
      if(__builtin_popcount((unsigned)m)==3)b.push_back(m);
    }
    for(int i=0;i<10;i++)for(int j=0;j<10;j++)if((a[i]&b[j])==a[i]) E.push_back({i,10+j});
  }else assert(false);
  assert((int)E.size()==g.n*3/2);
  return g;
}
struct Enumeration{
  int n,k; vector<vector<int>> adj, old, earlier;
  vector<vector<array<int,4>>> paths_late;
  vector<int> color;
  vector<string> solutions;
  long long visits=0;
  Enumeration(Graph g,int K):n(g.n),k(K),adj(n),old(n),earlier(n),paths_late(n),color(n,-1){
    for(auto [a,b]:g.edges){old[a].push_back(b);old[b].push_back(a);}
    // BFS ordering differs from the independent Python original-index recursion.
    queue<int> q;q.push(0);vector<int> order,vis(n);
    vis[0]=1;
    while(!q.empty()){
      int u=q.front();q.pop();order.push_back(u);
      for(int v:old[u])if(!vis[v]){vis[v]=1;q.push(v);}
    }
    assert((int)order.size()==n);
    vector<int> pos(n);for(int i=0;i<n;i++)pos[order[i]]=i;
    for(auto [u,v]:g.edges){int a=pos[u],b=pos[v];adj[a].push_back(b);adj[b].push_back(a);}
    for(int i=0;i<n;i++)for(int j:adj[i])if(j<i)earlier[i].push_back(j);
    // Each P4 is enumerated from its first endpoint and stored exactly once.
    set<array<int,4>> paths;
    for(int a=0;a<n;a++)for(int b:adj[a])for(int c:adj[b])if(c!=a)
      for(int d:adj[c])if(d!=a && d!=b){
        array<int,4> p={a,b,c,d};
        if(a>d) reverse(p.begin(),p.end());
        paths.insert(p);
      }
    for(auto p:paths){int last=*max_element(p.begin(),p.end());paths_late[last].push_back(p);}
  }
  void dfs(int i,int used){
    visits++;
    if(i==n){if(used==k){string s;for(int x:color)s.push_back(char('0'+x));solutions.push_back(s);}return;}
    for(int a=0;a<min(used+1,k);a++){
      bool good=true;
      for(int j:earlier[i])if(color[j]==a){good=false;break;}
      if(!good)continue;
      color[i]=a;
      for(auto p:paths_late[i])if(color[p[0]]==color[p[2]] && color[p[1]]==color[p[3]]){
        good=false;break;
      }
      if(good)dfs(i+1,max(used,a+1));
    }
    color[i]=-1;
  }
};
map<string,int> components(const vector<string>& canon){
  set<string> all;
  for(const string& s:canon){
    array<int,4> p={0,1,2,3};
    do{
      string t=s;
      for(char &c:t)c=char('0'+p[c-'0']);
      all.insert(t);
    }while(next_permutation(p.begin(),p.end()));
  }
  vector<string> v(all.begin(),all.end());
  unordered_map<string,int> ix;
  for(int i=0;i<(int)v.size();i++)ix[v[i]]=i;
  vector<vector<int>> adj(v.size());
  for(int i=0;i<(int)v.size();i++){
    string s=v[i];
    for(int j=0;j<(int)s.size();j++){
      char old=s[j];
      for(char c='0';c<='3';c++)if(c!=old){
        s[j]=c;auto it=ix.find(s);if(it!=ix.end())adj[i].push_back(it->second);
      }
      s[j]=old;
    }
  }
  vector<char> vis(v.size(),0);map<string,int> types;
  for(int i=0;i<(int)v.size();i++)if(!vis[i]){
    vector<int> Q={i};vis[i]=1;
    for(size_t t=0;t<Q.size();t++)for(int j:adj[Q[t]])if(!vis[j]){vis[j]=1;Q.push_back(j);}
    int N=(int)Q.size(),M=0;map<int,int> degrees;
    for(int j:Q){M+=(int)adj[j].size();degrees[(int)adj[j].size()]++;}
    M/=2;
    string shape="?";
    if(N==1&&M==0)shape="K1";
    if(N==2&&M==1)shape="K2";
    if(N==3&&M==2&&degrees==map<int,int>{{1,2},{2,1}})shape="P3";
    if(N==4&&M==4&&degrees==map<int,int>{{2,4}})shape="C4";
    if(N==8&&M==12&&degrees==map<int,int>{{3,8}}){
      // Verify bipartiteness; every 3-regular bipartite 8-vertex graph is Q3.
      vector<int> part(v.size(),-1);queue<int> qq;qq.push(Q[0]);part[Q[0]]=0;
      int left=0,right=0;
      while(!qq.empty()){
        int j=qq.front();qq.pop();(part[j]?right:left)++;
        for(int u:adj[j]){
          if(part[u]<0){part[u]=1-part[j];qq.push(u);}
          else assert(part[u]!=part[j]);
        }
      }
      assert(left==4 && right==4);shape="Q3";
    }
    if(N==9&&M==12&&degrees==map<int,int>{{2,4},{3,4},{4,1}}){
      int ctr=-1;for(int x:Q)if(adj[x].size()==4)ctr=x;
      assert(ctr>=0);
      for(int x:adj[ctr])assert(adj[x].size()==3);
      set<int> rim(Q.begin(),Q.end());rim.erase(ctr);
      for(int x:rim){int ri=0;for(int y:adj[x])if(rim.count(y)){ri++;assert(adj[x].size()!=adj[y].size());}assert(ri==2);}
      shape="P3xP3";
    }
    assert(shape!="?");types[shape]++;
  }
  long long edgecount=0;for(auto &x:adj)edgecount+=(int)x.size();edgecount/=2;
  cout<<" named="<<v.size()<<" recolor_edges="<<edgecount<<" components=";
  for(auto [s,n]:types)cout<<s<<":"<<n<<",";cout<<"\n";
  return types;
}
int main(){
  const vector<string> names={"Heawood","Mobius-Kantor","Pappus","Desargues"};
  const vector<long long> part={112,223,365,850};
  const vector<map<string,int>> expected={
    {{"Q3",336}},{{"K1",2280},{"K2",1152},{"C4",192}},
    {{"K1",3072},{"K2",1296},{"P3",648},{"Q3",144}},
    {{"K1",7200},{"K2",1440},{"Q3",480},{"P3xP3",720}}
  };
  for(int i=0;i<4;i++){
    auto G=make_graph(names[i]);Enumeration lower(G,3);lower.dfs(0,0);assert(lower.solutions.empty());
    Enumeration check(G,4);check.dfs(0,0);assert((long long)check.solutions.size()==part[i]);
    cout<<names[i]<<" n="<<G.n<<" partitions="<<check.solutions.size();
    assert(components(check.solutions)==expected[i]);
  }
  cout<<"PASS\n";
}
