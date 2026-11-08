#include <bits/stdc++.h>
using namespace std;
vector<string> words(int n){vector<string> w; int lim=1;for(int i=0;i<n;i++)lim*=3; for(int v=0;v<lim;v++){int k=v;string s(n,'0');for(int i=n-1;i>=0;i--){s[i]=char('0'+k%3);k/=3;}bool ok=true;for(int i=1;i<n;i++)if(s[i]==s[i-1])ok=false;if(ok)w.push_back(s);}return w;}
long long count_codes(int n){
 auto W=words(n),H=words(n-2),D=words(n-1);map<string,int> idx;for(int i=0;i<(int)W.size();i++)idx[W[i]]=i;
 vector<array<int,2>> pin(H.size()),pout(H.size());
 for(int z=0;z<(int)H.size();z++){
   vector<int>a,b;for(int i=0;i<(int)D.size();i++){if(D[i].substr(1)==H[z])a.push_back(i);if(D[i].substr(0,n-2)==H[z])b.push_back(i);}
   assert(a.size()==2&&b.size()==2);pin[z]={a[0],a[1]};pout[z]={b[0],b[1]};
 }
 long long ans=0,cycles=1LL<<H.size();assert(H.size()<=12);
 vector<array<int,3>> near(W.size());
 for(int i=0;i<(int)W.size();i++){
    auto w=W[i];near[i][0]=i;int j=1;
    for(char c='0';c<='2';c++)if(c!=w[0])near[i][j++]=idx.at(string(1,c)+w.substr(0,n-1));
 }
 for(long long mask=0;mask<cycles;mask++){
   vector<bool> chosen(W.size(),false);
   for(int z=0;z<(int)H.size();z++)for(int i=0;i<2;i++){
     auto a=D[pin[z][i]],b=D[pout[z][i^((mask>>z)&1)]];
     string w=a+b.back();chosen[idx.at(w)]=true;
   }
   vector<unsigned long long> sig; for(auto a:near){unsigned long long ss=0;for(int v:a)if(chosen[v])ss|=1ULL<<v;sig.push_back(ss);}
   sort(sig.begin(),sig.end());if(sig[0]!=0&&unique(sig.begin(),sig.end())==sig.end()) ans++;
 }
 return ans;
}
int main(){for(int n=3;n<=5;n++){auto r=count_codes(n); cout<<n<<" "<<r<<"\n"; if(r!=(n==3?4:n==4?27:1728))return 2;}cout<<"INDEPENDENT_CPP_OK\n";}
