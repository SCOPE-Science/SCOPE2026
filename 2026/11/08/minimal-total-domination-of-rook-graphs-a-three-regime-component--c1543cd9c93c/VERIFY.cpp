// Reproducible finite checks for the minimal-total-domination classification.
// Compile: c++ -O2 -std=c++17 VERIFY.cpp -o verify && ./verify
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <tuple>
#include <algorithm>
#include <stdexcept>
using namespace std;
using Count=unsigned long long;
using Poly=map<int,Count>;
Count fac(int n){Count ans=1;for(int i=2;i<=n;i++)ans*=i;return ans;}
Count binom(int n,int k){if(k<0||k>n)return 0; Count x=1;for(int i=1;i<=k;i++)x=x*(n-i+1)/i;return x;}
map<tuple<int,int,bool>,Poly> memo;
Poly comp(int r,int c,bool pairs){
 auto key=make_tuple(r,c,pairs);auto it=memo.find(key);if(it!=memo.end())return it->second;
 Poly out;if(r==0&&c==0){out[0]=1;return memo[key]=out;}if(r<=0||c<=0)return memo[key]=out;
 vector<tuple<int,int,int,Count>> types;
 if(pairs){types.emplace_back(1,2,2,1);types.emplace_back(2,1,2,1);}
 else{
  for(int j=2;j<=c;j++)types.emplace_back(1,j,j,1);
  types.emplace_back(2,1,2,1);
  for(int j=2;j<=min(r,c-1);j++)types.emplace_back(j,j+1,2*j,fac(j+1));
 }
 for(auto [a,b,k,mult]:types){
  if(a>r||b>c)continue;
  Count ways=binom(r-1,a-1)*binom(c,b)*mult;
  for(auto [d,v]:comp(r-a,c-b,pairs))out[k+d]+=ways*v;
 }
 return memo[key]=out;
}
Poly formula(int m,int n){Poly p;
 for(int r=1;r<m;r++)for(auto [k,v]:comp(r,n,false))p[k]+=binom(m,r)*v;
 for(int c=1;c<n;c++)for(auto [k,v]:comp(c,m,false))p[k]+=binom(n,c)*v;
 for(auto [k,v]:comp(m,n,true))p[k]+=v;
 return p;
}
// Separate graph-theoretic checker: a rook attacks exactly the cells on its row or column.
bool is_total(uint64_t mask,const vector<uint64_t>& adj){
 for(uint64_t a:adj)if((a&mask)==0)return false;
 return true;
}
// Check the claimed component types directly, independently of the component DP.
bool structural(uint64_t mask,int m,int n){
 vector<int> dr(m,0),dc(n,0);
 for(int e=0;e<m*n;e++)if(mask&(1ULL<<e)){dr[e/n]++;dc[e%n]++;}
 int missing_r=count(dr.begin(),dr.end(),0),missing_c=count(dc.begin(),dc.end(),0);
 if(missing_r&&missing_c)return false;
 vector<int> seen(m+n,0);
 for(int start=0;start<m+n;start++){
  bool active=(start<m?dr[start]!=0:dc[start-m]!=0);
  if(!active||seen[start])continue;
  vector<int> queue={start};seen[start]=1;
  for(size_t h=0;h<queue.size();h++){
   int u=queue[h];for(int e=0;e<m*n;e++)if(mask&(1ULL<<e)){
    int a=e/n,b=m+e%n;if(u==a||u==b){int v=(u==a?b:a);if(!seen[v]){seen[v]=1;queue.push_back(v);}}
   }
  }
  vector<int> in_comp(m+n,0);for(int v:queue)in_comp[v]=1;
  int rs=0,cs=0,edges=0,kcenter=0,leaves=0;
  for(int v:queue){if(v<m)rs++;else cs++;}
  for(int e=0;e<m*n;e++)if((mask&(1ULL<<e))&&in_comp[e/n]&&in_comp[m+e%n])edges++;
  if(!missing_r&&!missing_c){
   if(edges!=2||!((rs==1&&cs==2)||(rs==2&&cs==1)))return false;
  }else if(missing_r){
   bool H=(rs==1&&cs==edges&&edges>=2);
   if(H){for(int v:queue)if(v>=m&&dc[v-m]!=1)H=false;}
   bool V=(rs==2&&cs==1&&edges==2);
   if(V){for(int v:queue)if(v<m&&dr[v]!=1)V=false;}
   bool B=(rs>=2&&cs==rs+1&&edges==2*rs);
   if(B){for(int v:queue){if(v<m&&dr[v]!=2)B=false; if(v>=m){if(dc[v-m]==rs)kcenter++;else if(dc[v-m]==1)leaves++;else B=false;}} B=B&&kcenter==1&&leaves==rs;}
   if(!(H||V||B))return false;
  }else{
   bool H=(cs==1&&rs==edges&&edges>=2);
   if(H){for(int v:queue)if(v<m&&dr[v]!=1)H=false;}
   bool V=(cs==2&&rs==1&&edges==2);
   if(V){for(int v:queue)if(v>=m&&dc[v-m]!=1)V=false;}
   bool B=(cs>=2&&rs==cs+1&&edges==2*cs);
   if(B){for(int v:queue){if(v>=m&&dc[v-m]!=2)B=false; if(v<m){if(dr[v]==cs)kcenter++;else if(dr[v]==1)leaves++;else B=false;}} B=B&&kcenter==1&&leaves==cs;}
   if(!(H||V||B))return false;
  }
 }
 return true;
}
int main(){
 vector<pair<int,int>> cases={{2,2},{2,3},{2,4},{3,3},{3,4},{3,5},{3,6},{4,4},{4,5},{4,6},{5,5}};
 Count all=0,minimal=0;
 for(auto [m,n]:cases){
  int N=m*n;vector<uint64_t> adj(N,0);
  for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j&&(i/n==j/n||i%n==j%n))adj[i]|=1ULL<<j;
  Poly exact;uint64_t bound=1ULL<<N;all+=bound-1;
  for(uint64_t mask=1;mask<bound;mask++){
   if(!is_total(mask,adj))continue;
   bool is_min=true;uint64_t sub=mask;
   while(sub){int e=__builtin_ctzll(sub);sub&=sub-1;
    if(is_total(mask^(1ULL<<e),adj)){is_min=false;break;}
   }
   if(is_min){minimal++;exact[__builtin_popcountll(mask)]++;
    if(!structural(mask,m,n)){cerr<<"BAD "<<m<<"x"<<n<<" mask="<<mask<<"\n";throw runtime_error("minimal family not classified");}
   }
  }
  if(exact!=formula(m,n))throw runtime_error("enumerator does not match exhaustive search");
  cout<<m<<"x"<<n<<" ";for(auto [k,v]:exact)cout<<k<<":"<<v<<" ";cout<<"\n";
 }
 Poly big=formula(6,6);
 if(big!=Poly({{6,5112},{7,36720},{8,251100},{10,8640}}))throw runtime_error("large coefficient check failed");
 cout<<"VERIFY_OK instances="<<cases.size()<<" examined_subsets="<<all
     <<" minimal_sets="<<minimal<<" component_types=PASS coefficients=PASS square_6x6=PASS\n";
}
