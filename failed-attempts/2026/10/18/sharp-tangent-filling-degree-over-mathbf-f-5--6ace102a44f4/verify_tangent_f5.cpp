// Reproducible exact finite-field verification of the minimal degree in PG(2,5).
// Compile: c++ -O2 -std=c++17 verify_tangent_f5.cpp -o verify_tangent_f5
// Run: ./verify_tangent_f5  (expected: MINIMUM_DEGREE_4_VERIFIED)
#include <array>
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
using Point=array<int,3>;
using Monomial=array<int,3>;
constexpr uint32_t full=(uint32_t(1)<<31)-1;
int mod5(int a){a%=5;return a<0?a+5:a;}
int pow5(int a,int n){int r=1;while(n--)r=mod5(r*a);return r;}
vector<Point> points(){
 vector<Point> p;
 for(int x=0;x<5;x++)for(int y=0;y<5;y++)p.push_back({x,y,1});
 for(int x=0;x<5;x++)p.push_back({x,1,0});
 p.push_back({1,0,0});
 if(p.size()!=31)throw runtime_error("bad point enumeration");
 return p;
}
vector<Monomial> monomials(int d){
 vector<Monomial> r;
 for(int a=d;a>=0;a--)for(int b=d-a;b>=0;b--)r.push_back({a,b,d-a-b});
 return r;
}
struct System{
 vector<Point> p;
 vector<Monomial> mons;
 vector<vector<int>> V, Dx,Dy,Dz;
 array<uint32_t,125> line_masks{};
 System(int degree):p(points()),mons(monomials(degree)){
  for(int x=0;x<5;x++)for(int y=0;y<5;y++)for(int z=0;z<5;z++){
   uint32_t mask=0;
   for(int j=0;j<31;j++)if(mod5(x*p[j][0]+y*p[j][1]+z*p[j][2])==0)mask|=(uint32_t(1)<<j);
   line_masks[x+5*y+25*z]=(x||y||z)?mask:0;
  }
  for(const Point& q:p){
   vector<int> v,dx,dy,dz;
   for(const auto& m:mons){
    int f=1;
    for(int t=0;t<3;t++)f=mod5(f*pow5(q[t],m[t]));
    v.push_back(f);
    for(int t=0;t<3;t++){
     int e=m[t];
     int w=e;
     if(e)for(int k=0;k<3;k++)w=mod5(w*pow5(q[k],m[k]-(k==t)));
     if(t==0)dx.push_back(w);
     if(t==1)dy.push_back(w);
     if(t==2)dz.push_back(w);
    }
   }
   V.push_back(v);Dx.push_back(dx);Dy.push_back(dy);Dz.push_back(dz);
  }
 }
 int dot(const vector<int>& a,const vector<int>& b,int start){
  int z=0;for(size_t j=start;j<a.size();j++)z+=a[j]*b[j];return mod5(z);
 }
 struct Result{bool filling;int pts;int tangent_pts;uint32_t union_mask;};
 Result test(const vector<int>& co,int start=0){
  uint32_t covered=0;int n=0,nt=0;
  for(int j=0;j<31;j++){
   if(dot(V[j],co,start)!=0)continue;
   n++;
   int gx=dot(Dx[j],co,start),gy=dot(Dy[j],co,start),gz=dot(Dz[j],co,start);
   if(!(gx||gy||gz))continue;
   nt++;covered|=line_masks[gx+5*gy+25*gz];
  }
  return {covered==full,n,nt,covered};
 }
 long long census(){
  const int n=(int)mons.size();vector<int> co(n,0);
  long long seen=0,found=0;
  for(int lead=0;lead<n;lead++){
   long long bound=1;for(int j=lead+1;j<n;j++)bound*=5;
   co.assign(n,0);co[lead]=1;
   for(long long i=0;i<bound;i++){
    long long k=i;
    for(int j=lead+1;j<n;j++){co[j]=k%5;k/=5;}
    if(test(co,lead).filling)found++;
    seen++;
   }
  }
  if(found)throw runtime_error("unexpected lower-degree tangent-filling form");
  return seen;
 }
};
int main(){
 for(int degree=1;degree<=3;degree++){
  System s(degree);long long seen=s.census();
  long long expected=0,term=1;for(size_t j=0;j<s.mons.size();j++){expected+=term;term*=5;}
  if(seen!=expected)throw runtime_error("incomplete enumeration");
  cout<<"degree="<<degree<<" normalized_forms="<<seen<<" tangent_filling=0\n";
 }
 System s(4);
 // Monomials in descending x exponent then descending y exponent.
 // F = x^4 + x^3*y + y^3*z - z^4.
 vector<int> co={1,1,0,0,0,0,0,0,0,0,0,1,0,0,4};
 auto r=s.test(co);
 if(!r.filling || r.pts!=11 || r.tangent_pts!=11)throw runtime_error("quartic witness failed");
 cout<<"smooth_quartic_witness_rational_points="<<r.pts<<" tangent_points="<<r.tangent_pts<<" union_points=31\n";
 cout<<"MINIMUM_DEGREE_4_VERIFIED\n";
}
