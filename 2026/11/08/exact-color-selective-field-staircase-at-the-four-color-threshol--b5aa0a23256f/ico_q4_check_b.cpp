// Independent direct bit-mask enumeration using the two-pentagon geometric construction.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
int main(){
 vector<pair<int,int>> edge;
 for(int j=0;j<5;j++){
    int u=1+j,v=6+j, un=1+(j+1)%5,vn=6+(j+1)%5;
    edge.push_back({0,u});edge.push_back({11,v});
    edge.push_back({u,un});edge.push_back({v,vn});
    edge.push_back({u,v});edge.push_back({u,6+(j+4)%5});
 }
 assert(edge.size()==30);
 array<int,13> best; best.fill(10000);
 array<unsigned long long,13> multiplicity{};
 unsigned long long count=0;
 for(uint32_t packed=0;packed<(1u<<24);packed++){
     int spin[12],fav=0;
     for(int i=0;i<12;i++){spin[i]=(packed>>(2*i))&3;fav+=spin[i]==0;}
     int monochrom=0;
     for(auto e:edge)monochrom+=spin[e.first]==spin[e.second];
     if(monochrom<best[fav]){best[fav]=monochrom;multiplicity[fav]=1;}
     else if(monochrom==best[fav])multiplicity[fav]++;
     ++count;
 }
 const int b[]={3,2,1,0,1,3,5,8,11,15,20,25,30};
 const unsigned long long c[]={120,720,1080,240,1080,7560,6840,8640,1620,540,324,36,1};
 for(int i=0;i<=12;i++){if(best[i]!=b[i]||multiplicity[i]!=c[i]){cerr<<"mismatch "<<i<<" "<<best[i]<<" "<<multiplicity[i]<<"\n";return 2;}}
 assert(count==16777216ULL);
 cout<<"PASS: 16,777,216 configurations, geometry-derived edges, exact integer degeneracies\n";
}
