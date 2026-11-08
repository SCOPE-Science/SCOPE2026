// Independently generate all derangements and form adjacency using direct swaps.
#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <vector>
using namespace std;
int main(){
for(int n=3;n<=9;n++){
 vector<vector<int>> a;vector<int> p(n);iota(p.begin(),p.end(),0);
 do{bool ok=true;for(int i=0;i<n;i++)if(p[i]==i)ok=false;if(ok)a.push_back(p);}while(next_permutation(p.begin(),p.end()));
 map<vector<int>,int> where;for(int i=0;i<(int)a.size();i++)where[a[i]]=i;
 vector<int> parent(a.size()),size(a.size(),1),sig(a.size());iota(parent.begin(),parent.end(),0);
 auto find=[&](int v){while(parent[v]!=v){parent[v]=parent[parent[v]];v=parent[v];}return v;};
 auto join=[&](int a,int b){a=find(a);b=find(b);if(a!=b){parent[b]=a;size[a]+=size[b];}};
 int isolates=0;
 for(int j=0;j<(int)a.size();j++){
  int k=0,deg=0;for(int i=0;i<n;i++)k+=(a[j][i]>i);sig[j]=k;
  for(int i=0;i<n;i++){
   vector<int> q=a[j];swap(q[i],q[(i+1)%n]);auto it=where.find(q);
   if(it!=where.end()){join(j,it->second);deg++;}
  }
  isolates+=(deg==0);
 }
 map<int,int> components,counts;map<int,int> root_sig;
 for(int j=0;j<(int)a.size();j++){
  counts[sig[j]]++;int root=find(j);
  if(root_sig.count(root)&&root_sig[root]!=sig[j])return 1;
  root_sig[root]=sig[j];components[root]=size[root];
 }
 if((int)components.size()!=n-1||isolates!=2)return 2;
 map<int,int> bysig;for(auto kv:components)bysig[root_sig[kv.first]]=kv.second;
 if(bysig!=counts)return 3;
 cout<<"CPP_CYCLIC_PASS n="<<n<<" states="<<a.size()<<" components="<<components.size()<<" isolates="<<isolates<<"\n";
}
 cout<<"CPP_INDEPENDENT_EXHAUSTIVE_PASS\n";
}
