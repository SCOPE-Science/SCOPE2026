// Reproduce the full six-vertex strong-tournament Walsh spectrum by independent
// orientation enumeration, reachability, Walsh butterflies and graph-support orbits.
// g++ -O3 -std=c++17 verify_tournament_enumeration.cpp -o enumeration
// ./enumeration [--dump coefficients.txt] [--orbits support_orbits.tsv]
#include <algorithm>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 constexpr int n=6,m=15,N=1<<m;
 vector<pair<int,int>> e;int idx[6][6]{};
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){idx[i][j]=idx[j][i]=int(e.size());e.emplace_back(i,j);}
 vector<int> W(N,0), adj(n);int strong=0;
 for(int x=0;x<N;x++){
  fill(adj.begin(),adj.end(),0);
  for(int k=0;k<m;k++){auto [i,j]=e[k];if(x>>k&1)adj[i]|=1<<j;else adj[j]|=1<<i;}
  bool connected=true;
  for(int v=0;v<n&&connected;v++){
   int reach=1<<v;
   for(;;){int next=reach;for(int u=0;u<n;u++)if(reach>>u&1)next|=adj[u];if(next==reach)break;reach=next;}
   if(reach!=(1<<n)-1)connected=false;
  }
  if(connected){W[x]=1;++strong;}
 }
 for(int step=1;step<N;step*=2)
  for(int i=0;i<N;i+=2*step)
   for(int j=0;j<step;j++){
    int a=W[i+j],b=W[i+j+step];W[i+j]=a+b;W[i+j+step]=a-b;
   }
 map<int,int> magnitude,zero_by_support;int rank=0,smallest=1<<30;long long squares=0;
 for(int s=0;s<N;s++){
  int z=W[s];magnitude[abs(z)]++;squares+=1LL*z*z;
  if(z){rank++;smallest=min(smallest,abs(z));}else zero_by_support[__builtin_popcount((unsigned)s)]++;
 }
 assert(strong==22320 && rank==8416 && smallest==16 && squares==1LL*N*strong);
 vector<int> canon(N),forced(N,0);iota(canon.begin(),canon.end(),0);
 vector<int> perm(n);iota(perm.begin(),perm.end(),0);
 do{
  int dest[m], reverse_mask=0;
  for(int k=0;k<m;k++){
   auto [i,j]=e[k];dest[k]=idx[perm[i]][perm[j]];
   if(perm[i]>perm[j])reverse_mask|=1<<k;
  }
  for(int s=0;s<N;s++){
   int t=0;for(int k=0;k<m;k++)if(s>>k&1)t|=1<<dest[k];
   canon[s]=min(canon[s],t);
   if(t==s && __builtin_parity((unsigned)(s&reverse_mask)))forced[s]=1;
  }
 }while(next_permutation(perm.begin(),perm.end()));
 map<int,int> orbit_size;for(int s=0;s<N;s++)orbit_size[canon[s]]++;
 assert(orbit_size.size()==156);
 int zero_types=0,exception_types=0,exception_members=0,forced_zero_members=0;
 vector<string> lines;
 for(const auto &[rep,size]:orbit_size){
  int mag=abs(W[rep]),degree=__builtin_popcount((unsigned)rep);
  for(int s=0;s<N;s++)if(canon[s]==rep){assert(abs(W[s])==mag);assert(forced[s]==forced[rep]);}
  bool symmetry_forced=(degree%2==1)||forced[rep];
  if(mag==0){zero_types++;if(symmetry_forced)forced_zero_members+=size;else{
    exception_types++;exception_members+=size;
    assert(degree==8 && (rep==958||rep==1883) && size==360);
  }}else assert(!symmetry_forced);
  lines.push_back(to_string(rep)+"\t"+to_string(degree)+"\t"+to_string(size)+"\t"+to_string(mag)+"\t"+(symmetry_forced?"1":"0"));
 }
 assert(zero_types==124 && exception_types==2 && exception_members==720 && forced_zero_members==23632);
 vector<int> P(N);for(int i=0;i<N;i++)P[i]=(W[i]!=0);
 for(int step=1;step<N;step*=2)
  for(int i=0;i<N;i+=2*step)
   for(int j=0;j<step;j++){
    int a=P[i+j],b=P[i+j+step];P[i+j]=a+b;P[i+j+step]=a-b;
   }
 long long norm_num=0;for(int z:P)norm_num+=abs(z);assert(norm_num==1399040);
 cout<<"orientation enumeration: strong="<<strong<<" rank="<<rank<<" nullity="<<N-rank
     <<" min_nonzero="<<smallest<<" orbits="<<orbit_size.size()<<" zero_orbits="<<zero_types
     <<" exceptional_orbits="<<exception_types<<" exceptional_members="<<exception_members
     <<" projection_numerator="<<norm_num<<"\n";
 cout<<"hist:";for(auto [k,v]:magnitude)cout<<" "<<k<<":"<<v;cout<<"\n";
 cout<<"zero-support:";for(auto[k,v]:zero_by_support)cout<<" "<<k<<":"<<v;cout<<"\n";
 for(int i=1;i+1<argc;i+=2){string option=argv[i];if(option=="--dump"){
   ofstream f(argv[i+1]);for(auto x:W)f<<x<<'\n';
  }else if(option=="--orbits"){
   ofstream f(argv[i+1]);f<<"representative\tsupport_size\torbit_size\tabsolute_walsh\tsymmetry_forced\n";
   for(auto &s:lines)f<<s<<'\n';
  }else {cerr<<"unknown option\n";return 2;}
 }
}
