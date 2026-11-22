#include <bits/stdc++.h>
using namespace std;
int main(){
 vector<int> pairs;for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)pairs.push_back((1<<i)|(1<<j));
 vector<unsigned> adj(20);for(int i=0;i<10;i++)for(int j=0;j<10;j++)if(!(pairs[i]&pairs[j])){adj[i]|=1u<<(10+j);adj[10+j]|=1u<<i;}
 array<long long,21> all{},mx{};vector<unsigned> masks;
 for(unsigned s=0;s<(1u<<20);s++){
   bool ok=true;unsigned tmp=s;
   while(tmp){int i=__builtin_ctz(tmp);tmp&=tmp-1; if(__builtin_popcount(adj[i]&s)>1){ok=false;break;}}
   if(!ok)continue;
   int k=__builtin_popcount(s); all[k]++;
   bool maximal=true;
   for(int i=0;i<20;i++)if(!(s&(1u<<i))){
     unsigned t=s|(1u<<i); bool g=true;unsigned u=t;
     while(u){int j=__builtin_ctz(u);u&=u-1;if(__builtin_popcount(adj[j]&t)>1){g=false;break;}}
     if(g){maximal=false;break;}
   }
   if(maximal){mx[k]++; masks.push_back(s);}
 }
 cout << "all";for(auto x:all)cout<<" "<<x;cout<<"\n";
 cout << "maximal";for(auto x:mx)cout<<" "<<x;cout<<"\n";
 cout << "maximal_count "<<masks.size()<<"\n";
 for(auto s:masks)cout<<s<<"\n";
}
