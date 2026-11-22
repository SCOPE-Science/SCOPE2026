// Independent exact eight-edge census. Uses pairwise distinguishability,
// not partition refinement, to test minimality of the subset automaton.
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
using namespace std;
int main() {
  uint64_t count=0, full=0, minimal=0;uint64_t finals[16]={};
  for(uint64_t w=0;w<(1ull<<32);++w) {
    if(__builtin_popcountll(w)!=8)continue;
    ++count;
    array<array<uint8_t,16>,2> next{};
    for(int c=0;c<2;c++) {
      int edges[4];for(int i=0;i<4;i++)edges[i]=(w>>(16*c+4*i))&15;
      for(int s=0;s<16;s++)for(int j=0;j<4;j++)if(s&(1<<j))next[c][s]|=edges[j];
    }
    uint16_t visited=2; int q[16]={1}, size=1;
    for(int k=0;k<size;k++)for(int c=0;c<2;c++){
      int v=next[c][q[k]];
      if(!(visited&(1<<v))){visited |= 1<<v;q[size++]=v;}
    }
    if(size!=16)continue;
    full++;
    for(int F=1;F<16;F++){
      bool different[16][16]={};
      for(int i=0;i<16;i++)for(int j=0;j<16;j++)
        different[i][j] = bool(i&F)!=bool(j&F);
      bool changed=true;
      while(changed){changed=false;
        for(int i=0;i<16;i++)for(int j=i+1;j<16;j++)if(!different[i][j]){
          bool can = different[next[0][i]][next[0][j]] || different[next[1][i]][next[1][j]];
          if(can){different[i][j]=different[j][i]=true;changed=true;}
        }
      }
      bool all=true;
      for(int i=0;i<16;i++)for(int j=i+1;j<16;j++)if(!different[i][j])all=false;
      if(all){minimal++;finals[F]++;}
    }
  }
  cout << "EIGHT_EDGE_TABLES " << count << "\nFULL_REACHABLE " << full << "\nMINIMAL16 " << minimal << "\n";
  for(int f=1;f<16;f++)cout << f << " " << finals[f] << "\n";
  assert(count==10518300 && full==5808 && minimal==56544);
  cout << "CHECK PASS\n";
}
