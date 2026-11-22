// Exhaustive labelled-graph check of the seven-vertex triangle-free-vertex-set Euler transform.
// This checker does not use graph catalogues or isomorphism libraries.
#include <cstdio>
#include <cstdint>
#include <vector>
#include <array>
#include <cassert>
using namespace std;
int main(){
 for(int n=1;n<=7;n++){
  int edgeId[7][7]; for(auto &r:edgeId)for(auto &x:r)x=-1;
  int e=0;
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)edgeId[a][b]=edgeId[b][a]=e++;
  vector<pair<unsigned,unsigned long long>> triples;
  int triId[7][7][7]={};int t=0;
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++){
   unsigned em=(1u<<edgeId[a][b])|(1u<<edgeId[a][c])|(1u<<edgeId[b][c]);
   triples.emplace_back(em,(1ULL<<t)); triId[a][b][c]=t++;
  }
  vector<unsigned long long> contained(1u<<n,0);
  for(int s=0;s<(1<<n);s++){
   for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++)
    if((s&((1<<a)|(1<<b)|(1<<c)))==((1<<a)|(1<<b)|(1<<c)))
     contained[s]|=1ULL<<triId[a][b][c];
  }
  vector<unsigned> cliques4;
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++)for(int d=c+1;d<n;d++){
   unsigned mask=0;int v[]={a,b,c,d};
   for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)mask|=1u<<edgeId[v[i]][v[j]];
   cliques4.push_back(mask);
  }
  long long fourfree=0,large=0,wheel=0;int maxabs=0;long long hist[15]={};
  for(unsigned graph=0;graph<(1u<<e);graph++){
   bool bad=false;
   for(unsigned c:cliques4)if((graph&c)==c){bad=true;break;}
   if(bad)continue;
   fourfree++;
   unsigned long long tri=0;
   for(auto q:triples)if((graph&q.first)==q.first)tri|=q.second;
   int w=0;
   for(unsigned s=0;s<(1u<<n);s++)if((tri&contained[s])==0)w+=((n-__builtin_popcount(s))&1)?-1:1;
   if(w>=-7&&w<=7)hist[w+7]++;
   if(w>maxabs)maxabs=w;
   if(-w>maxabs)maxabs=-w;
   if(w>1||w< -1){
    large++;
    if(n!=7||w!=2){printf("UNEXPECTED n=%d mask=%u w=%d\n",n,graph,w);return 1;}
    int center=-1, deg[7]={};
    for(int a=0;a<n;a++)for(int b=a+1;b<n;b++) if(graph&(1u<<edgeId[a][b]))deg[a]++,deg[b]++;
    for(int a=0;a<n;a++)if(deg[a]==6){if(center!=-1){printf("2 CENTER ERROR\n");return 1;}center=a;}
    if(center==-1){printf("NO CENTER ERROR\n");return 1;}
    for(int a=0;a<n;a++)if(a!=center&&deg[a]!=3){printf("RIM DEG ERROR\n");return 1;}
    // A 2-regular six-vertex rim must be a single C6, not two triangles, as K4 is forbidden.
    wheel++;
   }
  }
  printf("n=%d K4-free-labelled=%lld exceptional=%lld wheels=%lld maxabs=%d histogram",n,fourfree,large,wheel,maxabs);
  for(int x=-7;x<=7;x++)if(hist[x+7])printf(" %d:%lld",x,hist[x+7]);
  puts("");
  if(n<=6&&large) return 1;
  if(n==7&&large!=420)return 1;
 }
 puts("EXHAUSTIVE_CENSUS_OK");
}
