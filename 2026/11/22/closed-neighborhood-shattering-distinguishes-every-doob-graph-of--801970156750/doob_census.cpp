#include <bits/stdc++.h>
using namespace std; using U=uint64_t; 
vector<U> graph(int typ,int closed){vector<U>N(64);for(int a=0;a<64;a++)for(int b=0;b<64;b++){
 bool adj=false;
 if(typ==0){ int ax=a/16,ay=(a/4)%4,az=a%4,bx=b/16,by=(b/4)%4,bz=b%4;adj=((ax!=bx)+(ay!=by)+(az!=bz))==1; }
 else {int as=a/4,bs=b/4,ak=a%4,bk=b%4; int dx=((as/4)-(bs/4)+4)%4, dy=((as%4)-(bs%4)+4)%4;
 bool sh=(dx==1&&dy==0)||(dx==3&&dy==0)||(dx==0&&dy==1)||(dx==0&&dy==3)||(dx==1&&dy==1)||(dx==3&&dy==3);
 adj=(as==bs ? ak!=bk : (ak==bk && sh));}
 if(adj||(closed&&a==b))N[a]|=(U(1)<<b);
 }return N;}
 bool shatter(const vector<U> &N, vector<int>& q){int k=q.size(); U full=~U(0);U tr[64];for(int h=0;h<64;h++){unsigned v=0;for(int i=0;i<k;i++)v|=((N[q[i]]>>h)&1)<<i;tr[h]=v;}
 U mask=0;for(int h=0;h<64;h++)mask|=U(1)<<tr[h];return __builtin_popcountll(mask)==(1<<k);
 }
 int main(int argc,char**argv){int typ=atoi(argv[1]),closed=atoi(argv[2]),maxk=atoi(argv[3]);auto N=graph(typ,closed); for(int i=0;i<64;i++)if(__builtin_popcountll(N[i])!=(closed?10:9)){cerr<<"degree mismatch";return 2;}
 vector<int> s; vector<unsigned long long> count(maxk+1),facets(maxk+1);vector<array<int,5>> reps; 
 function<void(int,int)>dfs=[&](int st,int k){if(k>0&&!shatter(N,s))return;count[k]++;
 if(k==maxk)return;
 for(int j=st;j<64;j++){s.push_back(j);dfs(j+1,k+1);s.pop_back();}
 };dfs(0,0);for(int k=0;k<=maxk;k++)cout<<k<<" "<<count[k]<<"\n"; }
