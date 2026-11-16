// Exact independent character sums over antichains, then over Fourier zeros.
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
static constexpr int Q = (1 << 16);
static map<int,int> read_csv(const string &p) {
    ifstream f(p); if (!f) { cerr<<"Missing "<<p<<"\n"; exit(2); }
    string line; getline(f,line); assert(line=="coefficient,multiplicity");
    map<int,int> v;
    while(getline(f,line)) { if(line.empty())continue;
        size_t comma=line.find(','); assert(comma!=string::npos);
        int x=stoi(line.substr(0,comma)); int n=stoi(line.substr(comma+1));
        assert(n>0 && !v.count(x)); v[x]=n;
    }
    return v;
}
static bool antichain(unsigned mask) {
    for (int a=0;a<16;a++) if ((mask>>a)&1U)
      for (int b=a+1;b<16;b++) if ((mask>>b)&1U)
        if ((a&b)==a || (a&b)==b) return false;
    return true;
}
int main(int argc,char**argv) {
    if(argc!=2) {cerr<<"usage: verify_direct PACKAGE_DIRECTORY\n";return 2;}
    const string d=argv[1];
    vector<unsigned> family;
    for(unsigned m=0;m<Q;m++) if(antichain(m))family.push_back(m);
    assert(family.size()==168);
    vector<int> w(Q);map<int,int> wh;
    vector<unsigned> zeros;
    for(int u=0;u<Q;u++) {
        int v=0;
        for(unsigned m:family) v+= (__builtin_popcount((unsigned)u&m)&1)?-1:1;
        w[u]=v;wh[v]++;
        if(v==0)zeros.push_back(u);
    }
    assert(zeros.size()==6611);
    assert(wh==read_csv(d+"/signed_walsh.csv"));
    // Since every nontrivial character sums to zero over the whole dual group,
    // the kernel of the support projection equals -the zero-set transform
    // away from the identity, avoiding any Walsh transform implementation.
    map<int,int> hh;
    int64_t l1=0, l2=0;
    for (unsigned x=0;x<Q;x++) {
        int h=0;
        if (x==0) h=Q-(int)zeros.size();
        else {
            int k=0;
            for(unsigned u:zeros)
                k+=(__builtin_popcount(u&x)&1)?-1:1;
            h=-k;
        }
        hh[h]++;l1+=abs(h);l2+=(int64_t)h*h;
    }
    assert(hh==read_csv(d+"/projection_kernel.csv"));
    assert(l1==3052046 && l2==(int64_t)Q*58925);
    cout << "ANTICHAIN_B4_DIRECT_PASS antichains=168 frequencies=65536 zeros=6611 "
         << "rank=58925 projection=1526023/32768\n";
}
