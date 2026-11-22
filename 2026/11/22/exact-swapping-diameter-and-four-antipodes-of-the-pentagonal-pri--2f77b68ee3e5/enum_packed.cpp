#include <bits/stdc++.h>
using namespace std;
int main(){
 // Independently encode each placement in 40 bits (four bits per vertex), and use a hash dictionary.
 vector<pair<int,int>> E;
 for(int i=0;i<5;++i){E.push_back({i,(i+1)%5});E.push_back({i+5,(i+1)%5+5});E.push_back({i,i+5});}
 uint64_t start=0;for(int i=0;i<10;++i)start|=uint64_t(i)<<(4*i);
 unordered_map<uint64_t,uint8_t> dist;
 dist.max_load_factor(0.75);dist.reserve(4000000);
 vector<uint64_t> q;q.reserve(3628800);q.push_back(start);dist[start]=0;
 size_t h=0;vector<int64_t> shells(25,0), gapcnt(25,0);vector<uint64_t> far, gapfar;
 int maxd=0,maxgap=-1;
 int gd[10][10];for(int i=0;i<10;++i)for(int j=0;j<10;++j){int x=abs(i%5-j%5); gd[i][j]=min(x,5-x)+(i/5!=j/5);}
 while(h<q.size()){
  uint64_t s=q[h++];uint8_t d=dist.find(s)->second;shells[d]++;
  if(d>maxd){maxd=d;far.clear();}if(d==maxd)far.push_back(s);
  int L=0;for(int i=0;i<10;++i)L+=gd[i][(s>>(4*i))&15];int gap=d-(L+1)/2;
  if(gap<0){cerr<<"lowerbound bug";exit(2);}
  if(gap>maxgap){maxgap=gap;gapfar.clear();}
  if(gap==maxgap)gapfar.push_back(s);
  gapcnt[gap]++;
  for(auto [a,b]:E){
   uint64_t x=(s>>(a*4))&15,y=(s>>(b*4))&15;
   uint64_t nxt=s^((x^y)<<(a*4))^((x^y)<<(b*4));
   if(dist.emplace(nxt,d+1).second)q.push_back(nxt);
  }
 }
 sort(far.begin(),far.end());
 cout<<"num="<<q.size()<<" diameter="<<maxd<<" antipodes="<<far.size()<<" maxgap="<<maxgap<<" gapcount="<<gapfar.size()<<"\n";
 for(int i=0;i<=maxd;++i)cout<<(i?",":"")<<shells[i];cout<<"\n";
 for(auto s:far){cout<<"FAR ";for(int j=0;j<10;++j)cout<<((s>>(4*j))&15);cout<<"\n";}
}
