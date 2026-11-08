// Independent exact checker: the Moser graph is the complement of K_{3,3}
// after subdividing one cross-edge. Uses integer base-k encodings and BFS.
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;

using Arr = array<int,7>;

static Arr decode(int w, int k) {
  Arr a{};
  for (int i=0; i<7; ++i) {a[i]=w%k; w/=k;}
  return a;
}

static vector<pair<int,int>> complement_edges() {
  bool utility[7][7] = {};
  auto put=[&](int x,int y) {utility[x][y]=utility[y][x]=true;};
  for (int l=0; l<3; ++l) for (int r=3; r<6; ++r)
    if (!(l==0 && r==3)) put(l,r);
  put(0,6); put(3,6);
  vector<pair<int,int>> edges;
  for (int a=0; a<7; ++a) for (int b=a+1; b<7; ++b)
    if (!utility[a][b]) edges.emplace_back(a,b);
  assert(edges.size()==11);
  return edges;
}

static void check(int k) {
  auto E=complement_edges();
  int power[8]; power[0]=1;
  for(int i=1;i<=7;++i) power[i]=power[i-1]*k;
  vector<int> valid(power[7],-1);
  vector<int> words;
  for(int word=0;word<power[7];++word) {
    Arr c=decode(word,k);
    bool proper=true;
    for(auto [a,b]:E) if(c[a]==c[b]) { proper=false; break; }
    if(proper){valid[word]=int(words.size());words.push_back(word);}
  }
  int n=words.size();
  vector<vector<int>> adj(n);
  map<int,int> degrees;
  for(int i=0;i<n;++i) {
    Arr c=decode(words[i],k);
    for(int v=0;v<7;++v) for(int col=0;col<k;++col)
      if(col!=c[v]) {
        int code=words[i]+(col-c[v])*power[v];
        if(valid[code]>=0) adj[i].push_back(valid[code]);
      }
    ++degrees[int(adj[i].size())];
  }
  int edges=0;for(auto &ns:adj)edges+=ns.size();assert(!(edges&1));edges/=2;
  map<int,long long> pair_hist;
  map<int,int> eccentricities;
  vector<int> dist(n);
  for(int s=0;s<n;++s){
    fill(dist.begin(),dist.end(),-1);
    queue<int> todo;todo.push(s);dist[s]=0;
    while(!todo.empty()){
      int v=todo.front();todo.pop();
      for(int w:adj[v]) if(dist[w]==-1){dist[w]=dist[v]+1;todo.push(w);}
    }
    int ecc=0;
    for(int t=0;t<n;++t){assert(dist[t]>=0);ecc=max(ecc,dist[t]);if(t>s) ++pair_hist[dist[t]];}
    ++eccentricities[ecc];
  }
  int radius=eccentricities.begin()->first,diameter=eccentricities.rbegin()->first;
  cout<<"k="<<k<<" states="<<n<<" edges="<<edges<<" radius="<<radius<<" diameter="<<diameter<<" degrees=";
  for(auto [x,v]:degrees)cout<<x<<":"<<v<<",";
  cout<<" ecc=";for(auto [x,v]:eccentricities)cout<<x<<":"<<v<<",";
  cout<<" pairs=";for(auto [x,v]:pair_hist)cout<<x<<":"<<v<<",";
  cout<<"\n";
  assert(n==(k==4?384:5040));
  assert(edges==(k==4?528:22560));
  assert(radius==diameter && diameter==(k==4?13:10));
  long long sum=0;for(auto [d,c]:pair_hist)sum+=c;
  assert(sum==1LL*n*(n-1)/2);
}
int main(){check(4);check(5);cout<<"COMPLEMENT_EXHAUSTIVE_BOTH_PALETTES_PASS\n";}
