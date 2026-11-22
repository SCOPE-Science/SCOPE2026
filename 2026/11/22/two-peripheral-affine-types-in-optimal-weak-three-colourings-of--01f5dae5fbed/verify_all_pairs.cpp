#include <bits/stdc++.h>
using namespace std;
int main(){
const int n=9,total=19683; vector<array<int,3>> lines;
for(int a=0;a<3;a++)for(int b=0;b<3;b++)if(a||b){if((a==0&&b==1)||(a==1))for(int c=0;c<3;c++){array<int,3> v;int s=0;for(int x=0;x<3;x++)for(int y=0;y<3;y++)if((a*x+b*y)%3==c)v[s++]=x*3+y;lines.push_back(v);}}
cout<<"lines "<<lines.size()<<"\n";
vector<int> p(10,1),id(total,-1),states;for(int i=1;i<=9;i++)p[i]=p[i-1]*3;
for(int code=0;code<total;code++){
 int a[9];int t=code;for(int i=0;i<9;i++){a[i]=t%3;t/=3;}
 bool ok=1;for(auto L:lines)if(a[L[0]]==a[L[1]]&&a[L[1]]==a[L[2]]){ok=0;break;}
 if(ok){id[code]=states.size();states.push_back(code);}
}
int N=states.size();vector<vector<int>>adj(N);long long edges=0;map<int,int>degree;
for(int i=0;i<N;i++){
 int z=states[i];for(int v=0;v<9;v++){
  int c=(z/p[v])%3;for(int d=0;d<3;d++)if(d!=c){int w=z+(d-c)*p[v];if(id[w]>=0)adj[i].push_back(id[w]);}
 }degree[adj[i].size()]++;edges+=adj[i].size();
}
cout<<"N "<<N<<" E "<<edges/2<<" degree";for(auto [k,v]:degree)cout<<" "<<k<<":"<<v;cout<<"\n";
map<int,int>ecc,distances;int rad=INT_MAX,diam=0;vector<int>ex(30),q(N),dd(N);
for(int i=0;i<N;i++){
 fill(dd.begin(),dd.end(),-1);dd[i]=0;int h=0,t=1;q[0]=i;
 while(h<t){int u=q[h++];for(int v:adj[u])if(dd[v]<0){dd[v]=dd[u]+1;q[t++]=v;}}
 if(t!=N){cerr<<"unconnected"<<i<<"\n";return 1;}
 int e=*max_element(dd.begin(),dd.end());ecc[e]++;rad=min(rad,e);diam=max(diam,e);if(i%1000==0)cerr<<i<<"/"<<N<<"\n";
 for(int j=i+1;j<N;j++)distances[dd[j]]++;
}
cout<<"radius "<<rad<<" diameter "<<diam<<"\necc";for(auto [k,v]:ecc)cout<<" "<<k<<":"<<v;cout<<"\ndistance";for(auto [k,v]:distances)cout<<" "<<k<<":"<<v;cout<<"\n";
}
