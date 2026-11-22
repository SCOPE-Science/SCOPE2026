// Independent finite certificate for exact shattering coefficients.
#include <algorithm>
#include <bitset>
#include <cstdint>
#include <cstdlib>
#include <deque>
#include <iostream>
#include <set>
#include <utility>
#include <vector>
using namespace std;
using Bits = bitset<128>;

vector<vector<int>> all_words(int n) {
    vector<vector<int>> w;
    for(int mask=0; mask<(1<<(n-1)); ++mask) {
        deque<int> d; d.push_back(1);
        for(int v=2;v<=n;++v) {
            if(mask & (1<<(v-2))) d.push_front(v);
            else d.push_back(v);
        }
        w.emplace_back(d.begin(),d.end());
    }
    return w;
}

void visit(size_t start, vector<Bits> const &atoms,
           vector<Bits> const &queries, Bits const &full,
           size_t depth, vector<uint64_t> &counts) {
    for(size_t j=start;j<queries.size();++j) {
        vector<Bits> children;
        bool valid=true;
        for(auto const &a: atoms) {
            auto yes = a & queries[j];
            auto no = a & (full ^ queries[j]);
            if(yes.none() || no.none()) {valid=false;break;}
            children.push_back(yes); children.push_back(no);
        }
        if(valid) {
            counts[depth]++;
            visit(j+1,children,queries,full,depth+1,counts);
        }
    }
}

int main(){
    vector<vector<uint64_t>> reference={
        {1},{1,4},{1,8,4},{1,14,22},{1,21,68,16},
        {1,30,150,116},{1,40,294,440,64},{1,52,510,1238,560}
    };
    for(int n=1;n<=8;++n) {
        auto words=all_words(n);
        Bits full; for(size_t i=0;i<words.size();++i)full.set(i);
        vector<Bits> queries;
        for(int pos=0;pos<n;++pos) for(int v=1;v<=n;++v) {
            Bits b;for(size_t i=0;i<words.size();++i)
                if(words[i][pos]==v) b.set(i);
            if(b.any() && b!=full) queries.push_back(b);
        }
        vector<uint64_t> counts(n+1,0);counts[0]=1;
        visit(0,{full},queries,full,1,counts);
        while(counts.size()>1 && counts.back()==0)counts.pop_back();
        if(counts!=reference[n-1]){cerr<<"MISMATCH "<<n<<"\n";return 1;}
        cout << "n=" << n << " possible=" << queries.size() << " faces=";
        for(auto c:counts)cout << c << ",";cout << "\n";
    }
    cout<<"INDEPENDENT_CPP_TRACE_CERTIFICATE_PASS\n";
}
