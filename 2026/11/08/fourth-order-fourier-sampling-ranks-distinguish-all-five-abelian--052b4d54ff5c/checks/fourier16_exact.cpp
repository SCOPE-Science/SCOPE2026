// Exact cyclotomic rank census for all abelian groups of order sixteen.
// All determinants are computed in Z[z]/(z^8+1), with z a primitive 16th root.
#include <bits/stdc++.h>
using namespace std;
using Quad=array<int,4>;
struct Group{
 vector<int> mod;
 vector<vector<int>> xy;
 int exponent[16][16]{};
 int sum[16][16]{};
 string name;
};
Group group(vector<int> mod){
 Group g;g.mod=mod;
 for(int i=0;i<(int)mod.size();i++){if(i)g.name+="x";g.name+=to_string(mod[i]);}
 for(int x=0;x<16;x++){int y=x;vector<int> a;for(int n:mod){a.push_back(y%n);y/=n;}g.xy.push_back(a);}
 for(int x=0;x<16;x++)for(int y=0;y<16;y++){
  int e=0,z=0,mult=1;
  for(int j=0;j<(int)mod.size();j++){
   e+=(16/mod[j])*g.xy[x][j]*g.xy[y][j];
   z+=((g.xy[x][j]+g.xy[y][j])%mod[j])*mult;mult*=mod[j];
  }
  g.exponent[x][y]=e%16;g.sum[x][y]=z;
 }
 return g;
}
vector<Quad> fours(){vector<Quad> out;for(int a=0;a<16;a++)for(int b=a+1;b<16;b++)for(int c=b+1;c<16;c++)for(int d=c+1;d<16;d++)out.push_back({a,b,c,d});return out;}
vector<pair<Quad,int>> orbits(const Group& g,const vector<Quad>& all){
 vector<pair<Quad,int>> out;
 for(auto a:all){
  unsigned mask=0;for(int v:a)mask|=1u<<v;
  unsigned minmask=mask;set<unsigned> orbit;
  for(int x=0;x<16;x++){
   unsigned t=0;for(int v:a)t|=1u<<g.sum[v][x];
   minmask=min(minmask,t);orbit.insert(t);
  }
  if(mask==minmask)out.push_back({a,(int)orbit.size()});
 }
 return out;
}
struct Term{array<int,4> perm;int parity;};
vector<Term> perms[5];
void init(){for(int n=2;n<=4;n++){
 array<int,4> a{};iota(a.begin(),a.end(),0);
 do{int c=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)c+=(a[i]>a[j]);perms[n].push_back({a,(c%2)?-1:1});}
 while(next_permutation(a.begin(),a.begin()+n));
 }}
bool minor_nonzero(int e[4][4],int n,const array<int,4>& rs,const array<int,4>& cs){
 int coeff[8]{};
 for(auto t:perms[n]){
  int power=0;
  for(int i=0;i<n;i++)power+=e[rs[i]][cs[t.perm[i]]];
  power%=16;
  coeff[power&7]+=t.parity*((power&8)?-1:1);
 }
 for(int c:coeff)if(c)return true;
 return false;
}
int exactrank(int e[4][4]){
 const array<int,4> full={0,1,2,3};
 if(minor_nonzero(e,4,full,full))return 4;
 for(int ar=0;ar<4;ar++)for(int ac=0;ac<4;ac++){
   array<int,4> rs{},cs{};int ri=0,ci=0;
   for(int i=0;i<4;i++){
    if(i!=ar)rs[ri++]=i;
    if(i!=ac)cs[ci++]=i;
   }
   if(minor_nonzero(e,3,rs,cs))return 3;
 }
 for(int a=0;a<4;a++)for(int b=a+1;b<4;b++)for(int c=0;c<4;c++)for(int d=c+1;d<4;d++){
  if(minor_nonzero(e,2,{a,b,0,0},{c,d,0,0}))return 2;
 }
 return 1;
}
int main(){
 init();auto all=fours();
 for(auto mod:vector<vector<int>>{{16},{8,2},{4,4},{4,2,2},{2,2,2,2}}){
  Group g=group(mod);auto rows=orbits(g,all);
  long long ranks[5]={};
  for(auto [a,mult]:rows)for(auto b:all){
   int E[4][4];for(int i=0;i<4;i++)for(int j=0;j<4;j++)E[i][j]=g.exponent[a[i]][b[j]];
   ranks[exactrank(E)]+=mult;
  }
  long long total=0;for(int r=1;r<=4;r++)total+=ranks[r];
  if(total!=3312400){cerr<<"BAD_TOTAL\n";return 1;}
  cout<<g.name;
  for(int r=1;r<=4;r++)cout<<" "<<ranks[r];
  cout<<"\n";
 }
}
