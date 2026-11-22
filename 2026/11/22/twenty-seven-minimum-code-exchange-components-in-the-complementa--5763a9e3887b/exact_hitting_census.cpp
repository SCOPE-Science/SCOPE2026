// Exact identification and optimum one-vertex-exchange census for the complementary nine-cycle prism.
// This is a standalone finite proof checker: all 2^18 subsets are tested by neighborhood-hitting clauses.
#include <bits/stdc++.h>
using namespace std;
int main(){
 constexpr int n=9,V=18;
 vector<uint32_t> N(V,0);
 auto add=[&](int a,int b){N[a]|=1u<<b;N[b]|=1u<<a;};
 for(int i=0;i<n;i++){
   add(i,(i+1)%n);add(i,i+n);
   for(int j=i+1;j<n;j++)if(j!=(i+1)%n && i!=(j+1)%n)add(i+n,j+n);
 }
 for(int i=0;i<V;i++)N[i]|=1u<<i;
 vector<uint32_t> requirements=N;
 for(int i=0;i<V;i++)for(int j=0;j<i;j++)requirements.push_back(N[i]^N[j]);
 if(requirements.size()!=171) return 1;
 vector<int> count(V+1,0), optimum;
 for(uint32_t S=0;S<(1u<<V);S++){
   bool valid=true;
   for(uint32_t R:requirements)if(!(R&S)){valid=false;break;}
   if(!valid)continue;
   int w=__builtin_popcount(S);count[w]++;
   if(w==7)optimum.push_back(S);
 }
 if(accumulate(count.begin(),count.begin()+7,0)!=0||count[7]!=90||optimum.size()!=90) return 2;
 unordered_map<uint32_t,int> index;
 for(int i=0;i<(int)optimum.size();i++)index[optimum[i]]=i;
 vector<vector<int>> adj(optimum.size());int edges=0;
 for(int i=0;i<(int)optimum.size();i++){
   uint32_t S=optimum[i];
   for(int a=0;a<V;a++)if((S>>a)&1u)
     for(int b=0;b<V;b++)if(!((S>>b)&1u)){
       auto it=index.find(S^(1u<<a)^(1u<<b));
       if(it!=index.end()){
         int j=it->second;adj[i].push_back(j);if(i<j)edges++;
       }
     }
 }
 if(edges!=81)return 3;
 vector<int> seen(optimum.size(),0);
 map<tuple<int,int,vector<int>>,int> components;
 for(int i=0;i<(int)optimum.size();i++)if(!seen[i]){
   queue<int>Q;Q.push(i);seen[i]=1;vector<int> comp;
   while(!Q.empty()){
     int x=Q.front();Q.pop();comp.push_back(x);
     for(int y:adj[x])if(!seen[y]){seen[y]=1;Q.push(y);}
   }
   vector<int> degrees;int twice_edges=0;
   for(int x:comp){degrees.push_back(adj[x].size());twice_edges+=adj[x].size();}
   sort(degrees.begin(),degrees.end());
   components[{(int)comp.size(),twice_edges/2,degrees}]++;
 }
 if(components[{5,6,{2,2,2,2,4}}]!=9 ||
    components[{3,2,{1,1,2}}]!=9 ||
    components[{2,1,{1,1}}]!=9 || components.size()!=3)return 4;
 cout<<"PASS all 262144 subsets; minimum 7; 90 optima; 81 exchanges; ";
 cout<<"9 bowties + 9 three-vertex paths + 9 edges.\n";
 cout<<"All cardinality counts:";
 for(int i=0;i<=V;i++)cout<<" "<<i<<":"<<count[i];
 cout<<"\n";
}
