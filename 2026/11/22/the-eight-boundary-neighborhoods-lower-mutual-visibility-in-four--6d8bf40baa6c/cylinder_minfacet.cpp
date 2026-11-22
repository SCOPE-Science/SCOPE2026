#include<bits/stdc++.h>
using namespace std;
using U=unsigned __int128;
int n,N;vector<vector<U>> PM; vector<pair<int,int>> V;vector<int> di;
inline int idx(int r,int c){return r*n+c;}
inline int d(int a,int b){auto [ra,ca]=V[a];auto[rb,cb]=V[b];int x=abs(ra-rb);return min(x,4-x)+abs(ca-cb);}
void dfs(int x,int b,U intern,vector<U>&out){if(x==b){out.push_back(intern);return;}auto [r,c]=V[x];int cand[4]={idx((r+1)%4,c),idx((r+3)%4,c),c+1<n?idx(r,c+1):-1,c>0?idx(r,c-1):-1};int old=d(x,b);for(int y:cand)if(y>=0&&d(y,b)==old-1)dfs(y,b,intern|(U(1)<<y),out);}
inline bool vis(int a,int b,U set){auto &p=PM[a*N+b];for(auto mask:p)if(!(set&mask))return true;return false;}
inline bool feasible(const vector<int>&s,U mask){for(int i=0;i<(int)s.size();i++)for(int j=i+1;j<(int)s.size();j++)if(!vis(s[i],s[j],mask))return false;return true;}
inline bool canadd(const vector<int>&s,U mask,int w){for(int u:s)if(!vis(u,w,mask))return false;for(int i=0;i<(int)s.size();i++)for(int j=i+1;j<(int)s.size();j++)if(!vis(s[i],s[j],mask|(U(1)<<w)))return false;return true;}
long long n3=0,n4=0,wrong=0;set<U> found;set<U> expected;
U mask_of(const vector<int>&p){U v=0;for(int x:p)v|=(U(1)<<x);return v;}
void setup_expected(){
 for(int r=0;r<4;r++)for(int c:{0,n-1}){
   vector<int> p={idx(r,c),idx((r+1)%4,c),idx((r+3)%4,c)};
   if(c+1<n)p.push_back(idx(r,c+1));else p.push_back(idx(r,c-1));
   expected.insert(mask_of(p));
 }
 if(n==2)for(int parity=0;parity<=1;parity++){
   vector<int> p;for(int r=0;r<4;r++)for(int c=0;c<n;c++)if((r+c)%2==parity)p.push_back(idx(r,c));
   expected.insert(mask_of(p));
 }
}
void scan(const vector<int>&s){U mask=0;for(auto u:s)mask|=U(1)<<u;if(!feasible(s,mask))return;bool maximal=true;for(int w=0;w<N;w++)if(!(mask&(U(1)<<w)) && canadd(s,mask,w)){maximal=false;break;}if(!maximal)return;if(s.size()==3)n3++;if(s.size()==4){n4++;found.insert(mask);if(!expected.count(mask))wrong++;}}
int main(int argc,char**argv){n=atoi(argv[1]);N=4*n;V.resize(N);for(int r=0;r<4;r++)for(int c=0;c<n;c++)V[idx(r,c)]={r,c};PM.resize(N*N);setup_expected();for(int a=0;a<N;a++)for(int b=a+1;b<N;b++){dfs(a,b,0,PM[a*N+b]);for(auto &mask:PM[a*N+b])mask &=~(U(1)<<b);PM[b*N+a]=PM[a*N+b];}
vector<int>s;auto start=chrono::steady_clock::now();for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++){s={a,b,c};scan(s);}for(int a=0;a<N;a++)for(int b=a+1;b<N;b++)for(int c=b+1;c<N;c++)for(int d=c+1;d<N;d++){s={a,b,c,d};scan(s);}cout<<"n="<<n<<" size3_facets="<<n3<<" size4_facets="<<n4<<" expected="<<expected.size()<<" incorrect="<<wrong<<" agreement="<<(found==expected?"YES":"NO")<<"\n";
if(n3||wrong||found!=expected)return 2;}
