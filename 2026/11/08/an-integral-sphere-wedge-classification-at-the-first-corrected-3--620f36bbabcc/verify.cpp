#include <bits/stdc++.h>
using namespace std;
using U=uint64_t; using I=long long;
vector<pair<int,int>> E;vector<U> A;vector<U> C8,C9;
unordered_map<U,unsigned char> Up;
unordered_map<U,unsigned char> Pivot;
unordered_map<U,vector<pair<int,I>>> Memo;
unordered_set<U> Active;
unordered_map<U,int> CritIndex;
long long Visits=0;
int pc(U x){return __builtin_popcountll(x);}
vector<pair<int,I>> reduce8(U f){
 auto ci=CritIndex.find(f);if(ci!=CritIndex.end())return {{ci->second,1}};
 auto it=Up.find(f);if(it==Up.end())return {};
 auto jt=Memo.find(f);if(jt!=Memo.end())return jt->second;
 if(!Active.insert(f).second){cerr<<"CYCLE in dimension 8\n";exit(3);} Visits++;
 int j=it->second;U hi=f^(U(1)<<j);int pos=pc(hi&((U(1)<<j)-1));I cof=(pos&1)?-1:1;
 map<int,I> acc;
 for(U z=hi;z;z&=z-1){int k=__builtin_ctzll(z);U lo=hi^(U(1)<<k);if(lo==f)continue;
  I sign=(pc(hi&((U(1)<<k)-1))&1)?-1:1;
  auto v=reduce8(lo);for(auto [id,c]:v)acc[id]-=cof*sign*c;
 }
 vector<pair<int,I>> ans;for(auto [k,v]:acc)if(v)ans.push_back({k,v});
 Active.erase(f);Memo.emplace(f,ans);return ans;
}
int main(int argc,char**argv){
 int n=argc>1?atoi(argv[1]):9;
 for(int i=0;i<3;i++)for(int j=0;j<n;j++){if(i<2)E.push_back({i*n+j,(i+1)*n+j});if(j<n-1)E.push_back({i*n+j,i*n+j+1});}
 A.reserve(10000000);
 function<void(int,U,U)> gen=[&](int k,U used,U mask){if(k==(int)E.size()){if(mask)A.push_back(mask);return;}gen(k+1,used,mask);U um=(U(1)<<E[k].first)|(U(1)<<E[k].second);if(!(used&um))gen(k+1,used|um,mask|(U(1)<<k));};gen(0,0,0);sort(A.begin(),A.end());
 vector<U> Full=A;
 vector<uint64_t> fvec(16,0);for(U f:Full){int k=pc(f);if(k>=16){cerr<<"face size over limit";return 8;}fvec[k]++;}
 long long chi=0;for(int k=1;k<16;k++)chi+=((k&1)?1:-1)* (long long)fvec[k];
 cout<<"euler_characteristic="<<chi<<" face_vector=";for(int k=1;k<16;k++)if(fvec[k])cout<<(k-1)<<":"<<fvec[k]<<" ";cout<<"\n";
 if(n==9&&chi!=164){cerr<<"Euler mismatch";return 9;}
 cout<<"faces="<<A.size()<<" edges="<<E.size()<<"\n";
 long long matched=0;
 for(int i=0;i<(int)E.size();i++){
   vector<U> B;B.reserve(A.size());long long nmatched=0;
   for(U f:A){bool has=(f>>i)&1;bool partner=binary_search(A.begin(),A.end(),f^(U(1)<<i));
     if(partner){if(!has){nmatched++;Pivot.emplace(f,(unsigned char)i);Pivot.emplace(f^(U(1)<<i),(unsigned char)i);if(pc(f)==9)Up.emplace(f,(unsigned char)i);}}
     else B.push_back(f);
   }
   matched+=nmatched;A.swap(B);
 }
 cout<<"matched_pairs="<<matched<<" critical="<<A.size()<<"\n";
 // Check acyclicity of the complete directed Hasse graph, with each
 // matched cover reversed and all other covers oriented downwards.
 unordered_map<U,int> ix;ix.reserve(Full.size()*1.4);
 vector<uint8_t> piv(Full.size(),255);
 for(int a=0;a<(int)Full.size();a++){
   ix.emplace(Full[a],a);
   auto it=Pivot.find(Full[a]);if(it!=Pivot.end())piv[a]=it->second;
 }
 vector<uint8_t> indeg(Full.size(),0);uint64_t incidence=0;
 auto for_out=[&](int a,auto &&emit){
   U f=Full[a];int p=piv[a];
   if(p!=255 && !(f&(U(1)<<p)))emit(f^(U(1)<<p));
   for(U z=f;z;z&=z-1){int k=__builtin_ctzll(z);
     if(k==p)continue;
     U low=f^(U(1)<<k);if(low)emit(low);
   }
 };
 for(int a=0;a<(int)Full.size();a++)for_out(a,[&](U mask){auto it=ix.find(mask);if(it==ix.end()){cerr<<"missing incidence";exit(5);}if(indeg[it->second]==255){cerr<<"indegree overflow";exit(5);}indeg[it->second]++;incidence++;});
 vector<int> queue;queue.reserve(Full.size());for(int a=0;a<(int)Full.size();a++)if(indeg[a]==0)queue.push_back(a);
 for(size_t cur=0;cur<queue.size();cur++){int a=queue[cur];for_out(a,[&](U mask){int j=ix.at(mask);if(!--indeg[j])queue.push_back(j);});}
 cout<<"hasse_incidences="<<incidence<<" DAG_visited="<<queue.size()<<" all_faces="<<Full.size()<<"\n";
 if(queue.size()!=Full.size()){cerr<<"GLOBAL_ACYCLICITY_FAIL\n";return 4;}
 ix.clear();ix.rehash(0);Pivot.clear();Pivot.rehash(0);Full.clear();Full.shrink_to_fit();
 
 map<int,int> critical_by_dim;
 for(U f:A){critical_by_dim[pc(f)-1]++;if(pc(f)==9)C8.push_back(f);if(pc(f)==10)C9.push_back(f);}
 cout<<"critical_cell_vector=";for(auto [d,num]:critical_by_dim)cout<<d<<":"<<num<<" ";cout<<"\n";
 cout<<"critical_dim8="<<C8.size()<<" critical_dim9="<<C9.size()<<" up8="<<Up.size()<<"\n";
 if(n!=9)return 0;
 for(int k=0;k<(int)C8.size();k++)CritIndex[C8[k]]=k;
 vector<vector<I>> B(C8.size(),vector<I>(C9.size()));
 for(int j=0;j<(int)C9.size();j++){
 U hi=C9[j];for(U z=hi;z;z&=z-1){int k=__builtin_ctzll(z);U f=hi^(U(1)<<k);I sign=(pc(hi&((U(1)<<k)-1))&1)?-1:1;for(auto [idx,val]:reduce8(f))B[idx][j]+=sign*val;}
 }
 cout<<"reduction_nodes="<<Visits<<"\n";
 cout<<"boundary_nonzero=";int nnz=0,maxabs=0;for(auto&row:B)for(auto x:row)if(x){nnz++;maxabs=max(maxabs,(int)abs(x));}cout<<nnz<<" max_abs="<<maxabs<<"\n";
 // integer elementary unit pivots; certificate has all pivots unit, so matrix equivalent [I;0]
 int rk=0;I maxgrowth=maxabs;
 while(rk<(int)C9.size()){
 int pi=-1,pj=-1;
 for(int i=rk;i<(int)C8.size()&&pi<0;i++)for(int j=rk;j<(int)C9.size();j++)if(abs(B[i][j])==1){pi=i;pj=j;break;}
 if(pi<0){cout<<"NO_UNIT_PIVOT at "<<rk<<"\n";break;}
 swap(B[rk],B[pi]);for(int i=0;i<(int)C8.size();i++)swap(B[i][rk],B[i][pj]);
 if(B[rk][rk]==-1)for(int j=rk;j<(int)C9.size();j++)B[rk][j]=-B[rk][j];
 for(int i=rk+1;i<(int)C8.size();i++){I c=B[i][rk];if(c)for(int j=rk;j<(int)C9.size();j++)B[i][j]-=c*B[rk][j];}
 for(int i=rk;i<(int)C8.size();i++)for(int j=rk;j<(int)C9.size();j++)maxgrowth=max(maxgrowth,abs(B[i][j]));
 rk++;
 }
 cout<<"unit_rank="<<rk<<" max_growth="<<maxgrowth<<"\n";
 if(rk==(int)C9.size()){bool clean=true;for(int i=rk;i<(int)C8.size();i++)for(int j=rk;j<(int)C9.size();j++)if(B[i][j])clean=false;
 cout<<"homotopy_wedge_S8="<<(C8.size()-rk)<<" full_unit_reduction="<<clean<<"\n"; if(clean&&C8.size()-rk==163&&C9.size()==49&&A.size()==262)cout<<"ALL_VERIFY_OK\n";}
}
