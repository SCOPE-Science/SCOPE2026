// Exhaustive Pappus 3-edge-colorings using direct constrained color search.
// Compile: g++ -O2 -std=c++17 coloring_checker.cpp -o check && ./check
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using State = array<int,27>;
vector<pair<int,int>> edges;
vector<int> incid[18];
vector<State> configs;
int used[18] = {};
State cur{};

State normalized(const State& s) {
    State res{};
    int m[3] = {-1,-1,-1}, next=0;
    for(int i=0;i<27;i++) {
        assert(s[i]>=0 && s[i]<3);
        if(m[s[i]] == -1) m[s[i]]=next++;
        res[i]=m[s[i]];
    }
    return res;
}
void generate(int e,int maximum) {
    if(e==27){configs.push_back(cur);return;}
    auto [u,v]=edges[e];
    for(int c=0;c<=min(2,maximum+1);c++) {
        if((used[u]&(1<<c)) || (used[v]&(1<<c))) continue;
        cur[e]=c;
        used[u]|=(1<<c);used[v]|=(1<<c);
        generate(e+1,max(maximum,c));
        used[u]^=(1<<c);used[v]^=(1<<c);
    }
}
vector<vector<int>> adj;
int main(){
    set<pair<int,int>> all;
    int shifts[6]={5,7,-7,7,-7,-5};
    for(int i=0;i<18;i++) {
        int j=(i+1)%18;
        all.insert(minmax(i,j));
        j=(i+shifts[i%6]+18)%18;
        all.insert(minmax(i,j));
    }
    edges.assign(all.begin(),all.end());
    assert(edges.size()==27);
    for(int i=0;i<27;i++) {
        auto [u,v]=edges[i];
        incid[u].push_back(i);incid[v].push_back(i);
    }
    for(int i=0;i<18;i++) assert(incid[i].size()==3);
    generate(0,-1);
    sort(configs.begin(),configs.end());
    configs.erase(unique(configs.begin(),configs.end()),configs.end());
    assert(configs.size()==20);
    map<State,int> id;
    for(int i=0;i<(int)configs.size();i++) id[configs[i]]=i;
    adj.resize(configs.size());
    int colours[][2]={{0,1},{0,2},{1,2}};
    for(int i=0;i<(int)configs.size();i++){
        auto s=configs[i];
        set<int> nbr;
        for(auto ab:colours){
            int a=ab[0], b=ab[1];
            vector<int> seen(27,0);
            for(int k=0;k<27;k++) if(!seen[k] && (s[k]==a || s[k]==b)) {
                queue<int> q;q.push(k);seen[k]=1;
                vector<int> cyc;
                while(!q.empty()){
                    int e=q.front();q.pop();cyc.push_back(e);
                    for(int v:{edges[e].first,edges[e].second}){
                        for(int f:incid[v]) if(!seen[f] && (s[f]==a || s[f]==b)) {
                            seen[f]=1;q.push(f);
                        }
                    }
                }
                State t=s;
                for(int e:cyc)t[e]=(t[e]==a?b:a);
                t=normalized(t);
                if(t!=s){assert(id.count(t));nbr.insert(id.at(t));}
            }
        }
        adj[i].assign(nbr.begin(),nbr.end());
    }
    int edge_count=0, hubs=0, spokes=0;
    for(int i=0;i<20;i++){
        int d=(int)adj[i].size();edge_count+=d;
        if(d==9)hubs++;else {assert(d==3);spokes++;}
        for(int j:adj[i]) assert(find(adj[j].begin(),adj[j].end(),i)!=adj[j].end());
    }
    assert(hubs==2 && spokes==18 && edge_count==72);
    vector<int> component(20,-1);vector<vector<int>> comps;
    for(int i=0;i<20;i++) if(component[i]==-1){
        int label=(int)comps.size();
        vector<int> current;
        queue<int> q;q.push(i);component[i]=label;
        while(!q.empty()){
            int v=q.front();q.pop();current.push_back(v);
            for(int w:adj[v]) if(component[w]==-1){component[w]=label;q.push(w);}
        }
        comps.push_back(current);
    }
    assert(comps.size()==2);
    for(const auto& comp:comps){
        assert(comp.size()==10);
        int hub=-1;
        for(int v:comp) if(adj[v].size()==9){assert(hub==-1);hub=v;}
        assert(hub>=0);
        int triangleEdges=0;
        for(int v:comp)if(v!=hub){
            int peripheral=0;
            for(int w:adj[v]) if(w!=hub){assert(component[w]==component[v]);peripheral++;}
            assert(peripheral==2);
            triangleEdges+=peripheral;
            // If the two neighbors of v are adjacent, the induced 2-factor is triangles.
            vector<int> others;
            for(int w:adj[v]) if(w!=hub) others.push_back(w);
            assert(find(adj[others[0]].begin(),adj[others[0]].end(),others[1])!=adj[others[0]].end());
        }
        assert(triangleEdges==18);
        for(int start:comp){
            vector<int> dist(20,-1);dist[start]=0;queue<int> q;q.push(start);
            while(!q.empty()){
                int v=q.front();q.pop();
                for(int w:adj[v])if(dist[w]<0){dist[w]=dist[v]+1;q.push(w);}
            }
            for(int v:comp) assert(dist[v]>=0 && dist[v]<=(start==hub?1:2));
        }
    }
    cout<<"PASS: 20 unlabelled proper 3-edge-colourings, 36 switch adjacencies\n";
    cout<<"PASS: two components, each the cone over three disjoint triangles\n";
    return 0;
}
