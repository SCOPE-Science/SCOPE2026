// Independent direct binary-state enumeration, separate from the transfer graph.
// Build: c++ -O3 -std=c++17 -o direct direct_evolution.cpp
#include <cassert>
#include <cstdint>
#include <iostream>
using namespace std;
uint32_t evolve(uint32_t state,int n,bool highlife) {
    uint32_t out=0;
    for (int x=0;x<n;x++) for (int y=0;y<3;y++) {
        int neighbours=0;
        for (int dx=-1;dx<=1;dx++) for(int dy=-1;dy<=1;dy++) {
            if(dx==0 && dy==0) continue;
            int xx=(x+dx+n)%n, yy=(y+dy+3)%3;
            neighbours+=(state>>(3*xx+yy))&1;
        }
        bool alive=(state>>(3*x+y))&1;
        if ((alive && (neighbours==2 || neighbours==3)) ||
            (!alive && (neighbours==3 || (highlife && neighbours==6))))
            out |= uint32_t(1)<<(3*x+y);
    }
    return out;
}
int main() {
    for(bool highlife:{false,true}){
        cout<<(highlife?"HighLife":"Life")<<"\n";
        for(int n=3;n<=7;n++) {
            uint64_t fixed=0, exactly_three=0;
            uint32_t limit=uint32_t(1)<<(3*n);
            for(uint32_t s=0;s<limit;s++) {
                uint32_t a=evolve(s,n,highlife);
                if(a==s) fixed++;
                uint32_t b=evolve(a,n,highlife);
                uint32_t c=evolve(b,n,highlife);
                if(c==s && a!=s) exactly_three++;
            }
            cout<<"n="<<n<<" fixed="<<fixed<<" exact_period_3="<<exactly_three<<"\n";
            assert(exactly_three==0);
        }
    }
}
