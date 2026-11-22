#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
long long counts[33]={},facets[33]={};
U third[32][32]={};
vector<array<int,3>> cons;
long long nodes=0;
void rec(int i,U sel,U forbid,int k){
 ++nodes;
 if(i==32){counts[k]++; if((sel|forbid)==U(0xffffffffu))facets[k]++; return;}
 rec(i+1,sel,forbid,k);
 if((forbid>>i)&1u)return;
 U f2=forbid;
 U b=sel;
 while(b){int j=__builtin_ctz(b);b&=b-1;f2|=third[i][j];}
 rec(i+1,sel|(U(1)<<i),f2,k+1);
}
int main(){
 int d=4,n=1<<d;
 vector<pair<int,int>> edges;int idx[16][16];memset(idx,-1,sizeof idx);
 for(int x=0;x<n;x++)for(int j=0;j<d;j++){int y=x^(1<<j);if(x<y){idx[x][y]=idx[y][x]=edges.size();edges.push_back({x,y});}}
 set<array<int,3>> ss;
 for(int x=0;x<n;x++)for(int y=x+1;y<n;y++){
  int dif=x^y;if(__builtin_popcount((unsigned)dif)<3)continue;
  vector<int> coords;for(int j=0;j<d;j++)if((dif>>j)&1)coords.push_back(j);
  do {int cur=x;vector<int> p;for(int j:coords){int z=cur^(1<<j);p.push_back(idx[cur][z]);cur=z;}
   for(int a=0;a<(int)p.size();a++)for(int b=a+1;b<(int)p.size();b++)for(int c=b+1;c<(int)p.size();c++){
    array<int,3> ar={p[a],p[b],p[c]};sort(ar.begin(),ar.end());ss.insert(ar);
   }
  }while(next_permutation(coords.begin(),coords.end()));
 }
 for(auto t:ss){for(int x=0;x<3;x++){int a=t[x],b=t[(x+1)%3],c=t[(x+2)%3];third[a][b]|=U(1)<<c;third[b][a]|=U(1)<<c;}}
 cerr<<"constraints "<<ss.size()<<"\n";auto start=chrono::steady_clock::now();
 rec(0,0,0,0);
 cerr<<"nodes "<<nodes<<" seconds "<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
 for(int i=0;i<=32;i++)if(counts[i])cout<<i<<" "<<counts[i]<<" "<<facets[i]<<"\n";
}
