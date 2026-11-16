// Standalone exact verification for additive Fourier spectra of Petersen proper colourings.
// Build: c++ -O2 -std=c++17 check.cpp -o check && ./check
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <utility>
#include <vector>
using namespace std;
using LL=long long;
constexpr int V=10;
vector<int> vertices;
vector<pair<int,int>> edges;
void graph(){
 for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)vertices.push_back((1<<i)|(1<<j));
 for(int i=0;i<V;i++)for(int j=i+1;j<V;j++)if((vertices[i]&vertices[j])==0)edges.push_back({i,j});
 assert(edges.size()==15);
}
vector<int> colorings(int q){
 const int N=(q==4?1<<20:59049); vector<int> ans;
 for(int mask=0;mask<N;mask++){
  int x=mask;int col[V];
  for(int j=0;j<V;j++){col[j]=x%q;x/=q;}
  bool ok=true;for(auto [i,j]:edges)if(col[i]==col[j]){ok=false;break;}
  if(ok)ans.push_back(mask);
 }
 return ans;
}
void fwht(vector<int>& a){
 for(int len=1;len<(int)a.size();len*=2)
  for(int i=0;i<(int)a.size();i+=len*2)
   for(int j=0;j<len;j++){
    int x=a[i+j],y=a[i+j+len];a[i+j]=x+y;a[i+j+len]=x-y;
   }
}
int balanced(int mask){int s=0;for(int j=0;j<V;j++){s^=mask&3;mask>>=2;}return s==0;}
int degree(int mask){int k=0;for(int j=0;j<V;j++){k+=((mask&3)!=0);mask>>=2;}return k;}
int pairing(int x,int u){return __builtin_parity((unsigned)(x&u))?-1:1;}
int permuted(int mask,int t){
 int p[5];iota(p,p+5,0);swap(p[t],p[t+1]);
 int next=0;
 for(int j=0;j<V;j++){
  int v=0;for(int b=0;b<5;b++)if(vertices[j]>>b&1)v|=1<<p[b];
  int idx=find(vertices.begin(),vertices.end(),v)-vertices.begin();
  next|=((mask>>(2*j))&3)<<(2*idx);
 }
 return next;
}
int relabel(int mask,int t){
 int next=0;
 for(int j=0;j<V;j++){
  int d=(mask>>(2*j))&3;
  // two generators of GL(2,2) acting on frequency labels
  if(t==0){if(d==1)d=2;else if(d==2)d=1;}
  else {if(d==2)d=3;else if(d==3)d=2;}
  next|=d<<(2*j);
 }
 return next;
}
void verify_four(){
 const int N=1<<20;auto C=colorings(4);assert(C.size()==12960);
 // Check the independent-set partition types against canonical color relabeling.
 set<array<int,V>> partitions;
 for(int x:C){
  int relabelled[4]={-1,-1,-1,-1}, next_label=0;
  array<int,V> part{};
  for(int j=0;j<V;j++){
   int v=(x>>(2*j))&3;
   if(relabelled[v]<0)relabelled[v]=next_label++;
   part[j]=relabelled[v];
  }
  partitions.insert(part);
 }
 int with_three=0,with_four=0;
 for(auto &p:partitions){int k=*max_element(p.begin(),p.end())+1;
  if(k==3)with_three++; else if(k==4)with_four++; else assert(false);
 }
 assert(with_three==20 && with_four==520);
 vector<int> F(N,0);for(int x:C)F[x]++;
 fwht(F);
 map<int,LL> hist;int zero=0,minabs=1e9,maxabs=0;
 LL parseval=0;int extra=0;vector<int> extra_weight(V+1,0);
 int witness=-1;
 for(int u=0;u<N;u++){
  int w=F[u];hist[w]++;parseval+=(LL)w*w;
  if(w==0){zero++;if(balanced(u)){extra++;extra_weight[degree(u)]++;if(degree(u)==6 && witness<0)witness=u;}}
  else {minabs=min(minabs,abs(w));maxabs=max(maxabs,abs(w));}
  if(!balanced(u))assert(w==0);
  assert(w%16==0);
 }
 assert(parseval==(LL)N*(LL)C.size());
 assert(zero==801222 && extra==14790 && hist.size()==83);
 assert(minabs==16 && maxabs==12960);
 assert(extra_weight[6]==1110 && extra_weight[7]==2880 && extra_weight[8]==3420 && extra_weight[9]==5040 && extra_weight[10]==2340);
 for(int i=0;i<6;i++)assert(extra_weight[i]==0);
 assert(witness>=0);
 int direct=0,positive=0,negative=0;
 for(int x:C){int w=pairing(x,witness);direct+=w;positive+=(w==1);negative+=(w==-1);}
 assert(direct==0 && positive==6480 && negative==6480);
 vector<int> K(N,0);for(int u=0;u<N;u++)K[u]=F[u]!=0;
 fwht(K);LL abs_sum=0;
 for(int x:K)abs_sum+=llabs((LL)x);
 assert(abs_sum==87263536);
 // Independent check: quotient all balanced frequencies by graph Aut(Petersen) = S5 and GL(2,2).
 // For each orbit representative, recompute the character sum directly from proper colourings.
 vector<unsigned char> seen(N,0);
 map<int,LL> orbit_hist;
 int orbit_count=0,covered=0;
 vector<int> queue_;queue_.reserve(N/4);
 for(int u=0;u<N;u++){
  if(!balanced(u) || seen[u])continue;
  queue_.clear(); queue_.push_back(u);seen[u]=1;
  for(size_t h=0;h<queue_.size();h++){
   int z=queue_[h];
   for(int t=0;t<6;t++){
    int y=t<4?permuted(z,t):relabel(z,t-4);
    assert(balanced(y));
    if(!seen[y]){seen[y]=1;queue_.push_back(y);}
   }
  }
  int v=0;
  for(int x:C)v+=pairing(x,u);
  assert(v==F[u]);
  for(int y:queue_)assert(F[y]==v);
  covered+=(int)queue_.size();orbit_hist[v]+=queue_.size();orbit_count++;
 }
 assert(covered==N/4);
 for(auto [v,n]:orbit_hist)if(v!=0)assert(hist[v]==n);
 for(auto [v,n]:hist)if(v!=0)assert(orbit_hist[v]==n);
 assert(hist[0]==orbit_hist[0]+3LL*N/4);
 // All 83 exact signed levels are embedded as a separate human-readable certificate.
 ifstream csv("SPECTRUM_Q4.csv");assert(csv.good());
 string row;getline(csv,row);assert(row=="multiplier,multiplicity");
 map<int,LL> cert;
 while(getline(csv,row)){if(row.empty())continue;size_t pos=row.find(',');
  assert(pos!=string::npos);int v=stoi(row.substr(0,pos));
  LL m=stoll(row.substr(pos+1));assert(cert.insert({v,m}).second);
 }
 assert(cert==hist);
 cout<<"FOUR_COLOR_PASS colorings="<<C.size()<<" frequencies="<<N
     <<" zero="<<zero<<" balanced_extra_zero="<<extra
     <<" rank="<<N-zero<<" min_nonzero="<<minabs
     <<" projection_abs_sum="<<abs_sum<<" projection_norm=5453971/65536"
     <<" minimum_extra_degree=6 count_at_degree6="<<extra_weight[6]
     <<" witness="<<witness<<" direct_positive="<<positive<<" direct_negative="<<negative
     <<" balanced_orbits="<<orbit_count<<" spectral_levels="<<hist.size()<<"\n";
}
// Cyclotomic integer encoding a+b*omega, omega^2+omega+1=0.
using Zomega=pair<int,int>;
void verify_three(){
 auto C=colorings(3);assert(C.size()==120);
 const int N=59049;vector<Zomega> F(N,{0,0});
 for(int x:C)F[x]={1,0};
 int p=1;
 for(int k=0;k<V;k++){
  for(int base=0;base<N;base+=3*p)
   for(int j=0;j<p;j++){
    int a=base+j,b=a+p,c=b+p;
    auto A=F[a],B=F[b],D=F[c];
    F[a]={A.first+B.first+D.first,A.second+B.second+D.second};
    F[b]={A.first-B.second+D.second-D.first,A.second+B.first-B.second-D.first};
    F[c]={A.first+B.second-B.first-D.second,A.second-B.first+D.first-D.second};
   }
  p*=3;
 }
 int zero=0,mag=INT32_MAX,rep=-1;
 LL sumsq=0;
 for(int u=0;u<N;u++){
  auto [a,b]=F[u];assert(b==0);
  int s=0,z=u;
  for(int k=0;k<V;k++){s+=z%3;z/=3;}
  if(s%3!=0)assert(a==0);
  else{assert(a!=0 && (a+60)%9==0);if(abs(a)<mag){mag=abs(a);rep=u;}}
  zero+=(a==0);sumsq+=(LL)a*a;
 }
 assert(zero==39366 && mag==3 && sumsq==(LL)N*(LL)C.size());
 assert(rep>=0);
 // Independent direct cyclotomic evaluation of the chosen extremizing coefficient.
 int a=0,b=0;
 for(int x:C){int xx=x,uu=rep,e=0;
  for(int k=0;k<V;k++){e+=(xx%3)*(uu%3);xx/=3;uu/=3;}
  e%=3;if(e==0)a++;else if(e==1)b++;else{a--;b--;}
 }
 assert(b==0 && a==F[rep].first);
 cout<<"THREE_COLOR_PASS colorings="<<C.size()<<" frequencies="<<N
     <<" zero="<<zero<<" rank="<<N-zero
     <<" min_nonzero="<<mag<<" representative="<<rep<<" multiplier="<<a<<"\n";
}
int main(){graph();verify_three();verify_four();return 0;}
