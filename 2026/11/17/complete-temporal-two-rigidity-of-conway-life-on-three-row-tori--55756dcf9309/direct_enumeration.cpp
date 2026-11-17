// Independent full-state check for 3-by-n toroidal Conway Life, n=3,...,7.
// C++17: g++ -O3 -std=c++17 direct_enumeration.cpp -o verify && ./verify
#include <cstdint>
#include <iostream>
#include <vector>
#include <cassert>
using U = std::uint64_t;

int main(){
  const U expected_fixed[] = {127,39,121,2595,1177};
  for(int n=3;n<=7;n++){
    const int sites=3*n;
    std::vector<U> neighbor(sites,0);
    for(int col=0;col<n;col++)for(int row=0;row<3;row++){
      int u=3*col+row;
      for(int dc=-1;dc<=1;dc++)for(int dr=-1;dr<=1;dr++){
        if(dc==0 && dr==0)continue;
        int v=3*((col+dc+n)%n)+(row+dr+3)%3;
        assert(u!=v);
        assert(!(neighbor[u]&(U(1)<<v)));
        neighbor[u]|=U(1)<<v;
      }
      assert(__builtin_popcountll(neighbor[u])==8);
    }
    auto evolve = [&](U x)->U{
      U y=0;
      for(int u=0;u<sites;u++){
        int count=__builtin_popcountll(x&neighbor[u]);
        bool on=((count==3) || (count==2 && ((x>>u)&1)));
        if(on)y |= U(1)<<u;
      }
      return y;
    };
    U fixed=0, nonfixed=0;
    std::vector<U> orbitStates;
    for(U x=0;x<(U(1)<<sites);x++){
      U y=evolve(x);
      if(y==x){fixed++;continue;}
      if(evolve(y)!=x)continue;
      nonfixed++;
      orbitStates.push_back(x);
    }
    U expected_nonfixed=(n%4==0 ? 4:0);
    assert(fixed==expected_fixed[n-3]);
    assert(nonfixed==expected_nonfixed);
    if(n==4){
      for(U x:orbitStates){
        // All columns must be either entirely occupied or entirely empty.
        for(int c=0;c<n;c++){
          U tri=(x>>(3*c))&7;
          assert(tri==0 || tri==7);
        }
      }
    }
    std::cout << "n="<<n<<" fixed="<<fixed<<" primitive_two_states="<<nonfixed
              <<" primitive_two_orbits="<<(nonfixed/2)<<" PASS\n";
  }
}
