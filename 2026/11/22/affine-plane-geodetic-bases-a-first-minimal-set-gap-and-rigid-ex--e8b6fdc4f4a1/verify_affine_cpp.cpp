// Independent shortest-path geodetic census for prime affine planes of orders two and three.
// Builds the incidence matrix from affine equations, uses Floyd--Warshall,
// and computes all closed geodetic intervals from distances.
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <map>
using namespace std;
int main(){
 for(int q: {2,3}){
  int P=q*q,L=q*(q+1),N=P+L;
  vector<vector<int>> d(N,vector<int>(N,100));
  for(int i=0;i<N;i++)d[i][i]=0;
  for(int x=0;x<q;x++)for(int y=0;y<q;y++){
   int point=x*q+y;
   for(int m=0;m<=q;m++)for(int b=0;b<q;b++){
    bool incident=(m==q? x==b :y==(m*x+b)%q);
    if(incident){int li=P+m*q+b;d[point][li]=d[li][point]=1;}
   }
  }
  for(int k=0;k<N;k++)for(int i=0;i<N;i++)for(int j=0;j<N;j++)d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
  for(int i=0;i<N;i++)assert(*max_element(d[i].begin(),d[i].end())<100);
  vector<vector<unsigned long long>> I(N,vector<unsigned long long>(N));
  for(int i=0;i<N;i++)for(int j=0;j<N;j++)for(int k=0;k<N;k++)if(d[i][k]+d[k][j]==d[i][j])I[i][j]|=1ULL<<k;
  unsigned long long FULL=(1ULL<<N)-1;
  map<int,long long> byLines;
  long long minsets=0,plussets=0,nonclass=0;
  for(int k : {q,q+1}){
    vector<int> c(k);for(int i=0;i<k;i++)c[i]=i;
    do{
      unsigned long long mask=0;
      for(int i=0;i<k;i++)for(int j=i+1;j<k;j++)mask |=I[c[i]][c[j]];
      if(mask==FULL){
       int lc=0; for(int a:c)lc+=(a>=P);
       bool containsClass=false;
       for(int m=0;m<=q;m++){
         int cnt=0; for(int a:c)if(a>=P && (a-P)/q==m)cnt++;
         if(cnt==q)containsClass=true;
       }
       if(k==q){minsets++;assert(containsClass);}
       else {plussets++;byLines[lc]++;if(!containsClass)nonclass++;}
      }
      int i=k-1;
      while(i>=0 && c[i]==N-k+i)--i;
      if(i<0)break;
      c[i]++;for(int j=i+1;j<k;j++)c[j]=c[j-1]+1;
    }while(true);
  }
  assert(minsets==q+1);
  assert(plussets==2LL*(q+1)*q*q+(q==2?6:0));
  assert(nonclass==(q==2?6:0));
  cout<<"q="<<q<<" | minimum="<<minsets<<" | (q+1)-sets="<<plussets<<" | exceptional="<<nonclass<<" | by # lines:";
  for(auto [a,b]:byLines)cout<<" ("<<a<<","<<b<<")";
  cout<<"\n";
 }
}
