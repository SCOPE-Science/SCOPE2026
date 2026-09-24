/* search.c — greedy DFS with backtracking for binary 2-abelian-cube-free words.
 *
 * Check: suffix ending at n, arm length m: blocks A=[n-3m,n-2m),B=[n-2m,n-m),C=[n-m,n).
 * 2-abelian equivalent iff first letters equal, last letters equal, digram counts equal.
 * Digram count in [l,r) = P[r-1]-P[l] with P[i]=#pairs starting at j<i.
 *
 * Usage: ./search TARGET SEED [OUTFILE] [LOGFILE]
 * Exits 0 with word file on reaching TARGET; logs obstructions (backtrack events).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static unsigned char *w;
static int *P[4];
static int N;

/* xorshift64 PRNG for per-position shuffle */
static unsigned long long rng_state;
static unsigned rnd(void){ rng_state^=rng_state<<13; rng_state^=rng_state>>7; rng_state^=rng_state<<17; return (unsigned)(rng_state>>32); }

/* Storage convention: P[k][i] = #{pairs starting at j < i} restricted to pairs
   fully inside the CURRENT word. When appending w[pos]=b (pos>=1), the pair
   starting at pos-1 becomes known: add to column (pos-1)+1 = pos. So we update
   P[k][pos], and set P[k][pos+1]=P[k][pos] (no pair starts at pos yet, since
   w[pos+1] is unknown). Column P[*][pos+1] is a placeholder until next append.
   Digram count in [l,r) (pairs starting in [l,r-1), all with j+1<r<=n so known)
   = P[k][r-1]-P[k][l]. */
static int creates_cube(int n){
    int m;
    for(m=1;m*3<=n;m++){
        if(!(w[n-3*m]==w[n-2*m] && w[n-2*m]==w[n-m])) continue;
        if(!(w[n-2*m-1]==w[n-m-1] && w[n-m-1]==w[n-1])) continue;
        if(m==1) return 1;
        if(m==2){
            /* single interior digram per block: compare directly (prefix sums
               would read placeholder columns) */
            int d0=(w[n-3*m]<<1)|w[n-3*m+1];
            int d1=(w[n-2*m]<<1)|w[n-2*m+1];
            int d2=(w[n-m]<<1)|w[n-m+1];
            if(d0==d1 && d1==d2) return m;
            continue;
        }
        int k;
        for(k=0;k<4;k++){
            int ca = P[k][n-2*m-1]-P[k][n-3*m];
            int cb = P[k][n-m-1]-P[k][n-2*m];
            if(ca!=cb) break;
            int cc = P[k][n-1]-P[k][n-m];
            if(cb!=cc) break;
        }
        if(k==4) return m;
    }
    return 0;
}

