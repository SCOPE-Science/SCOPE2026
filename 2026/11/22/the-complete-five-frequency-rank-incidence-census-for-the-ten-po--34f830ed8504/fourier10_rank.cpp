// Exact 5-by-5 Fourier minor rank census over Q(zeta_10).
// The four primitive tenth roots modulo 401 certify every minor of order <=5;
// see the mathematical reduction in RESULT.md.
#include <bits/stdc++.h>
using namespace std;
constexpr int p=401;
constexpr int roots[4]={29,83,329,362};
int mod(int x){x%=p;return x<0?x+p:x;}
int inverse(int x){int a=1,b=x,e=p-2;while(e){if(e&1)a=a*b%p;b=b*b%p;e>>=1;}return a;}
int rank5(const array<int,5>& r,const array<int,5>& c,const int pw[10]){
 int m[5][5];
 for(int i=0;i<5;++i)for(int j=0;j<5;++j)m[i][j]=pw[(r[i]*c[j])%10];
 int rk=0;
 for(int j=0;j<5;++j){
  int t=rk;
  while(t<5 && m[t][j]==0)++t;
  if(t==5)continue;
  for(int h=j;h<5;++h)swap(m[rk][h],m[t][h]);
  int inv=inverse(m[rk][j]);
  for(int i=rk+1;i<5;++i){
   if(!m[i][j])continue;
   int ratio=(m[i][j]*inv)%p;
   for(int k=j;k<5;++k)m[i][k]=mod(m[i][k]-ratio*m[rk][k]);
  }
  ++rk;if(rk==5)break;
 }
 return rk;
}
struct Entry{int mask;array<int,5> idx;};
int apply(int mask,int a,int b){int ans=0;for(int x=0;x<10;++x)if(mask>>x&1)ans|=1<<((a*x+b)%10);return ans;}
int canon(int mask){int b=1024;for(int a:{1,3,7,9})for(int k=0;k<10;k++)b=min(b,apply(mask,a,k));return b;}
bool type221(const array<int,5> &arr){int n[5]={0,0,0,0,0};for(int v:arr)n[v%5]++;sort(n,n+5);return n[0]==0&&n[1]==0&&n[2]==1&&n[3]==2&&n[4]==2;}
int main(){
 array<array<int,10>,4> P{};
 for(int u=0;u<4;++u){int v=1;for(int k=0;k<10;++k){P[u][k]=v;v=(v*roots[u])%p;}if(v!=1||P[u][5]!=400||P[u][2]==1){cerr<<"nonprimitive root\n";return 1;}}
 for(int u=0;u<4;u++)for(int v=u+1;v<4;v++)if(roots[u]==roots[v]){cerr<<"repeated root\n";return 6;}
 vector<Entry> sets;for(int mask=0;mask<1024;++mask)if(__builtin_popcount((unsigned)mask)==5){Entry e;e.mask=mask;int j=0;for(int k=0;k<10;++k)if(mask>>k&1)e.idx[j++]=k;sets.push_back(e);}
 map<int,array<long long,6>> orbits,rep;
 map<int,int> orbitSize;
 array<long long,6> total{};
 map<int,array<long long,6>> representative;
 for(auto &R:sets){
  array<long long,6> counts{};
  for(auto &C:sets){int r=0;for(int h=0;h<4;++h)r=max(r,rank5(R.idx,C.idx,P[h].data()));if(r<1||r>5){cerr<<"invalid rank\n";return 2;}bool predicted=((R.mask==341||R.mask==682)&&type221(C.idx)) || ((C.mask==341||C.mask==682)&&type221(R.idx));
  if((r==3)!=predicted){cerr<<"rank-three geometry mismatch "<<R.mask<<" "<<C.mask<<" "<<r<<"\n";return 5;}
  counts[r]++;total[r]++;}
  int ca=canon(R.mask);
  if(!representative.count(ca))representative[ca]=counts;
  else if(representative[ca]!=counts){cerr<<"affine row orbit inconsistency "<<ca<<"\n";return 3;}
  orbitSize[ca]++;
 }
 long long checksum=0;
 cout<<"{\"method\":\"four-prime-field-primitive-root rank maximum\",\"modulus\":401,\"roots\":[29,83,329,362],\"size\":5,\"row_sets\":"<<sets.size()<<",\"column_sets\":"<<sets.size()<<",\"total_ranks\":[";
 for(int k=0;k<=5;++k){if(k)cout<<",";cout<<total[k];checksum+=total[k];}
 cout<<"],\"orbits\":[";
 bool first=true;
 for(auto &[ca,n]:orbitSize){if(!first)cout<<",";first=false;
  cout<<"{\"row_mask\":"<<ca<<",\"orbit_size\":"<<n<<",\"ranks\":[";
  for(int k=0;k<=5;++k){if(k)cout<<",";cout<<representative[ca][k];}
  cout<<"]}";}
 cout<<"],\"rank_three_criterion_all_pairs_verified\":true,\"total_pairs\":"<<checksum<<"}\n";
 if(checksum!=63504){cerr<<"total mismatch\n";return 4;}
}
