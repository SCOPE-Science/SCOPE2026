#include <bits/stdc++.h>
using namespace std;
// Independent augmented chain ranks over F_2, using bitset elimination.
int main(){const int N=1<<20;int adj[20]={};auto add=[&](int a,int b){adj[a]|=1<<b;adj[b]|=1<<a;};for(int i=0;i<10;i++){add(i,(i+1)%10);add(i,i+10);add(10+i,10+(i+2)%10);}
 vector<uint8_t> valid(N);vector<vector<int>> f(21);valid[0]=1;f[0].push_back(0);for(int s=1;s<N;s++){int i=__builtin_ctz((unsigned)s),t=s^(1<<i);if(!valid[t])continue;int d=__builtin_popcount((unsigned)(adj[i]&t));if(d>1)continue;if(d==1){int j=__builtin_ctz((unsigned)(adj[i]&t));if(__builtin_popcount((unsigned)(adj[j]&t)))continue;}valid[s]=1;f[__builtin_popcount((unsigned)s)].push_back(s);}vector<int> idx(N,-1);vector<int> ranks(21,0);for(int k=1;k<=12;k++){for(int i=0;i<(int)f[k-1].size();i++)idx[f[k-1][i]]=i;int rows=f[k-1].size(), W=(rows+63)/64;vector<vector<uint64_t>> piv(rows);int rank=0;
 for(int s:f[k]){vector<uint64_t> v(W);for(int b=s;b;b&=b-1){int j=__builtin_ctz((unsigned)b);int row=idx[s^(1<<j)]; if(row<0){cerr<<"MISSING FACE\n";return 1;}v[row/64]^=1ull<<(row%64);}while(1){int p=-1;for(int w=W-1;w>=0;w--)if(v[w]){p=w*64+63-__builtin_clzll(v[w]);break;}if(p<0)break;if(piv[p].empty()){piv[p]=move(v);rank++;break;}for(int w=0;w<W;w++)v[w]^=piv[p][w];}}
 ranks[k]=rank;cout<<"rank d_"<<k-1<<" = "<<rank<<"\n";for(int s:f[k-1])idx[s]=-1;
 }
 cout<<"mod2 betti :";for(int k=1;k<=12;k++){int b=f[k].size()-ranks[k]-ranks[k+1];if(b)cout<<" dim"<<k-1<<"="<<b; if(b != ((k-1)==6 ? 1 : 0)){cerr<<"BETTI_MISMATCH dim="<<k-1<<"\n";return 2;}}cout<<"\nALL_MOD2_CHECKS_PASS\n";
}
