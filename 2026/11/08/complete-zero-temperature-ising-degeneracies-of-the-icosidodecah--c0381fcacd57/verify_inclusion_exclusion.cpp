// Exact inclusion-exclusion ground-state count, independent of backtracking,
// plus a separate full matching-polynomial enumeration at saturation.
// The 30-edge table is an alternative dodecahedral labeling, checked below
// by an explicit isomorphism to the canonical GP(10,2) construction.
#include <array>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
using i64=long long;
constexpr int E[30][2]={{0,1},{0,10},{0,19},{1,2},{1,8},{2,3},{2,6},{3,4},{3,19},{4,5},{4,17},{5,6},{5,15},{6,7},{7,8},{7,14},{8,9},{9,10},{9,13},{10,11},{11,12},{11,18},{12,13},{12,16},{13,14},{14,15},{15,16},{16,17},{17,18},{18,19}};
constexpr int map_gp[20]={0,1,2,12,14,4,3,13,11,19,9,8,7,17,15,5,6,16,18,10};
int inc[20][3], par[30],sz[30];
i64 H[31]={}, matching[11]={};
int root(int x){while(par[x]!=x){par[x]=par[par[x]];x=par[x];}return x;}
void join(int a,int b){a=root(a);b=root(b);if(a!=b){if(sz[a]<sz[b]){int t=a;a=b;b=t;}par[b]=a;sz[a]+=sz[b];}}
void check_graph(){
 int deg[20]={}, seen[20]={};
 for(int e=0;e<30;e++){
   int x=E[e][0],y=E[e][1];
   if(x<0||x>=20||y<0||y>=20||x==y)std::abort();
   inc[x][deg[x]++]=e;inc[y][deg[y]++]=e;
   int a=map_gp[x],b=map_gp[y];
   if(a>b){int t=a;a=b;b=t;}
   bool good=false;
   for(int i=0;i<10;i++){
     int pairs[3][2]={{i,(i+1)%10},{i,10+i},{10+i,10+(i+2)%10}};
     for(auto &p:pairs){int c=p[0],d=p[1];if(c>d){int t=c;c=d;d=t;}if(a==c&&b==d)good=true;}
   }
   if(!good)std::abort();
 }
 for(int v=0;v<20;v++){if(deg[v]!=3||map_gp[v]<0||map_gp[v]>=20||seen[map_gp[v]]++)std::abort();}
}
void inclusion_exclusion(){
 for(int mask=0;mask<(1<<20);mask++){
   for(int e=0;e<30;e++){par[e]=e;sz[e]=1;}
   for(int bits=mask;bits;bits&=bits-1){int v=__builtin_ctz((unsigned)bits);join(inc[v][0],inc[v][1]);join(inc[v][0],inc[v][2]);}
   i64 polynomial[31]={};polynomial[0]=1;
   for(int e=0;e<30;e++)if(par[e]==e){int s=sz[e];for(int k=30-s;k>=0;k--)polynomial[k+s]+=polynomial[k];}
   int sign=__builtin_parity((unsigned)mask)?-1:1;
   for(int k=0;k<=30;k++)H[k]+=sign*polynomial[k];
 }
}
void enumerate_matchings(unsigned remaining,int size){
 if(!remaining){++matching[size];return;}
 int v=__builtin_ctz(remaining);unsigned rest=remaining & ~(1u<<v);
 enumerate_matchings(rest,size); // vertex left unmatched
 for(auto &e:E){int u=-1;if(e[0]==v)u=e[1];if(e[1]==v)u=e[0];if(u>=0&&(rest&(1u<<u)))enumerate_matchings(rest&~(1u<<u),size+1);}
}
int main(){
 check_graph();inclusion_exclusion();enumerate_matchings((1u<<20)-1,0);
 constexpr i64 wantH[31]={0,0,0,0,0,0,0,0,0,0,36,3150,50265,287370,762390,1044828,762390,287370,50265,3150,36,0,0,0,0,0,0,0,0,0,0};
 constexpr i64 wantM[11]={1,30,375,2540,10155,24474,34805,27300,10260,1400,36};
 i64 sumH=0,sumM=0;
 for(int k=0;k<=30;k++){if(H[k]!=wantH[k]){std::fprintf(stderr,"ground k=%d actual=%lld expected=%lld\n",k,H[k],wantH[k]);return 1;}sumH+=H[k];}
 for(int k=0;k<=10;k++){if(matching[k]!=wantM[k]){std::fprintf(stderr,"matching k=%d actual=%lld expected=%lld\n",k,matching[k],wantM[k]);return 2;}sumM+=matching[k];}
 if(sumH!=3251250||sumM!=111376)return 3;
 std::printf("VERIFY_IE_OK zero_field=%lld saturation=%lld\n",sumH,sumM);
}
