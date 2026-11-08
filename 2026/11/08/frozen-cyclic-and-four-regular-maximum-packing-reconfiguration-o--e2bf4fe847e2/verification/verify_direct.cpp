// Exhaustive direct independent-set and edge generation, independent of gap encodings.
// Compile: g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

bool valid(uint64_t s, int N) {
    for (int u = 0; u < N; ++u) if (s >> u & 1ULL)
        for (int d=1;d<=2;++d) if (s >> ((u+d)%N) & 1ULL) return false;
    return true;
}
void generate(int N, int k, int at, int taken, uint64_t mask, vector<uint64_t>& out){
    if (taken == k) { if (valid(mask,N)) out.push_back(mask); return; }
    if (N-at < k-taken) return;
    generate(N,k,at+1,taken,mask,out);
    generate(N,k,at+1,taken+1,mask|(1ULL<<at),out);
}
int main(){
 for (int N=6;N<=26;++N){
    int m=N/3, r=N%3;
    vector<uint64_t> ss;generate(N,m,0,0,0,ss);
    unordered_map<uint64_t,int> ids;
    for(int i=0;i<(int)ss.size();++i) ids[ss[i]]=i;
    vector<vector<int>> g(ss.size());
    for (int i=0;i<(int)ss.size();++i){
        uint64_t s=ss[i];
        for (int u=0;u<N;++u) if (s>>u&1ULL)
          for(int d : {-2,-1,1,2}) {
              int v=(u+d+N)%N;
              if(s>>v&1ULL)continue;
              uint64_t t=s^(1ULL<<u)^(1ULL<<v);
              auto it=ids.find(t);
              if(it!=ids.end()) g[i].push_back(it->second);
          }
        sort(g[i].begin(),g[i].end());
        assert(unique(g[i].begin(),g[i].end())==g[i].end());
    }
    int edge_twice=0;
    for (int i=0;i<(int)ss.size();++i){
        edge_twice+=g[i].size();
        for(int j:g[i]) assert(binary_search(g[j].begin(),g[j].end(),i));
        if(r==0) assert(g[i].size()==0);
        if(r==1) assert(g[i].size()==2);
        if(r==2) assert(g[i].size()==4);
    }
    int triangles_x6=0;
    for(int u=0;u<(int)ss.size();++u)
        for(int v:g[u])
            for(int w:g[v]) if(binary_search(g[u].begin(),g[u].end(),w))
                ++triangles_x6;
    assert(triangles_x6%6==0);
    vector<char> seen(ss.size(),0);vector<int> components;
    for(int s=0;s<(int)ss.size();++s) if(!seen[s]){
        queue<int> q;q.push(s);seen[s]=1;int cnt=0;
        while(!q.empty()){
            int u=q.front();q.pop();++cnt;
            for(int v:g[u]) if(!seen[v]){seen[v]=1;q.push(v);}
        }
        components.push_back(cnt);
    }
    sort(components.begin(),components.end(),greater<int>());
    int want_v=r==0?3:(r==1?N:N*(m+1)/2);
    int want_e=r==0?0:(r==1?N:N*(m+1));
    int want_tri=r==2?N:0;
    assert((int)ss.size()==want_v);
    assert(edge_twice/2==want_e);
    assert(triangles_x6/6==want_tri);
    assert(components.size()==(r==0?3:1));
    if(r==0) assert(components==vector<int>({1,1,1}));
    else assert(components[0]==want_v);
    if(N>=22)cout<<"N="<<N<<" states="<<want_v<<" edges="<<want_e<<" triangles="<<want_tri<<"\n";
 }
 cout<<"DIRECT_ENUMERATION_PASS\n";
}
