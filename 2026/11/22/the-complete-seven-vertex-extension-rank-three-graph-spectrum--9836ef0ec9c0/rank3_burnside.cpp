// Exact seven-vertex graph census via Burnside's lemma; no external dependencies.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdio>
#include <vector>
using namespace std;
constexpr int n=7; using U=uint32_t;
int idx[7][7],ei[21],ej[21];
int fact(int x){int z=1;for(int i=2;i<=x;i++)z*=i;return z;}
bool good(U mask){
 unsigned char adj[7]={};
 for(int e=0;e<21;e++)if(mask&(1u<<e)) {adj[ei[e]]|=1u<<ej[e];adj[ej[e]]|=1u<<ei[e];}
 for(int v=0;v<n;v++) if(__builtin_popcount((unsigned)adj[v])==3){
   U A=adj[v],B=127u&~(A|(1u<<v)); bool yes=false,no=false;
   for(int w=0;w<7;w++)if(w!=v){
     U within=(adj[w] & (bool(A&(1u<<w)) ? (A&~(1u<<w)) : (B&~(1u<<w))));
     int c=__builtin_popcount(within);
     if(c!=1)continue;
     if(A&(1u<<w)) {int cross=__builtin_popcount((unsigned)(adj[w]&B)); if(cross>0&&cross<3) yes=true;}
     else {int cross=__builtin_popcount((unsigned)(adj[w]&A)); if(cross>0&&cross<3) no=true;}
   }
   if(yes&&no)return true;
 }
 return false;
}
int main(){
 int t=0;for(int i=0;i<7;i++)for(int j=i+1;j<7;j++){idx[i][j]=idx[j][i]=t;ei[t]=i;ej[t]=j;t++;}
 vector<vector<int>> parts; vector<int> buf;
 auto gen=[&](auto&& self,int r,int maxp)->void{if(r==0){parts.push_back(buf);return;}for(int i=min(r,maxp);i>=1;i--){buf.push_back(i);self(self,r-i,i);buf.pop_back();}};
 gen(gen,7,7);
 long long burn=0; int totalfixed=0; long long edgeweighted[22]={}; int labelledhist[22]={};
 puts("cycle_type,permutations,fixed_rank3_graphs,weighted_fixed");
 for(auto part:parts){
   int perm[7]={},st=0;
   for(int s:part){for(int k=0;k<s;k++)perm[st+k]=st+(k+1)%s;st+=s;}
   bool seen[21]={};vector<U> orbits;
   for(int k=0;k<21;k++)if(!seen[k]){
     U mask=0;int e=k;
     while(!seen[e]){seen[e]=true;mask|=1u<<e; e=idx[perm[ei[e]]][perm[ej[e]]];}
     orbits.push_back(mask);
   }
   int m=orbits.size(); uint64_t cnt=0; uint64_t local[22]={};
   for(U bits=0;bits<(1u<<m);bits++){
     U mask=0;
     for(int j=0;j<m;j++) if(bits>>j&1u)mask|=orbits[j];
     if(good(mask)){cnt++;local[__builtin_popcount(mask)]++;}
   }
   int d=1;for(int s:part)d*=s;
   for(int i=0;i<(int)part.size();){int j=i;while(j<(int)part.size()&&part[j]==part[i])j++;d*=fact(j-i);i=j;}
   int classsize=fact(7)/d;
   long long weighted=1LL*classsize*cnt;burn+=weighted; for(int e=0;e<=21;e++){edgeweighted[e]+=1LL*classsize*local[e];if(part.size()==7)labelledhist[e]=(int)local[e];}
   for(int j=0;j<(int)part.size();j++)printf("%s%d",j?"-":"",part[j]);
   printf(",%d,%llu,%lld\n",classsize,(unsigned long long)cnt,weighted);
   if(part.size()==7)totalfixed=cnt;
 }
 printf("LABELLED=%d BURNSIDE_SUM=%lld UNLABELLED=%lld\n",totalfixed,burn,burn/5040);
 const int expectedU[22]={0,0,0,0,0,0,1,10,31,61,83,83,61,31,10,1,0,0,0,0,0,0};
 const int expectedL[22]={0,0,0,0,0,0,5040,31500,99540,191520,254079,254079,191520,99540,31500,5040,0,0,0,0,0,0};
 puts("edge,unlabelled,labelled");
 for(int e=0;e<=21;e++){
   if(edgeweighted[e]%5040||edgeweighted[e]/5040!=expectedU[e]||labelledhist[e]!=expectedL[e])return 3;
   if(labelledhist[e])printf("%d,%lld,%d\n",e,edgeweighted[e]/5040,labelledhist[e]);
 }
 if(burn%5040||burn/5040!=372||totalfixed!=1163358)return 2;
 puts("BURNSIDE_ALL_CHECKS_OK");
 return 0;
}
