// Exhaustive graph checks for derangement swaps by position distance.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;

uint64_t encode(const vector<int> &a) {
    uint64_t k = 0;
    for (int x : a) k = (k << 4) | uint64_t(x);
    return k;
}
struct DSU {
    vector<int> parent, sz;
    explicit DSU(int n): parent(n), sz(n,1) {iota(parent.begin(),parent.end(),0);}
    int get(int x) {return parent[x]==x? x:parent[x]=get(parent[x]);}
    void unite(int x,int y) {x=get(x);y=get(y);if(x==y)return;if(sz[x]<sz[y])swap(x,y);parent[y]=x;sz[x]+=sz[y];}
};
int signature(const vector<int>& p) {
    int n=p.size(),s=0;
    for (int j=0;j<n;j++) if(p[j]>=2&&p[j]<n && j+1<p[j]) s|=1<<(p[j]-2);
    return s;
}
bool valid(const vector<int>& p) {
    for(int j=0;j<(int)p.size();j++)if(p[j]==j+1)return false;
    return true;
}
int main(){
    for(int n=3;n<=9;n++){
        vector<int> p(n); iota(p.begin(),p.end(),1);
        vector<vector<int>> a;
        unordered_map<uint64_t,int> ids;
        do{ if(!valid(p))continue; int id=a.size();a.push_back(p);ids[encode(p)]=id; }while(next_permutation(p.begin(),p.end()));
        DSU connected(a.size()),range2(a.size());
        vector<int> sig(a.size());
        for(int u=0;u<(int)a.size();u++)sig[u]=signature(a[u]);
        size_t edges1=0,edges2=0;
        vector<vector<char>> quotient(1<<(n-2),vector<char>(1<<(n-2),0));
        int isolated=0;
        for(int u=0;u<(int)a.size();u++){
            p=a[u];int degree=0;
            for(int i=0;i<n;i++)for(int j=i+1;j<n&&j<=i+2;j++){
                swap(p[i],p[j]);
                if(valid(p)){
                    auto it=ids.find(encode(p));assert(it!=ids.end());int v=it->second;
                    if(j==i+1){connected.unite(u,v);if(u<v)edges1++;degree++;assert(sig[u]==sig[v]);}
                    range2.unite(u,v);
                    if(j==i+2 && u<v)edges2++;
                    if(sig[u]!=sig[v]){
                        int ds=sig[u]^sig[v];assert(__builtin_popcount(unsigned(ds))==1);
                        quotient[sig[u]][sig[v]]=quotient[sig[v]][sig[u]]=1;
                    }
                }
                swap(p[i],p[j]);
            }
            if(degree==0)isolated++;
        }
        assert(isolated==2);
        vector<int> srep(1<<(n-2),-1);
        for(int u=0;u<(int)a.size();u++){
            int s=sig[u];
            if(srep[s]<0)srep[s]=connected.get(u);
            else assert(srep[s]==connected.get(u));
        }
        vector<int> comps;
        for(int s=0;s<(1<<(n-2));s++){
            assert(srep[s]>=0);
            for(int t=0;t<s;t++)assert(srep[s]!=srep[t]);
        }
        size_t qedges=0;
        for(int s=0;s<(1<<(n-2));s++)for(int t=0;t<s;t++){
            if(quotient[s][t]){assert(__builtin_popcount(unsigned(s^t))==1);qedges++;}
        }
        if(n>=4){
            assert(qedges==size_t(n-2)*(1u<<(n-3)));
            for(int u=1;u<(int)a.size();u++)assert(range2.get(u)==range2.get(0));
        } else {assert(qedges==0);assert(range2.get(0)!=range2.get(1));}
        cout<<"n="<<n<<" states="<<a.size()<<" fibers="<<srep.size()<<" qedges="<<qedges<<" adj_edges="<<edges1<<" range2_edges="<<edges2<<" PASS\n";
    }
    cout<<"CPP_EXHAUSTIVE_PASS\n";
}
