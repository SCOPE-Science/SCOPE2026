# Independent mathematical audit

## correctness

PASS

Read the exact trace-class weighted Schur norm reduction in Levene Theorem 3.8, match its normalized branch populations to 13 rational symmetric tridiagonal blocks A_+, A_- and A_l (l=1..11). Recomputed the supplied 13 integer dual reflection matrices with independent BigInt rational fraction arithmetic; every H_B is symmetric and max row-sum norm of H_B²-I is 32867079/100000000000000 <2/100000. Thus ||H_B||op≤1+1/100000 and trace duality gives ||B||1≥tr(H_B B)/(1+1/100000). Independently evaluated all traces and strict rational comparison T>20029/10000*(1+1/100000)*S, yielding certified lower approx 2.002944900198419. Core norm is 2(n-1)/n. For all n>=15, induced subgraph compression inherits the strict bound. No exact norm or optimality assertion.

## originality

PASS

Previously published results already establish productivity of all crown cores n>=13 and even n>=12, using much taller or more highly branched trees. Their larger family coverage DOES cover the generic productivity corollary here. However, those facts do not imply the specific 1000-branch, height-12 strict norm bound >2.0029. Levene Section 6 explicitly left that exact parameter instance as an unproved numerical observation. The exact rational witness resolves that distinct well-motivated precise statement; originality PASS is limited to the fixed quantitative certificate, not the family productivity slogan.

## value

PASS

The precise finite height-12 thousand-ary certificate resolves an explicit unverified numerical example in the motivating primary paper and quantifies its margin above two. This narrowly targeted exact fact has mathematical value independent of now-known taller-tree generic productivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
