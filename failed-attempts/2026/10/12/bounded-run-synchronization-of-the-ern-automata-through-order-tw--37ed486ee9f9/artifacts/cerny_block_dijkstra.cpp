// Independently weighted subset shortest paths using the normal form b(ab|aab)*.
// Every entry is a subset of the post-b states 0,...,n-2.
#include <bits/stdc++.h>
using namespace std;
static inline uint32_t rot(uint32_t x,int m,int k){uint32_t mask=(1u<<m)-1;return ((x<<k)&mask)|(x>>(m-k));}
int main(int argc,char**argv){
 int maxn=24;if(argc>1)maxn=stoi(argv[1]);if(maxn<3||maxn>24)return 2;
 for(int n=3;n<=maxn;n++){
  int m=n-1;uint32_t states=1u<<m,start=states-1;
  vector<uint32_t> dist(states,UINT32_MAX),par(states,UINT32_MAX);
  vector<vector<uint32_t>> buckets(2u*n*n+30);
  dist[start]=0;par[start]=UINT32_MAX-1;buckets[0].push_back(start);
  uint32_t goal=0,popped=0;int endd=-1;
  for(size_t d=0;d<buckets.size();d++){
   auto &bucket=buckets[d];
   for(size_t i=0;i<bucket.size();i++){
    uint32_t x=bucket[i];if(dist[x]!=d)continue;popped++;
    if(__builtin_popcount(x)==1){goal=x;endd=(int)d;break;}
    uint32_t f=rot(x,m,1);
    uint32_t g=rot(x,m,2);
    if(x&(1u<<(m-1)))g=(g&~2u)|1u;
    for(int j=0;j<2;j++){
     uint32_t y=j?g:f;uint32_t nd=d+(j?3u:2u);
     if(nd<dist[y]){
      dist[y]=nd;par[y]=x|(j?0x80000000u:0u);
      if(nd>=buckets.size()){cerr<<"Bucket capacity exceeded\n";return 6;}
      buckets[nd].push_back(y);
     }
    }
   }
   if(endd>=0)break;
  }
  if(endd<0){cerr<<"No reset for n="<<n<<'\n';return 3;}
  vector<char> blocks;
  for(uint32_t x=goal;x!=start;){uint32_t p=par[x];blocks.push_back(p&0x80000000u?'g':'f');x=p&0x7fffffffu;}
  reverse(blocks.begin(),blocks.end());
  string word="b";for(char c:blocks)word+=(c=='f'?"ab":"aab");
  if((int)word.size()!=1+endd){cerr<<"Length mismatch\n";return 4;}
  cout<<n<<" "<<word.size()<<" "<<popped<<" "<<count(blocks.begin(),blocks.end(),'f')<<" "<<count(blocks.begin(),blocks.end(),'g')<<" "<<word<<"\n";
 }
}
