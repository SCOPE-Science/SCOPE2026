// Exhaustive shortest synchronizing-word census for rank-six circular binary automata.
#include <bits/stdc++.h>
using namespace std;
using ull=unsigned long long;
struct Agg {ull count=0;};
int main(){
 const int FULL=255;
 int a[256];for(int s=0;s<256;s++)a[s]=((s<<1)&255)|(s>>7);
 int b[8],table[256],dist[256]; ull ways[256];
 unordered_map<ull,ull> tally;
 map<int,ull> thresholds; map<ull,ull> mults;
 ull classes=0,nonsync=0, wordsmax=0,maxcount=0;
 int highestL=0; vector<pair<ull,string>> extreme; 
 auto minrot=[&](ull x)->bool{
   for(int s=1;s<8;s++){
     ull y=0;
     for(int i=0;i<8;i++){
       // conjugate by shift s, new b[i]=b[(i-s)%8]+s
       int v=(int)((x>>(3*((i-s+8)&7)))&7);
       y|=(ull)((v+s)&7)<<(3*i);
     }
     if(y<x)return false;
   }
   return true;
 };
 for(ull x=0;x<(1ULL<<24);x++){
  int seen=0;
  for(int i=0;i<8;i++){b[i]=(x>>(3*i))&7;seen|=1<<b[i];}
  if(__builtin_popcount((unsigned)seen)!=6)continue;
  if(!minrot(x))continue;
  classes++;
  table[0]=0;
  for(int s=1;s<256;s++){int u=__builtin_ctz((unsigned)s);table[s]=table[s^(1<<u)]|(1<<b[u]);}
  fill(dist,dist+256,-1);fill(ways,ways+256,0);
  int queue[256],head=0,tail=0;queue[tail++]=255;dist[255]=0;ways[255]=1;
  int best=-1;
  while(head<tail){
    int s=queue[head++],depth=dist[s];
    if(best>=0&&depth>=best)continue;
    int next[2]={a[s],table[s]};
    for(int z:next){
      if(dist[z]<0){dist[z]=depth+1;queue[tail++]=z;}
      if(dist[z]==depth+1)ways[z]+=ways[s];
      if((z&(z-1))==0 && (best<0 || best>depth+1))best=depth+1;
    }
  }
  ull count=0;
  if(best<0){nonsync++;count=0;thresholds[-1]++;}
  else {
   for(int i=0;i<8;i++){int s=1<<i;if(dist[s]==best)count+=ways[s];}
   thresholds[best]++;highestL=max(highestL,best);
   if(count>wordsmax){wordsmax=count;maxcount=0;extreme.clear();}
   if(count==wordsmax){maxcount++;if(extreme.size()<15){ostringstream o;for(int i=0;i<8;i++)o<<b[i];extreme.emplace_back(count,o.str());}}
  }
  tally[((ull)(best+1)<<52)|count]++;
  mults[count]++;
 }
 cerr<<"classes "<<classes<<" nonsync "<<nonsync<<" largest shortest-word count "<<wordsmax<<" extremizer classes "<<maxcount<<" max length "<<highestL<<"\n";
 cout<<"{\"classes\":"<<classes<<",\"nonsync\":"<<nonsync<<",\"max_words\":"<<wordsmax<<",\"max_count\":"<<maxcount<<",\"max_threshold\":"<<highestL<<",\"thresholds\":[";
 bool first=true;
 for(auto [l,c]:thresholds){if(!first)cout<<",";first=false;cout<<"["<<l<<","<<c<<"]";}
 cout<<"],\"multiplicities\":[";first=true;
 for(auto [m,c]:mults){if(!first)cout<<",";first=false;cout<<"["<<m<<","<<c<<"]";}
 cout<<"],\"joint\":[";first=true;
 vector<pair<ull,ull>> v(tally.begin(),tally.end());sort(v.begin(),v.end());
 for(auto [key,c]:v){if(!first)cout<<",";first=false;cout<<"["<<int(key>>52)-1<<","<<(key&((1ULL<<52)-1))<<","<<c<<"]";}
 cout<<"],\"max_examples\":[";first=true;
 for(auto [m,s]:extreme){if(!first)cout<<",";first=false;cout<<"\""<<s<<"\"";}
 cout<<"]}\n";
}
