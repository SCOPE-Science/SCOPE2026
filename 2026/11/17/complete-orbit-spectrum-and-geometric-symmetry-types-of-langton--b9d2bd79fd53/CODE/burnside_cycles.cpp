#include <cstdint>
#include <vector>
#include <array>
#include <map>
#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;
static constexpr int SIDE=4,CELLS=16,STATES=4194304;
static constexpr int movex[4]={0,1,0,-1}, movey[4]={-1,0,1,0};
static inline unsigned encode(unsigned board,int x,int y,int dir){return (board<<6)|((4*y+x)<<2)|dir;}
static unsigned update(unsigned s){int d=s&3,pos=(s>>2)&15;unsigned board=s>>6;int x=pos&3,y=pos>>2;int old=(board>>pos)&1;int nd=(d+(old?3:1))%4;board^=(1u<<pos);x=(x+movex[nd]+4)&3;y=(y+movey[nd]+4)&3;return encode(board,x,y,nd);}
static unsigned inverse_update(unsigned s){int nd=s&3,pos=(s>>2)&15;unsigned board=s>>6;int x=pos&3,y=pos>>2;int px=(x-movex[nd]+4)&3,py=(y-movey[nd]+4)&3;int q=4*py+px;int old=1-((board>>q)&1);int pd=(nd+(old?1:3))&3;board^=1u<<q;return encode(board,px,py,pd);}
struct Isometry {int a,b,c,d,tx,ty,det;};
static unsigned iso_action(unsigned s,Isometry g){int dir=s&3,pos=(s>>2)&15;unsigned m=s>>6;int x=pos&3,y=pos>>2;auto newpos=[&](int x0,int y0){return pair<int,int>{(g.a*x0+g.b*y0+g.tx+16)&3,(g.c*x0+g.d*y0+g.ty+16)&3};};auto [nx,ny]=newpos(x,y);
 unsigned newmask=g.det<0?0xffffu:0;
 for(int i=0;i<16;++i)if((m>>i)&1){auto [xx,yy]=newpos(i&3,i>>2);newmask^=1u<<(4*yy+xx);}
 int ddx=g.a*movex[dir]+g.b*movey[dir],ddy=g.c*movex[dir]+g.d*movey[dir],nd=-1;
 for(int j=0;j<4;j++)if(ddx==movex[j]&&ddy==movey[j])nd=j;
 if(nd<0){cerr<<"invalid matrix\n";exit(11);}return encode(newmask,nx,ny,nd);
}
int main(){vector<uint32_t> f(STATES);vector<uint8_t> indeg(STATES,0);
 for(unsigned s=0;s<STATES;s++){unsigned t=update(s);f[s]=t;indeg[t]++;if(inverse_update(t)!=s){cerr<<"inverse fail "<<s<<"\n";return 2;}}
 for(unsigned i=0;i<STATES;i++)if(indeg[i]!=1){cerr<<"not permutation "<<i<<":"<<int(indeg[i])<<"\n";return 3;}
 vector<int32_t> orbit(STATES,-1); vector<uint32_t> rep;vector<uint16_t> lens;
 map<int,uint64_t> counts,states;
 for(uint32_t s=0;s<STATES;s++)if(orbit[s]==-1){uint32_t v=s;uint32_t len=0;int id=rep.size();do{if(orbit[v]!=-1){cerr<<"collision\n";return 4;} orbit[v]=id;len++;v=f[v];}while(v!=s); if(len>65535){cerr<<"long cycle\n";return 5;}rep.push_back(s);lens.push_back(len);counts[len]++;states[len]+=len;}
 vector<Isometry> group;
 // D4: signed permutation matrices, four diagonal and four anti-diagonal.
 for(int reflect=0;reflect<=1;reflect++)for(int swap=0;swap<=1;swap++)for(int sign=0;sign<2;sign++)for(int tx=0;tx<4;tx++)for(int ty=0;ty<4;ty++){
  int eps=sign?-1:1;int a=swap?0:eps,b=swap?eps:0,c=swap?(reflect?-eps:eps):0,d=swap?0:(reflect?-eps:eps);
  int det=a*d-b*c;group.push_back({a,b,c,d,tx,ty,det});
 }
 if(group.size()!=128){cerr<<"wrong group\n";return 8;}
 map<int,uint64_t> fixed;
 for(const auto& g:group){for(size_t j=0;j<rep.size();j++){
  unsigned t=iso_action(rep[j],g);if(orbit[t]==int(j))fixed[lens[j]]++;
 }}
 cout<<"states="<<STATES<<" cycles="<<rep.size()<<" all_indegree_one=1 inverse_all=1 group="<<group.size()<<"\n";
 cout<<"period cycles states burnside_fixed_sum symmetry_types\n";
 uint64_t nc=0,ns=0,nt=0;
 for(const auto &[p,c]:counts){if(fixed[p]%128){cerr<<"Burnside mismatch "<<p<<":"<<fixed[p]<<"\n";return 9;}uint64_t typ=fixed[p]/128;cout<<p<<" "<<c<<" "<<states[p]<<" "<<fixed[p]<<" "<<typ<<"\n";nc+=c;ns+=states[p];nt+=typ;}
 cout<<"total "<<nc<<" "<<ns<<" "<<nt<<"\n";
 cout<<"all_white_period="<<lens[orbit[encode(0,0,0,0)]]<<"\n";
 return 0;
}
