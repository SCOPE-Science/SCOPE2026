// Enumerates NOC clustering systems by the defining witness property.
// Compile: g++ -std=c++17 -O3 noc_incremental.cpp -o noc_census
#include <cstdint>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdlib>
using namespace std;
struct Work {
 int n, full; vector<int> optional, active, witness; vector<unsigned long long> hist; unsigned long long nodes=0,leaves=0,prunes=0;
 bool overlap(int a,int b){int c=a&b;return c && c!=a && c!=b;}
 int reticulations(){
   vector<int> sets=active;
   for(int i=0;i<n;++i) sets.push_back(1<<i);
   sets.push_back(full);
   int ret=0;
   for(int c:sets){
     int parents=0;
     for(int a:sets) if(a!=c && (a&c)==c){
       bool covered=true;
       for(int mid:sets) if(mid!=a && mid!=c && (mid&c)==c && (a&mid)==mid){covered=false;break;}
       if(covered) ++parents;
     }
     if(parents>=2) ++ret;
   }
   return ret;
 }
 void rec(int idx){
   ++nodes;
   if(idx==(int)optional.size()){
     ++leaves;int ret=reticulations(); if(ret>= (int)hist.size())hist.resize(ret+1);++hist[ret];return;
   }
   rec(idx+1); // omit optional cluster
   int s=optional[idx], w=s;
   vector<pair<int,int>> changes;
   bool ok=true;
   for(int j=0;j<(int)active.size();++j){
     int a=active[j]; if(!overlap(a,s))continue;
     w &= ~a;
     int nw=witness[j] & ~s;
     if(!nw){ok=false;break;}
     changes.emplace_back(j,witness[j]); witness[j]=nw;
   }
   if(ok && w){active.push_back(s);witness.push_back(w);rec(idx+1);active.pop_back();witness.pop_back();}
   else ++prunes;
   for(auto it=changes.rbegin();it!=changes.rend();++it)witness[it->first]=it->second;
 }
 void run(){full=(1<<n)-1;for(int m=1;m<full;++m) if(__builtin_popcount((unsigned)m)>=2) optional.push_back(m);
    // Order largest clusters first to prune quickly, but still enumerate all subsets.
    sort(optional.begin(),optional.end(),[](int a,int b){int pa=__builtin_popcount((unsigned)a),pb=__builtin_popcount((unsigned)b);return pa==pb?a<b:pa>pb;});
    rec(0);
    printf("n=%d optional=%zu leaves=%llu nodes=%llu prunes=%llu\n",n,optional.size(),leaves,nodes,prunes);
    for(int k=0;k<(int)hist.size();++k) if(hist[k])printf("k=%d count=%llu\n",k,hist[k]);
 }
};
int main(int argc,char**argv){int n=argc>1?atoi(argv[1]):5;if(n<2||n>6)return 2;Work w;w.n=n;w.run();}
