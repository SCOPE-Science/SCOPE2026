# Independent mathematical audit

## correctness

PASS

For odd n, maximality forces M=Phi(n) even and not a power of two (the competitor 2M or 3*2^(r-1) has equal totient). Writing M=2^r∏q_i^{e_i} gives v2(phi(M)) >= r-1+s <=v2(2n)=1; thus r=s=1, M=2q^e. Consequently M/phi(M)=2q/(q-1)<=3, equality only if q=3, and phi(M)<=2n forces M<=6n. Equality implies M=2*3^e=6n and n=3^(e-1); conversely phi(2*3^(a+1))=2*3^a. Includes n=1. Exact independent maxima checked for 300 odd inputs n<=599.

## originality

FAIL

The claimed iff is a **routine equality-case consequence of an already published stronger upper-bound proof**. Ozeki Proposition 5.2 proves Phi(n)<=6n for all odd n; its proof already shows the extremal M cannot be a power of two, derives r+s<=v2(n)+2, and on odd inputs forces M=2q^e. Ozeki’s ratio/product inequality immediately requires q=3 if M=6n, whence n=3^(e-1); Pelizzari–Punch explicitly give the infinite power-of-three equality family. The new proof reproduces these inputs and merely writes down the omitted equality sentence. No independent theorem survives prior implication, notwithstanding true correctness.

## value

FAIL

The equality locus is a natural question but this particular classification is a two-line equality check on Ozeki’s published odd-bound argument, combined with Pelizzari–Punch’s explicit sharp family. It introduces no new structural lemma, obstruction, classification technique, or nontrivial numerical invariant independent of those sources; scientific correctness and reproducibility do not restore value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
