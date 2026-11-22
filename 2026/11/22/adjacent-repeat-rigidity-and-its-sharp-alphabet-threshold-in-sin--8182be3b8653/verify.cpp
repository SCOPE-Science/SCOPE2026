// Exact finite verifier for three-symbol single-insertion list-two codes.
// Compile: g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
// Run: ./verify
#include <algorithm>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
using namespace std;

static void require(bool b, const char* what) {
    if (!b) { fprintf(stderr, "FAIL: %s\n",what); exit(1); }
}
static unsigned pop(uint32_t x) { return __builtin_popcount(x); }
static int idx3(int a,int b,int c,int q) { return (a*q+b)*q+c; }
static vector<uint32_t> output_masks(int q) {
    require(q<=3,"mask range");
    vector<uint32_t> masks;
    for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++)for(int d=0;d<q;d++) {
        int v[4]={a,b,c,d};uint32_t mask=0;
        for(int k=0;k<4;k++) {
            int u[3],p=0;
            for(int j=0;j<4;j++)if(j!=k)u[p++]=v[j];
            mask |= uint32_t(1)<<idx3(u[0],u[1],u[2],q);
        }
        masks.push_back(mask);
    }
    return masks;
}
static uint32_t adjacent_mask(int q) {
    uint32_t res=0;
    for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++)
        if(a==b||b==c)res|=uint32_t(1)<<idx3(a,b,c,q);
    return res;
}
static void verify_exhaustive(int q,int optimal) {
    auto masks=output_masks(q);
    const uint32_t limit=uint32_t(1)<<(q*q*q);
    const uint32_t target=adjacent_mask(q);
    require(pop(target)==unsigned(optimal),"adjacent-set size");
    for(auto mask:masks)require(pop(target&mask)<=2,"adjacent-set decoding");
    for(int k: {optimal+1,optimal}) {
        uint32_t s=(uint32_t(1)<<k)-1;
        uint64_t checked=0, feasible=0;
        uint32_t only=0;
        while(s<limit && s!=0) {
            ++checked;
            bool ok=true;
            for(auto out:masks)if(pop(s&out)>2) {ok=false;break;}
            if(ok){++feasible;only=s;}
            uint32_t low=s & (~s+1);uint32_t next=s+low;
            if(!next)break;
            s=(((next^s)>>2)/low)|next;
        }
        printf("q=%d cardinality=%d checked=%llu feasible=%llu\n",q,k,
            (unsigned long long)checked,(unsigned long long)feasible);
        require(feasible==(k==optimal ? 1ULL:0ULL),"size-layer count");
        if(k==optimal)require(only==target,"unique adjacent-repeat optimum");
    }
}
static const char* PATCH4 =
    "000 002 003 011 021 022 031 033 102 103 111 112 113 120 130 "
    "200 201 213 220 222 223 233 300 301 312 322 330 332 333";
static vector<string> words4() {
    vector<string> out; string s=PATCH4;
    for(size_t i=0;i<s.size();) {
        if(s[i]==' ') {++i;continue;}
        require(i+3<=s.size(),"word parse length");
        string w=s.substr(i,3);
        for(char ch:w)require(ch>='0' && ch<='3',"word parse alphabet");
        out.push_back(w);i+=3;
        require(i==s.size()||s[i]==' ',"word parse separator");
    }
    require(out.size()==29,"patch size");
    sort(out.begin(),out.end());
    require(unique(out.begin(),out.end())==out.end(),"duplicate codeword");
    return out;
}
static void verify_extension(int q,const vector<string>& core) {
    vector<unsigned char> chosen(q*q*q,0);
    for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++) {
        bool same_complete_block=(a/4==b/4 && b/4==c/4 && (a/4+1)*4<=q);
        if(!same_complete_block && (a==b||b==c))chosen[idx3(a,b,c,q)]=1;
    }
    for(int t=0;t<q/4;t++)for(auto &w:core) {
        int a=4*t+w[0]-'0',b=4*t+w[1]-'0',c=4*t+w[2]-'0';
        chosen[idx3(a,b,c,q)]=1;
    }
    int size=0;for(int v:chosen)size+=v;
    require(size==2*q*q-q+q/4,"extension size");
    int worst=0;
    for(int a=0;a<q;a++)for(int b=0;b<q;b++)for(int c=0;c<q;c++)for(int d=0;d<q;d++){
        int v[4]={a,b,c,d},seen[4],cnt=0;
        for(int k=0;k<4;k++) {
            int u[3],p=0;
            for(int j=0;j<4;j++)if(j!=k)u[p++]=v[j];
            int id=idx3(u[0],u[1],u[2],q);
            bool existing=false;
            for(int h=0;h<cnt;h++)if(seen[h]==id)existing=true;
            if(!existing&&chosen[id])seen[cnt++]=id;
        }
        worst=max(worst,cnt);
        require(cnt<=2,"extension output overfull");
    }
    printf("q=%d extended_size=%d maximum_list=%d\n",q,size,worst);
}
int main() {
    verify_exhaustive(2,6);
    verify_exhaustive(3,15);
    const auto core=words4();
    for(int q=4;q<=12;q++)verify_extension(q,core);
    puts("ALL_CHECKS_PASS");
}
