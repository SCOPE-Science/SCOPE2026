#include <bits/stdc++.h>
using namespace std;
static int ov[16][16];
static unordered_map<string,uint8_t> memo;
int gmin(const string &s){
 int n=s.size();if(n<=1)return 0;
 auto it=memo.find(s);if(it!=memo.end())return it->second;
 int mx=0; vector<tuple<int,int,int>> pairs;
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j){int o=ov[(unsigned char)s[i]&15][((unsigned char)s[j])>>4];
 if(o>mx){mx=o;pairs.clear();}if(o==mx&&o>0)pairs.emplace_back(i,j,o);}
 if(mx==0){memo.emplace(s,0);return 0;}
 int ans=255;
 for(auto [i,j,o]:pairs){
 string y; y.reserve(n-1);
 for(int t=0;t<n;t++)if(t!=i&&t!=j)y.push_back(s[t]);
 y.push_back(char((s[i]&240)|(s[j]&15)));
 sort(y.begin(),y.end(),[](char a,char b){return (unsigned char)a<(unsigned char)b;});
 ans=min(ans,o+gmin(y));
 }
 memo.emplace(s,(uint8_t)ans);return ans;
}
int main(int argc,char**argv){
 int cap=65536;if(argc>1)cap=atoi(argv[1]);int begin=1;if(argc>2)begin=atoi(argv[2]);
 for(int i=0;i<16;i++)for(int j=0;j<16;j++){
  if(i==j)continue;
  for(int k=1;k<4;k++)if((i&((1<<k)-1))==(j>>(4-k)))ov[i][j]=k;
 }
 int upper=1<<16;vector<array<unsigned char,16>> dp(upper);vector<unsigned char> opt(upper);
 for(int mask=1;mask<upper;mask++){
  int best=255;
  for(int j=0;j<16;j++)if(mask>>j&1){
   int sub=mask^(1<<j), v=255;
   if(!sub)v=4;
   else for(int i=0;i<16;i++)if(sub>>i&1)v=min(v,((int)dp[sub][i])+4-ov[i][j]);
   dp[mask][j]=v;best=min(best,v);
  }
  opt[mask]=(unsigned char)best;
 }
 int bestmask=0,bestlen=0,bestopt=1,bestcount=0;vector<int> bestmasks;
 for(int mask=begin;mask<cap;mask++){if(mask%128==0){unordered_map<string,uint8_t>().swap(memo);}

  string s;for(int i=0;i<16;i++)if(mask>>i&1)s.push_back(char(i*16+i));
  int n=s.size();int p=gmin(s);int gl=4*n-p;
  if(1LL*gl*bestopt>1LL*bestlen*opt[mask]){bestmask=mask;bestlen=gl;bestopt=opt[mask];bestcount=0;bestmasks.clear();}
  if(1LL*gl*bestopt==1LL*bestlen*opt[mask]){bestcount++;bestmasks.push_back(mask);}
  if(mask%100==0){cerr<<"PROGRESS "<<mask<<" / "<<cap<<" states "<<memo.size()<<"\n";}
 }
 cout<<"FINISH masks="<<(cap-begin)<<" max="<<bestlen<<"/"<<bestopt<<" first_mask="<<bestmask<<" maxima="<<bestcount<<" final_memo="<<memo.size()<<"\n";
 cout<<"MAX_MASKS";for(int m:bestmasks)cout<<" "<<m;cout<<"\n";
}
