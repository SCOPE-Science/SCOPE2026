#include <bits/stdc++.h>
using namespace std;
struct Exp{int e[4];};
vector<Exp> exps; int loc[4][4][4][4], support[20],derivSupport[20][4];
uint32_t sub[12][20]; uint32_t tab[12][2][1024];
int tt[4][4][4]; vector<array<int,3>> e3;
int degmon[4][20];
static inline int bitrank(vector<int> a){int r=0;for(int bit=3;bit>=0;--bit){int k=r;while(k<(int)a.size()&&!(a[k]&(1<<bit)))k++;if(k==(int)a.size())continue; swap(a[k],a[r]);for(int j=0;j<(int)a.size();j++)if(j!=r && (a[j]&(1<<bit)))a[j]^=a[r];r++;}return r;}
uint32_t transform(uint32_t f,int g){return tab[g][0][f&1023]^tab[g][1][f>>10];}
int R[16][16][10][20]; // not used
int basis[16][16][2]; uint16_t pullback[16][16][20];
int eval(uint32_t f,int point){int v=0;while(f){int j=__builtin_ctz(f);f&=f-1; if((point&support[j])==support[j])v^=1;}return v;}
int grad(uint32_t f,int point){int g=0;for(int axis=0;axis<4;axis++){int v=0;uint32_t r=f;while(r){int j=__builtin_ctz(r);r&=r-1;if(exps[j].e[axis]&1) {int sp=derivSupport[j][axis];if((point&sp)==sp)v^=1;}}g|=v<<axis;}return g;}
int rational_eck(uint32_t f,int &N){int E=0;N=0;for(int p=1;p<16;p++){if(eval(f,p))continue;N++;int g=grad(f,p);if(!g)continue;uint16_t poly=0;uint32_t r=f;while(r){int j=__builtin_ctz(r);r&=r-1;poly^=pullback[p][g][j];}
 // e3 ordering map s,t,u. Verify no s^3 (F(p)=0), s^2t/s^2u (grad tangent=0)
 int bad=0,a=0,b=0,c=0,d=0;
 for(int j=0;j<(int)e3.size();j++) if(poly>>j&1){auto z=e3[j];if(z[0]>0)bad=1;else if(z[1]==3)a=1;else if(z[1]==2)b=1;else if(z[1]==1)c=1;else d=1;}
 if(!bad && ((a*d)^(b*c)))E++;
}return E;}
int main(){memset(loc,-1,sizeof(loc)); for(int a=0;a<=3;a++) for(int b=0;b<=3-a;b++)for(int c=0;c<=3-a-b;c++){int d=3-a-b-c; int k=exps.size(); exps.push_back({a,b,c,d});loc[a][b][c][d]=k;}
for(int i=0;i<20;i++){int sp=0;for(int v=0;v<4;v++)if(exps[i].e[v])sp|=1<<v;support[i]=sp;for(int v=0;v<4;v++){int mask=0;for(int h=0;h<4;h++)if(exps[i].e[h]-(v==h)>0)mask|=1<<h;derivSupport[i][v]=mask;}}
int numg=0;for(int i=0;i<4;i++)for(int j=0;j<4;j++)if(i!=j){for(int k=0;k<20;k++){auto e=exps[k];uint32_t out=0;for(int t=0;t<=e.e[i];t++)if((t&e.e[i])==t){auto z=e;z.e[i]-=t;z.e[j]+=t;out^=1u<<loc[z.e[0]][z.e[1]][z.e[2]][z.e[3]];}sub[numg][k]=out;}for(int block=0;block<2;block++)for(int mask=0;mask<1024;mask++){uint32_t val=0;for(int bit=0;bit<10;bit++)if(mask>>bit&1)val^=sub[numg][block*10+bit];tab[numg][block][mask]=val;}numg++;}
// ternary monomials all degree 3
for(int a=0;a<=3;a++)for(int b=0;b<=3-a;b++){int c=3-a-b; tt[a][b][c]=e3.size();e3.push_back({a,b,c});}
// calculate pullbacks via polynomial multiplication using 3variable degree-index arrays
for(int p=1;p<16;p++)for(int g=1;g<16;g++)if(!(__builtin_parity((unsigned)(p&g)))){
 int u=0,v=0; for(int q=1;q<16;q++)if(!__builtin_parity((unsigned)(q&g)) && bitrank({p,q})==2){u=q;break;}
 for(int q=1;q<16;q++)if(!__builtin_parity((unsigned)(q&g)) && bitrank({p,u,q})==3){v=q;break;}
 if(!u||!v)continue;basis[p][g][0]=u;basis[p][g][1]=v;
 for(int k=0;k<20;k++){
  int coeff[4][4][4]={};coeff[0][0][0]=1;
  for(int axis=0;axis<4;axis++)for(int rep=0;rep<exps[k].e[axis];rep++){
   int next[4][4][4]={};for(int a=0;a<4;a++)for(int b=0;b<4-a;b++)for(int c=0;c<4-a-b;c++)if(coeff[a][b][c]){
    if(p>>axis&1 && a+1<=3)next[a+1][b][c]^=1;
    if(u>>axis&1 && b+1<=3)next[a][b+1][c]^=1;
    if(v>>axis&1 && c+1<=3)next[a][b][c+1]^=1;
   }memcpy(coeff,next,sizeof coeff);
  }
  uint16_t out=0;for(int j=0;j<10;j++){auto e=e3[j];if(coeff[e[0]][e[1]][e[2]])out|=1<<j;}pullback[p][g][k]=out;
 }
}
vector<uint8_t> visited(1u<<20,0); vector<uint32_t> q; q.reserve(20000);
map<pair<int,int>,long long> tots;int orbitIndex=0;
for(uint32_t f=1; f<(1u<<20); f++) if(!visited[f]){
 q.clear();q.push_back(f);visited[f]=1;
 for(size_t head=0;head<q.size();head++){
  uint32_t v=q[head];for(int k=0;k<12;k++){uint32_t w=transform(v,k);if(!visited[w]){visited[w]=1;q.push_back(w);}}
 }
 int N=0,E=rational_eck(f,N);
 orbitIndex++;printf("%d %u %zu %d %d\n",orbitIndex,f,q.size(),N,E);
 tots[{N,E}]+=q.size();
}
fprintf(stderr,"total orbits %d\n",orbitIndex);
}
