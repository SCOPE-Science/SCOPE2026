// Exhaustive direct signed-forest sums, independent of Walsh transforms.
#include <array>
#include <vector>
#include <map>
#include <iostream>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <cstdint>
using namespace std;
int main(){
 constexpr int n=6,m=15,N=1<<15;
 vector<pair<int,int>> E;
 for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)E.push_back({a,b});
 assert((int)E.size()==m);
 vector<int> forests;
 for(int mask=0;mask<N;mask++){
   bool adj[6][6]={};
   for(int i=0;i<m;i++)if(mask&(1<<i)){
      auto [u,v]=E[i];adj[u][v]=adj[v][u]=true;
   }
   bool seen[6]={};
   bool acyclic=true;
   auto walk=[&](auto&& walk,int v,int par)->void{
      seen[v]=true;
      for(int u=0;u<n;u++)if(adj[v][u]){
         if(!seen[u])walk(walk,u,v);
         else if(u!=par)acyclic=false;
      }
   };
   for(int v=0;v<n;v++)if(!seen[v])walk(walk,v,-1);
   if(acyclic)forests.push_back(mask);
 }
 assert(forests.size()==2932);
 vector<int> W(N,0);
 for(int s=0;s<N;s++){
   int val=0;
   for(int F:forests) val+= (__builtin_parity((unsigned)(s&F))?-1:1);
   W[s]=val;
 }
 int zeros=0,gap=99999, greatest=0;
 map<int,int> by_size, levels;
 long long parseval=0;
 for(int i=0;i<N;i++){
   int w=W[i];levels[w]++;parseval+=1LL*w*w;
   greatest=gcd(greatest,abs(w));
   if(w==0){zeros++;by_size[__builtin_popcount((unsigned)i)]++;}
   else gap=min(gap,abs(w));
 }
 assert(zeros==3105 && gap==4 && greatest==4 && levels.size()==49);
 const map<int,int> expected_by_size = {{5,180},{7,1080},{9,1800},{11,45}};
 assert(by_size==expected_by_size);
 assert(parseval==1LL*N*(int)forests.size());
 assert(levels.at(2932)==1 && levels.at(-560)==1);
 // Independently compute the projection kernel norm by 156 unlabeled-graph orbits.
 // This uses *direct* character sums over the support, not a fast Walsh transform.
 vector<array<int,m>> edge_maps;
 auto find_edge=[&](int a,int b)->int{if(a>b)swap(a,b);for(int e=0;e<m;e++)if(E[e]==make_pair(a,b))return e;assert(false);return -1;};
 array<int,n> p={0,1,2,3,4,5};
 do {
   array<int,m> mapedge{};
   for(int e=0;e<m;e++)mapedge[e]=find_edge(p[E[e].first],p[E[e].second]);
   edge_maps.push_back(mapedge);
 }while(next_permutation(p.begin(),p.end()));
 assert(edge_maps.size()==720);
 vector<unsigned char> seen_freq(N,0);
 vector<pair<int,int>> orbits;
 for(int r=0;r<N;r++)if(!seen_freq[r]){
   int count=0;
   for(const auto& pm:edge_maps){
     int v=0;
     for(int e=0;e<m;e++)if(r&(1<<e))v|=(1<<pm[e]);
     if(!seen_freq[v]){seen_freq[v]=1;count++;}
   }
   orbits.push_back({r,count});
 }
 assert(orbits.size()==156);
 long long normNumerator=0;
 for(auto [r, multiplicity]:orbits){
   int kernel=0;
   for(int s=0;s<N;s++)if(W[s]!=0)
     kernel+=__builtin_parity((unsigned)(r&s))?-1:1;
   normNumerator+=1LL*multiplicity*abs(kernel);
 }
 assert(normNumerator==1210058);
 int normalizer=gcd((int)normNumerator,N);
 assert(normNumerator/normalizer==605029 && N/normalizer==16384);
 // Verify precisely ten orbits of vanishing Fourier characters.
 int zero_orbits=0;
 for(auto [r, mult]:orbits)if(W[r]==0)zero_orbits++;
 assert(zero_orbits==10);
 cout<<"SIGNED_LEVELS=";for(const auto &p:levels)cout<<p.first<<":"<<p.second<<";";cout<<"\n";
 cout<<"DIRECT_CHECK_OK forests="<<forests.size()<<" zeros="<<zeros
     <<" nonzero="<<N-zeros<<" levels="<<levels.size()<<" gap="<<gap
     <<" gcd="<<greatest<<" parseval="<<parseval<<" zero_orbits="<<zero_orbits
     <<" projection_norm=605029/16384\n";
 return 0;
}
