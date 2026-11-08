// Full GF(2) elimination on the 3-by-n closed-neighborhood matrix.
#include <bits/stdc++.h>
using namespace std;
map<int,int> expected(int n){
 int q=n/6,r=n%6;
 if(r==0)return {{10*q,1}};
 if(r==1)return {{6*q+1,1}};
 if(r==2)return {{6*q+2,2},{6*q+4,2}};
 if(r==3)return {{6*q+5,1}};
 if(r==4)return {{10*q+10,1}};
 return {{6*q+6,6},{10*q+10,2}};
}
map<int,int> solve(int n){
 int N=3*n;
 vector<vector<unsigned char>> a(N,vector<unsigned char>(N+1));
 for(int col=0;col<n;col++)for(int row=0;row<3;row++){
   int i=col*3+row;
   for(auto [dr,dc]:vector<pair<int,int>>{{0,0},{-1,0},{1,0},{0,-1},{0,1}}){
     int r=row+dr,c=col+dc;
     if(0<=r&&r<3&&0<=c&&c<n)a[i][c*3+r]=1;
   }
   a[i][N]=1;
 }
 int rank=0;vector<int> piv;
 for(int c=0;c<N;c++){
   int j=rank;
   while(j<N && !a[j][c])j++;
   if(j==N)continue;
   swap(a[j],a[rank]);
   for(int i=0;i<N;i++)if(i!=rank && a[i][c])
     for(int k=c;k<=N;k++)a[i][k]^=a[rank][k];
   piv.push_back(c); rank++;
 }
 for(int i=rank;i<N;i++)assert(!a[i][N]);
 set<int> P(piv.begin(),piv.end());
 vector<int> free;
 for(int i=0;i<N;i++)if(!P.count(i))free.push_back(i);
 assert(free.size()<=3);
 map<int,int> ans;
 for(int m=0;m<(1<<free.size());m++){
   vector<int> x(N);
   for(int i=0;i<(int)free.size();i++)x[free[i]]=(m>>i)&1;
   for(int i=rank-1;i>=0;i--){
     int z=a[i][N];
     for(int j=piv[i]+1;j<N;j++)if(a[i][j])z^=x[j];
     x[piv[i]]=z;
   }
   for(int i=0;i<N;i++){
     int s=0;
     for(int j=0;j<N;j++)if(j==i || (i/3==j/3&&abs(i%3-j%3)==1) || (i%3==j%3&&abs(i/3-j/3)==1))s^=x[j];
     assert(s==1);
   }
   ans[accumulate(x.begin(),x.end(),0)]++;
 }
 return ans;
}
int main(){
 for(int n=1;n<=80;n++){
  auto s=solve(n),p=expected(n);
  if(s!=p){cerr<<"MISMATCH "<<n<<"\n";return 1;}
 }
 cout<<"GAUSSIAN_PASS n=1..80 full binary elimination, exact weight multiplicities and direct matrix replay\n";
}
