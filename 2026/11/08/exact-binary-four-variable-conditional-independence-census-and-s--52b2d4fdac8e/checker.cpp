#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iomanip>
#include <fstream>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <tuple>
#include <vector>
using namespace std;

struct Statement {int a,b,Z; vector<array<uint32_t,4>> corners;};
vector<Statement> all_statements() {
 vector<Statement> st;
 for(int a=0;a<4;a++)for(int b=a+1;b<4;b++)for(int Z=0;Z<16;Z++)
  if(!(Z&(1<<a)) && !(Z&(1<<b))) {
   Statement x; x.a=a;x.b=b;x.Z=Z;
   for(int z=0;z<16;z++) if((z&Z)==z) {
    array<uint32_t,4> q={0,0,0,0};
    for(int s=0;s<16;s++)if((s&Z)==z) {
     int t=(((s>>a)&1)<<1)|((s>>b)&1);
     q[t]|=uint32_t(1)<<s;
    }
    x.corners.push_back(q);
   }
   st.push_back(x);
  }
 return st;
}
// Lemma: binary conditional independence fails iff a conditioning fibre
// contains three corners or just one diagonal pair.
bool has_rectangular_fibres(uint32_t team, const Statement& s) {
 for(auto q:s.corners) {
  int present=0;
  for(int k=0;k<4;k++)if(team&q[k])present |= 1<<k;
  if(present==6 || present==9 || __builtin_popcount((unsigned)present)==3)return false;
 }
 return true;
}
// Independent direct reading of the forall/exists team-semantics definition.
bool directly_independent(uint32_t team, const Statement& st) {
 for(int s=0;s<16;s++)if(team & (uint32_t(1)<<s))
  for(int t=0;t<16;t++)if((team & (uint32_t(1)<<t)) && ((s&st.Z)==(t&st.Z))) {
   bool found=false;
   for(int u=0;u<16;u++)if(team & (uint32_t(1)<<u))
    if((u&st.Z)==(s&st.Z) && ((u>>st.a)&1)==((s>>st.a)&1)
       && ((u>>st.b)&1)==((t>>st.b)&1)) {found=true;break;}
   if(!found)return false;
  }
 return true;
}

