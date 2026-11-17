// Independent direct exhaustive simulation for the three-state B2/S/C3 rule.
// Two-row periodic Moore grid; eight offsets, counted with multiplicity.
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;

vector<int> step(const vector<int>& s, int n) {
    vector<int> t(2*n);
    for (int r=0;r<2;r++) for (int x=0;x<n;x++) {
        int p=r*n+x;
        if (s[p]==1) {t[p]=2; continue;}
        if (s[p]==2) {t[p]=0; continue;}
        int firing=0;
        for (int dr=-1;dr<=1;dr++) for (int dx=-1;dx<=1;dx++) {
            if (dr==0 && dx==0) continue;
            int rr=(r+dr+2)%2, xx=(x+dx+n)%n;
            firing+=(s[rr*n+xx]==1);
        }
        t[p]=(firing==2 ? 1:0);
    }
    return t;
}
int main() {
    const int expect[]={0,0,0,1,1,1,1};
    for (int n=3;n<=6;n++) {
        int64_t count=0, total=1;
        for (int i=0;i<2*n;i++) total*=3;
        for (int64_t code=0;code<total;code++) {
            int64_t tmp=code;
            vector<int> s(2*n);
            for (int &v:s) {v=tmp%3; tmp/=3;}
            auto y=step(step(step(s,n),n),n);
            if (y==s) count++;
        }
        assert(count==expect[n]);
        cout<<n<<' '<<total<<' '<<count<<' '<<(count-1)/3<<'\n';
    }
    // One explicit primitive three-cycle for n=12, using a phase-type word.
    // A phase -1 remains off; phase a fires at times a modulo three.
    const int phase_top[12]={-1,0,1,0,-1,2,0,2,-1,1,2,1};
    const int phase_bot[12]={0,2,-1,1,2,1,-1,0,1,0,-1,2};
    vector<int> original(24);
    for (int x=0;x<12;x++) {
        for (int r=0;r<2;r++) {
            const int phase=(r==0 ? phase_top[x]:phase_bot[x]);
            original[r*12+x]=(phase<0?0:(phase==0?1:(phase==1?0:2)));
        }
    }
    const auto after1=step(original,12);
    const auto after2=step(after1,12);
    const auto after3=step(after2,12);
    assert(after1!=original && after3==original);
    cout<<"n=12 witness primitive-three: PASSED\n";
    cout<<"ALL DIRECT CHECKS PASSED\n";
}
