#include <bits/stdc++.h>
using namespace std;
// Independent literal graph-neighborhood time stepping over F_3; no matrices or rank computations.
int main(){mt19937 gen(203717);int samples=0;
for(auto [m,n]:vector<pair<int,int>>{{3,3},{3,6},{6,3},{6,6}}){
 vector<pair<int,int>> v; for(int i=0;i<m;i++)for(int j=0;j<n;j++)if(i||j)v.push_back({i,j});
 int N=v.size();vector<vector<int>> neigh(N);
 for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j && (v[i].first==v[j].first||v[i].second==v[j].second))neigh[i].push_back(j);
 map<int,int> freq;int count= (N<=8?2500:300);
 for(int z=0;z<count;z++){
 vector<int> u(N),prev(N);for(int &x:u)x=gen()%3;for(int &x:prev)x=gen()%3;
 vector<int> a=u,b=prev;int period=0;
 for(int t=1;t<=72;t++){
 vector<int> c(N);
 for(int i=0;i<N;i++) {int s=-b[i];for(int j:neigh[i])s+=a[j];c[i]=((s%3)+3)%3;}
 b=a;a=c;
 if(a==u&&b==prev){period=t;break;}
 }
 if(!period || 72%period) return 1;
 if(period!=1&&period!=2&&period!=6&&period!=8&&period!=18&&period!=24&&period!=72) return 2;
 freq[period]++;samples++;
 }
 cout<<"PASS "<<m<<"x"<<n<<" punctured literal-walk samples "<<count<<", periods:";
 for(auto [p,c]:freq) cout<<" "<<p<<":"<<c;cout<<"\n";
 }
 cout<<"PASS "<<samples<<" independent direct wave trajectories, all period divisors of 72\n";
}
