#include<bits/stdc++.h>
using namespace std;
int main(){constexpr int n=24;array<uint32_t,n> adj{};auto add=[&](int a,int b){adj[a]|=1u<<b;adj[b]|=1u<<a;};for(int i=0;i<12;i++){add(i,(i+1)%12);add(i,i+12);add(12+i,12+(i+5)%12);}map<tuple<int,int,int>,long long> hist;map<int,long long> timehist;long long total=0,others=0;vector<uint32_t> opts;function<void(int,int,int)> scan=[&](int i,int left,int mask){if(!left){uint32_t seeds=(uint32_t)mask,remaining=((1u<<n)-1u)^seeds; // leaf peel
 int c=0,e=0;uint32_t seen=0;for(int u=0;u<n;u++)if(remaining&(1u<<u)){e+=__builtin_popcount(adj[u]&remaining);if(!(seen&(1u<<u))){c++;uint32_t todo=1u<<u;seen|=todo;while(todo){int x=__builtin_ctz(todo);todo &=todo-1;uint32_t ns=adj[x]&remaining&~seen;todo|=ns;seen|=ns;}}} e/=2;
 if(e!=n-7-c) return; // forest (note n-7 fixed)
 uint32_t infected=seeds;int t=0;while(infected!=((1u<<n)-1u)){uint32_t next=infected;for(int u=0;u<n;u++)if(!(infected>>u&1) && __builtin_popcount(adj[u]&infected)>=2) next|=1u<<u;if(next==infected){cerr<<"IMPOSSIBLE";exit(1);}infected=next;t++;}
 int se=0;for(int u=0;u<n;u++)if(seeds>>u&1)se+=__builtin_popcount(adj[u]&seeds);se/=2;total++;timehist[t]++;hist[{t,c,se}]++;opts.push_back(seeds);return;}
 for(int j=i;j<=n-left;j++)scan(j+1,left-1,mask|(1<<j));};scan(0,7,0);cerr<<"total "<<total<<" opts "<<opts.size()<<"\n";for(auto [t,c]:timehist)cerr<<"T "<<t<<"="<<c<<"\n";for(auto [key,count]:hist){auto [t,c,e]=key;cerr<<"T="<<t<<" c="<<c<<" e="<<e<<" : "<<count<<"\n";}cout<<"EXAMPLE "<<opts.front()<<"\n";}
