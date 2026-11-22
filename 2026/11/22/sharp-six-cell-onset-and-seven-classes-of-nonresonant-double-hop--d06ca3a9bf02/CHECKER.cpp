#include <iostream>
#include <vector>
#include <array>
#include <map>
#include <string>
#include <algorithm>
#include <chrono>
using namespace std;
struct CT {uint64_t labeled=0, weak=0, strong=0; array<int,36> example={}; bool have=false;};
array<array<int,2>,21> rows;
int A[6][6];
int main(){int z=0;for(int i=0;i<6;i++)for(int j=i;j<6;j++)rows[z++]={i,j};
map<array<int,3>,CT> counts;
map<array<int,3>,vector<string>> candidate;
const uint64_t total=85766121ull;
for(uint64_t ix=0;ix<total;ix++){
 uint64_t idx=ix;int t=0;
 for(int i=0;i<6;i++){
  const auto &r=rows[idx%21];idx/=21;
  for(int j=0;j<6;j++)A[i][j]=0;
  ++A[i][r[0]];++A[i][r[1]];t+=A[i][i];
 }
 int R=t-2;
 int t2=0;for(int i=0;i<6;i++)for(int j=0;j<6;j++)t2+=A[i][j]*A[j][i];
 int S=(t*t-t2)/2-2*R;
 if(S<2)continue;
 long long B[6][6]={};for(int i=0;i<6;i++)B[i][i]=1;
 long long coef[7]={1};bool bad=false;
 for(int k=1;k<=6;k++){
  long long Pm[6][6]={};for(int i=0;i<6;i++)for(int h=0;h<6;h++)if(A[i][h])for(int j=0;j<6;j++)Pm[i][j]+=A[i][h]*B[h][j];
  long long tr=0;for(int i=0;i<6;i++)tr+=Pm[i][i];if(tr%k){bad=true;break;}long long ck=-tr/k;coef[k]=ck;
  for(int i=0;i<6;i++)for(int j=0;j<6;j++)B[i][j]=Pm[i][j]+(i==j?ck:0);
 }
 if(bad)abort();
 long long P=coef[4]-2*R*S;
 if(P<=0 || 1ll*S*S<4*P || coef[3]!=-(2+R)*S || coef[5]!=-(2+R)*P || coef[6]!=2*R*P)continue;
 auto &c=counts[{R,S,(int)P}];c.labeled++;
if(1ll*S*S>4*P){string s(36,'0');for(int i=0;i<6;i++)for(int j=0;j<6;j++)s[6*i+j]=char('0'+A[i][j]);candidate[{R,S,(int)P}].push_back(s);}
 bool reach[6][6]={};for(int i=0;i<6;i++)for(int j=0;j<6;j++)reach[i][j]=(i==j || A[i][j]>0);
 for(int k=0;k<6;k++)for(int i=0;i<6;i++)for(int j=0;j<6;j++)reach[i][j]|=(reach[i][k]&&reach[k][j]);
 bool strong=true,weak=true;
 for(int i=0;i<6;i++)for(int j=0;j<6;j++){if(!reach[i][j])strong=false;if(!reach[i][j]&&!reach[j][i])weak=false;}
 if(strong)c.strong++;if(weak)c.weak++;
 if(!c.have && strong){c.have=true;for(int i=0;i<6;i++)for(int j=0;j<6;j++)c.example[i*6+j]=A[i][j];}
}
cout<<"TOTAL "<<total<<" STRATA "<<counts.size()<<"\n";
vector<array<int,6>> perms;array<int,6> perm={0,1,2,3,4,5};do{perms.push_back(perm);}while(next_permutation(perm.begin(),perm.end()));
for(auto &kv:candidate){map<string,int> classes;for(const string &s:kv.second){string best(36,'9');for(const auto &p:perms){string u(36,'0');for(int i=0;i<6;i++)for(int j=0;j<6;j++)u[6*i+j]=s[6*p[i]+p[j]];if(u<best)best=u;}classes[best]++;}cout<<"CLASSES R "<<kv.first[0]<<" S "<<kv.first[1]<<" P "<<kv.first[2]<<" COUNT "<<classes.size()<<" SIZE_GROUPS ";map<int,int> h;for(const auto &x:classes)h[x.second]++;for(auto [size, cnt]:h)cout<<size<<":"<<cnt<<" ";cout<<"\n";int z=0;for(const auto &x:classes)if(z++<12)cout<<"REP "<<x.first<<" ORBIT "<<x.second<<"\n";}
for(auto [key,c]:counts){cout<<"R "<<key[0]<<" S "<<key[1]<<" P "<<key[2]<<" LABEL "<<c.labeled<<" WEAK "<<c.weak<<" STRONG "<<c.strong<<"\n";
if(c.have){for(int i=0;i<6;i++){for(int j=0;j<6;j++)cout<<c.example[i*6+j];cout<<" ";}cout<<"\n";}}
}
