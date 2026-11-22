#include <bits/stdc++.h>
using namespace std;
int main(int argc, char **argv){vector<pair<int,int>> D;for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)D.push_back({a,b});
vector<array<int,3>> M;function<void(int,vector<int>)> rec=[&](int avail,vector<int> cur){if(!avail){M.push_back({cur[0],cur[1],cur[2]});return;}int a=__builtin_ctz((unsigned)avail);for(int b=a+1;b<6;b++)if(avail>>b&1){auto x=cur; x.push_back(find(D.begin(),D.end(),make_pair(a,b))-D.begin());rec(avail^(1<<a)^(1<<b),x);}};rec(63,{});
uint32_t adj[30]={};for(int j=0;j<15;j++)for(int i:M[j]){adj[i]|=1u<<(15+j); adj[15+j]|=1u<<i;}
uint32_t ALL=(1u<<30)-1;
ofstream out(argc>1 ? argv[1] : "optima.txt"); long long success=0, independent=0, forest=0, conn=0;int per[9]={}, extE[9]={}; map<int,int> rounds;int inducedS[10]={};uint32_t s=(1u<<8)-1;
while(s<=ALL){uint32_t U=ALL^s;int ie=0;uint32_t t=s;while(t){int v=__builtin_ctz(t);t&=t-1;ie+=__builtin_popcount(adj[v]&s);}ie/=2;if(!ie)independent++;int inducedE=45-3*8+ie;bool isforest=false,isconn=false;
if(inducedE<=21){uint32_t seen=0;int components=0;uint32_t unseen=U;while(unseen){components++;uint32_t front=unseen&-unseen;seen|=front;unseen^=front;while(front){uint32_t neigh=0,x=front;while(x){int v=__builtin_ctz(x);x&=x-1;neigh |= adj[v];}front=neigh&unseen;unseen^=front;seen|=front;}}isforest=inducedE==22-components;isconn=components==1;}
if(isforest)forest++;if(isconn)conn++;
uint32_t active=s;int r=0;while(1){uint32_t rem=ALL^active, add=0;while(rem){int v=__builtin_ctz(rem);rem&=rem-1;if(__builtin_popcount(adj[v]&active)>=2)add|=1u<<v;}if(!add)break;active|=add;r++;}
if(active==ALL){success++;per[__builtin_popcount(s&((1u<<15)-1))]++;rounds[r]++;inducedS[ie]++;out<<s<<"\n";if(!isforest) {cerr<<"not forest!\n";return 1;}}
uint32_t c=s&-s, next=s+c;if(!next||next>ALL)break;s=(((next^s)>>2)/c)|next;
}
cout<<"success "<<success<<" forest "<<forest<<" independent "<<independent<<" conn_tree "<<conn<<"\n";
cout<<"point profile ";for(int j=0;j<=8;j++)cout<<per[j]<<" ";cout<<"\nrounds ";for(auto [j,c]:rounds)cout<<j<<":"<<c<<" ";cout<<"\ninduced seed edges:";for(int j=0;j<10;j++)cout<<j<<":"<<inducedS[j]<<" ";cout<<"\n";
 if(success!=12780 || independent!=111225 || forest!=12780 || conn!=12780) return 1;
 if(rounds!=map<int,int>{{4,120},{5,660},{6,3360},{7,4320},{8,1440},{9,2880}}) return 2;
 cout<<"INCIDENCE_CENSUS_OK\n";
}
