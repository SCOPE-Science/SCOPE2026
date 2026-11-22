# Independent mathematical audit

## correctness

PASS

PASS. Each connected simple n-vertex graph with exactly n edges consists of one unique undirected simple cycle plus a forest rooted at its cycle vertices. Choosing k cycle vertices and applying all-minors matrix-tree yields U_n=(n−1)!/2·∑_{j=0}^{n−3}n^j/j!; exact cases U_3=1,U_4=15,U_5=222,U_6=3660,U_7=68295. For n≡3 mod4 the terminal rooted-forest summand is odd and all preceding summands even (their integer combinatorial factors carry n−3), so U_n odd and every ±1 Walsh coefficient W_n(S) is odd and nonzero. For arbitrary signed edge mask S, expand over unique cycles C and use signed net Laplacian L_σ to obtain W_n(S)=∑_C(∏_{e∈C}σ_e)det L_σ[[n]outsideV(C)]; this is an exact identity. Inspected source verify.cpp builds unicyclic families independently by connected n-edge masks and cycle-plus-rooted-forest parent maps, checks equality through n=7; for n=5,6 performs 1024/32768 full signed Walsh butterflies, direct signed summation for every coefficient, and independent signed forest determinants. Separately independently enumerated all n5/n6 connected edge masks and recomputed Walsh spectra, obtaining n5 212 zeros and rank812, zero weights 1:10,5:192,9:10; n6 1200 zeros and rank31568, zero weights 4:420,7:180,8:180,11:420, minimum nonzero gap 4. The zero four-edge supports at n6 are exactly degree multiset (0,1,1,2,2,2), i.e. P5⊔K1 (360) or triangle⊔edge⊔K1 (60); all lower weights nonzero. The Fourier-support indicator inverse Walsh transform has absolute numerator sums 8104 over 1024 and 580928 over32768, proving sharp min l1/l∞ endpoint projection constants 1013/128 and 9077/512 by translation averaging arbitrary projections onto the range. Exact complete finite census is exhaustive, not a claim about uncomputed higher n.

## originality

PASS

Best-of-knowledge original residual scientific increment after explicitly excluding known prior coverage; exact historical priority is not certified. Material compared at the statement and implication level; finite or generic overlaps are acknowledged.

## value

PASS

PASS. The small natural labelled-unicyclic ensemble has a nontrivial first zero-support boundary at four negative edges, an exhaustive graph-isomorphism classification of those first resonances, and exact optimal inverse and endpoint-projection constants. These are precise recoverability invariants a future graph-Fourier analyst could need, and the separate all-n parity guarantee gives structural context; the finite census need not be a general all-n spectrum theorem to be valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
