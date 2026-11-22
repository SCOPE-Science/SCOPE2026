#include <bits/stdc++.h>
using namespace std;
static constexpr int R=12;
static const int sizes[R]={1,1,1,2,1,1,1,1,2,3,2,2};
static const int quot[R]={3721,3628,3646,511,3708,3550,3768,3817,3624,2007,3063,3575};
// The quotient's diagonal bit indicates adjacency inside a block of size >= 2.
static vector<unsigned> expand(){
 vector<int> base(R); int n=0;for(int i=0;i<R;i++){base[i]=n;n+=sizes[i];}
 if(n!=18) throw runtime_error("order");
 vector<unsigned> adj(n,0);
 for(int i=0;i<R;i++)for(int j=0;j<R;j++) if(quot[i]&(1<<j))
  for(int a=0;a<sizes[i];a++)for(int b=0;b<sizes[j];b++)
   if(base[i]+a!=base[j]+b)adj[base[i]+a]|=1u<<(base[j]+b);
 for(int a=0;a<n;a++)for(int b=0;b<n;b++)if(((adj[a]>>b)&1)!=((adj[b]>>a)&1))throw runtime_error("asymmetry");
 return adj;
}
static bool zero_forces(const vector<unsigned>& adj,unsigned white){
 int n=adj.size();
 while(white){bool progress=false;
  for(int blue=0;blue<n;blue++)if(!(white>>blue&1)){
   unsigned todo=adj[blue]&white;
   if(todo && !(todo&(todo-1))){white^=todo;progress=true;break;}
  }
  if(!progress)return false;
 }
 return true;
}
static vector<long long> census(const vector<unsigned>& adj){
 int n=adj.size(); vector<long long> c(n+1);
 for(unsigned w=0;w<(1u<<n);w++)if(zero_forces(adj,w))c[n-__builtin_popcount(w)]++;
 return c;
}
int main(){auto a=expand();auto c=census(a);
 long long edges=0; for(auto x:a)edges+=__builtin_popcount(x);edges/=2;
 unsigned reached=1;for(int iter=0;iter<(int)a.size();iter++)for(int j=0;j<(int)a.size();j++)if(reached>>j&1)reached|=a[j];
 cout<<"N="<<a.size()<<" EDGES="<<edges<<" CONNECTED="<<(reached==((1u<<a.size())-1))<<"\n";
 cout<<"ADJ_MASKS";for(auto x:a)cout<<" "<<x;cout<<"\n";
 cout<<"COEFFICIENTS";for(auto x:c)cout<<" "<<x;cout<<"\n";
 if(!(c[13]>c[14] && c[15]>c[14]))return 3;
 if(c[13]!=690 || c[14]!=678 || c[15]!=680)return 4;
 cout<<"COUNTEREXAMPLE_18_PASS\n";
}
