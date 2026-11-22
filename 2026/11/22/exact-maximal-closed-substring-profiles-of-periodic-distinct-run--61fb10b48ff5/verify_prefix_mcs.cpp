// Standalone literal checker for maximal closed substring occurrences.
// Build: c++ -std=c++17 -O2 verify_prefix_mcs.cpp -o verify_prefix_mcs
// Run: ./verify_prefix_mcs
#include <algorithm>
#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <random>
#include <cassert>
using namespace std;
using interval=pair<int,int>;

set<interval> brute(const string &w){
 int n=w.size();
 vector<vector<int>> lcp(n+1,vector<int>(n+1,0));
 for(int i=n-1;i>=0;--i) for(int j=n-1;j>=0;--j)
  if(w[i]==w[j]) lcp[i][j]=1+lcp[i+1][j+1];
 vector<vector<bool>> cl(n,vector<bool>(n,false));
 for(int i=0;i<n;i++) for(int j=i;j<n;j++){
  if(j==i){cl[i][j]=true;continue;}
  int len=j-i+1,best=0;
  for(int t=1;t<len;t++) if(lcp[i][j-t+1]>=t)best=t;
  if(!best)continue;
  bool internal=false;
  for(int a=i+1;a<j-best+1;a++) if(lcp[i][a]>=best){internal=true;break;}
  cl[i][j]=!internal;
 }
 set<interval> out;
 for(int i=0;i<n;i++)for(int j=i;j<n;j++)
  if(cl[i][j] && (i==0||!cl[i-1][j]) && (j==n-1||!cl[i][j+1]))out.insert({i,j});
 return out;
}

set<interval> predicted(const string &w,const vector<int> &runs){
 int n=w.size(),q=runs.size(),p=0;
 for(int x:runs)p+=x;
 set<interval> out;
 // Full monochromatic maximal runs.
 for(int i=0;i<n;){int j=i+1;while(j<n&&w[j]==w[i])++j;out.insert({i,j-1});i=j;}
 // Adjacent same-letter-run partial complete returns.
 int start=0;
 for(int a=0;a<q;a++){
  for(int j=0;;j++){
   int s=j*p+start;
   if(s+p+1>n) break;
   for(int h=1;h<runs[a];h++) if(s+p+h<=n)
    out.insert({s+runs[a]-h,s+p+h-1});
  }
  start+=runs[a];
 }
 // Entire prefix closed iff its first and last cycle phases give a complete return.
 if(n>=p+runs[0])out.insert({0,n-1});
 return out;
}
int main(){
 long long cases=0,occurrences=0,compared=0;
 auto check=[&](const vector<int>&runs,int k,int t){
  string P;
  for(int i=0;i<(int)runs.size();i++)P.append(runs[i],char('a'+i));
  string W;
  for(int j=0;j<k;j++)W+=P;
  W+=P.substr(0,t);
  auto x=brute(W),y=predicted(W,runs);
  if(x!=y){
   cerr<<"MISMATCH P="<<P<<" k="<<k<<" t="<<t<<" brute="<<x.size()<<" predicted="<<y.size()<<'\n';
   for(auto z:x) if(!y.count(z))cerr<<"missing "<<z.first<<","<<z.second<<'\n';
   for(auto z:y) if(!x.count(z))cerr<<"extra "<<z.first<<","<<z.second<<'\n';
   exit(1);
  }
  cases++;occurrences+=x.size();compared+=W.size()*(W.size()+1LL)/2;
 };
 for(int q=2;q<=4;q++){
  long long total=1;for(int i=0;i<q;i++)total*=3;
  for(int code=0;code<total;code++){
   int x=code,p=0;vector<int> r(q);
   for(int j=0;j<q;j++){r[j]=1+x%3;x/=3;p+=r[j];}
   for(int k=1;k<=4;k++)for(int t=0;t<p;t++)check(r,k,t);
  }
 }
 std::mt19937 rng(741902);
 for(int z=0;z<180;z++){
  int q=2+rng()%7,k=1+rng()%4;vector<int> r(q);int p=0;
  for(int&i:r){i=1+rng()%5;p+=i;}
  if(p*k>140)k=1;
  check(r,k,rng()%p);
 }
 cout<<"PASS cases="<<cases<<" distinct_MCS_occurrences_checked="<<occurrences
     <<" substring_occurrences_considered="<<compared<<"\n";
}
