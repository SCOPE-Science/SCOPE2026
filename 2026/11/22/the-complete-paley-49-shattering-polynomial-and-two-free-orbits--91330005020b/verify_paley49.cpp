#include <bits/stdc++.h>
using namespace std;
// F49=F7[i], i^2=6; enumerate squares directly.
int mult(int x,int y){int a=x%7,b=x/7,c=y%7,d=y/7;return ((a*c+6*b*d)%7+7)%7+7*((a*d+b*c)%7);}
int sub(int x,int y){return ((x%7-y%7+7)%7)+7*((x/7-y/7+7)%7);}
int main(){
 bool square[49]={};for(int i=1;i<49;i++)square[mult(i,i)]=true;
 int adj[49][49];int deg=0;
 for(int x=0;x<49;x++)for(int y=0;y<49;y++)adj[x][y]=x!=y&&square[sub(x,y)];
 for(int j=0;j<49;j++)deg+=adj[0][j];
 assert(deg==24);
 cerr<<"degree "<<deg<<"\n";
 for(int k=1;k<=5;++k){
  uint64_t anch=0;vector<int>ids(k);ids[0]=0;long long ref=0;
  uint32_t goal=(k==5?0xffffffffu:((1u<<(1u<<k))-1u));
  auto rec=[&](auto&&self,int level,int start)->void{
    if(level==k){uint32_t seen=0;
      for(int c=0;c<49;c++){
        unsigned p=0;for(int i=0;i<k;i++)p|=unsigned(adj[c][ids[i]])<<i;
        seen|=uint32_t(1)<<p;if(seen==goal)break;
      }
      if(seen==goal){anch++;if(!ref){for(int j:ids)cout<<j<<',';cout<<" (witness k="<<k<<")\n";ref=1;}}
      return;
    }
    for(int i=start;i<=49-(k-level);i++){ids[level]=i;self(self,level+1,i+1);}
  };
  rec(rec,1,1);
  assert(anch%k==0);
  const uint64_t expected[6]={0,1,48,1128,16320,480};
  assert(anch==expected[k]);
  cout<<"k="<<k<<" anchored="<<anch<<" total="<<(49*anch/k)<<"\n";
 }
 cerr<<"EXHAUSTIVE_SQUARE_ENUMERATION_CHECKS_PASS\n";
}
