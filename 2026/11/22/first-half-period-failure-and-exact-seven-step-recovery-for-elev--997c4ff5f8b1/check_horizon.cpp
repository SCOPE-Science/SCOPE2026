// Exact finite classification of truncated left/right observations of prime cycles.
// C++17; no third-party dependencies. Compile: g++ -std=c++17 -O2 check_horizon.cpp -o check && ./check
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <vector>
using namespace std;

// Every p-cycle is uniquely (0,a[0],...,a[p-2]), where a permutes 1,...,p-1.
// Extremal label 0 always moves right, and p-1 always moves left, for 0<t<p;
// omitting those two constant signs loses no information.
vector<uint64_t> enumerate(int p, int K) {
    if ((p-2)*K>63) throw runtime_error("signature exceeds 63 bits");
    vector<uint64_t> out;
    int a[12]; iota(a,a+p-1,1);
    do {
        int f[12] = {0};
        int v=0;
        for(int i=0;i<p-1;i++){f[v]=a[i];v=a[i];}
        f[v]=0;
        int x[12];iota(x,x+p,0);
        uint64_t sig=0;
        for(int t=1;t<=K;t++) {
            for(int j=0;j<p;j++) x[j]=f[x[j]];
            for(int j=1;j<p-1;j++) sig=(sig<<1) | uint64_t(x[j]>j);
        }
        out.push_back(sig);
    } while(next_permutation(a,a+p-1));
    return out;
}

map<size_t,uint64_t> fibers(const vector<uint64_t>& full,int p,int K,int k){
    vector<uint64_t> a=full;
    int sh=(K-k)*(p-2);
    for(auto& v:a) v>>=sh;
    sort(a.begin(),a.end());
    map<size_t,uint64_t> hist;
    for(size_t i=0;i<a.size();) {
        size_t j=i+1;
        while(j<a.size() && a[j]==a[i]) ++j;
        hist[j-i]++;
        i=j;
    }
    return hist;
}

void require(bool x,const string& s){if(!x) throw runtime_error(s);}
int main() {
    for(int p:{3,5,7,11}) {
        int K=(p==11 ? 7 : p-1);
        const vector<uint64_t> a=enumerate(p,K);
        uint64_t factorial=1;
        for(int i=2;i<p;i++) factorial*=i;
        require(a.size()==factorial,"cycle enumeration incomplete");
        int minimum=0;
        for(int k=1;k<=K;k++) {
            const auto hist=fibers(a,p,K,k);
            uint64_t ncycles=0,nclasses=0,npairs=0;
            for(auto [size,multiplicity]:hist){
                ncycles+=size*multiplicity;
                nclasses+=multiplicity;
                npairs+=multiplicity*size*(size-1)/2;
            }
            require(ncycles==factorial,"partition count incorrect");
            if(!minimum && npairs==0) minimum=k;
            if(p==11 && k==6){
                require(hist.size()==3 && hist.at(1)==3470400 && hist.at(2)==77760
                    && hist.at(4)==720,"eleven-cycle six-step census mismatch");
                require(nclasses==3548880 && npairs==82080,"eleven-cycle ambiguity mismatch");
            }
            if((p==5&&k==2)||(p==7&&k==3)||(p==11&&k>=6)) {
                cout << "p="<<p<<" k="<<k<<" classes="<<nclasses
                  <<" colliding_pairs="<<npairs<<" fibers=";
                for(auto [sz,n]:hist)cout<<sz<<":"<<n<<",";
                cout<<"\n";
            }
        }
        cout<<"p="<<p<<" cycles="<<factorial<<" minimal_horizon="<<minimum<<"\n";
        require(minimum==(p==3?1:p==5?3:p==7?4:7),"minimum horizon mismatch");
    }
    cout<<"ALL EXACT FINITE CHECKS PASSED\n";
}
