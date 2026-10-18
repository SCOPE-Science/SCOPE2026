#include <bits/stdc++.h>
using namespace std;
long long assertions_count=0;

bool union_closed(uint32_t fam,int m){
    int q=1<<m;
    for(int a=0;a<q;a++) if(fam&(1u<<a))
      for(int b=0;b<q;b++) if(fam&(1u<<b)){
        assertions_count++;
        if(!(fam&(1u<<(a|b)))) return false;
      }
    return true;
}
bool inter_closed(uint32_t fam,int m){
    int q=1<<m;
    for(int a=0;a<q;a++) if(fam&(1u<<a))
      for(int b=0;b<q;b++) if(fam&(1u<<b)){
        assertions_count++;
        if(!(fam&(1u<<(a&b)))) return false;
      }
    return true;
}
uint32_t compfam(uint32_t fam,int m){
    int q=1<<m,U=q-1; uint32_t out=0;
    for(int s=0;s<q;s++) if(fam&(1u<<s)) out|=1u<<(U^s);
    return out;
}
int main(){
    map<int,long long> M{{1,2},{2,7},{3,61},{4,2480}};
    map<int,long long> I{{1,4},{2,14},{3,122},{4,4960}};
    for(int m=1;m<=4;m++){
      int q=1<<m; uint64_t total=1ull<<q, uc0=0, moore=0, inter=0;
      for(uint64_t f64=0;f64<total;f64++){
        uint32_t f=(uint32_t)f64;
        bool u=union_closed(f,m), i=inter_closed(f,m);
        if((f&1u)&&u){
          uc0++; uint32_t c=compfam(f,m);
          assertions_count+=3;
          if(!(c&(1u<<(q-1)))) return 2;
          if(!inter_closed(c,m)) return 3;
          if(compfam(c,m)!=f) return 4;
        }
        if((f&(1u<<(q-1)))&&i) moore++;
        if(i) inter++;
      }
      assertions_count+=4;
      if(uc0!=moore || (long long)moore!=M[m] || (long long)inter!=I[m] || inter!=2*moore) return 5;
      cout<<"m="<<m<<": union_closed_with_empty="<<uc0<<", Moore="<<moore<<", intersection_closed="<<inter<<"\n";
    }
    map<int,long long> Q{{0,2},{1,7},{2,2480}};
    for(auto [n,qv]:Q){assertions_count++; if(M[1<<n]!=qv) return 6; cout<<"n="<<n<<": q_n=M_(2^n)="<<qv<<"\n";}
    cout<<"VERIFY_OK "<<assertions_count<<" exact assertions/comparisons\n";
}
