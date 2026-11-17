// Independent direct Moore-neighborhood B3/S23 update for labelled 3-by-n tori.
// Compile: c++ -O3 -std=c++17 verify_direct.cpp -o verify_direct
// Run: ./verify_direct
#include <cstdint>
#include <iostream>
#include <array>
using namespace std;
int main() {
  const long long expected[8] = {0,0,0,127,39,121,2595,1177};
  for (int n=3; n<=7; ++n) {
    array<uint32_t,21> masks{};
    int m=3*n;
    for(int col=0; col<n; ++col) for(int row=0; row<3; ++row){
      int id=3*col+row;
      for(int dc=-1;dc<=1;++dc) for(int dr=-1;dr<=1;++dr){
        if(dc==0 && dr==0) continue;
        int cc=(col+dc+n)%n, rr=(row+dr+3)%3;
        masks[id] |= 1u << (3*cc+rr);
      }
      if (__builtin_popcount(masks[id])!=8) return 2;
    }
    long long count=0;
    uint32_t end=1u<<m;
    for(uint32_t config=0;config<end;++config){
      bool still=true;
      for(int i=0;i<m;++i){
        int a=__builtin_popcount(config&masks[i]);
        bool alive=(config>>i)&1u;
        bool next=alive ? (a==2 || a==3) : a==3;
        if(next!=alive){still=false;break;}
      }
      count+=still;
    }
    cout<<"n="<<n<<" configurations="<<end<<" fixed="<<count<<"\n";
    if(count!=expected[n])return 3;
  }
  cout<<"PASS: independent direct Moore-neighbor enumeration\n";
}
