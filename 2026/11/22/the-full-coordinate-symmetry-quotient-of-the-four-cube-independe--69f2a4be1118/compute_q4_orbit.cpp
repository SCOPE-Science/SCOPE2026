// Exact barycentric orbit-cell enumeration and collapse certificate for Ind(Q_4)/Aut(Q_4).
// Compile: g++ -std=c++17 -O2 compute_q4_orbit.cpp -o compute_q4_orbit
// Run: ./compute_q4_orbit q4_orbit_certificate.txt
#include <bits/stdc++.h>
using namespace std;
using u128=unsigned __int128;
struct hash128{size_t operator()(u128 x) const{return (uint64_t)x ^ ((uint64_t)(x>>64)*0x9e3779b97f4a7c15ULL);}};
using Chain=array<uint16_t,8>;
vector<array<uint8_t,16>> acts;
unordered_map<u128,int,hash128> lookup;
vector<Chain> repr;
vector<int> lengths;
long long nChains=0;
u128 encode(const Chain& a,int k){u128 u=0;for(int i=0;i<k;i++)u|=(u128)a[i]<<(16*i);return u;}
void process(const Chain& seq,int k){nChains++;u128 key=encode(seq,k);if(lookup.count(key))return;int id=repr.size();repr.push_back(seq);lengths.push_back(k);
for(auto &p:acts){Chain b{};for(int j=0;j<k;j++){uint16_t a=seq[j],bmask=0;while(a){int bit=__builtin_ctz((unsigned)a);a&=a-1;bmask|=(1u<<p[bit]);}b[j]=bmask;}lookup[encode(b,k)]=id;}}
void visit(const Chain& seq,int k,uint16_t current,uint16_t remaining){process(seq,k);if(!remaining)return;uint16_t sub=remaining;while(sub){Chain b=seq;b[k]=current|sub;visit(b,k+1,current|sub,remaining^sub);sub=(sub-1)&remaining;}}
int main(int argc,char**argv){if(argc!=2){cerr<<"Usage: ./compute_q4_orbit q4_orbit_certificate.txt\n";return 2;}auto st=chrono::steady_clock::now();array<int,4> aa={0,1,2,3};do{for(int shift=0;shift<16;shift++){array<uint8_t,16> a;for(int x=0;x<16;x++){int y=shift;for(int i=0;i<4;i++)if(x&(1<<i))y^=1<<aa[i];a[x]=y;}acts.push_back(a);}}while(next_permutation(aa.begin(),aa.end()));
vector<uint16_t> independent;uint16_t adj[16]={};for(int v=0;v<16;v++)for(int i=0;i<4;i++)adj[v]|=1u<<(v^(1<<i));
for(int mask=1;mask<(1<<16);mask++){bool ok=true;for(int v=0;v<16;v++)if(mask&(1<<v)){if(mask&adj[v]){ok=false;break;}}if(ok)independent.push_back(mask);}
lookup.reserve(2400000);repr.reserve(10000);lengths.reserve(10000);
for(uint16_t mask:independent){Chain seq{};uint16_t sub=mask;while(sub){seq[0]=sub;visit(seq,1,sub,mask^sub);sub=(sub-1)&mask;}}
fprintf(stderr,"generated chains %lld orbits %lu time %.3fs\n",nChains,repr.size(),chrono::duration<double>(chrono::steady_clock::now()-st).count());
vector<vector<int>> faces(repr.size());vector<vector<int>> cofaces(repr.size());array<int,10> cc{};
for(int id=0;id<(int)repr.size();id++){int k=lengths[id];cc[k-1]++;for(int d=0;d<k;d++){if(k==1)continue;Chain sub{};for(int i=0,j=0;i<k;i++)if(i!=d)sub[j++]=repr[id][i];int face=lookup.at(encode(sub,k-1));faces[id].push_back(face);cofaces[face].push_back(id);}}
fprintf(stderr,"f vector ");for(int i=0;i<9;i++)fprintf(stderr,"%d ",cc[i]);fprintf(stderr,"\n");
vector<uint8_t> alive(repr.size(),1);vector<pair<int,int>> steps; // face,coface
// free pairs: min free from highest dims
vector<int> aliveCofCount(repr.size());for(int id=0;id<(int)repr.size();id++)aliveCofCount[id]=cofaces[id].size();
priority_queue<pair<int,int>> pq;for(int i=0;i<(int)repr.size();i++)if(aliveCofCount[i]==1) pq.push({lengths[i],i});
while(!pq.empty()){auto [dim,f]=pq.top();pq.pop();if(!alive[f]||aliveCofCount[f]!=1)continue;int c=-1;for(int x:cofaces[f])if(alive[x]){c=x;break;}if(c<0||lengths[c]!=lengths[f]+1)continue;alive[f]=alive[c]=false;steps.emplace_back(f,c);for(int x:faces[f]){aliveCofCount[x]--;if(aliveCofCount[x]==1)pq.push({lengths[x],x});}for(int x:faces[c])if(x!=f){aliveCofCount[x]--;if(aliveCofCount[x]==1)pq.push({lengths[x],x});}}
cc.fill(0);int left=0;for(int i=0;i<(int)repr.size();i++)if(alive[i]){cc[lengths[i]-1]++;left++;}
fprintf(stderr,"collapses %zu left %d f vector ",steps.size(),left);for(int i=0;i<9;i++)fprintf(stderr,"%d ",cc[i]);fprintf(stderr,"time %.3fs\n",chrono::duration<double>(chrono::steady_clock::now()-st).count());
// output certificate for reproducibility
ofstream out(argv[1]);if(!out){cerr<<"Cannot open output\n";return 2;}out<<"faces "<<independent.size()<<" visits "<<nChains<<" unique_flags "<<lookup.size()<<" orbits "<<repr.size()<<"\n";for(int id=0;id<(int)repr.size();id++){out<<"CELL "<<id<<" "<<lengths[id];for(int j=0;j<lengths[id];j++)out<<" "<<repr[id][j];out<<"\n";}for(auto [f,c]:steps)out<<"COLLAPSE "<<f<<" "<<c<<"\n";
}
