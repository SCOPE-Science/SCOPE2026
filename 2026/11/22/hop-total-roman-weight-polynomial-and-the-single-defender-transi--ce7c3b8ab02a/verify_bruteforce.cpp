// Direct graph-distance verification of hop-total-Roman labelings.
#include <vector>
#include <iostream>
#include <map>
#include <string>
#include <cstdlib>
using namespace std;
int main(int argc, char**argv) {
 if(argc<3) return 2;
 vector<int> s; for(int j=1;j<argc;j++) {int x=atoi(argv[j]);if(x<2)return 2;s.push_back(x);}
 int n=1;for(auto x:s)n+=x;
 if(n>15) return 3;
 vector<vector<int>> a(n,vector<int>(n,0));
 int pos=1;
 for(int k:s) {
  for(int i=pos;i<pos+k;i++) {a[0][i]=a[i][0]=1;for(int j=pos;j<pos+k;j++)if(i!=j)a[i][j]=1;}
  pos+=k;
 }
 vector<vector<int>> d(n,vector<int>(n,999));
 for(int i=0;i<n;i++) for(int j=0;j<n;j++)d[i][j]=i==j?0:(a[i][j]?1:999);
 for(int k=0;k<n;k++)for(int i=0;i<n;i++)for(int j=0;j<n;j++)d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
 long long lim=1;for(int i=0;i<n;i++)lim*=3;
 map<int,long long> ans;
 vector<int> f(n);
 for(long long t=0;t<lim;t++) {
  long long v=t;int w=0;
  for(int i=0;i<n;i++){f[i]=v%3;v/=3;w+=f[i];}
  bool good=true;
  for(int i=0;i<n && good;i++) {
   if(f[i]==0){bool defended=false;for(int j=0;j<n;j++)if(f[j]==2 && d[i][j]==2){defended=true;break;}if(!defended)good=false;}
   else {bool neighbor=false;for(int j=0;j<n;j++)if(a[i][j]&&f[j]){neighbor=true;break;}if(!neighbor)good=false;}
  }
  if(good)ans[w]++;
 }
 for(int i=0;i<(int)s.size();i++) { cout<<(i?",":"")<<s[i]; } cout<<" ";
 for(auto x:ans) { cout<<x.first<<":"<<x.second<<" "; } cout<<"\n";
}
