// Exhaustive check of the structural lemma and small-order color optima.
#include <bits/stdc++.h>
using namespace std;
int main(){
 for(int n=5;n<=7;n++){
  vector<pair<int,int>> e;for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)e.push_back({a,b});int m=e.size();
  vector<uint32_t> N(m,0);for(int i=0;i<m;i++)for(int j=0;j<m;j++)if(i!=j){auto [a,b]=e[i];auto[c,d]=e[j];if(a!=c&&a!=d&&b!=c&&b!=d)N[i]|=1u<<j;}
  vector<uint32_t> valid,triangles,stars; long long unexpected=0,valid_count=0;
  for(uint32_t mask=1;mask<(1u<<m);mask++){
   int k=__builtin_popcount(mask);
   if(k>n-1)continue;
   bool independent=true;
   uint32_t q=mask;while(q){int j=__builtin_ctz(q);q&=q-1; if(N[j]&mask){independent=false;break;}}
   if(!independent)continue;
   bool odd=true;for(int i=0;i<m;i++){int t=__builtin_popcount(mask&N[i]);if(t && !(t&1)){odd=false;break;}}
   if(!odd)continue;
   valid_count++;
   bool classified=false;
   if(k==1)classified=true;
   if(k==3){set<int> v;int dv[30]={};uint32_t t=mask;while(t){int j=__builtin_ctz(t);t&=t-1;auto [a,b]=e[j];v.insert(a);v.insert(b);dv[a]++;dv[b]++;}if(v.size()==3 && *max_element(dv,dv+n)==2){classified=true;triangles.push_back(mask);}}
   if(k==n-1 && n%2==0){for(int x=0;x<n;x++){bool full=true;uint32_t t=mask;while(t){int j=__builtin_ctz(t);t&=t-1;auto[a,b]=e[j];if(a!=x&&b!=x)full=false;}if(full){classified=true;stars.push_back(mask);}}}
   if(!classified){unexpected++;if(unexpected<=3)cout<<"UNEXPECTED "<<n<<" "<<mask<<"\n";}
   valid.push_back(mask);
  }
  vector<vector<uint32_t>> by(m);for(auto u:valid){uint32_t t=u;while(t){int j=__builtin_ctz(t);t&=t-1;by[j].push_back(u);}}
  vector<unsigned char> dp(1u<<m,255);dp[0]=0;
  for(uint32_t mask=1;mask<(1u<<m);mask++){
   int bit=__builtin_ctz(mask);
   unsigned char best=255;
   for(auto c:by[bit])if((c&mask)==c && dp[mask^c]!=255)best=min(best,(unsigned char)(1+dp[mask^c]));
   dp[mask]=best;
  }
  cout<<"n="<<n<<" edge_vertices="<<m<<" accepted_classes="<<valid_count<<" triangles="<<triangles.size()<<" full_stars="<<stars.size()<<" unexpected="<<unexpected<<" exact_chi="<<(int)dp[(1u<<m)-1]<<"\n";
  if(unexpected) return 1;
 }
}
