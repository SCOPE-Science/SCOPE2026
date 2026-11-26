#include<bits/stdc++.h>
using namespace std;
int md(int x){x%=3;if(x<0)x+=3;return x;}
struct V {int x,y,z;};
int main(){
vector<V> P;for(int x=0;x<3;x++)for(int y=0;y<3;y++)for(int z=0;z<3;z++)if(x||y||z){int f=x?x:y?y:z;int inv=f==1?1:2;V v={md(x*inv),md(y*inv),md(z*inv)};if(find_if(P.begin(),P.end(),[&](V w){return w.x==v.x&&w.y==v.y&&w.z==v.z;})==P.end())P.push_back(v);}
int E[10][3];int n=0;for(int i=0;i<=3;i++)for(int j=0;j<=3-i;j++){E[n][0]=i;E[n][1]=j;E[n][2]=3-i-j;n++;}
int tab[13][10],der[13][10][3];for(int p=0;p<13;p++){int c[]={P[p].x,P[p].y,P[p].z};for(int t=0;t<10;t++){int a=1;for(int k=0;k<3;k++)for(int m=0;m<E[t][k];m++)a=md(a*c[k]);tab[p][t]=a;for(int k=0;k<3;k++){int b=E[t][k];if(!b){der[p][t][k]=0;continue;}for(int l=0;l<3;l++)for(int m=0;m<E[t][l]-(l==k);m++)b=md(b*c[l]);der[p][t][k]=b;}}}
map<pair<int,int>,int> freq; long long smoothrat=0,tanfill=0; vector<int> hits;
for(int code=1;code<59049;code++) {int coef[10],t=code;for(int i=0;i<10;i++){coef[i]=t%3;t/=3;}
bool smooth=true;int cpts=0;set<int> tangents;
for(int p=0;p<13;p++){int f=0;for(int j=0;j<10;j++)f+=coef[j]*tab[p][j];if(md(f))continue;cpts++;int gx=0,gy=0,gz=0;for(int j=0;j<10;j++){gx+=coef[j]*der[p][j][0];gy+=coef[j]*der[p][j][1];gz+=coef[j]*der[p][j][2];}gx=md(gx);gy=md(gy);gz=md(gz);if(!(gx||gy||gz)){smooth=false;break;}int fac=gx?gx:gy?gy:gz;int inv=fac==1?1:2; gx=md(gx*inv);gy=md(gy*inv);gz=md(gz*inv);for(int l=0;l<13;l++)if(P[l].x==gx&&P[l].y==gy&&P[l].z==gz){tangents.insert(l);break;}
}
if(!smooth)continue;smoothrat++;
bool fill=true;for(auto Q:P){bool touched=false;for(auto l:tangents){V A=P[l];if(md(A.x*Q.x+A.y*Q.y+A.z*Q.z)==0){touched=true;break;}}if(!touched){fill=false;break;}}if(fill){tanfill++;hits.push_back(code);freq[{cpts,(int)tangents.size()}]++;}
}
cout<<"smooth rational "<<smoothrat<<" tangent filling "<<tanfill<<"\n";for(auto [p,v]:freq)cout<<p.first<<" points; "<<p.second<<" lines: "<<v<<"\n";cout<<"example codes: ";for(int i=0;i<min(20,(int)hits.size());i++)cout<<hits[i]<<",";cout<<"\n";ofstream out("candidate_codes.txt");for(auto h:hits)out<<h<<"\n";
}
