// Independent path-tracing 4096-state census using the Duerer LCF graph.
// No external libraries; binary states stored as unsigned bitmasks.
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
constexpr int N=12, SIZE=1<<N;
using Adj=array<set<int>,N>;

Adj make_graph(){
    constexpr int shift[N]={-4,5,2,-4,-2,5,-5,2,4,-2,-5,4};
    Adj a;
    auto add=[&](int i,int j){assert(i!=j);a[i].insert(j);a[j].insert(i);};
    for(int i=0;i<N;++i){add(i,(i+1)%N);add(i,(i+shift[i]+N)%N);}
    int e=0;for(const auto& ns:a){assert(ns.size()==3);e+=(int)ns.size();}
    assert(e/2==18);
    return a;
}
int update(int x,const Adj& a){
    int y=0;
    for(int i=0;i<N;++i){int count=0;for(int j:a[i])count+=(x>>j)&1;
        if(count>=2)y|=(1<<i);}
    return y;
}
struct Outcome{int representative=-1;int entry=-1;int period=-1;};
int main(){
    Adj a=make_graph();
    vector<int> successor(SIZE);
    for(int x=0;x<SIZE;++x)successor[x]=update(x,a);
    vector<Outcome> out(SIZE);
    map<pair<int,int>,int> cycles; // (canonical state,temporal period)->orbit count
    for(int start=0;start<SIZE;++start){
        if(out[start].entry>=0)continue;
        vector<int> trail;vector<int> position(SIZE,-1);
        int x=start;
        while(position[x]<0 && out[x].entry<0){position[x]=trail.size();trail.push_back(x);x=successor[x];}
        if(position[x]>=0){
            int pos=position[x],per=(int)trail.size()-pos;
            assert(per==1 || per==2);
            int repr=*min_element(trail.begin()+pos,trail.end());
            ++cycles[{repr,per}];
            for(int k=pos;k<(int)trail.size();++k)out[trail[k]]={repr,0,per};
        }
        for(int k=(int)trail.size()-1;k>=0;--k){
            int y=trail[k];
            if(out[y].entry>=0)continue;
            Outcome q=out[successor[y]];
            assert(q.entry>=0);
            out[y]={q.representative,q.entry+1,q.period};
        }
    }
    map<int,int> basin,first;map<pair<int,int>,int> by_period,basin_spectrum;
    for(auto o:out){assert(o.entry>=0 && o.entry<=5 && (o.period==1 || o.period==2));
        ++basin[o.representative];++first[o.entry];++by_period[{o.period,o.entry}];}
    map<int,int> fix_basin,twoc_basin;
    int f=0,t=0;
    for(auto [pr,count]:cycles){assert(count==1);int b=basin.at(pr.first);
        if(pr.second==1){++f;++fix_basin[b];}else{++t;++twoc_basin[b];}}
    assert(f==14 && t==184);
    assert((first==map<int,int>{{0,382},{1,1278},{2,1140},{3,768},{4,432},{5,96}}));
    assert((fix_basin==map<int,int>{{1,2},{8,6},{13,4},{736,2}}));
    assert((twoc_basin==map<int,int>{{2,42},{4,24},{6,27},{10,24},{12,12},{14,12},{16,3},{21,24},{26,2},{70,12},{92,2}}));
    assert((by_period[{1,0}]==14 && by_period[{1,1}]==192 && by_period[{1,2}]==360 && by_period[{1,3}]==528 && by_period[{1,4}]==384 && by_period[{1,5}]==96));
    assert((by_period[{2,0}]==368 && by_period[{2,1}]==1086 && by_period[{2,2}]==780 && by_period[{2,3}]==240 && by_period[{2,4}]==48));
    assert(basin.at(0)==736 && basin.at(SIZE-1)==736);
    int states=0;for(auto [x,n]:basin)states+=n;assert(states==SIZE);
    // An explicit relabelling from this LCF representation to GP(6,2),
    // independently verifies that the two graph encodings name the same graph.
    const array<int,N> p={0,1,7,11,9,3,2,8,6,10,4,5};
    Adj gp;
    auto add=[&](int i,int j){gp[i].insert(j);gp[j].insert(i);};
    for(int i=0;i<6;++i){add(i,(i+1)%6);add(i,6+i);add(6+i,6+(i+2)%6);}
    set<int> perm(p.begin(),p.end());assert(perm.size()==N);
    for(int i=0;i<N;++i){set<int> s;for(int j:a[i])s.insert(p[j]);assert(s==gp[p[i]]);}
    cout<<"GRAPH=LCF(DUERER)=GP(6,2) V=12 E=18 STATES=4096\n";
    cout<<"CYCLES fixed="<<f<<" two="<<t<<"\n";
    cout<<"ENTRY";for(auto [d,num]:first)cout<<" "<<d<<":"<<num;cout<<"\n";
    cout<<"ENTRY_BY_PERIOD";for(auto [key,num]:by_period)cout<<" "<<key.first<<"/"<<key.second<<":"<<num;cout<<"\n";
    cout<<"BASINS_FIXED";for(auto [b,num]:fix_basin)cout<<" "<<b<<":"<<num;cout<<"\n";
    cout<<"BASINS_TWO";for(auto [b,num]:twoc_basin)cout<<" "<<b<<":"<<num;cout<<"\n";
    cout<<"CONSENSUS_BASINS "<<basin.at(0)<<" "<<basin.at(SIZE-1)<<"\n";
    cout<<"ALL CHECKS PASSED\n";
}
