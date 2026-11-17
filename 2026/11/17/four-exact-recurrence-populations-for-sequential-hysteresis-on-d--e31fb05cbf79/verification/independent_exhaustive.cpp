// Independent labelled-state exhaustive checker for the double-star sweep.
// Each integer encodes the hub states at bits 0,1 and the a and b leaves next.
// This enumerates the full configuration graph; it does not use profile reduction.
#include <iostream>
#include <vector>
#include <array>
#include <queue>
#include <cassert>
#include <cstdint>
using namespace std;
static int sweep(int x,int a,int b){
  int n=a+b+2;
  int h=x&1,j=(x>>1)&1;
  int ka=0,kb=0;
  for(int i=0;i<a;i++)ka+=(x>>(2+i))&1;
  for(int i=0;i<b;i++)kb+=(x>>(2+a+i))&1;
  int H=(h+j+ka >= (h?3:1));
  int J=(j+H+kb >= (j?3:1));
  int y=H|(J<<1);
  for(int i=0;i<a;i++)y|=(H && !(x&(1<<(2+i))))<<(2+i);
  for(int i=0;i<b;i++)y|=(J && !(x&(1<<(2+a+i))))<<(2+a+i);
  assert(y >=0 && y < (1<<n));return y;
}
static long long T(int n){if(n<4)return 0;return (1LL<<n)-2LL*n-2;}
int main(){
  int pairs=0;
  for(int a=1;a<=9;a++)for(int b=1;b<=9;b++){
    if(a+b+2>17)continue;
    int N=1<<(a+b+2);
    vector<int> f(N),in(N,0);
    for(int x=0;x<N;x++){f[x]=sweep(x,a,b);in[f[x]]++;}
    queue<int> q;
    for(int x=0;x<N;x++)if(!in[x])q.push(x);
    while(!q.empty()){
      int x=q.front();q.pop();if(--in[f[x]]==0)q.push(f[x]);
    }
    array<long long,7> counts{};
    vector<char> visited(N,false);
    for(int x=0;x<N;x++)if(in[x]>0 && !visited[x]){
      int k=0,y=x;
      do{visited[y]=true;y=f[y];k++;assert(k<=6);}while(y!=x);
      counts[k]+=k;
    }
    long long p2=((1LL<<a)-2)*((1LL<<b)-2);
    long long p3=(a>=2 && b>=2)?3:0;
    long long p6=3*(T(a)+T(b));
    if(counts[1]!=1 || counts[2]!=p2 || counts[3]!=p3 || counts[6]!=p6 || counts[4]!=0 || counts[5]!=0){
      cerr<<"FAIL a="<<a<<" b="<<b<<" counts:";
      for(int k=1;k<=6;k++)cerr<<' '<<k<<':'<<counts[k];
      cerr<<endl;return 1;
    }
    pairs++;
    if((a==1 && b==4) || (a==2 && b==5) || (a==4 && b==4) || (a==6 && b==7)){
      cout<<"D_("<<a<<","<<b<<"): recurrent states by period 1="<<counts[1]<<" 2="<<counts[2]<<" 3="<<counts[3]<<" 6="<<counts[6]<<'\n';
    }
  }
  cout<<"PASS: "<<pairs<<" parameter pairs; all labelled states independently classified.\n";
}
