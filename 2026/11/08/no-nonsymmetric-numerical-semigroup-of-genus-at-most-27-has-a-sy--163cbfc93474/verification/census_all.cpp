#include <bits/stdc++.h>
using namespace std; using U=__uint128_t;
bool has(U bits,int x){return x>=0&&x<128&&((bits>>x)&1);}
struct Info{int m,F;vector<int> gen;};
Info inf(U gaps){
 int F=-1,m=1;for(int i=0;i<120;i++)if(has(gaps,i))F=i;
 while(has(gaps,m))m++;
 vector<int> gen;
 for(int x=m;x<=F+m+1;x++){
  if(has(gaps,x))continue;
  bool minimal=true;
  for(int y=m;y<=x/2;y++)if(!has(gaps,y)&&!has(gaps,x-y)){minimal=false;break;}
  if(minimal)gen.push_back(x);
 }
 return {m,F,gen};
}
bool squaresym(const Info& I){
 int m2=I.m*I.m;
 vector<int> gs;
 for(int x:I.gen)for(int y:I.gen)gs.push_back(x*y);
 sort(gs.begin(),gs.end());gs.erase(unique(gs.begin(),gs.end()),gs.end());
 vector<long long>d(m2,LLONG_MAX/4);d[0]=0;
 using P=pair<long long,int>; priority_queue<P,vector<P>,greater<P>>Q;Q.push({0,0});
 while(!Q.empty()){
  auto [w,r]=Q.top();Q.pop();if(w!=d[r])continue;
  for(int g:gs){int s=(r+g)%m2;long long v=w+g;if(v<d[s]){d[s]=v;Q.push({v,s});}}
 }
 long long sum=0,mx=0;for(long long x:d){sum+=x;mx=max(mx,x);}
 long long g=sum/m2-(m2-1)/2;
 return 2*g==mx-m2+1;
}
int main(int argc,char**argv){int maxgen=argc>1?atoi(argv[1]):30;vector<U> states={U(0)};
 for(int g=0;g<maxgen;g++){
  vector<U> next;long long non=0;
  for(U mask:states){Info I=inf(mask);if(g&&2*g!=I.F+1){++non;if(squaresym(I)){
    cout<<"FOUND genus="<<g<<" f="<<I.F<<" generators=";for(int x:I.gen)cout<<x<<",";cout<<" gaps=";for(int x=1;x<=I.F;x++)if(has(mask,x))cout<<x<<",";cout<<endl;return 0;
   }}
   for(int x:I.gen)if(x>I.F){if(x>=128){cerr<<"bitoverflow";return 1;}next.push_back(mask | (U(1)<<x));}
  }
  cerr<<"genus "<<g<<" n "<<states.size()<<" nonsym "<<non<<" children "<<next.size()<<endl;
  states.swap(next);
 }
}
