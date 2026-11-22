// Independent binary-coordinate enumerator for half-spin generator incidence.
#include <algorithm>
#include <cassert>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
int qform(int x,int n){return __builtin_parity((x&((1<<n)-1)) & (x>>n));}
int polar(int x,int y,int n){int m=(1<<n)-1;return __builtin_parity(((x&m)&(y>>n))^((y&m)&(x>>n)));}
int main(){
 for(int n=2;n<=4;++n){
  vector<int> pts; for(int v=1;v<(1<<(2*n));++v)if(!qform(v,n))pts.push_back(v);
  set<vector<int>> all,one;
  auto add=[&](const vector<int>& base){
   vector<int> span={0};for(int v:base){int sz=span.size();for(int k=0;k<sz;++k)span.push_back(span[k]^v);}
   sort(span.begin(),span.end());span.erase(unique(span.begin(),span.end()),span.end());
   if((int)span.size()!=(1<<n))return;
   all.insert(span);
   int count=0;for(int x:span)if(x<(1<<n))++count;
   int d=0;while((1<<d)<count)++d;
   if((n-d)%2==0)one.insert(span);
  };
  // Enumerate unordered bases; prune all nonorthogonal pairs before extension.
  auto rec=[&](auto&& rec,vector<int>&base,int j)->void{
   if((int)base.size()==n){add(base);return;}
   for(int k=j;k<(int)pts.size();++k){
    bool ok=true;for(int v:base)if(polar(v,pts[k],n)){ok=false;break;}
    if(!ok)continue;
    base.push_back(pts[k]);rec(rec,base,k+1);base.pop_back();
   }
  };
  vector<int>base;rec(rec,base,0);
  assert(all.size()==2*one.size());
  int expected=n==2?3:n==3?15:135; assert((int)one.size()==expected);
  vector<vector<int>> G(one.begin(),one.end());
  auto trace=[&](const vector<int>&Q){int hit=0;for(auto &g:G){int t=0;for(int j=0;j<(int)Q.size();j++)if(binary_search(g.begin(),g.end(),Q[j]))t|=1<<j;hit|=1<<t;}return hit==((1<<(1<<Q.size()))-1);};
  if(n==3){int a=0,b=0,c=0;for(int i=0;i<(int)pts.size();i++){if(trace({pts[i]}))++a;for(int j=i+1;j<(int)pts.size();j++){if(trace({pts[i],pts[j]}))++b;for(int k=j+1;k<(int)pts.size();k++)if(trace({pts[i],pts[j],pts[k]}))++c;}}
    assert(a==35&&b==315&&c==0);cout<<"q=2 rank=3 one_family=15 faces=1,35,315,0\n";
  }
  if(n==4){set<vector<int>> facets;for(auto &g:G){vector<int>s;for(int x:g)if(x)s.push_back(x);for(int i=0;i<(int)s.size();i++)for(int j=i+1;j<(int)s.size();j++)for(int k=j+1;k<(int)s.size();k++)if((s[i]^s[j])!=s[k])facets.insert({s[i],s[j],s[k]});}
    assert(facets.size()==56700);
    int t=0;for(auto &f:facets){if(t%200==0)assert(trace(f));++t;}
    cout<<"q=2 rank=4 one_family=135 independent_singular_triples=56700\n";
  }
  if(n==2){int s=0;for(int x:pts)if(trace({x}))++s;assert(s==9);cout<<"q=2 rank=2 one_family=3 singleton=9\n";}
 }
}
