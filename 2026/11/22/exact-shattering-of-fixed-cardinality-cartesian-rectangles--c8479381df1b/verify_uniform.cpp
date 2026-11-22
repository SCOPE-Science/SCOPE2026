#include <bits/stdc++.h>
using namespace std;
using U=uint64_t;
vector<int> masks(int n,int k){ vector<int> out;for(int a=0;a<(1<<n);a++)if(__builtin_popcount((unsigned)a)==k)out.push_back(a);return out; }
vector<U> concepts(int m,int n,int r,int s){vector<U>out;for(int A:masks(m,r))for(int B:masks(n,s)){ U z=0;for(int i=0;i<m;i++)if(A>>i&1)for(int j=0;j<n;j++)if(B>>j&1)z|=(U(1)<<(i*n+j));out.push_back(z);}return out;}
bool shattered(const vector<int>&v,const vector<U>&cs){int k=v.size();U seen=0; for(U c:cs){int tr=0;for(int i=0;i<k;i++)if(c>>v[i]&1)tr|=1<<i;seen|=U(1)<<tr;} U all=(k==6?~U(0):((U(1)<<(1<<k))-1));return seen==all;}
void go(int m,int n,int r,int s,int maxk){auto cs=concepts(m,n,r,s);int N=m*n;vector<long long> out(maxk+1,0);vector<int>v;function<void(int,int)> dfs=[&](int p,int k){if((int)v.size()==k){out[k]+=shattered(v,cs);return;}for(int x=p;x<=N-(k-(int)v.size());x++){v.push_back(x);dfs(x+1,k);v.pop_back();}};for(int k=0;k<=maxk;k++)dfs(0,k);cout<<m<<'x'<<n<<" quota "<<r<<'x'<<s<<" concepts="<<cs.size()<<" polynomial:";for(int k=0;k<=maxk;k++)cout<<" "<<out[k];cout<<'\n';}
int main(){go(2,3,1,1,2);go(3,3,2,2,3);go(4,4,2,3,4);go(4,5,2,3,4);go(4,6,2,3,4);go(5,5,3,3,5);go(6,6,3,3,4);}
