#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
constexpr int W=4,H=5,V=20,NN=(1<<V),MASK=NN-1;
int advance(int s){int result=0;for(int x=0;x<W;x++)for(int y=0;y<H;y++){
 int i=x*H+y;
 int n=(s>>(((x+W-1)%W)*H+y))&1;
 int e=(s>>(((x+1)%W)*H+y))&1;
 int u=(s>>(x*H+(y+H-1)%H))&1;
 int d=(s>>(x*H+(y+1)%H))&1;
 int count=n+e+u+d;
 int vote=(count>=3)|| (count==2 && ((s>>i)&1));
 result |= vote<<i;
 }return result;}
int transform(int s,int shiftx,int shifty,int reflectionx,int reflectiony,int complement){
 int t=0;for(int x=0;x<W;x++)for(int y=0;y<H;y++){
 int xx=(shiftx+(reflectionx?W-x:x))%W;
 int yy=(shifty+(reflectiony?H-y:y))%H;
 if((s>>(x*H+y))&1) t |= 1<<(xx*H+yy);
 }return complement ? (t^MASK):t;
}
int main(){
 vector<int>target(NN);for(int s=0;s<NN;s++)target[s]=advance(s);
 vector<int>seen(NN,0),root(NN,-1),per(NN,-1),distance(NN,-1),reps;map<int,int>periodcycle;
 vector<int>stack;stack.reserve(1000);
 for(int initial=0;initial<NN;initial++){
  if(seen[initial])continue;
  stack.clear();int cursor=initial;
  while(!seen[cursor]){seen[cursor]=1;stack.push_back(cursor);cursor=target[cursor];}
  if(seen[cursor]==1){int index=0;while(stack[index]!=cursor)++index;
    int id=(int)reps.size(),len=(int)stack.size()-index;
    reps.push_back(cursor);periodcycle[len]++;
    for(int k=index;k<(int)stack.size();k++){int s=stack[k];root[s]=id;per[s]=len;distance[s]=0;}
  }
  for(int k=(int)stack.size()-1;k>=0;k--){int s=stack[k]; if(root[s]<0){int next=target[s];root[s]=root[next];per[s]=per[next];distance[s]=distance[next]+1;}seen[s]=2;}
 }
 map<int,int>orbits=periodcycle,basins,shell;map<pair<int,int>,int>cross;
 int maxdistance=0;
 for(int s=0;s<NN;s++){assert(distance[s]>=0&&per[s]>0);basins[per[s]]++;shell[distance[s]]++;cross[{per[s],distance[s]}]++;maxdistance=max(maxdistance,distance[s]);}
 map<int,long long>burnside;
 for(int flip=0;flip<2;flip++)for(int rx=0;rx<2;rx++)for(int ry=0;ry<2;ry++)for(int dx=0;dx<W;dx++)for(int dy=0;dy<H;dy++){
  map<int,long long>fixed;
  for(int s:reps){int t=transform(s,dx,dy,rx,ry,flip);if(root[t]==root[s])fixed[per[s]]++;}
  for(auto [p,num]:fixed)burnside[p]+=num;
 }
 cout<<"all "<<NN<<" cycles "<<reps.size()<<" maximum_entry "<<maxdistance<<"\n";
 cout<<"orbits";for(auto [p,n]:orbits)cout<<" "<<p<<":"<<n;cout<<"\n";
 cout<<"basins";for(auto [p,n]:basins)cout<<" "<<p<<":"<<n;cout<<"\n";
 cout<<"entry";for(auto [d,n]:shell)cout<<" "<<d<<":"<<n;cout<<"\n";
 cout<<"period_and_entry";for(auto [key,num]:cross)cout<<" "<<key.first<<","<<key.second<<":"<<num;cout<<"\n";
 cout<<"Burnside_sum";for(auto [p,n]:burnside){assert(n%160==0);cout<<" "<<p<<":"<<n<<"/160="<<n/160;}cout<<"\n";
 // Check periodic-point characterization without assuming the maximal orbit length a priori.
 int fixed=0,two=0;for(int s=0;s<NN;s++){int a=target[s],b=target[a];if(a==s)fixed++;else if(b==s)two++;}
 cout<<"direct_fixed "<<fixed<<" direct_two_cycle_states "<<two<<"\n";
}
