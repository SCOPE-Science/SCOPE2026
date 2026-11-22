// Independent direct enumeration of simultaneous-attack defenses on clique bouquets.
// Build: c++ -O2 -std=c++17 verify_independent.cpp -o verify_independent
// Run: ./verify_independent
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <stdexcept>
#include <vector>
using namespace std;

map<int,long long> enumerate(int m,int r) {
    const int n=1+m*r;
    vector<uint32_t> adj(n,0);
    for (int v=1; v<n; ++v) {
        adj[0] |= (1u<<v);
        adj[v] |= 1u;
    }
    for(int p=0;p<m;++p) for(int a=0;a<r;++a)
        for(int b=a+1;b<r;++b) {
            int v=1+p*r+a,w=1+p*r+b;
            adj[v] |= 1u<<w; adj[w] |= 1u<<v;
        }
    long long limit=1;
    for(int i=0;i<n;++i) limit*=3;
    map<int,long long> hist;
    vector<int> z;
    for(long long encoding=0;encoding<limit;++encoding) {
        long long a=encoding;
        uint32_t two=0;
        int weight=0;
        z.clear();
        for(int v=0;v<n;++v) {
            int label=a%3;a/=3;weight+=label;
            if(label==2)two|=1u<<v;
            else if(label==0)z.push_back(v);
        }
        bool valid=true;
        for(int v:z) if(!(adj[v]&two)) {valid=false;break;}
        if(!valid) continue;
        for(int i=0;i<(int)z.size()&&valid;++i)
            for(int j=i+1;j<(int)z.size();++j)
                if(__builtin_popcount((adj[z[i]]|adj[z[j]])&two)<2)
                    {valid=false;break;}
        if(valid) hist[weight]++;
    }
    return hist;
}
int main(){
    const vector<array<int,4>> tests={
        {2,2,4,4}, {3,2,6,20}, {2,3,6,63},
        {3,3,8,108}, {2,4,6,16}, {2,5,6,25},
        {3,4,8,64}
    };
    for(auto q:tests){
        auto h=enumerate(q[0],q[1]);
        if(h.begin()->first!=q[2]||h.begin()->second!=q[3])
            throw runtime_error("incorrect minimum coefficient");
        long long total=0;
        for(auto p:h)total+=p.second;
        cout<<"m="<<q[0]<<" r="<<q[1]<<" min="<<h.begin()->first
            <<" count="<<h.begin()->second<<" total="<<total<<"\n";
    }
    cout<<"INDEPENDENT_CHECK_OK\n";
}
