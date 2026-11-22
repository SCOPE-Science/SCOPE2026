// Standalone finite checker for a 16-vertex Cayley graph and power-domination exchange.
#include <bits/stdc++.h>
using namespace std;
int main() {
 const unsigned full = 65535u;
 int step[5]={1,2,4,8,15};
 unsigned nbh[16]={};
 for (int v=0;v<16;++v) for(int d:step) nbh[v]|=1u<<(v^d);
 auto countbits=[](unsigned a) {return __builtin_popcount(a);};
 auto closure=[&](unsigned s){
   unsigned o=s;
   for(int v=0;v<16;v++) if(s>>v&1) o|=nbh[v];
   int waves=0;
   while(true){
     unsigned add=0;
     for(int v=0;v<16;v++) if(o>>v&1){
       unsigned w=nbh[v]&~o;
       if(w && !(w&(w-1)))add|=w;
     }
     if(!(add&~o)) return make_pair(o,waves);
     o|=add; ++waves;
   }
 };
 array<int,17> cnt={};
 vector<unsigned char> good(65536,0);
 vector<unsigned> minimum, fail3,fail4;
 for(unsigned s=0;s<65536;++s){
   auto [o,w]=closure(s);
   bool ok=o==full;
   good[s]=ok; int k=countbits(s);
   if(ok){cnt[k]++;if(w>1) return 1;}
   if(k==3){if(ok)minimum.push_back(s);else fail3.push_back(s);}
   if(k==4&&!ok)fail4.push_back(s);
   int edges=0; int deg[16]={};
   if(k==3 || k==4) {
     for(int a=0;a<16;++a) if(s>>a&1)for(int b=a+1;b<16;++b) if((s>>b&1) && (nbh[a]>>b&1)){
       edges++;deg[a]++;deg[b]++;
     }
     if(k==3 && ok != (edges==0 || edges==2))return 2;
     if(k==4){
       bool matching=edges==2;
       for(int v=0;v<16;++v)if(s>>v&1 && deg[v]!=1)matching=false;
       if((!ok)!=matching)return 3;
     }
   }
   if(k<=2&&ok)return 4;
   if(k>=5&&!ok)return 5;
 }
 if(minimum.size()!=320 || fail3.size()!=240 || fail4.size()!=60 || cnt[4]!=1760)return 6;
 for(unsigned x:fail3){int ext=0;for(unsigned y:fail4)if((x&y)==x)ext++; if(ext!=1)return 7;}
 vector<int> ids(65536,-1);
 for(int i=0;i<(int)minimum.size();++i)ids[minimum[i]]=i;
 vector<vector<int>> adj(minimum.size());
 long long e=0;
 for(int i=0;i<(int)minimum.size();++i){
   unsigned s=minimum[i];
   for(int a=0;a<16;++a)if(s>>a&1)
   for(int b=0;b<16;++b)if(!(s>>b&1)){
     unsigned t=(s^(1u<<a))|(1u<<b);
     if(ids[t]>=0)adj[i].push_back(ids[t]);
   }
   if(adj[i].size()!=21)return 8;
   e+=adj[i].size();
 }
 if(e/2!=3360)return 9;
 for(int root=0;root<(int)minimum.size();++root){
   vector<int> d(minimum.size(),-1);queue<int> q;q.push(root);d[root]=0;
   while(!q.empty()){
     int v=q.front();q.pop();
     for(int u:adj[v])if(d[u]==-1){d[u]=d[v]+1;q.push(u);}
   }
   array<int,4> shells={};
   for(int z:d){if(z<0||z>3)return 10;shells[z]++;}
   if(shells!=array<int,4>{1,21,126,172})return 11;
 }
 cout<<"CPP_VERIFY_OK states=65536 min=320 failed3=240 failed4=60 unique_extension=240 edges=3360 diameter=3\n";
}
