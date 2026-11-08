#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
uint64_t splitmix(uint64_t &s) {s+=0x9e3779b97f4a7c15ULL;uint64_t z=s;z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;return z^(z>>31);}
uint32_t reverse_word(uint32_t w,int n){uint32_t res=0;for(int i=0;i<n;i++){res=(res<<1)|(w&1);w>>=1;}return res;}
vector<unsigned char> prefix_key(uint32_t x,int n){
 array<int,25> p{};for(int i=0;i<n;i++)p[i+1]=p[i]+((x>>i)&1);
 vector<unsigned char> key((n+1)*(n+2)/2,0);
 for(int left=0;left<n;left++)for(int right=left+1;right<=n;right++){
  int len=right-left,ones=p[right]-p[left];key[len*(len+1)/2-1+ones]++;
 }
 return key;
}
int main(int argc,char **argv){int n=argc>1?stoi(argv[1]):23;uint64_t seed=0x42694eb17107ULL;uint64_t weight[25][25]={};for(int i=0;i<=n;i++)for(int j=0;j<=n;j++)weight[i][j]=splitmix(seed);
 vector<pair<uint64_t,uint32_t>> rec(1U<<n);
 for(uint32_t w=0;w<(1U<<n);w++){
  int p[25]={0};for(int i=0;i<n;i++)p[i+1]=p[i]+((w>>i)&1);
  uint64_t h=0;
  for(int l=0;l<n;l++)for(int r=l+1;r<=n;r++)h+=weight[r-l][p[r]-p[l]];
  rec[w]={h,w};
 }
 sort(rec.begin(),rec.end());
 map<size_t,uint64_t> counts;uint64_t hashed_collisions=0;vector<array<uint32_t,4>> four;
 for(size_t i=0;i<rec.size();){size_t end=i+1;while(end<rec.size()&&rec[end].first==rec[i].first)end++;
  if(end==i+1){if(reverse_word(rec[i].second,n)!=rec[i].second)return 2;counts[1]++;}
  else if(end==i+2&&reverse_word(rec[i].second,n)==rec[i+1].second){counts[2]++;}
  else {
   map<vector<unsigned char>,vector<uint32_t>> actual;
   for(size_t j=i;j<end;j++)actual[prefix_key(rec[j].second,n)].push_back(rec[j].second);
   hashed_collisions+=actual.size()>1;
   for(auto &[k,v]:actual){counts[v.size()]++;if(v.size()==4){sort(v.begin(),v.end());four.push_back({v[0],v[1],v[2],v[3]});}}
  }i=end;
 }
 sort(four.begin(),four.end());
 ofstream o("independent_four_"+to_string(n)+".txt");for(auto v:four)o<<v[0]<<' '<<v[1]<<' '<<v[2]<<' '<<v[3]<<'\n';
 cout<<"n="<<n<<" collisions="<<hashed_collisions<<"\n";for(auto [k,v]:counts)cout<<"class_size="<<k<<" class_count="<<v<<"\n";
}
