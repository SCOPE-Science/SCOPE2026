// Exhaustive certificate for smallest inclusion-maximal mutual-visibility sets of Q_6.
// Compile: g++ -std=c++17 -O3 verify_permutations.cpp -o verify_permutations
// Vertices are six-bit integers, adjacent when they differ in one bit.
#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;
constexpr int DIM=6, N=1<<DIM;
static vector<uint64_t> path_interiors[N][N];

// A shortest path flips each differing coordinate exactly once.
static vector<uint64_t> interiors(int a, int b) {
    vector<int> diff;
    for(int j=0;j<DIM;++j) if(((a^b)>>j)&1)diff.push_back(j);
    vector<uint64_t> result;
    do {
        int current=a;
        uint64_t path_mask=0;
        for(int step=0;step+1<(int)diff.size();++step){
            current^=1<<diff[step];
            path_mask|=uint64_t(1)<<current;
        }
        result.push_back(path_mask);
    }while(next_permutation(diff.begin(),diff.end()));
    return result;
}
static bool mutual(uint64_t S) {
    int vertices[8],k=0;
    for(uint64_t remaining=S;remaining;remaining&=remaining-1)
        vertices[k++]=__builtin_ctzll(remaining);
    for(int i=0;i<k;++i)for(int j=i+1;j<k;++j){
        bool found=false;
        for(uint64_t interior:path_interiors[vertices[i]][vertices[j]])
            if((S&interior)==0){found=true;break;}
        if(!found)return false;
    }
    return true;
}
static bool inclusion_maximal(uint64_t S) {
    // Caller has already checked mutual visibility.
    for(int vertex=0;vertex<N;++vertex)if(!(S&(uint64_t(1)<<vertex)))
        if(mutual(S|(uint64_t(1)<<vertex)))return false;
    return true;
}
static uint64_t closed_neighborhood(int x){
    uint64_t m=uint64_t(1)<<x;
    for(int j=0;j<DIM;++j)m|=uint64_t(1)<<(x^(1<<j));
    return m;
}
int main() {
    for(int a=0;a<N;++a)for(int b=a+1;b<N;++b)
        path_interiors[a][b]=interiors(a,b);
    for(int k=2;k<=7;++k){
        int r=k-1;
        uint64_t t=(uint64_t(1)<<r)-1,visited=0,feasible=0,maximal=0;
        vector<uint64_t> minimal;
        while(t<(uint64_t(1)<<63)){
            uint64_t S=uint64_t(1)|(t<<1); // All k-sets containing vertex zero.
            if(mutual(S)){
                ++feasible;
                if(inclusion_maximal(S)){
                    ++maximal;
                    minimal.push_back(S);
                }
            }
            ++visited;
            uint64_t low=t&-t, next=t+low;
            if(!low||next>=(uint64_t(1)<<63))break;
            t=(((t^next)>>2)/low)|next; // next fixed-cardinality mask
        }
        cout<<"k="<<k<<" considered="<<visited<<" feasible="<<feasible
            <<" maximal="<<maximal<<"\n";
        if(k<7 && maximal!=0)return 1;
        if(k==7){
            if(maximal!=7)return 2;
            for(uint64_t S:minimal){
                bool a_star=false;
                for(int center=0;center<N;++center)
                    if(S==closed_neighborhood(center)){a_star=true;break;}
                if(!a_star)return 3;
            }
        }
    }
    cout<<"PERMUTATION_VERIFY_OK\n";
}
