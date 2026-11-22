#include <bits/stdc++.h>
using namespace std;
using U=__uint128_t;
const int Q=81;
int dg[81][4], adds[81][81], negs[81], muls[81][81];
U bitmask[81], ALL=((U)1<<81)-1;
int enc(int a[4]) {int r=0,t=1;for(int i=0;i<4;i++){r+=a[i]*t;t*=3;}return r;}
void init(){
for(int x=0;x<81;x++){int t=x;for(int j=0;j<4;j++){dg[x][j]=t%3;t/=3;}}
for(int x=0;x<81;x++){
 int tmp[4];for(int j=0;j<4;j++)tmp[j]=(3-dg[x][j])%3;negs[x]=enc(tmp);
 for(int y=0;y<81;y++){
  int a[4];for(int j=0;j<4;j++)a[j]=(dg[x][j]+dg[y][j])%3;adds[x][y]=enc(a);
  int b[7]={};for(int i=0;i<4;i++)for(int j=0;j<4;j++)b[i+j]=(b[i+j]+dg[x][i]*dg[y][j])%3;
  // t^4+t+2=0, hence t^4=2*t+1
  for(int z=6;z>=4;z--){int c=b[z];b[z]=0;b[z-4]=(b[z-4]+c)%3;b[z-3]=(b[z-3]+2*c)%3;}
  muls[x][y]=enc(b);
 }
}
 bool squares[81]={};for(int i=1;i<81;i++)squares[muls[i][i]]=true;
 int ct=0;for(int i=0;i<81;i++)ct+=squares[i];assert(ct==40);
 for(int y=0;y<81;y++){U mm=0;for(int v=0;v<81;v++)if(squares[adds[y][negs[v]]])mm|=((U)1<<v);bitmask[y]=mm; assert(__builtin_popcountll((uint64_t)mm)+__builtin_popcountll((uint64_t)(mm>>64))==40);}
}
static uint64_t trial=0;
inline bool shattered(int* s,int k){
 U states[64]; states[0]=ALL;int n=1;
 for(int i=0;i<k;i++){
  U m=bitmask[s[i]],notm=ALL^m;
  for(int j=0;j<n;j++){
    U x=states[j]; U a=x&m,b=x&notm;
    if(!a||!b)return false;
    states[j]=a;states[n+j]=b;
  }
  n<<=1;
 }
 return true;
}
int main(int argc,char** argv){init();cerr<<"verified field arithmetic\n";int maxk=argc>1?atoi(argv[1]):6;int s[6]={0};
for(int k=0;k<=maxk;k++){
 unsigned long long count=0,passed=0;
 if(!k){cout<<"k 0 normalized 1 shattered 1 all 1\n";continue;}
 function<void(int,int)> dfs=[&](int pos,int start){
  if(pos==k){count++;if(shattered(s,k)){passed++; if(k==6 && passed<=15){cerr<<"seed ";for(int i=0;i<k;i++)cerr<<s[i]<<' ';cerr<<'\n';}}return;}
  for(int v=start;v<81;v++){s[pos]=v;dfs(pos+1,v+1);}
 };dfs(1,1);
 cout<<"k "<<k<<" normalized "<<count<<" shattered "<<passed<<" all "<<passed*81/k<<"\n"<<flush;
}
}
