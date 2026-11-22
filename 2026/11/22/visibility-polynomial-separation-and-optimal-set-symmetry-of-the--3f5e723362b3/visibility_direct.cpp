// Exhaustive shortest-path visibility census on two labelled graphs.
// Requires C++17; independent of the forbidden-hypergraph implementation.
#include <array>
#include <vector>
#include <queue>
#include <iostream>
#include <cassert>
using namespace std;
using Board=array<array<int,16>,16>;
Board graph(bool shr) {
    Board a{};
    for(int u=0;u<16;u++)for(int v=0;v<16;v++)if(u!=v){
        int x=u/4,y=u%4,X=v/4,Y=v%4;
        if(!shr)a[u][v]=(x==X||y==Y);
        else{
            int dx=(X-x+4)%4,dy=(Y-y+4)%4;
            a[u][v]=((dx==1||dx==3)&&dy==0)||((dy==1||dy==3)&&dx==0)||((dx==1&&dy==1)||(dx==3&&dy==3));
        }
    }
    for(int i=0;i<16;i++){int degree=0;for(int j=0;j<16;j++)degree+=a[i][j];assert(degree==6);}
    return a;
}
int dist(const Board &a,int start,int end,unsigned forbidden){
    array<int,16> d;d.fill(-1);queue<int>q;d[start]=0;q.push(start);
    while(!q.empty()){
      int u=q.front();q.pop();if(u==end)return d[u];
      for(int v=0;v<16;v++)if(a[u][v]&&d[v]<0&&(!(forbidden>>v&1)||v==end)){
        d[v]=d[u]+1;q.push(v);
      }
    }
    return -1;
}
int main(){
   const array<array<long,11>,2> expected{{
     {1,16,120,560,1784,3936,5728,4768,1512,96,0},
     {1,16,120,560,1760,3744,5216,4432,2004,384,32}
   }};
   for(int g=0;g<2;g++){
      Board a=graph(g);
      array<long,17> counts{};
      for(unsigned mask=0;mask<(1u<<16);mask++){
        bool ok=true;
        for(int u=0;u<16&&ok;u++)if(mask>>u&1)
         for(int v=u+1;v<16;v++)if(mask>>v&1){
           int natural=dist(a,u,v,0u);
           int clear=dist(a,u,v,mask&~((1u<<u)|(1u<<v)));
           if(clear!=natural){ok=false;break;}
         }
        if(ok)counts[__builtin_popcount(mask)]++;
      }
      for(int i=0;i<17;i++)assert(counts[i]==(i<=10?expected[g][i]:0));
      cout<<(g?"S":"R")<<" ";for(int i=0;i<=10;i++)cout<<counts[i]<<" ";cout<<"\n";
   }
   cout<<"VISIBILITY_DIRECT_CPP_OK\n";
}
