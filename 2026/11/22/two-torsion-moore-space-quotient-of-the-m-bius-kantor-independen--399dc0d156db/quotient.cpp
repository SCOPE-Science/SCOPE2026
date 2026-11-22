#include <bits/stdc++.h>
using namespace std;
struct Key {array<uint16_t,8> f{}; uint8_t len=0;bool operator==(Key const& o) const{if(len!=o.len)return false;for(int i=0;i<len;i++)if(f[i]!=o.f[i])return false;return true;}};
struct Hash {size_t operator()(Key const& k)const {uint64_t h=0xcbf29ce484222325ULL;for(int i=0;i<k.len;i++) {h^=k.f[i];h*=0x100000001b3ULL;}return h^k.len;}};
vector<array<int,16>> aut;vector<vector<uint16_t>> transmaps;unordered_map<Key,int,Hash> cm;vector<Key> cells;vector<vector<int>> boundary,upper; vector<int> lens;
int nperms=0;
bool adjacency[16][16]={};int partial_map[16],reverse_map[16];
void enumerate_aut(int assigned){
 if(assigned==16){array<int,16> p;for(int i=0;i<16;i++)p[i]=partial_map[i];aut.push_back(p);return;}
 int v=-1,best=-1;
 for(int i=0;i<16;i++)if(partial_map[i]<0){int score=0;for(int j=0;j<16;j++)if(partial_map[j]>=0&&adjacency[i][j])score++;if(score>best){best=score;v=i;}}
 for(int w=0;w<16;w++)if(reverse_map[w]<0){bool ok=true;
 for(int i=0;i<16;i++)if(partial_map[i]>=0 && adjacency[v][i]!=adjacency[w][partial_map[i]]){ok=false;break;}
 if(ok){partial_map[v]=w;reverse_map[w]=v;enumerate_aut(assigned+1);partial_map[v]=-1;reverse_map[w]=-1;}}
}

Key canonical(Key k){Key best=k; for(int p=0;p<nperms;p++){Key q; q.len=k.len; for(int i=0;i<k.len;i++) q.f[i]=transmaps[p][k.f[i]];bool less=false;for(int i=0;i<k.len;i++){if(q.f[i]<best.f[i]){less=true;break;}if(q.f[i]>best.f[i])break;}if(less)best=q;}return best;}
int get(Key const &k){auto ck=canonical(k); auto it=cm.find(ck); if(it!=cm.end())return it->second; int id=cells.size();cells.push_back(ck);cm.emplace(ck,id);lens.push_back(ck.len);return id;}
void walk(int face,Key &k){k.f[k.len++]=face;get(k); for(int sub=(face-1)&face;sub;sub=(sub-1)&face) { // restrict to independent since any subset independent
 walk(sub,k);
}k.len--;}
int main(int argc,char**argv){string out=argc>1?argv[1]:"quotient_certificate.txt";
vector<pair<int,int>> edges;for(int i=0;i<8;i++){edges.push_back({i,(i+1)%8});edges.push_back({i,8+i});edges.push_back({8+i,8+(i+3)%8});}
for(auto [u,v]:edges){adjacency[u][v]=adjacency[v][u]=true;}
fill(partial_map,partial_map+16,-1);fill(reverse_map,reverse_map+16,-1);
enumerate_aut(0);nperms=aut.size();if(nperms!=96){cerr<<"automorphism enumeration "<<nperms<<"\n";return 1;}
transmaps.assign(nperms,vector<uint16_t>(1<<16));for(int p=0;p<nperms;p++)for(int m=1;m<(1<<16);m++){int b=__builtin_ctz((unsigned)m);transmaps[p][m]=transmaps[p][m^(1<<b)]|(1<<aut[p][b]);}
vector<int> faces;for(int m=1;m<(1<<16);m++){bool ok=true;for(auto [u,v]:edges)if((m&(1<<u))&&(m&(1<<v))){ok=false;break;} if(ok)faces.push_back(m);}cerr<<"faces "<<faces.size()<<"\n";
cm.reserve(20000); cells.reserve(20000);Key k;
for(int face:faces)walk(face,k);
cerr<<"orbit cells "<<cells.size()<<"\n"; if(faces.size()!=1090 || cells.size()!=24875)return 7;
int N=cells.size();boundary.assign(N,{});upper.assign(N,{});
for(int id=0;id<N;id++)if(lens[id]>1){Key x=cells[id];for(int i=0;i<x.len;i++){Key y; y.len=x.len-1;for(int j=0,t=0;j<x.len;j++)if(j!=i)y.f[t++]=x.f[j];int b=get(y);boundary[id].push_back(b);upper[b].push_back(id);}}if((int)cells.size()!=N){cerr<<"new faces created";return 2;}
vector<int> nco(N);for(int i=0;i<N;i++)nco[i]=upper[i].size();deque<int> todo;for(int i=0;i<N;i++)if(nco[i]==1)todo.push_back(i);
vector<bool> alive(N,true);vector<pair<int,int>> collapses;
while(!todo.empty()){int low=todo.front();todo.pop_front();if(!alive[low]||nco[low]!=1)continue;int high=-1;for(int h:upper[low])if(alive[h]){if(high>=0){cerr<<"bad coface";return 3;}high=h;}if(high<0){cerr<<"missing coface";return 4;}
// check maximal high (no higher alive)
if(nco[high]){cerr<<"coface not maximal "<<nco[high]<<"\n";return 5;}
alive[low]=alive[high]=false;collapses.push_back({low,high});for(int b:boundary[low]){--nco[b];if(nco[b]==1)todo.push_back(b);}for(int b:boundary[high]){--nco[b];if(nco[b]==1)todo.push_back(b);}
}
map<int,int>counts,remain;for(int i=0;i<N;i++){counts[lens[i]-1]++;if(alive[i])remain[lens[i]-1]++;}
cerr<<"cells by dim ";for(auto [d,x]:counts)cerr<<d<<":"<<x<<" ";cerr<<"\nremaining ";for(auto [d,x]:remain)cerr<<d<<":"<<x<<" ";cerr<<"\ncollapses "<<collapses.size()<<"\n";
ofstream f(out);f<<"AUT "<<nperms<<" FACES "<<faces.size()<<" CELLS "<<N<<" COLLAPSES "<<collapses.size()<<"\n";for(auto [d,x]:counts)f<<"COUNT "<<d<<" "<<x<<"\n";for(auto [d,x]:remain)f<<"REMAIN "<<d<<" "<<x<<"\n";for(auto [lo,hi]:collapses)f<<"PAIR "<<lo<<" "<<hi<<"\n";for(int i=0;i<N;i++)if(alive[i]){f<<"LIVE "<<i<<" "<<lens[i];for(int j=0;j<lens[i];j++)f<<" "<<cells[i].f[j];f<<"\n";}f.close();
ofstream z("residual_cells.txt");for(int i=0;i<N;i++)if(alive[i]){z<<"C "<<i<<" "<<(int)lens[i]-1;for(int j=0;j<lens[i];j++)z<<" "<<cells[i].f[j];z<<" |";for(int j=0;j<(int)boundary[i].size();j++){int b=boundary[i][j];if(!alive[b]){cerr<<"invalid boundary of residual "<<i<<" face "<<b<<"\n";return 6;}z<<" "<<b<<":"<<(j%2?-1:1);}z<<"\n";}z.close(); cerr<<"MK_ORBIT_CELL_COLLAPSE_OK"<<"\n";
}
