#include <bits/stdc++.h>
using namespace std;
// token-swapping on C_5 square K_2, vertices 0..4 outer ring and 5..9 inner ring.
const int N=10; const int SZ=3628800;
int fact[11];
inline int rankp(const uint8_t* p){
 int r=0; unsigned seen=0;
 for(int i=0;i<N;i++){
  unsigned v=p[i]; unsigned small=__builtin_popcount(seen & ((1u<<v)-1));
  r+=(v-small)*fact[N-1-i]; seen|=1u<<v;
 }
 return r;
}
inline void unrank(int r,uint8_t* p){
 unsigned rem=(1u<<N)-1;
 for(int i=0;i<N;i++){
  int f=fact[N-1-i], q=r/f; r%=f;
  int v=-1;for(int b=0;b<10;b++)if(rem&(1u<<b)){v=b;if(q--==0)break;}
  p[i]=v; rem^=1u<<v;
 }
}
int main(){
 fact[0]=1;for(int i=1;i<=10;i++)fact[i]=i*fact[i-1];
 vector<pair<int,int>> edges;
 for(int z=0;z<2;z++)for(int i=0;i<5;i++)edges.push_back({z*5+i,z*5+(i+1)%5});
 for(int i=0;i<5;i++)edges.push_back({i,i+5});
 vector<uint8_t> dist(SZ,255);vector<int> q(SZ); int head=0,tail=1; q[0]=0;dist[0]=0;
 vector<long long> shell(50,0);int maxd=0, maxgap=0;
 long long gapmaxcount=0;
 vector<int> antipodes, gapstates;
 uint8_t p[N];
 while(head<tail){int r=q[head++],d=dist[r]; shell[d]++; maxd=max(maxd,d);
  unrank(r,p);
  int sum=0;
  for(int i=0;i<10;i++){
   int dest=p[i];int a=i%5,b=dest%5;
   int h=abs(a-b);h=min(h,5-h);
   sum+=h+(i/5!=dest/5);
  }
  int bound=(sum+1)/2; // ceiling of half the total displacement
  int gap=d-bound;
  if(gap<0){cerr<<"lower bound violated "<<r<<endl;return 1;}
  if(gap>maxgap){maxgap=gap;gapmaxcount=0;gapstates.clear();}
  if(gap==maxgap){gapmaxcount++;gapstates.push_back(r);}
  for(auto [a,b]:edges){swap(p[a],p[b]);int rr=rankp(p);swap(p[a],p[b]);
   if(dist[rr]==255){dist[rr]=d+1;q[tail++]=rr;}
  }
 }
 for(int i=0;i<SZ;i++)if(dist[i]==maxd)antipodes.push_back(i);
 cout<<"reached="<<tail<<" edges="<<edges.size()<<" diameter="<<maxd<<" shell=";
 for(int d=0;d<=maxd;d++)cout<<(d?",":"")<<shell[d];
 cout<<"\nantipodes="<<antipodes.size()<<" maxgap="<<maxgap<<" gapmaxcount="<<gapmaxcount<<"\n";
 for(size_t i=0;i<min((size_t)20,antipodes.size());i++){unrank(antipodes[i],p);cout<<"ANT "<<antipodes[i]<<" ";for(int k=0;k<10;k++)cout<<int(p[k]);cout<<"\n";}
 for(size_t i=0;i<min((size_t)12,gapstates.size());i++){unrank(gapstates[i],p);cout<<"GAP "<<gapstates[i]<<" ";for(int k=0;k<10;k++)cout<<int(p[k]);cout<<"\n";}
 // Check total state count
 long long total=0; for(int d=0;d<=maxd;d++)total+=shell[d];if(total!=SZ)abort();
}
