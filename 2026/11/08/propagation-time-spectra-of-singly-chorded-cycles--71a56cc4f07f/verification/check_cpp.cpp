// Standard simultaneous zero-forcing simulation, with integer bit masks.
// Reconstructs the graph directly from a cyclic edge list and an extra chord.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int step_count(int n,const vector<uint64_t>& adj,int u,int v) {
    uint64_t blue=(uint64_t(1)<<u)|(uint64_t(1)<<v);
    const uint64_t full=(uint64_t(1)<<n)-1;
    for(int round=0;round<=n;round++) {
        if(blue==full)return round;
        uint64_t add=0;
        for(int x=0;x<n;x++)if((blue>>x)&1) {
            uint64_t white=adj[x]&~blue;
            if(white && (white&(white-1))==0)add|=white;
        }
        if(!add)return -1;
        blue|=add;
    }
    assert(false);return -2;
}
int main() {
    long long checked_pairs=0;int graph_count=0;
    for(int n=4;n<=22;n++)for(int a=2;a<=n-2;a++){
        int b=n-a;
        vector<uint64_t> adj(n,0);
        auto edge=[&](int x,int y){adj[x]|=uint64_t(1)<<y;adj[y]|=uint64_t(1)<<x;};
        for(int k=0;k<n;k++)edge(k,(k+1)%n);
        edge(0,a);
        map<int,int> histogram;
        int forcing_sets=0;
        for(int u=0;u<n;u++)for(int v=u+1;v<n;v++){
            int t=step_count(n,adj,u,v);
            bool adjacent=(v==u+1 || (u==0 && v==n-1));
            if(!adjacent)assert(t==-1);
            else {
                assert(t>=0);
                forcing_sets++;
                int theoretical=-1;
                if(v==u+1 && u<a) theoretical=max(u,a-1-u)+b/2;
                else if(v==u+1) {
                    int j=u-a;
                    theoretical=max(j,b-1-j)+a/2;
                }else theoretical=b-1+a/2; // edge (n-1,0): j=b-1
                assert(t==theoretical);
                histogram[t]++;
            }
            checked_pairs++;
        }
        assert(forcing_sets==n);
        int min_t=a/2+b/2;
        int max_t=max(a-1+b/2,b-1+a/2);
        assert(histogram.begin()->first==min_t && histogram.rbegin()->first==max_t);
        for(int t=min_t;t<=max_t;t++)assert(histogram.count(t));
        int efficient=2+(a%2==0)+(b%2==0);
        assert(histogram[min_t]==efficient);
        int cycle_min=(n-2+1)/2; // ceil((n-2)/2)
        assert(min_t-cycle_min==((a%2==0 && b%2==0)?1:0));
        graph_count++;
    }
    cout<<"INDEPENDENT_CPP_PASS graphs="<<graph_count<<" pairs="<<checked_pairs
        <<" n=4..22 all chord positions and all two-seed sets\n";
}
