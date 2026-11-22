#include <bits/stdc++.h>
using namespace std;
using u128=__uint128_t;
struct H{size_t operator()(u128 x)const{return (uint64_t)x^(uint64_t)(x>>64)*0x9e3779b97f4a7c15ULL;}};
using Flag=array<uint16_t,8>;
struct Data{vector<Flag> c;unordered_map<u128,int,H> idx;vector<vector<pair<int,int>>> boundary,coface;vector<unsigned char>alive;vector<int>degree;};
vector<Data> D;
vector<int> faces;
int trans[8][1364];
vector<vector<int>> sup;
u128 key(const Flag &f,int l){u128 x=0;for(int i=0;i<l;i++)x|=(u128)f[i]<<(11*i);return x;}
Flag canonical(const Flag&f,int l){Flag best=f;for(int a=0;a<8;a++){Flag cur{};for(int j=0;j<l;j++)cur[j]=trans[a][f[j]];if(lexicographical_compare(cur.begin(),cur.begin()+l,best.begin(),best.begin()+l))best=cur;}return best;}
int main(){auto tic=chrono::steady_clock::now();auto secs=[&](){return chrono::duration<double>(chrono::steady_clock::now()-tic).count();};
 const int N=16;array<int,N> adj{};for(int i=0;i<N;i++)for(int j=0;j<N;j++){int x=abs(i/4-j/4),y=abs(i%4-j%4);if((x==1&&y==2)||(x==2&&y==1))adj[i]|=1<<j;}
 function<void(int,int)> rec=[&](int s,int possible){if(s)faces.push_back(s);while(possible){int b=possible&-possible;possible^=b;int v=__builtin_ctz((unsigned)b);rec(s|b,possible&~adj[v]);}};rec(0,(1<<N)-1);
 sort(faces.begin(),faces.end());unordered_map<int,int> face_idx;for(int i=0;i<(int)faces.size();i++)face_idx[faces[i]]=i;
 vector<array<int,N>> perms;for(int a=0;a<8;a++){array<int,N> p;for(int i=0;i<N;i++){int r=i/4,c=i%4;if(a>=4)c=3-c;for(int t=0;t<a%4;t++){int r2=c,c2=3-r;r=r2;c=c2;}p[i]=4*r+c;}perms.push_back(p);}
 for(int a=0;a<8;a++)for(int i=0;i<(int)faces.size();i++){int fm=0;for(int j=0;j<N;j++)if((faces[i]>>j)&1)fm|=1<<perms[a][j];trans[a][i]=face_idx.at(fm);}
 sup.resize(faces.size());for(int i=0;i<(int)faces.size();i++)for(int j=0;j<(int)faces.size();j++)if(i!=j&&(faces[i]&faces[j])==faces[i])sup[i].push_back(j);
 vector<Flag> current;for(int i=0;i<(int)faces.size();i++){Flag f{};f[0]=i;if(key(canonical(f,1),1)==key(f,1))current.push_back(f);}
 for(int d=0;d<8&&current.size();d++){
  Data data;data.c=move(current);data.idx.reserve(data.c.size()*1.2);for(int i=0;i<(int)data.c.size();i++)data.idx[key(data.c[i],d+1)]=i;
  cerr<<"dim "<<d<<" n="<<data.c.size()<<" at="<<secs()<<"\n";
  if(d>0){auto &lower=D.back();data.boundary.resize(data.c.size());lower.coface.resize(lower.c.size());
   for(int i=0;i<(int)data.c.size();i++){
    auto &f=data.c[i];vector<pair<int,int>> b;
    for(int j=0;j<=d;j++){Flag sub{};int k=0;for(int h=0;h<=d;h++)if(h!=j)sub[k++]=f[h];auto can=canonical(sub,d);int idx=lower.idx.at(key(can,d));bool found=false;for(auto &kv:b)if(kv.first==idx){kv.second+=((j%2)?-1:1);found=true;break;}if(!found)b.push_back({idx,((j%2)?-1:1)});}
    for(auto [r,v]:b)if(v){data.boundary[i].push_back({r,v});lower.coface[r].push_back({i,v});}
   }
  }
  D.push_back(move(data));
  vector<Flag> next;next.reserve(D.back().c.size()*2);
  for(const auto &ch:D.back().c){auto last=ch[d];int same[8];int ns=0;
   for(int a=0;a<8;a++){bool ok=1;for(int j=0;j<=d;j++)if(trans[a][ch[j]]!=ch[j]){ok=0;break;}if(ok)same[ns++]=a;}
   for(int s:sup[last]){int mm=s;for(int j=0;j<ns;j++)mm=min(mm,trans[same[j]][s]);if(mm==s){Flag f=ch;f[d+1]=s;next.push_back(f);}}
  }
  current=move(next);
 }
 // collapse free-face pairs with coefficient +-1
 for(auto &dd:D){dd.alive.assign(dd.c.size(),1);dd.degree.assign(dd.c.size(),0);}
 deque<pair<int,int>> q;
 for(int d=0;d+1<(int)D.size();d++)for(int f=0;f<(int)D[d].c.size();f++){D[d].degree[f]=D[d].coface[f].size();if(D[d].degree[f]==1&&abs(D[d].coface[f][0].second)==1)q.push_back({d,f});}
 int ncollapse=0;
 while(q.size()){
  auto [d,f]=q.front();q.pop_front();if(!D[d].alive[f]||D[d].degree[f]!=1)continue;
  int c=-1,coef=0;for(auto [i,v]:D[d].coface[f])if(D[d+1].alive[i]){c=i;coef=v;break;}
  if(c<0||abs(coef)!=1)continue;
  D[d].alive[f]=0;D[d+1].alive[c]=0;ncollapse++;
  for(auto [r,v]:D[d+1].boundary[c])if(D[d].alive[r]){int deg=--D[d].degree[r];if(deg==1){for(auto [ci,w]:D[d].coface[r])if(D[d+1].alive[ci]&&abs(w)==1){q.push_back({d,r});break;}}}
  if(d>0)for(auto [r,v]:D[d].boundary[f])if(D[d-1].alive[r]){int deg=--D[d-1].degree[r];if(deg==1){for(auto [ci,w]:D[d-1].coface[r])if(D[d].alive[ci]&&abs(w)==1){q.push_back({d-1,r});break;}}}
 }
 cerr<<"COLLAPSE "<<ncollapse<<" elapsed "<<secs()<<" remain:";for(auto &dd:D)cerr<<' '<<count(dd.alive.begin(),dd.alive.end(),1);cerr<<"\n";
 // save remaining boundary rows and cell positions to file text, each d block, rows d-1 index remapped
 ofstream out("quotient_reduced.txt");out<<D.size()<<'\n';vector<vector<int>> id(D.size());for(int d=0;d<(int)D.size();d++){id[d].assign(D[d].c.size(),-1);int n=0;for(int i=0;i<(int)D[d].c.size();i++)if(D[d].alive[i])id[d][i]=n++;out<<n<<'\n';}
 for(int d=1;d<(int)D.size();d++)for(int i=0;i<(int)D[d].c.size();i++)if(D[d].alive[i]){vector<pair<int,int>> b;for(auto [r,v]:D[d].boundary[i])if(D[d-1].alive[r])b.push_back({id[d-1][r],v});out<<b.size();for(auto [r,v]:b)out<<' '<<r<<' '<<v;out<<'\n';}
 out<<"FLAGS\n";for(int d=0;d<(int)D.size();d++)for(int i=0;i<(int)D[d].c.size();i++)if(D[d].alive[i]){out<<d;for(int j=0;j<=d;j++)out<<" "<<D[d].c[i][j];out<<"\n";}
 out.close();cerr<<"wrote reduced elapsed "<<secs()<<"\n";
}
