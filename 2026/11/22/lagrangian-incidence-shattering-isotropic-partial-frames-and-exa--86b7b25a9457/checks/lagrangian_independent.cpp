// Finite symplectic incidence and exact reduced mod-two homology verifier.
// Standalone: c++ -O2 -std=c++17 lagrangian_independent.cpp -o check && ./check
#include <bits/stdc++.h>
using namespace std;
static int skew(int a,int b,int n){int z=0;for(int i=0;i<n;i++)z^=(((a>>i)&1)&((b>>(n+i))&1)) ^ (((b>>i)&1)&((a>>(n+i))&1));return z;}
static uint64_t spanmask(const vector<int>& v){vector<int>s{0};for(int x:v){int t=s.size();for(int i=0;i<t;i++)s.push_back(s[i]^x);}uint64_t z=0;for(int x:s)z|=1ULL<<x;return z;}
static int binaryrank(vector<vector<uint64_t>> col,int rows){int words=(rows+63)/64;unordered_map<int,vector<uint64_t>> piv;int rank=0;for(auto &v:col){while(1){int at=-1;for(int w=words-1;w>=0;w--){if(v[w]){at=64*w+63-__builtin_clzll(v[w]);break;}}if(at<0)break;auto it=piv.find(at);if(it==piv.end()){piv.emplace(at,v);rank++;break;}for(int w=0;w<words;w++)v[w]^=it->second[w];}}return rank;}
int main(){for(int n=1;n<=3;n++){int N=1<<(2*n);set<uint64_t> lagset;vector<int> tmp;
function<void(int)> build=[&](int start){if((int)tmp.size()==n){lagset.insert(spanmask(tmp));return;}for(int v=start;v<N;v++){bool ok=true;for(int t:tmp)if(skew(v,t,n))ok=false;if(!ok)continue;auto nxt=tmp;nxt.push_back(v);if(__builtin_popcountll(spanmask(nxt))!=(1<<(int)nxt.size()))continue;tmp.push_back(v);build(v+1);tmp.pop_back();}}; build(1);
vector<uint64_t> lags(lagset.begin(),lagset.end()); vector<vector<int>> pts(n+1);vector<vector<vector<int>>> faces(n+1);faces[0].push_back({});vector<int> f(n+1);f[0]=1;
for(int k=1;k<=n;k++){vector<int> x;function<void(int)> dfs=[&](int next){if((int)x.size()==k){bool pred=(int)__builtin_popcountll(spanmask(x))==(1<<k);for(int i=0;i<k;i++)for(int j=0;j<i;j++) if(skew(x[i],x[j],n))pred=false;
vector<bool> seen(1<<k);int nseen=0;for(uint64_t L:lags){int pattern=0;for(int j=0;j<k;j++)if((L>>x[j])&1)pattern|=1<<j;if(!seen[pattern]){seen[pattern]=true;nseen++;}}bool actual=nseen==(1<<k);if(actual!=pred){cerr<<"SHATTERING DISAGREEMENT n="<<n<<" k="<<k<<endl;exit(3);}if(actual){faces[k].push_back(x);f[k]++;}return;}for(int j=next;j<N;j++){x.push_back(j);dfs(j+1);x.pop_back();}};dfs(1);}
vector<int> rank(n+1);rank[0]=0;
for(int k=1;k<=n;k++){map<vector<int>,int> ids;for(int i=0;i<(int)faces[k-1].size();i++)ids[faces[k-1][i]]=i;int r=faces[k-1].size(),words=(r+63)/64;vector<vector<uint64_t>> cols;cols.reserve(f[k]);for(const auto &s:faces[k]){vector<uint64_t> v(words);for(int j=0;j<k;j++){auto t=s;t.erase(t.begin()+j);int idx=ids.at(t);v[idx/64]^=1ULL<<(idx%64);}cols.push_back(move(v));}rank[k]=binaryrank(move(cols),r);}
cout<<"n="<<n<<" lagrangians="<<lags.size()<<" faces=";for(int k=0;k<=n;k++)cout<<f[k]<<(k==n?" ":",");cout<<"augmented_boundary_ranks=";for(int k=1;k<=n;k++)cout<<rank[k]<<(k==n?" ":",");cout<<"reduced_betti=";for(int k=1;k<=n;k++){int b=f[k]-rank[k]-(k==n?0:rank[k+1]);cout<<b<<(k==n?"":",");}cout<<endl;
if(n==1&&!(lags.size()==3&&f[1]==3&&rank[1]==1))return 4;
if(n==2&&!(lags.size()==15&&f[1]==15&&f[2]==45&&rank[1]==1&&rank[2]==14))return 5;
if(n==3&&!(lags.size()==135&&f[1]==63&&f[2]==945&&f[3]==3780&&rank[1]==1&&rank[2]==62&&rank[3]==883))return 6;
}cout<<"ALL PASS"<<endl;}
