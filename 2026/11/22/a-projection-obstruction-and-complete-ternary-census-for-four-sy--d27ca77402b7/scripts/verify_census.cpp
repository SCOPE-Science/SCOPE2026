// Independent C++17 enumeration of optimal ternary four-letter comma-free codes.
// Exhaustive increasing-index search, testing every ordered splicing triple.
#include <array>
#include <algorithm>
#include <cassert>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>
using namespace std;
using Word=array<int,4>;
vector<Word> words;
vector<vector<int>> adj;
array<long long, 82> histogram{};
vector<vector<int>> maxima;
string splice(const Word &a,const Word&b,int j) {
    string s;
    for (int i=j;i<4;i++)s+=char('0'+a[i]);
    for (int i=0;i<j;i++)s+=char('0'+b[i]);
    return s;
}
string str(Word w) { string s; for(int x:w)s+=char('0'+x); return s; }
bool valid(const vector<int>& c) {
    set<string> names;
    for(int i:c)names.insert(str(words[i]));
    for(int i:c)for(int j:c)for(int shift=1;shift<=3;shift++)
        if(names.count(splice(words[i],words[j],shift)))return false;
    return true;
}
void recurse(vector<int>& c, const vector<int>& candidates) {
    if (!c.empty()) {
        assert(valid(c));
        histogram[c.size()]++;
        if(c.size()==5)maxima.push_back(c);
    }
    for(int z=0;z<(int)candidates.size();z++) {
        int a=candidates[z]; c.push_back(a);
        if (valid(c)) {
            vector<int> rem;
            for(int y=z+1;y<(int)candidates.size();y++)
                if(adj[a][candidates[y]])rem.push_back(candidates[y]);
            recurse(c,rem);
        }
        c.pop_back();
    }
}
int main(){
    for(int a=0;a<3;a++)for(int b=0;b<3;b++)for(int c=0;c<3;c++)for(int d=0;d<3;d++) {
        Word w{a,b,c,d};
        if (splice(w,w,1)==str(w)||splice(w,w,2)==str(w)||splice(w,w,3)==str(w))continue;
        words.push_back(w);
    }
    int n=words.size(); assert(n==72);
    adj.assign(n,vector<int>(n));
    int edges=0;
    for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){
        int d=0;for(int t=0;t<4;t++)d+=(words[i][t]!=words[j][t]);
        if(d>=3){adj[i][j]=adj[j][i]=1;edges++;}
    }
    vector<int> c; vector<int> cand(n);iota(cand.begin(),cand.end(),0);
    recurse(c,cand);
    assert(histogram[5]==1548 && histogram[6]==0);
    set<string> codebooks;
    for(const auto& code:maxima){
        string s;for(int i:code)s+=str(words[i]);
        codebooks.insert(s);
    }
    vector<int> p={0,1,2}; set<string> representatives;
    for(const auto& code:maxima){
        string mn(100,'9');
        do {
            for(int rev=0;rev<2;rev++){
                vector<string> vv;
                for(int i:code){string s;for(int j=0;j<4;j++)s+=char('0'+p[words[i][rev?3-j:j]]);vv.push_back(s);}
                sort(vv.begin(),vv.end());string joined;for(auto &s:vv)joined+=s;
                mn=min(mn,joined);
            }
        }while(next_permutation(p.begin(),p.end()));
        representatives.insert(mn);
        p={0,1,2};
    }
    assert(representatives.size()==129);
    cout << "candidate_words "<<n<<" edges "<<edges<<"\n";
    cout << "valid_by_size";
    for(int i=1;i<=7;i++) if(histogram[i])cout<<" "<<i<<":"<<histogram[i];
    cout << "\noptimal "<<maxima.size()<<" orbits "<<representatives.size()<<"\n";
    return 0;
}
