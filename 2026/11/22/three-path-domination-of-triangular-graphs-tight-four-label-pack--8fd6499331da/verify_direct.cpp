#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>
using namespace std;
struct P3 {int a,b,c; unsigned long long dominated; unsigned int support;};
void check(int n, int predicted_k, unsigned long long expected, bool exact_count) {
 vector<pair<int,int>> edge;
 for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)edge.push_back({a,b});
 int m=edge.size(); if(m>64)throw runtime_error("not for this size");
 vector<unsigned long long> closed(m);
 for(int i=0;i<m;i++)for(int j=0;j<m;j++)
  if(i==j || edge[i].first==edge[j].first || edge[i].first==edge[j].second || edge[i].second==edge[j].first || edge[i].second==edge[j].second) closed[i] |= 1ULL<<j;
 vector<P3> paths;
 for(int b=0;b<m;b++)for(int a=0;a<m;a++)if(a!=b && (closed[a]>>b&1ULL))
   for(int c=a+1;c<m;c++) if(c!=b && (closed[b]>>c&1ULL)) {
    unsigned int s=0; for(int j:{a,b,c})s |= 1U<<edge[j].first | 1U<<edge[j].second;
    paths.push_back({a,b,c,closed[a]|closed[b]|closed[c],s});
   }
 unsigned long long full=(1ULL<<m)-1;
 unsigned long long single=0,pair=0,goodtight=0; vector<std::pair<size_t,size_t>> samples;
 for(auto& p:paths)if(p.dominated==full)single++;
 if(predicted_k==2)for(size_t i=0;i<paths.size();i++)for(size_t j=i+1;j<paths.size();j++)
  if((paths[i].dominated | paths[j].dominated)==full) {
   pair++; if(n==9 && samples.size()<30) samples.push_back({i,j});
   if((paths[i].support & paths[j].support)==0 && __builtin_popcount(paths[i].support)==4 && __builtin_popcount(paths[j].support)==4)goodtight++;
  }
 unsigned long long observed=predicted_k==1?single:pair;
 cout<<"n="<<n<<" Jvertices="<<m<<" paths="<<paths.size()<<" min_count="<<observed<<" tight="<<goodtight<<"\n";
 if(exact_count && observed!=expected)throw runtime_error("count mismatch");
 if(predicted_k==2 && n==9 && goodtight!=pair)throw runtime_error("non-tight optimum at n=9");
 if(n==9)for(auto [i,j]:samples){int deg=0;for(size_t p=0;p<paths.size();p++){
   if(p!=i && p!=j && (paths[p].dominated | paths[j].dominated)==full)deg++;
   if(p!=i && p!=j && (paths[p].dominated | paths[i].dominated)==full)deg++;
  }if(deg!=238)throw runtime_error("sample exchange degree mismatch");
 }
 if(n>=5 && single!=0 && predicted_k>1)throw runtime_error("unexpected single path");
}
int main(){check(5,1,120,true); check(8,2,0,false); check(9,2,181440,true); cout<<"DIRECT CHECKS PASSED\n";}
