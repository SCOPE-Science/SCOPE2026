// Exact enumeration of five-cell, valency-two regular zero-Hopf networks.
// Compile: g++ -O2 -std=c++17 checker.cpp -o checker
// Run: ./checker > catalogue.tsv 2> summary.txt
// No external libraries, network access, or floating-point operations.
#include <array>
#include <algorithm>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
using namespace std;
using Mat=array<int,25>;
using Perm=array<int,5>;
struct Counter {long labeled=0,connected=0,strong=0,classes=0,strong_classes=0;};
int det_at(const Mat&A,int x,const vector<pair<Perm,int>>&sgns){
 long ans=0;
 for(const auto& ps:sgns){long term=ps.second;for(int i=0;i<5;i++){
  int j=ps.first[i];term*= (i==j?x:0)-A[i*5+j];
 }ans+=term;}return int(ans);
}
int trace(const Mat&A){int z=0;for(int i=0;i<5;i++)z+=A[6*i];return z;}
Mat mul(const Mat&A,const Mat&B){Mat C{};for(int i=0;i<5;i++)for(int j=0;j<5;j++)for(int k=0;k<5;k++)C[5*i+j]+=A[5*i+k]*B[5*k+j];return C;}
int pow_trace(const Mat&A,int k){Mat p{};for(int i=0;i<5;i++)p[i*5+i]=1;for(int t=0;t<k;t++)p=mul(p,A);return trace(p);}
// All permutation relabellings simultaneously permute rows and columns.
pair<Mat,int> canonical(const Mat&A,const vector<Perm>&perms){
 Mat best;best.fill(3);int stabilizer=0;
 for(auto& p:perms){Mat B{};for(int i=0;i<5;i++)for(int j=0;j<5;j++)B[5*i+j]=A[5*p[i]+p[j]];
  if(B<best)best=B;
  if(B==A)stabilizer++;
 }return {best,stabilizer};
}
bool strong(const Mat&A){for(int s=0;s<5;s++){
 bool visited[5]={};visited[s]=true;bool changed=true;
 while(changed){changed=false;for(int i=0;i<5;i++)if(visited[i])for(int j=0;j<5;j++)if(A[5*i+j]&&!visited[j]){visited[j]=true;changed=true;}}
 for(bool v:visited)if(!v)return false;
 }return true;
}
bool connected(const Mat&A){bool visited[5]={true,false,false,false,false};bool changed=true;
 while(changed){changed=false;for(int i=0;i<5;i++)if(visited[i])for(int j=0;j<5;j++)if((A[5*i+j]||A[5*j+i])&&!visited[j]){visited[j]=true;changed=true;}}
 for(bool v:visited)if(!v)return false;return true;
}
int main(){
 vector<array<int,5>> choices;
 for(int i=0;i<5;i++)for(int j=i;j<5;j++){array<int,5> r{};r[i]++;r[j]++;choices.push_back(r);}
 assert(choices.size()==15);
 vector<Perm> perms;vector<pair<Perm,int>> signed_perms;Perm p={0,1,2,3,4};do{
 perms.push_back(p);int inversions=0;for(int i=0;i<5;i++)for(int j=i+1;j<5;j++)if(p[i]>p[j])inversions++;
 signed_perms.push_back({p, (inversions%2)?-1:1});
 }while(next_permutation(p.begin(),p.end())); assert(perms.size()==120);
 // The characteristic target is (x-2)*x*(x-r)*(x*x+q).
 map<pair<int,int>,Counter> stats;
 set<Mat> seen;
 long all=0,maybes=0,spectral=0,connected_total=0;
 long fixed_sum=0,strong_fixed_sum=0;
 struct Row{int r,q;Mat A;int aut,orbit;bool sc;}; vector<Row> catalogue;
 for(int code=0;code<759375;code++){
  int cur=code;Mat A{};
  for(int i=0;i<5;i++){auto r=choices[cur%15];cur/=15;for(int j=0;j<5;j++)A[5*i+j]=r[j];}
  all++;
  int r=trace(A)-2;
  if(r!=-2 && r!=-1 && r!=1)continue;
  int t2=0;for(int i=0;i<5;i++)for(int j=0;j<5;j++)t2+=A[i*5+j]*A[j*5+i];
  int twice_q=4+r*r-t2;
  if(twice_q%2)continue;
  int q=twice_q/2;
  if(q<1||q>4)continue;
  maybes++;
  // Independent direct characteristic-polynomial test: monic quintics
  // agreeing at five distinct abscissae are identical. Both have 2 as root.
  bool matches=true;
  for(int x:{-1,0,1,3}){
   int target=(x-2)*x*(x-r)*(x*x+q);
   if(det_at(A,x,signed_perms)!=target){matches=false;break;}
  }
  if(!matches)continue;
  // Second, independent verification from power traces of every eigenvalue.
  int tr3=pow_trace(A,3),tr4=pow_trace(A,4),tr5=pow_trace(A,5);
  if(tr3!=8+r*r*r||tr4!=16+r*r*r*r+2*q*q||tr5!=32+r*r*r*r*r){
   fprintf(stderr,"INTERNAL DISAGREEMENT at code %d\n",code);return 2;
  }
  spectral++;
  bool con=connected(A),sc=strong(A);
  if(!con)continue;
  connected_total++;
  auto type=make_pair(r,q);stats[type].labeled++;stats[type].connected++;
  if(sc)stats[type].strong++;
  auto ca=canonical(A,perms);
  fixed_sum+=ca.second;
  if(sc)strong_fixed_sum+=ca.second;
  if(seen.insert(ca.first).second){
    stats[type].classes++;
    if(sc)stats[type].strong_classes++;
    assert(120%ca.second==0);
    catalogue.push_back({r,q,ca.first,ca.second,120/ca.second,sc});
  }
 }
 assert(all==759375 && spectral==21960 && connected_total==spectral);
 assert(catalogue.size()==191 && fixed_sum/120==191 && fixed_sum%120==0);
 assert(strong_fixed_sum/120==56 && strong_fixed_sum%120==0);
 sort(catalogue.begin(),catalogue.end(),[](auto&a,auto&b){
  if(a.r!=b.r)return a.r<b.r;if(a.q!=b.q)return a.q<b.q;return a.A<b.A;
 });
 printf("r\tq\tcanonical_row_major\tautomorphisms\tlabeled_orbit_size\tstrongly_connected\n");
 for(auto row:catalogue){printf("%d\t%d\t",row.r,row.q);for(int v:row.A)printf("%d",v);
   printf("\t%d\t%d\t%d\n",row.aut,row.orbit,row.sc?1:0);}
 fprintf(stderr,"all=%ld initial_spectral_candidates=%ld exact_spectral=%ld connected=%ld, iso=%zu, Burnside_fixed_sum=%ld, strong_fixed_sum=%ld\n",all,maybes,spectral,connected_total,catalogue.size(),fixed_sum,strong_fixed_sum);
 for(auto &[type,c]:stats){fprintf(stderr,"r=%d q=%d labeled=%ld classes=%ld strong_labeled=%ld strong_classes=%ld\n",type.first,type.second,c.labeled,c.classes,c.strong,c.strong_classes);}
}
