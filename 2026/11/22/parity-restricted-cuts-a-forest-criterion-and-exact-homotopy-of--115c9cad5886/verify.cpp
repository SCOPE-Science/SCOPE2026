// Independent binary-matrix rank certification for parity-constrained cuts.
// C++17: c++ -O2 -std=c++17 verify.cpp -o verify_cpp && ./verify_cpp
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
#include <numeric>
#include <utility>
using namespace std;
int rank_binary(vector<uint64_t> cols) {
    uint64_t basis[64]={}; int ans=0;
    for(auto x:cols){
        while(x){int p=63-__builtin_clzll(x);
            if(!basis[p]){basis[p]=x;ans++;break;}
            x^=basis[p];
        }
    }
    return ans;
}
bool graph_criterion(int n,const vector<pair<int,int>>& e, uint32_t mask){
    vector<int> parent(n);iota(parent.begin(),parent.end(),0);
    auto root=[&](int u){while(parent[u]!=u) u=parent[u];return u;};
    for(int k=0;k<(int)e.size();k++) if(mask>>k&1){
        int u=root(e[k].first),v=root(e[k].second);
        if(u==v)return false;
        parent[u]=v;
    }
    if(n%2)return true;
    vector<int> sz(n);
    for(int i=0;i<n;i++)sz[root(i)]++;
    for(int t:sz)if(t%2)return true;
    return false;
}
int main(){
    for(int n=3;n<=6;n++){
        vector<pair<int,int>> e;
        for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)e.push_back({u,v});
        int m=e.size();vector<uint64_t> col(m,0);
        int row=0;
        for(int S=0;S<(1<<n);S++){
            if(__builtin_popcount((unsigned)S)&1)continue;
            for(int j=0;j<m;j++){
                auto [u,v]=e[j];
                if(((S>>u)^(S>>v))&1)col[j] |=uint64_t(1)<<row;
            }
            row++;
        }
        vector<uint64_t> count(n+1);
        for(uint32_t mask=0;mask<(1u<<m);mask++){
            vector<uint64_t> X;
            for(int j=0;j<m;j++)if((mask>>j)&1)X.push_back(col[j]);
            bool independent=rank_binary(X)==(int)X.size();
            assert(independent==graph_criterion(n,e,mask));
            if(independent)count[X.size()]++;
        }
        cout<<"n="<<n<<" f=";
        for(int k=0;k<=n;k++)cout<<count[k]<<(k==n?'\n':',');
    }
}
