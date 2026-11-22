#include <bits/stdc++.h>
using namespace std;
long long choose(int n,int k){ if(k<0||k>n)return 0; long long v=1;for(int i=1;i<=k;i++) v=v*(n-i+1)/i;return v; }
int main(){
 for(int n=4;n<=8;n++){
  vector<pair<int,int>> E;for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)E.push_back({a,b});
  vector<uint64_t> H;
  for(int a=0;a<n;a++){uint64_t mask=0;for(int i=0;i<(int)E.size();i++)if(E[i].first==a||E[i].second==a)mask|=1ULL<<i; H.push_back(mask);}
  for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++){
   uint64_t mask=0;for(int i=0;i<(int)E.size();i++){auto [u,v]=E[i];if((u==a||u==b||u==c)&&(v==a||v==b||v==c))mask|=1ULL<<i;}H.push_back(mask);
  }
  assert((long long)H.size()==n+choose(n,3));
  vector<long long> count(5,0);
  int m=E.size();
  for(int k=0;k<=4;k++){
   vector<int> ids(k); iota(ids.begin(),ids.end(),0);
   bool done=false;
   while(!done){
    unsigned int traces=0;
    for(uint64_t mask:H){int pat=0;for(int j=0;j<k;j++)pat|=((mask>>ids[j])&1ULL)<<j;traces|=(1U<<pat);}
    bool all=__builtin_popcount(traces)==(1<<k);
    bool structural=k<=3;
    for(int i=0;i<k;i++)for(int j=i+1;j<k;j++){
     auto [a,b]=E[ids[i]];auto [c,d]=E[ids[j]];
     if(a!=c&&a!=d&&b!=c&&b!=d)structural=false;
    }
    if(all!=structural){cerr<<"mismatch at n="<<n<<" k="<<k<<"\n";return 2;}
    count[k]+=all;
    if(k==0)break;
    int idx=k-1;
    while(idx>=0&&ids[idx]==m-k+idx)idx--;
    if(idx<0) done=true;else{ids[idx]++;for(int j=idx+1;j<k;j++)ids[j]=ids[j-1]+1;}
   }
  }
  vector<long long> expected={1,choose(n,2),n*choose(n-1,2),n*choose(n-1,3)+choose(n,3),0};
  if(count!=expected) return 3;
  cout<<"n="<<n<<" concepts="<<H.size()<<" shattered=";
  for(auto v:count)cout<<v<<",";
  cout<<" OK\n";
 }
 cout<<"VERIFY_OK\n";
}
