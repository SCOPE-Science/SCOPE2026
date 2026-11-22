#include <bits/stdc++.h>
using namespace std;
int O[16][16];
unordered_map<string, uint64_t> memo;
uint64_t rec(const string& state) {
 if(state.size()==1)return 1ull;
 auto it=memo.find(state);if(it!=memo.end())return it->second;
 int mx=-1,n=state.size();
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j)mx=max(mx,O[((unsigned char)state[i])&15][((unsigned char)state[j])>>4]);
 uint64_t bits=0;
 for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(i!=j&&O[((unsigned char)state[i])&15][((unsigned char)state[j])>>4]==mx){
 string t;for(int z=0;z<n;z++)if(z!=i&&z!=j)t.push_back(state[z]);
 t.push_back((char)(((unsigned char)state[i]&0xf0)|((unsigned char)state[j]&0x0f)));
 sort(t.begin(),t.end(),[](char a,char b){return (unsigned char)a<(unsigned char)b;});
 bits |= (rec(t)<<mx);
 }
 memo[state]=bits;return bits;
}
int main(){vector<string> a;for(int i=0;i<16;i++){string x;for(int bit=3;bit>=0;bit--)x.push_back('0'+((i>>bit)&1));a.push_back(x);}
 for(int i=0;i<16;i++)for(int j=0;j<16;j++){O[i][j]=0;for(int k=1;k<=3;k++)if(a[i].substr(4-k)==a[j].substr(0,k))O[i][j]=k;}
 string start;for(int i=0;i<16;i++)start.push_back(char(i*17));
 uint64_t bits=rec(start);
 cout << "states="<<memo.size()<< " lengths=";
 for(int saved=0;saved<64;saved++)if((bits>>saved)&1)cout << 64-saved << ",";
 cout<<"\n"; cout.flush();_Exit(0);
}
