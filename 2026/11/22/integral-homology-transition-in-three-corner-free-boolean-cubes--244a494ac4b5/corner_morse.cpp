#include <bits/stdc++.h>
using namespace std;
uint32_t forb[32][32];int vertex_count;vector<uint32_t> faces;unordered_map<uint32_t,int> idx;vector<int> partner;vector<uint8_t> status;vector<int> criticalid;vector<int> order;
void dfs(uint32_t mask,int v){if(v==vertex_count){faces.push_back(mask);return;}dfs(mask,v+1);for(int j=0;j<v;j++)if(mask>>j&1)for(int k=j+1;k<v;k++)if(mask>>k&1)if(forb[j][k]>>v&1)return;dfs(mask|(1u<<v),v+1);}
using Vec=vector<int64_t>;
int target_d,nrows;unordered_map<int,Vec> memo;long long calls=0,maxcoef=0;
int sign_delete(uint32_t m,int v){return (__builtin_popcount(m&((1u<<v)-1))%2)?-1:1;}
Vec const& reduce(int id){static const Vec empty;calls++;if(status[id]==2)return empty;auto it=memo.find(id);if(it!=memo.end())return it->second;Vec out(nrows,0);if(status[id]==0){int j=criticalid[id];if(j<0||j>=nrows){cerr<<"invalid crit "<<id<<" target "<<target_d<<endl;abort();}out[j]=1;}else{assert(status[id]==1);int upper=partner[id];uint32_t m=faces[upper];uint32_t low=faces[id];int diff=__builtin_ctz(m^low);int s0=sign_delete(m,diff);
for(int v=0;v<32;v++)if(m>>v&1){int rid=idx.at(m^(1u<<v));if(rid==id)continue;auto const& b=reduce(rid);int s=-s0*sign_delete(m,v);for(int k=0;k<(int)b.size();k++){out[k]+=(int64_t)s*b[k];maxcoef=max(maxcoef,llabs(out[k]));if(maxcoef>1000000000){cerr<<"big coefficient"<<endl;abort();}}}}
auto p=memo.emplace(id,move(out));return p.first->second;}
int main(int argc,char**argv){if(argc!=2){cerr<<"Usage: corner_morse n (2<=n<=5)\n";return 2;}int dim=stoi(argv[1]);if(dim<2||dim>5)return 2;vertex_count=1<<dim;order.resize(vertex_count);for(int a=0;a<dim;a++)for(int b=a+1;b<dim;b++){int bm=(1<<a)|(1<<b);for(int o=0;o<vertex_count;o++)if(!(o&bm)){int v[4]={o,o^(1<<a),o^(1<<b),o^bm};sort(v,v+4);for(int i=0;i<4;i++)for(int j=i+1;j<4;j++)for(int k=j+1;k<4;k++)forb[v[i]][v[j]]|=1u<<v[k];}}
dfs(0,0);sort(faces.begin(),faces.end());int N=faces.size();cerr<<"faces "<<N<<'\n';ofstream summary("summary_n"+to_string(dim)+".txt");summary<<"vertices "<<vertex_count<<"\nfaces "<<N<<"\n";
vector<int64_t> fcount(vertex_count+1);for(uint32_t mask:faces)fcount[__builtin_popcount(mask)]++;for(int k=0;k<=vertex_count;k++)if(fcount[k])summary<<"face_size "<<k<<" "<<fcount[k]<<"\n";
idx.reserve(N*1.35);for(int i=0;i<N;i++)idx[faces[i]]=i;partner.assign(N,-1);status.resize(N,0);iota(order.begin(),order.end(),0);
for(int v:order){uint32_t bit=1u<<v;for(int i=0;i<N;i++)if(status[i]==0 && !(faces[i]&bit)){auto it=idx.find(faces[i]|bit);if(it!=idx.end()&&!status[it->second]){int j=it->second;partner[i]=j;partner[j]=i;status[i]=1;status[j]=2;}}}
criticalid.assign(N,-1);map<int,vector<int>> bydim;for(int i=0;i<N;i++)if(!status[i]){int dim=__builtin_popcount(faces[i])-1;criticalid[i]=bydim[dim].size();bydim[dim].push_back(i);}
for(auto &[d,inds]:bydim){cerr<<"critical "<<d<<" "<<inds.size()<<'\n';summary<<"critical "<<d<<" "<<inds.size()<<"\n";}
for(auto &[d,inds]:bydim){if(d<1)continue;auto jt=bydim.find(d-1);nrows=jt==bydim.end()?0:jt->second.size();target_d=d-1;memo.clear();memo.reserve(100000);calls=0;maxcoef=0;
ofstream of("boundary_n"+to_string(dim)+"_d"+to_string(d)+".txt");of<<nrows<<" "<<inds.size()<<'\n';cerr<<"boundary "<<d<<" to "<<d-1<<" "<<nrows<<" x "<<inds.size()<<'\n';
for(int c=0;c<(int)inds.size();c++){int id=inds[c];uint32_t m=faces[id];Vec out(nrows,0);for(int v=0;v<32;v++)if(m>>v&1){int rid=idx.at(m^(1u<<v));auto const &r=reduce(rid);int s=sign_delete(m,v);for(int k=0;k<(int)r.size();k++)out[k]+=(int64_t)s*r[k];}for(int i=0;i<nrows;i++)of<<out[i]<<(i+1==nrows?'\n':' ');if(nrows==0)of<<'\n';}
cerr<<"DONE boundary "<<d<<" memo="<<memo.size()<<" calls="<<calls<<" maxcoef="<<maxcoef<<'\n';}
}
