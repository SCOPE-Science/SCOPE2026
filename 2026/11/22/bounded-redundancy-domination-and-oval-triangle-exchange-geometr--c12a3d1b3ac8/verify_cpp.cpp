#include <bits/stdc++.h>
using namespace std; using ull=unsigned long long;
int mod(int x){x%=3;return x<0?x+3:x;}
struct P{int x,y,z; bool operator<(P const&o)const{return tie(x,y,z)<tie(o.x,o.y,o.z);} };
vector<P> V;
int N=26;ull maskall=(1ULL<<26)-1;ull nb[26];
vector<ull> valid;array<long long,8> sizecount{};map<pair<int,int>,int> parts;
void enumerate(int first,int rem,ull mask,int size){
 if(!rem){
  for(int i=0;i<N;i++) if(!(mask>>i&1)){
   int c=__builtin_popcountll(mask&nb[i]);if(c==0||c>2)return;
  }
  sizecount[size]++;parts[{size,__builtin_popcountll(mask&((1ULL<<13)-1))}]++;
  if(size==7)valid.push_back(mask);return;
 }
 for(int i=first;i<=N-rem;i++)enumerate(i+1,rem-1,mask|(1ULL<<i),size);
}
int main(){
 // A genuinely different affine-plus-infinity model of PG(2,3).
 // Points 3*x+y for x,y in F3, and infinity points 9+d for d=0,1,2,3.
 // Lines 3*d+b: d=0,1,2 means y=d*x+b, d=3 means x=b;
 // line 12 is the line at infinity.
 for(int d=0;d<4;d++)for(int b=0;b<3;b++){
    int l=3*d+b; nb[13+l]|=1ULL<<(9+d);nb[9+d]|=1ULL<<(13+l);
    for(int x=0;x<3;x++)for(int y=0;y<3;y++){
      if((d==3&&x==b)||(d<3&&mod(y-d*x)==b)){
        int p=3*x+y;nb[p]|=1ULL<<(13+l);nb[13+l]|=1ULL<<p;
      }
    }
 }
 for(int d=0;d<4;d++){nb[9+d]|=1ULL<<(13+12);nb[25]|=1ULL<<(9+d);}
 for(int i=0;i<13;i++)for(int j=i+1;j<13;j++){
  int common=0;for(int l=0;l<13;l++)if((nb[i]&(1ULL<<(13+l)))&&(nb[j]&(1ULL<<(13+l))))common++;
  assert(common==1);
 }
 for(int i=0;i<N;i++)assert(__builtin_popcountll(nb[i])==4);
 for(int k=1;k<=7;k++)enumerate(0,k,0,k);
 assert(sizecount[7]==468);for(int k=1;k<=6;k++)assert(sizecount[k]==0);
 assert(parts[make_pair(7,3)]==234 && parts[make_pair(7,4)]==234 && parts.size()==2);
 int n=valid.size();vector<vector<int>> G(n);
 for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(__builtin_popcountll(valid[i]&valid[j])==6){G[i].push_back(j);G[j].push_back(i);}
 long long edges=0;int diameter=0;set<vector<int>> profiles;
 for(int i=0;i<n;i++){
  assert(G[i].size()==4);edges+=G[i].size();
  vector<int> d(n,-1),cnt;queue<int> Q;Q.push(i);d[i]=0;
  while(!Q.empty()){
   int u=Q.front();Q.pop();for(int v:G[u])if(d[v]<0){d[v]=d[u]+1;Q.push(v);}
  }
  assert(find(d.begin(),d.end(),-1)==d.end());int m=*max_element(d.begin(),d.end());diameter=max(diameter,m);
  cnt.resize(m+1);for(int z:d)cnt[z]++;profiles.insert(cnt);
 }
 assert(edges/2==936 && diameter==9 && profiles.size()==1);
 cout<<"exhaustive 26-vertex size 1..7, PG(2,3): 468 minima, 234+234, 936 edges, degree 4, diameter 9\n";
 for(auto cnt:*profiles.begin()){cout<<cnt<<" ";}cout<<"\nC++ EXHAUSTIVE CHECK PASS\n";
}
