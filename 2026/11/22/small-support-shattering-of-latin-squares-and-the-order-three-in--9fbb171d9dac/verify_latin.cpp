// Exhaustive reconstruction through coordinate isotopes of the cyclic Latin table.
#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using Triple=array<int,3>;
static vector<array<int,3>> perms(){
    vector<array<int,3>> out; array<int,3> p{0,1,2};
    do {out.push_back(p);} while(next_permutation(p.begin(),p.end()));
    return out;
}
int main(){
    auto P=perms();
    set<array<int,9>> squares;
    for(auto r:P) for(auto c:P) for(auto s:P){
        array<int,9> L{};
        for(int i=0;i<3;i++)for(int j=0;j<3;j++)
            L[3*i+j]=s[(r[i]+c[j])%3];
        squares.insert(L);
    }
    assert(squares.size()==12);
    vector<Triple> pts;
    for(int r=0;r<3;r++)for(int c=0;c<3;c++)for(int s=0;s<3;s++)pts.push_back({r,c,s});
    vector<uint32_t> concepts;
    for(auto L:squares){
        uint32_t bits=0;
        for(int i=0;i<27;i++)if(L[3*pts[i][0]+pts[i][1]]==pts[i][2])bits|=1u<<i;
        concepts.push_back(bits);
    }
    array<int,5> f{};
    vector<array<int,2>> edges;
    vector<array<int,3>> triangles;
    auto shattered=[&](const vector<int>& s)->bool{
        set<unsigned> traces;
        for(uint32_t L:concepts){
            unsigned pattern=0;
            for(unsigned k=0;k<s.size();k++)if(L&(1u<<s[k]))pattern|=1u<<k;
            traces.insert(pattern);
        }
        return traces.size()==(1u<<s.size());
    };
    f[0]=1;
    for(int a=0;a<27;a++) if(shattered({a}))f[1]++;
    for(int a=0;a<27;a++)for(int b=a+1;b<27;b++)
        if(shattered({a,b})){f[2]++;edges.push_back({a,b});}
    for(int a=0;a<27;a++)for(int b=a+1;b<27;b++)for(int c=b+1;c<27;c++)
        if(shattered({a,b,c})){f[3]++;triangles.push_back({a,b,c});}
    for(int a=0;a<27;a++)for(int b=a+1;b<27;b++)for(int c=b+1;c<27;c++)for(int d=c+1;d<27;d++)
        if(shattered({a,b,c,d}))f[4]++;
    assert((f==array<int,5>{1,27,270,216,0}));
    map<array<int,2>,int> eid;
    for(int i=0;i<int(edges.size());i++)eid[edges[i]]=i;
    set<int> tri_edges;
    array<bitset<300>,300> basis{};
    int rank=0;
    for(auto t:triangles){
        bitset<300> b;
        for(int i=0;i<3;i++)for(int j=i+1;j<3;j++){
            array<int,2> e{t[i],t[j]};
            int ix=eid.at(e);b.set(ix);tri_edges.insert(ix);
        }
        for(int piv=299;piv>=0;piv--){
            if(!b[piv])continue;
            if(basis[piv].none()) {basis[piv]=b;rank++;break;}
            b^=basis[piv];
        }
    }
    assert(tri_edges.size()==162);
    assert(edges.size()-tri_edges.size()==108);
    assert(rank==133);
    assert(int(edges.size())-26-rank==111);
    assert(int(triangles.size())-rank==83);
    cout<<"LATIN_ISOTOPE_PASS squares=12 polynomial=1,27,270,216,0 facets=108,216 rank=133 beta=111,83\n";
}