int main(int argc,char**argv){
    if(argc<3){fprintf(stderr,"usage: %s TARGET SEED [OUT] [OBSLOG]\n",argv[0]);return 2;}
    int target=atoi(argv[1]);
    unsigned long long seed=strtoull(argv[2],0,10);
    const char* out=argc>3?argv[3]:"word.txt";
    const char* obslog=argc>4?argv[4]:"obstructions.csv";
    N=target;
    w=malloc(N); if(!w){perror("malloc");return 1;}
    for(int k=0;k<4;k++){P[k]=calloc(N+1,sizeof(int)); if(!P[k]){perror("calloc");return 1;}}
    /* tried-bit stacks: order[pos][2], next idx ptr */
    unsigned char *ord0=malloc(N), *ord1=malloc(N), *nxt=malloc(N);
    if(!ord0||!ord1||!nxt){perror("malloc2");return 1;}
    rng_state = seed ? seed : 0x9e3779b97f4a7c15ULL;
    /* prefix counts P[k][0]=0; maintain P[k][i] for current length */
    int pos=0;          /* current length */
    long backtracks=0, nodes=0;
    long *obs_pos=NULL; int *obs_m=NULL; size_t obs_cap=0, obs_n=0;
    FILE *flog=fopen(obslog,"w");
    if(!flog){perror("fopen log");return 1;}
    fprintf(flog,"event,pos,m,detail\n");
    clock_t t0=clock();
    /* init orders lazily */
    memset(nxt,0,N);
    /* NOTE: prefix columns P[k][i] are maintained for the CURRENT path only.
       Convention: P[k][i] = #{pairs starting at j<i} among the current word.
       Appending w[pos]=b reveals the pair starting at pos-1 (if pos>=1).
       Column pos currently holds a placeholder (= value copied when length was
       pos); we add the new pair into column pos, then set column pos+1 = column
       pos as the new placeholder. On backtrack, columns > pos are stale but are
       always repaired in order when positions are retried (column pos is
       recomputed as placeholder-copy + ремонта? NO — see below).
       STALENESS SUBTLETY: after backtracking from length L to pos<L, column pos
       already contains the pair starting at pos-1 (added when pos was first
       reached). When we retry pos with the second bit, we must NOT add again:
       the pair (w[pos-1], new_b) differs from the stale one. Fix: before adding,
       subtract the stale pair's contribution, i.e. recompute column pos from
       column pos-1. We do that explicitly: save the stale pair code from the
       previous occupant w[pos] (still in w[] until overwritten) and correct.
       Simplest correct repair: P[k][pos] = P[k][pos-1] + (k == newcode), using
       w[pos-1] (shared prefix, valid) and new b. This overwrites any stale
       content. For pos=0 just copy zeros. */
    for(int i=0;i<N;i++){ /* pre-generate shuffle per position deterministically */
        unsigned r=rnd();
        if(r&1){ord0[i]=0;ord1[i]=1;}else{ord0[i]=1;ord1[i]=0;}
    }
    while(pos<target){
        if(nxt[pos]>=2){ /* both bits exhausted (returned via backtrack): go deeper back */
            nxt[pos]=0;
            if(pos==0){fprintf(stderr,"FAILED at root\n");break;}
            backtracks++;
            fprintf(flog,"backtrack,%d,0,nodes=%ld\n",pos,nodes);
            pos--;
            continue;
        }
        unsigned char b = (nxt[pos]==0)?ord0[pos]:ord1[pos];
        /* place w[pos]=b; repair column pos from the trusted column pos-1
           (overwrites any stale backtrack content), then set placeholder. */
        w[pos]=b;
        if(pos>=1){
            int c=(w[pos-1]<<1)|b;
            for(int k=0;k<4;k++) P[k][pos]=P[k][pos-1]+(k==c);
            for(int k=0;k<4;k++) P[k][pos+1]=P[k][pos];
        }else{
            for(int k=0;k<4;k++) P[k][pos+1]=P[k][pos];
        }
        nodes++;
        int m=creates_cube(pos+1);
        if(m){
            /* obstruction: bit b at pos would close a suffix 2-abelian cube of
               arm m. Log pos, m, bit, plus the cube's digram signature' of the
               would-be third block C=[pos+1-m,pos+1): its first/last letters
               and counts of 00,01,10,11 — the data a future constructor needs
               to understand what made extension fail here. */
            int l3 = pos+1-m;
            int first3 = w[l3], last3 = w[pos];
            int cc0 = P[0][pos]-P[0][l3], cc1 = P[1][pos]-P[1][l3];
            int cc2 = P[2][pos]-P[2][l3], cc3 = P[3][pos]-P[3][l3];
            if(obs_n<10000000){
                fprintf(flog,"block,%d,%d,bit=%d first3=%d last3=%d sig=%d-%d-%d-%d\n",pos,m,b,first3,last3,cc0,cc1,cc2,cc3);
            }
            nxt[pos]++;
            /* retry same pos with second bit on next iteration (guard at top
               backtracks further only after second bit also fails) */
        }else{
            /* accept b: consume it so a later backtrack tries the alternative */
            nxt[pos]++;
            pos++;
            if(pos%20000==0){
                double el=(double)(clock()-t0)/CLOCKS_PER_SEC;
                fprintf(stderr,"len %d backtracks %ld nodes %ld t=%.1fs\n",pos,backtracks,nodes,el);
            }
        }
    }
    double el=(double)(clock()-t0)/CLOCKS_PER_SEC;
    fprintf(stderr,"final len %d backtracks %ld nodes %ld t=%.1fs\n",pos,backtracks,nodes,el);
    fprintf(flog,"summary,%d,0,backtracks=%ld nodes=%ld time=%.2f\n",pos,backtracks,nodes,el);
    fclose(flog);
    if(pos>=target){
        FILE *f=fopen(out,"w");
        if(!f){perror("fopen out");return 1;}
        for(int i=0;i<target;i++) fputc('0'+w[i],f);
        fputc('\n',f);
        fclose(f);
    }
    return (pos>=target)?0:3;
}