int main(int argc, char** argv) {
 auto st=all_statements();assert(st.size()==24);
 map<uint32_t,pair<int,int>> profile;
 map<uint32_t,uint32_t> witness;
 uint64_t comparisons=0;
 for(uint32_t team=1;team<65536;team++) {
  uint32_t sig=0;
  for(int j=0;j<24;j++) {
   bool quick=has_rectangular_fibres(team,st[j]);
   bool direct=directly_independent(team,st[j]);
   assert(quick==direct);comparisons++;
   if(quick)sig|=uint32_t(1)<<j;
  }
  int size=__builtin_popcount(team);
  auto it=profile.find(sig);
  if(it==profile.end()) {profile[sig]={size,1};witness[sig]=team;}
  else {it->second.second++;
    if(size < it->second.first) {it->second.first=size;witness[sig]=team;}
  }
 }
 assert(comparisons==65535ULL*24);
 assert(profile.size()==1342);
 map<int,int> min_dist;
 int total_teams=0,sharp_witness_count=0;
 uint32_t sharp_profile=0,sharp_team=0;
 for(const auto& [sig,p]:profile) {
  min_dist[p.first]++;total_teams+=p.second;
  if(p.first==10) {
   sharp_witness_count++;
   if(!sharp_team){sharp_profile=sig;sharp_team=witness[sig];}
  }
 }
 assert(total_teams==65535);
 assert((min_dist==map<int,int>{{1,1},{2,11},{3,29},{4,114},{5,264},{6,397},{7,307},{8,129},{9,62},{10,28}}));
 assert(sharp_witness_count==28);
 
 

 // The induced S4 action on statements is exact: variable names are kept distinct.
 map<tuple<int,int,int>,int> id;
 for(int j=0;j<24;j++)id[{st[j].a,st[j].b,st[j].Z}]=j;
 array<int,4> p={0,1,2,3};
 set<uint32_t> visited;
 map<int,int> orbit_sizes,orbit_min;
 int num_orbits=0;
 map<uint32_t,tuple<int,int,uint32_t>> orbit_data;
 for(const auto& [sig,stats]:profile) {
  if(visited.count(sig))continue;
  set<uint32_t> orbit;
  p={0,1,2,3};
  do {
   uint32_t transformed=0;
   for(int j=0;j<24;j++)if(sig&(uint32_t(1)<<j)) {
    int a=p[st[j].a],b=p[st[j].b];if(a>b)swap(a,b);
    int Z=0;for(int k=0;k<4;k++)if(st[j].Z&(1<<k))Z|=1<<p[k];
    transformed|=uint32_t(1)<<id.at({a,b,Z});
   }
   assert(profile.count(transformed));orbit.insert(transformed);
  }while(next_permutation(p.begin(),p.end()));
  for(auto x:orbit){assert(visited.insert(x).second);assert(profile[x].first==stats.first);}
  orbit_sizes[orbit.size()]++;orbit_min[stats.first]++;num_orbits++;
  orbit_data[*orbit.begin()]={int(orbit.size()),stats.first,witness.at(*orbit.begin())};
  if(stats.first==10)cout<<"ten_world_orbit_canonical="<<hex<<setw(6)<<setfill('0')<<*orbit.begin()<<dec
     <<" orbit_size="<<orbit.size()<<" team="<<hex<<setw(4)<<witness.at(*orbit.begin())<<dec<<"\n";
 }
 
 assert(num_orbits==125);
 assert(visited.size()==profile.size());
 assert((orbit_sizes==map<int,int>{{1,5},{3,7},{4,14},{6,22},{12,60},{24,17}}));
 assert((orbit_min==map<int,int>{{1,1},{2,3},{3,5},{4,15},{5,24},{6,31},{7,22},{8,14},{9,6},{10,4}}));
 assert(profile.at((1u<<24)-1).second==81);
 
 
 

 if(argc==2 && string(argv[1])=="--tables") {
  ofstream profiles("profiles.csv"), orbits("orbits.csv");
  assert(profiles.good() && orbits.good());
  profiles<<"profile_hex,min_worlds,team_count,example_team_hex\n";
  orbits<<"canonical_profile_hex,orbit_size,min_worlds,example_team_hex\n";
  for(const auto& [signature,stats]:profile) {
   profiles<<hex<<setw(6)<<setfill('0')<<signature<<dec<<","<<stats.first<<","<<stats.second<<","<<hex<<setw(4)<<witness[signature]<<dec<<"\n";
  }
  for(const auto& [signature,info]:orbit_data) {
   orbits<<hex<<setw(6)<<setfill('0')<<signature<<dec<<","<<get<0>(info)<<","<<get<1>(info)<<","<<hex<<setw(4)<<get<2>(info)<<dec<<"\n";
  }
  profiles.close();orbits.close();
  assert(profiles.good() && orbits.good());
 }
 cout<<"TEAM_CI4_EXHAUSTIVE_OK\n";
 cout<<"teams="<<total_teams<<" statements="<<st.size()<<" definition_comparisons="<<comparisons<<"\n";
 cout<<"profiles="<<profile.size()<<" name_permutation_orbits="<<num_orbits<<" sharp_world_bound=10\n";
 cout<<"minimum_world_distribution:";
 for(auto [s,n]:min_dist){cout<<" "<<s<<":"<<n;} cout<<"\n";
 cout<<"orbit_minimum_world_distribution:";
 for(auto [s,n]:orbit_min){cout<<" "<<s<<":"<<n;} cout<<"\n";
 cout<<"orbit_size_distribution:";
 for(auto [s,n]:orbit_sizes){cout<<" "<<s<<":"<<n;} cout<<"\n";
 cout<<"ten_world_profile="<<hex<<setw(6)<<setfill('0')<<sharp_profile
     <<" example_team="<<setw(4)<<sharp_team<<dec<<"\n";
}
