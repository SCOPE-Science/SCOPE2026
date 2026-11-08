#include <bits/stdc++.h>
using namespace std;
using A4=array<int,4>;
struct Group {
  vector<int> mod;
  vector<vector<int>> coords;
  int expn[16][16]{};
  int add[16][16]{};
  string label;
};
int modpow(int a,int e,int p=97){int r=1;for(;e;e>>=1,a=a*a%p)if(e&1)r=r*a%p;return r;}
vector<A4> sets4(){vector<A4> s;for(int a=0;a<16;a++)for(int b=a+1;b<16;b++)for(int c=b+1;c<16;c++)for(int d=c+1;d<16;d++)s.push_back({a,b,c,d});return s;}
Group makegroup(vector<int> mod){
 Group g;g.mod=mod;g.label="";for(size_t k=0;k<mod.size();k++){if(k)g.label+="x";g.label+=to_string(mod[k]);}
 for(int x=0;x<16;x++){int w=x;vector<int> a;for(int n:mod){a.push_back(w%n);w/=n;}g.coords.push_back(a);}
 for(int x=0;x<16;x++)for(int y=0;y<16;y++){
   int e=0,z=0,mult=1;
   for(size_t j=0;j<mod.size();j++){
     e+=(16/mod[j])*g.coords[x][j]*g.coords[y][j];
     z+=((g.coords[x][j]+g.coords[y][j])%mod[j])*mult;
     mult*=mod[j];
   }
   g.expn[x][y]=e%16;g.add[x][y]=z;
 }
 return g;
}
int rank4(const int tab[16][16],const A4 &as,const A4 &bs,const int inv[97]){
 int a[4][4];for(int i=0;i<4;i++)for(int j=0;j<4;j++)a[i][j]=tab[as[i]][bs[j]];
 int r=0;for(int j=0;j<4 && r<4;j++){
  int p=r;while(p<4 && !a[p][j])p++;if(p==4)continue;
  if(p!=r)for(int k=j;k<4;k++)swap(a[p][k],a[r][k]);
  int invp=inv[a[r][j]];
  for(int i=r+1;i<4;i++){if(!a[i][j])continue;int f=a[i][j]*invp%97;
   for(int k=j+1;k<4;k++){int x=a[i][k]-f*a[r][k]%97;a[i][k]=x<0?x+97:x;}
   a[i][j]=0;
  }r++;
 }return r;
}
uint16_t shifted(const Group& g,const A4 &a,int x){uint16_t s=0;for(int k:a)s|=uint16_t(1)<<g.add[k][x];return s;}
vector<pair<A4,int>> roworbits(const Group& g,const vector<A4>& ss){
 vector<pair<A4,int>> ret;
 for(const auto& a:ss){
  uint16_t mask=0;for(int x:a)mask|=uint16_t(1)<<x;
  uint16_t mn=mask;
  set<uint16_t> trans;
  for(int x=0;x<16;x++){auto v=shifted(g,a,x);mn=min(mn,v);trans.insert(v);}
  if(mask==mn)ret.push_back({a,int(trans.size())});
 }
 return ret;
}
int main(){
 auto ss=sets4();int inv[97]{};for(int x=1;x<97;x++)inv[x]=modpow(x,95);
 int g=5;int z=modpow(g,6);if(modpow(z,16)!=1 || modpow(z,8)==1){cerr<<"BAD_ROOT"<<endl;return 1;}
 vector<int> roots;for(int k=1;k<16;k+=2)roots.push_back(modpow(z,k));
 cout<<"ROOTS";for(int x:roots)cout<<" "<<x;cout<<"\n";
 for(auto mods:vector<vector<int>>{{16},{8,2},{4,4},{4,2,2},{2,2,2,2}}){
  auto G=makegroup(mods);
  vector<pair<A4,int>> orbs; for(auto a:ss)orbs.push_back({a,1});
  int tab[8][16][16]{};
  for(int k=0;k<8;k++){
   int powers[16];for(int j=0;j<16;j++)powers[j]=modpow(roots[k],j);
   for(int x=0;x<16;x++)for(int y=0;y<16;y++)tab[k][x][y]=powers[G.expn[x][y]];
  }
  long long count[5]={};long long hist[5][5]={};
  for(auto [a,weight]:orbs){
   for(const auto &b:ss){
    int rank=rank4(tab[0],a,b,inv);
    if(rank<4)for(int k=1;k<8 && rank<4;k++)rank=max(rank,rank4(tab[k],a,b,inv));
    if(rank<1 || rank>4){cerr<<"BAD_RANK\n";return 1;}
    count[rank]+=weight;
    hist[rank][0]++;
   }
  }
  long long total=0;for(int r=1;r<=4;r++)total+=count[r];
  if(total!=(long long)ss.size()*ss.size()){cerr<<"BAD_TOTAL\n";return 1;}
  cout<<"GROUP "<<G.label<<" ROW_ORBITS "<<orbs.size()<<" COUNTS";
  for(int r=1;r<=4;r++)cout<<" "<<count[r];
  cout<<" TOTAL "<<total<<"\n"<<flush;
 }
}
