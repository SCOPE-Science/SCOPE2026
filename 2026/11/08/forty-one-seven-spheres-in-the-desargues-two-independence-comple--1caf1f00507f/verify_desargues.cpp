// Reproducible finite verification for the Desargues P3-devoid complex.
// C++17; compile: g++ -O2 -std=c++17 verify_desargues.cpp -o verify && ./verify
// Only graph definitions, face tests, pairings and finite poset checks are used.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <vector>
using namespace std;
static constexpr int n=20, N=1<<20;
void require(bool b,const char*msg){if(!b){cerr<<"FAILED: "<<msg<<"\n";exit(1);}}
struct Graph{
 array<unsigned,20> adj{};
 void edge(int u,int v){require(u!=v,"loop");adj[u]|=1u<<v;adj[v]|=1u<<u;}
 bool has(int u,int v)const{return (adj[u]>>v)&1u;}
 int edges()const{int e=0;for(auto x:adj)e+=__builtin_popcount(x);return e/2;}
};
Graph generalized_petersen(){Graph g;for(int i=0;i<10;i++){
 g.edge(i,(i+1)%10);g.edge(i,10+i);g.edge(10+i,10+(i+3)%10);
}return g;}
Graph incidence_graph(){Graph g;
 array<unsigned,20> subsets{};int p=0;
 for(int a=0;a<5;a++)for(int b=a+1;b<5;b++)subsets[p++]=(1u<<a)|(1u<<b);
 for(int a=0;a<5;a++)for(int b=a+1;b<5;b++)for(int c=b+1;c<5;c++)
  subsets[p++]=(1u<<a)|(1u<<b)|(1u<<c);
 require(p==20,"incidence graph vertices");
 for(int a=0;a<10;a++)for(int b=10;b<20;b++)
   if((subsets[a]&subsets[b])==subsets[a])g.edge(a,b);
 return g;
}
vector<unsigned char> faces_by_degree(const Graph &g){
 vector<unsigned char> ok(N,0);ok[0]=1;
 for(unsigned s=1;s<(unsigned)N;s++){
  int v=__builtin_ctz(s), t=s&(s-1);
  if(!ok[t])continue;
  unsigned neighbors=g.adj[v]&t;
  if((neighbors&(neighbors-1u))!=0)continue;
  if(neighbors && (g.adj[__builtin_ctz(neighbors)]&t))continue;
  ok[s]=1;
 }
 return ok;
}
vector<unsigned char> faces_by_three_paths(const Graph &h, const array<int,20> &gp_to_inc){
 array<int,20> inc_to_gp{};
 array<unsigned char,20> seen{};
 for(int i=0;i<20;i++){require(gp_to_inc[i]>=0&&gp_to_inc[i]<20,"map range");
  require(!seen[gp_to_inc[i]],"map injective");seen[gp_to_inc[i]]=1;inc_to_gp[gp_to_inc[i]]=i;
 }
 vector<unsigned> forb;
 for(int m=0;m<20;m++){
  vector<int> nb;for(int i=0;i<20;i++)if(h.has(m,i))nb.push_back(i);
  for(int i=0;i<(int)nb.size();i++)for(int j=i+1;j<(int)nb.size();j++)
   forb.push_back((1u<<inc_to_gp[m])|(1u<<inc_to_gp[nb[i]])|(1u<<inc_to_gp[nb[j]]));
 }
 sort(forb.begin(),forb.end());forb.erase(unique(forb.begin(),forb.end()),forb.end());
 require(forb.size()==60,"sixty three-path obstructions");
 vector<vector<unsigned>> contains(20);
 for(unsigned f:forb)for(int i=0;i<20;i++)if((f>>i)&1u)contains[i].push_back(f);
 vector<unsigned char> ok(N,0);ok[0]=1;
 for(unsigned s=1;s<(unsigned)N;s++){
  int v=__builtin_ctz(s),t=s&(s-1); if(!ok[t])continue;
  bool allowed=true;
  for(unsigned f:contains[v])if((s&f)==f){allowed=false;break;}
  if(allowed)ok[s]=1;
 }
 return ok;
}
struct MorseOutput {int pairs=0,critical_zero=0,critical_seven=0;long long incidences=0;int processed=0;array<int,20> critical{};};
MorseOutput verify_morse(const vector<unsigned char>& ok, const array<int,20>&order){
 vector<int> pair(N,-1);
 for(int v:order){unsigned bit=1u<<v;
  for(unsigned s=1;s<(unsigned)N;s++){
   if(!ok[s]||pair[s]!=-1||(s&bit))continue;
   unsigned t=s|bit;
   if(ok[t]&&pair[t]==-1){pair[s]=t;pair[t]=s;}
  }
 }
 MorseOutput o;
 for(unsigned s=1;s<(unsigned)N;s++)if(ok[s]){
   if(pair[s]==-1)o.critical[__builtin_popcount(s)-1]++;
   else if((unsigned)pair[s]>s)o.pairs++;
 }
 for(int i=0;i<20;i++){
  if(i==0)o.critical_zero=o.critical[i];
  if(i==7)o.critical_seven=o.critical[i];
  if(i!=0&&i!=7)require(!o.critical[i],"wrong critical dimension");
 }
 require(o.critical_zero==1&&o.critical_seven==41,"critical cell profile");
 // Reorient the full nonempty-face Hasse diagram: matched edges point up.
 // At each topological-sort step, traverse unmatched downward and (if lower) matched upward.
 vector<int> indeg(N,0);
 for(unsigned s=1;s<(unsigned)N;s++)if(ok[s]){
  for(unsigned bits=s;bits;bits&=bits-1){
   unsigned t=s^(1u<<__builtin_ctz(bits));if(!t)continue;
   o.incidences++;
   if(pair[t]==(int)s)indeg[s]++;else indeg[t]++;
  }
 }
 vector<unsigned> queue;queue.reserve(70000);
 for(unsigned s=1;s<(unsigned)N;s++)if(ok[s]&&indeg[s]==0)queue.push_back(s);
 for(size_t head=0;head<queue.size();head++){
  unsigned s=queue[head];
  for(unsigned bits=s;bits;bits&=bits-1){
   unsigned t=s^(1u<<__builtin_ctz(bits));if(!t||pair[t]==(int)s)continue;
   if(--indeg[t]==0)queue.push_back(t);
  }
  if(pair[s]>(int)s){unsigned t=pair[s];if(--indeg[t]==0)queue.push_back(t);}
 }
 o.processed=queue.size();
 require(o.processed==62048,"acyclicity failed");
 require(o.incidences==400760,"face-poset incidence count");
 require(o.pairs==31003,"pair count");
 return o;
}
int main(){
 const Graph gp=generalized_petersen(), inc=incidence_graph();
 require(gp.edges()==30&&inc.edges()==30,"30 edges in both representations");
 for(auto g:{gp,inc})for(unsigned x:g.adj)require(__builtin_popcount(x)==3,"cubic graph");
 const array<int,20> gp_to_inc={0,10,4,16,7,19,9,15,3,12,11,1,17,5,13,8,18,2,14,6};
 for(int u=0;u<20;u++)for(int v=0;v<20;v++)
  require(gp.has(u,v)==inc.has(gp_to_inc[u],gp_to_inc[v]),"verified isomorphism");
 const auto a=faces_by_degree(gp),b=faces_by_three_paths(inc,gp_to_inc);
 require(a==b,"independently computed face families disagree");
 array<int,13> facevec{},facets{};
 int total=0;long long euler=0;
 for(unsigned s=1;s<(unsigned)N;s++)if(a[s]){
  int size=__builtin_popcount(s);require(size<=12,"facet dimension check");
  facevec[size]++;total++;euler+=size%2?-1:1;
  bool maximal=true;
  for(int v=0;v<20;v++)if(!(s&(1u<<v))&&a[s|(1u<<v)]){maximal=false;break;}
  if(maximal)facets[size]++;
 }
 require(total==62048,"total face count");
 require(euler==40,"Euler characteristic");
 cout<<"GP(10,3) and 2-subset/3-subset incidence graph: 20 vertices, 30 edges; all adjacencies verified\n";
 cout<<"Independent degree-test and three-path-test face enumerations: IDENTICAL\n";
 cout<<"nonempty_faces="<<total<<" face_counts_by_cardinality=";
 for(int i=1;i<=12;i++){cout<<(i==1?"":",")<<facevec[i];}cout<<"\n";
 cout<<"maximal_face_counts_by_cardinality=";
 for(int i=1;i<=12;i++){cout<<(i==1?"":",")<<facets[i];}cout<<"\n";
 cout<<"Euler="<<-euler<<" reduced_Euler="<<-euler-1<<"\n"; // standard alternating sum of face counts is -euler
 for(int mult:{7,3}){
  array<int,20> order{};for(int i=0;i<20;i++)order[i]=(mult*i)%20;
  const auto out=verify_morse(a,order);
  cout<<"matching_order_multiplier="<<mult<<" matched_pairs="<<out.pairs
      <<" critical_vertex="<<out.critical_zero<<" critical_7_cells="<<out.critical_seven
      <<" oriented_Hasse_edges="<<out.incidences<<" topologically_processed="<<out.processed<<"\n";
 }
 cout<<"ALL_CHECKS_PASS\n";
}
