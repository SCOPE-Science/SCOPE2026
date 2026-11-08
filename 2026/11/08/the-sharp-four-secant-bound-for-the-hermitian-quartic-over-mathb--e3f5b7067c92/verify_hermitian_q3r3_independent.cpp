// Independent exhaustive line-first census over F_3[t]/(t^6+t^5+2).
// Unlike the point-pair verifier, this scans all 532171 lines directly.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
constexpr int Q=729,N=Q*Q+Q+1;
using F=uint16_t;
static F S[Q][Q], M[Q][Q], Neg[Q], Inv[Q], D4[Q];
struct Triple{F x,y,z;};
int prod(int a,int b){int aa[6],bb[6],p[11]={};for(int i=0;i<6;i++){aa[i]=a%3;bb[i]=b%3;a/=3;b/=3;}
 for(int i=0;i<6;i++)for(int j=0;j<6;j++)p[i+j]=(p[i+j]+aa[i]*bb[j])%3;
 for(int i=10;i>=6;i--){int v=p[i];p[i]=0;p[i-6]=(p[i-6]+v)%3;p[i-1]=(p[i-1]+2*v)%3;}
 int w=0,m=1;for(int i=0;i<6;i++){w+=p[i]*m;m*=3;}return w;}
void init(){
 for(int a=0;a<Q;a++)for(int b=0;b<Q;b++){int i=a,j=b,z=0,unit=1;for(int k=0;k<6;k++){z+=((i%3+j%3)%3)*unit;unit*=3;i/=3;j/=3;}S[a][b]=z;M[a][b]=prod(a,b);}
 for(int a=0;a<Q;a++)for(int b=0;b<Q;b++)if(S[a][b]==0){Neg[a]=b;break;}
 for(int a=1;a<Q;a++)for(int b=1;b<Q;b++)if(M[a][b]==1){Inv[a]=b;break;}
 for(int a=1;a<Q;a++)assert(M[a][Inv[a]]==1);
 for(int a=0;a<Q;a++)D4[a]=M[M[a][a]][M[a][a]];
 // 3^6-Frobenius identity checks independently of defining irreducibility test.
 for(int a=0;a<Q;a++){int b=a;for(int k=0;k<6;k++)b=M[M[b][b]][b];assert(b==a);}
}
int index(const Triple &a){if(a.z){int t=Inv[a.z];return M[a.x][t]*Q+M[a.y][t];}
 if(a.y) return Q*Q+M[a.x][Inv[a.y]];
 assert(a.x);return N-1;}
Triple point(int i){if(i<Q*Q)return {(F)(i/Q),(F)(i%Q),1};if(i<N-1)return {(F)(i-Q*Q),1,0};return {1,0,0};}
Triple line(int i){return point(i);}
int main(){init();vector<Triple> curve;vector<unsigned char> yes(N,0);curve.reserve(900);
 for(int i=0;i<N;i++){auto p=point(i);if(S[S[D4[p.x]][D4[p.y]]][D4[p.z]]==0){curve.push_back(p);yes[i]=1;}}
 assert(curve.size()==892);
 vector<uint16_t> coverage(N,0);long long secant_lines=0;map<int,int> characters;
 for(int i=0;i<N;i++){
   auto l=line(i);int n=0;for(auto p:curve){int v=S[S[M[l.x][p.x]][M[l.y][p.y]]][M[l.z][p.z]];if(!v)n++;}
   characters[n]++;if(n!=4)continue;secant_lines++;
   if(l.z){for(int t=0;t<Q;t++){Triple p={1,(F)t,(F)S[Neg[l.x]][Neg[M[l.y][t]]]};coverage[index(p)]++;}Triple p={0,1,Neg[l.y]};coverage[index(p)]++;}
   else if(l.y){for(int t=0;t<Q;t++){Triple p={(F)t,(F)M[Neg[l.x]][t],1};coverage[index(p)]++;}Triple p={1,Neg[l.x],0};coverage[index(p)]++;}
   else {for(int t=0;t<Q;t++){Triple p={0,(F)t,1};coverage[index(p)]++;}coverage[index({0,1,0})]++;}
 }
 long long sum=0;map<int,int> ext,on;int minval=9999;int maxval=0, minpoints=0, maxpoints=0;
 for(int id=0;id<N;id++){int k=coverage[id];sum+=k;if(yes[id])on[k]++;else{ext[k]++;minval=min(minval,k);maxval=max(maxval,k);}}
 for(int id=0;id<N;id++)if(!yes[id]){minpoints+=(coverage[id]==minval);maxpoints+=(coverage[id]==maxval);}
 assert(sum==secant_lines*730);assert(secant_lines==39879);assert(minval==25);assert(maxval==222);
 cout<<"field_poly=t^6+t^5+2; rational_curve_points="<<curve.size()<<"\n";
 cout<<"line_characters:";for(auto [k,v]:characters)cout<<" "<<k<<":"<<v;cout<<"\n";
 cout<<"four_secants="<<secant_lines<<" external_min="<<minval<<" multiplicity="<<minpoints<<" external_max="<<maxval<<" multiplicity="<<maxpoints<<"\n";
 cout<<"external_distribution:";for(auto [k,v]:ext)cout<<" "<<k<<":"<<v;cout<<"\n";
 cout<<"curve_distribution:";for(auto [k,v]:on)cout<<" "<<k<<":"<<v;cout<<"\n";
 // The 63 extremal off-curve points should be precisely PG(2,F_9)\H(F_9).
 int f9=0, f9ext=0;
 for(int i=0;i<N;i++){auto p=point(i);bool sub=true;for(int a:{(int)p.x,(int)p.y,(int)p.z}){int t=a;for(int j=0;j<2;j++)t=M[M[t][t]][t];if(t!=a)sub=false;}
 if(sub){f9++;if(!yes[i]){f9ext++;assert(coverage[i]==222);}}if(!yes[i] && coverage[i]==222)assert(sub);
 }
 assert(f9==91&&f9ext==63);
 cout<<"F9_subplane_points="<<f9<<" offcurve_extremal="<<f9ext<<"\n";
 const map<int,int> expected_external={{25,1512},{48,36288},{49,60480},{50,36288},{51,12096},{52,36288},{53,18144},{54,67032},{55,12096},{56,72576},{57,36288},{58,48384},{59,54432},{61,12096},{62,9072},{65,18144},{222,63}};
 assert(ext==expected_external);
 assert((on==map<int,int>{{175,864},{297,28}}));
 assert((characters==map<int,int>{{0,158760},{1,175420},{2,158112},{4,39879}}));
 cout<<"HERMITIAN_Q3_R3_INDEPENDENT_PASS\n";
}
