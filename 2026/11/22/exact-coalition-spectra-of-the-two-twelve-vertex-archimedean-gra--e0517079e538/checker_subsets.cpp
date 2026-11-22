#include <bits/stdc++.h>
using namespace std;
using U=unsigned;
int main(int argc,char**argv){int mode=(argc>1)?atoi(argv[1]):0;
 vector<pair<int,int>> e;
 if(!mode){for(int a=0;a<8;a++)for(int k=0;k<3;k++) if(!(a&(1<<k)))e.push_back({a,a^(1<<k)});}
 else{for(int a=0;a<4;a++)for(int b=0;b<4;b++)if(a!=b)e.push_back({a,b});}
 int n=e.size(), universe=(1<<n)-1;
 vector<U> N(n);for(int a=0;a<n;a++){N[a]=1u<<a;for(int b=0;b<n;b++){if(a==b)continue;bool edge=!mode?(e[a].first==e[b].first||e[a].first==e[b].second||e[a].second==e[b].first||e[a].second==e[b].second):(e[a].first==e[b].first||(e[a].first==e[b].second&&e[a].second==e[b].first));if(edge)N[a]|=1u<<b;}}
 // Independently compute a set's failure-to-dominate as its uncovered vertex mask.
 vector<U> missed(1u<<n); missed[0]=universe;
 for(U s=1;s<(1u<<n);s++){U b=s&-s;missed[s]=missed[s^b]&~N[__builtin_ctz(b)];}
 vector<U> blocks;long long cnt[13]={};long long node=0;map<vector<int>,int> profiles;vector<vector<U>> tops;
 auto run=[&](auto&&self,U remain)->void{
   if(!remain){node++;int k=blocks.size();for(int i=0;i<k;i++){if(missed[blocks[i]]==0) return;bool linked=false;for(int j=0;j<k;j++) if(j!=i && (missed[blocks[i]]&missed[blocks[j]])==0){linked=true;break;}if(!linked)return;}
      cnt[k]++;if(k==8){auto bs=blocks;sort(bs.begin(),bs.end());tops.push_back(bs);vector<int> ss;for(auto b:bs)ss.push_back(__builtin_popcount(b));sort(ss.begin(),ss.end());profiles[ss]++;}
      return;
   }
   U low=remain&-remain;
   for(U sub=remain;sub;sub=(sub-1)&remain){if(!(sub&low))continue;blocks.push_back(sub);self(self,remain^sub);blocks.pop_back();}
 };
 run(run,universe);
 cout<<"mode="<<mode<<" total partitions="<<node<<" counts=";for(int i=0;i<=n;i++)if(cnt[i])cout<<i<<":"<<cnt[i]<<" ";cout<<"\n";
 cout<<"optimum_profiles=";for(auto [k,v]:profiles){for(int s:k)cout<<s<<",";cout<<":"<<v<<" ";}cout<<"\n";
 for(auto bs:tops){for(auto b:bs)cout<<b<<" ";cout<<"\n";}
}
