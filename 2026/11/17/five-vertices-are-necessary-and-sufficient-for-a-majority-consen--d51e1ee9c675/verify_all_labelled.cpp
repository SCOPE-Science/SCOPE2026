// Exhaustive verification of a five-vertex majority-consensus edge-deletion theorem.
// C++17, no external libraries. Vertex and graph masks are unsigned integers.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct Graph {
 int n; vector<pair<int,int>> edges; vector<unsigned> adj;
 Graph(int sz,unsigned mask):n(sz),adj(sz,0) {
  int k=0;
  for(int i=0;i<n;i++) for(int j=i+1;j<n;j++,k++)
   if(mask & (1U<<k)) {edges.emplace_back(i,j);adj[i]|=1U<<j;adj[j]|=1U<<i;}
 }
 bool connected() const {
  unsigned have=1; unsigned previous=0;
  while(have!=previous) {
   previous=have;
   for(int v=0;v<n;v++) if(have&(1U<<v)) have|=adj[v];
  }
  return have==((1U<<n)-1);
 }
 unsigned successor(unsigned s) const {
  unsigned r=0;
  for(int v=0;v<n;v++) {
   int k=__builtin_popcount(s & adj[v]);
   int d=__builtin_popcount(adj[v]);
   if(2*k>d || (2*k==d && (s & (1U<<v)))) r|=1U<<v;
  }
  return r;
 }
 uint64_t consensus_basin() const {
  int z=1<<n; vector<vector<unsigned>> pre(z);
  for(int s=0;s<z;s++) pre[successor(s)].push_back(s);
  queue<int> q; q.push(0);q.push(z-1);
  uint64_t marked=1ULL | (1ULL<<(z-1));
  while(!q.empty()) {
   int y=q.front();q.pop();
   for(unsigned x:pre[y]) if(!(marked & (1ULL<<x))) {
     marked |= 1ULL<<x; q.push(x);
   }
  }
  return marked;
 }
};

int main(){
 for(int n=2;n<=5;n++) {
  const int nE=n*(n-1)/2;
  unsigned connected_graphs=0, qualifying_pairs=0, deletion_pairs=0;
  unsigned first_mask=0,first_edge=0;bool have=false;
  for(unsigned mask=0;mask<(1U<<nE);mask++){
   Graph G(n,mask);
   if(!G.connected())continue;
   ++connected_graphs;
   uint64_t b=G.consensus_basin();
   for(int k=0;k<nE;k++) if(mask&(1U<<k)) {
    Graph H(n,mask^(1U<<k));
    if(!H.connected())continue;
    ++deletion_pairs;
    uint64_t h=H.consensus_basin();
    unsigned gsz=__builtin_popcountll(b),hsz=__builtin_popcountll(h);
    if(hsz>gsz && (b &~h)) {
     ++qualifying_pairs;
     if(!have)first_mask=mask,first_edge=k,have=true;
    }
   }
  }
  cout<<"n="<<n<<" connected_labelled_graphs="<<connected_graphs
      <<" nonbridge_labelled_edge_deletions="<<deletion_pairs
      <<" gain_and_loss_pairs="<<qualifying_pairs;
  if(have)cout<<" first_graph_mask="<<first_mask<<" first_deleted_index="<<first_edge;
  cout<<"\n";
 }
 const array<pair<int,int>,6> A={{{0,1},{0,2},{0,3},{0,4},{1,2},{1,3}}};
 const array<pair<int,int>,6> B={{{0,1},{0,3},{0,4},{1,2},{2,3},{3,4}}};
 auto report=[](const array<pair<int,int>,6>& E,pair<int,int> removal,const char* name){
  unsigned m=0,del=0;int k=0;
  for(int i=0;i<5;i++)for(int j=i+1;j<5;j++,k++){
   for(auto p:E) if(p==make_pair(i,j)) m|=1U<<k;
   if(make_pair(i,j)==removal)del=1U<<k;
  }
  Graph G(5,m),H(5,m^del);
  auto x=G.consensus_basin(),y=H.consensus_basin();
  cout<<name<<" Gmask="<<m<<" deleted_bit="<<del
    <<" G_basin="<<__builtin_popcountll(x)<<" H_basin="<<__builtin_popcountll(y)
    <<" lost="<<__builtin_popcountll(x&~y)<<" gained="<<__builtin_popcountll(y&~x)<<"\n";
  cout<<"lost_states=";for(int s=0;s<32;s++)if((x&~y)&(1ULL<<s))cout<<s<<",";cout<<"\n";
  cout<<"gained_states=";for(int s=0;s<32;s++)if((y&~x)&(1ULL<<s))cout<<s<<",";cout<<"\n";
 };
 report(A,{1,2},"diamond_leaf");
 report(B,{0,4},"house");
}
