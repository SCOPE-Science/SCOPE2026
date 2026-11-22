// Finite-state certificate for majority voting on two nineteen-vertex tournaments.
// Compile: c++ -std=c++17 -O2 -Wall -Wextra verify_direct.cpp -o verify_direct
// Run: ./verify_direct
#include <array>
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
#include <cassert>
using namespace std;
constexpr int N=19, S=1<<N, FULL=S-1;

int update(int state, const vector<int>& offsets) {
    int next=0;
    for(int vertex=0;vertex<N;++vertex) {
        int yes=0;
        for(int offset:offsets) yes += (state >> ((vertex+offset)%N)) & 1;
        if(2*yes > (int)offsets.size()) next |= 1<<vertex;
    }
    return next;
}

vector<int> build(const vector<int>& offsets) {
    vector<int> succ(S);
    for(int state=0;state<S;++state) succ[state]=update(state,offsets);
    return succ;
}

int advance(int u, const vector<int>& succ, int steps) {
    for(int i=0;i<steps;++i)u=succ[u];
    return u;
}

int rotation(int state, int r) {
    r%=N;
    if(r==0)return state;
    return ((state << r) | (state >> (N-r))) & FULL;
}

void cyclic_case() {
    vector<int> offsets{1,2,3,4,5,6,7,8,9};
    const auto succ=build(offsets);
    map<pair<int,int>,long long> by_entry_period;
    map<int,long long> by_arc_length;
    long long by_consensus[2]={0,0};
    int longest=0, witness=-1;
    for(int initial=0; initial<S; ++initial) {
        int current=initial;
        int entry=-1;
        for(int t=0;t<=4;++t) {
            if(advance(current,succ,19)==current) {entry=t;break;}
            current=succ[current];
        }
        if(entry<0) {cerr<<"Not periodic at update four: "<<initial<<"\n";exit(1);}
        if(entry>longest) {longest=entry;witness=initial;}
        const int p=succ[current]==current?1:19;
        if(p==1) {
            if(current==0)by_consensus[0]++;
            else if(current==FULL)by_consensus[1]++;
            else {cerr<<"Nonunanimous fixed state\n";exit(1);}
        } else {
            int k=__builtin_popcount((unsigned)current);
            if(k<5||k>14){cerr<<"Wrong number of ones\n";exit(1);}
            bool arc=false;
            for(int t=0;t<N;t++) if(rotation((1<<k)-1,t)==current)arc=true;
            if(!arc){cerr<<"Not an arc: "<<current<<"\n";exit(1);}
            by_arc_length[k]++;
        }
        by_entry_period[{entry,p}]++;
    }
    assert(longest==4);
    assert(by_entry_period[make_pair(0,1)]==2);
    assert(by_entry_period[make_pair(0,19)]==190);
    assert(by_consensus[0]==137903 && by_consensus[1]==137903);
    const map<int,long long> expected{{5,13376},{6,18202},{7,24947},{8,34200},{9,33516},{10,33516},{11,34200},{12,24947},{13,18202},{14,13376}};
    assert(by_arc_length==expected);
    for(int k=5;k<=14;k++)for(int t=0;t<19;t++) {
        int a=rotation((1<<k)-1,t);
        assert(succ[a]==rotation(a,14)); // shift by -5
    }
    // Stronger global certificate, including sharpness.
    int failures_preceding=0;
    for(int initial=0;initial<S;initial++) {
       assert(advance(initial,succ,23)==advance(initial,succ,4));
       if(advance(initial,succ,22)!=advance(initial,succ,3)) ++failures_preceding;
    }
    assert(failures_preceding>0);
    cout<<"CYCLIC19 states "<<S<<" longest "<<longest<<" witness "<<witness
        <<" failed_F22_eq_F3 "<<failures_preceding<<"\n";
    for(const auto& [key,n]:by_entry_period)cout<<"CYCLIC19 entry="<<key.first<<" period="<<key.second<<" count="<<n<<"\n";
    for(const auto& [k,n]:by_arc_length)cout<<"CYCLIC19 arc_length="<<k<<" basin="<<n<<"\n";
    cout<<"CYCLIC19 consensus_basins "<<by_consensus[0]<<" "<<by_consensus[1]<<"\n";
}

void paley_case() {
    vector<int> offsets;
    for(int i=1;i<N;i++) {
        bool square=false;
        for(int j=1;j<N;j++)if(j*j%N==i)square=true;
        if(square)offsets.push_back(i);
    }
    assert(offsets.size()==9);
    const auto succ=build(offsets);
    long long fixed=0, four=0, nineteen=0, max_depth=0;
    map<int,long long> period_cycles;
    map<pair<int,int>,long long> entries;
    for(int initial=0; initial<S;initial++) {
        int current=initial,entry=-1;
        for(int t=0;t<=7;t++) {
            if(advance(current,succ,76)==current) {entry=t;break;}
            current=succ[current];
        }
        if(entry<0){cerr<<"Paley slow state: "<<initial<<"\n";exit(1);}
        max_depth=max(max_depth,(long long)entry);
        int p=0;
        for(int t: {1,4,19,76})if(advance(current,succ,t)==current){p=t;break;}
        if(p==1)fixed++;
        else if(p==4)four++;
        else if(p==19)nineteen++;
        else {cerr<<"Unexpected Paley orbit\n";exit(1);}
        entries[{entry,p}]++;
    }
    assert(fixed==516764 && four==6156 && nineteen==1368 && max_depth==7);
    assert(entries[make_pair(0,4)]==1368 && entries[make_pair(0,19)]==342);
    cout<<"PALEY19 states "<<S<<" fixed_attraction "<<fixed<<" period4_attraction "<<four
      <<" period19_attraction "<<nineteen<<" sharp_depth "<<max_depth<<"\n";
    cout<<"PALEY19 primitive_period4 "<<1368/4<<" primitive_period19 "<<342/19<<"\n";
}
int main(){cyclic_case();paley_case();return 0;}
