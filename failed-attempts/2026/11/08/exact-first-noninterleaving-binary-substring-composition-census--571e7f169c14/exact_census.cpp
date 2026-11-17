#include <bits/stdc++.h>
using namespace std;
using ull=uint64_t;
static ull rd(ull &x){x+=0x9e3779b97f4a7c15ULL;ull z=x;z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;z=(z^(z>>27))*0x94d049bb133111ebULL;return z^(z>>31);}
static uint32_t revbits(uint32_t x,int n){uint32_t r=0;for(int i=0;i<n;i++){r=(r<<1)|(x&1);x>>=1;}return r;}
static vector<uint8_t> profile(uint32_t v,int n){
 vector<uint8_t> a; a.reserve((n+1)*(n+2)/2);uint32_t p[28]={0};for(int i=0;i<n;i++)p[i+1]=p[i]+((v>>i)&1);
 for(int len=1;len<=n;len++){uint8_t counts[28]={0};for(int j=0;j+len<=n;j++)counts[p[j+len]-p[j]]++;for(int k=0;k<=len;k++)a.push_back(counts[k]);}
 return a;
}
int main(int argc,char**argv){
 int n=atoi(argv[1]);auto t0=chrono::steady_clock::now();uint32_t N=1U<<n;ull R[28][28]={};ull seed=0x3141592653589793ULL;for(int i=0;i<=n;i++)for(int j=0;j<=n;j++)R[i][j]=rd(seed);
 vector<pair<ull,uint32_t>> all;all.resize(N);
 for(uint32_t v=0;v<N;v++){
   ull h=0;for(int len=1;len<=n;len++){uint32_t mask=(1u<<len)-1;for(int j=0;j+len<=n;j++)h+=R[len][__builtin_popcount((v>>j)&mask)];}
   all[v]={h,v};
 }
 cerr<<"hashed "<<N<<" time="<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"s\n";
 sort(all.begin(),all.end());cerr<<"sorted time="<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"s\n";
 map<int,uint64_t> hist;uint64_t collision_groups=0, prof_count=0, heavy=0;
 ofstream fout(string("equicomposable_")+to_string(n)+".txt");
 for(size_t i=0;i<all.size();){size_t j=i+1;while(j<all.size()&&all[j].first==all[i].first)j++;
   if(j==i+1){if(revbits(all[i].second,n)!=all[i].second){cerr<<"bad singleton: "<<all[i].second<<"\n";return 2;}hist[1]++;prof_count++;}
   else if(j==i+2 && revbits(all[i].second,n)==all[i+1].second){hist[2]++;prof_count++;}
   else {
    map<vector<uint8_t>,vector<uint32_t>> groups;
    for(size_t k=i;k<j;k++)groups[profile(all[k].second,n)].push_back(all[k].second);
    if(groups.size()>1)collision_groups++;
    for(auto &[key,vals]:groups){hist[(int)vals.size()]++;prof_count++;if(vals.size()>2){heavy++;fout<<vals.size();for(auto x:vals)fout<<" "<<x;fout<<"\n";}}
   }
   i=j;
 }
 cerr<<"finished time="<<chrono::duration<double>(chrono::steady_clock::now()-t0).count()<<"s\n";
 cout<<"n="<<n<<" profiles="<<prof_count<<" heavy="<<heavy<<" hash_collision_groups="<<collision_groups<<"\n";
 for(auto [size,num]:hist)cout<<"size="<<size<<" classes="<<num<<" words="<<size*num<<"\n";
}
