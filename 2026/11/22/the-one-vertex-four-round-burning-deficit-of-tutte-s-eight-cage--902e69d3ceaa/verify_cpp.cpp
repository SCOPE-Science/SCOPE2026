// Independent exact checker: C++17, no external dependencies.
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
using Edge=pair<int,int>;
using Matching=array<Edge,3>;
int main(){
    vector<Edge> E;
    for(int a=0;a<6;a++)for(int b=a+1;b<6;b++) E.push_back({a,b});
    map<Edge,int> ix;
    for(int k=0;k<15;k++)ix[E[k]]=k;
    vector<Matching> F;
    // Each syntheme has its lowest element paired with one of five choices.
    for(int b=1;b<6;b++){
        vector<int> rest;
        for(int u=1;u<6;u++)if(u!=b)rest.push_back(u);
        for(int j=1;j<4;j++){
            int p=rest[0],q=rest[j];
            vector<int> r;
            for(int u:rest)if(u!=p && u!=q)r.push_back(u);
            Matching M={Edge(0,b),Edge(p,q),Edge(r[0],r[1])};
            F.push_back(M);
        }
    }
    assert(F.size()==15);
    vector<vector<int>> g(30);
    for(int j=0;j<15;j++) for(Edge e:F[j]){
        int p=ix.at(e);g[p].push_back(15+j);g[15+j].push_back(p);
    }
    for(auto& x:g)assert(x.size()==3);
    vector<vector<int>> d(30,vector<int>(30,-1));
    for(int s=0;s<30;s++){
        queue<int> q;q.push(s);d[s][s]=0;
        while(!q.empty()){
            int u=q.front();q.pop();
            for(int v:g[u])if(d[s][v]<0){d[s][v]=d[s][u]+1;q.push(v);}
        }
        array<int,5> sh={};
        for(int t:d[s]){assert(t>=0 && t<=4);sh[t]++;}
        assert((sh==array<int,5>{1,3,6,12,8}));
    }
    uint32_t B[5][30]={};
    for(int r=0;r<=4;r++)for(int u=0;u<30;u++)for(int v=0;v<30;v++)if(d[u][v]<=r)B[r][u]|=1u<<v;
    constexpr uint32_t ALL=(1u<<30)-1;
    long long good=0, d2=0,d4=0;
    array<int,30> count_first={};
    array<array<int,30>,30> missing={};
    int mmax=0,invalid=0;
    for(int a=0;a<30;a++)for(int b=0;b<30;b++){
      uint32_t x=B[3][a]|B[2][b];
      for(int c=0;c<30;c++){
        uint32_t y=x|B[1][c];
        for(int e=0;e<30;e++){
            uint32_t z=y|(1u<<e);
            int n=__builtin_popcount(z);mmax=max(mmax,n);
            if(n==29){
                int w=__builtin_ctz(ALL^z);
                ++good;++count_first[a];++missing[a][w];
                if(d[a][b]==2)d2++;
                else if(d[a][b]==4)d4++;
                else assert(false);
                if(!(d[a][b]>=1 && d[a][c]>=2 && d[a][e]>=3 &&
                     d[b][c]>=1 && d[b][e]>=2 && d[c][e]>=1))++invalid;
            }
        }
      }
    }
    assert(mmax==29 && good==2160 && d2==720 && d4==1440 && invalid==0);
    for(int a=0;a<30;a++){
      assert(count_first[a]==72);
      for(int w=0;w<30;w++)assert(missing[a][w]==(d[a][w]==4?9:0));
    }
    cout<<"CHECKER_CPP_OK\n";
    cout<<"vertices=30 edges=45 diameter=4\n";
    cout<<"maximum_four_round_coverage="<<mmax<<"\n";
    cout<<"four_round_schedules_29="<<good<<"\n";
    cout<<"by_second_distance=2:"<<d2<<",4:"<<d4<<"\n";
    cout<<"ordered_antipodal_source_survivor_pairs=240 per_pair=9\n";
    cout<<"all_29_schedules_strict="<<(invalid==0?"true":"false")<<"\n";
}
