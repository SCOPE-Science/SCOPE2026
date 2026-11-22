#include <bits/stdc++.h>
using namespace std;
int main(){ const int n=9;const int D=4; long long total=0, sync=0, prim_non=0, impr_non=0, prim_sync=0, impr_sync=0; int b[n]; const int N=387420489;int first[n];bool got=false;
 for(int z=0;z<N;z++){int y=z,mask=0;for(int i=0;i<n;i++){b[i]=y%9;y/=9;mask|=1<<b[i];}if(__builtin_popcount((unsigned)mask)!=7)continue;total++;
 bool impr=true;for(int i=0;i<3;i++)if(b[i]%3!=b[i+3]%3||b[i]%3!=b[i+6]%3)impr=false;
 unsigned char T[5]={};for(int d=1;d<=4;d++){unsigned char u=0;for(int i=0;i<n;i++){int delta=abs(b[i]-b[(i+d)%n]);int dst=min(delta,n-delta);u|=1<<dst;}T[d]=u;}
 int reached=1,old;do{old=reached;for(int d=1;d<=D;d++)if(T[d]&old)reached|=1<<d;}while(old!=reached);
 bool issync=reached==31;if(issync){sync++;if(impr)impr_sync++;else prim_sync++;}else{if(impr)impr_non++;else {prim_non++;if(!got){got=true;for(int i=0;i<n;i++)first[i]=b[i];cerr<<"EARLY PRIMITIVE NONSYNC z="<<z<<" map=";for(int i=0;i<n;i++)cerr<<first[i]<<',';cerr<<'\n';}}}
 }
 cout<<"rank7 total "<<total<<" primitive nonsync "<<prim_non<<" impr nonsync "<<impr_non<<" primitive sync "<<prim_sync<<" impr sync "<<impr_sync<<'\n';
}
