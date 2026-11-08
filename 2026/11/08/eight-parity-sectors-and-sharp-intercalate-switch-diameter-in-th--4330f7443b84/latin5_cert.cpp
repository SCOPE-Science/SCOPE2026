// A complete order-five Latin-square intercalate reconfiguration certificate.
// Compile: c++ -std=c++17 -O2 latin5_cert.cpp -o latin5_cert
// Execute: ./latin5_cert
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <unordered_map>
#include <vector>
using namespace std;
using Square = array<unsigned char, 25>;
using Perm = array<unsigned char, 5>;

static vector<Square> all;
static vector<Perm> permutation_list;
static array<int, 5> used{};
static Square partial{};

[[noreturn]] void fail(const char *m) { cerr << "FAILED: " << m << '\n'; exit(1); }
void require(bool b, const char *m) { if (!b) fail(m); }
uint64_t pack(const Square &s) {
    uint64_t v=0;
    for (unsigned char x:s) v=5*v+x;
    return v;
}
void enumerate(int r) {
    if (r==5) {all.push_back(partial);return;}
    for (const auto &p:permutation_list) {
        bool fits=true;
        for (int c=0;c<5;c++) if (used[c]&(1<<p[c])){fits=false;break;}
        if (!fits) continue;
        for(int c=0;c<5;c++){partial[5*r+c]=p[c];used[c]|=1<<p[c];}
        enumerate(r+1);
        for(int c=0;c<5;c++)used[c]^=1<<p[c];
    }
}
int sign(const Perm &p) {
    int z=0;
    for(int a=0;a<5;a++)for(int b=a+1;b<5;b++)z^=p[a]>p[b];
    return z;
}
int main() {
    Perm p{0,1,2,3,4};
    do {permutation_list.push_back(p);} while(next_permutation(p.begin(),p.end()));
    enumerate(0);
    require(all.size()==161280,"Latin enumeration count");
    unordered_map<uint64_t,int> lookup;lookup.reserve(350000);
    for(int k=0;k<(int)all.size();k++)
        require(lookup.emplace(pack(all[k]),k).second,"duplicate Latin square");
    vector<vector<int>> graph(all.size());
    map<int,int> degrees;
    int twice_edges=0;
    for(int i=0;i<(int)all.size();i++){
        const auto &s=all[i];
        for(int r=0;r<5;r++)for(int t=r+1;t<5;t++)
        for(int c=0;c<5;c++)for(int d=c+1;d<5;d++){
            int a=5*r+c,b=5*r+d,e=5*t+c,f=5*t+d;
            if(s[a]!=s[f] || s[b]!=s[e])continue;
            Square copy=s;
            swap(copy[a],copy[b]);swap(copy[e],copy[f]);
            auto found=lookup.find(pack(copy));
            require(found!=lookup.end(),"flip leaves Latin space");
            graph[i].push_back(found->second);
        }
        auto &nei=graph[i];sort(nei.begin(),nei.end());
        require(unique(nei.begin(),nei.end())==nei.end(),"duplicate trade");
        degrees[(int)nei.size()]++;
        twice_edges+=(int)nei.size();
    }
    require(degrees==map<int,int>{{0,17280},{4,144000}},"degree spectrum");
    require(twice_edges==576000,"edge count");
    for(int i=0;i<(int)all.size();i++)for(int j:graph[i]){
        require(binary_search(graph[j].begin(),graph[j].end(),i),"asymmetric trade");
    }
    vector<int> component(all.size(),-1);
    vector<vector<int>> blocks;
    for(int i=0;i<(int)all.size();i++)if(component[i]<0){
        int id=(int)blocks.size();blocks.emplace_back();
        component[i]=id;queue<int> bfs;bfs.push(i);
        while(!bfs.empty()){
            int u=bfs.front();bfs.pop();blocks.back().push_back(u);
            for(int v:graph[u])if(component[v]<0){component[v]=id;bfs.push(v);}
        }
    }
    map<int,int> component_sizes;
    for(auto &b:blocks)component_sizes[(int)b.size()]++;
    require(component_sizes==map<int,int>{{1,17280},{18000,8}},"component sizes");
    int origin=-1;
    for(auto &b:blocks)if(b.size()==18000){origin=b[0];break;}
    require(origin>=0,"nontrivial component");
    vector<int> distance(all.size(),-1),hist;
    queue<int> bfs;bfs.push(origin);distance[origin]=0;
    while(!bfs.empty()){
        int u=bfs.front();bfs.pop();
        if(distance[u]>=(int)hist.size())hist.resize(distance[u]+1);
        hist[distance[u]]++;
        for(int v:graph[u])if(distance[v]<0){distance[v]=distance[u]+1;bfs.push(v);}
    }
    const vector<int> expected={1,4,12,36,108,252,612,1284,2256,3624,4812,3828,1112,59};
    require(hist==expected,"distance distribution");
    // For each image of the seed under S5(row)xS5(column)xS5(symbol),
    // record the signs of the chosen three permutations. A conflict would
    // invalidate the eight-component intrinsic invariant.
    vector<int> signature(all.size(),-1);
    array<int,120> parity{};
    for(int i=0;i<120;i++)parity[i]=sign(permutation_list[i]);
    const Square seed=all[origin];
    for(int ir=0;ir<120;ir++)for(int ic=0;ic<120;ic++)for(int is=0;is<120;is++){
        Square result{};
        for(int r=0;r<5;r++)for(int c=0;c<5;c++)
            result[5*permutation_list[ir][r]+permutation_list[ic][c]]=
                permutation_list[is][seed[5*r+c]];
        auto it=lookup.find(pack(result));
        require(it!=lookup.end(),"isotopy action not Latin");
        int idx=it->second;
        int label=4*parity[ir]+2*parity[ic]+parity[is];
        require(signature[idx]<0 || signature[idx]==label,"signature not well-defined");
        signature[idx]=label;
    }
    map<int,int> signature_sizes;
    map<int,set<int>> signature_components;
    for(int i=0;i<(int)all.size();i++){
        signature_sizes[signature[i]]++;
        if(signature[i]>=0)signature_components[signature[i]].insert(component[i]);
        for(int j:graph[i])require(signature[i]==signature[j],"signature changes under trade");
    }
    require(signature_sizes[-1]==17280,"unlabelled states not isolated");
    for(int a=0;a<8;a++){
        require(signature_sizes[a]==18000,"parity sector size");
        require(signature_components[a].size()==1,"parity sector disconnected");
        int idx=*signature_components[a].begin();
        require(blocks[idx].size()==18000,"parity sector size conflict");
    }
    set<int> sectors;
    for(auto &x:signature_components)sectors.insert(*x.second.begin());
    require(sectors.size()==8,"distinct parity sectors");
    // Every sector is a relabelling of the seed sector and the even
    // isotopy subgroup is transitive within it; therefore the one-source
    // breadth-first distances are the distances from every mobile vertex.
    cout<<"LATIN5_EXHAUSTIVE_ORBIT_CERTIFICATE_PASS\n";
    cout<<"states=161280 isolated=17280 mobile_components=8 sector_size=18000\n";
    cout<<"edges=288000 degree_mobile=4 radius_mobile=13 diameter_mobile=13\n";
    cout<<"profile=";
    for(size_t i=0;i<hist.size();i++)cout<<(i?",":"")<<hist[i];
    cout<<"\n8 consistent parity sectors; no parity-crossing trades\n";
    return 0;
}
