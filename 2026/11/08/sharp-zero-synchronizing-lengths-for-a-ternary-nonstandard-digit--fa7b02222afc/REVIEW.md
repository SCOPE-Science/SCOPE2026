# Independent mathematical audit

## correctness

PASS

For D_k={0,1,3^{k+1}-1} and carry states K=[-M,0], M=(3^{k+1}-1)/2, iterating the carry equation gives zero synchronization iff [A-M,A] is contained in the unique ternary residue representative set T_l. The balanced ternary decomposition x=U+B V, B=3^{k+1}, shows that any run of consecutive values in T_l for l<=k+1 has length <=2: three consecutive low digits cannot keep the same -1 digit indicator V. The residue-1 elements of any represented run give r(l)<=3r(l-1)+2 and hence r(2k)<=3^k-1<M+1. At length 2k+1, balanced digit construction shows [BH-H,BH+M] contained in T_{2k+1}; A=3^k M+v, 0<=v<=H, gives at least H+1=(3^k+1)/2 shortest reset words. Independently enumerated carry-state image subsets for k=1..4: minimum lengths exactly 3,5,7,9, and verified construction on all states. Uniform symbolic lower and upper bounds, not finite enumeration, cover every integer k>=1.

## originality

PASS

An exact logarithmic-in-digit-height synchronization length for one natural infinite family, beyond Zhou’s qualitative gcd(digit set) synchronization criterion. Classical slow-reset automata and existing Resultary automata studies have other transition maps; no dominant exact count found. Residual risk of unindexed scalar complete-residue automata classifications remains.

## value

PASS

Determines a sharp reset length for an infinite naturally constructed family of nonstandard place-value systems, with matching combinatorial lower and constructive upper bounds, quantifying a genuine problem left beyond qualitative synchronization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
