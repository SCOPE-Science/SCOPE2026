// Independent exact verification on the folded 4-cube presentation.
// Vertex labels are four-bit words; generator differences are 1,2,4,8,15.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra verify_folded4.cpp -o verify_folded4
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

static const int moves[5]={1,2,4,8,15};
array<unsigned,16> adj;

bool good(unsigned m){
    unsigned seen[16]={0}; int n=0;
    for(int v=0;v<16;v++) if(!(m&(1u<<v))){
        unsigned s=adj[v]&m;
        if(!s)return false;
        for(int j=0;j<n;j++) if(seen[j]==s) return false;
        seen[n++]=s;
    }
    return true;
}

int kind(unsigned m){
    // 0 independent, 1 exactly one edge, 2 a 4-star, 3 all others
    int degrees[5], n=0, links=0;
    for(int v=0;v<16;v++) if(m&(1u<<v)){
        int d=__builtin_popcount(adj[v]&m);
        degrees[n++]=d;
        links+=d;
    }
    if(n!=5)return 3;
    sort(degrees,degrees+5);
    if(links==0)return 0;
    if(links==2 && degrees[0]==0 && degrees[1]==0 && degrees[2]==0 && degrees[3]==1 && degrees[4]==1)return 1;
    if(links==8 && degrees[0]==1 && degrees[1]==1 && degrees[2]==1 && degrees[3]==1 && degrees[4]==4)return 2;
    return 3;
}

struct Result{int edges, components, radius, diameter;map<int,int> ecc;array<int,3> degree;map<pair<int,int>,int> links;};
Result solve(const vector<unsigned>& a, const vector<int>& types,bool slide){
    unordered_map<unsigned,int> index;
    for(int i=0;i<(int)a.size();i++) index[a[i]]=i;
    vector<vector<int>> g(a.size());
    int edges=0;
    map<pair<int,int>,int> links;
    for(int i=0;i<(int)a.size();i++){
        unsigned z=a[i];
        for(int old=0;old<16;old++)if(z&(1u<<old)){
            for(int fresh=0;fresh<16;fresh++)if(!(z&(1u<<fresh))){
                if(slide && !(adj[old]&(1u<<fresh)))continue;
                unsigned newmask=z^(1u<<old)^(1u<<fresh);
                auto it=index.find(newmask);
                if(it==index.end() || i>=it->second)continue;
                int j=it->second;
                g[i].push_back(j);g[j].push_back(i);edges++;
                links[minmax(types[i],types[j])]++;
            }
        }
    }
    vector<char> visited(a.size(),0);
    int cc=0, radius=999,diameter=0;
    map<int,int> ecc;
    for(int i=0;i<(int)a.size();i++){
        if(visited[i])continue;
        cc++;queue<int> q;q.push(i);visited[i]=1;
        vector<int> comp;
        while(!q.empty()){
            int u=q.front();q.pop();comp.push_back(u);
            for(int v:g[u])if(!visited[v]){visited[v]=1;q.push(v);}
        }
        assert(comp.size()==a.size());
        for(int v:comp){
            vector<int> distance(a.size(),-1);distance[v]=0;
            queue<int> bfs;bfs.push(v);int far=0;int seen=0;
            while(!bfs.empty()){
                int u=bfs.front();bfs.pop();seen++;
                far=max(far,distance[u]);
                for(int w:g[u])if(distance[w]<0){distance[w]=distance[u]+1;bfs.push(w);}
            }
            assert(seen==(int)comp.size());
            radius=min(radius,far);diameter=max(diameter,far);ecc[far]++;
        }
    }
    array<int,3> deg={-1,-1,-1};
    for(int i=0;i<(int)a.size();i++){
        int d=(int)g[i].size();int t=types[i];
        assert(t>=0 && t<3);
        if(deg[t]<0)deg[t]=d;
        else assert(deg[t]==d);
    }
    return {edges,cc,radius,diameter,ecc,deg,links};
}

int main(){
    for(int v=0;v<16;v++)for(int d:moves)adj[v]|=1u<<(v^d);
    for(int v=0;v<16;v++) assert(__builtin_popcount(adj[v])==5);
    int lower=0;
    vector<unsigned> optimal;
    array<int,4> shapes={0,0,0,0};
    for(unsigned m=0;m<(1u<<16);m++){
        int k=__builtin_popcount(m);
        if(k<5 && good(m))lower++;
        if(k!=5)continue;
        int t=kind(m);
        shapes[t]++;
        bool is_good=good(m);
        assert(is_good==(t!=3));
        if(is_good)optimal.push_back(m);
    }
    assert(lower==0);
    assert(shapes[0]==16 && shapes[1]==320 && shapes[2]==80 && shapes[3]==3952);
    assert(optimal.size()==416);
    vector<int> types;
    for(unsigned m:optimal)types.push_back(kind(m));
    Result jump=solve(optimal,types,false);
    Result slide=solve(optimal,types,true);
    assert(jump.edges==2960 && slide.edges==1360);
    assert(jump.components==1 && slide.components==1);
    assert(jump.radius==5 && jump.diameter==6);
    assert(slide.radius==6 && slide.diameter==7);
    auto show=[](const Result& r){
        cout<<"edges="<<r.edges<<" components="<<r.components<<" radius="<<r.radius<<" diameter="<<r.diameter;
        cout<<" degrees(I,E,S)="<<r.degree[0]<<","<<r.degree[1]<<","<<r.degree[2]<<" ecc=";
        for(auto [k,n]:r.ecc)cout<<k<<":"<<n<<",";
        cout<<" connections=";
        for(auto [p,n]:r.links)cout<<p.first<<"-"<<p.second<<":"<<n<<",";
        cout<<"\n";
    };
    cout<<"graph=folded4 vertices=16 degree=5 min=5 count="<<optimal.size()<<" all_five=4368";
    cout<<" induced(I,E,S,other)="<<shapes[0]<<","<<shapes[1]<<","<<shapes[2]<<","<<shapes[3]<<"\n";
    cout<<"jump ";show(jump);
    cout<<"slide ";show(slide);
}
