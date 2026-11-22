// Enumerate every rooted graph on n-1 points and count distinct spectra.
// This deliberately does not construct isomorphism orbits.
// Compile: c++ -std=c++17 -O2 independent_count.cpp -o independent_count && ./independent_count
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;
struct Profile { array<unsigned char,29> x{};bool operator==(Profile const& b)const{return x==b.x;} };
struct Hash {size_t operator()(Profile const& a)const{
 uint64_t h=14695981039346656037ULL;
 for(unsigned char c:a.x){h^=c;h*=1099511628211ULL;}
 return (size_t)h;
}};
int main(){
 const int expectation[]={1,1,1,2,3,7,16,54,219};
 for(int n=1;n<=8;n++){
  int m=n-1,k=m*(m-1)/2,M=1<<m,G=1<<k;
  vector<pair<int,int>> edge;
  for(int i=0;i<m;i++)for(int j=i+1;j<m;j++)edge.push_back({i,j});
  vector<unsigned> cuts(M);
  for(int s=0;s<M;s++)for(int j=0;j<k;j++){
   auto[a,b]=edge[j];if(((s>>a)^(s>>b))&1)cuts[s]|=1u<<j;
  }
  unordered_set<Profile,Hash> profiles;
  profiles.reserve(2500);
  for(int g=0;g<G;g++){
   Profile p;
   for(int s=0;s<M;s++){
    int wt=__builtin_popcount((unsigned)s)+__builtin_popcount((unsigned)(g^cuts[s]));
    p.x[wt]++;
   }
   profiles.insert(p);
  }
  assert(profiles.size()==(size_t)expectation[n]);
  cout<<"N="<<n<<" rooted_graphs="<<G<<" distinct_profiles="<<profiles.size()<<"\n";
 }
 cout<<"INDEPENDENT_VERIFY_OK\n";
}
