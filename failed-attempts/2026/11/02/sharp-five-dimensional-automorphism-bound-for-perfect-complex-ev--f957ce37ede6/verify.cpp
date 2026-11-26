// Exhaustive support-graph upper bound for dimension-five perfect evolution algebras.
// Compile: g++ -std=c++17 -O3 -DNDEBUG evolution5_bound.cpp -o evolution5_bound
// Run: ./evolution5_bound
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <cstdlib>
#include <string>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
constexpr int n = 5;
constexpr uint32_t total = 1u << (n*n);
struct P {
    array<int,n> p{}; // vertex i maps to p[i]
    array<unsigned,1<<n> col{}; // mapped row bits
};
vector<P> perms;
static inline uint32_t conjugate(uint32_t mask, const P& perm) {
    uint32_t result=0;
    for(int i=0;i<n;++i) {
        unsigned bits=(mask>>(n*i)) & ((1<<n)-1);
        result |= uint32_t(perm.col[bits]) << (n*perm.p[i]);
    }
    return result;
}
static int gcd(int a,int b) {while(b){int t=a%b;a=b;b=t;}return a;}
static int lcm(int a,int b) {return a/gcd(a,b)*b;}
// Find cycle-cover permutation among graph edges, choose smallest root count.
static bool cycle_cover(uint32_t mask, array<int,n>& best, int& bound) {
    bool found=false; bound=0;
    for(const auto& v:perms) {
        bool valid=true;
        for(int i=0;i<n;++i) if(!(mask&(1u<<(n*i+v.p[i])))){valid=false;break;}
        if(!valid)continue;
        int prod=1;array<bool,n> seen{};
        for(int i=0;i<n;++i)if(!seen[i]){
            int len=0,j=i;
            while(!seen[j]){seen[j]=true;j=v.p[j];++len;}
            prod*=((1<<len)-1);
        }
        if(!found||prod<bound){found=true;bound=prod;best=v.p;}
    }
    return found;
}
static int diagonal_group_size(uint32_t mask,const array<int,n>& cover,int upper) {
    array<int,n> cycle{},power{},rootorder{};
    int cyc=0,L=1;
    for(int i=0;i<n;++i)if(rootorder[i]==0){
        int j=i,len=0;
        do{++len;j=cover[j];}while(j!=i);
        int d=(1<<len)-1;
        L=lcm(L,d);
        int k=0;
        do{cycle[j]=cyc;power[j]=1<<k;rootorder[j]=d;
           ++k;j=cover[j];}while(j!=i);
        ++cyc;
    }
    // Enumerate exponent choices for the cycle roots, with all exponents in Z/L.
    vector<int> bases; for(int i=0;i<n;++i)if(power[i]==1) bases.push_back(i);
    // Note one base per cycle; all cycles have exactly one power==1.
    int valid=0;
    vector<pair<int,int>> edges;
    for(int i=0;i<n;++i)for(int j=0;j<n;++j)
        if(mask&(1u<<(n*i+j)))edges.emplace_back(i,j);
    for(int ix=0;ix<upper;++ix){
        int z=ix;
        array<int,n> initial{};
        for(int base:bases){int ord=rootorder[base];initial[cycle[base]]=z%ord;z/=ord;}
        array<int,n> exps{};
        for(int i=0;i<n;++i){int ord=rootorder[i];
            exps[i]=((long long)(L/ord)*power[i]*initial[cycle[i]])%L;
        }
        bool ok=true;
        for(auto [i,j]:edges) if(exps[j]!=(2*exps[i])%L){ok=false;break;}
        valid+=ok;
    }
    return valid;
}
int main(int argc, char** argv) {
    array<int,n> pp{};iota(pp.begin(),pp.end(),0);
    do{
        P r; r.p=pp;
        for(int b=0;b<(1<<n);++b){unsigned out=0;
            for(int j=0;j<n;++j) if((b>>j)&1)out|=1u<<pp[j];
            r.col[b]=out;
        }
        perms.push_back(r);
    }while(next_permutation(pp.begin(),pp.end()));
    if(argc==2) { // optional independent per-graph inspection
        uint32_t mask=uint32_t(std::stoul(argv[1]));
        if(mask>=total) return 3;
        int aut=0;
        for(const auto& p:perms)aut+=(conjugate(mask,p)==mask);
        array<int,n> cover{}; int cand=0;
        if(!cycle_cover(mask,cover,cand)){
            cout<<"mask="<<mask<<" no_cycle_cover aut="<<aut<<"\n";
            return 0;
        }
        int D=diagonal_group_size(mask,cover,cand);
        cout<<"mask="<<mask<<" diagonal="<<D<<" aut="<<aut
            <<" bound="<<D*aut<<"\n";
        return 0;
    }
    vector<uint8_t> seen((total+7u)/8u,0);
    auto check=[&](uint32_t mask){return (seen[mask>>3]>>(mask&7))&1;};
    auto mark=[&](uint32_t mask){seen[mask>>3]|=uint8_t(1<<(mask&7));};
    uint64_t representatives=0, qualifying=0, weighted=0;
    int max_bound=0, max_graph_aut=0; uint32_t first_best=0, second_mask=0;
    map<int, uint64_t> max_hist;
    for(uint32_t mask=0; mask<total;++mask){
        if(check(mask)) continue;
        ++representatives; int graph_aut=0;
        for(auto& p:perms){uint32_t image=conjugate(mask,p);
            graph_aut += (image==mask);
            mark(image);
        }
        array<int,n> cover{};int cand=0;
        if(!cycle_cover(mask,cover,cand))continue;
        ++qualifying;
        int D=diagonal_group_size(mask,cover,cand);
        int product=D*graph_aut;
        max_hist[product]++;
        if(product>max_bound){max_bound=product;first_best=mask;max_graph_aut=graph_aut;}
        if(product==155)++weighted;
        if(product==126)second_mask=mask;
        if(product>155){cerr<<"COUNTEREXAMPLE mask="<<mask<<" |D|="<<D<<" |AutG|="<<graph_aut<<" bound="<<product<<"\n";return 2;}
    }
    cout<<"n=5\n"<<"labeled_graphs="<<total<<"\n"
        <<"unlabeled_graphs="<<representatives<<"\n"
        <<"unlabeled_cycle_cover_graphs="<<qualifying<<"\n"
        <<"max_diagonal_times_graph_aut="<<max_bound<<"\n"
        <<"max_representative_mask="<<first_best<<"\n"
        <<"max_representative_aut="<<max_graph_aut<<"\n"
        <<"unlabeled_graphs_attaining_upper_bound="<<weighted<<"\n"
        <<"second_highest_bound_126_mask="<<second_mask<<"\n";
    for(auto [val,num]:max_hist) if(val>=120) cout<<"bound_"<<val<<"_graphs="<<num<<"\n";
    cout<<"VERIFY_OK\n";
}
