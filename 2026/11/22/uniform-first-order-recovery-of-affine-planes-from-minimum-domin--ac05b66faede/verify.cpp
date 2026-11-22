// Independent finite-prime-field checks of affine incidence domination and shattering.
#include <bits/stdc++.h>
using namespace std;
using U=unsigned long long;
int main(){
 for(int q:{2,3,5,7}){
  int np=q*q,nl=q*(q+1),n=np+nl;
  vector<vector<int>> line(nl);
  for(int d=0;d<=q;d++)for(int b=0;b<q;b++){
   int j=d*q+b;
   for(int x=0;x<q;x++)for(int y=0;y<q;y++)
    if((d==q?x==b:((y+d*x)%q)==b))line[j].push_back(x*q+y);
   assert((int)line[j].size()==q);
  }
  vector<vector<int>> family(nl,vector<int>(n));
  for(int d=0;d<=q;d++)for(int b=0;b<q;b++){
   int h=d*q+b;
   for(int p:line[h])family[h][p]=1;
   for(int c=0;c<q;c++)if(c!=b)family[h][np+d*q+c]=1;
  }
  int poly[]={0,0,0,0};
  for(int k=0;k<=3;k++){
   vector<int> ind(k);
   auto rec=[&](auto&& self,int dep,int start)->void{
    if(dep==k){
      bool seen[8]={};int cnt=0;
      for(auto const& h:family){int v=0;for(int i=0;i<k;i++)v|=h[ind[i]]<<i;
       if(!seen[v]){seen[v]=true;cnt++;}}
      if(cnt==(1<<k))poly[k]++;
      return;
    }
    for(int i=start;i<=n-(k-dep);i++){ind[dep]=i;self(self,dep+1,i+1);}
   };
   rec(rec,0,0);
  }
  long long expected2=(q==2?6:1LL*q*(q*q-1)*(3*q+1)/2);
  assert(poly[0]==1&&poly[1]==n&&poly[2]==expected2&&poly[3]==0);
  vector<vector<char>> R(n,vector<char>(n,0));
  for(int x=0;x<n;x++)for(int y=x+1;y<n;y++){
   int bits=0;for(const auto& h:family)bits|=1<<(h[x]*2+h[y]);
   if(bits==15)R[x][y]=R[y][x]=1;
  }
  for(int v=0;v<n;v++){
   bool ispoint=true;
   for(int x=0;x<n;x++)if(x!=v&&!R[v][x])
    for(int y=x+1;y<n;y++)if(y!=v&&!R[v][y]&&R[x][y])ispoint=false;
   assert(ispoint==(v<np));
  }
  if(q>=3)for(int p=0;p<np;p++)for(int j=0;j<nl;j++){
   bool incident=find(line[j].begin(),line[j].end(),p)!=line[j].end();
   assert(R[p][np+j]==!incident);
  }
  if(q<=3){
   vector<U> dom(n,0);assert(n<=21);
   for(int i=0;i<n;i++)dom[i]|=1ULL<<i;
   for(int j=0;j<nl;j++)for(int p:line[j]){
    dom[p]|=1ULL<<(np+j);dom[np+j]|=1ULL<<p;
   }
   U all=(1ULL<<n)-1;int cnt=0;
   for(U S=0;S<=all;S++){
    if(__builtin_popcountll(S)!=2*q-1)continue;
    U cov=0;for(int i=0;i<n;i++)if((S>>i)&1)cov|=dom[i];
    if(cov==all){cnt++;bool found=false;for(int j=0;j<nl;j++){
      U h=0;for(int i=0;i<n;i++)if(family[j][i])h|=1ULL<<i;
      if(S==h)found=true;
     }assert(found);}
   }
   assert(cnt==nl);
  }
  cout<<"q="<<q<<" families="<<nl<<" support_coeffs="<<poly[0]<<","<<poly[1]<<","<<poly[2]<<","<<poly[3]<<" recovered="<<(q>=3?"yes":"boundary")<<"\n";
 }
}
