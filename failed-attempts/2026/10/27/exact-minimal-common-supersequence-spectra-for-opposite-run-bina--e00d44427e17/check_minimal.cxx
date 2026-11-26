#include <bits/stdc++.h>
using namespace std;
static bool subseq(const string &pat,const string &w){int i=0;for(char x:w)if(i<(int)pat.size()&&x==pat[i])++i;return i==(int)pat.size();}
static bool is_minimal(const string &A,const string &B,const string &w){
 if(!subseq(A,w)||!subseq(B,w))return false;
 for(int k=0;k<(int)w.size();++k){string v=w.substr(0,k)+w.substr(k+1);if(subseq(A,v)&&subseq(B,v))return false;}
 return true;
}
static bool structural(int m,const string &w){
 int zeros=count(w.begin(),w.end(),'0'),ones=(int)w.size()-zeros;
 if(zeros<ones){string v=w;for(char &x:v)x=(x=='0'?'1':'0');return structural(m,v);}
 if(zeros!=2*m||ones<m||ones>=2*m)return false;
 int j=ones-m,z=0,p=-1,q=-1;
 for(int i=0;i<(int)w.size();++i)if(w[i]=='0'){++z;if(z==m)p=i;if(z==m+1)q=i;}
 int left=count(w.begin(),w.begin()+p,'1');
 int central=count(w.begin()+p+1,w.begin()+q,'1');
 int right=count(w.begin()+q+1,w.end(),'1');
 return left==j&&central==m-j&&right==j;
}
int main(){
 for(int m=1;m<=5;++m){string A=string(m,'0')+string(m,'1'),B=string(m,'1')+string(m,'0');
 vector<long long>c(m,0);long long examined=0;
 for(int n=3*m;n<=4*m;++n){for(uint32_t mask=0;mask<(1u<<n);++mask){string w(n,'0');for(int k=0;k<n;++k)if(mask&(1u<<k))w[k]='1';
 bool a=is_minimal(A,B,w),b=structural(m,w);if(a!=b){cerr<<"MISMATCH m="<<m<<" w="<<w<<" a="<<a<<" b="<<b<<'\n';return 2;}
 if(a){if(n==4*m){cerr<<"MAX LEN ERROR\n";return 3;}c[n-3*m]++;}
 examined++;}}
 cout<<"m="<<m<<" checked="<<examined<<" counts:";
 for(int j=0;j<m;++j){long long f=1;for(int k=1;k<=j;++k)f=f*(m+k-1)/k;
 long long expected=2*f*f;
 if(c[j]!=expected){cerr<<"COUNT ERROR m="<<m<<" j="<<j<<" expected="<<expected<<" got="<<c[j]<<'\n';return 4;}
 cout<<" "<<c[j];}
 cout<<"\n";}
 cout<<"VERIFY_OK\n";
}
