#include <bits/stdc++.h>
using namespace std;
constexpr int W=4,H=4,B=16, NM=1<<B,NS=NM*B*4;
int dx[4]={0,1,0,-1},dy[4]={-1,0,1,0};
int index(int m,int p,int d){return ((m*B+p)<<2)+d;}
int step(int id){int d=id&3;int p=(id>>2)&15;int m=id>>6;int x=p%4,y=p/4;d=(d+((m>>p)&1?3:1))&3;m^=(1<<p);x=(x+dx[d]+4)%4;y=(y+dy[d]+4)%4;return index(m,x+4*y,d);}
struct Sym{ int perm[16],dp[4],reflection;};
vector<Sym> syms(){ vector<Sym> a;
 for(int flip=0;flip<2;flip++)for(int rot=0;rot<4;rot++)for(int tx=0;tx<4;tx++)for(int ty=0;ty<4;ty++){
 Sym s; s.reflection=flip;
 auto tr=[&](int x,int y){if(flip)x=-x;for(int i=0;i<rot;i++){int xx=-y; y=x;x=xx;}return pair<int,int>{(x+tx+20)%4,(y+ty+20)%4};};
 for(int p=0;p<16;p++){auto [x,y]=tr(p%4,p/4);s.perm[p]=x+4*y;}
 for(int d=0;d<4;d++){auto [x0,y0]=tr(0,0);auto [x1,y1]=tr((dx[d]+4)%4,(dy[d]+4)%4);int ddx=(x1-x0+4)%4, ddy=(y1-y0+4)%4; for(int j=0;j<4;j++)if((dx[j]+4)%4==ddx && (dy[j]+4)%4==ddy){s.dp[d]=j;break;}}
 a.push_back(s);
 }return a;
}
int transform(int id,const Sym &s){int d=id&3,p=(id>>2)&15,m=id>>6;int out=s.reflection?65535:0;
 for(int i=0;i<16;i++)if((m>>i)&1)out^=1<<s.perm[i];
 return index(out,s.perm[p],s.dp[d]);}
int main(){auto sy=syms();cerr<<"sym size "<<sy.size()<<"\n";
 for(int k=0;k<NS;k+=157){int x=step(k);for(auto &s:sy)if(step(transform(k,s))!=transform(x,s)){cerr<<"commutation fail "<<k<<"\n";exit(2);}}
 for (int k=0;k<NS;k++)for(int g: {1,4,16,64})if(step(transform(k,sy[g]))!=transform(step(k),sy[g])){cerr<<"generator commutation failure "<<k<<" "<<g<<"\n";exit(6);}
 vector<int> which(NS,-1), rep, period;map<int,int> cyc, states;
 for(int id=0;id<NS;id++)if(which[id]<0){int cid=rep.size(), curr=id,len=0;
 do{if(which[curr]>=0){cerr<<"not permutation "<<id<<"\n";exit(4);}which[curr]=cid;curr=step(curr);len++;}while(curr!=id);
 rep.push_back(id);period.push_back(len);cyc[len]++;states[len]+=len;}
 vector<char> seen(rep.size());map<int,int> typ;
 for(int j=0;j<(int)rep.size();j++)if(!seen[j]){
 int num=0; for(auto &s:sy){int k=which[transform(rep[j],s)]; if(!seen[k]){seen[k]=1;num++;}}
 typ[period[j]]++;
 }
 cout<<"states="<<NS<<" cycles="<<rep.size()<<"\n";
 cout<<"period cycles states symmetry_types\n";
 long totalc=0,totals=0,totalt=0;
 for(auto &[p,c]:cyc){cout<<p<<" "<<c<<" "<<states[p]<<" "<<typ[p]<<"\n";totalc+=c;totals+=states[p];totalt+=typ[p];}
 cout<<"total "<<totalc<<" "<<totals<<" "<<totalt<<"\n";
 // all-white all dir orientations
 for(int d=0;d<4;d++)cout<<"white dir "<<d<<" period "<<period[which[index(0,0,d)]]<<"\n";
}
