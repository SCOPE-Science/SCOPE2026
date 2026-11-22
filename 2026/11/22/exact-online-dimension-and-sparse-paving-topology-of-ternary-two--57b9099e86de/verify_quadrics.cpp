// Independent finite-field quadratic-form and exhaustive adaptive-dimension verifier.
#include <bits/stdc++.h>
using namespace std;
int mod3(int x){x%=3;return x<0?x+3:x;}
int det3(const array<array<int,3>,3>&a){return mod3(a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]));}
int main(){
 vector<array<int,3>> pts;
 for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int z=0;z<3;z++){
  if(!(x||y||z))continue;
  int t=x?x:(y?y:z),scale=t==1?1:2;
  array<int,3>v={mod3(x*scale),mod3(y*scale),mod3(z*scale)};
  if(find(pts.begin(),pts.end(),v)==pts.end())pts.push_back(v);
 }
 sort(pts.begin(),pts.end());assert(pts.size()==13);
 vector<int> conics;
 for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++)for(int d=0;d<3;d++)for(int e=0;e<3;e++)for(int f=0;f<3;f++){
  array<int,6>v={a,b,c,d,e,f};int initial=0;
  for(int t:v){if(t){initial=t;break;}}
  if(initial!=1)continue;
  array<array<int,3>,3>h={array<int,3>{2*a,d,e},array<int,3>{d,2*b,f},array<int,3>{e,f,2*c}};
  if(det3(h)==0)continue;
  int m=0;
  for(int i=0;i<13;i++){
   auto [x,y,z]=pts[i];
   if(mod3(a*x*x+b*y*y+c*z*z+d*x*y+e*x*z+f*y*z)==0)m|=(1<<i);
  }
  assert(__builtin_popcount((unsigned)m)==4);
  conics.push_back(m);
 }
 sort(conics.begin(),conics.end());conics.erase(unique(conics.begin(),conics.end()),conics.end());assert(conics.size()==234);
 set<int> un;
 for(size_t i=0;i<conics.size();i++)for(size_t j=i+1;j<conics.size();j++)un.insert(conics[i]|conics[j]);
 vector<int> concepts(un.begin(),un.end());assert(concepts.size()==4641);
 array<int,14> faces{};
 vector<int> bad7,good7;
 for(int s=0;s<(1<<13);s++){
  int k=__builtin_popcount((unsigned)s);
  vector<uint8_t>seen(1<<13,0);int cnt=0;
  for(int u:concepts){int t=u&s;if(!seen[t]){seen[t]=1;cnt++;}}
  if(cnt==(1<<k)){faces[k]++;if(k==7)good7.push_back(s);}else if(k==7)bad7.push_back(s);
 }
 array<int,14>expected={1,13,78,286,715,1287,1716,1638,0,0,0,0,0,0};assert(faces==expected);
 vector<int> lines;
 for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++){
  array<int,3>v={a,b,c};int initial=0;for(int t:v)if(t){initial=t;break;}if(initial!=1)continue;
  int mask=0;for(int i=0;i<13;i++){auto [x,y,z]=pts[i];if(mod3(a*x+b*y+c*z)==0)mask|=1<<i;}lines.push_back(mask);
 }
 assert(lines.size()==13);
 set<int>two_lines;for(int i=0;i<13;i++)for(int j=i+1;j<13;j++)two_lines.insert(lines[i]|lines[j]);
 assert(two_lines.size()==78 && set<int>(bad7.begin(),bad7.end())==two_lines);
 int p3[14];p3[0]=1;for(int i=1;i<=13;i++)p3[i]=3*p3[i-1];int T=p3[13];
 vector<int>counts(T,0);
 for(int u:concepts){int state=0;for(int i=0;i<13;i++)state+=p3[i]*((u>>i&1)?2:1);counts[state]++;}
 for(int i=0;i<13;i++)for(int s=0;s<T;s++)if((s/p3[i])%3==0)counts[s]=counts[s+p3[i]]+counts[s+2*p3[i]];
 assert(counts[0]==(int)concepts.size());
 vector<uint8_t>dp(T,0);
 for(int s=T-1;s>=0;s--){if(counts[s]<2)continue;int best=0;
  for(int i=0;i<13;i++)if((s/p3[i])%3==0){int a=s+p3[i],b=s+2*p3[i];
   if(counts[a]&&counts[b])best=max(best,1+min((int)dp[a],(int)dp[b]));
  }dp[s]=best;
 }
 assert(dp[0]==8);
 long long chi=-1;for(int k=1;k<=7;k++)chi += ((k-1)%2 ? -1:1)*faces[k];
 // reduced Euler characteristic: -1 + f_0 - f_1 + ... + f_6 = 714.
 assert(chi==714);
 cout<<"points=13 conics="<<conics.size()<<" distinct_unions="<<concepts.size()<<"\n";
 cout<<"faces:";for(int k=0;k<=7;k++)cout<<' '<<faces[k];cout<<"\n";
 cout<<"forbidden_sevens="<<bad7.size()<<" (all two-line unions)\n";
 cout<<"Littlestone_dimension="<<(int)dp[0]<<"\n";
 cout<<"reduced_euler_characteristic="<<chi<<"\n";
}
