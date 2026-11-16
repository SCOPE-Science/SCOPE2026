#include <bits/stdc++.h>
using namespace std;
const int r[30][8]={
{1,0,0,0,0,0,0,0},
{0,1,0,0,0,0,0,0},
{0,0,1,0,0,0,0,0},
{0,0,0,1,0,0,0,0},
{0,0,0,0,1,0,0,0},
{0,0,0,0,0,1,0,0},
{0,0,0,0,0,0,1,0},
{0,0,0,0,0,0,0,1},
{-1,-1,0,1,1,1,0,-1},
{1,0,-1,-1,0,0,1,1},
{-1,0,0,0,0,1,0,0},
{0,-1,0,0,0,0,1,0},
{0,0,-1,0,0,0,0,1},
{-1,-1,0,0,1,1,0,-1},
{1,0,-1,-1,-1,0,1,1},
{-1,0,0,0,0,0,0,0},
{0,-1,0,0,0,0,0,0},
{0,0,-1,0,0,0,0,0},
{0,0,0,-1,0,0,0,0},
{0,0,0,0,-1,0,0,0},
{0,0,0,0,0,-1,0,0},
{0,0,0,0,0,0,-1,0},
{0,0,0,0,0,0,0,-1},
{1,1,0,-1,-1,-1,0,1},
{-1,0,1,1,0,0,-1,-1},
{1,0,0,0,0,-1,0,0},
{0,1,0,0,0,0,-1,0},
{0,0,1,0,0,0,0,-1},
{1,1,0,0,-1,-1,0,1},
{-1,0,1,1,1,0,-1,-1},
};
int main(){int pow6[5]={1,6,36,216,1296};
int masks[7776]={}; for(int code=0;code<7776;code++){
 int a[5],z=code;for(int t=0;t<5;t++){a[t]=z%6;z/=6;}
 for(int k=0;k<5;k++){
  int s[8]={};for(int t=0;t<5;t++){
   int e=(5*a[t]-6*k*t)%30;if(e<0)e+=30;
   for(int j=0;j<8;j++)s[j]+=r[e][j];
  }
  bool zero=true;for(int j=0;j<8;j++)if(s[j])zero=false;
  if(zero)masks[code]|=(1<<k);
 }
}
int phase[1296][5];for(int w=0;w<1296;w++){int z=w;phase[w][0]=0;for(int t=1;t<5;t++){phase[w][t]=z%6;z/=6;}}
map<string,long long> profiles;map<int,long long> sums;long long total=0;
for(int f=0;f<1296;f++)for(int g=0;g<1296;g++){
 int rows[5],num=0;
 for(int x=0;x<5;x++){
  int code=0;for(int t=0;t<5;t++){
   int e=phase[f][t]-phase[g][(t-x+5)%5];if(e<0)e+=6;
   code+=e*pow6[t];
  }
  rows[x]=__builtin_popcount((unsigned)masks[code]); num+=rows[x];
 }
 sort(rows,rows+5);string key;for(int t:rows)key+=char('0'+t);
 profiles[key]++;sums[25-num]++;total++;
}
const map<int,long long> expected={{5,1},{19,600},{20,120},{21,5875},{22,1200},{23,30600},{24,322200},{25,1319020}};
const map<string,long long> exp_profiles={{"00000",1319020},{"00001",322200},{"00004",5875},{"00011",30600},{"00111",1200},{"00114",600},{"11111",120},{"44444",1}};
if(total!=1679616 || sums!=expected || profiles!=exp_profiles){cerr<<"FAILED: mismatch in direct cyclotomic Fourier test\n";return 1;}
cout<<"PASS: direct 30th-root cyclotomic reduction for all 1,679,616 pairs\n";for(auto &x:sums)cout<<"support "<<x.first<<" count "<<x.second<<"\n";
for(auto &x:profiles)cout<<"profile "<<x.first<<" count "<<x.second<<"\n";
}
