// Independent prefix-generated checks of 321-avoiding permutation graphs.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra verify_prefix.cpp -o verify_prefix
// Run: ./verify_prefix . All finite checks are supplementary to the all-n proof.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
#include <numeric>
using namespace std;

void produce(int n,vector<int>& p,vector<char>& used,vector<vector<int>>& out){
    if((int)p.size()==n){out.push_back(p);return;}
    for(int x=1;x<=n;x++) if(!used[x]){
        bool forbidden=false;
        for(int j=0;j<(int)p.size();j++)
            for(int i=0;i<j;i++) if(p[i]>p[j] && p[j]>x) forbidden=true;
        if(forbidden)continue;
        used[x]=1;p.push_back(x);
        produce(n,p,used,out);
        p.pop_back();used[x]=0;
    }
}
vector<int> bfs(const vector<vector<int>>& adj,int src){
    vector<int> d(adj.size(),-1); queue<int> q;
    q.push(src);d[src]=0;
    while(!q.empty()){
        int u=q.front();q.pop();
        for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;q.push(v);}
    }
    return d;
}
int main(){
    const vector<int> cat={0,1,2,5,14,42,132,429,1430,4862,16796};
    const vector<int> diam={0,0,1,4,7,12,17,24,31,40,49};
    for(int n=1;n<=10;n++){
        vector<vector<int>> states;vector<int> p; vector<char> used(n+1);
        produce(n,p,used,states);
        assert((int)states.size()==cat[n]);
        map<vector<int>,int> index;
        for(int j=0;j<(int)states.size();j++) index[states[j]]=j;
        vector<vector<int>> adj(states.size());
        int edgecount=0;
        for(int j=0;j<(int)states.size();j++)for(int k=0;k<n-1;k++){
            vector<int> q=states[j];swap(q[k],q[k+1]);
            auto it=index.find(q);
            if(it!=index.end()){
                adj[j].push_back(it->second);
                edgecount++;
            }
        }
        assert(edgecount%2==0);
        int l=(n-1)/2,c=l+1;
        vector<int> a{c},b;
        for(int x=c+1;x<=n;x++){a.push_back(x);b.push_back(x);}
        for(int x=1;x<c;x++){a.push_back(x);b.push_back(x);}
        b.push_back(c);
        int ia=index.at(a),ib=index.at(b);
        auto ds=bfs(adj,ia);
        assert(*min_element(ds.begin(),ds.end())==0);
        assert(find(ds.begin(),ds.end(),-1)==ds.end());
        assert(ds[ib]==diam[n]);
        if(n<=8){
            int dmax=0;
            for(int i=0;i<(int)states.size();i++){
                auto d=bfs(adj,i);
                dmax=max(dmax,*max_element(d.begin(),d.end()));
            }
            assert(dmax==diam[n]);
        }
        cout<<"n="<<n<<" states="<<states.size()<<" edges="<<edgecount/2
            <<" constructed_pair_distance="<<ds[ib]
            <<(n<=8?" all_sources_checked":" witness_only")<<'\n';
    }
    cout<<"PREFIX_ENUMERATION_321_SWAP_METRICS_PASS\n";
}
