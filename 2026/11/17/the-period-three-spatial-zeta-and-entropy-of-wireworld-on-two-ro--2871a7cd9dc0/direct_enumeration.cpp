#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
// 0 empty, 1 head, 2 tail, 3 wire. Moore offsets are counted, including
// the two vertical incidences to the opposite row on a two-row periodic grid.
static uint64_t evolve(uint64_t x, int n) {
    uint64_t y=0;
    for (int c=0;c<n;c++) for (int r=0;r<2;r++) {
        int q=2*c+r;
        int v=(x>>(2*q))&3;
        int nv=0;
        if (v==0) nv=0;
        else if(v==1) nv=2;
        else if(v==2) nv=3;
        else {
            int h=0;
            for (int dc=-1;dc<=1;dc++) for (int dr=-1;dr<=1;dr++) {
                if(dc==0 && dr==0) continue;
                int cc=(c+dc+n)%n, rr=(r+dr+2)%2;
                h+=(((x>>(2*(2*cc+rr)))&3)==1);
            }
            nv=(h==1 || h==2)?1:3;
        }
        y|=uint64_t(nv)<<(2*q);
    }
    return y;
}
int main() {
    for (int n=3;n<=6;n++) {
        uint64_t total=uint64_t(1)<<(4*n), fixed3=0, fixed1=0;
        for (uint64_t x=0;x<total;x++) {
            uint64_t y=evolve(x,n), z=evolve(y,n), w=evolve(z,n);
            fixed1+=(y==x);
            fixed3+=(w==x);
        }
        cout << n << " " << fixed1 << " " << fixed3 << " " << (fixed3-fixed1)/3 << "\n";
    }
}
