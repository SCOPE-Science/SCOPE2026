#include <bits/stdc++.h>
using namespace std;
unordered_map<string,unsigned char> cache;
int overlap(const string &a,const string &b){for(int r=min(a.size(),b.size());r>=1;r--){if(a.compare(a.size()-r,r,b,0,r)==0)return r;}return 0;}
string key(vector<string> const& state){string s;for(auto&x:state){s+=x;s+='|';}return s;}
int longest(vector<string> a){if(a.size()==1)return a[0].size();sort(a.begin(),a.end());string k=key(a);auto p=cache.find(k);if(p!=cache.end())return p->second;int bestOv=-1;vector<pair<int,int>> pairs;
 for(int i=0;i<(int)a.size();i++)for(int j=0;j<(int)a.size();j++)if(i!=j){int v=overlap(a[i],a[j]);if(v>bestOv){bestOv=v;pairs.clear();}if(v==bestOv)pairs.emplace_back(i,j);}
 int ans=0;for(auto [i,j]:pairs){vector<string>b;for(int h=0;h<(int)a.size();h++)if(h!=i&&h!=j)b.push_back(a[h]);b.push_back(a[i]+a[j].substr(bestOv));ans=max(ans,longest(b));}
 cache.emplace(k,(unsigned char)ans);return ans;
}
int main(int argc,char**argv){int lim=argc>1?atoi(argv[1]):8;string W[16];for(int i=0;i<16;i++){for(int b=3;b>=0;b--)W[i]+=char('0'+((i>>b)&1));}
 int popnum[9]={},popden[9]={},cnt[9]={};long long nstates=0;
 // 16^2 matrix overlaps for iterative Hamilton DP
 int ov[16][16];for(int i=0;i<16;i++)for(int j=0;j<16;j++)ov[i][j]=overlap(W[i],W[j]);
 for(int s=1;s<(1<<16);s++){
  int m=__builtin_popcount((unsigned)s);if(m>lim)continue;
  vector<string> a;vector<int> v;for(int i=0;i<16;i++)if(s>>i&1){a.push_back(W[i]);v.push_back(i);}
  int g=longest(a);
  int full=(1<<m)-1;int d[256][8];if(m>8){cerr<<"bad size";return 1;}fill(&d[0][0],&d[0][0]+256*8,INT_MAX/3);
  for(int i=0;i<m;i++)d[1<<i][i]=4;
  for(int mask=1;mask<=full;mask++)for(int i=0;i<m;i++)if(d[mask][i]<INT_MAX/4)for(int j=0;j<m;j++)if(!(mask>>j&1))d[mask|1<<j][j]=min(d[mask|1<<j][j],d[mask][i]+4-ov[v[i]][v[j]]);
  int opt=INT_MAX;for(int j=0;j<m;j++)opt=min(opt,d[full][j]);
  if(popden[m]==0||g*popden[m]>popnum[m]*opt){popnum[m]=g;popden[m]=opt;cnt[m]=0;}if(g*popden[m]==popnum[m]*opt)cnt[m]++;
  if(m==8&&2*g>3*opt)cout<<"BAD "<<s<<" "<<g<<" "<<opt<<"\n";
 }
 for(int m=1;m<=lim;m++)cout<<"ROW "<<m<<" "<<popnum[m]<<" "<<popden[m]<<" "<<cnt[m]<<"\n";
 cout<<"STATES "<<cache.size()<<"\n";
}
