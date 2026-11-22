#include <bits/stdc++.h>
using namespace std;
struct Node {int L,R,U,D,C,row;};
vector<Node>N;vector<int>sizeC,solution;long long calls=0;chrono::steady_clock::time_point start;
int add(int col,int row){int id=N.size();N.push_back({id,id,N[col].U,col,col,row});N[N[col].U].D=id;N[col].U=id;sizeC[col]++;return id;}
void cover(int c){N[N[c].R].L=N[c].L;N[N[c].L].R=N[c].R;for(int i=N[c].D;i!=c;i=N[i].D)for(int j=N[i].R;j!=i;j=N[j].R){N[N[j].D].U=N[j].U;N[N[j].U].D=N[j].D;sizeC[N[j].C]--;}}
void uncover(int c){for(int i=N[c].U;i!=c;i=N[i].U)for(int j=N[i].L;j!=i;j=N[j].L){sizeC[N[j].C]++;N[N[j].D].U=j;N[N[j].U].D=j;}N[N[c].R].L=c;N[N[c].L].R=c;}
bool dfs(){calls++;if(N[0].R==0){cout<<"FOUND "<<solution.size()<<"\n";for(int x:solution)cout<<x<<" ";cout<<"\n";return true;}int c=-1,sz=INT_MAX;for(int i=N[0].R;i!=0;i=N[i].R){if(sizeC[i]<sz){sz=sizeC[i];c=i;if(sz<2)break;}}if(sz==0)return false;cover(c);for(int i=N[c].D;i!=c;i=N[i].D){solution.push_back(N[i].row);for(int j=N[i].R;j!=i;j=N[j].R)cover(N[j].C);if(dfs())return true;for(int j=N[i].L;j!=i;j=N[j].L)uncover(N[j].C);solution.pop_back();}uncover(c);return false;}
int main(){int nr,nc;cin>>nr>>nc;N.push_back({0,0,0,0,0,-1});sizeC.resize(nc+1);for(int i=1;i<=nc;i++){N.push_back({i-1,i+1,i,i,i,-1});}N[0].L=nc;N[0].R=1;N[nc].R=0;vector<vector<int>> rows(nr);for(int i=0;i<nr;i++){for(int k=0;k<7;k++){int x;cin>>x;rows[i].push_back(x+1);}}
 for(int i=0;i<nr;i++){int fst=-1,last=-1;for(int c:rows[i]){int id=add(c,i);if(fst==-1)fst=id;else{N[id].L=last;N[last].R=id;}last=id;}N[fst].L=last;N[last].R=fst;}
 start=chrono::steady_clock::now();bool good=dfs();if(!good)cerr<<"NO FOUND after calls="<<calls<<" sec="<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<"\n";
}
