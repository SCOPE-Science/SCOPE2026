// Exact finite verification of a strong metric dimension at order 25.
// Build: g++ -O2 -std=c++17 gp25_independent.cpp -o gp25_independent
#include <array>
#include <vector>
#include <queue>
#include <iostream>
#include <cstdint>
#include <cassert>
using namespace std;
constexpr int n=25, N=50;
using Matrix=array<array<int,N>,N>;
int main(){
  array<vector<int>,N> G;
  auto edge=[&](int a,int b){G[a].push_back(b);G[b].push_back(a);};
  for(int i=0;i<n;++i){edge(i,(i+1)%n);edge(i,n+i);edge(n+i,n+(i+2)%n);}
  for(int i=0;i<N;++i)assert(G[i].size()==3);
  Matrix d{};
  for(int src=0;src<N;++src){
    d[src].fill(-1);d[src][src]=0;queue<int> q;q.push(src);
    while(!q.empty()){int a=q.front();q.pop();for(int b:G[a])if(d[src][b]<0){d[src][b]=d[src][a]+1;q.push(b);}}
    for(int v=0;v<N;++v)assert(d[src][v]>=0);
  }
  array<array<bool,N>,N> M{};int uu=0,vv=0,mixed=0;
  for(int a=0;a<N;++a)for(int b=a+1;b<N;++b){
    bool m=true;
    for(int x:G[a])if(d[x][b]>d[a][b])m=false;
    for(int y:G[b])if(d[a][y]>d[a][b])m=false;
    M[a][b]=M[b][a]=m;
    if(m){if(a<n && b<n)++uu;else if(a>=n && b>=n)++vv;else ++mixed;}
    bool predicted=false;
    if(a<n && b<n){int delta=(b-a)%n;for(int z:{5,7,9,11,12})if(delta==z||delta==n-z)predicted=true;}
    else if(a>=n && b>=n){int delta=(b-a)%n;for(int z:{9,11})if(delta==z||delta==n-z)predicted=true;}
    assert(m==predicted);
  }
  assert(uu==125&&vv==50&&mixed==0);
  // Here a position is initially unselected precisely if its layer index
  // belongs to one of the two explicit independent sets.
  array<bool,N> omitted{};
  for(int z:{6,8,10,12,14,16})omitted[z]=true;
  for(int z:{2,4,7,9,12,14,17,19,22,24})omitted[n+z]=true;
  int selected=0,unresolved=0;
  for(int x=0;x<N;++x)selected+=!omitted[x];
  assert(selected==34);
  for(int a=0;a<N;++a)for(int b=a+1;b<N;++b){
    if(M[a][b])assert(!omitted[a] || !omitted[b]);
    bool resolves=false;
    for(int z=0;z<N;++z)if(!omitted[z]){
      if(d[z][a]==d[z][b]+d[a][b]||d[z][b]==d[z][a]+d[a][b]){resolves=true;break;}
    }
    if(!resolves)++unresolved;
  }
  assert(unresolved==0);
  // Complete enumeration of subsets of each 25-vertex layer. An independent
  // set larger than r would contain an independent set of size r+1.
  // Iteration over increasing combinations is exhaustive: every r-subset
  // is represented by exactly one increasing list.
  auto countIndependent=[&](int off,int target){
    long long valid=0, tested=0;
    vector<int> a(target);
    auto rec=[&](auto&& self,int depth,int start)->void{
      if(depth==target){++valid;++tested;return;}
      for(int x=start;x<=n-(target-depth);++x){
        bool ok=true;
        for(int j=0;j<depth;++j)if(M[off+x][off+a[j]]){ok=false;break;}
        if(!ok)continue;
        a[depth]=x;self(self,depth+1,x+1);
      }
    };
    rec(rec,0,0);
    return valid;
  };
  long long iu6=countIndependent(0,6),iu7=countIndependent(0,7);
  long long iv10=countIndependent(n,10),iv11=countIndependent(n,11);
  assert(iu6>0 && iu7==0 && iv10>0 && iv11==0);
  cout<<"uu="<<uu<<" vv="<<vv<<" cross="<<mixed<<" direct_pairs="<<N*(N-1)/2<<" unresolved="<<unresolved<<"\n";
  cout<<"independent U6="<<iu6<<" U7="<<iu7<<" V10="<<iv10<<" V11="<<iv11<<"\n";
  cout<<"minimum strong metric dimension="<<selected<<" minimum bases="<<iu6*iv10<<"\n";
}
