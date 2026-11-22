#include <bits/stdc++.h>
using namespace std;
struct A {unsigned char t[2][8]; int rt;};
vector<A> v(729);
int shortest(int id1,int id2,string *w=nullptr){
 auto &x=v[id1], &y=v[id2]; int d[64]; fill(d,d+64,-1);int par[64],chr[64];int qu[64],head=0,tail=0;int start=7*8+7; d[start]=0;qu[tail++]=start;
 while(head<tail){int z=qu[head++],p=z/8,q=z%8;if(__builtin_popcount((unsigned)p)==1 && __builtin_popcount((unsigned)q)==1){if(w){string s;int j=z;while(d[j]){s.push_back(chr[j]?'b':'a');j=par[j];}reverse(s.begin(),s.end());*w=s;}return d[z];}
 for(int c=0;c<2;c++){int nz=x.t[c][p]*8+y.t[c][q];if(d[nz]<0){d[nz]=d[z]+1;par[nz]=z;chr[nz]=c;qu[tail++]=nz;}}}
 return -1;
}
int main(){
 for(int id=0;id<729;id++){int ds[2][3];int z=id;for(int c=0;c<2;c++)for(int s=0;s<3;s++){ds[c][s]=z%3;z/=3;}for(int c=0;c<2;c++)for(int m=0;m<8;m++){int out=0;for(int s=0;s<3;s++)if(m&(1<<s))out|=1<<ds[c][s];v[id].t[c][m]=out;}v[id].rt=shortest(id,id);}
 map<int,long long> hist;map<pair<int,int>,map<int,long long>> byrt;int maxrt=0,max1=-1,max2=-1;long long sync=0;map<int,long long> syhist;
 for(int a=0;a<729;a++){syhist[v[a].rt]++;if(v[a].rt<0)continue;for(int b=0;b<729;b++){if(v[b].rt<0)continue;int r=shortest(a,b);if(r<0){cerr<<"FAIL cannot synchronize!";return 1;}hist[r]++;byrt[{v[a].rt,v[b].rt}][r]++;sync++;if(r>maxrt){maxrt=r;max1=a;max2=b;}}}
 cout<<"single hist";for(auto [k,n]:syhist)cout<<" "<<k<<":"<<n;cout<<"\nsync pairs "<<sync<<"\n";cout<<"joint hist";for(auto [k,n]:hist)cout<<" "<<k<<":"<<n;cout<<"\nmax "<<maxrt<<" example "<<max1<<" "<<max2<<"\n";
 for(auto &[p,h]:byrt){cout<<"single("<<p.first<<","<<p.second<<"):";for(auto [k,n]:h)cout<<" "<<k<<":"<<n;cout<<"\n";}
 string w;shortest(max1,max2,&w);cout<<"witness "<<w<<"\n";
 for(int j:{max1,max2}){int z=j;cout<<"transitions "<<j<<": ";for(int c=0;c<2;c++){cout<<(c?'b':'a')<<"=";for(int s=0;s<3;s++){cout<<z%3;z/=3;}cout<<" ";}cout<<"\n";}
}
