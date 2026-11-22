// Independent exhaustive checker: array-based propagation and breadth-first search.
#include <algorithm>
#include <array>
#include <cstdio>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
constexpr int n=19;
array<array<int,n>,n> edge{};
vector<int> masks;
map<int,int> time_by_mask;

int finish_time(int mask){
    array<char,n> viewed{};
    for(int v=0;v<n;v++) if(mask&(1<<v)) {
        viewed[v]=1;
        for(int u=0;u<n;u++) if(edge[v][u]) viewed[u]=1;
    }
    int rounds=1;
    while(true){
        bool all=true;
        for(int v=0;v<n;v++) if(!viewed[v])all=false;
        if(all)return rounds;
        auto next=viewed;
        for(int v=0;v<n;v++)if(viewed[v]){
            int alone=-1,unknown=0;
            for(int u=0;u<n;u++)if(edge[v][u]&&!viewed[u]){alone=u;unknown++;}
            if(unknown==1)next[alone]=1;
        }
        if(next==viewed)return -1;
        viewed=next;rounds++;
    }
}

vector<vector<int>> transitions(bool must_slide){
    vector<vector<int>> arcs(masks.size());
    for(size_t i=0;i<masks.size();i++) {
        int s=masks[i];
        for(int a=0;a<n;a++)if(s&(1<<a))
        for(int b=0;b<n;b++)if(!(s&(1<<b))){
            if(must_slide&&!edge[a][b])continue;
            int t=s^(1<<a)^(1<<b);
            auto found=lower_bound(masks.begin(),masks.end(),t);
            if(found!=masks.end()&&*found==t)
                arcs[i].push_back(static_cast<int>(found-masks.begin()));
        }
    }
    return arcs;
}
vector<vector<short>> distances(const vector<vector<int>>& arcs){
    vector<vector<short>> result;
    for(int i=0;i<(int)arcs.size();i++){
        vector<short> dist(arcs.size(),-1);
        queue<int> q;q.push(i);dist[i]=0;
        while(!q.empty()){
            int u=q.front();q.pop();
            for(int v:arcs[u])if(dist[v]==-1){dist[v]=dist[u]+1;q.push(v);}
        }
        for(short d:dist)assert(d!=-1);
        result.push_back(move(dist));
    }
    return result;
}
int main(){
    ifstream in("graph_edges.txt");
    if(!in)throw runtime_error("graph_edges.txt is required in the working directory");
    string line;int edges_read=0;
    while(getline(in,line)){
        if(line.empty()||line[0]=='#')continue;
        int a=0,b=0;
        if(sscanf(line.c_str(),"%d %d",&a,&b)!=2)throw runtime_error("bad edge row");
        assert(1<=a&&a<b&&b<=n&&!edge[a-1][b-1]);
        edge[a-1][b-1]=edge[b-1][a-1]=1;edges_read++;
    }
    assert(edges_read==38);
    for(int i=0;i<n;i++){
        int deg=0;for(int j=0;j<n;j++)deg+=edge[i][j];assert(deg==4);
    }
    for(int a=0;a<n;a++) assert(finish_time(1<<a)==-1);
    for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)assert(finish_time((1<<a)|(1<<b))==-1);
    map<int,int> times;
    for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++){
        int mask=(1<<a)|(1<<b)|(1<<c);
        int t=finish_time(mask);
        if(t>0){masks.push_back(mask);time_by_mask[mask]=t;times[t]++;}
    }
    sort(masks.begin(),masks.end());
    assert(masks.size()==753);
    assert((times==map<int,int>{{2,109},{3,320},{4,204},{5,120}}));
    auto jump=transitions(false), slide=transitions(true);
    long long je=0,se=0;
    for(auto& x:jump)je+=x.size();
    for(auto& x:slide)se+=x.size();
    assert(je==2*14538&&se==2*3452);
    auto jd=distances(jump),sd=distances(slide);
    map<int,long long> jhist,shist,surcharge;
    map<int,int> jecc,secc;
    int exceptional=0;int match_all=0;
    for(int i=0;i<(int)masks.size();i++){
        int maxj=0,maxs=0;
        for(int j=0;j<(int)masks.size();j++){
            maxj=max(maxj,(int)jd[i][j]);maxs=max(maxs,(int)sd[i][j]);
            if(j>i){
                jhist[jd[i][j]]++;shist[sd[i][j]]++;
                int x=sd[i][j]-jd[i][j];surcharge[x]++;
                if(x==4){
                    exceptional++;
                    assert(sd[i][j]==7&&jd[i][j]==3);
                    assert((masks[i]&masks[j])==0);
                    assert(time_by_mask[masks[i]]==4 && time_by_mask[masks[j]]==4);
                }
                match_all++;
            }
        }
        jecc[maxj]++;secc[maxs]++;
    }
    assert(match_all==283128);
    assert((jecc==map<int,int>{{3,753}}));
    assert((secc==map<int,int>{{6,717},{7,36}}));
    assert((jhist==map<int,long long>{{1,14538},{2,104022},{3,164568}}));
    assert((shist==map<int,long long>{{1,3452},{2,20484},{3,67788},{4,110994},{5,70116},{6,10270},{7,24}}));
    assert((surcharge==map<int,long long>{{0,29788},{1,131574},{2,109054},{3,12688},{4,24}}));
    assert(exceptional==24);
    cout<<"PASS independent arrays: 753 optima, 3452 slides, connected diameter 7, 24 maximal surcharges\n";
    cout<<"PASS all 283128 unordered configuration pairs and exact distance profiles\n";
}
