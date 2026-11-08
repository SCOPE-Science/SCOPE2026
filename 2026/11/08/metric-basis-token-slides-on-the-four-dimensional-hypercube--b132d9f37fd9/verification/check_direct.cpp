// Complete metric-basis relocation graph of the binary four-cube.
// Compile: g++ -O2 -std=c++17 check_direct.cpp -o check_direct
#include <bits/stdc++.h>
using namespace std;
int dist4(int a,int b) {return __builtin_popcount((unsigned)(a^b));}
bool resolves(const vector<int>& s) {
  set<vector<int>> profiles;
  for(int x=0;x<16;x++) {
    vector<int> p;
    for(int y:s) p.push_back(dist4(x,y));
    if(!profiles.insert(p).second) return false;
  }
  return true;
}
int main() {
  int n3=0;
  for(int a=0;a<16;a++)for(int b=a+1;b<16;b++)for(int c=b+1;c<16;c++)
    if(resolves({a,b,c})) n3++;
  vector<int> states;
  for(int a=0;a<16;a++)for(int b=a+1;b<16;b++)for(int c=b+1;c<16;c++)for(int d=c+1;d<16;d++)
    if(resolves({a,b,c,d})) states.push_back((1<<a)|(1<<b)|(1<<c)|(1<<d));
  map<int,int> idx; for(int i=0;i<(int)states.size();i++)idx[states[i]]=i;
  vector<vector<int>> adj(states.size());
  for(int i=0;i<(int)states.size();i++) {
    int mask=states[i];
    for(int x=0;x<16;x++)if((mask>>x)&1)
      for(int bit=0;bit<4;bit++) {
        int y=x^(1<<bit);
        if(!(mask&(1<<y))) {
          int other=mask^(1<<x)^(1<<y);
          auto it=idx.find(other);
          if(it!=idx.end()) adj[i].push_back(it->second);
        }
      }
    sort(adj[i].begin(),adj[i].end());
    assert(unique(adj[i].begin(),adj[i].end())==adj[i].end());
  }
  long long degsum=0;
  map<int,int> degree,ecc,cc;
  for(int i=0;i<(int)states.size();i++) {
    degree[adj[i].size()]++; degsum+=adj[i].size();
    for(int j:adj[i])assert(find(adj[j].begin(),adj[j].end(),i)!=adj[j].end());
  }
  vector<int> component(states.size(),-1);int cn=0;
  for(int root=0;root<(int)states.size();root++) if(component[root]==-1){
    queue<int> q;q.push(root);component[root]=cn;int size=0;
    while(!q.empty()){int u=q.front();q.pop();size++;
      for(int v:adj[u])if(component[v]==-1){component[v]=cn;q.push(v);}}
    cc[size]++;cn++;
  }
  for(int root=0;root<(int)states.size();root++) {
    vector<int> d(states.size(),-1);d[root]=0;queue<int> q;q.push(root);
    while(!q.empty()){int u=q.front();q.pop();for(int v:adj[u])if(d[v]==-1){d[v]=d[u]+1;q.push(v);}}
    int mx=*max_element(d.begin(),d.end());
    assert(*min_element(d.begin(),d.end())>=0);
    ecc[mx]++;
  }
  cout << "minimum_resolving_cardinality=4\n";
  cout << "resolving_triples="<<n3<<"\n";
  cout << "metric_bases="<<states.size()<<"\n";
  cout << "edges="<<degsum/2<<"\n";
  cout << "components="<<cn<<"\n";
  cout << "degree:";for(auto [x,c]:degree)cout<<' '<<x<<':'<<c;cout<<'\n';
  cout << "eccentricity:";for(auto [x,c]:ecc)cout<<' '<<x<<':'<<c;cout<<'\n';
  cout << "component_sizes:";for(auto [x,c]:cc)cout<<' '<<x<<':'<<c;cout<<'\n';
  assert(n3==0 && states.size()==928 && degsum/2==3584 && cn==1);
  assert((degree==map<int,int>{{7,512},{8,384},{16,32}}));
  assert((ecc==map<int,int>{{8,64},{9,592},{10,272}}));
}
