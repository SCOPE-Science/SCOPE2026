// Independent finite enumeration: affine lines are cosets of five binary 2-spaces.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
int multiply(int a,int b) {
    int c=0;
    for(int i=0;i<2;i++) for(int j=0;j<2;j++)
        if((a>>i&1)&&(b>>j&1))c^=1<<(i+j);
    if(c&4)c^=7;
    return c;
}
int main(){
    // A point is encoded as x+4*y, unlike the verification in Python.
    vector<int> directions;
    directions.push_back((1<<0)|(1<<1)|(1<<2)|(1<<3)); // horizontal offsets x
    for(int m=0;m<4;m++){
        int vec=0;
        for(int t=0;t<4;t++) vec |=1<<(t+4*multiply(m,t));
        directions.push_back(vec);
    }
    // The first direction already equals slope zero; replace duplicate by vertical.
    directions[0]=(1<<0)|(1<<4)|(1<<8)|(1<<12);
    set<int> seen;
    vector<int> lines;
    for(int dir:directions) {
        set<int> cosets;
        for(int base=0;base<16;base++){
            int x=base%4,y=base/4;
            int line=0;
            for(int t=0;t<16;t++) if(dir>>t&1) {
                int u=t%4,v=t/4;
                line |= 1<<((x^u)+4*(y^v));
            }
            cosets.insert(line);
        }
        assert(cosets.size()==4);
        for(int l:cosets){assert(__builtin_popcount((unsigned)l)==4);seen.insert(l);lines.push_back(l);}
    }
    assert(lines.size()==20 && seen.size()==20);
    vector<int> states;
    map<int,int> dirOf;
    for(int bits=0;bits<(1<<16);bits++){
        bool ok=true;
        for(int l:lines) if((bits&l)==0 || (bits&l)==l){ok=false;break;}
        if(!ok)continue;
        states.push_back(bits);
        assert(__builtin_popcount((unsigned)bits)==8);
        int nd=0;
        for(int d=0;d<5;d++) {
            bool balanced=true;
            for(int j=0;j<4;j++)if(__builtin_popcount((unsigned)(bits&lines[4*d+j]))!=2)balanced=false;
            if(balanced){dirOf[bits]=d;nd++;}
        }
        assert(nd==1);
    }
    assert(states.size()==120);
    array<int,5> counts={};
    for(int b:states)counts[dirOf.at(b)]++;
    for(int n:counts)assert(n==24);
    vector<vector<int>> adj(120);
    map<pair<int,int>,int> pairs;
    for(int i=0;i<120;i++)for(int j=i+1;j<120;j++){
        int h=__builtin_popcount((unsigned)(states[i]^states[j]));
        pairs[{dirOf[states[i]]==dirOf[states[j]],h}]++;
        if(h==6){adj[i].push_back(j);adj[j].push_back(i);}
    }
    assert(pairs[make_pair(1,8)]==1320 && pairs[make_pair(1,16)]==60);
    assert(pairs[make_pair(0,6)]==2880 && pairs[make_pair(0,10)]==2880);
    map<pair<int,int>,int> metric;int edges=0;
    for(int i=0;i<120;i++){
        assert(adj[i].size()==48);edges+=adj[i].size();
        vector<int> dist(120,-1);queue<int> q;
        dist[i]=0;q.push(i);
        while(!q.empty()){
            int v=q.front();q.pop();
            for(int w:adj[v])if(dist[w]<0){dist[w]=dist[v]+1;q.push(w);}
        }
        array<int,4> shells={};
        for(int j=0;j<120;j++){
            assert(dist[j]>=0 && dist[j]<=3);shells[dist[j]]++;
            metric[{__builtin_popcount((unsigned)(states[i]^states[j])),dist[j]}]++;
            if(dist[j]==3)assert((states[i]^states[j])==0xffff);
        }
        assert(shells[0]==1 && shells[1]==48 && shells[2]==70 && shells[3]==1);
    }
    assert(edges==5760 && metric[make_pair(8,2)]==2640);
    assert(metric[make_pair(10,2)]==5760 && metric[make_pair(16,3)]==120);
    // Exact-eight flips have no cross-direction edges and have all
    // within-direction edges except identity and color complement.
    for(int i=0;i<120;i++){
        int n=0;
        for(int j=0;j<120;j++)if(__builtin_popcount((unsigned)(states[i]^states[j]))==8){
            assert(dirOf[states[i]]==dirOf[states[j]]);n++;
        }
        assert(n==22);
    }
    cout<<"SUCCESS: independent coset model gives 120 states, 2880 six-flip edges, diameter 3, and five 24-state eight-flip components.\n";
}
