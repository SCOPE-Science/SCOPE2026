// Self-contained exhaustive verification of optimum locating-dominating sets of GP(10,2).
// c++ -O2 -std=c++17 checks/verify_ld_cpp.cpp -o /tmp/verify_ld && /tmp/verify_ld
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <unordered_map>
#include <set>
#include <queue>
#include <vector>
#include <algorithm>
using U=std::uint32_t;
int main(){
    std::array<U,20> adj{};
    auto edge=[&](int a,int b){adj[a]|=U(1)<<b;adj[b]|=U(1)<<a;};
    for(int i=0;i<10;i++){
        edge(i,(i+1)%10);edge(i,10+i);edge(10+i,10+((i+2)%10));
    }
    std::array<U,20> closed{};
    for(int i=0;i<20;i++){assert(__builtin_popcount(adj[i])==3);closed[i]=adj[i]|(U(1)<<i);}
    std::vector<U> states;
    std::array<int,8> layers{};
    for(U mask=0;mask<(U(1)<<20);mask++){
        int k=__builtin_popcount(mask);
        if(k==0||k>7)continue;
        std::set<U> signatures;
        bool okay=true;
        for(int v=0;v<20;v++) if(!((mask>>v)&1U)) {
            U sig=closed[v]&mask;
            if(!sig||!signatures.insert(sig).second){okay=false;break;}
        }
        if(okay){layers[k]++;if(k==7)states.push_back(mask);}
    }
    for(int k=1;k<7;k++)assert(layers[k]==0);
    assert(layers[7]==220 && states.size()==220);
    std::unordered_map<U,int> id;
    for(int i=0;i<(int)states.size();i++)id.emplace(states[i],i);
    std::vector<std::vector<int>> g(states.size());
    int edgecount=0;
    for(int i=0;i<(int)states.size();i++){
        U mask=states[i];
        for(int out=0;out<20;out++) if((mask>>out)&1U)
          for(int in=0;in<20;in++) if(!((mask>>in)&1U)){
            U t=mask^(U(1)<<out)^(U(1)<<in);
            auto it=id.find(t);if(it==id.end())continue;
            assert((adj[out]>>in)&1U); // every valid jump is an edge slide
            g[i].push_back(it->second);
            if(i<it->second)edgecount++;
          }
    }
    assert(edgecount==570);
    std::array<int,21> hist{};
    for(auto const &a:g){assert(a.size()<=20);hist[a.size()]++;}
    assert(hist[4]==120 && hist[6]==40 && hist[7]==60);
    int radius=500,diameter=0;
    for(int src=0;src<(int)g.size();src++){
        std::vector<int> dist(g.size(),-1);
        dist[src]=0;std::queue<int> q;q.push(src);
        while(!q.empty()){
            int v=q.front();q.pop();
            for(int w:g[v])if(dist[w]==-1){dist[w]=dist[v]+1;q.push(w);}
        }
        assert(*std::min_element(dist.begin(),dist.end())>=0);
        int ecc=*std::max_element(dist.begin(),dist.end());
        radius=std::min(radius,ecc);diameter=std::max(diameter,ecc);
    }
    assert(radius==8 && diameter==9);
    std::cout<<"CPP_LD_PASS min=7 count=220 edges=570 degree_profile=4:120,6:40,7:60\n";
    std::cout<<"CPP_LD_PASS all_valid_jumps_are_slides=yes connected=yes radius=8 diameter=9\n";
    return 0;
}
