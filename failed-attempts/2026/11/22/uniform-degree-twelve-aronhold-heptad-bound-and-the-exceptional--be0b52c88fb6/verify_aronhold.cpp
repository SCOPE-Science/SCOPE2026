#include <bits/stdc++.h>
using namespace std;using U=uint64_t;
int B(int a,int b){return __builtin_parity((a&7)&(b>>3))^__builtin_parity((a>>3)&(b&7));}
int q(int a){return __builtin_parity((a&7)&(a>>3));}
int qa(int a,int x){return q(x)^B(a,x);}
int val(U m,int x){int r=0;for(int i=0;i<6;i++)if((x>>i)&1)r^=(m>>(6*i))&63;return r;}
U trans(U m,int v){U r=0;for(int j=0;j<6;j++){int c=(m>>(6*j))&63;if(B(c,v))c^=v;r|=U(c)<<(6*j);}return r;}
int invbasis(U m,int j){for(int i=0;i<64;i++)if(val(m,i)==(1<<j))return i;assert(0);return -1;}
int main(){vector<int> odds,evens;for(int a=0;a<64;a++)(q(a)?odds:evens).push_back(a);assert(odds.size()==28);
vector<array<int,7>> ah;unordered_map<uint32_t,int> octid;
for(int a=0;a<28;a++)for(int b=a+1;b<28;b++)for(int c=b+1;c<28;c++)for(int d=c+1;d<28;d++)for(int e=d+1;e<28;e++)for(int f=e+1;f<28;f++)for(int g=f+1;g<28;g++){
 array<int,7> t={a,b,c,d,e,f,g};bool ok=1;
 for(int i=0;i<7&&ok;i++)for(int j=i+1;j<7&&ok;j++)for(int k=j+1;k<7;k++)if(q(odds[t[i]]^odds[t[j]]^odds[t[k]])!=0){ok=0;break;}
 if(ok){uint32_t key=0;for(int k:t)key|=1u<<k;octid[key]=ah.size();ah.push_back(t);}
}
fprintf(stderr,"aronhold=%zu\n",ah.size());if(ah.size()!=288)return 1;
U id=0;for(int j=0;j<6;j++)id|=U(1<<j)<<(6*j);
vector<U> G;G.reserve(1451520);unordered_set<U>S;S.reserve(1600000);S.insert(id);G.push_back(id);
for(size_t i=0;i<G.size();i++)for(int v=1;v<64;v++){U m=trans(G[i],v);if(S.insert(m).second)G.push_back(m);}assert(G.size()==1451520);
map<pair<vector<int>,vector<int>>,pair<U,long long>> reps;
for(U m:G){int inv[6];for(int j=0;j<6;j++)inv[j]=invbasis(m,j);int perm[64];for(int a=0;a<64;a++){int b=0;for(int j=0;j<6;j++)if(qa(a,inv[j]))b^=(1<<((j+3)%6));perm[a]=b;}
 auto orbit=[&](vector<int>&arr){bool seen[64]={};vector<int>c;for(int a:arr){if(seen[a])continue;int y=a,k=0;do{seen[y]=1;y=perm[y];k++;}while(y!=a);c.push_back(k);}sort(c.begin(),c.end());return c;};
 auto sig=make_pair(orbit(odds),orbit(evens));auto&item=reps[sig];if(item.second++==0)item.first=m;
}
fprintf(stderr,"reps=%zu\n",reps.size());assert(reps.size()==30);
map<int,long long> degree_mass;map<int,int> kinds;
for(auto&[sig,item]:reps){U m=item.first;int inv[6];for(int j=0;j<6;j++)inv[j]=invbasis(m,j);
 int p[64];for(int a=0;a<64;a++){int b=0;for(int j=0;j<6;j++)if(qa(a,inv[j]))b^=(1<<((j+3)%6));p[a]=b;}
 int idx[64];fill(begin(idx),end(idx),-1);for(int k=0;k<28;k++)idx[odds[k]]=k;
 int aperm[288];for(int h=0;h<288;h++){uint32_t mask=0;for(int a:ah[h])mask|=1u<<idx[p[odds[a]]];auto it=octid.find(mask);if(it==octid.end()){cerr<<"not heptad";return 2;}aperm[h]=it->second;}
 bool seen[288]={};vector<int>cycle;for(int a=0;a<288;a++)if(!seen[a]){int x=a,n=0;do{seen[x]=1;x=aperm[x];n++;}while(x!=a);cycle.push_back(n);}
 sort(cycle.begin(),cycle.end());int mn=cycle[0];degree_mass[mn]+=item.second;kinds[mn]++;
 cout<<"ARON_MIN "<<mn<<" CLASS_SIZE "<<item.second<<" ODD_MIN "<<sig.first.front()<<" EVEN_MIN "<<sig.second.front()<<" ARON_PROFILE";for(auto len:cycle)cout<<" "<<len;cout<<"\n";
}
for(auto [v,n]:degree_mass)cout<<"MIN "<<v<<" ELEMENT_COUNT "<<n<<" CLASSES "<<kinds[v]<<"\n";
}
