// Exact modular certificate for three-basis support uncertainty.
#include <array>
#include <algorithm>
#include <iostream>
#include <vector>
#include <cstdint>
using namespace std;
static int modpow(int b,int e,int p){int r=1; for(;e;e>>=1,b=b*b%p)if(e&1)r=r*b%p; return r;}
static bool fullrank(const vector<array<int,7>>& rows, const int *ix, int p, int q, const array<int,101>& inverse){
 int mat[8][7];
 for(int i=0;i<p+1;i++)for(int j=0;j<p;j++)mat[i][j]=rows[ix[i]][j];
 int h=0;
 for(int k=0;k<p;k++){
  int pivot=h;while(pivot<p+1 && mat[pivot][k]==0)++pivot;
  if(pivot==p+1)continue;
  for(int j=k;j<p;j++)swap(mat[h][j],mat[pivot][j]);
  const int inv=inverse[mat[h][k]];
  for(int i=h+1;i<p+1;i++)if(mat[i][k]){
   int z=mat[i][k]*inv%q; mat[i][k]=0;
   for(int j=k+1;j<p;j++){
    int y=mat[i][j]-z*mat[h][j]%q;
    mat[i][j]= y<0 ? y+q : y;
   }
  }
  if(++h==p)return true;
 }
 return false;
}
static void run(int p,int q,int root){
 if(root==1 || modpow(root,p,q)!=1){cerr<<"invalid primitive-root certificate"<<endl;exit(3);}
 array<int,101> inverse{};for(int i=1;i<q;i++)inverse[i]=modpow(i,q-2,q);
 vector<vector<array<int,7>>> basis(p+1);
 for(int b=0;b<p;b++){
  array<int,7> v{};v[b]=1;basis[0].push_back(v);
 }
 for(int a=0;a<p;a++) for(int b=0;b<p;b++){
  array<int,7> v{};
  for(int t=0;t<p;t++)v[t]=modpow(root,(a*t*t+b*t)%p,q);
  basis[a+1].push_back(v);
 }
 long long total=0;int triples=0;int ix[8];
 for(int a=0;a<p+1;a++)for(int b=a+1;b<p+1;b++)for(int c=b+1;c<p+1;c++){
  ++triples;
  vector<array<int,7>> rows;
  for(int base:{a,b,c})for(auto v:basis[base])rows.push_back(v);
  for(int i=0;i<p+1;i++)ix[i]=i;
  for(;;){
   if(!fullrank(rows,ix,p,q,inverse)){
    cout<<"FAIL prime="<<p<<" bases="<<a<<","<<b<<","<<c<<" rows=";
    for(int j=0;j<p+1;j++)cout<<ix[j]<<",";
    cout<<'\n';exit(2);
   }
   ++total;
   int i=p;
   while(i>=0&&ix[i]==3*p-(p+1)+i)i--;
   if(i<0)break;
   ++ix[i];for(int j=i+1;j<p+1;j++)ix[j]=ix[j-1]+1;
  }
 }
 cout << "CHECK_OK p="<<p<<" modulus="<<q<<" root="<<root<<" triples="<<triples<<" rank_certificates="<<total<<'\n';
}
int main(){run(5,101,95);run(7,29,16);}
