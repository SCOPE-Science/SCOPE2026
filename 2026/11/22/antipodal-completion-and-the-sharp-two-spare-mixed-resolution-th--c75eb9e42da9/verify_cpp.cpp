// Independent finite certificate: witness hypergraph of mixed element pairs.
// Compile with: g++ -std=c++17 -O2 verify_cpp.cpp -o verify_cpp
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
int main() {
    constexpr int n=12, INF=99;
    int d[n][n];
    for(int i=0;i<n;i++)for(int j=0;j<n;j++) d[i][j]=(i==j?0:INF);
    auto add=[&](int u,int v){d[u][v]=d[v][u]=1;};
    for(int i=0;i<5;i++) {
        int a=2+i,b=7+i;
        add(0,a);add(1,b);add(a,2+(i+1)%5);
        add(b,7+(i+1)%5);add(a,b);add(a,7+(i+4)%5);
    }
    vector<pair<int,int>> ed;
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(d[i][j]==1)ed.push_back({i,j});
    assert(ed.size()==30);
    for(int k=0;k<n;k++)for(int i=0;i<n;i++)for(int j=0;j<n;j++)
        d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
    // Landmark table: columns are 12 vertices and 30 edges.
    int r[n][42];
    for(int w=0;w<n;w++) {
        for(int i=0;i<n;i++)r[w][i]=d[w][i];
        for(int i=0;i<30;i++)r[w][n+i]=min(d[w][ed[i].first],d[w][ed[i].second]);
    }
    // A subset resolves all items iff it intersects the witness mask
    // for each of the 861 unordered pairs of graph elements.
    vector<int> witnesses;
    for(int a=0;a<42;a++)for(int b=a+1;b<42;b++){
        int mask=0;
        for(int w=0;w<n;w++)if(r[w][a]!=r[w][b])mask|=(1<<w);
        assert(mask!=0);
        witnesses.push_back(mask);
    }
    assert(witnesses.size()==861);
    array<bool,4096> good{};map<int,int> count, minimal;
    for(int s=0;s<4096;s++){
        bool ok=true;
        for(int m:witnesses)if(!(s&m)){ok=false;break;}
        if(ok){good[s]=true;count[__builtin_popcount((unsigned)s)]++;}
    }
    assert((count==map<int,int>{{6,20},{7,240},{8,405},{9,220},{10,66},{11,12},{12,1}}));
    for(int s=0;s<4096;s++)if(good[s]){
        bool inclusion_minimal=true;
        for(int w=0;w<n;w++)if(s&(1<<w))if(good[s^(1<<w)])inclusion_minimal=false;
        if(inclusion_minimal)minimal[__builtin_popcount((unsigned)s)]++;
    }
    assert((minimal==map<int,int>{{6,20},{7,120}}));
    vector<pair<int,int>> antipodes;
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(d[i][j]==3)antipodes.push_back({i,j});
    assert(antipodes.size()==6);
    set<int> expected;
    for(int i=0;i<6;i++)for(int j=i+1;j<6;j++)for(int k=j+1;k<6;k++){
        int s=0;
        for(int t:{i,j,k}){
            s|=1<<antipodes[t].first;
            s|=1<<antipodes[t].second;
        }
        expected.insert(s);
    }
    int matched=0;
    for(int s=0;s<4096;s++)if(good[s] && __builtin_popcount((unsigned)s)==6){
        assert(expected.count(s));matched++;
    }
    assert(matched==20 && expected.size()==20);
    int shape_cycle=0,shape_triangles=0;
    for(int s:expected){
        int degree[n]={}; int tri=0;
        for(int i=0;i<n;i++)if(s&(1<<i)){
            for(int j=0;j<n;j++)if((s&(1<<j)) && d[i][j]==1)degree[i]++;
            assert(degree[i]==2);
        }
        for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int k=j+1;k<n;k++)
            if((s&(1<<i))&&(s&(1<<j))&&(s&(1<<k))&&
                d[i][j]==1&&d[i][k]==1&&d[j][k]==1)tri++;
        assert(tri==0 || tri==2);
        if(tri==0)shape_cycle++; else shape_triangles++;
    }
    assert(shape_cycle==10 && shape_triangles==10);
    // Independently reconstruct addition/deletion configuration graphs.
    const int expected_components[]={20,140,1};
    const int expected_nodes[]={20,260,665};
    for(int budget=6;budget<=8;budget++){
        array<bool,4096> seen{};
        int comps=0,total=0,number_optimals=0;
        map<int,int> component_sizes;
        for(int i=0;i<4096;i++){
            if(!good[i] || __builtin_popcount((unsigned)i)>budget || seen[i])continue;
            comps++;int size=0,n_opt=0;
            queue<int> Q;Q.push(i);seen[i]=true;
            while(!Q.empty()){
                int state=Q.front();Q.pop();size++;
                if(__builtin_popcount((unsigned)state)==6)n_opt++;
                for(int v=0;v<n;v++){
                    int next=state^(1<<v);
                    if(good[next]&&!seen[next]&&__builtin_popcount((unsigned)next)<=budget){
                        seen[next]=true;Q.push(next);
                    }
                }
            }
            component_sizes[size]++;total+=size;number_optimals+=n_opt;
        }
        assert(comps==expected_components[budget-6]);
        assert(total==expected_nodes[budget-6] && number_optimals==20);
        if(budget==7)assert((component_sizes==map<int,int>{{1,120},{7,20}}));
        if(budget==8)assert((component_sizes==map<int,int>{{665,1}}));
    }
    cout<<"ICOSAHEDRAL_MIXED_WITNESS_VERIFY_OK\n";
    cout<<"all 20 240 405 220 66 12 1\n";
    cout<<"minimal 20 120; min shapes C6=10 2K3=10; budgets components 20 140 1\n";
}
