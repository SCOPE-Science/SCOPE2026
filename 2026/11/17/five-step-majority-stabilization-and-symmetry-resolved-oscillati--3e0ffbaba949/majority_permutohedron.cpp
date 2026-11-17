#include <bits/stdc++.h>
using namespace std;
static constexpr int N=24, M=1<<N;
static uint32_t nxt[M];
static uint8_t neigh[N][3];
static uint8_t perm24[N][4];
static uint32_t transbit[48][N];
uint32_t apply(uint32_t x){
 uint32_t y=0;
 for(int i=0;i<N;i++){
  int a=(x>>neigh[i][0])&1, b=(x>>neigh[i][1])&1, c=(x>>neigh[i][2])&1;
  y |= ((a+b+c)>=2) ? (1u<<i):0;
 }
 return y;
}
int main(){
 vector<array<int,4>> p;
 array<int,4> q{0,1,2,3};do {p.push_back(q);}while(next_permutation(q.begin(),q.end()));
 map<array<int,4>,int> id;for(int i=0;i<N;i++){id[p[i]]=i; for(int j=0;j<4;j++)perm24[i][j]=p[i][j];}
 for(int i=0;i<N;i++){for(int j=0;j<3;j++){auto b=p[i];swap(b[j],b[j+1]); neigh[i][j]=id.at(b);}}
 // 24 value permutations, and independent position reversal automorphism
 for(int a=0;a<24;a++)for(int rev=0;rev<2;rev++)for(int i=0;i<24;i++){
    array<int,4> b;
    for(int j=0;j<4;j++){int x=p[i][rev?3-j:j];b[j]=p[a][x];}
    transbit[a*2+rev][i]=1u<<id.at(b);
 }
 // All 48 permutations are distinct full-graph automorphisms.
 set<array<uint32_t,N>> distinct;
 for(int g=0;g<48;g++){
    array<uint32_t,N> row{};
    for(int i=0;i<N;i++){
       row[i]=transbit[g][i];
       int new_i=__builtin_ctz(row[i]);
       for(int k=0;k<3;k++){
         int j=neigh[i][k],new_j=__builtin_ctz(transbit[g][j]);
         assert(neigh[new_i][0]==new_j||neigh[new_i][1]==new_j||neigh[new_i][2]==new_j);
       }
    }
    distinct.insert(row);
 }
 assert(distinct.size()==48);
 for(int i=0;i<24;i++)for(int k=0;k<3;k++) assert(neigh[neigh[i][k]][0]==i||neigh[neigh[i][k]][1]==i||neigh[neigh[i][k]][2]==i);
 for(uint32_t x=0;x<M;x++)nxt[x]=apply(x);
 cerr << "map_ready" << endl;
 vector<unsigned long long> fixed_by_depth(64),cycle2_by_depth(64);
 unsigned long long rec_fixed=0,rec_period2=0; int maxd=-1; unsigned long long distance_state=0;
 map<int,unsigned long long> recurrent_by_weight,fix_by_weight; uint32_t witness=UINT32_MAX;
 for(uint32_t x=0;x<M;x++){
  uint32_t y=x;int d=0;
  while(true){uint32_t z=nxt[y], zz=nxt[z];if(zz==y){bool fixed=(z==y);if(fixed)fixed_by_depth[d]++;else cycle2_by_depth[d]++;if(d==0){if(fixed){rec_fixed++;fix_by_weight[__builtin_popcount(x)]++;}else rec_period2++;recurrent_by_weight[__builtin_popcount(x)]++;}break;}
   y=z;d++; if(d>=64){cerr<<"excess depth "<<x<<endl;return 1;}
  }
  if(d==5 && witness==UINT32_MAX) witness=x;maxd=max(maxd,d);distance_state+=d;
 }
 cout<<"{\"vertices\":24,\"states\":"<<M<<",\"fixed\":"<<rec_fixed<<",\"period2_states\":"<<rec_period2<<",\"period2_orbits\":"<<rec_period2/2<<",\"max_transient\":"<<maxd<<",\"depth_sum\":"<<distance_state<<",\"fixed_entry\":[";
 for(int d=0;d<=maxd;d++)cout<<(d?",":"")<<fixed_by_depth[d];cout<<"],\"period2_entry\":[";
 for(int d=0;d<=maxd;d++)cout<<(d?",":"")<<cycle2_by_depth[d];cout<<"],\"recurrent_weight\":{";
 int count=0;for(auto [wt,v]:recurrent_by_weight)cout<<(count++?",":"")<<"\""<<wt<<"\":"<<v;cout<<"},\"fixed_by_weight\":{";count=0;for(auto [wt,v]:fix_by_weight)cout<<(count++?",":"")<<"\""<<wt<<"\":"<<v;cout<<"},\"first_depth_five_witness\":"<<witness<<"}\n";
 // Symmetry classify recurrent configurations; period2 quotient phase
 auto transform=[&](uint32_t x,int g){uint32_t y=0;while(x){int b=__builtin_ctz(x);x&=x-1;y|=transbit[g][b];}return y;};
 unordered_set<uint32_t> seenfixed,seen2;
 map<int,int> fixed_orbits,orbit2;map<int,int> fixed_orbits_weight,period2_orbits_weight;
 for(uint32_t x=0;x<M;x++){
  if(nxt[x]==x && !seenfixed.count(x)){
   set<uint32_t> orbit;
   for(int g=0;g<48;g++)orbit.insert(transform(x,g));
   for(auto y:orbit)seenfixed.insert(y);
   fixed_orbits[orbit.size()]++; fixed_orbits_weight[__builtin_popcount(x)]++;
  }
  if(nxt[nxt[x]]==x&&nxt[x]!=x){uint32_t c=min(x,nxt[x]); if(seen2.count(c))continue;
    set<uint32_t> orb;
    for(int g=0;g<48;g++){uint32_t u=transform(x,g);orb.insert(min(u,nxt[u]));}
    for(auto y:orb)seen2.insert(y);
    orbit2[orb.size()]++;period2_orbits_weight[__builtin_popcount(x)]++;
  }
 }
 cerr<<"fixed orbit-size types: "<<fixed_orbits.size()<<endl;
 cout<<"{\"fixed_symmetry_orbit_sizes\":{";count=0;for(auto [a,b]:fixed_orbits)cout<<(count++?",":"")<<"\""<<a<<"\":"<<b;cout<<"},\"period2_symmetry_orbit_sizes\":{";count=0;for(auto [a,b]:orbit2)cout<<(count++?",":"")<<"\""<<a<<"\":"<<b;cout<<"},\"fixed_symmetry_classes\":"<<accumulate(fixed_orbits.begin(),fixed_orbits.end(),0,[](int t,const auto&kv){return t+kv.second;})<<",\"period2_symmetry_classes\":"<<accumulate(orbit2.begin(),orbit2.end(),0,[](int t,const auto&kv){return t+kv.second;})<<"}\n";
}
