// Finite, exhaustive space-time transfer graph for B3/S23 and B36/S23
// on periodic three-row Moore grids. Build: c++ -O3 -std=c++17 -o graph space_time_graph.cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

constexpr int K = 512, V = K*K;
int update_column(int left, int mid, int right, bool highlife) {
    int output = 0;
    for (int row=0; row<3; ++row) {
        int neighbours = 0;
        for (int dr=-1; dr<=1; ++dr) {
            int r = (row+dr+3)%3;
            neighbours += (left>>r)&1;
            neighbours += (right>>r)&1;
            if (dr != 0) neighbours += (mid>>r)&1;
        }
        bool alive = (mid>>row)&1;
        if ((alive && (neighbours==2 || neighbours==3)) ||
            (!alive && (neighbours==3 || (highlife && neighbours==6))))
            output |= 1<<row;
    }
    return output;
}
struct Stats { long long edges; int nontrivial_components, cyclic_vertices, varying_vertices; vector<int> sizes, cyc_ids; };
Stats calculate(bool highlife) {
    int allowed[8][8][8] = {};
    for (int a=0;a<8;a++) for (int b=0;b<8;b++) for (int c=0;c<8;c++)
        allowed[a][b][update_column(a,b,c,highlife)] |= 1<<c;
    vector<vector<int>> forward(V), backward(V);
    vector<unsigned char> self(V,0);
    long long edges=0;
    for (int A=0;A<K;A++) for (int B=0;B<K;B++) {
        array<int,3> masks;
        bool possible = true;
        for (int t=0;t<3;t++) {
            int a=(A>>(3*t))&7;
            int b=(B>>(3*t))&7;
            int b_next=(B>>(3*((t+1)%3)))&7;
            masks[t]=allowed[a][b][b_next];
            if (masks[t]==0) possible=false;
        }
        if (!possible) continue;
        for(int i=0;i<8;i++) if((masks[0]>>i)&1)
        for(int j=0;j<8;j++) if((masks[1]>>j)&1)
        for(int k=0;k<8;k++) if((masks[2]>>k)&1) {
            int C=i|(j<<3)|(k<<6);
            int u=A*K+B, v=B*K+C;
            forward[u].push_back(v);
            backward[v].push_back(u);
            self[u] |= (u==v);
            ++edges;
        }
    }
    // Iterative Kosaraju, visiting all vertices, including isolated ones.
    vector<unsigned char> visited(V,0);
    vector<int> order;
    order.reserve(V);
    for(int root=0;root<V;root++) if(!visited[root]) {
        vector<pair<int,int>> stack={{root,0}};
        visited[root]=1;
        while(!stack.empty()) {
            int u=stack.back().first;
            int &cursor=stack.back().second;
            if(cursor<(int)forward[u].size()) {
                int v=forward[u][cursor++];
                if(!visited[v]) { visited[v]=1; stack.push_back({v,0}); }
            } else { order.push_back(u); stack.pop_back(); }
        }
    }
    vector<int> comp(V,-1), sizes;
    for(int pos=V-1;pos>=0;--pos) {
        int root=order[pos];
        if(comp[root]>=0) continue;
        int id=(int)sizes.size(), count=0;
        vector<int> stack={root}; comp[root]=id;
        while(!stack.empty()) {
            int u=stack.back();stack.pop_back();++count;
            for(int v:backward[u]) if(comp[v]<0) {
                comp[v]=id;stack.push_back(v);
            }
        }
        sizes.push_back(count);
    }
    Stats s{edges,0,0,0,{},{}};
    for(int sz:sizes) if(sz>1) { s.sizes.push_back(sz);s.nontrivial_components++; }
    sort(s.sizes.begin(),s.sizes.end(),greater<int>());
    for(int u=0;u<V;u++) if(sizes[comp[u]]>1 || self[u]) {
        s.cyclic_vertices++;
        s.cyc_ids.push_back(u);
        int A=u/K, B=u%K;
        auto static_column=[](int X){return (X&7)==((X>>3)&7) && (X&7)==((X>>6)&7);};
        if(!static_column(A) || !static_column(B)) s.varying_vertices++;
    }
    return s;
}
int main() {
    Stats life=calculate(false), highlife=calculate(true);
    for(auto mode:{make_pair("Life",life),make_pair("HighLife",highlife)}) {
        const auto &s=mode.second;
        cout<<mode.first<<" vertices="<<V<<" edges="<<s.edges
            <<" nontrivial_SCC_sizes=";
        for(int size:s.sizes)cout<<size<<",";
        cout<<" cyclic_vertices="<<s.cyclic_vertices
            <<" time_varying_cyclic_vertices="<<s.varying_vertices<<"\n";
        assert(s.sizes==vector<int>({30,27}));
        assert(s.cyclic_vertices==57 && s.varying_vertices==0);
    }
    assert(life.edges==294072 && highlife.edges==321875);
    assert(life.cyc_ids==highlife.cyc_ids);
    cout<<"Equal recurrent vertex sets: yes\n";
}
