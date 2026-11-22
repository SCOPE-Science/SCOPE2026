#include <bits/stdc++.h>
using namespace std;
static int parity(unsigned x){return __builtin_parity(x);}
static int bil(int x,int y){return parity((x&21u)&((y&42u)>>1))^parity(((x&42u)>>1)&(y&21u));}
static int q0(int x){int v=0;for(int i=0;i<3;i++)v^=((x>>(2*i))&(x>>(2*i+1))&1);return v;}
static int act(uint64_t g,int v){int u=0;for(int i=0;i<6;i++)if(v&(1<<i))u^=(g>>(6*i))&63;return u;}
static uint64_t mult(uint64_t a,uint64_t b){uint64_t c=0;for(int j=0;j<6;j++)c|=(uint64_t)act(a,(b>>(6*j))&63)<<(6*j);return c;}
static uint64_t trans(uint64_t g,int v){for(int i=0;i<6;i++)if(bil(1<<i,v))g^=(uint64_t)act(g,v)<<(6*i);return g;}
static uint64_t identity(){uint64_t r=0;for(int i=0;i<6;i++)r|=(uint64_t)(1<<i)<<(6*i);return r;}
static vector<int> theta_perm(uint64_t g,int paritytype){
 vector<int>theta;int index[64];fill(index,index+64,-1);
 for(int a=0;a<64;a++)if(q0(a)==paritytype){index[a]=(int)theta.size();theta.push_back(a);}
 vector<int>p(theta.size());
 for(size_t j=0;j<theta.size();j++){
  int a=theta[j],b=0;
  for(int i=0;i<6;i++){int img=act(g,1<<i);if(q0(img)^bil(a,img))b|=1<<(i^1);}
  if(index[b]<0){cerr<<"Theta parity not preserved!\n";exit(1);}p[j]=index[b];
 }
 return p;
}
static string cycles(const vector<int>&p){vector<int>n;vector<bool>vis(p.size());
 for(size_t i=0;i<p.size();i++)if(!vis[i]){int j=i,v=0;do{vis[j]=true;v++;j=p[j];if(v>int(p.size()))abort();}while(j!=int(i));n.push_back(v);}
 sort(n.begin(),n.end());map<int,int>c;for(int a:n)c[a]++;string s;
 for(auto [a,b]:c){if(!s.empty())s+=" ";s+=to_string(a)+"^"+to_string(b);}return s;
}
int main(){const auto E=identity();vector<int>gens={1,2,4,8,16,32,21,42,5};
 vector<uint64_t>G;G.reserve(1500000);unordered_set<uint64_t>S;S.reserve(2100000);
 G.push_back(E);S.insert(E);
 for(size_t i=0;i<G.size();i++)for(int v:gens){uint64_t a=trans(G[i],v);if(S.insert(a).second)G.push_back(a);}
 if(G.size()!=1451520){cerr<<"Wrong group size\n";return 1;}
 uint64_t A=0;
 for(uint64_t g:G){uint64_t pow=E;for(int j=0;j<9;j++)pow=mult(g,pow);
   if(pow!=E)continue;
   pow=E;for(int j=0;j<3;j++)pow=mult(g,pow);
   if(pow==E)continue;
   if(cycles(theta_perm(g,0))=="9^4" && cycles(theta_perm(g,1))=="1^1 9^3"){A=g;break;}
 }
 if(!A){cerr<<"No 9-cycle witness\n";return 2;}
 int centralizer=0;for(uint64_t g:G)if(mult(g,A)==mult(A,g))centralizer++;
 if(centralizer!=9){cerr<<"Unexpected centralizer\n";return 3;}
 cout<<"Sp6(2) elements="<<G.size()<<" even theta=36 odd theta=28\n";
 cout<<"order-9 witness="<<A<<" centralizer="<<centralizer<<"\n";
 uint64_t p=E;
 for(int k=0;k<9;k++){
  cout<<"power "<<k<<": even="<<cycles(theta_perm(p,0))<<" odd="<<cycles(theta_perm(p,1))<<"\n";
  p=mult(A,p);
 }
 if(p!=E)return 4;
 int q=19;int cnt[3]={};for(int c=1;c<q;c++){
  int x=1;for(int j=0;j<(q-1)/9;j++)x=x*c%q;
  int ord=1,v=x;while(v!=1){v=v*x%q;ord++;if(ord>9)abort();}
  if(ord==1)cnt[0]++;else if(ord==3)cnt[1]++;else if(ord==9)cnt[2]++;else abort();
 }
 cout<<"Kummer character orders over F19: "<<cnt[0]<<","<<cnt[1]<<","<<cnt[2]<<"\n";
 if(cnt[0]!=2||cnt[1]!=4||cnt[2]!=12)return 5;
}
