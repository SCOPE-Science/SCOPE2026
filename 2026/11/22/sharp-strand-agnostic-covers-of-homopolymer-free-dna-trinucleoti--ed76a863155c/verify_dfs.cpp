// Independent exhaustive trail enumeration, using no cached dynamic-programming states.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
struct Edge {int end, orbit, ch;};
vector<Edge> outgoing[12];
vector<array<int,2>> vertices;
map<pair<int,int>,int> vertex_index;
long long nodes=0, full18=0, linear19=0, cyclic20=0;
string linear_witness, cyclic_witness;
constexpr int full=(1<<18)-1;

void explore(int cur,int start,int visited,int extra_ata,int extra_cgc,int length,string &word) {
    ++nodes;
    if(length==18 && visited==full) ++full18;
    if(length==19 && visited==full && extra_ata+extra_cgc==1) {
        ++linear19;
        if(linear_witness.empty()) linear_witness=word;
    }
    if(length==20) {
        if(visited==full && extra_ata==1 && extra_cgc==1 && cur==start) {
            ++cyclic20;
            if(cyclic_witness.empty()) cyclic_witness=word;
        }
        return;
    }
    for(const Edge &e:outgoing[cur]) {
        bool used=visited & (1<<e.orbit);
        if(used && e.orbit!=5 && e.orbit!=11) continue;
        if(used && e.orbit==5 && extra_ata==1) continue;
        if(used && e.orbit==11 && extra_cgc==1) continue;
        int n_ata=extra_ata+(used && e.orbit==5);
        int n_cgc=extra_cgc+(used && e.orbit==11);
        word.push_back("ACGT"[e.ch]);
        explore(e.end,start,visited|(1<<e.orbit),n_ata,n_cgc,length+1,word);
        word.pop_back();
    }
}
int main() {
    auto rc=[](array<int,3> x){return array<int,3>{3-x[2],3-x[1],3-x[0]};};
    for(int a=0;a<4;++a)for(int b=0;b<4;++b)if(a!=b){
        vertex_index[{a,b}]=vertices.size(); vertices.push_back({a,b});
    }
    map<array<int,3>,int> orbit;
    for(int a=0;a<4;++a)for(int b=0;b<4;++b)for(int c=0;c<4;++c)if(a!=b&&b!=c){
        array<int,3> triple={a,b,c}; orbit[min(triple,rc(triple))]=0;
    }
    assert(orbit.size()==18);
    int k=0; for(auto &kv:orbit) kv.second=k++;
    assert(orbit.at({0,3,0})==5 && orbit.at({1,2,1})==11);
    for(int a=0;a<4;++a)for(int b=0;b<4;++b)for(int c=0;c<4;++c)if(a!=b&&b!=c){
        array<int,3> triple={a,b,c};
        outgoing[vertex_index.at({a,b})].push_back({vertex_index.at({b,c}),orbit.at(min(triple,rc(triple))),c});
    }
    for(int s=0;s<12;++s){
        string word; word.push_back("ACGT"[vertices[s][0]]);word.push_back("ACGT"[vertices[s][1]]);
        explore(s,s,0,0,0,0,word);
    }
    assert(full18==0 && linear19==57984 && cyclic20==289920);
    assert(cyclic20%20==0 && cyclic20/20==14496);
    cout<<"DFS_VERIFY_OK no_exact_18="<<full18<<" linear19="<<linear19
        <<" cyclic20_rooted="<<cyclic20<<" circular_necklaces="<<cyclic20/20<<"\n";
    cout<<"examples "<<linear_witness<<" "<<cyclic_witness<<"\n";
}
