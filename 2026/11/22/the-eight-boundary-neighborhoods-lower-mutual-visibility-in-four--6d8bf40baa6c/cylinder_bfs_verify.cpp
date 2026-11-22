#include <bits/stdc++.h>
using namespace std;
int n,N;vector<vector<int>> adj;
inline int vertex(int r,int c){return r*n+c;}
int dist_formula(int a,int b){int ra=a/n,rb=b/n,ca=a%n,cb=b%n;int dr=abs(ra-rb);return min(dr,4-dr)+abs(ca-cb);}
bool pair_visible(int a,int b,uint64_t selected){
 int depth[64];fill(depth,depth+N,-1);int queue_[64],head=0,tail=0;
 queue_[tail++]=a;depth[a]=0;int target=dist_formula(a,b);
 while(head<tail){int u=queue_[head++];if(u==b)return depth[u]==target;
  for(int w:adj[u]) if(depth[w]==-1 && (w==b || !(selected&(1ULL<<w)))){
    depth[w]=depth[u]+1;queue_[tail++]=w;
  }
 }return false;
}
bool feasible(const vector<int>&set,uint64_t bits){for(int i=0;i<(int)set.size();i++)for(int j=i+1;j<(int)set.size();j++)if(!pair_visible(set[i],set[j],bits))return false;return true;}
bool maximal(const vector<int>&set,uint64_t bits){if(!feasible(set,bits))return false;for(int w=0;w<N;w++)if(!(bits&(1ULL<<w))){auto t=set;t.push_back(w);if(feasible(t,bits|(1ULL<<w)))return false;}return true;}
int main(int argc,char**argv){if(argc!=2)return 1;n=atoi(argv[1]);N=4*n;if(N>64)return 1;adj.resize(N);
 for(int r=0;r<4;r++)for(int c=0;c<n;c++){
  int a=vertex(r,c);adj[a].push_back(vertex((r+1)%4,c));adj[a].push_back(vertex((r+3)%4,c));
  if(c>0)adj[a].push_back(vertex(r,c-1));if(c+1<n)adj[a].push_back(vertex(r,c+1));
 }
 long long count3=0,count4=0,other4=0;vector<int> ss;set<uint64_t> expected;
 for(int r=0;r<4;r++)for(int c:{0,n-1}){
  uint64_t mask=0;for(int v:{vertex(r,c),vertex((r+1)%4,c),vertex((r+3)%4,c),vertex(r,c==0?1:n-2)})mask|=1ULL<<v;
  expected.insert(mask);
 }
 if(n==2)for(int p=0;p<2;p++){uint64_t mask=0;for(int r=0;r<4;r++)for(int c=0;c<2;c++)if((r+c)%2==p)mask|=1ULL<<vertex(r,c);expected.insert(mask);}
 set<uint64_t> seen;
 for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++){
  uint64_t mask=(1ULL<<a)|(1ULL<<b)|(1ULL<<c);ss={a,b,c};if(maximal(ss,mask))count3++;
  for(int d=c+1;d<N;d++){
    uint64_t mask4=mask|(1ULL<<d);ss={a,b,c,d};if(maximal(ss,mask4)){count4++;seen.insert(mask4);if(!expected.count(mask4))other4++;}
  }
 }
 cout<<"n="<<n<<" bfs_three="<<count3<<" bfs_four="<<count4<<" agreed="<<(seen==expected)<<"\n";
 return count3||other4||seen!=expected;
}
