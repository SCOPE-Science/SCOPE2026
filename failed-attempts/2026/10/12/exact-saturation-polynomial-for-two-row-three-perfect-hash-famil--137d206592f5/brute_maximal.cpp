#include <bits/stdc++.h>
using namespace std;
int main(int argc,char**argv){int q=argc>1?stoi(argv[1]):5;if(q<3 || q>5){cerr<<"This exhaustive checker is supported for q=3,4,5 only.\n";return 2;}int N=q*q;vector<vector<pair<int,int>>> triples(N);
for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++)if(c!=b)for(int d=0;d<q;d++)if(d!=a){ // path (a,b), (a,c), (d,c)
 int e=a*q+b, f=a*q+c,g=d*q+c;
 triples[e].emplace_back(f,g);triples[f].emplace_back(e,g);triples[g].emplace_back(e,f);
}
unsigned long long good=0, maximal=0;map<int,unsigned long long> sizes;
auto permitted=[&](uint64_t mask,int e){for(auto [f,g]:triples[e])if((mask>>f&1ULL)&&(mask>>g&1ULL))return false;return true;};
function<void(int,uint64_t)>dfs=[&](int e,uint64_t mask){if(e==N){good++;bool maxv=true;for(int a=0;a<N;a++)if(!(mask>>a&1)&&permitted(mask,a)){maxv=false;break;}if(maxv){maximal++;sizes[__builtin_popcountll(mask)]++;}return;}dfs(e+1,mask);if(permitted(mask,e))dfs(e+1,mask|(1ULL<<e));};dfs(0,0);
cout<<"q="<<q<<" valid="<<good<<" maximal="<<maximal<<" sizes=";for(auto[k,v]:sizes)cout<<k<<":"<<v<<" ";cout<<"\n";}
