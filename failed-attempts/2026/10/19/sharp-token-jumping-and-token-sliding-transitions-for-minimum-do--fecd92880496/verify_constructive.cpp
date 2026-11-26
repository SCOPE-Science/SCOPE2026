// Standalone structural enumerator for optimum configurations of K(n,2).
// Build: g++ -std=c++17 -O2 verify_constructive.cpp -o verifier
#include <bits/stdc++.h>
using namespace std;
using E=pair<int,int>;using T=array<E,3>;
struct Node{T a; bool triangle;};
string repr(const T &t){string s;for(auto e:t){s+=to_string(e.first)+","+to_string(e.second)+";";}return s;}
T canonical(T t){sort(t.begin(),t.end());return t;}
long long choose(long long n,int k){if(n<k)return 0;long long a=1;for(int i=0;i<k;++i)a=a*(n-i)/(i+1);return a;}
long long fact(int n){long long a=1;for(int i=2;i<=n;i++)a*=i;return a;}
int main(){
 for(int n=5;n<=11;++n){
  vector<Node> states;unordered_map<string,int> ids;
  auto add=[&](T t,bool triangle){t=canonical(t);string key=repr(t);if(ids.count(key))throw runtime_error("duplicate");ids[key]=states.size();states.push_back({t,triangle});};
  for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)for(int c=b+1;c<n;++c)
   add({E{a,b},E{a,c},E{b,c}},true);
  for(int a=0;a<n;++a)for(int b=a+1;b<n;++b)for(int c=b+1;c<n;++c)
  for(int d=c+1;d<n;++d)for(int e=d+1;e<n;++e)for(int f=e+1;f<n;++f){
   array<int,6> x={a,b,c,d,e,f};
   // Fifteen perfect matchings on six fixed labels, obtained recursively.
   function<void(vector<E>,vector<int>)> rec=[&](vector<E> v,vector<int> left){
    if(left.empty()) {add({v[0],v[1],v[2]},false);return;}
    int u=left[0];for(size_t j=1;j<left.size();++j){auto next=left;int w=next[j];next.erase(next.begin()+j);next.erase(next.begin());
      auto v2=v;v2.emplace_back(u,w);rec(v2,next);}
   };rec({},vector<int>(x.begin(),x.end()));
  }
  long long match=choose(n,6)*15;assert((long long)states.size()==choose(n,3)+match);
  for(auto st:states){
   set<E> selected(st.a.begin(),st.a.end());
   for(int a=0;a<n;++a)for(int b=a+1;b<n;++b){E e{a,b};if(selected.count(e))continue;
    bool dominated=false;for(auto f:st.a)if(f.first!=a&&f.second!=a&&f.first!=b&&f.second!=b){dominated=true;break;}
    if(!dominated)throw runtime_error("non-dominating constructed configuration");
   }
  }
  cout<<"n="<<n<<" total="<<states.size()<<" triangles="<<choose(n,3)<<" matchings="<<match;
  for(int slide=0;slide<=1;++slide){
   vector<vector<int>> adj(states.size());long long edges=0;
   for(size_t i=0;i<states.size();++i)if(!states[i].triangle){auto old=states[i].a;
    for(int k=0;k<3;++k)for(int a=0;a<n;++a)for(int b=a+1;b<n;++b){E newer{a,b};
     if(newer==old[k])continue;
     if(slide && (a==old[k].first||a==old[k].second||b==old[k].first||b==old[k].second))continue;
     T next=old;next[k]=newer;next=canonical(next);
     auto it=ids.find(repr(next));if(it!=ids.end()){
      assert(!states[it->second].triangle);
      adj[i].push_back(it->second);
     }
    }
    sort(adj[i].begin(),adj[i].end());adj[i].erase(unique(adj[i].begin(),adj[i].end()),adj[i].end());
   }
   map<int,int> sizes;vector<int> seen(states.size());int d=-1;
   for(size_t i=0;i<states.size();++i){
    if(states[i].triangle){assert(adj[i].empty());continue;}
    if(d<0)d=adj[i].size();assert((int)adj[i].size()==d);
   }
   if(!slide){int predicted=3*(choose(n-4,2)-1);if(match)assert(d==predicted);}
   else {int predicted=3*choose(n-6,2);if(match)assert(d==predicted);}
   for(size_t i=0;i<states.size();++i){edges+=adj[i].size();if(seen[i])continue;
    vector<int> queue={int(i)};seen[i]=1;
    for(size_t k=0;k<queue.size();++k)for(int v:adj[queue[k]])if(!seen[v]){seen[v]=1;queue.push_back(v);}
    sizes[queue.size()]++;
   }
   assert(edges%2==0);edges/=2;
   if(n>=9){assert(sizes.at(1)==choose(n,3));assert(sizes.at(match)==1);}
   if(slide && n==8){assert(sizes.at(1)==56 && sizes.at(4)==105);}
   if(!slide && n>=7){assert(sizes.at(1)==choose(n,3));assert(sizes.at(match)==1);}
   cout<<(slide?" TS":" TJ")<<"_edges="<<edges<<"_degree="<<d<<"_components=";
   for(auto [sz,c]:sizes)cout<<sz<<":"<<c<<";";
  }
  cout<<"\n";
 }
}
