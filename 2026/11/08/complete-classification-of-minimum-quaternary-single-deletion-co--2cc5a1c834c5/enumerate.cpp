// Independent six-subset census for quaternary single-deletion covers.
// C++17; every set of six distinct length-three words is considered once.
#include <cstdint>
#include <iostream>
using namespace std;

static unsigned int deletion_shadow(int i) {
    int a = i / 16, b = (i / 4) % 4, c = i % 4;
    return (1u << (4*a+b)) | (1u << (4*a+c)) | (1u << (4*b+c));
}
static void print_word(int i) {
    cout << i/16 << (i/4)%4 << i%4;
}
int main() {
    unsigned int s[64];
    for (int i=0;i<64;++i) s[i]=deletion_shadow(i);
    for (int a=0;a<59;++a) for (int b=a+1;b<60;++b)
      for (int c=b+1;c<61;++c) {
        unsigned int u=s[a]|s[b]|s[c];
        // Three remaining codewords can cover at most nine more ordered pairs.
        if (__builtin_popcount(u) < 7) continue;
        for (int d=c+1;d<62;++d) {
          unsigned int v=u|s[d];
          if (__builtin_popcount(v) < 10) continue;
          for (int e=d+1;e<63;++e) {
            unsigned int w=v|s[e];
            if (__builtin_popcount(w) < 13) continue;
            for (int f=e+1;f<64;++f) if ((w|s[f]) == 65535u) {
                const int code[6]={a,b,c,d,e,f};
                for (int j=0;j<6;++j) {
                    if (j) cout << ',';
                    print_word(code[j]);
                }
                cout << '\n';
            }
          }
        }
      }
}
