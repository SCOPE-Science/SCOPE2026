// Reproducible exhaustive integer verification of the Heawood non-matching filtration.
// Compile: c++ -O3 -std=c++17 verify_nonmatching_heawood.cpp -o verify_nm
// Run: ./verify_nm
// Uses only the C++17 standard library. No external datasets or network access.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <stdexcept>
#include <unordered_map>
#include <vector>
#include <functional>
#include <string>
using namespace std;
constexpr int E = 21;
constexpr int N = 1 << E;
using VLL = vector<long long>;
struct Data {
    vector<pair<int,int>> edge;
    vector<uint32_t> meet;
    vector<uint8_t> matching_number;
    Data():meet(E),matching_number(N) {
        for(int p=0;p<7;p++) for(int d:{0,1,3}) edge.emplace_back(p,(p+d)%7);
        for(int i=0;i<E;i++) for(int j=0;j<E;j++)
            if(edge[i].first==edge[j].first || edge[i].second==edge[j].second)
                meet[i] |= (1U<<j);
        for(int s=1;s<N;s++) {
            int i=__builtin_ctz((unsigned)s),r=s&(s-1);
            matching_number[s] = max((int)matching_number[r],1+(int)matching_number[r&~meet[i]]);
        }
    }
};
void independently_verify_matching_number(const Data& D){
    // Independently enumerate *only matchings*, then perform a subset zeta
    // transform to determine the maximum matching in every one of 2^21 edge sets.
    vector<uint8_t> best(N,0);array<int,8> matches{};
    function<void(int,int,int,int,int)> enumerate = [&](int first,int points,int lines,int mask,int size){
        best[mask] = size;matches[size]++;
        for(int i=first;i<E;i++) {
            auto [p,l]=D.edge[i];
            if((points&(1<<p))==0 && (lines&(1<<l))==0)
                enumerate(i+1,points|(1<<p),lines|(1<<l),mask|(1<<i),size+1);
        }
    };
    enumerate(0,0,0,0,0);
    for(int i=0;i<E;i++)for(int s=0;s<N;s++)if(s&(1<<i))
        best[s]=max(best[s],best[s^(1<<i)]);
    for(int s=0;s<N;s++)if(best[s]!=D.matching_number[s])
        throw runtime_error("independent matching-number discrepancy");
    if(matches!=array<int,8>{1,21,168,644,1218,1050,336,24})
        throw runtime_error("matching enumeration discrepancy");
    cout<<"INDEPENDENT_MATCHING_DP_PASS 2097152 1,21,168,644,1218,1050,336,24\n";
    // Incidence axioms of the seven-point projective plane.
    for(int p=0;p<7;p++) {
        int degree=0;for(auto [q,l]:D.edge)if(q==p)degree++;
        if(degree!=3)throw runtime_error("point degree");
    }
    for(int p=0;p<7;p++)for(int q=p+1;q<7;q++) {
        int common=0;for(int l=0;l<7;l++){
            bool in_p=false,in_q=false;
            for(auto [a,b]:D.edge)if(b==l){if(a==p)in_p=true;if(a==q)in_q=true;}
            if(in_p&&in_q)common++;
        }
        if(common!=1)throw runtime_error("line incidence axiom");
    }
    cout<<"FANO_INCIDENCE_PASS\n";
}
struct Morse {
    int k;
    vector<int> mate;
    vector<uint8_t> remain;
    map<int,vector<int>> critical;
    long long facecount=0,incidences=0;
    Morse(const Data& D,int threshold,bool reverse):k(threshold),mate(N,-1),remain(N,0){
        for(int s=1;s<N;s++)if(D.matching_number[s]<k){remain[s]=1;facecount++;}
        vector<int> order(E);iota(order.begin(),order.end(),0);
        if(reverse)std::reverse(order.begin(),order.end());
        for(int i:order){int bit=1<<i;for(int s=1;s<N;s++)
            if(remain[s] && !(s&bit) && remain[s|bit]){
                int t=s|bit;remain[s]=remain[t]=0;mate[s]=t;mate[t]=s;
            }
        }
        for(int s=1;s<N;s++)if(remain[s])
            critical[__builtin_popcount((unsigned)s)-1].push_back(s);
        // Exact global acyclicity check on every incidence in the face poset:
        // paired cover relations point upward, all other cover relations downward.
        vector<uint8_t> indegree(N,0);
        for(int s=1;s<N;s++)if(D.matching_number[s]<k)
            for(int rest=s;rest;rest&=rest-1){
                int b=rest&-rest,t=s^b;
                if(!t)continue;
                incidences++;
                if(mate[t]==s)indegree[s]++;else indegree[t]++;
            }
        vector<int> q;q.reserve(facecount);
        for(int s=1;s<N;s++)if(D.matching_number[s]<k && !indegree[s])q.push_back(s);
        for(size_t h=0;h<q.size();h++){
            int s=q[h],t=mate[s];
            if(t>s && --indegree[t]==0)q.push_back(t);
            for(int rest=s;rest;rest&=rest-1){
                int b=rest&-rest,r=s^b;
                if(r && mate[r]!=s && --indegree[r]==0)q.push_back(r);
            }
        }
        if((long long)q.size()!=facecount)throw runtime_error("acyclicity failed");
    }
    vector<VLL> boundary(int upper_dimension)const{
        auto up_it=critical.find(upper_dimension),lo_it=critical.find(upper_dimension-1);
        if(up_it==critical.end()||lo_it==critical.end())return {};
        const auto &up=up_it->second,&lo=lo_it->second;const int m=lo.size();
        unordered_map<int,int> id;for(int j=0;j<m;j++)id[lo[j]]=j;
        unordered_map<int,VLL> memo;
        memo.reserve(8192);
        function<VLL(int)> reduce = [&](int s)->VLL{
            VLL z(m,0);
            auto found=id.find(s);
            if(found!=id.end()){z[found->second]=1;return z;}
            if(mate[s]<s)return z; // upper cell paired with one dimension below
            auto it=memo.find(s);if(it!=memo.end())return it->second;
            int t=mate[s];if(t<=s)throw runtime_error("unexpected match");
            int removed=t^s;
            int eps_s=__builtin_popcount((unsigned)(s&(removed-1)))%2?-1:1;
            for(int sub=t;sub;sub&=sub-1){
                int b=sub&-sub;if(b==removed)continue;
                int eps_r=__builtin_popcount((unsigned)(t&(b-1)))%2?-1:1;
                VLL v=reduce(t^b);
                for(int j=0;j<m;j++)z[j]-=eps_s*eps_r*v[j];
            }
            memo.emplace(s,z);
            return z;
        };
        vector<VLL> rows;
        for(int s:up){
            VLL z(m,0);
            for(int sub=s;sub;sub&=sub-1){
                int b=sub&-sub;
                int eps=__builtin_popcount((unsigned)(s&(b-1)))%2?-1:1;
                VLL v=reduce(s^b);
                for(int j=0;j<m;j++)z[j]+=eps*v[j];
            }
            rows.push_back(z);
        }
        return rows;
    }
};
long long det_small(vector<VLL> M){
    const int n=M.size();if(!n)return 1;
    if(n==1)return M[0][0];
    long long ans=0;
    for(int j=0;j<n;j++){
        vector<VLL> S;
        for(int r=1;r<n;r++){
            VLL row;
            for(int c=0;c<n;c++)if(c!=j)row.push_back(M[r][c]);
            S.push_back(row);
        }
        ans+=(j%2?-1:1)*M[0][j]*det_small(S);
    }
    return ans;
}
int main(){
 try{
    const Data D;
    independently_verify_matching_number(D);
    const long long face_expected[]={0,0,77,2331,33971,254240,963641,1844248};
    const long long inc_expected[]={0,0,126,8715,189231,1862259,8593830,18646131};
    const int sphere_expected[]={0,0,8,36,92,113,36,1};
    for(int k=2;k<=7;k++){
        Morse forward(D,k,false),backward(D,k,true);
        if(forward.facecount!=face_expected[k]||backward.facecount!=face_expected[k])throw runtime_error("face counts");
        if(forward.incidences!=inc_expected[k]||backward.incidences!=inc_expected[k])throw runtime_error("incidence counts");
        cout<<"MATCHING_ACYCLIC k="<<k<<" faces="<<forward.facecount<<" incidences="<<forward.incidences<<" fwd=";
        for(auto [d,v]:forward.critical)cout<<d<<":"<<v.size()<<",";
        cout<<" rev=";for(auto [d,v]:backward.critical)cout<<d<<":"<<v.size()<<",";cout<<"\n";
        if(k<=4||k==7){
            if(backward.critical.size()!=2 || backward.critical[0].size()!=1 ||
               (int)backward.critical[2*k-3].size()!=sphere_expected[k])
                throw runtime_error("unmatched cell dimensions for perfect wedge");
        } else if(k==5) {
            auto B=backward.boundary(8);
            if(B.size()!=1 || B[0].size()!=114 || B[0][11]!=-1)
                throw runtime_error("primitive 1-by-114 Morse boundary");
            cout<<"INTEGER_MORSE_BOUNDARY k=5 shape=1x114 pivot_col=11 pivot_value="<<B[0][11]<<"\n";
            auto BF=forward.boundary(8);
            if(BF.size()!=1 || BF[0].size()!=114 || BF[0][0]!=1)
                throw runtime_error("independent forward-order Morse boundary at k=5");
            cout<<"SECOND_MORSE_BOUNDARY k=5 shape=1x114 pivot_col=0 pivot_value="<<BF[0][0]<<"\n";
        }else if(k==6) {
            auto B=backward.boundary(10);
            if(B.size()!=5 || B[0].size()!=41)throw runtime_error("Morse boundary dimensions");
            const vector<int> piv={1,7,13,19,24};
            vector<VLL> M;
            for(auto &row:B){VLL x;for(int j:piv)x.push_back(row[j]);M.push_back(x);}
            auto det=det_small(M);
            if(abs(det)!=1)throw runtime_error("integer unimodular minor");
            cout<<"INTEGER_MORSE_BOUNDARY k=6 shape=5x41 pivot_cols=1,7,13,19,24 det="<<det<<"\n";
            auto BF=forward.boundary(10);
            if(BF.size()!=6 || BF[0].size()!=42)
                throw runtime_error("independent forward-order Morse boundary dimensions at k=6");
            const vector<int> piv2={2,7,13,38,32,23};
            vector<VLL> M2;
            for(auto &row:BF){VLL x;for(int j:piv2)x.push_back(row[j]);M2.push_back(x);}
            auto det2=det_small(M2);
            if(abs(det2)!=1)throw runtime_error("forward-order integral unimodular minor");
            cout<<"SECOND_MORSE_BOUNDARY k=6 shape=6x42 pivot_cols=2,7,13,38,32,23 det="<<det2<<"\n";
        }
    }
    // NM_8 is the full simplex, since H has a maximum matching of size seven.
    for(int s=0;s<N;s++)if(D.matching_number[s]>7)throw runtime_error("matching exceeds seven");
    cout<<"FINAL_HOMOTOPY_MULTIPLICITIES 8,36,92,113,36,1\n";
    cout<<"ALL_CHECKS_PASS\n";
 }catch(const exception&e){cerr<<"CHECK_FAILED "<<e.what()<<"\n";return 1;}
}
