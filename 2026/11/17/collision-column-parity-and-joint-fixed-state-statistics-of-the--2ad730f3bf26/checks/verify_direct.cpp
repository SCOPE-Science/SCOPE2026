// Independent exhaustive verification of HPP fixed states and their two observables.
// Site masks: north 1, east 2, south 4, west 8.
// Input x is an array of 2n four-bit site masks.
#include <cstdint>
#include <iostream>
#include <map>
#include <utility>
#include <vector>

static uint64_t one_step(uint64_t x, int n) {
    uint64_t out = 0;
    for (int row = 0; row < 2; ++row) {
        for (int j = 0; j < n; ++j) {
            const int other = (1-row)*n+j;
            const int left = row*n+(j+n-1)%n;
            const int right = row*n+(j+1)%n;
            int mask = ((x>>(4*other))&1) |
                       ((x>>(4*left+1))&1)*2 |
                       ((x>>(4*other+2))&1)*4 |
                       ((x>>(4*right+3))&1)*8;
            if (mask == 5) mask=10;
            else if (mask == 10) mask=5;
            out |= static_cast<uint64_t>(mask) << (4*(row*n+j));
        }
    }
    return out;
}

int main(){
 for(int n=2;n<=3;n++){
    std::map<std::pair<int,int>,uint64_t> hist;
    uint64_t total=0;
    const uint64_t limit=uint64_t(1) << (8*n);
    for(uint64_t x=0;x<limit;x++){
        if(one_step(x,n)!=x) continue;
        int occupied=0,collision_columns=0;
        for(int j=0;j<n;j++){
            int m0=(x>>(4*j))&15, m1=(x>>(4*(n+j)))&15;
            occupied+=__builtin_popcount(static_cast<unsigned>(m0));
            occupied+=__builtin_popcount(static_cast<unsigned>(m1));
            if(m0==5||m0==10){
                if(m1!=(m0==5?10:5)){std::cerr<<"collision pairing violation\n";return 2;}
                collision_columns++;
            } else if(m1==5||m1==10) {std::cerr<<"unpaired collision\n";return 3;}
        }
        hist[{occupied,collision_columns}]++;
        total++;
    }
    std::cout<<"n="<<n<<" count="<<total<<"\n";
    for(auto const &[k,v]:hist)
        std::cout<<"occupancy="<<k.first<<" collision_columns="<<k.second<<" count="<<v<<"\n";
 }
}
