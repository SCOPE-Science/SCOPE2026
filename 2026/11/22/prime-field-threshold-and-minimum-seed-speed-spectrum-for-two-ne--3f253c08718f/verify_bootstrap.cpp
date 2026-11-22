// Independent exhaustive checker for two-neighbor bootstrap on PG(2,q), q=2,3,4.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
int mul(int x,int y,int q) {
    if (q!=4) return (x*y)%q;
    const int t[4][4]={{0,0,0,0},{0,1,2,3},{0,2,3,1},{0,3,1,2}};
    return t[x][y];
}
int plus_(int x,int y,int q){return q==4 ? (x^y):(x+y)%q;}
vector<array<int,3>> vectors(int q){
    set<array<int,3>> vs;
    for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++){
        if(a==0&&b==0&&c==0)continue;
        int lead=a?a:(b?b:c),inv=1;
        while(mul(lead,inv,q)!=1) inv++;
        vs.insert({mul(a,inv,q),mul(b,inv,q),mul(c,inv,q)});
    }
    return vector<array<int,3>>(vs.begin(),vs.end());
}
vector<uint64_t> graph(int q,int &v){
    auto P=vectors(q); v=P.size();
    assert(v==q*q+q+1);
    vector<uint64_t> adj(2*v,0);
    for(int i=0;i<v;i++)for(int j=0;j<v;j++){
        int d=0;
        for(int k=0;k<3;k++)d=plus_(d,mul(P[i][k],P[j][k],q),q);
        if(d==0){adj[i]|=1ULL<<(v+j);adj[v+j]|=1ULL<<i;}
    }
    return adj;
}
pair<bool,int> infected(const vector<uint64_t>&adj,uint64_t seed){
    uint64_t mask=seed;
    int steps=0; int n=adj.size();
    const uint64_t all=(1ULL<<n)-1;
    for(;;){
        uint64_t nxt=mask;
        for(int i=0;i<n;i++)if(!(mask&(1ULL<<i)))
            if(__builtin_popcountll(mask&adj[i])>=2)nxt|=1ULL<<i;
        if(nxt==mask) return {mask==all,steps};
        mask=nxt;steps++;
    }
}
void run(int q){
    int v;auto adj=graph(q,v);
    int k=q==4?5:4;
    map<int,uint64_t> shore;
    map<pair<int,int>,uint64_t> times;
    for(int sz=k-1;sz<=k;sz++){
        uint64_t num_good=0;
        vector<int> ix(sz);
        for(int t=0;t<sz;t++)ix[t]=t;
        while(true){
            uint64_t seed=0;
            for(auto x:ix)seed|=1ULL<<x;
            auto [good,steps]=infected(adj,seed);
            if(good){
                num_good++;
                if(sz==k){int s=0;for(auto x:ix)if(x<v)s++;shore[s]++;times[{s,steps}]++;}
            }
            int at=sz-1;
            for(;at>=0;at--)if(ix[at]<(2*v-sz+at))break;
            if(at<0)break;
            ix[at]++;
            for(int t=at+1;t<sz;t++)ix[t]=ix[t-1]+1;
        }
        if(sz==k-1)assert(num_good==0);
        cout << "q="<<q<<" k="<<sz<<" good="<<num_good<<"\n";
    }
    const map<int,uint64_t> expected = q==2 ? map<int,uint64_t>{{0,7},{1,28},{3,28},{4,7}} :
        q==3 ? map<int,uint64_t>{{0,234},{1,936},{3,936},{4,234}} :
         map<int,uint64_t>{{0,11088},{1,55440},{2,100800},{3,100800},{4,55440},{5,11088}};
    assert(shore==expected);
    for(auto [key,n]:times)cout<<"shore="<<key.first<<" rounds="<<key.second<<" count="<<n<<"\n";
    assert(q!=4 || (times.at({0,4})==1008 && times.at({2,6})==30240 && times.at({5,5})==10080));
}
int main(){run(2);run(3);run(4);cout<<"VERIFY_OK\n";}
