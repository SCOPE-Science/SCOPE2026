// Exact enumeration of forbidden-transitive-triangle orientations and their
// one-, two- and three-point extension profiles. C++17, standard library only.
#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;

struct Census { int labelled=0, distinct_signatures=0, classes=0; map<pair<int,int>,set<int>> signatures; };

int ipow(int a,int b){int v=1;while(b--)v*=a;return v;}

vector<pair<int,int>> edges(int n) {
    vector<pair<int,int>> z;
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)z.push_back({i,j});
    return z;
}

vector<int> decode(int code,int count){
    vector<int> s(count);
    for(int j=0;j<count;j++){s[j]=code%3-1;code/=3;}
    return s;
}

bool admissible_old(int n,const vector<int>& s,const vector<vector<int>>& idx){
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++)for(int k=j+1;k<n;k++){
        int a=s[idx[i][j]], b=s[idx[i][k]], c=s[idx[j][k]];
        if(a && b && c && !(a==1 && b==-1 && c==1)
                          && !(a==-1 && b==1 && c==-1))return false;
    }
    return true;
}

bool admissible_unary(const vector<int>& p,const vector<int>& s,
                      const vector<pair<int,int>>& e){
    for(int t=0;t<(int)e.size();t++){
        int u=e[t].first,v=e[t].second,d=s[t];
        if(d && p[u] && p[v] && !(p[u]==d && p[v]==-d))return false;
    }
    return true;
}

bool adjacent_compatible(const vector<int>& p,const vector<int>& q){
    for(int i=0;i<(int)p.size();i++)
        if(p[i] && q[i] && !(p[i]==-1 && q[i]==1))return false;
    return true;
}

int canonical(const vector<int>& s,const vector<pair<int,int>>& e,
              const vector<vector<int>>& idx,const vector<vector<int>>& perms){
    int best=ipow(3,(int)e.size());
    for(auto const& perm:perms)for(int flip:{-1,1}){
        int code=0,mult=1;
        for(auto [i,j]:e){
            int a=perm[i],b=perm[j],dir=1;
            if(a>b){swap(a,b);dir=-1;}
            code+=mult*(1+s[idx[a][b]]*dir*flip);
            mult*=3;
        }
        best=min(best,code);
    }
    return best;
}

Census census(int n){
    Census out; auto e=edges(n);int m=e.size(),np=ipow(3,n);
    vector<vector<int>> idx(n,vector<int>(n,0));
    for(int t=0;t<m;t++)idx[e[t].first][e[t].second]=t;
    vector<vector<int>> profiles;
    for(int p=0;p<np;p++)profiles.push_back(decode(p,n));
    vector<bitset<243>> allowed(np);
    for(int p=0;p<np;p++)for(int q=0;q<np;q++)
        if(adjacent_compatible(profiles[p],profiles[q]))allowed[p].set(q);
    vector<int> perm(n);iota(perm.begin(),perm.end(),0);
    vector<vector<int>> perms;
    do {perms.push_back(perm);}while(next_permutation(perm.begin(),perm.end()));
    for(int g=0;g<ipow(3,m);g++){
        auto s=decode(g,m);
        if(!admissible_old(n,s,idx))continue;
        out.labelled++;
        bitset<243> active;vector<int> good;
        for(int p=0;p<np;p++)if(admissible_unary(profiles[p],s,e)){
            good.push_back(p);active.set(p);
        }
        int r=0;
        for(int p:good)r+=(allowed[p]&active).count();
        out.signatures[{(int)good.size(),r}].insert(canonical(s,e,idx,perms));
    }
    out.distinct_signatures=out.signatures.size();
    for(auto const& v:out.signatures)out.classes+=v.second.size();
    return out;
}

long long t3(int n,int code){
    auto e=edges(n);auto s=decode(code,e.size());
    vector<vector<int>> profiles;
    for(int p=0;p<ipow(3,n);p++){
        auto v=decode(p,n);
        if(admissible_unary(v,s,e))profiles.push_back(v);
    }
    int q=profiles.size();vector<vector<int>> A(q,vector<int>(q));
    vector<long long> rows(q),cols(q);long long R=0;
    for(int i=0;i<q;i++)for(int j=0;j<q;j++){
        A[i][j]=adjacent_compatible(profiles[i],profiles[j]);
        rows[i]+=A[i][j];cols[j]+=A[i][j];R+=A[i][j];
    }
    long long rr=0,cc=0,rc=0,tri=0;
    for(int i=0;i<q;i++){
        rr+=rows[i]*rows[i];cc+=cols[i]*cols[i];rc+=rows[i]*cols[i];
        for(int j=0;j<q;j++)if(A[i][j])
            for(int k=0;k<q;k++)tri+=(long long)A[j][k]*A[k][i];
    }
    assert(q==44 && R==973);
    return (long long)q*q*q+6LL*q*R+3*rr+3*cc+6*rc+2*tri;
}

int main(){
    const int label_counts[]={1,1,3,21,317,9735};
    const int sig_counts[]={1,1,2,5,17,78};
    for(int n=0;n<=5;n++){
        Census r=census(n);
        int collisions=0;for(auto const& v:r.signatures)
            if(v.second.size()>1)collisions++;
        cout<<"n="<<n<<" labelled="<<r.labelled
            <<" signatures="<<r.distinct_signatures
            <<" converse_isomorphism_classes="<<r.classes
            <<" colliding_signatures="<<collisions<<'\n';
        assert(r.labelled==label_counts[n]);
        assert(r.distinct_signatures==sig_counts[n]);
        if(n<=4)assert(collisions==0);
        if(n==5){
            assert(collisions==1);
            auto it=r.signatures.find({44,973});
            assert(it!=r.signatures.end());
            assert((it->second == set<int>{3048,3124}));
        }
    }
    long long x=t3(5,3048),y=t3(5,3124);
    cout<<"representative_3048: N1=44 R=973 N2=3882 N3="<<x<<'\n';
    cout<<"representative_3124: N1=44 R=973 N2=3882 N3="<<y<<'\n';
    assert(x==653452 && y==658282 && y-x==4830);
    cout<<"EXACT_FIVE_VERTEX_COLLISION_OK\n";
}
