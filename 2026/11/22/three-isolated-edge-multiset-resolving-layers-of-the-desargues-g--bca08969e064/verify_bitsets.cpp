#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
    // Bipartite inclusion graph of the 2- and 3-subsets of a five-set.
    // Vertices use ascending five-bit masks.
    vector<int> V;
    for (int x=0;x<32;++x)
        if (__builtin_popcount((unsigned)x)==2 || __builtin_popcount((unsigned)x)==3)
            V.push_back(x);
    const int n=(int)V.size();
    if(n!=20) return 1;
    vector<vector<int>> adj(n);
    vector<pair<int,int>> edges;
    for(int a=0;a<n;++a) for(int b=a+1;b<n;++b)
        if(__builtin_popcount((unsigned)(V[a]^V[b]))==1){
            adj[a].push_back(b); adj[b].push_back(a); edges.emplace_back(a,b);
        }
    if(edges.size()!=30) return 2;
    int dist[20][20];
    for(int root=0;root<n;++root){
        fill(dist[root],dist[root]+20,-1);
        dist[root][root]=0;
        queue<int> q; q.push(root);
        while(!q.empty()){
            int x=q.front(); q.pop();
            for(int y:adj[x]) if(dist[root][y]<0){
                dist[root][y]=dist[root][x]+1; q.push(y);
            }
        }
    }
    // For every edge, bitmask of vertices at each edge-distance level.
    vector<array<uint32_t,5>> shells;
    for(auto [a,b]:edges){
        array<uint32_t,5> t{};
        for(int root=0;root<n;++root){
            int d=min(dist[root][a],dist[root][b]);
            if(d<0 || d>4) return 3;
            t[d] |= 1u<<root;
        }
        shells.push_back(t);
    }
    uint64_t count[21]{};
    ofstream certificate;
    if(argc==2){certificate.open(argv[1]);if(!certificate) return 4;}
    for(uint32_t S=0;S<(1u<<20);++S){
        int k=__builtin_popcount(S);
        uint64_t seen[30];int distinct=0;
        for(const auto& sh:shells){
            uint64_t code=0;
            for(int level=0;level<5;++level){
                int c=__builtin_popcount(sh[level]&S);
                code |= uint64_t(c) << (5*level);
            }
            bool found=false;
            for(int j=0;j<distinct;++j) if(seen[j]==code){found=true;break;}
            if(!found) seen[distinct++]=code;
        }
        if(distinct==30){
            ++count[k];
            if(k==8 && argc==2) certificate<<S<<'\n';
        }
    }
    for(int k=0;k<=20;++k) if(count[k]) cout<<k<<":"<<count[k]<<" ";
    cout<<"\n";
    if(count[8]!=720 || count[10]!=960 || count[12]!=720) return 5;
    for(int k=0;k<=20;++k) if(k!=8 && k!=10 && k!=12 && count[k]) return 6;
    cout<<"BITSET_EXHAUSTIVE_OK\n";
}
