// Exact full Walsh certificate for signed matchings on six labeled vertices.
// C++17 standard library only; no external dependencies.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void matchings(int remaining,const vector<pair<int,int>>& edges,int m,vector<int>&out){
 if(!remaining){out.push_back(m);return;}
 int v=__builtin_ctz((unsigned)remaining);
 int rest=remaining^(1<<v);
 matchings(rest,edges,m,out);
 for(int j=v+1;j<6;j++)if(rest&(1<<j)){
  int e=-1;
  for(int q=0;q<(int)edges.size();q++)if(edges[q].first==v&&edges[q].second==j)e=q;
  assert(e>=0);matchings(rest^(1<<j),edges,m|(1<<e),out);
 }
}
void fwht(vector<long long>&a){
 for(int step=1;step<(int)a.size();step*=2)
  for(int i=0;i<(int)a.size();i+=2*step)
   for(int j=i;j<i+step;j++){
    long long x=a[j],y=a[j+step];a[j]=x+y;a[j+step]=x-y;
   }
}
int main(int argc,char**argv){
 constexpr int n=6,E=15,N=1<<E;
 vector<pair<int,int>> edges;
 int lookup[6][6];
 for(int u=0;u<n;u++)for(int v=u+1;v<n;v++){
  int i=(int)edges.size();edges.emplace_back(u,v);lookup[u][v]=lookup[v][u]=i;
 }
 vector<int> masks;
 matchings((1<<n)-1,edges,0,masks);
 assert(masks.size()==76);
 vector<long long> w(N,0);
 for(int mask:masks)w[mask]++;
 fwht(w);
 const map<int,int> expected={
  {-24,6},{-20,75},{-16,465},{-12,1740},{-8,4105},{-4,6348},
  {0,6825},{4,5540},{8,3570},{12,1815},{16,963},{20,660},
  {24,240},{28,100},{32,195},{36,60},{44,45},{56,15},{76,1}};
 map<int,int> hist,zc;
 for(int t=0;t<N;t++){
  hist[(int)w[t]]++;
  if(!w[t])zc[__builtin_popcount((unsigned)t)]++;
 }
 assert(hist==expected);
 assert((zc==map<int,int>{{5,480},{7,2880},{9,2280},{11,1185}}));
 long long parseval=0;
 for(auto v:w)parseval+=v*v;
 assert(parseval==(long long)N*76);
 vector<long long> p(N);
 for(int i=0;i<N;i++)p[i]=(w[i]!=0);
 fwht(p);
 long long l1=0,plancherel=0;
 for(auto v:p){l1+=llabs(v);plancherel+=v*v;}
 assert(l1==1524338);assert(plancherel==(long long)N*25943);
 // Count isomorphism classes and their orbit sizes under all 720 relabelings.
 vector<array<unsigned char,E>> perms;
 vector<int> a={0,1,2,3,4,5};
 do{
  array<unsigned char,E> trans{};
  for(int i=0;i<E;i++){
   auto [u,v]=edges[i];trans[i]=(unsigned char)lookup[a[u]][a[v]];
  }
  perms.push_back(trans);
 }while(next_permutation(a.begin(),a.end()));
 assert(perms.size()==720);
 map<int,int> orbits;
 for(int t=0;t<N;t++)if(w[t]==0){
  int best=t;
  for(const auto& perm:perms){
   int q=0;
   for(int i=0;i<E;i++)if(t&(1<<i))q|=1<<perm[i];
   if(q<best)best=q;
  }
  orbits[best]++;
 }
 assert(orbits.size()==26);
 map<int,int> orbit_sizes;
 for(auto [rep,count]:orbits)orbit_sizes[count]++;
 assert((orbit_sizes==map<int,int>{{30,1},{45,1},{60,2},{90,1},{120,2},{180,7},{360,10},{720,2}}));
 if(argc>2){
  ofstream cert(argv[2]);
  cert<<"canonical_negative_edge_bitmask,negative_edges,orbit_size,degree_sequence\n";
  for(auto [rep,count]:orbits){
   vector<int> deg(6,0);
   for(int i=0;i<E;i++)if(rep&(1<<i)){auto [u,v]=edges[i];deg[u]++;deg[v]++;}
   sort(deg.begin(),deg.end(),greater<int>());
   cert<<rep<<","<<__builtin_popcount((unsigned)rep)<<","<<count<<",\"";
   for(int j=0;j<6;j++)cert<<(j?" ":"")<<deg[j];
   cert<<"\"\n";
  }
 }
 if(argc>1){
  ofstream out(argv[1],ios::binary);
  for(auto v:w){int32_t x=(int32_t)v;
   unsigned char bytes[4];for(int j=0;j<4;j++)bytes[j]=(unsigned char)((uint32_t)x>>(8*j));
   out.write((char*)bytes,4);
  }
 }
 cout<<"n6 spectrum levels="<<hist.size()<<" nullity_reduced="<<hist[0]
     <<" rank_reduced="<<N-hist[0]<<" orbit_classes="<<orbits.size()
     <<" endpoint="<<l1<<"/"<<N<<"\n";
 cout<<"orbit size histogram:";
 for(auto [s,count]:orbit_sizes)cout<<" "<<s<<":"<<count;
 cout<<"\nINVO_FOURIER_CPP_PASS\n";
}
