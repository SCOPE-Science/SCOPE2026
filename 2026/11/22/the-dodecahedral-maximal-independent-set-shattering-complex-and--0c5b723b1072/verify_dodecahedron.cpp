// Exhaustive finite computation for the dodecahedral maximal-independent-set shattering complex.
// C++17; standard library only. No external data or randomness.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;
using U = uint32_t;
static constexpr int N=20, FULL=1<<20;
static int pc(U x){return __builtin_popcount(x);}
static int low(U x){return __builtin_ctz(x);}
static int gf2rank(const vector<U>& upper,const vector<U>& lower){
    unordered_map<U,int> row;
    for(int i=0;i<(int)lower.size();++i)row.emplace(lower[i],i);
    int nwords=((int)lower.size()+63)/64;
    vector<vector<uint64_t>> pivot(lower.size());
    int rank=0;
    for(U face:upper){
        vector<uint64_t> col(nwords,0);
        for(U a=face;a;a&=a-1){ U sub=face^(U(1)<<low(a));
            auto it=row.find(sub); assert(it!=row.end());
            int j=it->second;col[j>>6]^=uint64_t(1)<<(j&63);
        }
        for(;;){
            int p=-1;
            for(int j=nwords-1;j>=0;--j)if(col[j]){p=(j<<6)+63-__builtin_clzll(col[j]);break;}
            if(p==-1)break;
            if(pivot[p].empty()){pivot[p]=move(col);++rank;break;}
            for(int j=0;j<nwords;++j)col[j]^=pivot[p][j];
        }
    }
    return rank;
}
int main(){
    array<U,N> adjacency{};
    auto edge=[&](int a,int b){adjacency[a]|=U(1)<<b;adjacency[b]|=U(1)<<a;};
    for(int i=0;i<10;++i){edge(i,(i+1)%10);edge(i,10+i);edge(10+i,10+(i+2)%10);}
    vector<uint8_t> independent(FULL,0), shattered(FULL,0); independent[0]=1;
    vector<U> maximal;
    array<int,9> maximalSizes{};
    for(int s=1;s<FULL;++s){int b=low(s), t=s^(1<<b);
        independent[s]=independent[t] && !(adjacency[b]&t);
    }
    array<int,9> independentSizes{};
    for(U s=0;s<FULL;++s)if(independent[s]){
        ++independentSizes[pc(s)];
        bool isMaximal=true;
        for(int i=0;i<N;++i)if(!(s&(U(1)<<i)) && !(s&adjacency[i])){isMaximal=false;break;}
        if(isMaximal){maximal.push_back(s);++maximalSizes[pc(s)];}
    }
    assert((independentSizes==array<int,9>{1,20,160,660,1510,1912,1240,320,5}));
    assert(maximal.size()==295 && maximalSizes[6]==10 && maximalSizes[7]==280 && maximalSizes[8]==5);
    vector<vector<U>> faces(7);
    for(U s=0;s<FULL;++s)if(independent[s]){
        const int k=pc(s);
        // 295 hypotheses cannot realize 512 distinct traces.
        if(k>8)continue;
        array<int,8> positions{};int j=0;
        for(U a=s;a;a&=a-1)positions[j++]=low(a);
        array<uint8_t,256> traces{};int traceCount=0;
        for(U m:maximal){
            int trace=0;for(int i=0;i<k;++i)if(m&(U(1)<<positions[i]))trace|=1<<i;
            if(!traces[trace]){traces[trace]=1;++traceCount;}
        }
        if(traceCount==(1<<k)){
            shattered[s]=1;
            assert(k<=6);
            faces[k].push_back(s);
        }
    }
    array<int,7> expected{1,20,160,660,1470,1572,310};
    for(int k=0;k<7;++k)assert((int)faces[k].size()==expected[k]);
    array<int,7> facetCount{};
    for(int k=0;k<7;++k)for(U s:faces[k]){
        bool maximalFace=true;
        for(int j=0;j<N;++j)if(!(s&(U(1)<<j)) && shattered[s|(U(1)<<j)]){
            maximalFace=false;break;
        }
        if(maximalFace)++facetCount[k];
    }
    assert(facetCount[4]==10 && facetCount[5]==672 && facetCount[6]==310);
    for(int k=0;k<7;++k)if(k!=4 && k!=5 && k!=6)assert(facetCount[k]==0);
    const array<int,6> expectedRank{1,19,141,519,941,305};
    array<int,8> rank{};
    for(int k=1;k<=6;++k){rank[k]=gf2rank(faces[k],faces[k-1]);assert(rank[k]==expectedRank[k-1]);}
    array<int,7> betti{};
    for(int k=0;k<=6;++k)betti[k]=(int)faces[k].size()-rank[k]-rank[k+1];
    assert((betti==array<int,7>{0,0,0,0,10,326,5}));
    cout<<"PASS dodecahedron: maximal independent sets 295 (10,280,5), faces 1 20 160 660 1470 1572 310, facets 10 672 310, reduced F2 Betti in dimensions 3 4 5 = 10 326 5\n";
}
