// Exhaustive finite-state certificate for Conway Life B3/S23 on a 4-by-5 torus.
// Build: g++ -std=c++17 -O2 verify_paths.cpp -o verify_paths
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
constexpr int H=4,W=5,N=H*W,LIMIT=1<<N;

int main() {
    array<int,N> mask{};
    for(int y=0;y<H;y++)for(int x=0;x<W;x++)
        for(int dy=-1;dy<=1;dy++)for(int dx=-1;dx<=1;dx++)if(dx||dy)
            mask[y*W+x]|=1<<(((y+dy+H)%H)*W+(x+dx+W)%W);
    for(auto m:mask)assert(__builtin_popcount((unsigned)m)==8);
    vector<int> next(LIMIT),visit(LIMIT,-1),depth(LIMIT,-1),orbit(LIMIT,-1);
    for(int s=0;s<LIMIT;s++) {
        int out=0;
        for(int j=0;j<N;j++) {
            int k=__builtin_popcount((unsigned)(s&mask[j]));
            if(k==3||(k==2&&(s&(1<<j))))out|=1<<j;
        }
        next[s]=out;
    }
    vector<vector<int>> cycles;
    vector<int> period,basin;
    map<int,long long> entry_hist,basin_hist;
    vector<int> path;
    for(int seed=0;seed<LIMIT;seed++) {
        if(depth[seed]>=0)continue;
        path.clear();
        int v=seed;
        while(depth[v]<0&&visit[v]<0) {
            visit[v]=int(path.size());path.push_back(v);v=next[v];
        }
        if(visit[v]>=0) {
            int start=visit[v],id=int(cycles.size());
            cycles.emplace_back(path.begin()+start,path.end());
            period.push_back(int(path.size())-start);basin.push_back(0);
            for(int j=start;j<int(path.size());j++) {
                int x=path[j];orbit[x]=id;depth[x]=0;
            }
        }
        for(int j=int(path.size())-1;j>=0;j--) {
            int x=path[j];
            if(depth[x]<0) {depth[x]=depth[next[x]]+1;orbit[x]=orbit[next[x]];}
            ++basin[orbit[x]];++entry_hist[depth[x]];
        }
        for(int x:path)visit[x]=-1;
    }
    map<int,int> cycle_hist;
    for(int p:period)cycle_hist[p]++;
    for(int id=0;id<int(cycles.size());id++)basin_hist[period[id]]+=basin[id];

    // The rectangular torus has 4*5 translations, two independent reversals:
    // 80 distinct graph automorphisms. Its unequal sides forbid swapping axes.
    set<array<int,N>> group;
    for(int sy:{-1,1})for(int sx:{-1,1})for(int ty=0;ty<H;ty++)for(int tx=0;tx<W;tx++) {
        array<int,N> perm{};
        for(int y=0;y<H;y++)for(int x=0;x<W;x++)
            perm[y*W+x]=((sy*y+ty+H)%H)*W+((sx*x+tx+W)%W);
        group.insert(perm);
    }
    assert(group.size()==80);
    map<int,map<int,int>> geometry;
    set<int> seen;
    for(int id=0;id<int(cycles.size());id++)if(!seen.count(id)) {
        set<int> image_orbits;
        for(const auto &perm:group) {
            int representative=cycles[id][0],z=0;
            for(int j=0;j<N;j++)if(representative&(1<<j))z|=1<<perm[j];
            assert(depth[z]==0);image_orbits.insert(orbit[z]);
        }
        for(int k:image_orbits) {assert(period[k]==period[id]);seen.insert(k);}
        geometry[period[id]][int(image_orbits.size())]++;
    }
    long long totalentry=0,totalbasin=0;for(auto [d,n]:entry_hist)totalentry+=n;
    for(auto [p,n]:basin_hist)totalbasin+=n;
    assert(totalentry==LIMIT&&totalbasin==LIMIT);
    cout<<"cycle counts:";for(auto [p,n]:cycle_hist)cout<<" "<<p<<":"<<n;
    cout<<"\nentry:";for(auto [t,n]:entry_hist)cout<<" "<<t<<":"<<n;
    cout<<"\nbasins:";for(auto [p,n]:basin_hist)cout<<" "<<p<<":"<<n;
    cout<<"\nmax basin "<<*max_element(basin.begin(),basin.end())<<" cycles "<<cycles.size();
    cout<<"\ngeometry:";int nt=0;
    for(auto [p,by_size]:geometry) {
        cout<<" period="<<p<<"{";
        for(auto [size,count]:by_size) {cout<<size<<":"<<count<<",";nt+=count;}
        cout<<"}";
    }
    cout<<"\ntypes "<<nt<<"\n";
    int witness=-1;
    for(int x=0;x<LIMIT;x++)if(depth[x]==21){witness=x;break;}
    cout<<"empty basin "<<basin[orbit[0]]<<"; max transient witness "<<witness;
    cout<<"; period-5 witness ";for(int i=0;i<int(period.size());i++)if(period[i]==5){cout<<cycles[i][0];break;}
    cout<<"; period-10 witness ";for(int i=0;i<int(period.size());i++)if(period[i]==10){cout<<cycles[i][0];break;}
    cout<<"\n";
}
