#include <bits/stdc++.h>
using namespace std;
constexpr int P=5,Q=6;
const int u[6]={1,1,0,-1,-1,0},v[6]={0,1,1,0,-1,-1};
struct Ptn {array<int,P> a;};
vector<Ptn> seqs(int q){vector<Ptn>s; for(int z=0;z<(int)pow(q,P-1);z++){int n=z;Ptn t;t.a[0]=0; for(int i=1;i<P;i++){t.a[i]=n%q;n/=q;}s.push_back(t);}return s;}
int main(){const int q=6;vector<Ptn> ss=seqs(q);map<pair<int,int>,long long> cnt;map<pair<int,int>,array<int,10>> ex;map<string,long long> profiles;
long long sum=0;int worst=0;
for(int fi=0;fi<(int)ss.size();fi++)for(int gi=0;gi<(int)ss.size();gi++){
 auto &f=ss[fi].a,&g=ss[gi].a;int dc=0,flat=0;array<int,5> rzs{};
 for(int x=0;x<P;x++){
  int rs=0,is=0;bool same=1;int first=-1;
  for(int t=0;t<P;t++){
   int e=(q+f[t]-g[(t-x+P)%P])%q;
   int z=e*(6/q);rs+=u[z];is+=v[z];if(first==-1)first=e; else if(e!=first)same=0;
  }
  if(rs==0&&is==0){dc++;rzs[x]++;}
  if(same){flat++;rzs[x]+=4;}
 }
 int support=P*P-dc-4*flat;cnt[{dc,flat}]++;int zeros=25-support;worst=max(worst,zeros);
 if(ex.find({dc,flat})==ex.end()){array<int,10> w{};copy(f.begin(),f.end(),w.begin());copy(g.begin(),g.end(),w.begin()+5);ex[{dc,flat}]=w;}
 sort(rzs.begin(),rzs.end());string key;for(int x:rzs)key+=to_string(x);profiles[key]++;
 sum++;
}
const map<pair<int,int>,long long> expected={{{0,0},1319020},{{0,1},5875},{{0,5},1},{{1,0},322200},{{2,0},30600},{{2,1},600},{{3,0},1200},{{5,0},120}};
if(cnt!=expected || sum!=1679616 || worst!=20){cerr<<"FAILED: wrong count\n";return 1;}
const map<string,long long> expected_profiles={{"00000",1319020},{"00001",322200},{"00004",5875},{"00011",30600},{"00111",1200},{"00114",600},{"11111",120},{"44444",1}};
if(profiles!=expected_profiles){cerr<<"FAILED: wrong profile\n";return 1;}
cout<<"PASS: all 1,679,616 normalized pairs, structural Fourier tests\n";
for(auto&[p,n]:cnt){auto a=ex[p];cout<<"dc="<<p.first<<" flat="<<p.second<<" support="<<25-p.first-4*p.second<<" count="<<n<<" witness=";for(int x:a)cout<<x;cout<<"\n";}
cout<<"profiles "<<profiles.size()<<"\n";for(auto&[p,n]:profiles)cout<<p<<" "<<n<<"\n";
}
