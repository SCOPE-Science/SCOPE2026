# A five-point phase-alphabet reversal for full-spark cyclic Gabor frames

## Finding
Let \(\omega=e^{2\pi i/5}\), and for \(q\in\{1,2,3,4,5\}\) let \(\mu_q=\{e^{2\pi i j/q}:0\le j<q\}\). For a window \(g\in\mu_q^5\), form the unnormalized \(5\)-by-\(25\) cyclic Gabor matrix
\[
A_g[t,5x+y]=\omega^{yt}g(t-x),\qquad t,x,y\in\mathbb Z/5\mathbb Z.
\]
Call \(g\) *full spark* when every \(5\)-column restriction of \(A_g\) is invertible over \(\mathbb C\). Equivalently, arbitrary five retained Gabor atoms recover every signal, even following twenty erasures.

**Exact classification.** The number of full-spark windows with \(g(0)=1\), among all \(q^4\) normalized \(q\)-phase windows, is:

| Phase-alphabet size \(q\) | All normalized windows | Full spark | Not full spark |
|---:|---:|---:|---:|
| 1 | 1 | 0 | 1 |
| 2 | 16 | 5 | 11 |
| 3 | 81 | 60 | 21 |
| 4 | 256 | 205 | 51 |
| 5 | 625 | 0 | 625 |

Removing normalization multiplies each full-spark count by \(q\); the respective numbers of full-spark indexed windows are \(0,10,180,820,0\).

More precisely, for binary phases \(\mu_2=\{1,-1\}\), the full-spark windows are *exactly* the ten length-five sign words with a single sign different from the other four. The normalized five words have exponents \((0,1,0,0,0)\), \((0,0,1,0,0)\), \((0,0,0,1,0)\), \((0,0,0,0,1)\), and \((0,1,1,1,1)\) for \(g(t)=(-1)^{a_t}\). In particular, \((1,-1,1,1,1)\) generates a full-spark Gabor frame, whereas **no** five-root phase word does. The alphabet index is nonmonotone: the sets \(\mu_q\) are not nested for different \(q\).

## Assumptions and scope
The underlying group is precisely \(\mathbb Z/5\mathbb Z\); phase coefficients are *exact* complex roots of unity of order dividing \(q\). The full Gabor system includes all 25 ordered time-frequency shifts, with the columns ordered as \(5x+y\). Linear independence is over \(\mathbb C\). The scalar phase of the window does not affect spark, so multiplying a window by \(g(0)^{-1}\) identifies each scalar-phase orbit with one normalized word \(g(0)=1\); each orbit has exactly \(q\) indexed words. The classification does not concern general complex windows, higher cyclic orders, or phase alphabets larger than five.

## Proof
**Exact cyclotomic zero oracle.** Fix one of the five alphabets, and let \(L=\operatorname{lcm}(5,q)\). Every determinant \(\Delta\) of a five-column submatrix of \(A_g\) belongs to the integer ring \(\mathbb Z[\zeta_L]\), where \(\zeta_L=e^{2\pi i/L}\). Its field degree \(\varphi(L)\) is at most eight. All entries of every Galois conjugate of this submatrix have modulus one. Hadamard's inequality therefore gives
\[
|\sigma(\Delta)|\le 5^{5/2},\qquad
|N_{\mathbb Q(\zeta_L)/\mathbb Q}(\Delta)|\le 5^{5\varphi(L)/2}\le 5^{20}=95{,}367{,}431{,}640{,}625.
\]
The norm is an integer. Take the distinct primes \(p_1=10{,}000{,}141\) and \(p_2=10{,}000{,}261\), whose product is \(100{,}004{,}020{,}036{,}801>5^{20}\). Each is congruent to one modulo 60. Primitive 60th roots in their respective prime fields are \(11^{(p_1-1)/60}\) and \(2^{(p_2-1)/60}\); the accompanying code verifies primality and the exact multiplicative order. Substituting the induced primitive \(L\)-th root defines a ring map \(\mathbb Z[\zeta_L]\to\mathbb F_{p_i}\).

A nonzero modular determinant proves \(\Delta\ne0\). Conversely, if a determinant evaluates to zero modulo **both** primes, each prime divides its integer field norm (the modular root defines a prime ideal of residue degree one). Since the product exceeds the absolute norm bound, the norm must be zero, hence \(\Delta=0\) over \(\mathbb C\). Thus the pair of modular determinant tests decides complex singularity exactly, without numerical thresholds. No assumption of irreducibility of the Gabor determinant is used.

**Exhaustive finite classification.** Write \(g(t)=e^{2\pi i a_t/q}\) with \(a_0=0\) and each \(a_t\in\{0,\ldots,q-1\}\). The checker `artifacts/gabor_phase_census.cpp` enumerates every \(q^4\) such word and each of the \(\binom{25}{5}=53{,}130\) increasing five-column selections. For any window it stops at the first pair-of-primes certified zero determinant, recording that five-column witness in `artifacts/witnesses.tsv`; only windows having all minors nonzero are counted full spark. The exhaustive counters give the table above. All 709 deficient normalized windows have stored singular witnesses, including all 625 fifth-root windows; the complement comprises 270 full-spark normalized words across the other alphabets. The five surviving normalized sign words are exactly those displayed, proving the binary characterization.

