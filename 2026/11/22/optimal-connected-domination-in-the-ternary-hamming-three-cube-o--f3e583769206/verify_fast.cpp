// Exact finite verification for the connected-dominating-set reconfiguration of K3 square K3 square K3.
// Build: g++ -std=c++17 -O3 verify_fast.cpp -o verify_fast
// Run:   ./verify_fast
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

int main() {
    constexpr int N = 27;
    constexpr uint32_t FULL = (uint32_t(1) << N) - 1;
    array<uint32_t,N> nbr{};
    for(int i=0;i<N;++i) for(int j=0;j<N;++j){
        int a=i,b=j,dist=0;
        for(int t=0;t<3;++t){dist+=(a%3!=b%3);a/=3;b/=3;}
        if(dist==1)nbr[i]|=uint32_t(1)<<j;
    }
    auto valid=[&](uint32_t s){
        uint32_t dom=s;
        for(uint32_t v=s;v;v&=v-1)dom|=nbr[__builtin_ctz(v)];
        if(dom!=FULL)return false;
        uint32_t seen=s&-s,front=seen;
        while(front){
            int i=__builtin_ctz(front);front&=front-1;
            uint32_t newer=nbr[i]&s&~seen;
            seen|=newer;front|=newer;
        }
        return seen==s;
    };
    vector<uint32_t> states;
    array<long long,9> tested{},solutions{};
    for(int k=4;k<=8;++k){
        uint32_t s=(uint32_t(1)<<k)-1;
        while(s<=FULL){
            ++tested[k];
            if(valid(s)){
                ++solutions[k];
                if(k==8)states.push_back(s);
            }
            uint32_t c=s&-s,r=s+c;
            if(!r||r>FULL)break;
            s=(((r^s)>>2)/c)|r;
        }
    }
    for(int k=4;k<=7;++k)assert(solutions[k]==0);
    assert(tested[8]==2220075 && states.size()==11340);
    unordered_map<uint32_t,int> locate;
    locate.reserve(states.size()*2);
    for(int i=0;i<(int)states.size();++i)locate.emplace(states[i],i);
    int n=states.size();
    vector<vector<int>> jump(n),slide(n);
    long long ej=0,es=0;
    for(int i=0;i<n;++i){
        uint32_t s=states[i];
        for(uint32_t x=s;x;x&=x-1){
            int u=__builtin_ctz(x);
            for(uint32_t y=FULL&~s;y;y&=y-1){
                int v=__builtin_ctz(y);
                auto it=locate.find(s^(uint32_t(1)<<u)^(uint32_t(1)<<v));
                if(it==locate.end()||it->second<=i)continue;
                int j=it->second;
                jump[i].push_back(j);jump[j].push_back(i);++ej;
                if((nbr[u]>>v)&1){slide[i].push_back(j);slide[j].push_back(i);++es;}
            }
        }
    }
    assert(ej==73386 && es==14094);
    map<int,int> slideSizes;
    map<int,int> slideDiametersBySize;
    vector<int> comp(n,-1);
    int cid=0;
    for(int v=0;v<n;++v){
        if(comp[v]!=-1)continue;
        vector<int> vertices{v};comp[v]=cid;
        for(size_t t=0;t<vertices.size();++t)
            for(int w:slide[vertices[t]])if(comp[w]==-1){comp[w]=cid;vertices.push_back(w);}
        ++slideSizes[(int)vertices.size()];
        int dia=0;
        for(int x:vertices){
            vector<int> d(n,-1);vector<int> q{x};d[x]=0;
            for(size_t z=0;z<q.size();++z)
                for(int w:slide[q[z]])if(d[w]<0){d[w]=d[q[z]]+1;q.push_back(w);}
            for(int y:vertices)dia=max(dia,d[y]);
        }
        if(slideDiametersBySize.count(vertices.size()))assert(slideDiametersBySize[(int)vertices.size()]==dia);
        else slideDiametersBySize[(int)vertices.size()]=dia;
        ++cid;
    }
    assert(cid==504);
    assert((slideSizes==map<int,int>{{2,162},{9,72},{18,108},{52,162}}));
    assert((slideDiametersBySize==map<int,int>{{2,1},{9,4},{18,9},{52,11}}));
    map<int,long long> jumpDistribution;
    map<int,int> eccDistribution;
    for(int i=0;i<n;++i){
        vector<int> d(n,-1),q{i};d[i]=0;
        for(size_t t=0;t<q.size();++t)
            for(int w:jump[q[t]])if(d[w]<0){d[w]=d[q[t]]+1;q.push_back(w);}
        assert((int)q.size()==n);
        int eccentricity=*max_element(d.begin(),d.end());
        ++eccDistribution[eccentricity];
        for(int j=i+1;j<n;++j)++jumpDistribution[d[j]];
    }
    assert((eccDistribution==map<int,int>{{9,11340}}));
    const map<int,long long> expected{{1,73386},{2,448416},{3,1964574},{4,5972616},
        {5,12581730},{6,19397880},{7,17513334},{8,6099786},{9,240408}};
    assert(jumpDistribution==expected);
    cout<<"VERIFIED k=8 configurations=11340 jump_edges=73386 slide_edges=14094 "
        <<"jump_radius=9 jump_diameter=9 slide_components=504\n";
    for(auto [size,count]:slideSizes)
        cout<<"component_size="<<size<<" count="<<count<<" diameter="<<slideDiametersBySize[size]<<"\n";
    for(auto [dist,count]:jumpDistribution)cout<<"jump_pair_distance="<<dist<<" count="<<count<<"\n";
}
