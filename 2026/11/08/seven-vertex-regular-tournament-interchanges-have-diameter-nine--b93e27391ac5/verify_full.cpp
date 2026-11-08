#include <bits/stdc++.h>
using namespace std;
int id[7][7];
int main(){
 int m=0;for(int i=0;i<7;i++)for(int j=i+1;j<7;j++)id[i][j]=id[j][i]=m++;
 vector<int> states;states.reserve(2640);
 for(int mask=0;mask<(1<<21);mask++){
  int deg[7]={};for(int i=0;i<7;i++)for(int j=i+1;j<7;j++){
   if(mask&(1<<id[i][j]))deg[i]++;else deg[j]++;
  }
  bool ok=1;for(int i=0;i<7;i++)if(deg[i]!=3){ok=0;break;}
  if(ok)states.push_back(mask);
 }
 cerr<<"states "<<states.size()<<"\n";
 unordered_map<int,int> index;for(int i=0;i<(int)states.size();i++)index[states[i]]=i;
 vector<array<int,3>> triples;for(int a=0;a<7;a++)for(int b=a+1;b<7;b++)for(int c=b+1;c<7;c++)triples.push_back({a,b,c});
 vector<vector<int>> adj(states.size());long long edges=0;
 vector<int> hist(36);for(int i=0;i<(int)states.size();i++){
  int mm=states[i];
  for(auto [a,b,c]:triples){
    int p=(mm>>id[a][b])&1,q=(mm>>id[a][c])&1,r=(mm>>id[b][c])&1;
    if(p==r && p!=q){
      int mm2=mm^(1<<id[a][b])^(1<<id[a][c])^(1<<id[b][c]);
      auto it=index.find(mm2);if(it==index.end()){cerr<<"ERROR NONREG\n";return 1;}
      adj[i].push_back(it->second);
    }
  }
  hist[adj[i].size()]++;edges+=adj[i].size();
 }
 cerr<<"edges "<<edges/2<<" deg_hist ";for(int k=0;k<36;k++)if(hist[k])cerr<<k<<":"<<hist[k]<<",";cerr<<"\n";
 int D=0,R=INT_MAX;vector<long long> distcount(states.size(),0);map<int,int> ecc;
 vector<int> eccs(states.size()), per(100);long long pairs=0;
 for(int s=0;s<(int)states.size();s++){
  vector<int> d(states.size(),-1);queue<int>q;d[s]=0;q.push(s);
  while(!q.empty()){int v=q.front();q.pop();for(int w:adj[v])if(d[w]<0){d[w]=d[v]+1;q.push(w);}}
  if(any_of(d.begin(),d.end(),[](int k){return k<0;})){cerr<<"DISCONNECTED\n";return 2;}
  int e=*max_element(d.begin(),d.end());
  ecc[e]++;eccs[s]=e; D=max(D,e);R=min(R,e);
  int far=0;for(int j=0;j<(int)states.size();j++)if(d[j]==9){far++;if(states[j]!=(states[s]^((1<<21)-1))){cerr<<"NONCOMPLEMENT DIAMETRAL PAIR\n";return 3;}}
  if(e==9 && far!=1){cerr<<"NONUNIQUE ANTIPODE\n";return 4;}
  for(int j=s+1;j<(int)states.size();j++){per[d[j]]++;pairs++;}
 }
 cout<<"N="<<states.size()<<" M="<<edges/2<<" R="<<R<<" D="<<D<<"\nEcc ";for(auto [e,n]:ecc)cout<<e<<":"<<n<<" ";cout<<"\nPairs ";for(int k=0;k<100;k++)if(per[k])cout<<k<<":"<<per[k]<<" ";cout<<"\n";
 const vector<int> expected={0,18480,120120,447720,970200,1116960,637440,158880,13320,360};
 if(states.size()!=2640||edges/2!=18480||R!=8||D!=9||ecc[8]!=1920||ecc[9]!=720||!equal(expected.begin(),expected.end(),per.begin()) || pairs!=3483480){cerr<<"METRIC CHECK FAILED\n";return 5;}
 for(int i=0;i<2640;i++){if(adj[i].size()!=14){cerr<<"DEGREE FAILED\n";return 6;}}
 cout<<"CPP_EXHAUSTIVE_PASS\n";

}
