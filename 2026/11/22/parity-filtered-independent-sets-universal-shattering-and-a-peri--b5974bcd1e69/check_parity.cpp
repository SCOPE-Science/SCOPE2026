#include <bits/stdc++.h>
using namespace std;
using Mask=bitset<256>;
struct Solver{
  int n; vector<int> hyp; vector<Mask> col; unordered_map<string,int> memo;
  explicit Solver(int N,int P):n(N){
    for(int s=0;s<(1<<n);++s){
      if((__builtin_popcount((unsigned)s)&1)!=P || (s&(s<<1)))continue;
      hyp.push_back(s);
    }
    if(hyp.size()>256)throw runtime_error("hypothesis bound exceeded");
    for(int j=0;j<n;++j){Mask a;for(int i=0;i<(int)hyp.size();++i)if(hyp[i]&(1<<j))a.set(i);col.push_back(a);}
  }
  int ldim(const Mask& W){
    string key=W.to_string();auto it=memo.find(key);if(it!=memo.end())return it->second;
    int best=0;
    for(int j=0;j<n;++j){
      Mask a=W&col[j],b=W&(~col[j]);
      if(a.none()||b.none())continue;
      int ra=ldim(a),rb=ldim(b);
      best=max(best,1+min(ra,rb));
    }
    memo.emplace(move(key),best);return best;
  }
  pair<int,vector<int>> static_faces(){
    int vc=0;vector<int> counts(n+1);
    for(int S=0;S<(1<<n);++S){
      // Direct trace enumeration, with no use of the private-neighbor criterion.
      unordered_set<int> traces;
      for(int h:hyp)traces.insert(h&S);
      int k=__builtin_popcount((unsigned)S);
      if(traces.size()==(size_t)(1<<k)){counts[k]++;vc=max(vc,k);}
    }
    return {vc,counts};
  }
};
int main(){
  for(int n=1;n<=12;++n)for(int p=0;p<2;++p){
    Solver z(n,p);auto [vc,poly]=z.static_faces();Mask all;
    for(size_t i=0;i<z.hyp.size();++i)all.set(i);
    int online=z.ldim(all);
    int ev=(n==1?0:n==2?p:(n==4&&p==0?2:(n-1)/2));
    int eo=(n%2?(n-1)/2:(n/2)%2==p?n/2:n/2-1);
    if(vc!=ev||online!=eo){cerr<<"FAILED "<<n<<" "<<p<<" "<<vc<<" "<<online<<"\n";return 2;}
    cout<<"PATH n="<<n<<" parity="<<p<<" hypotheses="<<z.hyp.size()<<" vc="<<vc<<" ldim="<<online<<" coeffs=";
    for(int j=0;j<=n;++j)if(poly[j])cout<<j<<":"<<poly[j]<<",";
    cout<<" states="<<z.memo.size()<<"\n";
  }
  cout<<"RESULT PASS 24 independent path/parity cases\n";
}
