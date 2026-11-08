// Independent enumeration via disjoint permutation perfect matchings.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra verify_switch_5x5.cpp -o verify_switch_5x5
#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <vector>
using namespace std;
using Rows = array<int,5>;

int main() {
    set<Rows> forms;
    array<int,5> p={0,1,2,3,4};
    do {
        array<int,5> q={0,1,2,3,4};
        do {
            bool disjoint=true;
            for(int r=0;r<5;r++)if(p[r]==q[r])disjoint=false;
            if(disjoint){
                Rows x{};
                for(int r=0;r<5;r++)x[r]=(1<<p[r])|(1<<q[r]);
                forms.insert(x);
            }
        } while(next_permutation(q.begin(),q.end()));
    } while(next_permutation(p.begin(),p.end()));
    vector<Rows> states(forms.begin(),forms.end());
    assert(states.size()==2040);
    map<Rows,int> pos;
    for(int i=0;i<(int)states.size();i++)pos[states[i]]=i;
    vector<vector<int>> adj(states.size());
    for(int i=0;i<(int)states.size();i++){
        const auto& a=states[i];
        for(int r=0;r<5;r++)for(int s=r+1;s<5;s++)
         for(int u=0;u<5;u++)for(int v=u+1;v<5;v++){
            int p=(a[r]>>u)&1,q=(a[r]>>v)&1,t=(a[s]>>u)&1,w=(a[s]>>v)&1;
            if((p&&!q&&!t&&w)||(!p&&q&&t&&!w)){
                auto b=a;
                b[r]^=(1<<u)|(1<<v);
                b[s]^=(1<<u)|(1<<v);
                adj[i].push_back(pos.at(b));
            }
         }
    }
    long long sumdeg=0;
    map<int,int> degrees;
    for(auto& a:adj){
        sort(a.begin(),a.end());
        assert(unique(a.begin(),a.end())==a.end());
        sumdeg+=a.size(); degrees[a.size()]++;
    }
    assert(sumdeg==52200);
    assert(degrees[25]==1440 && degrees[27]==600 && degrees.size()==2);
    for(int i=0;i<(int)states.size();i++)
      for(int j:adj[i])assert(binary_search(adj[j].begin(),adj[j].end(),i));

    Rows a={3,6,12,24,17};
    Rows b={3,3,12,20,24};
    assert(pos.count(a)&&pos.count(b));
    auto bfs=[&](Rows start, vector<int> expected){
        vector<int> d(states.size(),-1);
        queue<int> q;
        int s=pos.at(start);d[s]=0;q.push(s);
        while(!q.empty()){
            int u=q.front();q.pop();
            for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;q.push(v);}
        }
        assert(count(d.begin(),d.end(),-1)==0);
        vector<int> counts(expected.size());
        for(int x:d){assert(x>=0&&x<(int)expected.size());counts[x]++;}
        assert(counts==expected);
        return d;
    };
    vector<int> d1=bfs(a,{1,25,230,810,831,141,2});
    vector<int> d2=bfs(b,{1,27,242,840,810,120});
    Rows antipode2={12,24,17,3,6};
    Rows antipode3={24,17,3,6,12};
    assert(d1[pos.at(antipode2)]==6&&d1[pos.at(antipode3)]==6);
    assert(count(d1.begin(),d1.end(),6)==2);
    cout<<"CPP_SYMMETRY_PASS states=2040 edges=26100 canonical_distance_profiles_valid=true"<<endl;
    cout<<"CPP_ANTIPODES_PASS two_cyclic_shifts=true"<<endl;
}
