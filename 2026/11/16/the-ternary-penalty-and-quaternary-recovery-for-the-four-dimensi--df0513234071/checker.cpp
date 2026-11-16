// Exact fourth-moment census for the 16-character unit cube.
// Compile: g++ -O3 -std=c++17 checker.cpp -o checker
// Run: ./checker 2; ./checker 3; ./checker 4
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <string>
#include <vector>
using namespace std;
using A=array<int,16>;
int sqnorm(const array<int,4>& c, int q){
 if(q==2) return (c[0]-c[1])*(c[0]-c[1]);
 if(q==3) return c[0]*c[0]+c[1]*c[1]+c[2]*c[2]-c[0]*c[1]-c[0]*c[2]-c[1]*c[2];
 return (c[0]-c[2])*(c[0]-c[2])+(c[1]-c[3])*(c[1]-c[3]);
}
int independent_convolution(const A& a,int q){
 array<array<int,4>,81> sums{};
 for(int x=0;x<16;x++)for(int y=0;y<16;y++){
   int t=0,p=1;
   for(int j=0;j<4;j++){t+=(((x>>j)&1)+((y>>j)&1))*p;p*=3;}
   sums[t][(a[x]+a[y])%q]++;
 }
 int M=0;for(auto& c:sums)M+=sqnorm(c,q);return M;
}
int main(int argc,char**argv){
 if(argc!=2){cerr<<"Usage: ./checker {2|3|4}\n";return 2;}
 int q=atoi(argv[1]); if(q<2||q>4){cerr<<"Unsupported q\n";return 2;}
 vector<pair<int,int>> shift[81];
 for(int code=0;code<81;code++){
   int v=code,dir[4];for(int j=0;j<4;j++){dir[j]=v%3-1;v/=3;}
   for(int x=0;x<16;x++){
     int y=x;bool ok=true;
     for(int j=0;j<4;j++){
       int b=((x>>j)&1)+dir[j];
       if(b<0||b>1){ok=false;break;}
       if(b!=((x>>j)&1)) y^=1<<j;
     }
     if(ok)shift[code].push_back({y,x});
   }
 }
 int freeidx[11],k=0;
 for(int x=0;x<16;x++)if(x!=0&&x!=1&&x!=2&&x!=4&&x!=8)freeidx[k++]=x;
 if(k!=11){cerr<<"Gauge failure\n";return 3;}
 uint64_t total=1;for(int i=0;i<11;i++)total*=q;
 int minM=numeric_limits<int>::max(),second=minM;
 uint64_t nMin=0;
 vector<string> minimizers;
 for(uint64_t code=0;code<total;code++){
   A a{};uint64_t v=code;
   for(int i=0;i<11;i++){a[freeidx[i]]=v%q;v/=q;}
   int M=0;
   for(int d=0;d<81;d++){
     array<int,4> c{};
     for(auto [y,x]:shift[d])c[(a[y]-a[x]+q)%q]++;
     M+=sqnorm(c,q);
   }
   if(M<minM){second=minM;minM=M;nMin=0;minimizers.clear();}
   if(M==minM){
     nMin++;string s;for(int x=0;x<16;x++)s.push_back('0'+a[x]);minimizers.push_back(s);
   }else if(M<second)second=M;
 }
 const int expectedMin[5]={0,0,336,384,336};
 const int expectedSecond[5]={0,0,400,396,368};
 const uint64_t expectedCount[5]={0,0,12,240,24};
 if(minM!=expectedMin[q]||second!=expectedSecond[q]||nMin!=expectedCount[q]){
   cerr<<"Incorrect min/next/count for alphabet "<<q<<"\n";return 4;
 }
 for(auto& s:minimizers){
   A a{};for(int i=0;i<16;i++)a[i]=s[i]-'0';
   if(independent_convolution(a,q)!=minM){cerr<<"Independent convolution mismatch\n";return 5;}
 }
 cout<<"CHECK_PASS alphabet="<<q<<" normalized_inputs="<<total
     <<" minimum="<<minM<<" next="<<second<<" normalized_minimizers="<<nMin<<"\n";
 if(q>=3){for(const auto& s:minimizers)cout<<s<<'\n';}
}
