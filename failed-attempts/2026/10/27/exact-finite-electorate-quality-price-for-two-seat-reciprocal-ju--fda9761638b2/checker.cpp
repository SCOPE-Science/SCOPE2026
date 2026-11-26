// Exact finite-domain regression for the two-seat reciprocal-JR quality-price theorem.
// Compile: g++ -O2 -std=c++17 checker.cpp -o checker && ./checker
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;
static const int QUALITY[] = {6,8,9,12}; // exact twelfths, all <=1
struct Totals { unsigned long long cases=0, sharp_hits=0; };
static bool is_rjr(const vector<int>& supp,const vector<int>& q,int n,int a,int b){
  int represented=supp[a]|supp[b];
  int unrepresented=((1<<n)-1) & ~represented;
  for(int c=0;c<(int)supp.size();++c){
    int eligible=__builtin_popcount((unsigned)(supp[c]&unrepresented));
    if(2*q[c]*eligible >= 12*n) return false;
  }
  return true;
}
static void process(const vector<int>& supp,const vector<int>& q,int n,Totals &z){
  int m=supp.size();
  int top=0, best=-1;
  for(int i=0;i<m;i++)for(int j=i+1;j<m;j++){
    int s=q[i]+q[j]; top=max(top,s);
    if(is_rjr(supp,q,n,i,j))best=max(best,s);
  }
  if(best<0){cerr<<"No reciprocal JR!"<<endl;exit(2);}
  // (top / best) <= 4(n-1)/(3n-2), entirely in exact integers.
  if((long long)top*(3*n-2)>(long long)best*4*(n-1)){
    cerr<<"Counterexample: n="<<n<<" top="<<top<<" best="<<best<<endl;
    for(int x:supp)cerr<<x<<",";cerr<<endl; for(int x:q)cerr<<x<<",";cerr<<endl;exit(2);
  }
  ++z.cases;
  if((long long)top*(3*n-2)==(long long)best*4*(n-1))++z.sharp_hits;
}
static void exhaust(int n,int m){
  int smax=(1<<n)-1;
  vector<int> supp(m),q(m);
  Totals z;
  unsigned long long patterns=1, values=1;
  for(int i=0;i<m;i++){patterns*=smax;values*=4;}
  for(unsigned long long ip=0;ip<patterns;ip++){
    unsigned long long tmp=ip;
    for(int j=0;j<m;j++){supp[j]=1+(tmp % smax);tmp/=smax;}
    for(unsigned long long iq=0;iq<values;iq++){
      unsigned long long t=iq;
      for(int j=0;j<m;j++){q[j]=QUALITY[t%4];t/=4;}
      process(supp,q,n,z);
    }
  }
  cout<<"n="<<n<<" m="<<m<<" exhaustive="<<z.cases<<" equality="<<z.sharp_hits<<" PASS\n";
}
static void extremal(int n){
  vector<int> supp={1,1,((1<<n)-1)^1};
  // Work at common denominator 2(n-1), not restricted to the quality grid.
  int den=2*(n-1);
  vector<int> q={den,den,n};
  int best=-1;
  for(int i=0;i<3;i++)for(int j=i+1;j<3;j++){
    int uncovered=((1<<n)-1)&~(supp[i]|supp[j]);
    bool valid=true;
    for(int c=0;c<3;c++) if(2*q[c]*__builtin_popcount((unsigned)(supp[c]&uncovered))>=n*den)valid=false;
    if(valid)best=max(best,q[i]+q[j]);
  }
  assert(best==den+n);
  assert((long long)2*den*(3*n-2)==(long long)4*(n-1)*(den+n));
  cout<<"n="<<n<<" exact-extremal PASS\n";
}
int main(){
  for(int n=2;n<=5;n++)exhaust(n,3);
  for(int n=2;n<=3;n++)exhaust(n,4);
  for(int n=2;n<=15;n++)extremal(n);
  cout<<"ALL EXACT CHECKS PASS\n";
}
