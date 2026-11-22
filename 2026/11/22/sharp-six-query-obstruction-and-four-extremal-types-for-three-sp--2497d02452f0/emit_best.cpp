#include <bits/stdc++.h>
using namespace std;
int n,k,m,NW; vector<int> weights; vector<int> cols, rows; unsigned int seen[1024]; unsigned int tick=1; uint64_t subspaces=0,good=0; vector<int> witness; map<int,int> distribution;
void assess(){
  subspaces++; ++tick;
  int count=0;
  for(int w:weights){
   int y=w;
   for(int j=0;j<k;j++) if((y>>cols[j])&1) y^=rows[j];
   if(seen[y]!=tick){seen[y]=tick;count++;}
  }
  distribution[count]++; if(n==9&&k==3&&count==63){for(auto z:rows)cerr<<z<<" ";cerr<<"\n";}
  if(count==(1<<(n-k))){good++;if(witness.empty())witness=rows;}
}
void rec(vector<pair<int,int>>&free,int t){
 if(t==(int)free.size()){assess();return;}
 auto [r,c]=free[t];rec(free,t+1);rows[r]|=(1<<c);rec(free,t+1);rows[r]^=(1<<c);
}
void pv(int first,int depth){
 if(depth==k){
  rows.assign(k,0);for(int j=0;j<k;j++) rows[j]=1<<cols[j];
  vector<pair<int,int>> free;
  for(int r=0;r<k;r++)for(int c=cols[r]+1;c<n;c++)if(find(cols.begin(),cols.end(),c)==cols.end()) free.push_back({r,c});
  rec(free,0);return;
 }
 for(int c=first;c<=n-(k-depth);c++){cols.push_back(c);pv(c+1,depth+1);cols.pop_back();}
}
int main(int argc,char**argv){n=atoi(argv[1]);k=atoi(argv[2]);m=n-k;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int l=j+1;l<n;l++)weights.push_back((1<<i)|(1<<j)|(1<<l));pv(0,0);
 cout<<"n="<<n<<" m="<<m<<" kernel="<<k<<" subspaces="<<subspaces<<" success="<<good<<"\n";
 cout<<"first-witness-kernel-rows:";for(int x:witness)cout<<" "<<x;cout<<"\n";
 cout<<"rank-max-distribution:";int top=0;for(auto [x,c]:distribution)top=max(top,x);cout<<" max="<<top<<" count="<<distribution[top]<<"\n";
 for(auto [x,c]:distribution) if(x>=top-4)cout<<x<<":"<<c<<" ";cout<<"\n";
}
