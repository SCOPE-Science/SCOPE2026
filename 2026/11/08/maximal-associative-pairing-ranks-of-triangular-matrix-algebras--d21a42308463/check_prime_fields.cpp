// Standalone exhaustive verifier for maximal-rank associative multiplication pairings.
// No external packages: g++ -std=c++17 -O2 triangular_frobenius_maxrank_checker.cpp -o verify && ./verify
#include <bits/stdc++.h>
using namespace std;
long long ipow(int a,int e){long long v=1;while(e--)v*=a;return v;}
int invp(int a,int q){for(int b=1;b<q;b++)if(a*b%q==1)return b;throw runtime_error("nonunit");}
int rankmod(vector<vector<int>> a,int q){if(a.empty())return 0;int r=0,rows=a.size(),cols=a[0].size();for(int j=0;j<cols && r<rows;j++){int k=r;while(k<rows&&a[k][j]==0)k++;if(k==rows)continue;swap(a[r],a[k]);int inv=invp(a[r][j],q);for(int t=j;t<cols;t++)a[r][t]=a[r][t]*inv%q;for(int i=r+1;i<rows;i++)if(a[i][j]){int s=a[i][j];for(int t=j;t<cols;t++)a[i][t]=(a[i][t]-s*a[r][t]%q+q)%q;}r++;}return r;}
long long prediction(int n,int q){int m=(n+1)/2;long long gl=1;for(int i=0;i<m;i++)gl*=ipow(q,m)-ipow(q,i);long long free=ipow(q,m*(m-1));if(n%2)return free*gl;
 long long glprev=1;for(int i=0;i<m-1;i++)glprev*=ipow(q,m-1)-ipow(q,i);
 long long gauss=(ipow(q,m)-1)/(q-1),rankm1=gauss*gauss*glprev;
 return free*(gl*ipow(q,2*m)+rankm1*ipow(q,m-1)*ipow(q,m-1)*(q-1)*(q-1));}
void run(int n,int q){vector<pair<int,int>> indices;for(int i=0;i<n;i++)for(int j=i;j<n;j++)indices.emplace_back(i,j);int dim=indices.size(), target=((n+1)*(n+1))/4;long long total=ipow(q,dim),good=0,disagree=0;for(long long code=0;code<total;code++){long long v=code;int a[6][6]{};for(auto [i,j]:indices){a[i][j]=v%q;v/=q;}vector<vector<int>> gram(dim,vector<int>(dim));for(int ii=0;ii<dim;ii++){auto [i,j]=indices[ii];for(int kk=0;kk<dim;kk++){auto [k,l]=indices[kk];gram[ii][kk]=(j==k?a[i][l]:0);}}
 int rank=rankmod(gram,q);int blocks=0;for(int j=0;j<n;j++){vector<vector<int>> h(j+1,vector<int>(n-j));for(int i=0;i<=j;i++)for(int l=j;l<n;l++)h[i][l-j]=a[i][l];blocks+=rankmod(h,q);}if(blocks!=rank)disagree++;if(rank==target)good++;}
 long long expected=prediction(n,q);cout<<"n="<<n<<" q="<<q<<" dim="<<dim<<" total="<<total<<" optimal="<<good<<" expected="<<expected<<" block_mismatches="<<disagree<<" "<<((good==expected&&disagree==0)?"PASS":"FAIL")<<"\n";if(good!=expected||disagree)exit(1);
}
int main(){for(auto [n,q]:vector<pair<int,int>>{{1,2},{2,2},{2,3},{2,5},{3,2},{3,3},{3,5},{4,2},{4,3},{5,2}})run(n,q);cout<<"ALL_MAXRANK_MULTIPLICATION_FORM_CHECKS_PASS\n";}
