#include <bits/stdc++.h>
using namespace std;
int main(){const int n=3,N=1<<n,ALL=N-1;
 vector<array<int,8>> cand[N];
 for(int a=0;a<N;a++){
  vector<int> t;for(int u=0;u<N;u++)if((u&a)==u)t.push_back(u);
  vector<int> z;for(int u=0;u<N;u++)if((u&a)==0)z.push_back(u);
  function<void(int,array<int,8>)> rec=[&](int i,array<int,8> x){
   if(i==(int)t.size()){
    for(int v:t)for(int w:t)if((v&w)==v&&((x[v]&x[w])!=x[v]))return;
    cand[a].push_back(x);return;
   }
   for(int b:z){auto y=x;y[t[i]]=b;rec(i+1,y);}
  };rec(0,{});
 }
 for(int a=0;a<N;a++)cerr<<a<<":"<<cand[a].size()<<" ";cerr<<"\n";
 array<array<int,8>,8> s;
 long long count=0,ok[8]={}; long long fixed[6]={};
 vector<array<int,3>> perms; array<int,3> pr={0,1,2};do{perms.push_back(pr);}while(next_permutation(pr.begin(),pr.end()));
 int pm[6][8];for(int g=0;g<6;g++)for(int a=0;a<8;a++){int v=0;for(int i=0;i<3;i++)if(a&(1<<i))v|=1<<perms[g][i];pm[g][a]=v;}
 long long checks=0;
 function<void(int)> solve=[&](int a){
  if(a==N){count++;ok[s[0][0]]++;for(int g=0;g<6;g++){bool invariant=true;for(int x=0;x<8&&invariant;x++)for(int y=0;y<8;y++){int f=(x&y)|s[x][x&y];int xp=pm[g][x],yp=pm[g][y];int fp=(xp&yp)|s[xp][xp&yp];if(pm[g][f]!=fp){invariant=false;break;}}if(invariant)fixed[g]++;}return;}
  for(auto &c:cand[a]){
   s[a]=c;bool good=true;
   for(int b=0;b<a&&good;b++)if((a&b)==b){
    for(int t=0;t<N;t++)if((t&b)==t){
     int v=t|s[b][t];int u=v&a;
     if(s[a][u]& ~(v|a)){good=false;break;}
     // since sigma_a outside a, (v|a) equivalent v outside a
    }
   }
   if(good)solve(a+1);
  }
 };solve(0);
 cout<<"count="<<count<<" by_empty=";for(int i=0;i<8;i++)cout<<i<<":"<<ok[i]<<" ";cout<<"\nfixed=";for(int g=0;g<6;g++)cout<<fixed[g]<<" ";cout<<" orbit="<<accumulate(fixed,fixed+6,0LL)/6<<"\n";
}
