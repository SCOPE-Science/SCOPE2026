#include <bits/stdc++.h>
using namespace std;
static long long cases=0, sync_count=0, nonsync_count=0, primitive_nonsync=0, bad_quota=0, split_counts[2][2]={};
static int a[9],v[9],blocks[9];
void run_partition(const vector<vector<int>>& groups,int kernel_kind){
 int lab[9];for(int j=0;j<7;j++)for(int pos:groups[j])lab[pos]=j;
 iota(v,v+9,0);
 do{
   if(v[7]>v[8])continue;
   int b[9];for(int i=0;i<9;i++)b[i]=v[lab[i]];
   // Begin with all pairs already merged by b; add all reverse cyclic and reverse b preimages until stable.
   // A pair is compressed iff an edge in the 36-state pair automaton leads to a compressed pair.
   bool reachable[9][9]={};
   for(int i=0;i<9;i++)for(int j=i+1;j<9;j++)if(b[i]==b[j])reachable[i][j]=1;
   bool change;
   do{
     change=false;
     for(int i=0;i<9;i++)for(int j=i+1;j<9;j++){
       if(reachable[i][j])continue;
       int ai=(i+1)%9,aj=(j+1)%9;if(ai>aj)swap(ai,aj);
       int bi=b[i],bj=b[j];if(bi>bj)swap(bi,bj);
       if(reachable[ai][aj] || (bi!=bj && reachable[bi][bj])) {reachable[i][j]=1;change=true;}
     }
   }while(change);
   bool s=true;for(int i=0;i<9;i++)for(int j=i+1;j<9;j++)if(!reachable[i][j])s=false;
   bool c3=true;for(int i=0;i<3;i++)if(b[i]%3!=b[i+3]%3||b[i]%3!=b[i+6]%3)c3=false;
   cases++; if(s)sync_count++;else nonsync_count++;
   if(!s&&!c3){primitive_nonsync++; if(primitive_nonsync<4){cerr<<"COUNTEREXAMPLE ";for(int u:b)cerr<<u<<',';cerr<<'\n';}}
   split_counts[kernel_kind][!s]++;
 }while(next_permutation(v,v+9));
}
int main(){
 for(int x=0;x<9;x++)for(int y=x+1;y<9;y++)for(int z=y+1;z<9;z++){
   vector<vector<int>>g={{x,y,z}};for(int i=0;i<9;i++)if(i!=x&&i!=y&&i!=z)g.push_back({i});run_partition(g,0);
 }
 for(int x=0;x<9;x++)for(int y=x+1;y<9;y++)for(int z=0;z<9;z++)for(int t=z+1;t<9;t++){
   if(z==x||z==y||t==x||t==y)continue;
   if(make_pair(x,y)>make_pair(z,t))continue;
   vector<vector<int>>g={{x,y},{z,t}};for(int i=0;i<9;i++)if(i!=x&&i!=y&&i!=z&&i!=t)g.push_back({i});run_partition(g,1);
 }
 cout<<"total="<<cases<<" synchronizing="<<sync_count<<" nonsynchronizing="<<nonsync_count<<" primitive_nonsync="<<primitive_nonsync<<'\n';
 cout<<"triple sync="<<split_counts[0][0]<<" nonsync="<<split_counts[0][1]<<'\n';
 cout<<"two_pairs sync="<<split_counts[1][0]<<" nonsync="<<split_counts[1][1]<<'\n';
}
