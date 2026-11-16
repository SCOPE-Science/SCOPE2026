// Exact integer permanent verification of all signed edge assignments of Q4.
// C++17, self contained: c++ -O2 -std=c++17 verify_permanent.cpp -o verify_permanent
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <utility>
#include <vector>
using namespace std;

static void transform(vector<int>& a) {
    for(int step=1; step<(int)a.size(); step*=2)
        for(int base=0; base<(int)a.size(); base+=2*step)
            for(int j=base;j<base+step;++j) {
                const int x=a[j], y=a[j+step];
                a[j]=x+y; a[j+step]=x-y;
            }
}

int main(){
    vector<pair<int,int>> edges;
    for(int u=0;u<16;++u) for(int b=0;b<4;++b){
        int v=u^(1<<b);
        if(u<v) edges.emplace_back(u,v);
    }
    sort(edges.begin(),edges.end());
    assert(edges.size()==32);
    vector<int> parent(16);iota(parent.begin(),parent.end(),0);
    auto root=[&](int v) {while(parent[v]!=v) v=parent[v]; return v;};
    vector<bool> istree(32,false);
    for(int i=0;i<32;++i){
        int a=root(edges[i].first),b=root(edges[i].second);
        if(a!=b){parent[a]=b;istree[i]=true;}
    }
    vector<int> chord(32,-1);
    int dim=0; for(int i=0;i<32;++i) if(!istree[i]) chord[i]=dim++;
    assert(dim==17);

    vector<int> even,odd;
    for(int u=0;u<16;++u)
        (__builtin_popcount((unsigned)u)%2 ? odd : even).push_back(u);
    assert(even.size()==8 && odd.size()==8);
    int cidx[8][8];
    for(auto& row:cidx) for(int& c:row) c=-1;
    for(int i=0;i<32;++i){
        int u=edges[i].first,v=edges[i].second;
        if(__builtin_popcount((unsigned)u)%2) swap(u,v);
        auto a=find(even.begin(),even.end(),u)-even.begin();
        auto b=find(odd.begin(),odd.end(),v)-odd.begin();
        assert(a<8 && b<8);
        cidx[a][b]=chord[i];
    }
    const int N=1<<dim;
    vector<int> vals(N),dp(256),next(256);
    int adjacency[8][8];
    for(int row=0;row<8;++row) for(int col=0;col<8;++col)
        adjacency[row][col]=cidx[row][col]!=-1 ||
            [&]{int u=even[row],v=odd[col];
                return __builtin_popcount((unsigned)(u^v))==1;}();
    for(int bits=0;bits<N;++bits){
        fill(dp.begin(),dp.end(),0); dp[0]=1;
        for(int r=0;r<8;++r){
            fill(next.begin(),next.end(),0);
            for(int subset=0;subset<256;++subset) if(__builtin_popcount((unsigned)subset)==r && dp[subset]){
                for(int col=0;col<8;++col) if(!(subset&(1<<col)) && adjacency[r][col]){
                    int ci=cidx[r][col];
                    int sign=(ci>=0 && (bits&(1<<ci))) ? -1:1;
                    next[subset|(1<<col)]+=dp[subset]*sign;
                }
            }
            dp.swap(next);
        }
        vals[bits]=dp[255];
    }
    map<int,int> hist;
    int gcdval=0;
    int64_t moment=0;
    for(int v:vals){hist[abs(v)]++;gcdval=gcd(gcdval,abs(v));moment+=(int64_t)v*v;}
    assert(moment==(int64_t)N*272);
    assert(hist[0]==44230 && hist[8]==44896 && gcdval==8);
    vector<int> projection(N);
    for(int i=0;i<N;++i) projection[i]=vals[i]!=0;
    transform(projection);
    int64_t L1=0;for(int x:projection) L1+=abs(x);
    assert(L1==10389668);
    cout << "{\"zero_reduced\":"<<hist[0]<<",\"nonzero_reduced\":"<<N-hist[0]
         <<",\"min_positive\":8,\"projection_abs_sum\":"<<L1
         <<",\"projection_denominator\":"<<N<<",\"gcd_all\":"<<gcdval
         <<",\"parseval_squared_sum\":"<<moment<<",\"abs_histogram\":{";
    bool first=true;
    for(auto kv:hist){if(!first)cout<<',';first=false;cout<<'"'<<kv.first<<"\":"<<kv.second;}
    cout<<"}}\n";
}
