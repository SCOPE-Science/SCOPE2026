// Independent finite census for optimal-domination membership on the doily.
// Compile: c++ -std=c++17 -O2 crosscheck_gq2.cpp -o crosscheck_gq2
// Run: ./crosscheck_gq2
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;
using U=uint64_t;
struct Bits {U a,b;};
Bits yes[30];
long long faces[6]={},quad_types[5]={};
int subset[5];
bool symp(int a,int b){return (__builtin_popcount((a&1 && b&4)?1:0) + (bool(a&4)&&bool(b&1)) + (bool(a&2)&&bool(b&8)) + (bool(a&8)&&bool(b&2)))%2;}
void descend(int start,int k,const vector<Bits>&parts){
    ++faces[k];
    if(k==4){int npoints=0;for(int i=0;i<4;i++)npoints+=subset[i]<15;++quad_types[npoints];}
    if(k==5)return;
    for(int v=start;v<30;v++){
        vector<Bits> next;bool ok=true;
        for(Bits b:parts){Bits t{b.a&yes[v].a,b.b&yes[v].b};Bits f{b.a&~yes[v].a,b.b&~yes[v].b};
            if(!(t.a||t.b)||!(f.a||f.b)){ok=false;break;}
            next.push_back(t);next.push_back(f);
        }
        if(ok){subset[k]=v;descend(v+1,k+1,next);}
    }
}
int main(){
    set<array<int,3>> line_set;
    for(int a=1;a<=15;a++)for(int b=a+1;b<=15;b++)if(!symp(a,b)){
        array<int,3> line{a,b,a^b};sort(line.begin(),line.end());line_set.insert(line);
    }
    assert(line_set.size()==15);
    vector<array<int,3>> lines(line_set.begin(),line_set.end());
    vector<vector<int>> adj(30);
    for(int j=0;j<15;j++)for(int p:lines[j]){adj[p-1].push_back(j+15);adj[j+15].push_back(p-1);}
    for(auto&nbrs:adj)assert(nbrs.size()==3);
    set<vector<int>> ds;
    for(int p=0;p<15;p++)for(int ell:adj[p]){
        set<int> forbidden{p,ell};
        for(int v:adj[p])forbidden.insert(v);
        for(int v:adj[ell])forbidden.insert(v);
        set<int> dist2;
        for(int u:{p,ell})for(int v:adj[u])for(int w:adj[v])if(!forbidden.count(w))dist2.insert(w);
        assert(dist2.size()==8);
        for(int pole:{p,ell}){vector<int> D(dist2.begin(),dist2.end());D.push_back(pole);sort(D.begin(),D.end());assert(D.size()==9);
            for(int w=0;w<30;w++){bool covered=binary_search(D.begin(),D.end(),w);for(int v:adj[w])covered|=binary_search(D.begin(),D.end(),v);assert(covered);}
            ds.insert(D);
        }
    }
    assert(ds.size()==90);int id=0;int degree[30]={};
    for(const auto&D:ds){for(int v:D){degree[v]++;if(id<64)yes[v].a|=U(1)<<id;else yes[v].b|=U(1)<<(id-64);}id++;}
    for(int d:degree)assert(d==27);
    vector<Bits> init{{~U(0),(U(1)<<26)-1}};
    descend(0,0,init);
    const long long expected[6]={1,30,390,2730,420,0};
    for(int k=0;k<6;k++){cout<<"faces["<<k<<"]="<<faces[k]<<"\n";assert(faces[k]==expected[k]);}
    cout<<"quadruples by point-count:";for(int k=0;k<5;k++)cout<<" "<<k<<":"<<quad_types[k];cout<<"\n";
    assert(quad_types[1]==120&&quad_types[2]==180&&quad_types[3]==120&&quad_types[0]==0&&quad_types[4]==0);
    cout<<"90_DOMINATING_SETS_30_VERTICES_ALL_CENSUS_CHECKS_PASS\n";
}
