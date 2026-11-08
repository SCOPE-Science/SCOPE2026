#include <bits/stdc++.h>
using namespace std;
int mulf(int a,int b){int v=0;while(b){if(b&1)v^=a;a<<=1;if(a&4)a^=7;b>>=1;}return v;}
int powf(int x,int n){int r=1;while(n--)r=mulf(r,x);return r;}
int main(int argc,char** argv){
 vector<array<int,3>> P;for(int x=0;x<4;x++)for(int y=0;y<4;y++)P.push_back({1,x,y});for(int y=0;y<4;y++)P.push_back({0,1,y});P.push_back({0,0,1});
 array<array<int,3>,10> expo={{{3,0,0},{0,3,0},{0,0,3},{2,1,0},{2,0,1},{1,2,0},{0,2,1},{1,0,2},{0,1,2},{1,1,1}}};
 int m[4][4];for(int a=0;a<4;a++)for(int b=0;b<4;b++)m[a][b]=mulf(a,b);
 uint32_t LM[21]={};for(int l=0;l<21;l++)for(int p=0;p<21;p++){int v=0;for(int t=0;t<3;t++)v^=m[P[p][t]][P[l][t]];if(!v)LM[l]|=1u<<p;}
 int ev[21][10],dv[21][3][10];for(int p=0;p<21;p++)for(int i=0;i<10;i++){
  int mon=1;for(int t=0;t<3;t++)mon=m[mon][powf(P[p][t],expo[i][t])];ev[p][i]=mon;
  for(int j=0;j<3;j++){int mon2=expo[i][j]%2; if(mon2)for(int t=0;t<3;t++)mon2=m[mon2][powf(P[p][t],expo[i][t]-(t==j?1:0))];dv[p][j][i]=mon2;}
 }
 int li[64];fill(li,li+64,-1);for(int i=0;i<21;i++){auto x=P[i]; li[x[0]*16+x[1]*4+x[2]]=i;}
 auto norm=[&](int a,int b,int c){int v=a?a:b?b:c;int iv=m[v][v];return li[m[a][iv]*16+m[b][iv]*4+m[c][iv]];};
 vector<int> tangent,blocking,both;int hist[22]={},bcount[22]={},tcnt[22]={};int eligible=0,nonrat=0;
 for(int mask=1;mask<(1<<20);mask++){
  int x=mask,coef[10];for(int i=0;i<10;i++){coef[i]=x&3;x>>=2;}int first=0;while(first<10&&!coef[first])first++;if(first==10||coef[first]!=1)continue;
  uint32_t pts=0, covered=0;bool rat_smooth=true;int n=0;
  for(int p=0;p<21;p++){
   int v=0,g0=0,g1=0,g2=0;
   for(int j=0;j<10;j++){int a=coef[j];if(!a)continue;v^=m[a][ev[p][j]];g0^=m[a][dv[p][0][j]];g1^=m[a][dv[p][1][j]];g2^=m[a][dv[p][2][j]];}
   if(v==0){pts|=1u<<p;n++;if(!g0&&!g1&&!g2)rat_smooth=false;else{int l=norm(g0,g1,g2);covered|=LM[l];}}
  }
  if(!rat_smooth){nonrat++;continue;}eligible++;hist[n]++;
  bool B=true;for(auto l:LM)if(!(l&pts)){B=false;break;}
  bool T=covered==((1u<<21)-1);
  if(T){tangent.push_back(mask);tcnt[n]++;}
  if(B){blocking.push_back(mask);bcount[n]++;}
  if(T&&B)both.push_back(mask);
 }
 cout<<"rat-smooth "<<eligible<<" rat-sing "<<nonrat<<" tangent "<<tangent.size()<<" blocking "<<blocking.size()<<" both "<<both.size()<<"\n";
 for(int n=0;n<22;n++)if(hist[n])cout<<"n="<<n<<" rat-smooth="<<hist[n]<<" tangent="<<tcnt[n]<<" blocking="<<bcount[n]<<"\n";
 if(argc>1){ofstream o(argv[1]);if(!o)return 2;for(int v:both)o<<v<<"\n";}
 if(eligible!=248928||nonrat!=100597||tangent.size()!=6328||blocking.size()!=6328||both.size()!=6328||tcnt[9]!=280||tcnt[10]!=6048||bcount[9]!=280||bcount[10]!=6048)return 3;
 cout<<"F4_CUBIC_TANGENT_BLOCKING_CENSUS_PASS 349525 6328 280 6048\n";
 return 0;
}
