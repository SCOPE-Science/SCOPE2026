#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
using namespace std;
// Independent enumeration as multiset permutations. Every rank-7 transformation
// with omitted image 0 has one doubled image d=1..7; its output multiset
// contains d twice and every other number 1..7 once.
int main(){
 int tr[256];for(int s=0;s<256;s++)tr[s]=((s<<1)&255)|(s>>7);
 int triple[56], nt=0;
 for(int s=1;s<256;s++)if(__builtin_popcount((unsigned)s)==3)triple[nt++]=s;
 map<int,long long> hist;long long total=0,non=0;
 int highest=-1,extcount=0;array<int,8> extremal{};
 int move[256];int seen[256]={};int q[256],epoch=0;
 for(int repeated=1; repeated<=7;repeated++){
   array<int,8> b{};
   int k=0;
   for(int v=1;v<=7;v++)b[k++]=v;
   b[7]=repeated;
   sort(b.begin(),b.end());
   do {
     move[0]=0;
     for(int mask=1;mask<256;mask++){
       int i=__builtin_ctz((unsigned)mask);
       move[mask]=move[mask&(mask-1)]|(1<<b[i]);
     }
     bool bad=false;int worst=0;
     for(int index=0;index<56;index++){
       int start=triple[index],lo=0,hi=0,ans=-1;
       ++epoch;seen[start]=epoch;q[hi++]=start;
       int d[256];d[start]=0;
       while(lo<hi){int s=q[lo++];if((s&(s-1))==0){ans=d[s];break;}
         int u=tr[s],v=move[s];
         if(seen[u]!=epoch){seen[u]=epoch;d[u]=d[s]+1;q[hi++]=u;}
         if(seen[v]!=epoch){seen[v]=epoch;d[v]=d[s]+1;q[hi++]=v;}
       }
       if(ans<0){bad=true;break;}
       worst=max(worst,ans);
     }
     if(bad)non++;
     else {hist[worst]++;if(worst>highest){highest=worst;extcount=0;extremal=b;}if(worst==highest)extcount++;}
     total++;
   }while(next_permutation(b.begin(),b.end()));
 }
 cout<<"TOTAL "<<total<<" NON "<<non<<" MAX "<<highest<<" EXTREMA "<<extcount<<"\n";
 cout<<"TRIPLE_HIST ";for(auto [x,y]:hist)cout<<x<<":"<<y<<" ";cout<<"\n";
 cout<<"EXTREMAL ";for(auto x:extremal)cout<<x;cout<<"\n";
}
