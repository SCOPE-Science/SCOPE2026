#include <array>
#include <vector>
#include <queue>
#include <iostream>
#include <cstdint>
#include <functional>
using namespace std;
using U=uint32_t;
int main(){
 const int n=18; array<U,n> neigh{};
 for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int m=0;m<3;m++)for(int t=0;t<3;t++)if(y==(m*x+t)%3){int i=3*x+y,j=9+3*m+t;neigh[i]|=U(1)<<j;neigh[j]|=U(1)<<i;} 
 int orig[n][n];for(int a=0;a<n;a++){
    for(int b=0;b<n;b++)orig[a][b]=100;
    queue<int>q;q.push(a);orig[a][a]=0;
    while(!q.empty()){int v=q.front();q.pop();U x=neigh[v];while(x){int w=__builtin_ctz(x);x&=x-1;if(orig[a][w]>orig[a][v]+1){orig[a][w]=orig[a][v]+1;q.push(w);}}}
 }
 auto distBlocked=[&](int src,int dst,U blocked){
  queue<int>q;int ds[n];for(int a=0;a<n;a++)ds[a]=100;ds[src]=0;q.push(src);
  while(!q.empty()){int a=q.front();q.pop();U x=neigh[a]&~blocked;while(x){int b=__builtin_ctz(x);x&=x-1;if(ds[b]==100){ds[b]=ds[a]+1;if(b==dst)return ds[b];q.push(b);}}}
  return 100;
 };
 auto visible=[&](U set){
  U x=set;while(x){int i=__builtin_ctz(x);x&=x-1;U y=x;while(y){int j=__builtin_ctz(y);y&=y-1;if(orig[i][j]>1&&distBlocked(i,j,set&~((U(1)<<i)|(U(1)<<j)))!=orig[i][j])return false;}}
  return true;
 };
 const U full=(U(1)<<n)-1;
 vector<unsigned char> seen(full+1,0),good(full+1,0);good[0]=seen[0]=1;
 for(U s=0;s<=full;s++) if(good[s]){
   U remains=full&~s;
   while(remains){U b=remains&(-remains);remains-=b;U t=s|b;
     if(!seen[t]){seen[t]=1;good[t]=visible(t);}
   }
 }
 long long c[21]={},f[21]={};U goodcount=0;
 for(U s=0;s<=full;s++)if(good[s]){int k=__builtin_popcount(s);c[k]++;goodcount++;
   bool facet=true;U remains=full&~s;while(remains){U b=remains&(-remains);remains-=b;if(good[s|b]){facet=false;break;}}
   if(facet)f[k]++;
 }
 cout<<"independent BFS good="<<goodcount<<"\nP=";
 for(int k=0;k<=n;k++) if(c[k])cout<<k<<":"<<c[k]<<",";
 cout<<"\nF=";for(int k=0;k<=n;k++)if(f[k])cout<<k<<":"<<f[k]<<",";
 cout<<"\n";
 unsigned long long h=1469598103934665603ull;for(U s=0;s<=full;s++){h^=good[s];h*=1099511628211ull;}cout<<"hash="<<hex<<h<<dec<<"\n";
 return 0;
}
