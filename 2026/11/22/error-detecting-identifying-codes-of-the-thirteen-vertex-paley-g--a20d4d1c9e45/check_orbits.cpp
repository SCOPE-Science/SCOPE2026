// An independent arithmetic/affine-orbit certificate for the DET:IC polynomial
// of the Paley graph on 13 vertices. No library dependencies beyond the C++ standard.
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
constexpr int n=13, total=1<<n;
bool edge(int x,int y){if(x==y)return false;int r=(x-y+13)%13;return r==1||r==3||r==4||r==9||r==10||r==12;}
int count_bits(int m){return __builtin_popcount((unsigned)m);}
array<int,n> closed() {
  array<int,n> a{};
  for(int u=0;u<n;u++)for(int v=0;v<n;v++)if(u==v||edge(u,v))a[u]|=1<<v;
  return a;
}
int first_four_block(int omission,const array<int,n>& h){
  for(int u=0;u<n;u++)for(int v=u+1;v<n;v++) if(edge(u,v)){
    int A=h[u]&~h[v],B=h[v]&~h[u];
    if(count_bits(omission&A)>=2&&count_bits(omission&B)>=2)return 1;
  }
  return 0;
}
int four_witness_count(int omission,const array<int,n>& h){
  int count=0;
  for(int u=0;u<n;u++)for(int v=u+1;v<n;v++)if(edge(u,v)){
    int A=h[u]&~h[v],B=h[v]&~h[u];
    if(count_bits(omission&A)>=2&&count_bits(omission&B)>=2)count++;
  }
  return count;
}
int transform(int mask,int mul,int shift){
  int v=0;for(int x=0;x<n;x++)if(mask&(1<<x))v|=1<<((mul*x+shift)%13);
  return v;
}
int main(){
  const auto H=closed();
  for(int u=0;u<n;u++)assert(count_bits(H[u])==7);
  array<int,14> good{},bad{};
  set<int> B;
  for(int m=0;m<total;m++)if(count_bits(m)==4){
    int witnesses=four_witness_count(m,H);
    assert(witnesses<=1);
    if(witnesses){B.insert(m);bad[4]++;}else good[4]++;
  }
  assert(B.size()==351&&good[4]==364);
  map<int,int> five_block_hist;
  for(int m=0;m<total;m++)if(count_bits(m)==5){
    int blocked=0;
    for(int x=0;x<n;x++)if(m&(1<<x)) if(B.count(m^(1<<x)))blocked++;
    five_block_hist[blocked]++;
    assert(blocked>=1);
  }
  assert((five_block_hist==map<int,int>{{1,273},{2,312},{3,546},{4,156}}));
  for(int k=0;k<=13;k++){
    if(k<9)continue;
    for(int omission=0;omission<total;omission++)if(count_bits(omission)==n-k){
      assert(count_bits(omission)<=4);
      if(count_bits(omission)<4||!B.count(omission))good[k]++;
    }
  }
  assert(good[9]==364&&good[10]==286&&good[11]==78&&good[12]==13&&good[13]==1);
  const int units[]={1,3,4,9,10,12};
  for(int k: {4,5}){
    set<int> unseen;
    for(int m=0;m<total;m++)if(count_bits(m)==k)unseen.insert(m);
    int orbit_count=0, permitted_orbits=0;
    while(!unseen.empty()){
      int rep=*unseen.begin();set<int> orb;
      for(int a:units)for(int b=0;b<n;b++)orb.insert(transform(rep,a,b));
      int oc=-1;
      for(int m:orb){
        assert(unseen.count(m));unseen.erase(m);
        int c=0;
        if(k==4)c=B.count(m)?1:0;
        else for(int x=0;x<n;x++)if(m&(1<<x))c+=B.count(m^(1<<x));
        if(oc==-1)oc=c;else assert(oc==c);
      }
      assert((int)orb.size()==26||(int)orb.size()==39||(int)orb.size()==78);
      orbit_count++;
      cout<<"orbit "<<k<<" "<<orb.size()<<" "<<oc<<" ";
      bool first=true;
      for(int x=0;x<n;x++)if(rep&(1<<x)){if(!first)cout<<",";cout<<x;first=false;}
      cout<<"\n";
      if(k==4&&!oc)permitted_orbits++;
    }
    if(k==4){assert(orbit_count==13&&permitted_orbits==7);}
    else assert(orbit_count==19);
    cout<<"omission_"<<k<<"_affine_orbits "<<orbit_count<<"\n";
  }
  cout<<"unique_adjacent_pair_witnesses "<<B.size()<<"\n";
  cout<<"five_omission_forbidden_tetrads";
  for(auto x:five_block_hist)cout<<" "<<x.first<<":"<<x.second;
  cout<<"\n";
  cout<<"det_code_polynomial";for(int k=9;k<=13;k++)cout<<" "<<k<<":"<<good[k];cout<<"\n";
  cout<<"orbit_verification_PASS\n";
}
