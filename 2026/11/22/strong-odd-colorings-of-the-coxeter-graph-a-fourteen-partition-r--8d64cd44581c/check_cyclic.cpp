// Exact finite enumeration of strong odd four-colourings of the Coxeter graph.
// Standard C++17; no external libraries. Vertex labels are described in RESULT.md.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
using namespace std;

static constexpr int N = 28, K = 4;
using Domains = array<uint8_t,N>;
using Four = array<int,4>;
array<array<int,3>,N> neighbor;
vector<Four> allowed;
uint64_t leaves=0, nodes=0;
set<string> partitions;
map<Four,int> small_counts;

Four small_class(const Domains& d) {
    array<int,K> count{};
    for (auto x:d) { assert(x && (x&(x-1))==0); count[__builtin_ctz(x)]++; }
    vector<int> sizes(count.begin(),count.end());sort(sizes.begin(),sizes.end());
    assert((sizes==vector<int>{4,8,8,8}));
    int c=-1;
    for(int i=0;i<K;i++) if(count[i]==4) c=i;
    assert(c>=0);
    Four a{};int j=0;
    for(int i=0;i<N;i++)if(d[i]==(1<<c))a[j++]=i;
    assert(j==4);
    return a;
}
string canonical(const Domains& d){
    int ren[K]={-1,-1,-1,-1}, next=0;
    string out;
    for(auto x:d){int old=__builtin_ctz(x);if(ren[old]<0)ren[old]=next++;
        out+=char('0'+ren[old]); }
    assert(next==4);
    return out;
}

bool propagate(Domains& d){
    bool changed=true;
    while(changed){
        changed=false;
        for(int v=0;v<N;v++){
            int verts[4]={v,neighbor[v][0],neighbor[v][1],neighbor[v][2]};
            uint8_t support[4]={};
            for(auto p:allowed){
                int j=0;
                for(;j<4;j++)if(!(d[verts[j]]&(1<<p[j])))break;
                if(j!=4)continue;
                for(j=0;j<4;j++)support[j]|=(1<<p[j]);
            }
            for(int j=0;j<4;j++){
                int x=verts[j];uint8_t nd=d[x]&support[j];
                if(!nd)return false;
                if(nd!=d[x]){d[x]=nd;changed=true;}
            }
        }
    }
    return true;
}
void enumerate(Domains d){
    ++nodes;
    if(!propagate(d))return;
    int v=-1, best=5;
    for(int i=0;i<N;i++){
        int count=__builtin_popcount((unsigned)d[i]);
        if(count>1 && count<best){best=count;v=i;}
    }
    if(v<0){
        ++leaves;
        Four S=small_class(d);
        small_counts[S]++;
        partitions.insert(canonical(d));
        // Direct postcondition for both properness and neighborhood parity.
        for(int i=0;i<N;i++){
            int c=__builtin_ctz((unsigned)d[i]);
            int counts[K]={};
            for(int j:neighbor[i]){
                int cc=__builtin_ctz((unsigned)d[j]);
                assert(cc!=c);++counts[cc];
            }
            for(int t:counts)assert(t==0 || t%2==1);
        }
        return;
    }
    for(int c=0;c<K;c++)if(d[v]&(1<<c)){
        Domains nd=d;nd[v]=1<<c;enumerate(nd);
    }
}
int main(){
    // Cyclic seven-claw model: central vertices 0..6, leaves 7+7*j+i.
    array<int,3> steps={1,2,4};
    array<int,N> deg{};
    for(int i=0;i<7;i++)for(int j=0;j<3;j++){
        int u=7+7*j+i, w=7+7*j+(i+steps[j])%7;
        int e[2][2]={{i,u},{u,w}};
        for(auto &p:e){int x=p[0],y=p[1];
            assert(deg[x]<3 && deg[y]<3);
            neighbor[x][deg[x]++]=y;neighbor[y][deg[y]++]=x;}
    }
    for(auto d:deg)assert(d==3);
    for(int c=0;c<K;c++){
        vector<int> other;
        for(int d=0;d<K;d++)if(d!=c)other.push_back(d);
        for(int d:other)allowed.push_back({c,d,d,d});
        do{allowed.push_back({c,other[0],other[1],other[2]});}
          while(next_permutation(other.begin(),other.end()));
    }
    assert(allowed.size()==36);
    Domains d;d.fill(15);d[0]=1; // Fix first colour name by global symmetry.
    enumerate(d);

    // Independent distance-four-clique census, directly from breadth-first search.
    array<array<int,N>,N> distance{};
    for(int s=0;s<N;s++){
        distance[s].fill(-1);distance[s][s]=0;
        queue<int> q;q.push(s);
        while(!q.empty()){
            int v=q.front();q.pop();
            for(int w:neighbor[v])if(distance[s][w]<0){
                distance[s][w]=distance[s][v]+1;q.push(w);}
        }
    }
    int maxdist=0;
    for(int a=0;a<N;a++)for(int b=0;b<N;b++){
        assert(distance[a][b]>=0);maxdist=max(maxdist,distance[a][b]);
    }
    assert(maxdist==4);
    set<Four> diametral;
    for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)
    for(int c=b+1;c<N;c++)for(int d=c+1;d<N;d++){
        int v[4]={a,b,c,d};bool ok=true;
        for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)
            if(distance[v[i]][v[j]]!=4)ok=false;
        if(ok)diametral.insert({a,b,c,d});
    }
    set<Four> formula;
    for(int i=0;i<7;i++){
        for(auto offsets: {array<int,3>{4,1,2},array<int,3>{3,6,5}}){
            Four a={i,7+(i+offsets[0])%7,
                14+(i+offsets[1])%7,21+(i+offsets[2])%7};
            sort(a.begin(),a.end());formula.insert(a);
        }
    }
    assert(diametral==formula);
    assert(small_counts.size()==14);
    for(auto p:formula)assert(small_counts[p]==6);
    assert(leaves==84);
    assert(partitions.size()==14);
    assert(nodes==544);
    cout<<"vertices=28 edges=42 cubic=1\n";
    cout<<"allowed_local_templates=36\n";
    cout<<"root_fixed_colours=84 search_nodes="<<nodes<<"\n";
    cout<<"named_four_colours="<<leaves*4<<" unlabeled_partitions="<<partitions.size()<<"\n";
    cout<<"all_class_sizes=4,8,8,8\n";
    cout<<"diametral_four_sets="<<diametral.size()<<" unique_small_class_extensions=1\n";
    cout<<"representative="<<*partitions.begin()<<"\n";
}
