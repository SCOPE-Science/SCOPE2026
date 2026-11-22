// Exhaustive check for each permutation schedule on C_n, 3 <= n <= 8.
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;
int sweep(int x,int n,const vector<int>&order){
 for(int v:order){
  int l=(v+n-1)%n,r=(v+1)%n;
  int c=(x>>v)&1, a=(x>>l)&1,b=(x>>r)&1;
  int nc = c ? (a&b) : (a|b);
  x=(x&~(1<<v))|(nc<<v);
 }
 return x;
}
int main(){
 long long schedules=0, states=0;
 for(int n=3;n<=8;n++){
  vector<int> order(n);iota(order.begin(),order.end(),0);
  long long c=0;
  do{
   vector<int>pos(n);
   for(int i=0;i<n;i++)pos[order[i]]=i;
   int a=0;
   for(int i=0;i<n;i++)a+=pos[i]<pos[(i+1)%n];
   int b=n-a, N=1<<n;
   vector<int>f(N),last(N,-1),index(N,-1),which(N,-1),period(N,-1),entry(N,-1);
   for(int x=0;x<N;x++)f[x]=sweep(x,n,order);
   map<int,int>periodic;
   for(int x=0;x<N;x++){
    if(period[x]>=0)continue;
    vector<int>path;
    int u=x;
    while(period[u]<0 && index[u]<0){index[u]=(int)path.size();path.push_back(u);u=f[u];}
    if(period[u]<0){
     int start=index[u], len=(int)path.size()-start;
     for(int j=start;j<(int)path.size();j++){int y=path[j];period[y]=len;entry[y]=0;}
     for(int j=start-1;j>=0;j--){int y=path[j];period[y]=len;entry[y]=entry[f[y]]+1;}
    }else{
     for(int j=(int)path.size()-1;j>=0;j--){int y=path[j];period[y]=period[f[y]];entry[y]=entry[f[y]]+1;}
    }
    for(int y:path)index[y]=-1;
   }
   int rec=0;
   for(int x=0;x<N;x++){
    int wA=0,wB=0;
    for(int i=0;i<n;i++){
     if(((x>>i)^(x>>((i+1)%n)))&1){
      if(pos[i]<pos[(i+1)%n])wA++;
      else wB++;
     }
    }
    bool isrec=(wA==0||wB==0);
    if((entry[x]==0)!=isrec){cerr<<"Recurrent mismatch n="<<n<<" x="<<x<<"\n";return 1;}
    if(entry[x]==0){periodic[period[x]]++;rec++;}
   }
   if(rec!=(1<<a)+(1<<b)-2){cerr<<"Count mismatch";return 2;}
   for(int d=1;d<=n;d++){
    int got=0;
    for(auto [p,count]:periodic)if(d%p==0)got+=count;
    int want=(1<<gcd(a,d))+(1<<gcd(b,d))-2;
    if(got!=want){cerr<<"Period mismatch n="<<n<<" a="<<a<<" b="<<b<<" d="<<d<<" got="<<got<<" want="<<want<<"\n";return 3;}
   }
   c++;schedules++;states+=N;
  }while(next_permutation(order.begin(),order.end()));
  cout<<"n="<<n<<" schedules="<<c<<" passed\n";
 }
 cout<<"PASS all_orders schedules="<<schedules<<" state_schedule_pairs="<<states<<"\n";
}
