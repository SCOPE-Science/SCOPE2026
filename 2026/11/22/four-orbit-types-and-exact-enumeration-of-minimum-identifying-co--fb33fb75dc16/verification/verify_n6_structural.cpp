#include <bits/stdc++.h>
using namespace std;
int main(){const int n=6,N=36,k=9; uint64_t row[6]={},col[6]={}, nb[36];
for(int i=0;i<n;i++)for(int j=0;j<n;j++){row[i]|=1ULL<<(i*n+j);col[j]|=1ULL<<(i*n+j);}for(int i=0;i<n;i++)for(int j=0;j<n;j++)nb[i*n+j]=row[i]|col[j];
long long all=0,selected=0,valid=0,type0=0,type1=0,other=0;map<string,long long> patterns;auto t=chrono::steady_clock::now();
for(uint64_t x=(1ULL<<k)-1;x<(1ULL<<N);){++all;
 bool good=true;
 for(int i=0;i<n;i++)if(!(x&row[i]) || !(x&col[i])){good=false;break;}
 if(good){
 int leafrow[6]={},leafcol[6]={};int isolated=0;
 for(uint64_t bits=x;bits;bits&=bits-1){int q=__builtin_ctzll(bits),r=q/n,c=q%n;
  bool rl=__builtin_popcountll(x&row[r])==1,cl=__builtin_popcountll(x&col[c])==1;
  if(cl && ++leafrow[r]>1){good=false;break;}
  if(rl && ++leafcol[c]>1){good=false;break;}
  if(rl&&cl)isolated++;
 }
 if(isolated>1)good=false;
 if(good){++selected;
  // independent check: all 36 closed-neighbourhood signatures distinct and nonempty
  uint64_t seen[36];int used=0;
  for(int z=0;z<36;z++){uint64_t s=nb[z]&x;if(!s){good=false;break;}
   for(int t=0;t<used;t++){if(s==seen[t]){good=false;break;}}
   if(!good)break;seen[used++]=s;
  }
  if(good){++valid; if(isolated==0)++type0;else if(isolated==1)++type1;else other++;
     int dd[12]={},adj[12][12]={};
     for(uint64_t bits=x;bits;bits&=bits-1){int q=__builtin_ctzll(bits),r=q/n,c=q%n;adj[r][n+c]=adj[n+c][r]=1;dd[r]++;dd[n+c]++;}
     bool seenNode[12]={};vector<string> cs;
     for(int z=0;z<12;z++){if(seenNode[z])continue;vector<int> todo={z},vs;seenNode[z]=true;
        for(int t=0;t<(int)todo.size();t++){int v=todo[t];vs.push_back(v);for(int j=0;j<12;j++)if(adj[v][j]&&!seenNode[j]){seenNode[j]=true;todo.push_back(j);}}
        vector<int> degrees;for(int v:vs)degrees.push_back(dd[v]);sort(degrees.begin(),degrees.end());string q=to_string(vs.size())+":";for(int a:degrees)q+=to_string(a);cs.push_back(q);
     } sort(cs.begin(),cs.end());string shape;for(auto c:cs)shape+=c+"/"; patterns[shape]++;
   }
 }
 }
 uint64_t c=x&-x;uint64_t y=x+c;x=(((x^y)>>2)/c)|y;
}
auto e=chrono::duration<double>(chrono::steady_clock::now()-t).count();
for(auto [k,v]:patterns)cout<<v<<" "<<k<<"\n"; cout<<"all "<<all<<" candidates structurally allowed "<<selected<<" valid "<<valid<<" no isolated "<<type0<<" one isolated "<<type1<<" other "<<other<<" seconds "<<e<<endl;
}
