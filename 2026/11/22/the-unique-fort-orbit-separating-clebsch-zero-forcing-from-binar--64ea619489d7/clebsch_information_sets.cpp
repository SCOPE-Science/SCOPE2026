// Independent finite checker using folded-hypercube adjacency and sequential forcing.
// g++ -O2 -std=c++17 clebsch_information_sets.cpp -o check && ./check
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
using namespace std;
constexpr unsigned FULL=(1u<<16)-1;
array<unsigned,16> adj{};
int size(unsigned x){return __builtin_popcount(x);}
int rank6(unsigned whites){
    array<unsigned,16> basis{};int r=0;
    for(int j=0;j<16;j++)if(whites&(1u<<j)){
        unsigned column=adj[j] | (1u<<j);
        while(column){int p=31-__builtin_clz(column);
            if(!basis[p]){basis[p]=column;r++;break;}
            column^=basis[p];
        }
    }
    return r;
}
bool forcing(unsigned whites){
    while(whites){bool progressed=false;
        for(int u=0;u<16;u++)if(!(whites&(1u<<u))){
            unsigned w=whites&adj[u];
            if(w && !(w&(w-1))){whites ^= w;progressed=true;break;}
        }
        if(!progressed)return false;
    }
    return true;
}
bool exceptional(unsigned w){
    array<int,6> d{};int i=0;
    for(int u=0;u<16;u++)if(w&(1u<<u))d[i++]=size(w&adj[u]);
    sort(d.begin(),d.end());
    return d==array<int,6>{0,0,0,1,1,2};
}
int main(){
    // Fifth cube coordinate becomes antipodal matching in four-bit quotient.
    for(int v=0;v<16;v++){
        for(int j=0;j<4;j++)adj[v]|=1u<<(v^(1<<j));
        adj[v]|=1u<<(v^15);
        assert(size(adj[v])==5);
    }
    assert(rank6(FULL)==6);
    int total=0,linear=0,force=0,exceptions=0,others=0;
    for(unsigned w=0;w<=FULL;w++)if(size(w)==6){
        ++total;
        bool a=rank6(w)==6, b=forcing(w), c=exceptional(w);
        if(b!=(a&&!c)){cerr << "FAIL at mask "<<w<<"\n";return 1;}
        linear+=a;force+=b;exceptions+=c;others+=!a;
    }
    assert(total==8008 && linear==4032 && force==3872 &&
           exceptions==160 && others==3976);
    unsigned a=0,b=0;
    for(int v:{1,6,11,12,14,15})a|=1u<<v;
    for(int v:{1,2,5,8,10,15})b|=1u<<v;
    assert(forcing(a)&&forcing(b));
    for(int y:{2,5,8,10})assert(!forcing(a^(1u<<14)^(1u<<y)));
    assert(rank6(a^(1u<<14)^(1u<<10))==6);
    assert(exceptional(a^(1u<<14)^(1u<<10)));
    cout<<"PASS: all 8008 masks; rank6=4032 forcing=3872 "
        <<"P3+3isolates=160 others=3976; exchange obstruction\n";
}
