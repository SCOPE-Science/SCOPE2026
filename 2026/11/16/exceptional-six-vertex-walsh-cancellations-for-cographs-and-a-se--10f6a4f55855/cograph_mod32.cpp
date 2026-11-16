#include <bits/stdc++.h>
using namespace std;using ll=long long;
// Independent cograph recognition: recursively separate connected components of a graph or its complement.
int n=7,m=21;int E[7][7];
int neighbor(int graph,int v,int rest,bool complement){int a=0;for(int u=0;u<n;u++)if(rest&(1<<u)){if((bool)(graph&(1<<E[v][u])) != complement)a|=(1<<u);}return a;}
vector<int> parts(int graph,int V,bool complement){vector<int> a;int un=V;while(un){int p=1<<__builtin_ctz((unsigned)un),set=p,queue=p;un^=p;while(queue){int v=__builtin_ctz((unsigned)queue);queue^=1<<v;int ext=neighbor(graph,v,un,complement);queue|=ext;set|=ext;un&=~ext;}a.push_back(set);}return a;}
bool cog(int g,int V){if((V&(V-1))==0)return true;auto cc=parts(g,V,false);if(cc.size()==1){cc=parts(g,V,true);if(cc.size()==1)return false;}for(int c:cc)if(!cog(g,c))return false;return true;}
int main(){for(int i=0,k=0;i<n;i++)for(int j=i+1;j<n;j++)E[i][j]=E[j][i]=k++;
int N=1<<m;vector<int> cnt(N);ll objects=0,moment_sum=0;for(int g=0;g<N;g++)if(cog(g,(1<<n)-1)){objects++;int ed[21],size=0;for(int i=0;i<m;i++)if(g>>i&1)ed[size++]=i;
++cnt[0];for(int i=0;i<size;i++){int a=1<<ed[i];++cnt[a];for(int j=i+1;j<size;j++){int b=a|(1<<ed[j]);++cnt[b];for(int k=j+1;k<size;k++){int c=b|(1<<ed[k]);++cnt[c];for(int l=k+1;l<size;l++)++cnt[c|(1<<ed[l])];}}}}
long long checked[5]={},fail[5]={},mim[5]={},mam[5]={};for(int i=0;i<5;i++)mim[i]=INT_MAX;
for(int mask=0;mask<N;mask++){int k=__builtin_popcount((unsigned)mask);if(k>4)continue;checked[k]++;mim[k]=min(mim[k],(ll)cnt[mask]);mam[k]=max(mam[k],(ll)cnt[mask]);int mod=1<<(5-k);int target=k==0?16:k==1?8:0;if(cnt[mask]%mod!=target)fail[k]++;}
cout<<"cographs="<<objects<<"\n";for(int k=0;k<=4;k++)cout<<"forced edges="<<k<<" patterns="<<checked[k]<<" count_min="<<mim[k]<<" count_max="<<mam[k]<<" modulo="<<(1<<(5-k))<<" expected_residue="<<(k==0?16:k==1?8:0)<<" failures="<<fail[k]<<"\n";
if(objects!=78416)return 1;for(int k=0;k<=4;k++)if(fail[k])return 2;
cout<<"Therefore W(S) is 16 mod 32 for even |S| by finite moment identities.\n";
return 0;}
