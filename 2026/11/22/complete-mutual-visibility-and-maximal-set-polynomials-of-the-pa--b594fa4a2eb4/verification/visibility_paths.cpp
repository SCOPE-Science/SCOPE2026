#include <bits/stdc++.h>
using namespace std;
using U=uint32_t;
int main(){
const int N=18;vector<vector<int>> a(N);for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int m=0;m<3;m++)for(int t=0;t<3;t++)if(y==(m*x+t)%3){int i=3*x+y,j=9+3*m+t;a[i].push_back(j);a[j].push_back(i);} 
vector<vector<int>> dist(N,vector<int>(N,100));for(int i=0;i<N;i++){queue<int>q;q.push(i);dist[i][i]=0;while(!q.empty()){int v=q.front();q.pop();for(int w:a[v])if(dist[i][w]>dist[i][v]+1){dist[i][w]=dist[i][v]+1;q.push(w);}}}
vector<vector<vector<U>>> paths(N,vector<vector<U>>(N));
function<void(int,int,int,U)> dfs=[&](int s,int t,int v,U mask){if(v==t){paths[s][t].push_back(mask);return;}for(int w:a[v])if(dist[s][w]==dist[s][v]+1&&dist[w][t]+dist[s][w]==dist[s][t])dfs(s,t,w,mask|((w==t)?0u:(1u<<w)));};
for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)dfs(i,j,i,0);
int maxlength=0;for(int i=0;i<N;i++)for(int j=i+1;j<N;j++)maxlength=max(maxlength,(int)paths[i][j].size());
vector<unsigned char> good(1<<N,0);vector<long long> cnt(N+1),facet(N+1);U full=(1u<<N)-1;
for(U s=0;s<=full;s++){bool ok=true;U t=s;while(t && ok){int i=__builtin_ctz(t);t&=t-1;U z=t;while(z){int j=__builtin_ctz(z);z&=z-1;if(dist[i][j]==1)continue;bool found=false;for(U p:paths[i][j]) if(!(p&s)){found=true;break;}if(!found){ok=false;break;}}}if(ok){good[s]=1;cnt[__builtin_popcount(s)]++;}}
ofstream ff("maximal_sets.txt",ios::trunc);for(U s=0;s<=full;s++)if(good[s]){bool maximal=true;for(U r=full^s;r;r&=r-1){U k=r&-r;if(good[s|k]){maximal=false;break;}}if(maximal){facet[__builtin_popcount(s)]++; if(__builtin_popcount(s)>=6) ff<<s<<"\n";}}
ff.close();cout << "N="<<N<<" max_paths="<<maxlength<<"\n";
cout<<"counts:";for(int k=0;k<=N;k++)if(cnt[k])cout<<" "<<k<<":"<<cnt[k];cout<<"\n";
cout<<"facets:";for(int k=0;k<=N;k++)if(facet[k])cout<<" "<<k<<":"<<facet[k];cout<<"\n";
ofstream fg("visibility_states.bin",ios::binary);fg.write((char*)good.data(),good.size());fg.close();
// hash of all good masks for crosscheck
unsigned long long h=1469598103934665603ull;for(U s=0;s<=full;s++) {h^=good[s];h*=1099511628211ull;}cout<<"fnv64="<<hex<<h<<dec<<"\n";
}
