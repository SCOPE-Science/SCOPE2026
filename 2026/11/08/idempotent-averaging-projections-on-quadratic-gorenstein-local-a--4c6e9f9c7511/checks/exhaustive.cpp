#include <bits/stdc++.h>
using namespace std;
int q,m,n,kind;
int md(int x){x%=q;return x<0?x+q:x;}
void mult(const int*a,const int*b,int*c){fill(c,c+n,0);c[0]=md(a[0]*b[0]);for(int i=1;i<=m;i++)c[i]=md(a[0]*b[i]+a[i]*b[0]);int dot=0; // kind 0: hyperbolic plane; kind 1: diagonal identity
if(kind==0) dot=a[1]*b[2]+a[2]*b[1]; else for(int i=1;i<=m;i++)dot+=a[i]*b[i];
c[n-1]=md(a[0]*b[n-1]+a[n-1]*b[0]+dot);
}
void apply(const int*P,const int*x,int*y){fill(y,y+n,0);for(int i=0;i<n;i++)for(int j=0;j<n;j++)y[i]+=P[i*n+j]*x[j];for(int i=0;i<n;i++)y[i]=md(y[i]);}
int main(int argc,char**argv){q=atoi(argv[1]);m=atoi(argv[2]);kind=atoi(argv[3]);n=m+2;bool full=argc>4 && string(argv[4])=="full";int J=full?n:n-1; long long total=1;for(int i=0;i<n*J;i++)total*=q;if(total>15000000){cerr<<"too many";return 1;}vector<long long> hist(n+1,0);long long failId=0,failA=0,nonrad=0; vector<int>P(n*n),PX(n*n),A(n),B(n),C(n),D(n),E(n),F(n);vector<int>basis(n*n);for(int i=0;i<n;i++)basis[i*n+i]=1;
for(long long code=0;code<total;code++){fill(P.begin(),P.end(),0);if(!full)P[0]=1;long long t=code;for(int j=(full?0:1);j<n;j++)for(int i=0;i<n;i++){P[i*n+j]=t%q;t/=q;}
bool ok=true;for(int j=0;j<n&&ok;j++){for(int i=0;i<n;i++){int s=0;for(int k=0;k<n;k++)s+=P[i*n+k]*P[k*n+j];if(md(s)!=P[i*n+j]){ok=false;break;}}}if(!ok){failId++;continue;}
for(int j=0;j<n&&ok;j++)for(int k=0;k<n&&ok;k++){ // e_j P(e_k) vs P(e_j)P(e_k)
  for(int i=0;i<n;i++){A[i]=basis[j*n+i];B[i]=P[i*n+k];C[i]=P[i*n+j];}
  mult(A.data(),B.data(),D.data());apply(P.data(),D.data(),E.data());mult(C.data(),B.data(),F.data());if(E!=F)ok=false;
}
if(!ok){failA++;continue;}
int rank=0;vector<int>R=P;for(int col=0,row=0;col<n&&row<n;col++){int k=row;while(k<n&&R[k*n+col]==0)k++;if(k==n)continue;for(int j=col;j<n;j++)swap(R[k*n+j],R[row*n+j]);int inv=1;while(inv*R[row*n+col]%q!=1)inv++;for(int j=col;j<n;j++)R[row*n+j]=md(R[row*n+j]*inv);for(int i=0;i<n;i++)if(i!=row){int a=R[i*n+col];for(int j=col;j<n;j++)R[i*n+j]=md(R[i*n+j]-a*R[row*n+j]);}row++;rank++;}
hist[rank]++;for(int j=1;j<n;j++)if(P[j]!=0){nonrad++;break;}
}
cout<<"field="<<q<<" m="<<m<<" form="<<kind<<" candidates="<<total<<" idempotent_fail="<<failId<<" averaging_fail="<<failA<<" histogram=";for(auto h:hist)cout<<h<<",";cout<<" nonrad="<<nonrad<<"\n";
}
