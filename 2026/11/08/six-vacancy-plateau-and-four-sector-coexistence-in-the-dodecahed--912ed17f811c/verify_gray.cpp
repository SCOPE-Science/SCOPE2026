#include <bits/stdc++.h>
using namespace std;
struct Cell {int e=999; unsigned long long count=0;};
int main(){
 const int N=20;
 const int ed[30][2]={{0,1},{0,10},{10,12},{1,2},{1,11},{11,13},{2,3},{2,12},{12,14},{3,4},{3,13},{13,15},{4,5},{4,14},{14,16},{5,6},{5,15},{15,17},{6,7},{6,16},{16,18},{7,8},{7,17},{17,19},{8,9},{8,18},{18,10},{9,0},{9,19},{19,11}};
 int adj[N][3],deg[N]={};
 for(auto &e:ed){int u=e[0],v=e[1];adj[u][deg[u]++]=v;adj[v][deg[v]++]=u;}
 for(int i=0;i<N;i++)if(deg[i]!=3){cerr<<"ERROR";return 1;}
 Cell a[21][41];
 int digit[N]={},dir[N],s[N];for(int i=0;i<N;i++){dir[i]=1;s[i]=-1;}
 int E=30,M=-20,Q=20;
 auto record=[&](){auto &c=a[Q][M+20];if(E<c.e){c.e=E;c.count=1;}else if(E==c.e)c.count++;};
 unsigned long long c=0;record();c++;
 while(1){int i=0;for(;i<N;i++)if(digit[i]+dir[i]>=0 && digit[i]+dir[i]<=2)break;if(i==N)break;
  for(int j=0;j<i;j++)dir[j]=-dir[j];
  int old=s[i],nw=digit[i]+dir[i]-1;
  E+=(nw-old)*(s[adj[i][0]]+s[adj[i][1]]+s[adj[i][2]]);
  M+=nw-old;Q+=nw*nw-old*old;s[i]=nw;digit[i]+=dir[i];record();c++;
 }
 cerr<<"EXHAUSTED "<<c<<" expected 3486784401\n";
 for(int q=0;q<=20;q++)for(int m=-20;m<=20;m++){auto &x=a[q][m+20];if(x.count)cout<<q<<","<<m<<","<<x.e<<","<<x.count<<"\n";}
 return (c==3486784401ULL)?0:1;
}
