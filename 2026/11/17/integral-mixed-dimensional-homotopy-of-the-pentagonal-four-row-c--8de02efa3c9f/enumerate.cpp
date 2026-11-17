#include <bits/stdc++.h>
using namespace std; using U=uint64_t;
int main(int argc,char**argv){int R=argc>1?atoi(argv[1]):4,C=argc>2?atoi(argv[2]):5;
 vector<pair<int,int>> ed; for(int r=0;r<R;r++)for(int c=0;c<C;c++){if(r+1<R)ed.push_back({r*C+c,(r+1)*C+c});ed.push_back({r*C+c,r*C+(c+1)%C});}
 int E=ed.size();cerr<<"vertices "<<R*C<<" edges "<<E<<"\n"; if(E>63)return 1;
 vector<U> vmask(E);for(int i=0;i<E;i++)vmask[i]=(U(1)<<ed[i].first)|(U(1)<<ed[i].second);
 vector<U> faces;faces.reserve(3000000);
 auto dfs=[&](auto&& self,int e,U used,U mask)->void{if(e==E){faces.push_back(mask);return;}self(self,e+1,used,mask); if(!(used&vmask[e]))self(self,e+1,used|vmask[e],mask|(U(1)<<e));};dfs(dfs,0,0,0);
 cerr<<"faces incl empty "<<faces.size()<<"\n";map<int,int>fv;for(U x:faces)fv[__builtin_popcountll(x)-1]++;cerr<<"fvector ";for(auto [d,n]:fv)cerr<<d<<":"<<n<<" ";cerr<<"\n";
 unordered_set<U> remaining(faces.begin(),faces.end());vector<int> order(E);iota(order.begin(),order.end(),0);
 if(argc>3){mt19937 rng(atoi(argv[3]));shuffle(order.begin(),order.end(),rng);}
 vector<pair<U,U>> pairs; pairs.reserve(faces.size()/2);
 for(int i:order){U b=U(1)<<i;int pairs0=pairs.size();for(U x:faces){if((x&b)||!remaining.count(x))continue;U y=x|b;if(remaining.erase(y)){remaining.erase(x);pairs.push_back({x,y});}}cerr<<"step "<<i<<" paired "<<pairs.size()-pairs0<<" left "<<remaining.size()<<"\n";}
 map<int,int> critical;for(U x:remaining)critical[__builtin_popcountll(x)-1]++;
 cerr<<"critical " ;for(auto [d,n]:critical)cerr<<d<<":"<<n<<" ";cerr<<"\n";
 if(getenv("NOOUT"))return 0;ofstream out("complex.txt");out<<"R "<<R<<" C "<<C<<" E "<<E<<" faces "<<faces.size()<<" pairs "<<pairs.size()<<"\n";for(auto e:ed)out<<e.first<<" "<<e.second<<"\n";out<<"critical\n";for(auto [d,n]:critical)out<<d<<" "<<n<<"\n";out<<"masks\n";for(U x:remaining)out<<x<<"\n";out<<"pairs\n";for(auto [x,y]:pairs)out<<x<<" "<<y<<"\n";
}
