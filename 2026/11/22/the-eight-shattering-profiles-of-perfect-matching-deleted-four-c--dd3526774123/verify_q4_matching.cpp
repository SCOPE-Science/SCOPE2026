// Deterministic exhaustive checker for vertex-membership shattering of
// maximal independent sets after perfect-matching deletion in the 4-cube.
// Compile: g++ -std=c++17 -O2 verify_q4_matching.cpp -o verify && ./verify
#include <bits/stdc++.h>
using namespace std;
using U=uint32_t; using Match=vector<pair<int,int>>;
constexpr int N=16;
constexpr U ALL=(1u<<N)-1;
using Vec7=array<int,7>;
vector<Match> matchings;
vector<array<int,N>> cubeAutos;
vector<pair<int,int>> cubeEdges;
array<U,N> cubeAdj{};
int bitIndex(U b){return __builtin_ctz(b);}
void generateMatchings(U remaining, Match &m) {
 if (!remaining) {Match x=m;sort(x.begin(),x.end());matchings.push_back(x);return;}
 int u=bitIndex(remaining);
 U next=(remaining & ~(1u<<u)) & cubeAdj[u];
 while(next){U b=next&-next;next-=b;int v=bitIndex(b);m.push_back({u,v});generateMatchings(remaining&~(1u<<u)&~b,m);m.pop_back();}
}
Match transform(const Match &m, const array<int,N> &p){
 Match out;
 for(auto [u,v]:m){int x=p[u],y=p[v];if(x>y)swap(x,y);out.push_back({x,y});}
 sort(out.begin(),out.end());return out;
}
vector<U> maximalIndependentSets(const array<U,N>& adj){
 array<U,N> compat{};
 for(int i=0;i<N;++i)compat[i]=ALL & ~(adj[i]|(1u<<i));
 vector<U> out;
 function<void(U,U,U)> bk=[&](U R,U P,U X){
   if(!P&&!X){out.push_back(R);return;}
   while(P){U b=P&-P;P-=b;int v=bitIndex(b);
      bk(R|b,P&compat[v],X&compat[v]);X|=b;
   }
 };
 bk(0,ALL,0);
 sort(out.begin(),out.end());return out;
}
struct Stats{Vec7 polynomial{}, facets{}; map<int,int> misSizes;};
Stats calculate(const Match& m) {
 array<U,N> adj=cubeAdj;
 for(auto [u,v]:m){adj[u]&=~(1u<<v);adj[v]&=~(1u<<u);}
 auto mis=maximalIndependentSets(adj);
 Stats out;
 for(U r:mis)out.misSizes[__builtin_popcount(r)]++;
 vector<unsigned char> face(1<<N,0);
 for(U s=0;s<(1u<<N);++s){
  int k=__builtin_popcount(s);
  if(k>=7 || (1u<<k)>mis.size())continue;
  bool independent=true;
  for(U t=s;t;){U b=t&-t;t-=b;if(adj[bitIndex(b)]&t){independent=false;break;}}
  if(!independent)continue;
  int vs[16],cnt=0;
  for(int v=0;v<N;++v)if(s>>v&1)vs[cnt++]=v;
  uint64_t traces=0;
  for(U r:mis){
   int id=0;
   for(int j=0;j<k;++j)if(r>>vs[j]&1)id|=1<<j;
   traces|=1ull<<id;
  }
  if(__builtin_popcountll(traces)==(1<<k)){face[s]=1;out.polynomial[k]++;}
 }
 for(U s=0;s<(1u<<N);++s)if(face[s]){
  bool maximal=true;
  for(int i=0;i<N;++i)if(!(s>>i&1) && face[s|(1u<<i)]){maximal=false;break;}
  if(maximal)out.facets[__builtin_popcount(s)]++;
 }
 return out;
}
void printVec(const Vec7&v){cout<<'[';for(int i=0;i<7;++i){if(i)cout<<',';cout<<v[i];}cout<<']';}
int main(){
 for(int v=0;v<N;++v)for(int j=0;j<4;++j){int w=v^(1<<j);cubeAdj[v]|=1u<<w;if(v<w)cubeEdges.push_back({v,w});}
 Match x;generateMatchings(ALL,x);sort(matchings.begin(),matchings.end());
 if(matchings.size()!=272){cerr<<"Unexpected perfect matching count "<<matchings.size()<<'\n';return 1;}
 array<int,4> pi={0,1,2,3};
 do{for(int t=0;t<N;++t){array<int,N> p{};for(int v=0;v<N;++v){int w=t;for(int i=0;i<4;++i)if(v>>i&1)w^=1<<pi[i];p[v]=w;}cubeAutos.push_back(p);}}while(next_permutation(pi.begin(),pi.end()));
 if(cubeAutos.size()!=384){cerr<<"wrong automorphism group size";return 1;}
 set<Match> pending(matchings.begin(),matchings.end());
 const int expectedOrbit[]={4,48,24,48,96,12,32,8};
 const Vec7 expectedPoly[]={
  {1,16,96,256,256,0,0},{1,16,96,240,168,0,0},
  {1,16,96,224,88,0,0},{1,16,96,232,120,0,0},
  {1,16,96,240,169,0,0},{1,16,96,256,256,0,0},
  {1,16,96,248,209,36,0},{1,16,96,272,296,48,0}};
 const Vec7 expectedFacets[]={
  {0,0,0,0,256,0,0},{0,0,0,24,168,0,0},
  {0,0,0,64,88,0,0},{0,0,0,24,120,0,0},
  {0,0,0,16,169,0,0},{0,0,0,0,256,0,0},
  {0,0,0,12,77,36,0},{0,0,0,0,128,48,0}};
 int i=0,countsVC5=0,pureCount=0;
 while(!pending.empty()){
  auto rep=*pending.begin();set<Match> orb;
  for(auto &p:cubeAutos)orb.insert(transform(rep,p));
  for(auto &y:orb)if(!pending.erase(y)){cerr<<"nonpartition orbit\n";return 1;}
  // For the eight-member class, a fixed relabeling identifies the retained
  // graph with the generalized Petersen graph GP(8,3).
  if(i==7){
    const int label[N]={0,10,8,13,7,15,6,5,1,2,11,3,9,12,14,4};
    set<pair<int,int>> imageEdges;
    for(auto [u,v]:cubeEdges)if(find(rep.begin(),rep.end(),make_pair(u,v))==rep.end()){
      int a=label[u],b=label[v];if(a>b)swap(a,b);imageEdges.insert({a,b});
    }
    set<pair<int,int>> gpEdges;
    auto add=[&](int a,int b){if(a>b)swap(a,b);gpEdges.insert({a,b});};
    for(int j=0;j<8;++j){add(j,(j+1)%8);add(j,j+8);add(j+8,8+(j+3)%8);}
    if(imageEdges!=gpEdges){cerr<<"GP(8,3) graph identity failed\n";return 1;}
  }
  auto stats=calculate(rep);
  if(i>=8 || (int)orb.size()!=expectedOrbit[i] || stats.polynomial!=expectedPoly[i] || stats.facets!=expectedFacets[i]){
   cerr<<"Mismatch class "<<i<<'\n';return 1;
  }
  cout<<"class="<<i+1<<" orbit="<<orb.size()<<" concept_sizes=";
  for(auto[k,v]:stats.misSizes)cout<<k<<':'<<v<<',';
  cout<<" shattered=";printVec(stats.polynomial);
  cout<<" facets=";printVec(stats.facets);cout<<'\n';
  if(stats.polynomial[5])countsVC5+=orb.size();
  if(stats.facets[5]+stats.facets[4]+stats.facets[3] == stats.facets[4] && !stats.facets[3])pureCount+=orb.size();
  ++i;
 }
 if(i!=8 || countsVC5!=40 || pureCount!=16){cerr<<"wrong overall invariants\n";return 1;}
 cout<<"Q4_MATCHING_SHATTER_PASS matchings=272 orbits=8 vc5=40 pure=16\n";
 return 0;
}
