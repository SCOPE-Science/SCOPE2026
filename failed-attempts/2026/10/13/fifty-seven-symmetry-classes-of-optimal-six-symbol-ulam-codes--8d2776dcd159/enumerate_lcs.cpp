#include <bits/stdc++.h>
using namespace std;
using P=array<unsigned char,6>;
int lcs(P a,P b){int q[6],lis[6],L=0; for(int i=0;i<6;i++)q[b[i]]=i; for(int i=0;i<6;i++){int x=q[a[i]]; int j=lower_bound(lis,lis+L,x)-lis;lis[j]=x;if(j==L)L++;}return L;}
string encode(P p){string s;for(auto c:p)s+=char('0'+c);return s;}
int main(){vector<P>p;P a={0,1,2,3,4,5};do{p.push_back(a);}while(next_permutation(a.begin(),a.end()));int n=p.size(); vector<vector<uint8_t>>adj(n,vector<uint8_t>(n));for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)if(lcs(p[i],p[j])<=2)adj[i][j]=adj[j][i]=1;
vector<int>N;for(int i=1;i<n;i++)if(adj[0][i])N.push_back(i);cerr<<"neighbors="<<N.size()<<"\n";
map<string,long long>classes; long long count=0; vector<array<int,4>>reps;
for(int ii=0;ii<(int)N.size();ii++)for(int jj=ii+1;jj<(int)N.size();jj++){int u=N[ii],v=N[jj];if(!adj[u][v])continue;for(int kk=jj+1;kk<(int)N.size();kk++){int w=N[kk];if(!adj[u][w]||!adj[v][w])continue;count++;
for (int t:N) if(t!=u&&t!=v&&t!=w&&adj[u][t]&&adj[v][t]&&adj[w][t]) {cerr<<"ERROR: five-word code"<<endl;return 1;}
array<int,4>code={0,u,v,w}; string key="";for(int r=0;r<2;r++)for(int k=0;k<4;k++){
P zero=p[code[k]];if(r)reverse(zero.begin(),zero.end()); P inv;for(int i=0;i<6;i++)inv[zero[i]]=i;
array<string,4>strings;for(int t=0;t<4;t++){P q=p[code[t]];if(r)reverse(q.begin(),q.end());for(int i=0;i<6;i++)q[i]=inv[q[i]];strings[t]=encode(q);}sort(strings.begin(),strings.end());string ss;for(auto s:strings){ss+=s+"|";}if(key.empty()||ss<key)key=ss;
}classes[key]++;}}
cerr<<"normalized_solutions="<<count<<" orbit_classes="<<classes.size()<<"\n";
map<long long,int> hist; for(auto [key,mult]:classes)hist[mult]++;
if(N.size()!=132||count!=298||classes.size()!=57||hist!=map<long long,int>{{2,7},{4,29},{8,21}}){cerr<<"CENSUS_MISMATCH"<<endl;return 2;}
cout<<"VERIFY_OK permutations=720 neighbors=132 normalized=298 labeled=53640 classes=57 no_five=1"<<endl;for(auto [m,h]:hist)cerr<<"multiplicity="<<m<<" classes="<<h<<"\n";
for(auto [key,mult]:classes)cout<<mult<<" "<<key<<"\n";
}
