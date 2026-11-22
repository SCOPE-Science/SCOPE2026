// Separate exact census on the Cayley model of the 27-vertex Holt graph.
// Build: c++ -O2 -std=c++17 -Wall -Wextra verify_group.cpp -o verify_group
// Run: ./verify_group
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;
using U=uint32_t;
static const int N=27;
using Adj=array<U,N>;
static U all=(1u<<N)-1;
int idx(int x,int y) { return 9*((y%3+3)%3)+((x%9+9)%9); }
Adj make_graph(){
    Adj a{};
    // Group: a^9=b^3=1, b^-1 a b=a^4; generators a and c=ba^-1.
    // Elements a^x b^y, with right products by a^+/-1 and c^+/-1.
    int pow7[3]={1,7,4};
    for(int y=0;y<3;y++)for(int x=0;x<9;x++){
        int p=idx(x,y), t=pow7[y];
        for(int v : {idx(x+t,y),idx(x-t,y),idx(x+2*t,y+1),idx(x+t,y+2)})
            a[p] |= 1u<<v;
    }
    for(int i=0;i<N;i++){
        assert(__builtin_popcount(a[i])==4);
        for(int j=0;j<N;j++)assert(bool(a[i]&(1u<<j))==bool(a[j]&(1u<<i)));
    }
    return a;
}
// Observe neighbors and propagate synchronously until fixed point.
int rounds(U s, const Adj& a){
    U obs=s;
    for(int i=0;i<N;i++)if(s&(1u<<i))obs|=a[i];
    int t=1;
    while(obs!=all){
        U nxt=obs;
        for(int i=0;i<N;i++)if(obs & (1u<<i)){
            U rem=a[i]&~obs;
            if(rem && !(rem&(rem-1)))nxt|=rem;
        }
        if(nxt==obs)return 0;
        obs=nxt;t++;
    }
    return t;
}
vector<int> bfs(const vector<vector<int>>& e,int source){
    vector<int>d(e.size(),-1);queue<int>q;q.push(source);d[source]=0;
    while(!q.empty()){
        int v=q.front();q.pop();
        for(int w:e[v])if(d[w]==-1){d[w]=d[v]+1;q.push(w);}
    }
    for(int k:d)assert(k>=0);
    return d;
}
int main(){
    auto a=make_graph();
    for(int i=0;i<N;i++)assert(rounds(1u<<i,a)==0);
    for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)assert(rounds((1u<<i)|(1u<<j),a)==0);
    vector<U> opt;map<int,int> phase;
    for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)for(int k=j+1;k<N;k++){
        U m=(1u<<i)|(1u<<j)|(1u<<k);int r=rounds(m,a);
        if(r){opt.push_back(m);phase[r]++;}
    }
    assert(opt.size()==567 && phase[5]==351 && phase[6]==216);
    unordered_map<U,int> where;
    for(size_t z=0;z<opt.size();z++)where[opt[z]]=(int)z;
    vector<vector<int>> jumps(opt.size()),slides(opt.size());
    for(size_t z=0;z<opt.size();z++){
        U m=opt[z];
        for(int u=0;u<N;u++)if(m&(1u<<u))
            for(int v=0;v<N;v++)if(!(m&(1u<<v))){
                U nn=m^(1u<<u)^(1u<<v);
                auto it=where.find(nn);
                if(it!=where.end()){
                    jumps[z].push_back(it->second);
                    if(a[u]&(1u<<v))slides[z].push_back(it->second);
                }
            }
    }
    long long ej=0,es=0;
    for (const auto& v : jumps) ej += v.size();
    for (const auto& v : slides) es += v.size();
    assert(ej==10800 && es==2484);
    map<int,int> eJ,eS;map<int,long long> delta;long long onesix=0, pairs=0;
    for(size_t i=0;i<opt.size();i++){
        vector<int> dj=bfs(jumps,(int)i), ds=bfs(slides,(int)i);
        int mj=0,ms=0;
        for(size_t j=0;j<opt.size();j++){mj=max(mj,dj[j]);ms=max(ms,ds[j]);}
        eJ[mj]++;eS[ms]++;
        for(size_t j=i+1;j<opt.size();j++){
            delta[ds[j]-dj[j]]++;
            if(dj[j]==1 && ds[j]==6)onesix++;
            pairs++;
        }
    }
    assert(pairs==160461 && eJ[4]==567 && eS[7]==432 && eS[8]==135);
    assert(delta.size()==6 && delta[0]==12501 && delta[1]==34830 && delta[2]==54189
      && delta[3]==47250 && delta[4]==11340 && delta[5]==351 && onesix==54);
    cout<<"PASS group-Cayley model: 567 configurations, jump edges="<<ej/2
        <<", slide edges="<<es/2<<", radii 4 and 7, diameters 4 and 8.\n";
    cout<<"PASS all 160461 unordered pairs: excess distribution";
    for(const auto& p:delta)cout<<" "<<p.first<<":"<<p.second;
    cout<<"; jump-one slide-six pairs="<<onesix<<".\n";
}
