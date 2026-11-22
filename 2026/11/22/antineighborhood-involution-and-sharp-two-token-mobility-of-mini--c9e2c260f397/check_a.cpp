// Finite verification of minimum 2-rainbow domination in the Clebsch graph.
// C++17; compile: g++ -std=c++17 -O2 check_a.cpp -o check_a && ./check_a
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
static int bits(unsigned x) {return __builtin_popcount(x);}
int main() {
  constexpr int n=16, ALL=(1<<16)-1;
  unsigned N[n]{};
  for(int x=0;x<n;x++) for(int d:{1,2,4,8,15}) N[x]|=1u<<(x^d);
  for(int x=0;x<n;x++){assert(bits(N[x])==5);for(int y=0;y<n;y++)
    assert(bool(N[x]&(1u<<y))==bool(N[y]&(1u<<x)));}
  vector<unsigned> cover(1<<16);for(int x=1;x<(1<<16);x++){
    int j=__builtin_ctz((unsigned)x);cover[x]=cover[x^(1<<j)]|N[j];}
  vector<vector<unsigned>> masks(17);
  for(unsigned m=0;m<(1u<<16);m++)masks[bits(m)].push_back(m);
  vector<pair<unsigned,unsigned>> F;
  for(int w=0;w<=6;w++) {
    int cnt=0;
    for(int a=0;a<=w;a++)for(unsigned A:masks[a])for(unsigned B:masks[w-a]){
      unsigned blank=ALL^(A|B);
      if((blank&~cover[A])==0&&(blank&~cover[B])==0){
        cnt++;if(w==6)F.emplace_back(A,B);
      }
    }
    if(w<6) assert(cnt==0);
    if(w==6) assert(cnt==320);
    cout<<"weight_"<<w<<"="<<cnt<<"\n";
  }
  sort(F.begin(),F.end());assert(unique(F.begin(),F.end())==F.end());
  map<int,int> t;for(auto [A,B]:F){assert(bits(A)==3&&bits(B)==3&&!(A&B));
    int e=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)
      if((A>>i&1)&&(A>>j&1)&&(N[i]>>j&1))e++;
    t[e]++;
    assert(B==(unsigned)(ALL^(A|cover[A])));
    assert(A==(unsigned)(ALL^(B|cover[B])));
  }
  assert(t[0]==160&&t[2]==160&&t.size()==2);
  cout<<"independent_first="<<t[0]<<" path_first="<<t[2]<<"\n";
  int m=F.size();vector<vector<int>> adj(m);map<pair<int,int>,int> pairdist;int e=0;
  long long counts[7]{};
  for(int i=0;i<m;i++)for(int j=i+1;j<m;j++){
    int da=bits(F[i].first^F[j].first)/2;
    int db=bits(F[i].second^F[j].second)/2;
    counts[da+db]++;
    if(da+db==1)assert(false);
    if(da+db==2){assert(da==1&&db==1);adj[i].push_back(j);adj[j].push_back(i);e++;}
  }
  assert(e==1440&&counts[2]==1440&&counts[3]==2880&&counts[4]==13920&&counts[5]==14400&&counts[6]==18400);
  int S[6]={1,9,54,159,90,7};long long wiener_twice=0;
  int triangle_thrice=0;
  for(int i=0;i<m;i++){
    assert(adj[i].size()==9);
    vector<int> dist(m,-1);dist[i]=0;queue<int> q;q.push(i);
    while(!q.empty()){int u=q.front();q.pop();for(int v:adj[u])if(dist[v]<0){dist[v]=dist[u]+1;q.push(v);}}
    int shell[6]{};for(int d:dist){assert(d>=0&&d<=5);shell[d]++;wiener_twice+=d;}
    for(int j=0;j<6;j++)assert(shell[j]==S[j]);
    for(int j:adj[i])for(int k:adj[j])if(k!=i&&find(adj[i].begin(),adj[i].end(),k)!=adj[i].end())triangle_thrice++;
  }
  assert(triangle_thrice==0&&wiener_twice/2==158240);
  cout<<"optima=320 one_token_edges=0 two_token_edges="<<e<<"\n";
  cout<<"two_token_degree=9 diameter=5 shells=1,9,54,159,90,7\n";
  cout<<"triangles=0 wiener="<<wiener_twice/2<<"\n";
}
