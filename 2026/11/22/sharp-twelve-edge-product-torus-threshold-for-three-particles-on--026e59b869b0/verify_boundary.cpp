#include <bits/stdc++.h>
using namespace std;
int main(){vector<pair<int,int>> E={{0,1},{0,2},{0,4},{1,11},{1,14},{2,3},{2,4},{3,6},{3,8},{4,5},{5,16},{5,18},{6,7},{6,8},{7,10},{7,12},{8,9},{9,17},{9,20},{10,11},{10,12},{11,14},{12,13},{13,21},{13,22},{14,15},{15,19},{15,23},{16,17},{16,18},{17,20},{18,19},{19,23},{20,21},{21,22},{22,23}};
vector<vector<int>> inc(24);for(int i=0;i<36;i++){inc[E[i].first].push_back(i);inc[E[i].second].push_back(i);}for(auto &x:inc)sort(x.begin(),x.end());
map<tuple<int,int,int,int,int>,int> R;int nr=0;for(int u=0;u<24;u++)for(int v=u+1;v<24;v++)for(int a=1;a<=2;a++)for(int b=1;b<=2;b++)for(int e=0;e<36;e++)R[{u,v,a,b,e}]=nr++;
vector<map<int,long long,greater<int>>> pv(nr);vector<char> used(nr,0);int rank=0,col=0;long long ops=0;long long peak=1;auto norm=[](long long a){return a;};
for(int u=0;u<24;u++)for(int v=u+1;v<24;v++)for(int w=v+1;w<24;w++)for(int a=1;a<=2;a++)for(int b=1;b<=2;b++)for(int c=1;c<=2;c++){
 map<int,long long,greater<int>> x;
 auto add=[&](int p,int q,int lp,int lq,int e,int sig){int j=R[{p,q,lp,lq,e}];int y=norm(x[j]+sig);if(y)x[j]=y;else x.erase(j);};
 add(v,w,b,c,inc[u][a],1);add(v,w,b,c,inc[u][0],-1);
 add(u,w,a,c,inc[v][b],-1);add(u,w,a,c,inc[v][0],1);
 add(u,v,a,b,inc[w][c],1);add(u,v,a,b,inc[w][0],-1);
 col++;
 while(!x.empty()){
  int h=x.begin()->first;long long val=x.begin()->second;
  if(!used[h]){if(llabs(val)!=1){cerr<<"NONUNIT row="<<h<<" val="<<val<<" col="<<col<<" rank="<<rank<<"\n";return 2;} if(val==-1){for(auto &p:x)p.second=-p.second;} pv[h].swap(x);used[h]=1;rank++;break;}
  auto &y=pv[h];for(const auto &p:y){int j=p.first;long long z=(x.count(j)?x[j]:0)-val*p.second;peak=max(peak,llabs(z)); if(peak>100000000LL){cerr<<"integer growth limit exceeded\n";return 4;}if(z)x[j]=z;else x.erase(j);}ops++;
 }
 
}
if(col!=16192 || nr!=39744 || rank!=16096){cerr<<"Unexpected differential dimensions or rank\n";return 3;} cout<<"BOUNDARY_INTEGER_UNIT_PIVOTS_OK C3="<<col<<" C2="<<nr<<" rank="<<rank<<" nullity="<<col-rank<<" peak="<<peak<<"\n";
}
