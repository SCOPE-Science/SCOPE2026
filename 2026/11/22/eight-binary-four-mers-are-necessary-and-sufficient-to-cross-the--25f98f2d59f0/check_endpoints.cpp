#include <bits/stdc++.h>
using namespace std;
struct K { uint64_t a,b; bool operator==(K const&o)const{return a==o.a&&b==o.b;}};
struct H{size_t operator()(K const&x)const {uint64_t v=x.a*0x9e3779b97f4a7c15ULL ^ (x.b+0xbf58476d1ce4e5b9ULL);v^=v>>30;v*=0xbf58476d1ce4e5b9ULL;v^=v>>27;return v^(v>>31);}};
int ov[16][16];
unordered_map<K,uint8_t,H> memo;
long long nodes=0;
uint8_t go(vector<uint8_t> const& a){
 int m=a.size(); if(m<2)return 0;
 K k{0,0};for(int i=0;i<m;i++){if(i<8)k.a|=(uint64_t)a[i]<<(8*i);else k.b|=(uint64_t)a[i]<<(8*(i-8));}k.b|=(uint64_t)m<<60;
 auto it=memo.find(k);if(it!=memo.end())return it->second;
 int mx=-1; vector<pair<int,int>> pairs;
 for(int i=0;i<m;i++)for(int j=0;j<m;j++)if(i!=j){int val=ov[a[i]&15][a[j]>>4]; if(val>mx){mx=val;pairs.clear();}if(val==mx)pairs.push_back({i,j});}
 int best=100;
 for(auto [i,j]:pairs){vector<uint8_t>b;b.reserve(m-1);for(int z=0;z<m;z++)if(z!=i&&z!=j)b.push_back(a[z]);b.push_back((a[i]&0xf0)|(a[j]&0x0f));sort(b.begin(),b.end());best=min(best,mx+(int)go(b));}
 memo.emplace(k,(uint8_t)best);return best;
}
int main(int argc,char **argv){int maxm=argc>1?atoi(argv[1]):8; for(int i=0;i<16;i++)for(int j=0;j<16;j++)if(i!=j){for(int r=1;r<4;r++)if((i&((1<<r)-1))==(j>>(4-r))){ov[i][j]=r;}}
 // encoding: upper nibble HEAD, lower nibble TAIL. a[i] &15 = tail, a[j]>>4 = head
 vector<vector<int>> dp(1<<16,vector<int>(16,-999));for(int i=0;i<16;i++)dp[1<<i][i]=0;
 for(int S=1;S<(1<<16);S++)for(int j=0;j<16;j++)if(dp[S][j]>=0)for(int t=0;t<16;t++)if(!(S&(1<<t))){int &d=dp[S|(1<<t)][t];d=max(d,dp[S][j]+ov[j][t]);}
 int mxnum=0,mxden=1;long long maxcount=0;int bestsubset=0;map<pair<int,int>,int> count;int lastm=0;int max_n[17]={0},max_d[17]={0};long long cnt[17]={0};int reps[17]={0};
 for(int S=1;S<(1<<16);S++){
  int m=__builtin_popcount((unsigned)S);if(m>maxm)continue;
  vector<uint8_t>a; for(int i=0;i<16;i++)if(S&(1<<i))a.push_back((i<<4)|i);
  int g=go(a),op=0;for(int i=0;i<16;i++)if(S&(1<<i))op=max(op,dp[S][i]);
  int gl=4*m-g,ol=4*m-op;count[{gl,ol}]++; if(m==8 && 2*gl>3*ol)cerr<<"BAD "<<S<<" "<<gl<<" "<<ol<<"\n"; if(max_d[m]==0 || gl*max_d[m]>max_n[m]*ol){max_n[m]=gl;max_d[m]=ol;cnt[m]=0;reps[m]=S;} if(gl*max_d[m]==max_n[m]*ol)cnt[m]++;
  if(gl*mxden>mxnum*ol){mxnum=gl;mxden=ol;bestsubset=S;maxcount=0;}
  if(gl*mxden==mxnum*ol)maxcount++;
  if(m>lastm){lastm=m;cerr<<"m="<<m<<" memo="<<memo.size()<<" best="<<mxnum<<"/"<<mxden<<" states="<<S<<"\n";}
 }
 cout<<"MAX m<="<<maxm<<" ratio="<<mxnum<<"/"<<mxden<<" count="<<maxcount<<" subset="<<bestsubset<<" memo="<<memo.size()<<"\n";
 for(int m=1;m<=maxm;m++)cout<<"m "<<m<<" ratio "<<max_n[m]<<"/"<<max_d[m]<<" count "<<cnt[m]<<" rep "<<reps[m]<<"\n"; for(auto [p,n]:count){if(p.first*mxden==mxnum*p.second)cout<<"case "<<p.first<<" "<<p.second<<" "<<n<<"\n";}
}
