#include <bits/stdc++.h>
using namespace std;
const int q=5;
using V=array<uint8_t,6>;
using Mat=array<V,3>;
static int cnt=0;
int md(int x){x%=5;if(x<0)x+=5;return x;}
int det(V a){
 int A=a[0], B=a[1], C=a[2],D=a[3],E=a[4],F=a[5];
 // symmetric associated matrix times 2 = [[2A,D,E],[D,2B,F],[E,F,2C]]
 return md(2*A*(4*B*C-F*F)-D*(2*C*D-F*E)+E*(D*F-2*B*E));
}
bool good(Mat rows){
 for(int a=0;a<5;a++)for(int b=0;b<5;b++){
   V v{};for(int k=0;k<6;k++)v[k]=md(rows[0][k]+a*rows[1][k]+b*rows[2][k]);if(det(v)==0)return false;
 }
 for(int b=0;b<5;b++){
   V v{};for(int k=0;k<6;k++)v[k]=md(rows[1][k]+b*rows[2][k]);if(det(v)==0)return false;
 }
 if(det(rows[2])==0)return false;
 return true;
}
vector<Mat> out;
void enumerate(){
 for(int p0=0;p0<6;p0++)for(int p1=p0+1;p1<6;p1++)for(int p2=p1+1;p2<6;p2++){
  Mat rows{};rows[0][p0]=rows[1][p1]=rows[2][p2]=1;
  vector<pair<int,int>> slots;
  for(int i=0;i<3;i++)for(int j=0;j<6;j++)if(j> (i==0?p0:i==1?p1:p2) && j!=p0 && j!=p1 && j!=p2)slots.push_back({i,j});
  int mx=1;for(int i=0;i<(int)slots.size();i++)mx*=5;
  for(int x=0;x<mx;x++){
   int z=x;for(auto [i,j]:slots){rows[i][j]=z%5;z/=5;}
   cnt++;
   if(good(rows))out.push_back(rows);
  }
 }
}
int main(){enumerate(); cerr<<"total="<<cnt<<" smooth_nets="<<out.size()<<"\n";ofstream f("conic_nets_q5.bin",ios::binary);for(auto a:out)for(auto b:a)f.write((char*)b.data(),6);}
