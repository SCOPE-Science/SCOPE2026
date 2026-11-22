// Exhaustive, independently coded three-step Greenberg-Hastings simulation on 3 by n open rectangular strips.
#include <iostream>
#include <vector>
#include <cassert>
using namespace std;
int main(){
 const long long expected[]={0,0,6,84,774};
 for(int n=2;n<=4;n++){
  int m=3*n; long long all=1, cycles=0, rest=0;
  for(int j=0;j<m;j++)all*=3;
  vector<vector<int>> adj(m);
  for(int x=0;x<n;x++)for(int y=0;y<3;y++){
   int i=3*x+y;
   if(x>0)adj[i].push_back(i-3);
   if(x<n-1)adj[i].push_back(i+3);
   if(y>0)adj[i].push_back(i-1);
   if(y<2)adj[i].push_back(i+1);
  }
  vector<int> c(m),d(m),orig(m);
  for(long long s=0;s<all;s++){
   auto z=s;
   for(int i=0;i<m;i++){c[i]=z%3;z/=3;orig[i]=c[i];}
   bool fixed=true;
   for(int t=0;t<3;t++){
    for(int i=0;i<m;i++){
     if(c[i]==1)d[i]=2;
     else if(c[i]==2)d[i]=0;
     else{
      d[i]=0;
      for(int v:adj[i])if(c[v]==1){d[i]=1;break;}
     }
    }
    c.swap(d);
    if(t==0)fixed=(c==orig);
   }
   if(c==orig){if(fixed)rest++;else cycles++;}
  }
  cout<<"n="<<n<<" states="<<all<<" primitive-three-states="<<cycles<<" fixed="<<rest<<"\n";
  assert(cycles==expected[n]&&rest==1);
 }
 cout<<"Independent exhaustive check PASSED\n";
}
