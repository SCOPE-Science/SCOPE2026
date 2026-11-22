#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
U N[50],C[50], ALL=(1ULL<<50)-1;
int arr[7];
int observe(U s){
 U o=s;
 while(s){int i=__builtin_ctzll(s);s&=s-1;o|=N[i];}
 int rounds=1;
 while(o!=ALL){
   U t=o, a=o;
   while(t){int i=__builtin_ctzll(t);t&=t-1;U u=N[i]&~o;if(u && !(u&(u-1)))a|=u;}
   if(a==o)return 0;
   o=a;rounds++;
 }
 return rounds;
}
int main(){
 for(int h=0;h<5;h++)for(int j=0;j<5;j++){
  int p=5*h+j;
  N[p]|=1ULL<<(5*h+(j+1)%5);N[p]|=1ULL<<(5*h+(j+4)%5);
  for(int k=0;k<5;k++){int q=25+5*k+(h*k+j)%5;N[p]|=1ULL<<q;N[q]|=1ULL<<p;}
  int q=25+5*h+j;
  N[q]|=1ULL<<(25+5*h+(j+2)%5);N[q]|=1ULL<<(25+5*h+(j+3)%5);
 }
 for(int i=0;i<50;i++) { assert(__builtin_popcountll(N[i])==7); for(int j=0;j<50;j++)assert(((N[i]>>j)&1)==((N[j]>>i)&1)); }
 for(int k=1;k<=6;k++){
  map<pair<int,int>,uint64_t> bins;
  uint64_t candidates=0,success=0; U exemplar=0;
  auto t=chrono::steady_clock::now();
  function<void(int,int,U)> go=[&](int d,int start,U mask){
   if(d==k){
    candidates++;
    int r=observe(mask);
    if(r){
     success++; if(!exemplar)exemplar=mask;
     int e=0;
     U x=mask;while(x){int i=__builtin_ctzll(x);x&=x-1;e+=__builtin_popcountll(N[i]&x);}
     bins[{r,e}]++;
    }
    return;
   }
   for(int i=start;i<=50-(k-d);i++)go(d+1,i+1,mask|(1ULL<<i));
  };
  go(0,0,0);
  cerr<<"size="<<k<<" candidates="<<candidates<<" good="<<success<<" seconds="<<chrono::duration<double>(chrono::steady_clock::now()-t).count()<<" exemplar="<<exemplar<<"\n";
  for(auto [ke,v]:bins)cout<<k<<" "<<ke.first<<" "<<ke.second<<" "<<v<<"\n";
  cout.flush();
  if(success)break;
 }
}
