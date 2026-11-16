#include <bits/stdc++.h>
using namespace std;
const int P=101;
int m(int x){x%=P;return x<0?x+P:x;}
int pw(int x,int n){int r=1;while(n){if(n&1)r=r*x%P;x=x*x%P;n>>=1;}return r;}
struct Pt{int x,y,z;string label;};
int main(){int phi=m((1+45)*pw(2,99)%P), a=m(phi-1);vector<Pt> pts;
for(int sx:{-1,1})for(int sy:{-1,1})for(int sz:{-1,1})pts.push_back({m(sx),m(sy),m(sz),to_string(sx)+","+to_string(sy)+","+to_string(sz)});
for(int sy:{-1,1})for(int sz:{-1,1})pts.push_back({0,m(sy*a),m(sz*phi),"0,"+to_string(sy)+"/phi,"+to_string(sz)+"phi"});
for(int sx:{-1,1})for(int sy:{-1,1})pts.push_back({m(sx*a),m(sy*phi),0,to_string(sx)+"/phi,"+to_string(sy)+"phi,0"});
for(int sx:{-1,1})for(int sz:{-1,1})pts.push_back({m(sx*phi),0,m(sz*a),to_string(sx)+"phi,0,"+to_string(sz)+"/phi"});
int A[20][9];
for(int i=0;i<20;i++){auto [x,y,z,s]=pts[i];int v[9]={1,x,y,z,m(x*y),m(y*z),m(z*x),m(x*x-y*y),m(y*y-z*z)};copy(v,v+9,A[i]);}
map<unsigned, int> closures;long long count8=0, skipped=0;int maxsz=0;vector<unsigned> top;
for(unsigned mask=0;mask<(1u<<20);mask++){if(__builtin_popcount(mask)!=8)continue; int R[8][9];int t=0;for(int i=0;i<20;i++)if(mask>>i&1)copy(A[i],A[i]+9,R[t++]);int piv[8],rank=0;
for(int j=0;j<9&&rank<8;j++){int k=rank;while(k<8&&R[k][j]==0)k++;if(k==8)continue;for(int h=0;h<9;h++)swap(R[rank][h],R[k][h]);int inv=pw(R[rank][j],99);for(int h=j;h<9;h++)R[rank][h]=R[rank][h]*inv%P;for(int i=0;i<8;i++)if(i!=rank&&R[i][j]){int v=R[i][j];for(int h=j;h<9;h++)R[i][h]=m(R[i][h]-v*R[rank][h]);}piv[rank++]=j;}
if(rank<8){skipped++;continue;}count8++;int freej=0;while(freej<9&&find(piv,piv+8,freej)!=piv+8)freej++;
int c[9]={};c[freej]=1;for(int i=0;i<8;i++)c[piv[i]]=m(-R[i][freej]);unsigned close=0;
for(int i=0;i<20;i++){int val=0;for(int j=0;j<9;j++)val=(val+A[i][j]*c[j])%P;if(val==0)close|=(1u<<i);}closures[close]++;int s=__builtin_popcount(close);if(s>maxsz){maxsz=s;top.clear();top.push_back(close);}else if(s==maxsz&&find(top.begin(),top.end(),close)==top.end())top.push_back(close);
}
map<int,int> hist;for(auto &it:closures)hist[__builtin_popcount(it.first)]++;
cout<<"phi mod P "<<phi<<" rank8="<<count8<<" skipped="<<skipped<<" closures="<<closures.size()<<" max="<<maxsz<<" top="<<top.size()<<"\n";
for(auto [s,n]:hist)cout<<"size "<<s<<": "<<n<<" hyperplanes\n";
for(unsigned cm:top){cout<<"maxmask "<<cm<<" indices ";for(int i=0;i<20;i++)if(cm>>i&1)cout<<i<<",";cout<<"\n";}
for(int i=0;i<20;i++)cout<<"vertex "<<i<<" "<<pts[i].label<<"\n";
}
