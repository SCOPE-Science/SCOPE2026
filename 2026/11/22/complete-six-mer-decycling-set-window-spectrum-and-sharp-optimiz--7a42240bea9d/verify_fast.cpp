// Enumerate one choice per rotation orbit in binary order-six de Bruijn graph.
// Every candidate of minimum cardinality must have exactly one element per orbit.
// Prune partial choices when the induced graph on finalized-orbit survivors is cyclic.
#include <bits/stdc++.h>
using namespace std;
const int K=6,N=64;
using U=uint64_t;
vector<vector<int>> orbs;
uint64_t nodes=0, leaves=0, acyclic=0, pruning[16]={};
map<int,long long> hist;
int first_choice[14]={};
int idx_order[14];
inline int topo(U active){
    unsigned char indeg[N]={};
    int qq[N]; int front=0,back=0;
    U a=active;
    while(a){int x=__builtin_ctzll(a);a&=a-1;
        int y=(x*2)&63;
        if(active>>y&1)indeg[y]++;
        if(active>>(y|1)&1)indeg[y|1]++;
    }
    a=active;
    while(a){int x=__builtin_ctzll(a);a&=a-1;if(!indeg[x])qq[back++]=x;}
    int cnt=0;
    while(front<back){int x=qq[front++];cnt++;
        int y=(x*2)&63;
        if((active>>y&1)&&!--indeg[y])qq[back++]=y;
        y|=1;
        if((active>>y&1)&&!--indeg[y])qq[back++]=y;
    }
    return cnt==__builtin_popcountll(active);
}
int longest(U active){
    unsigned char indeg[N]={}; int dist[N]={}; int qq[N]; int front=0,back=0;
    U a=active;
    while(a){int x=__builtin_ctzll(a);a&=a-1;
        int y=(x*2)&63;
        if(active>>y&1)indeg[y]++;
        if(active>>(y|1)&1)indeg[y|1]++;
    }
    a=active;
    while(a){int x=__builtin_ctzll(a);a&=a-1;if(!indeg[x])qq[back++]=x,dist[x]=1;}
    int cnt=0,mx=0;
    while(front<back){int x=qq[front++];cnt++;mx=max(mx,dist[x]);
        for(int y0=0;y0<2;y0++){
            int y=((x*2)&63)|y0;
            if(active>>y&1){dist[y]=max(dist[y],dist[x]+1);if(!--indeg[y])qq[back++]=y;}
        }
    }
    return cnt==__builtin_popcountll(active)?mx:0;
}
void rec(int d,U active){
    ++nodes;
    if(d==14){leaves++;int L=longest(active);if(!L){cerr<<"INVALID LEAF"<<endl;exit(1);}hist[L]++;acyclic++;return;}
    int idx=idx_order[d];auto &o=orbs[idx];U all=0;
    for(int x:o) all |= (1ULL<<x);
    for(int x:o){
        U a=active|(all^(1ULL<<x));
        // Checking from level 3 onward avoids tiny pointless checks
        if(d>=3&&!topo(a)){pruning[d]++;continue;}
        first_choice[idx]=x;
        rec(d+1,a);
    }
}
int main(int argc,char**argv){
    bool seen[N]={};
    for(int x=0;x<N;x++)if(!seen[x]){vector<int>v;int y=x;while(!seen[y]){seen[y]=1;v.push_back(y);y=((y<<1)&63)|(y>>5);}orbs.push_back(v);}
    // Try rank-order: large orbits first (more vertices each), delay small to gain pruning.
    vector<int> ord(14);iota(ord.begin(),ord.end(),0);
    stable_sort(ord.begin(),ord.end(),[&](int a,int b){return orbs[a].size()>orbs[b].size();});
    // Fixed singleton deletions can be chosen last or first; all sides same.
    for(int i=0;i<14;i++)idx_order[i]=ord[i];
    cerr<<"order:";for(int i:ord)cerr<<" "<<i;cerr<<endl;
    auto st=chrono::steady_clock::now();rec(0,0);
    cerr<<"seconds "<<chrono::duration<double>(chrono::steady_clock::now()-st).count()<<" nodes "<<nodes<<" leaves "<<leaves<<" accepted "<<acyclic<<endl;
    for(int i=0;i<14;i++)cerr<<"pruned "<<i<<" "<<pruning[i]<<endl;
    for(auto kv:hist)cout<<kv.first<<" "<<kv.second<<"\n";
}
