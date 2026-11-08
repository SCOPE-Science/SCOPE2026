#include <bits/stdc++.h>
using namespace std;
using ll=long long;
struct Dat {int minE[17]; ll cnt[17]; array<int,16> colors; long long visited=0;};
int main(){for(int kind=0;kind<2;kind++){
 vector<vector<int>> adj(16);auto id=[](int x,int y){return 4*x+y;};
 for(int x=0;x<4;x++)for(int y=0;y<4;y++)for(int u=0;u<4;u++)for(int v=0;v<4;v++){
  if(x==u && y==v)continue;
  bool edge= (kind==0) ? (x==u || y==v) : ((u-x+4)%4==1 && (v-y+4)%4==0) || ((u-x+4)%4==3 && (v-y+4)%4==0)||((u-x+4)%4==0 && (v-y+4)%4==1)||((u-x+4)%4==0 && (v-y+4)%4==3)||((u-x+4)%4==1 && (v-y+4)%4==1)||((u-x+4)%4==3 && (v-y+4)%4==3);
  if(edge)adj[id(x,y)].push_back(id(u,v));
 }
 for(int i=0;i<16;i++) {
  if(adj[i].size()!=6)return 4;
  for(int j=i+1;j<16;j++) {
   int common=0;
   for(int k:adj[i])for(int l:adj[j])if(k==l)common++;
   if(common!=2)return 5;
  }
 }
 int minE[17];ll cnt[17];fill(minE,minE+17,10000);fill(cnt,cnt+17,0);
 array<int,16> c;ll nleaf=0;
 function<void(int,int,int)> dfs=[&](int d,int E,int N){
  if(d==16){nleaf++;if(E<minE[N]){minE[N]=E;cnt[N]=1;} else if(E==minE[N])cnt[N]++;return;}
  for(int color=0;color<3;color++){
   int de=0;for(auto j:adj[d])if(j<d && c[j]==color)de++;
   c[d]=color;dfs(d+1,E+de,N+(color==0));
  }
 };
 dfs(0,0,0);
 if(nleaf!=43046721ull)return 6;
 cout << (kind==0?"rook":"shrikhande")<<"\n";
 for(int i=0;i<=16;i++)cout << i << " "<<minE[i]<<" "<<cnt[i]<<"\n";

 }
}
