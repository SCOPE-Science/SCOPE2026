#include <bits/stdc++.h>
using namespace std;
// Basis (E11,E12,E13,E22,E23,E33), GF(2).
int st[6]={0,0,0,1,1,2}, en[6]={0,1,2,1,2,2};
uint8_t mul[64][64];
inline int parity(int a){return __builtin_parity((unsigned)a);}
int main(){
 for(int x=0;x<64;x++) for(int y=0;y<64;y++){
  int z=0;
  for(int i=0;i<6;i++)if((x>>i)&1)for(int j=0;j<6;j++)if((y>>j)&1){
   if(en[i]!=st[j]) continue;
   for(int k=0;k<6;k++)if(st[k]==st[i]&&en[k]==en[j]) {z^=(1<<k);break;}
  }mul[x][y]=(uint8_t)z;
 }
 uint64_t total=0, rank2maps=0, closed=0, active=0, allplanes=0;
 map<uint64_t,int> hist;
 map<int,uint64_t> image_tally;
 int maxfiber=0,minfiber=INT_MAX;
 vector<tuple<int,int,int>> active_planes;
 for(int u=1;u<64;u++)for(int v=u+1;v<64;v++){
   int w=u^v; if(v>w)continue; // u and v are first two sorted nonzero elements of the plane
   ++allplanes;
   int cnt=0;
   bool subalg=true;
   for(int x:{u,v,w})for(int y:{u,v,w})if(mul[x][y]!=0&&mul[x][y]!=u&&mul[x][y]!=v&&mul[x][y]!=w)subalg=false;
   if(subalg)++closed;
   for(int a=1;a<64;a++)for(int b=1;b<64;b++) if(a!=b){
     ++rank2maps;
     uint8_t px[6];
     for(int i=0;i<6;i++)px[i]=(((a>>i)&1)?u:0)^(((b>>i)&1)?v:0);
     bool ok=true;
     for(int i=0;i<6 && ok;i++) for(int j=0;j<6;j++){
       int z=mul[px[i]][1<<j]^mul[1<<i][px[j]];
       int rhs=(parity(z&a)?u:0)^(parity(z&b)?v:0);
       if(mul[px[i]][px[j]]!=rhs){ok=false;break;}
     }
     if(ok) ++cnt;
   }
   if(cnt>0){
    ++active; total+=cnt;maxfiber=max(maxfiber,cnt);minfiber=min(minfiber,cnt);
    active_planes.emplace_back(u,v,cnt);
    image_tally[subalg]+=cnt;
   }
   hist[cnt]++;
 }
 cout<<"planes "<<allplanes<<" closed "<<closed<<" candidate_rank_two_maps "<<rank2maps<<"\n";
 cout<<"nonzero_fiber_planes "<<active<<" total_rank2_RB "<<total<<" minfiber "<<minfiber<<" maxfiber "<<maxfiber<<"\n";
 cout<<"FIBER_HIST";for(auto [v,n]:hist)cout<<" "<<v<<":"<<n;cout<<"\n";
 cout<<"IMAGE_TALLY";for(auto [k,n]:image_tally)cout<<" "<<k<<":"<<n;cout<<"\n";
 assert(allplanes==651 && closed==100 && rank2maps==2542806);
 assert(active==58 && total==652 && hist[0]==593 && hist[3]==24 && hist[4]==8 && hist[5]==16 && hist[6]==8 && hist[210]==2);
 for(auto [u,v,n]:active_planes)cout<<"ACTIVE "<<u<<" "<<v<<" "<<n<<"\n";
 cout<<"VERIFY_OK\n";
}
