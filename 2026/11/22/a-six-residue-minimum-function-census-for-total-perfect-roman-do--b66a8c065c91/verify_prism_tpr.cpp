// Finite certificate for a rational-transfer proof of minimum total perfect Roman functions on cycle prisms.
// Compile: c++ -O2 -std=c++17 verify_prism_tpr.cpp -o verify_prism_tpr
#include <array>
#include <vector>
#include <algorithm>
#include <iostream>
#include <stdexcept>
using namespace std;
using U=unsigned __int128;
struct Arc {int v,c;};
void check(bool yes,const char* msg){if(!yes)throw runtime_error(msg);}
int main(){
 try {
  array<array<int,2>,9> a{};for(int x=0;x<9;x++)a[x]={x/3,x%3};
  vector<vector<Arc>> raw(81);
  for(int x=0;x<9;x++)for(int y=0;y<9;y++)for(int z=0;z<9;z++){
   bool good=true;
   for(int r=0;r<2;r++){
    const int u=a[x][r],v=a[y][r],w=a[z][r],s=a[y][1-r];
    if(v==0 && ((u==2)+(w==2)+(s==2)!=1))good=false;
    if(v>0 && !((u>0)||(w>0)||(s>0)))good=false;
   }
   if(good)raw[x*9+y].push_back({y*9+z,3*(a[y][0]+a[y][1])-4});
  }
  int arc_count=0;for(const auto& v:raw)arc_count+=v.size();check(arc_count==468,"raw arc count");
  array<int,81> h{};
  for(int it=0;it<81;it++){
   bool change=false;
   for(int u=0;u<81;u++)for(auto e:raw[u])if(h[e.v]>h[u]+e.c){h[e.v]=h[u]+e.c;change=true;}
   if(!change)break;
   check(it!=80,"negative cycle in potential calculation");
  }
  vector<vector<Arc>> B(81);
  array<array<bool,81>,81> reach{};
  int zeros=0,ones=0;
  for(int u=0;u<81;u++){
   reach[u][u]=true;
   for(auto e:raw[u]){
    int c=e.c+h[u]-h[e.v];check(c>=0,"negative reduced arc");
    B[u].push_back({e.v,c});
    if(c==0){reach[u][e.v]=true;zeros++;}
    if(c==1)ones++;
   }
  }
  check(zeros==105 && ones==32,"reduced arc counts");
  for(int k=0;k<81;k++)for(int i=0;i<81;i++)if(reach[i][k])for(int j=0;j<81;j++)if(reach[k][j])reach[i][j]=true;
  array<bool,81> seen{};vector<int> cycle_sizes;
  for(int i=0;i<81;i++)if(!seen[i]){
   vector<int> comp;
   for(int j=0;j<81;j++)if(reach[i][j]&&reach[j][i]){comp.push_back(j);seen[j]=true;}
   bool cyclic=comp.size()>1;
   if(!cyclic)for(auto e:B[i])if(e.v==i && e.c==0)cyclic=true;
   if(cyclic){
    int inside=0;
    for(int u:comp)for(auto e:B[u])if(e.c==0&&find(comp.begin(),comp.end(),e.v)!=comp.end())inside++;
    check(inside==(int)comp.size(),"not a simple directed zero-cycle");
    cycle_sizes.push_back((int)comp.size());
   }
  }
  sort(cycle_sizes.begin(),cycle_sizes.end());check(cycle_sizes==vector<int>({3,6}),"zero-cycle determinant");
  // For every cost-one transition, find all possible zero-cost return path lengths mod 6.
  // Exactly six cost-one transitions admit a return, all with resulting closed length 5 mod 6.
  int closing=0;
  for(int u=0;u<81;u++)for(auto e:B[u])if(e.c==1){
   bool mark[81][6]{};vector<pair<int,int>> stack={{e.v,0}};mark[e.v][0]=true;
   for(size_t z=0;z<stack.size();z++){
    auto [v,r]=stack[z];
    for(auto f:B[v])if(f.c==0){int s=(r+1)%6;if(!mark[f.v][s]){mark[f.v][s]=true;stack.push_back({f.v,s});}}
   }
   for(int r=0;r<6;r++)if(mark[u][r]){closing++;check((r+1)%6==5,"forbidden cost-one cycle residue");}
  }
  check(closing==6,"cost-one closure count");
  // Coefficients of q^0,...,q^4 in tr(B(q)^n), n <= 345.
  constexpr int LIM=345;
  vector<array<U,5>> totals(LIM+1);
  vector<array<U,5>> dp(81), nd(81);
  for(int start=0;start<81;start++){
   for(auto &x:dp)x.fill(0);
   dp[start][0]=1;
   for(int n=1;n<=LIM;n++){
    for(auto &x:nd)x.fill(0);
    for(int u=0;u<81;u++)for(auto e:B[u])if(e.c<=4)
      for(int d=e.c;d<=4;d++) {
        const U add=dp[u][d-e.c];
        check(~U(0)-nd[e.v][d]>=add,"128-bit intermediate overflow");
        nd[e.v][d]+=add;
      }
    dp.swap(nd);
    for(int d=0;d<=4;d++){
      check(~U(0)-totals[n][d]>=dp[start][d],"128-bit total overflow");
      totals[n][d]+=dp[start][d];
     }
   }
  }
  for(int n=1;n<=LIM;n++){
   const U N=n;
   U c0=(n%6==3?3:n%6==0?9:0);
   U c1=(n%6==5?6*N:0);
   U c2=(n==1?3:(n%6==1?5*N:n%6==4?3*N*N:0));
   U c4=(n==2?7:(n%6==2?N*(N*N*N-2*N*N+17*N-52)/4:
                    n%6==5?N*(12*N*N+13*N-71)/6:0));
   // For n=2 the special case avoids the negative quartic; all other arithmetic is nonnegative.
   check(totals[n][0]==c0,"cost-zero formula");
   check(totals[n][1]==c1,"cost-one formula");
   check(totals[n][2]==c2,"cost-two formula");
   check(totals[n][4]==c4,"cost-four formula");
  }
  cout<<"PRISM_TPR_VERIFIED_345: 81 states, 468 arcs, zero cycles 3 and 6, cost-one residue 5, four rational coefficient laws\n";
 }catch(const exception &e){cerr<<"VERIFY_FAILED: "<<e.what()<<"\n";return 1;}
}
