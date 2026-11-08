#include <bits/stdc++.h>
using namespace std;
constexpr int Q=729, N=Q*Q+Q+1;
static uint16_t addT[Q][Q], subT[Q][Q], mulT[Q][Q], invT[Q], pow4[Q];
struct P {int x,y,z;};
int enc(int a,int b,int c){
    if(a) {int ai=invT[a]; return mulT[b][ai]*Q+mulT[c][ai];}
    if(b) return Q*Q+mulT[c][invT[b]];
    assert(c);return N-1;
}
P dec(int id){ if(id<Q*Q)return {1,id/Q,id%Q};if(id<N-1)return {0,1,id-Q*Q};return {0,0,1};}
int fieldmult(int a,int b){int A[11]={}, aa[6],bb[6];for(int i=0;i<6;i++){aa[i]=a%3;a/=3;bb[i]=b%3;b/=3;}
for(int i=0;i<6;i++)for(int j=0;j<6;j++)A[i+j]=(A[i+j]+aa[i]*bb[j])%3;
for(int k=10;k>=6;k--){int v=A[k];A[k]=0;A[k-6]=(A[k-6]+v)%3;A[k-5]=(A[k-5]+2*v)%3;}
int z=0,p=1;for(int i=0;i<6;i++){z+=A[i]*p;p*=3;}return z;}
void init(){
  int dig[Q][6]{};for(int a=0;a<Q;a++){int x=a;for(int i=0;i<6;i++){dig[a][i]=x%3;x/=3;}}
  for(int a=0;a<Q;a++)for(int b=0;b<Q;b++){int ac=0,su=0,base=1;for(int j=0;j<6;j++){ac+=((dig[a][j]+dig[b][j])%3)*base;su+=((dig[a][j]+3-dig[b][j])%3)*base;base*=3;}addT[a][b]=ac;subT[a][b]=su;mulT[a][b]=fieldmult(a,b);}
  for(int a=1;a<Q;a++){for(int b=1;b<Q;b++)if(mulT[a][b]==1){invT[a]=b;break;}assert(invT[a]);}
  for(int a=0;a<Q;a++)pow4[a]=mulT[mulT[a][a]][mulT[a][a]];
  // verify tables via Frobenius field property and t^6+t+2 polynomial relation
  for(int a=1;a<Q;a++){assert(mulT[a][invT[a]]==1);int x=a;for(int i=0;i<6;i++)x=mulT[mulT[x][x]][x];assert(x==a);}
}
int main(){init();vector<P> pts;pts.reserve(1000);vector<unsigned char> oncurve(N);
 for(int id=0;id<N;id++){P p=dec(id); if(addT[addT[pow4[p.x]][pow4[p.y]]][pow4[p.z]]==0){pts.push_back(p);oncurve[id]=1;}}
 cout<<"field=3^6 polynomial=t^6+t+2 points="<<pts.size()<<" plane="<<N<<"\n";
 assert(pts.size()==892);
 vector<uint16_t> pairfreq(N,0);
 for(size_t i=0;i<pts.size();i++)for(size_t j=i+1;j<pts.size();j++){
 auto a=pts[i],b=pts[j];
 int A=subT[mulT[a.y][b.z]][mulT[a.z][b.y]];
 int B=subT[mulT[a.z][b.x]][mulT[a.x][b.z]];
 int C=subT[mulT[a.x][b.y]][mulT[a.y][b.x]];
 int id=enc(A,B,C);pairfreq[id]++;
 }
 map<int,int> linefreq;for(auto n:pairfreq)linefreq[n]++;cout<<"pairfreq";for(auto [n,v]:linefreq)cout<<" "<<n<<":"<<v;cout<<"\n";
 // Every 4-secant contains 6 unordered pairs of its 4 rational points.
 int full=0;vector<uint16_t> secants(N,0);for(int id=0;id<N;id++)if(pairfreq[id]==6){full++;P L=dec(id);int A=L.x,B=L.y,C=L.z;
 if(B){int iv=invT[B];for(int z=0;z<Q;z++){int y=mulT[iv][subT[0][addT[A][mulT[C][z]]]];secants[y*Q+z]++;}int inf;if(C){inf=Q*Q+mulT[B][subT[0][invT[C]]];}else inf=N-1;secants[inf]++;}
 else if(C){int z=mulT[invT[C]][subT[0][A]];for(int y=0;y<Q;y++)secants[y*Q+z]++;secants[Q*Q]++;}
 else{for(int n=Q*Q;n<N;n++)secants[n]++;}
 }
 assert(full==linefreq[6]);map<int,int> extfreq,curvefreq;
 long long incidences=0;int minout=Q+1,maxout=-1, uncovered=0;
 for(int id=0;id<N;id++){incidences+=secants[id];if(oncurve[id])curvefreq[secants[id]]++;else{extfreq[secants[id]]++;minout=min(minout,(int)secants[id]);maxout=max(maxout,(int)secants[id]);if(secants[id]==0)uncovered++;}}
 assert(incidences==1LL*full*(Q+1));
 cout<<"four_secants="<<full<<" incidences="<<incidences<<" min_external="<<minout<<" max_external="<<maxout<<" uncovered="<<uncovered<<"\n";
 cout<<"external_spectrum";for(auto [n,v]:extfreq)cout<<" "<<n<<":"<<v;cout<<"\n";
 const map<int,int> expected_external={{25,1512},{48,36288},{49,60480},{50,36288},{51,12096},{52,36288},{53,18144},{54,67032},{55,12096},{56,72576},{57,36288},{58,48384},{59,54432},{61,12096},{62,9072},{65,18144},{222,63}};
 assert(extfreq==expected_external);
 assert((curvefreq==map<int,int>{{175,864},{297,28}}));
 assert((linefreq==map<int,int>{{0,334180},{1,158112},{6,39879}}));
 cout<<"oncurve_spectrum";for(auto [n,v]:curvefreq)cout<<" "<<n<<":"<<v;cout<<"\n";
 // Check the rational-point count on every four-secant independently of pair frequency.
 int checked=0;for(int id=0;id<N;id++)if(pairfreq[id]==6){P L=dec(id);int n=0;for(P p:pts){int v=addT[addT[mulT[L.x][p.x]][mulT[L.y][p.y]]][mulT[L.z][p.z]];if(v==0)n++;}assert(n==4);checked++;}
 cout<<"verified_four_secants="<<checked<<"\n";
 cout<<"HERMITIAN_Q3_R3_EXHAUSTIVE_PASS\n";
}
