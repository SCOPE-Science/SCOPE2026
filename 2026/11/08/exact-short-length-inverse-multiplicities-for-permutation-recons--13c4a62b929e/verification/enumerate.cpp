#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;

// Every length-n difference record uses (n-1) base-16 digits, n <= 10.
uint64_t signature(const vector<int>& p) {
    uint64_t key = 0;
    for (size_t i = 1; i < p.size(); ++i) {
        int d = abs(p[i]-p[i-1]);
        assert(d > 0 && d < 16);
        key = (key<<4) | uint64_t(d);
    }
    return key;
}
vector<int> decode(uint64_t key, int n) {
    vector<int> d(n-1);
    for (int i=n-2; i>=0; --i) { d[i]=key&15; key>>=4; }
    assert(key==0);
    return d;
}
int main() {
    const vector<int> expected_max={0,0,2,2,6,4,8,8,30,12,24};
    for (int n=2; n<=10; ++n) {
        vector<int> p(n);
        iota(p.begin(), p.end(), 1);
        unordered_map<uint64_t,unsigned> frequencies;
        uint64_t total=0;
        do { ++frequencies[signature(p)]; ++total; }
        while(next_permutation(p.begin(),p.end()));
        map<unsigned,uint64_t> hist;
        unsigned maxfreq=0;
        vector<uint64_t> maximizing;
        for(auto const& kv:frequencies) {
            ++hist[kv.second];
            if(kv.second>maxfreq) {maxfreq=kv.second; maximizing.clear();}
            if(kv.second==maxfreq)maximizing.push_back(kv.first);
        }
        uint64_t recovered=0;
        for(auto const& kv:hist)recovered+=kv.first*kv.second;
        assert(recovered==total);
        assert(maxfreq==unsigned(expected_max[n]));
        sort(maximizing.begin(),maximizing.end());
        cout << "n="<<n<<" permutations="<<total<<" records="<<frequencies.size()
             <<" max="<<maxfreq<<" maximizing="<<maximizing.size()<<" hist=";
        for(auto const& kv:hist)cout<<kv.first<<":"<<kv.second<<",";
        cout<<"\n";
        if(n==8) {
            assert(maximizing.size()==1);
            assert(decode(maximizing[0],8)==vector<int>({4,2,4,1,4,2,4}));
        }
        if(n==9)assert(maximizing.size()==20);
        if(n==10)assert(maximizing.size()==5);
    }
    cout << "VERIFY_OK\n";
}
