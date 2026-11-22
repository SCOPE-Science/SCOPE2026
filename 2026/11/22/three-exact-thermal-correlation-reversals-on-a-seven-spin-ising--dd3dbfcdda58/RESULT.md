# Three exact thermal correlation reversals on a seven-spin Ising ring

## Finding

The zero-field signed nearest-neighbor Ising model on the simple cycle \(C_7\) has a choice of **fixed nonzero integer exchange couplings** for which one pair correlation changes sign **exactly three times** as inverse temperature varies over \((0,\infty)\). More precisely, on the cyclic edges \((0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(6,0)\), respectively, take
\[
 (J_{01},J_{12},J_{23},J_{34},J_{45},J_{56},J_{60})=(2,6,8,16,15,3,-3).
\]
Then \(\langle\sigma_0\sigma_3\rangle_\beta\) has sign pattern **positive, negative, positive, negative**, separated by exactly three simple positive-inverse-temperature zeros. For every larger simple cycle \(C_n\), \(n\ge7\), some finite nonzero real edge couplings give **at least three** reversals. No assertion is made that seven is the minimum order allowing three reversals.

## Assumptions and scope

Spins \(\sigma_v\in\{-1,+1\}\) have Hamiltonian \(H=-\sum_{e=\{i,j\}}J_e\sigma_i\sigma_j\), zero field and Gibbs law proportional to \(\exp(-\beta H)\), \(\beta>0\). In zero field the mean of each spin vanishes; the two-point expectation is also its covariance. The bonds are fixed while temperature varies, and their absolute magnitudes are not assumed equal. A reversal means a genuine switch between positive and negative correlations at an isolated zero, not a thermodynamic phase transition.

## Proof

**Two-arc formula.** The two paths between vertices \(0\) and \(3\) have positive-magnitude products
\[
 A(\beta)=\tanh(2\beta)\tanh(6\beta)\tanh(8\beta),\qquad
 B(\beta)=\tanh^2(3\beta)\tanh(15\beta)\tanh(16\beta).
\]
Exactly one bond has negative sign, on the second arc. Expanding \(e^{\beta J\sigma_i\sigma_j}=\cosh(\beta J)(1+\sigma_i\sigma_j\tanh(\beta J))\) and summing spins shows
\[
 C(\beta):=\langle\sigma_0\sigma_3\rangle_\beta=\frac{A(\beta)-B(\beta)}{1-A(\beta)B(\beta)}.
\]
The denominator is positive since \(0<A,B<1\).

**Exact polynomial and root count.** Let \(x=\tanh\beta\in(0,1)\), and define integer polynomials for every positive integer \(k\):
\[
 N_k(x)=\sum_{j\text{ odd}}\binom kj x^j,\qquad
 D_k(x)=\sum_{j\text{ even}}\binom kj x^j.
\]
Then \(\tanh(k\beta)=N_k(x)/D_k(x)\), and all \(D_k(x)>0\) on \((0,1)\). Put \(\mathcal A=(2,6,8)\), \(\mathcal B=(3,3,15,16)\), and
\[
 F(x)=\left(\prod_{a\in\mathcal A}N_a(x)\right)
       \left(\prod_{b\in\mathcal B}D_b(x)\right)
       -\left(\prod_{b\in\mathcal B}N_b(x)\right)
       \left(\prod_{a\in\mathcal A}D_a(x)\right).
\]
This polynomial has degree \(52\), and its first three coefficients vanish; define \(G(x)=F(x)/x^3\), of degree \(49\). The transformation \(y=x/(1-x)\) sends \((0,1)\) bijectively to \((0,\infty)\). Direct exact integer binomial convolution gives
\[
 Q(y)=(1+y)^{49}G\left(\frac y{1+y}\right),
\]
whose nonzero coefficients, read in ascending degree, have precisely three sign variations. The full algorithm to construct \(Q\) and count its sign variations appears in `verify.py`; it uses only integer additions, products, and binomial coefficients. Descartes' rule bounds the number of roots of \(Q\) on \((0,\infty)\), counted with multiplicity, by three.

At the four rational points \(x=1/20,\ 1/10,\ 1/6,\ 1/3\), exact rational arithmetic establishes the successive signs of \(F(x)\) to be \(+,-,+,-\). Since the denominator and \(x^3\) are positive, continuity forces a different sign-changing zero in each of the three intervening intervals. The Descartes bound shows that these are **all** the zeros on \((0,1)\), each simple. The continuous bijection \(\beta=\operatorname{arctanh}x\) preserves this order and proves the exact thermal sign pattern.

**Extension to every longer cycle.** Replace any one original bond by a series path with the original exchange on one edge and any additional positive bonds of common strength \(M\). For any fixed \(\beta>0\), the corresponding arc product gains a factor \(\tanh(M\beta)\) for each added edge, tending to one as \(M\to\infty\). The zero-field two-arc correlation therefore converges at each of the four rational witness temperatures to the original correlation. For every fixed desired cycle length, all four strict signs persist for sufficiently large but finite \(M\), yielding at least three reversals by continuity. No claim of exactly three reversals is made for these longer cycles.

## Verification

Run `python3 verify.py` using the standard library. The program constructs \(F\) by exact integer convolution, computes the binomial transform \(Q\) and checks exactly three coefficient sign variations. It verifies the four alternating rational signs and separately enumerates all \(2^7\) spin configurations with **exact rational relative Boltzmann weights** at each of those four points, confirming the two-arc formula without using its derivation. Its successful output is `SEVEN_CYCLE_THREE_REVERSALS_CERTIFIED 3 4 exact enumerations`. The all-length extension is proved by a limiting argument, not by finitely many tests.

## Relationship to prior work

Tanaka and Miyashita, arXiv:1003.0200, Section II.1, analyze a decorated frustrated Ising bond exhibiting a single temperature-induced correlation sign reversal. Kobayashi, Fukumoto and Oguchi, arXiv:0901.3181, study frustrated diamond hierarchical Ising structures and thermal correlations, not this finite-cycle zero count. A published 2026 result, *Two thermal correlation reversals in a frustrated five-path Ising network*, establishes exactly two reversals in an equal-absolute-bond-magnitude network. An earlier exact signed-cycle result establishes a sharp five-site witness for **two** reversals, and examples on all larger cycles. Neither of these results implies the present **three** reversals or its exhaustive root-count certificate. The elementary two-path high-temperature expansion is standard and is not claimed as new.

## Limitations

The construction demonstrates three reversals at seven sites, not their minimal possible graph order. The larger-cycle extension guarantees at least three rather than exactly three roots. All statements concern fixed, spatially nonuniform signed couplings at zero field, with no disorder averaging or thermodynamic transition. Earlier unindexed results or a stronger general theorem on signed cyclic Ising correlations could subsume the seven-site example; independent historical review remains necessary.

## References

1. S. Tanaka and S. Miyashita, *Non-monotonic Dynamics in Frustrated Ising Model with Time-Dependent Transverse Field*, arXiv:1003.0200, first public 2010-02-28. https://arxiv.org/abs/1003.0200
2. H. Kobayashi, Y. Fukumoto, A. Oguchi, *Frustrated Ising Model on a Diamond Hierarchical Lattice*, arXiv:0901.3181, first public 2009-01-21. https://arxiv.org/abs/0901.3181
3. *Two thermal correlation reversals in a frustrated five-path Ising network*, public result, 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-two-thermal-correlation-reversals-in-a-frustrated-five-path-isin--5f20f141402e
