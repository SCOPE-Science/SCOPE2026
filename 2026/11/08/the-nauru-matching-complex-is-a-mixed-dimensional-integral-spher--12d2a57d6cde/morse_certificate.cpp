// Exact integral Morse certificate for the ordinary matching complex of GP(12,5).
// Build: g++ -O2 -std=c++17 morse_certificate.cpp -o morse_certificate
// Run:   ./morse_certificate > morse_boundary.txt
// All simplices, matching pairs and the entire reversed Hasse digraph are generated
// from the graph definition. The critical boundary is computed by gradient recursion.
#include <bits/stdc++.h>
using namespace std;
using M=uint64_t;using LL=long long;
vector<pair<int,int>> edges;vector<M> faces;
unordered_map<M,M> upper,lower;
unordered_set<M> U;
vector<M> c7,c8;
vector<vector<LL>> mat;
void rec(int i,uint32_t used,M m){if(i==36){faces.push_back(m);return;}rec(i+1,used,m);auto [a,b]=edges[i];if(!(used&(1u<<a))&&!(used&(1u<<b))) rec(i+1,used|(1u<<a)|(1u<<b),m|(1ull<<i));}
int sign(M m,int bit){return (__builtin_popcountll(m&((1ull<<bit)-1))%2==0)?1:-1;}
// critical indices map; recurrence for a 7cell, coefficients in critical 7-cell basis.
unordered_map<M,int> critical7;
unordered_map<M,vector<LL>> cache;
long long expansions=0;
vector<LL> projection(M t){
 auto cit=cache.find(t);if(cit!=cache.end())return cit->second;
 vector<LL> v(c7.size());
 auto it=critical7.find(t);
 if(it!=critical7.end()){v[it->second]=1;return cache[t]=std::move(v);}
 auto pit=upper.find(t);if(pit==upper.end())return cache[t]=std::move(v);
 M s=pit->second;M b=s^t; int i=__builtin_ctzll(b);int pivot=sign(s,i);
 // boundary of matched upper cell s, except t
 M rem=s;while(rem){int j=__builtin_ctzll(rem);rem&=rem-1;if(j==i)continue; M u=s^(1ull<<j);int coeff=-pivot*sign(s,j); auto z=projection(u);for(int k=0;k<(int)v.size();k++){LL p; if(__builtin_mul_overflow((LL)coeff,z[k],&p) || __builtin_add_overflow(v[k],p,&v[k])){cerr<<"signed-integer overflow in gradient recursion\n";return {};}}}
 ++expansions;
 return cache[t]=std::move(v);
}
int main(){auto st=chrono::steady_clock::now();for(int i=0;i<12;i++){edges.push_back({i,(i+1)%12});edges.push_back({i,i+12});edges.push_back({i+12,12+(i+5)%12});}
rec(0,0,0);cerr<<"enumerated_faces_including_empty="<<faces.size()<<"\n"; U.reserve(faces.size()*2);U.insert(faces.begin(),faces.end());upper.reserve(faces.size());lower.reserve(faces.size());
for(int v=0;v<36;v++){vector<pair<M,M>> pairs;for(M f:U){if(f && !(f&(1ull<<v)) && U.count(f|(1ull<<v)))pairs.emplace_back(f,f|(1ull<<v));}
for(auto[a,b]:pairs){if(U.erase(a)){U.erase(b);upper[a]=b;lower[b]=a;}}}
for(M f:U){int d=__builtin_popcountll(f)-1;if(d==7)c7.push_back(f);if(d==8)c8.push_back(f);}
sort(c7.begin(),c7.end());sort(c8.begin(),c8.end());for(int i=0;i<(int)c7.size();i++)critical7[c7[i]]=i;

map<int,int> crit;for(M f:U)crit[__builtin_popcountll(f)-1]++;
cerr<<"matched_pairs="<<upper.size()<<" critical_empty="<<crit[-1]<<" critical_0="<<crit[0]<<" critical_7="<<crit[7]<<" critical_8="<<crit[8]<<"\n";
if(faces.size()!=1157484 || upper.size()!=578655 || U.size()!=174 || crit[-1]!=1 || crit[0]!=1 || crit[7]!=132 || crit[8]!=40)return 2;


// Verify that the full reversed-matched Hasse diagram has no directed cycle.
unordered_map<M,int> index; index.reserve(faces.size()*2);
for(int i=0;i<(int)faces.size();i++)index.emplace(faces[i],i);
vector<int> indeg(faces.size());long long hasse=0;
for(int i=0;i<(int)faces.size();i++){
 M f=faces[i],rem=f;
 while(rem){int bit=__builtin_ctzll(rem);rem&=rem-1;M g=f^(1ull<<bit);hasse++;
 auto it=upper.find(g);if(it!=upper.end()&&it->second==f)indeg[i]++;
 else indeg[index.at(g)]++;
 }
}
vector<int> queue;queue.reserve(faces.size());for(int i=0;i<(int)faces.size();i++)if(indeg[i]==0)queue.push_back(i);
for(int qi=0;qi<(int)queue.size();qi++){
 M f=faces[queue[qi]];auto it=upper.find(f);if(it!=upper.end()){
 int j=index.at(it->second);if(--indeg[j]==0)queue.push_back(j);
 }
 M rem=f;while(rem){int bit=__builtin_ctzll(rem);rem&=rem-1;M g=f^(1ull<<bit);
 auto pit=upper.find(g);if(pit!=upper.end()&&pit->second==f)continue;
 int j=index.at(g);if(--indeg[j]==0)queue.push_back(j);
 }
}
if(queue.size()!=faces.size()){cerr<<"ACYCLICITY FAILURE visited="<<queue.size()<<endl;return 3;}
cerr<<"ACYCLICITY_PASS hasse="<<hasse<<" visited="<<queue.size()<<endl;
index.clear();index.rehash(0);indeg.clear();queue.clear();

mat=vector<vector<LL>>(c7.size(),vector<LL>(c8.size()));
for(int col=0;col<(int)c8.size();col++){M s=c8[col]; M rem=s;while(rem){int j=__builtin_ctzll(rem);rem&=rem-1;M t=s^(1ull<<j);auto z=projection(t);int coeff=sign(s,j);for(int i=0;i<(int)c7.size();i++){LL p; if(__builtin_mul_overflow((LL)coeff,z[i],&p)||__builtin_add_overflow(mat[i][col],p,&mat[i][col])){cerr<<"signed-integer overflow in boundary accumulation\n";return 4;}}}
}
cout<<c7.size()<<" "<<c8.size()<<"\n";for(auto&row:mat){for(int j=0;j<(int)row.size();j++){if(j)cout<<' ';cout<<row[j];}cout<<'\n';}
long long Mx=0;for(auto&r:mat)for(auto x:r)Mx=max(Mx,llabs(x));cerr<<"boundary_max_entry="<<Mx<<" boundary_nonzero="<<([&](){long long n=0;for(auto&r:mat)for(auto x:r)if(x)n++;return n;})()<<"\n";cerr<<"NAURU_DISCRETE_MORSE_PASS\n";
}
