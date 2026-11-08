// Independent direct vertex-by-vertex graph majority evolution.
// Vertices 0..r-1 form the ordinary clique, r is the hub, r+1..r+s are leaves.
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;
using U = uint32_t;
U advance(U x,const vector<vector<int>>& nbr) {
    U y=0;
    for(int v=0;v<(int)nbr.size();++v) {
        int ones=0;for(int w:nbr[v]) ones+=(x>>w)&1;
        int bit=(x>>v)&1;
        if(2*ones>(int)nbr[v].size() || (2*ones==(int)nbr[v].size() && bit))y|=U(1)<<v;
    }
    return y;
}
unsigned long long choose(int n,int k){unsigned long long z=1;for(int i=1;i<=k;i++)z=z*(n-i+1)/i;return z;}
int main(){
    unsigned long long explored=0;int param=0;
    for(int r=2;r<=8;r++)for(int s=1;s<=r+2;s++) {
        int N=r+s+1;if(N>19)continue;
        vector<vector<int>> nbr(N);
        for(int i=0;i<=r;i++)for(int j=i+1;j<=r;j++){
            nbr[i].push_back(j);nbr[j].push_back(i);
        }
        for(int j=r+1;j<N;j++){nbr[r].push_back(j);nbr[j].push_back(r);}
        map<pair<int,int>,unsigned long long> census;
        for(U x=0;x<(U(1)<<N);x++){
            U a=advance(x,nbr), b=advance(a,nbr), c=advance(b,nbr), d=advance(c,nbr);
            U e=advance(d,nbr);
            assert(e==c); // universal eventual 2-periodicity by the third update
            pair<int,int> key;
            if(a==x)key={0,1};
            else if(b==x)key={0,2};
            else if(b==a)key={1,1};
            else if(c==a)key={1,2};
            else if(c==b)key={2,1};
            else if(d==c)key={3,1};
            else if(d==b)key={2,2};
            else {cerr<<"Unclassified state "<<x<<"\n";return 2;}
            census[key]++;
        }
        unsigned long long C=r%2?choose(r,(r-1)/2):0;
        unsigned long long a=0;for(int i=0;i<=(s-1)/2;i++)a+=choose(s,i);
        unsigned long long tie=((r+s)%2==0)?choose(r+s,(r+s)/2):0;
        unsigned long long pow=1ULL<<(r+s);
        if(s<=r) {
            unsigned long long fixed=2+(s>=r?2:0);
            unsigned long long cycles=C+(s>r?2:0);
            if(census[{0,1}]!=fixed || census[{0,2}]!=2*cycles){
                cerr<<"Recurrent mismatch r="<<r<<" s="<<s<<"\n";return 1;
            }
            explored+=U(1)<<N;param++;continue;
        }
        map<pair<int,int>,unsigned long long> expected={
            {{0,1},4},{{0,2},4+2*C},{{1,1},pow+tie-4-2*C*a},
            {{1,2},pow-tie-4-2*C},{{2,1},2*C*a}
        };
        for(const auto &[key,val]:expected)if(census[key]!=val){
            cerr<<"Mismatch r="<<r<<" s="<<s<<" at "<<key.first<<","<<key.second<<": "<<census[key]<<" vs "<<val<<"\n";return 1;
        }
        for(const auto &[key,val]:census)if(!expected.count(key)) {cerr<<"extra class\n";return 1;}
        explored+=U(1)<<N;param++;
    }
    cout<<"PASS: direct independent graph updates; "<<explored<<" labelled states over "<<param<<" parameter pairs.\n";
}
