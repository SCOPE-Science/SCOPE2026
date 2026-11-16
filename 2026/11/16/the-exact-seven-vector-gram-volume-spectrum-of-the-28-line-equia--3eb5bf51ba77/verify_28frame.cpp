#include <bits/stdc++.h>
using namespace std;
long long det7(int a[7][7]){
 long long b[7][7]; for(int i=0;i<7;i++)for(int j=0;j<7;j++)b[i][j]=a[i][j];
 long long sgn=1,den=1;
 for(int k=0;k<6;k++){
  int t=k;while(t<7 && b[t][k]==0)t++;
  if(t==7)return 0;
  if(t!=k){for(int j=0;j<7;j++)swap(b[t][j],b[k][j]);sgn=-sgn;}
  long long pivot=b[k][k];
  for(int i=k+1;i<7;i++)for(int j=k+1;j<7;j++){
   __int128 val=(__int128)b[i][j]*pivot-(__int128)b[i][k]*b[k][j];
   if(val%den)exit(1);
   b[i][j]=(long long)(val/den);
  }
  for(int i=k+1;i<7;i++)b[i][k]=0;
  den=pivot;
 }
 return sgn*b[6][6];
}
int main(){vector<pair<int,int>> edges;for(int i=0;i<8;i++)for(int j=i+1;j<8;j++)edges.push_back({i,j});
 int a[7][7]; map<long long,long long>cnt; long long total=0;
 for(int x0=0;x0<22;x0++)for(int x1=x0+1;x1<23;x1++)for(int x2=x1+1;x2<24;x2++)for(int x3=x2+1;x3<25;x3++)for(int x4=x3+1;x4<26;x4++)for(int x5=x4+1;x5<27;x5++)for(int x6=x5+1;x6<28;x6++){
  int s[]={x0,x1,x2,x3,x4,x5,x6};
  for(int j=0;j<7;j++){auto [u,v]=edges[s[j]]; for(int i=0;i<7;i++)a[i][j]=((i==u||i==v)?3:-1);}
  long long d=llabs(det7(a)); cnt[d]++;total++;
 }
 cerr<<"total="<<total<<"\n";for(auto [v,n]:cnt)cout<<v<<" "<<n<<"\n";
 if(total!=1184040 || cnt!=map<long long,long long>{{0,662760},{4096,508896},{8192,12096},{12288,288}})return 2;
 cout<<"FRAME_DETERMINANT_ENUMERATION_OK\n";
}
