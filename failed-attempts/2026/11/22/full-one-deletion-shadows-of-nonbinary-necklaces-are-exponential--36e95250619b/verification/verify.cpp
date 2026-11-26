// Exhaustive checks for one-deletion shadows of circular words.
// Build: c++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify
// Run:   ./verify
#include <algorithm>
#include <cstdint>
#include <iostream>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

string canonical(string s) {
    string best=s;
    for(size_t k=1;k<s.size();++k) {
        string t=s.substr(k)+s.substr(0,k);
        if(t<best) best=t;
    }
    return best;
}
int shadow(string const& w) {
    set<string> out;
    for(size_t i=0;i<w.size();++i)
        out.insert(canonical(w.substr(0,i)+w.substr(i+1)));
    return (int)out.size();
}
bool proper(string const& w) {
    for(size_t i=0;i<w.size();++i)
        if(w[i]==w[(i+1)%w.size()]) return false;
    return true;
}
void demand(bool t,const string& msg) {if(!t) throw runtime_error(msg);}
uint64_t ipow(uint64_t q,int n) {uint64_t a=1;while(n--)a*=q;return a;}
void enumerate(int q,int n) {
    const uint64_t total=ipow(q,n);
    uint64_t proper_count=0,full_count=0;
    int best=0;
    string w(n,'0');
    for(uint64_t v=0;v<total;v++) {
        uint64_t k=v;
        for(int i=n-1;i>=0;i--) {w[i]=char('0'+k%q);k/=q;}
        int d=shadow(w);
        demand(d<=n,"shadow too large");
        if(proper(w)) {
            ++proper_count;
        } else {
            demand(d<n,"nonproper full shadow");
        }
        if(d==n) {++full_count; demand(proper(w),"full but not proper");}
        best=max(best,d);
    }
    uint64_t expected=ipow(q-1,n)+(n%2==0 ? uint64_t(q-1):0);
    if(n%2==1) expected-=q-1;
    demand(best==n,"maximum mismatch");
    demand(proper_count==expected,"proper coloring polynomial mismatch");
    demand(full_count>0,"no maximizers");
    cout<<"q="<<q<<" n="<<n<<" checked="<<total<<" max="<<best
        <<" proper="<<proper_count<<" full="<<full_count<<'\n';
}
void fixed_point_test(int n) {
    // For a hypothetical collision between deletions at i,j, rotate the
    // remaining indexed positions by k and close the matching i -> j.
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int k=0;k<n-1;k++) {
        vector<int> left,right,pi(n,-1);
        for(int a=0;a<n;a++)if(a!=i)left.push_back(a);
        for(int a=0;a<n;a++)if(a!=j)right.push_back(a);
        for(int t=0;t<n-1;t++)pi[left[t]]=right[(t+k)%(n-1)];
        pi[i]=j;
        vector<int> seen(n,0);
        int cycles=0;
        for(int a=0;a<n;a++) {
            demand(pi[a]>=0,"unmapped site");
            if(!seen[a]) {
                ++cycles;
                for(int b=a;!seen[b];b=pi[b])seen[b]=1;
            }
        }
        if(cycles>n/2) {
            // Verify that some adjacent positions are forced equal.
            for(int a=0;a<n;a++)seen[a]=0;
            vector<int> cls(n,-1);int cc=0;
            for(int a=0;a<n;a++)if(cls[a]<0) {
                for(int b=a;cls[b]<0;b=pi[b])cls[b]=cc;
                cc++;
            }
            bool bad=false;
            for(int a=0;a<n;a++)if(cls[a]==cls[(a+1)%n])bad=true;
            demand(bad,"large-cycle compatible collision");
        }
    }
}
void witnesses() {
    for(int q=3;q<=7;q++)for(int n=3;n<=256;n++) {
        string w="2";
        for(int i=0;i<n-1;i++) w+=char('0'+i%2);
        demand(shadow(w)==n,"marker construction failure");
    }
}
int main(){
    try {
        for(int n=3;n<=12;n++)enumerate(3,n);
        for(int n=3;n<=7;n++)enumerate(4,n);
        for(int n=3;n<=30;n++)fixed_point_test(n);
        witnesses();
        cout<<"VERIFY_OK all finite checks complete\n";
    } catch(const exception& e) {
        cerr<<"VERIFY_FAILED "<<e.what()<<'\n'; return 1;
    }
}
