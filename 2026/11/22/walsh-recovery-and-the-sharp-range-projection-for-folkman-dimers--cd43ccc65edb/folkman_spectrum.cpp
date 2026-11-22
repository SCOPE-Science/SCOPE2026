#include <bits/stdc++.h>
using namespace std;
using i64=long long;
struct E{int u,v;};
void fwht(vector<i64>& a){for(size_t h=1;h<a.size();h*=2)for(size_t i=0;i<a.size();i+=2*h)for(size_t j=i;j<i+h;j++){auto x=a[j],y=a[j+h];a[j]=x+y;a[j+h]=x-y;}}
int main(){
 vector<pair<int,int>> pairs; for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)pairs.push_back({i,j});
 vector<E> edges;vector<array<int,4>> inc;
 for(int e=0;e<10;e++){auto [i,j]=pairs[e];array<int,4> a;for(int q=0;q<4;q++){a[q]=(int)edges.size();edges.push_back({10+e,2*(q<2?i:j)+(q&1)});}inc.push_back(a);}
 if(edges.size()!=40){cerr<<"bad graph";return 1;}
 vector<vector<pair<int,int>>> adj(20); for(int e=0;e<40;e++){auto [u,v]=edges[e];adj[u].push_back({v,e});adj[v].push_back({u,e});}
 for(auto a:adj)if(a.size()!=4){cerr<<"degree mismatch";return 2;}
 // BFS tree
 vector<int> seen(20);queue<int> q; seen[0]=1;q.push(0);vector<int> tree(40);int t=0;
 while(!q.empty()){int u=q.front();q.pop();for(auto [v,e]:adj[u])if(!seen[v]){seen[v]=1;tree[e]=1;t++;q.push(v);}}
 if(t!=19) return 3;
 vector<int> chord(40,-1);int nc=0;for(int e=0;e<40;e++)if(!tree[e])chord[e]=nc++;
 if(nc!=21) return 4;
 size_t N=1u<<nc;
 vector<i64> f(N,0);vector<vector<int>> matches;
 array<int,10> ch{};
 function<void(int,unsigned)> dfs=[&](int e,unsigned used){
  if(e==10){unsigned z=0;vector<int> m;for(int k=0;k<10;k++){int id=inc[k][ch[k]];m.push_back(id);if(chord[id]>=0)z^=1u<<chord[id];}f[z]++;matches.push_back(m);return;}
  for(int c=0;c<4;c++){int id=inc[e][c];unsigned s=1u<<edges[id].v;if(!(used&s)){ch[e]=c;dfs(e+1,used|s);}}
 };
 dfs(0,0);
 if(matches.size()!=768) {cerr<<"incorrect matchings: "<<matches.size();return 5;}
 // Independent enumeration: orient every K5 edge toward one endpoint with indegrees exactly 2,
 // then assign the two incoming edges to its two copies.
 vector<i64> g(N,0);int regular=0;int nassign=0;
 for(int orient=0;orient<(1<<10);orient++){
  array<vector<int>,5> in;for(int e=0;e<10;e++){auto [i,j]=pairs[e];int v=((orient>>e)&1)?i:j;in[v].push_back(e);}
  bool ok=1;for(auto v:in)if(v.size()!=2)ok=0;if(!ok)continue;regular++;
  for(int a=0;a<32;a++){
   unsigned z=0;
   for(int i=0;i<5;i++)for(int k=0;k<2;k++){
    int e=in[i][k];int c=(a>>i)&1;int copy=(k^c);int id=(pairs[e].first==i)?inc[e][copy]:inc[e][2+copy];
    if(chord[id]>=0)z^=1u<<chord[id];
   }
   g[z]++;nassign++;
  }
 }
 if(regular!=24||nassign!=768||g!=f){cerr<<"independent enumeration mismatch: "<<regular<<","<<nassign;return 6;}
 long long collisions=0,nonempty=0;for(auto x:f){if(x>1)collisions+=x-1;if(x)nonempty++;}
 vector<i64> F=f;fwht(F);
 map<i64,i64> hist;long long nz=0;long long minabs=LLONG_MAX,maxabs=0;long long pos=0,neg=0;
 vector<i64> support(N);
 for(size_t i=0;i<N;i++){
  auto v=F[i];hist[v]++;
  if(v!=0){nz++;support[i]=1;minabs=min(minabs,llabs(v));maxabs=max(maxabs,llabs(v));if(v>0)pos++;else neg++;}
 }
 if(F[0]!=768 || nz==0)return 7;
 vector<i64> p=support;fwht(p);i64 l1num=0;for(auto v:p)l1num+=llabs(v);
 // check boolean inverse spectrum via second WHT
 fwht(F);for(size_t i=0;i<N;i++)if(F[i]!=(i64)N*f[i]){cerr<<"inversion fail";return 8;}
 cout<<"FOLKMAN_WALSH_PASS\n";
 cout<<"vertices=20 edges=40 tree=19 cycle_rank="<<nc<<"\n";
 cout<<"regular_orientations="<<regular<<" perfect_matchings="<<matches.size()<<"\n";
 cout<<"distinct_chord_patterns="<<nonempty<<" collisions="<<collisions<<"\n";
 cout<<"reduced_characters="<<N<<" nonzero="<<nz<<" zero="<<(N-nz)<<"\n";
 cout<<"full_rank="<<(nz*(1ll<<19))<<" full_nullity="<<((N-nz)*(1ll<<19))<<"\n";
 cout<<"positive="<<pos<<" negative="<<neg<<" minabs="<<minabs<<" maxabs="<<maxabs<<"\n";
 cout<<"projection_L1_fraction="<<l1num<<"/"<<N<<"\n";
 cout<<"levels="<<hist.size()<<"\n";
 for(auto [a,b]:hist)cout<<a<<":"<<b<<" ";cout<<"\n";
 cout<<"tree_edges=";for(int i=0;i<40;i++)if(tree[i])cout<<i<<",";cout<<"\n";
 cout<<"sample_match=";for(auto e:matches[0])cout<<e<<",";cout<<"\n";
 return 0;
}
