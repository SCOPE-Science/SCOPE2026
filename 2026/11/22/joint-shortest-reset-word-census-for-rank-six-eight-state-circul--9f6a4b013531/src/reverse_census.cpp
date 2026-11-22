// Independent reverse breadth-first exact census of shortest synchronizing words.
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
using namespace std;
using u64=uint64_t;
int main(){
 constexpr int M=256;
 int rot[M];for(int s=0;s<M;s++)rot[s]=((s*2)&255)|(s>>7);
 map<pair<int,u64>,u64> joint;
 map<u64,u64> wordcounts;
 u64 classes=0,notreset=0;
 u64 peak=0,numpeak=0;int peaklen=-1;u64 peakmap=0;
 int b[8],image[M],predhead[M],predsrc[510],prednext[510];
 int dd[M],queue[M];u64 cnt[M];
 for(u64 index=0; index < (1ull<<24); ++index){
  unsigned mask=0;
  for(int j=0;j<8;j++){b[j]=(index>>(3*j))&7;mask|=1u<<b[j];}
  if(__builtin_popcount(mask)!=6)continue;
  bool rep=true;
  for(int k=1;k<8&&rep;k++){
   u64 r=0;
   for(int j=0;j<8;j++){
    const int original=(j+8-k)%8;
    r|=(u64)((b[original]+k)%8)<<(3*j);
   }
   if(r<index)rep=false;
  }
  if(!rep)continue;
  ++classes;
  image[0]=0;
  for(int s=1;s<M;s++){
   const int bit=__builtin_ctz((unsigned)s);
   image[s]=image[s&(s-1)]|(1<<b[bit]);
  }
  fill(predhead,predhead+M,-1);
  int e=0;
  for(int s=1;s<M;s++){
   int target[2]={rot[s],image[s]};
   for(int c=0;c<2;c++){
    int y=target[c];predsrc[e]=s;prednext[e]=predhead[y];predhead[y]=e;e++;
   }
  }
  fill(dd,dd+M,-1); fill(cnt,cnt+M,0);
  int r=0,w=0;
  for(int j=0;j<8;j++){
   const int t=1<<j;
   dd[t]=0;cnt[t]=1;queue[w++]=t;
  }
  while(r<w){
    int y=queue[r++];
    for(int edge=predhead[y];edge!=-1;edge=prednext[edge]){
     int x=predsrc[edge];
     if(dd[x]<0){dd[x]=dd[y]+1;queue[w++]=x;}
     if(dd[x]==dd[y]+1){if(__builtin_add_overflow(cnt[x],cnt[y],&cnt[x])){cerr<<"OVERFLOW reverse "<<index<<"\n";return 2;}}
    }
  }
  int d=dd[255];u64 count=(d<0?0:cnt[255]);
  joint[{d,count}]++;wordcounts[count]++;
  if(d<0)notreset++;
  if(count>peak){peak=count;numpeak=1;peaklen=d;peakmap=index;}
  else if(count==peak){numpeak++;}
 }
 cout<<"classes "<<classes<<" nonreset "<<notreset<<" peak "<<peak<<" peak_count "<<numpeak<<" peak_length "<<peaklen<<" peak_encoding "<<peakmap<<"\n";
 cout<<"joint_groups "<<joint.size()<<" count_groups "<<wordcounts.size()<<"\n";
 for(auto const &p:joint) cout<<p.first.first<<","<<p.first.second<<","<<p.second<<"\n";
}