**Independent integer check of both extremes.** A second implementation, `artifacts/symbolic_cyclotomic_check.cpp`, uses no finite fields. It directly expands each determinant into its 120 signed permutation terms. For fifth-root windows the result is \(\sum_{j=0}^4c_j\omega^j\) with integer \(c_j\), and it vanishes if and only if all five \(c_j\) are equal, because \(1+X+X^2+X^3+X^4\) is the minimal polynomial of \(\omega\). For binary windows, the signs are incorporated as integer \(-1\) multipliers. This independently yields exactly five full-spark normalized binary windows and zero full-spark normalized fifth-root windows, with the same exhaustive minor-check counts. The intermediate ternary and quaternary totals are certified by the two-prime algebraic norm argument above; a second symbolic implementation is not claimed for them.

## Verification
The self-contained package includes all of the following: `artifacts/gabor_phase_census.cpp`, `artifacts/symbolic_cyclotomic_check.cpp`, `artifacts/witnesses.tsv`, and exact run outputs `artifacts/census.out`, `artifacts/symbolic.out`. From the package directory, build using `g++ -O2 -std=c++17 artifacts/gabor_phase_census.cpp -o census` and run `./census reproduced.tsv`, then use `cmp reproduced.tsv artifacts/witnesses.tsv` to compare the 709 stored certificates. Compile `g++ -O3 -std=c++17 artifacts/symbolic_cyclotomic_check.cpp -o symbolic`, run `./symbolic`, and compare output to `artifacts/symbolic.out`. The numerical engine performs only modular integer arithmetic; the independent extreme-case checker performs only signed integer arithmetic. Each selected determinant has a rigorous all-embeddings norm bound, so these exhaustive finite computations prove the complex claims rather than merely suggest them.

## Relationship to prior work
Lawrence, Pfander and Walnut established generic full spark for cyclic groups of prime order, including five, but their generic-density theorem does not choose a restricted phase alphabet and does not imply the stated quantitative counts or the fifth-root obstruction. Malikiosis later constructed full-spark Gabor windows at general cyclic dimensions using other high-order cyclotomic phases; those constructions also do not determine this short-alphabet census. His separate spark-deficiency theorem for noncyclic groups does not apply to the cyclic five-group.

Existing exact studies of fifth-root cyclic *cross-short-time Fourier transform support* concern the number of nonzero transform entries when **both** input signals have fifth-root coefficients. Full spark instead requires control of five-atom dependencies, equivalently every nonzero *arbitrary complex* input signal; the restricted cross-transform support distribution does not imply the present result. Similarly, finite real sign-line general-position classifications do not cover all 25 complex-modulated cyclic Gabor vectors. The present contribution is the exact phase-alphabet full-spark classification and the binary-versus-pentaphase reversal.

## Limitations
The result is a finite exact census only for five time samples and alphabet sizes one through five; it does not assert a pattern for other prime lengths or phase orders, nor does it quantify smallest positive singular values or noise robustness beyond full-spark erasure recoverability. The independent signed-determinant implementation covers the binary and fifth-root extremes, whereas the intermediate counts rely on the fully verified two-prime norm-lifted checker. A bounded literature search and detailed comparisons cannot exclude an unindexed polyphase-code or Gabor-minor enumeration that already implies the same finite classification. Independent external mathematical review has not been performed.

## References
1. J. Lawrence, G. E. Pfander, D. Walnut, *Linear Independence of Gabor Systems in Finite Dimensional Vector Spaces*, Journal of Fourier Analysis and Applications **11** (2005), 715–726, DOI: 10.1007/s00041-005-5017-6, dated public journal record 2005-12-29. https://doi.org/10.1007/s00041-005-5017-6
2. R.-D. Malikiosis, *A note on Gabor frames in finite dimensions*, arXiv:1304.7709v1, first public 2013-04-29, particularly Theorem 1.2 and the explicit construction section. https://arxiv.org/abs/1304.7709
3. R.-D. Malikiosis, *Spark deficient Gabor frames*, arXiv:1602.09012v1, first public 2016-02-29, particularly Theorem 1.1 and the cyclic discussion. https://arxiv.org/abs/1602.09012
4. *The exact pentaphase cross-ambiguity support spectrum on the five-cycle*, mathematical research record and its full finding/proof, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-the-exact-pentaphase-cross-ambiguity-support-spectrum-on-the-fiv--bf80aa47100d
5. *Full-spark capacity of five-dimensional flat sign lines*, mathematical research record and its full finding/proof, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-full-spark-capacity-of-five-dimensional-flat-sign-lines--dae2935843e5
