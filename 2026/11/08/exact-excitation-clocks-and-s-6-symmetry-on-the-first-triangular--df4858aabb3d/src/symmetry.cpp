#include <bits/stdc++.h>
using namespace std;
const int n=15;int p3[16], mask[15];vector<pair<int,int>> vert;
int F(int st){int x=st,active=0;for(int i=0;i<n;i++){int c=x%3;x/=3;if(c==1)active|=1<<i;} x=st;int z=0;for(int i=0;i<n;i++){int c=x%3;x/=3;int nc=c==1?2:(c==2?0:((mask[i]&active)!=0));z+=nc*p3[i];}return z;}
int canon(int s,int L){int m=s;for(int i=1;i<L;i++){s=F(s);m=min(m,s);}return m;}
int main(){p3[0]=1;for(int i=1;i<=n;i++)p3[i]=3*p3[i-1];for(int a=0;a<6;a++)for(int b=a+1;b<6;b++)vert.push_back({a,b});map<pair<int,int>,int> idx;for(int i=0;i<n;i++)idx[vert[i]]=i;
 for(int i=0;i<n;i++)for(int j=0;j<n;j++){auto [a,b]=vert[i];auto [c,d]=vert[j];if(a!=c&&a!=d&&b!=c&&b!=d)mask[i]|=1<<j;}
 map<int,vector<int>> rp;ifstream fi("representatives.txt");int L,s;while(fi>>L>>s)rp[L].push_back(s);
 vector<array<int,15>> G;array<int,6> p={0,1,2,3,4,5};do{array<int,15> m{};for(int i=0;i<15;i++){auto [a,b]=vert[i];int c=p[a],d=p[b];if(c>d)swap(c,d);m[i]=idx[{c,d}];}G.push_back(m);}while(next_permutation(p.begin(),p.end()));
 cout<<"aut_count "<<G.size()<<"\n";
 for(auto &[L,reps]:rp){
   long long pervertex_bad=0;
   map< vector<int>,int > prof;
   for(int u:reps){int z=u;vector<int> fire(15,0),ex(L);for(int t=0;t<L;t++){int y=z,tot=0;for(int i=0;i<15;i++){int c=y%3;y/=3;if(c==1){fire[i]++;tot++;}}ex[t]=tot;z=F(z);}if(z!=u){cerr<<"ERROR cycle not closed\n";return 1;}
   for(int a=1;a<15;a++)if(fire[a]!=fire[0])pervertex_bad++;
   auto best=ex;for(int t=1;t<L;t++){auto rot=ex;rotate(rot.begin(),rot.begin()+t,rot.end());if(rot<best)best=rot;}prof[best]++;
   }
   cout<<"PHASE "<<L<<" per_vertex_nonuniform "<<pervertex_bad<<" profiles "<<prof.size()<<"\n";
   for(auto [v,c]:prof){cout<<"profile ";for(int x:v)cout<<x<<",";cout<<" cycles "<<c<<"\n";}
   map<int,int> where;for(int i=0;i<reps.size();i++)where[reps[i]]=i;vector<int> parent(reps.size());iota(parent.begin(),parent.end(),0); auto root=[&](int k){while(parent[k]!=k)k=parent[k]=parent[parent[k]];return k;};
  for(int i=0;i<reps.size();i++)for(auto &perm:G){int orig=reps[i],z=0;for(int v=0;v<15;v++){int col=(orig/p3[v])%3;z+=col*p3[perm[v]];}
   z=canon(z,L);auto it=where.find(z);if(it==where.end()){cerr<<"rep missing period "<<L<<" state "<<z<<"\n";return 1;} int a=root(i),b=root(it->second);if(a!=b)parent[a]=b;
  }
  map<int,vector<int>> classes;for(int i=0;i<reps.size();i++)classes[root(i)].push_back(reps[i]);
  cout<<"PERIOD "<<L<<" cycles "<<reps.size()<<" symmetry_classes "<<classes.size()<<"\n";
  for(auto &[r,cl]:classes){int s=*min_element(cl.begin(),cl.end());cout<<"orbit "<<cl.size()<<" group_stabilizer "<<G.size()/cl.size()<<" rep "<<s<<" digits ";for(int i=0;i<n;i++)cout<<(s/p3[i])%3;cout<<"\n";}
 }
}
