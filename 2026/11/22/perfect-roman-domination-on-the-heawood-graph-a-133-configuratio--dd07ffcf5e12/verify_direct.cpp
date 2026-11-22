// Direct exhaustive verification of perfect Roman labellings on Fano incidence graph.
#include <array>
#include <iostream>
#include <cstdint>
#include <cassert>
using namespace std;
int main(){
  int adj[14][14]={};
  for(int j=0;j<7;j++)for(int p:{j,(j+1)%7,(j+3)%7}) adj[p][7+j]=adj[7+j][p]=1;
  long long poly[29]={};long long types[8][8]={};long long valid=0;
  int f[14];
  const int N=4782969; // 3^14
  for(int code=0;code<N;code++){
    int t=code,w=0,p=0,l=0;
    for(int v=0;v<14;v++){f[v]=t%3;t/=3;w+=f[v];if(f[v]==2){if(v<7)p++;else l++;}}
    bool ok=true;
    for(int v=0;v<14&&ok;v++)if(f[v]==0){int x=0;for(int u=0;u<14;u++)if(adj[v][u]&&f[u]==2)x++;if(x!=1)ok=false;}
    if(ok){poly[w]++;valid++;if(w==10)types[p][l]++;}
  }
  const long long expect[]={0,0,0,0,0,0,0,0,0,0,133,1064,4578,12530,23913,34664,40803,40138,33607,24360,15813,9312,4977,2422,1043,364,91,14,1};
  for(int k=0;k<=28;k++){if(poly[k]!=expect[k]){cerr<<"mismatch k="<<k<<" got="<<poly[k]<<" expect="<<expect[k]<<endl;return 1;}}
  if(types[1][1]!=28 || types[2][1]!=42 || types[1][2]!=42 || types[2][2]!=21) return 2;
  int tot=0;for(int a=0;a<8;a++)for(int b=0;b<8;b++)tot+=types[a][b];if(tot!=133)return 3;
  cout<<"PRD_DIRECT_EXHAUSTIVE_OK labelings="<<valid<<" min_weight=10 min_count="<<tot<<"\n";
  for(int k=0;k<=28;k++)if(poly[k])cout<<k<<":"<<poly[k]<<(k==28?'\n':' ');
  return 0;
}
