// Standalone independent exact checker, C++17.
// Petersen is reconstructed as a generalized Petersen graph GP(5,2).
// No third-party libraries.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using Edge=pair<int,int>;
static bool has_edge(const vector<Edge>& es,int a,int b){
    if(a>b) swap(a,b);
    return binary_search(es.begin(),es.end(),Edge(a,b));
}
static bool factor(const vector<Edge>& edges,int mask){
    array<int,10> degree{};array<vector<int>,10> nbr;
    for(int i=0;i<15;i++) if(mask&(1<<i)){
        auto [a,b]=edges[i];degree[a]++;degree[b]++;nbr[a].push_back(b);nbr[b].push_back(a);
    }
    auto sorted=degree;sort(sorted.begin(),sorted.end());
    if(sorted!=array<int,10>{0,1,1,1,1,1,1,2,2,2}) return false;
    int seen=0;vector<pair<int,int>> comps;
    for(int a=0;a<10;a++) if(!(seen&(1<<a))){
        queue<int> q;q.push(a);seen|=1<<a;int count=0,degree_sum=0;
        while(!q.empty()){
            int v=q.front();q.pop();count++;degree_sum+=degree[v];
            for(int u:nbr[v]) if(!(seen&(1<<u))){seen|=1<<u;q.push(u);}
        }
        comps.push_back({count,degree_sum/2});
    }
    sort(comps.begin(),comps.end());
    return comps==vector<pair<int,int>>{{1,0},{3,2},{3,2},{3,2}};
}
int main(){
    set<Edge> es;
    auto add=[&](int a,int b){if(a>b)swap(a,b);es.insert({a,b});};
    for(int i=0;i<5;i++){
        add(i,(i+1)%5);add(i,5+i);add(5+i,5+(i+2)%5);
    }
    vector<Edge> edges(es.begin(),es.end());
    assert(edges.size()==15);
    // Check isomorphism with the disjoint-pair model on all ten original vertices.
    vector<Edge> pair_model;
    vector<int> subsets;
    for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)subsets.push_back((1<<i)|(1<<j));
    for(int i=0;i<10;i++)for(int j=i+1;j<10;j++)if(!(subsets[i]&subsets[j]))pair_model.push_back({i,j});
    int mapKGtoGP[10]={0,9,2,8,3,6,7,5,1,4};
    for(int i=0;i<10;i++)for(int j=i+1;j<10;j++){
        assert(has_edge(pair_model,i,j)==has_edge(edges,mapKGtoGP[i],mapKGtoGP[j]));
    }
    array<int,15> N{};
    for(int i=0;i<15;i++)for(int j=0;j<15;j++)if(i!=j){
        auto [a,b]=edges[i];auto [c,d]=edges[j];
        if(a==c||a==d||b==c||b==d)N[i]|=1<<j;
    }
    for(auto x:N)assert(__builtin_popcount((unsigned)x)==4);
    vector<int> minimum;array<int,16> histogram{};
    int p3count=0;
    for(int m=0;m<(1<<15);m++){
        int k=__builtin_popcount((unsigned)m);
        bool total=true;
        for(int i=0;i<15;i++) if(!(N[i]&m)){total=false;break;}
        if(total){
            set<int> signatures;
            for(int i=0;i<15;i++)if(!(m&(1<<i)))signatures.insert(N[i]&m);
            if((int)signatures.size()==15-k){histogram[k]++;if(k==6) minimum.push_back(m);}
        }
        if(k==6){
            bool ismin=total;
            if(ismin){set<int>s;for(int i=0;i<15;i++)if(!(m&(1<<i)))s.insert(N[i]&m);ismin=(s.size()==9);}
            assert(ismin==factor(edges,m));
            if(factor(edges,m))p3count++;
        }
    }
    array<int,16> expected={0,0,0,0,0,0,110,1590,3810,4150,2838,1350,455,105,15,1};
    assert(histogram==expected);assert(minimum.size()==110&&p3count==110);
    set<int> code(minimum.begin(),minimum.end());
    map<int,vector<int>> adj;
    for(int m:minimum){
        for(int i=0;i<15;i++)if(m&(1<<i))for(int j=0;j<15;j++)if(!(m&(1<<j))){
            int t=m^(1<<i)^(1<<j);if(code.count(t))adj[m].push_back(t);
        }
    }
    map<int,int> degrees;int twice_edges=0;
    for(auto &[m,nbr]:adj){degrees[(int)nbr.size()]++;twice_edges+=(int)nbr.size();}
    assert((degrees==map<int,int>{{3,40},{4,60},{6,10}}));
    assert(twice_edges==420);
    int radius=110,diameter=0;map<int,int> eccentricities;
    for(int source:minimum){
        map<int,int> distances;queue<int> q;q.push(source);distances[source]=0;
        while(!q.empty()){
            int u=q.front();q.pop();
            for(int v:adj[u]) if(!distances.count(v)){
                distances[v]=distances[u]+1;q.push(v);
            }
        }
        assert(distances.size()==110);
        int ecc=0;for(auto [v,d]:distances)ecc=max(ecc,d);
        radius=min(radius,ecc);diameter=max(diameter,ecc);eccentricities[ecc]++;
    }
    assert(radius==6&&diameter==7);
    assert((eccentricities==map<int,int>{{6,60},{7,50}}));
    cout<<"PASS_PETERSEN_LINE_LTD_GP_32768\n";
    cout<<"MINIMA 110 THREE_PATH_FOREST 110 EXCHANGE_EDGES 210 RADIUS 6 DIAMETER 7\n";
}
