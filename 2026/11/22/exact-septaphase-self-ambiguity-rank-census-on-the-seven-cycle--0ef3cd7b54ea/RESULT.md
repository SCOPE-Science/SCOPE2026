# Exact septaphase self-ambiguity rank census on the seven-cycle

## Finding
Let \(\zeta=\exp(2\pi i/7)\). For every full-support window \(g:\mathbb Z_7\to\mu_7\) of seventh-root phases, define its cyclic periodic self-ambiguity coefficients by
\[
A_g(u,v)=\sum_{x\in\mathbb Z_7}g(x+u)\overline{g(x)}\zeta^{-vx}.
\]
The number \(r(g)=|\{(u,v)\in\mathbb Z_7^2:A_g(u,v)\ne0\}|\) has **exactly five possible values**. After dividing out the common seventh-root scalar by fixing \(g(0)=1\), their complete incidence distribution is

| Exact nonzero ambiguity count \(r(g)\) | Number of normalized windows |
|---:|---:|
| 7 | 49 |
| 37 | 14,406 |
| 39 | 18,522 |
| 41 | 24,696 |
| 43 | 59,976 |
| **Total** | **117,649** |

Thus \(r(g)=7\) **if and only if** \(g\) is a quadratic phase chirp. Every other seven-phase window has \(r(g)\ge37\), and that bound is attained by exactly \(14,406\) normalized windows. The possible nontrivial rank losses are sharply restricted: \(r(g)\in\{37,39,41,43\}\), even though the universal constant-envelope Fourier-support bound is weaker.

The full **delay-row zero profile** is also classified. For \(j=1,2,3\), let \(z_j(g)=|\{v:A_g(j,v)=0\}|\); the negative-delay row has the same number of zeros. Exactly the following six profile families occur; "permutations" means the three coordinate permutations of the indicated triple (or one when all entries agree).

| \((z_1,z_2,z_3)\) | Normalized count per indicated triple | Number of triples |
|---|---:|---:|
| \((0,0,0)\) | 59,976 | 1 |
| Permutations of \((1,0,0)\) | 8,232 | 3 |
| Permutations of \((2,0,0)\) | 2,058 | 3 |
| Permutations of \((1,1,0)\) | 4,116 | 3 |
| \((1,1,1)\) | 14,406 | 1 |
| \((6,6,6)\) | 49 | 1 |

Each profile gives the rank by \(r(g)=43-2(z_1+z_2+z_3)\). In particular, the sharp rank-37 case has *exactly one missing modulation at each nonzero delay*. There is no phase word with an intermediate profile outside these six families.

The same rank is the exact complex rank of the full seven-cycle **Gabor intensity-lifting** map, obtained by measuring every time-frequency shift of \(g\). This is a linear matrix-recovery rank, not an assertion about the weaker nonlinear phase-retrieval problem for arbitrary rank-one signals.

## Assumptions and scope
The cyclic indices, phase exponents, and modulation frequencies are taken modulo seven. \(\mu_7=\{\zeta^j:0\le j\le6\}\). All seven window entries have modulus one, with no zero entry; there are \(7^7\) indexed windows before quotienting by a common scalar and exactly \(7^6\) normalized ones. Normalization \(g(0)=1\) is unique and does not affect the ambiguity zero set. The optional unit vector \(h=g/\sqrt7\) is used for the normalized Gabor lifting; scaling does not affect its rank.

Let \((T_ug)(x)=g(x-u)\), \((M_vg)(x)=\zeta^{vx}g(x)\), and \(P_{u,v}=(M_vT_uh)(M_vT_uh)^*\). Define the complex-linear measurement lifting
\[
\mathcal L_h:\mathbb C^{7\times7}\longrightarrow\mathbb C^{49},\qquad
(\mathcal L_h X)(u,v)=\operatorname{tr}(X P_{u,v}).
\]
Its rank is invariant under the choice of scalar multiple of \(g\). The claim concerns the complete 49-measurement orbit, not a subsampled frame or reconstruction-condition number.

## Proof
**1. Exact cyclotomic zero test.** Write \(g(x)=\zeta^{a_x}\), with \(a_0=0\) and \(a_1,\ldots,a_6\in\mathbb F_7\). For a fixed delay and frequency,
\[
A_g(u,v)=\sum_{x=0}^6\zeta^{a_{x+u}-a_x-vx}.
\]
Define the multiplicities \(n_j=|\{x:a_{x+u}-a_x-vx\equiv j\pmod7\}|\) for \(j=0,\ldots,6\). They are nonnegative integers summing to seven. The minimal polynomial of the primitive seventh root \(\zeta\) over \(\mathbb Q\) is \(\Phi_7(X)=1+X+\cdots+X^6\). The polynomial \(\sum_j n_j X^j\) has degree at most six, so it vanishes at \(\zeta\) if and only if its coefficients are all equal. Their sum forces \(n_0=\cdots=n_6=1\). Hence
\[
\boxed{A_g(u,v)=0\iff x\longmapsto a_{x+u}-a_x-vx\text{ is a permutation of }\mathbb F_7.}
\]
This is an exact integer decision procedure; no approximate complex calculation is used to decide a zero.

**2. Forced zero row and time reversal.** The zero-delay row satisfies \(A_g(0,0)=7\) and \(A_g(0,v)=0\) for the six nonzero \(v\). Direct substitution gives
\[
\overline{A_g(u,v)}=\zeta^{-uv}A_g(-u,-v),
\]
so the two delay rows at \(u\) and \(-u\) have equal zero counts. Consequently the total ambiguity support size is \(43-2(z_1+z_2+z_3)\).

**3. Exact finite exhaustion and completeness.** Every phase word modulo a common scalar is uniquely the exponent tuple \((0,a_1,\ldots,a_6)\), and hence the exhaustive domain has precisely \(7^6=117649\) elements. The included `artifacts/verify_census.py` loops over this exact domain, across all seven delays and seven modulations, applies the integer permutation predicate of Step 1, and accumulates the complete counts of \(r(g)\) and the ordered triple \((z_1,z_2,z_3)\). Its precise expected histogram and all twelve ordered triple values are hard-coded and asserted. The resulting six profile families and full rank table above exhaust the domain, establishing every listed existence, bound, and nonexistence claim. This is an exhaustive finite proof, not an extrapolation from sample data.

**4. Independent parameterization and mathematical rank interpretation.** The separate `artifacts/verify_increments.cpp` enumerates the seven cyclic increments \(d_x=a_x-a_{x-1}\), subject to \(\sum_{x=0}^6 d_x=0\). It chooses the six free increments and reconstructs the phase word by integration; this is a bijection onto the same normalized domain, using a different enumeration order. Instead of testing distinctness, it expands each ambiguity value in the six-dimensional integer cyclotomic quotient basis and checks whether all seven residue multiplicities are equal. It independently reproduces both the rank distribution and all twelve ordered profiles.

The normalized Weyl operators \(7^{-1/2}M_vT_u\) form an orthonormal basis of the 49-dimensional matrix space under the Hilbert--Schmidt pairing. Fourier transforming the orbit of the rank-one projector \(hh^*\) diagonalizes the corresponding measurement map in that Weyl basis, with a multiplier proportional to \(A_h(u,v)=A_g(u,v)/7\) at each Weyl coordinate. Therefore \(\operatorname{rank}_{\mathbb C}\mathcal L_h\) is exactly \(r(g)\), as claimed.

**5. Equality at the minimal stratum.** Every quadratic exponent \(a_x=Ax^2+Bx\) gives a phase-difference word affine in \(x\) for every nonzero delay, so each row has exactly one nonzero modulation, and \(r(g)=7\). Conversely, the exhaustive table shows that precisely 49 normalized words have rank seven. There are exactly \(7^2=49\) distinct normalized quadratic exponent words, so these and only these form the minimal stratum. The rank-37 examples are automatically nonquadratic, and their count and precise zeros follow from their uniquely specified profile in Step 3.

As a finer structural cross-check, unique interpolation in the Newton finite-difference basis gives the following rank distributions by the algebraic degree of the exponent function \(a:\mathbb F_7\to\mathbb F_7\):

| Exponent degree | Nonzero counts by rank |
|---:|---|
| 0, 1, 2 | rank 7: 1, 6, 42 respectively |
| 3 | rank 43: 294 |
| 4 | rank 43: 2,058 |
| 5 | rank 39: 6,174; rank 43: 8,232 |
| 6 | rank 37: 14,406; rank 39: 12,348; rank 41: 24,696; rank 43: 49,392 |

These degree-resolved counts, independent of the compressed profile table, are also verified by the exact Python certificate.

## Verification
Both programs require only standard facilities. Run `python3 artifacts/verify_census.py`, followed by `g++ -O2 -std=c++17 artifacts/verify_increments.cpp -o verify_increments` and `./verify_increments`. The former prints `SEPTAPHASE_P7_EXACT_PASS total=117649`; the latter prints `SEPTAPHASE_P7_INCREMENT_PASS total=117649`. Their complete recorded outputs are supplied as `artifacts/python_output.txt` and `artifacts/cpp_output.txt`.

The Python implementation independently records the 12 profiles, rank counts, and degree strata. The C++ implementation independently checks the rank counts and 12 profiles using a cyclic-increment parameterization and the cyclotomic-quotient coefficient criterion. Because every normalized window is visited exactly once and all decisions are exact integers, these bounded computations constitute a rigorous finite certificate. They do not establish analogous assertions for other prime lengths or other phase alphabets.

## Relationship to prior work
Krahmer, Pfander, and Rashkov [1] give general STFT-support inequalities, including their prime-order lower bound, but not the full seventh-root seven-cycle self-ambiguity distribution. The 2011 Benedetto--Benedetto--Woodworth study [2] motivates polyphase ambiguity support and magnitude design, but concerns Björck/CAZAC sequences and does not give this exhaustive incidence classification. Bojarovska and Flinth [3] identify why ambiguity zeros govern full Gabor matrix-recovery rank; that known diagonalization is an input, not claimed as new.

Among closer subsequent published finite records, *Sharp hexaphase self-ambiguity support spectrum on the seven-cycle* [4] classifies a **different six-root alphabet**, with support \(\{7,39,41,43\}\). The seventh-root alphabet here has an additional sharp rank-37 stratum and a distinct complete profile distribution. *The exact pentaphase cross-ambiguity support spectrum on the five-cycle* [5] concerns a smaller cyclic group and pairs of independently coded sequences. *A phase-only ambiguity support gap beyond quadratic chirps* [6] proves the much weaker all-prime nonquadratic support lower bound \(4p-3\), which is 25 at order seven. *Exact Gabor lifting ranks and fourth ambiguity moments of quartic prime-field chirps* [7] concerns one particular polynomial-phase family, not all seventh-root phase words of length seven. These are comparisons of statements and implications; mere differences in titles or counting parameters do not establish historical priority. An unindexed earlier septaphase radar-code census remains a risk.

## Limitations
This is a complete **finite** theorem only for the native seventh-root phase alphabet and the cyclic group of order seven. A rank histogram does not give the magnitudes of the nonzero ambiguity coefficients, reconstruction noise stability, or nonlinear injectivity for arbitrary signals. The result does not claim full-rank lifting: every unimodular window has six forced zero-delay modulation zeros and hence rank at most 43. Independent mathematical audit has not been performed, and an independently unindexed equivalent computation is not excluded.

## References
1. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time--frequency representations on finite Abelian groups and applications*, arXiv:math/0611493v1, first public 2006-11-16, Proposition 4.4 and Section 5. https://arxiv.org/html/math/0611493v1
2. J. J. Benedetto, R. L. Benedetto, and J. T. Woodworth, *Optimal ambiguity functions and Weil's exponential sum bound*, arXiv:1107.1887v1, first public 2011-07-10. https://arxiv.org/html/1107.1887v1
3. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1, first public 2015-03-19. https://arxiv.org/abs/1503.05800
4. *Sharp hexaphase self-ambiguity support spectrum on the seven-cycle*, published mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-sharp-hexaphase-self-ambiguity-support-spectrum-on-the-seven-cyc--348df602476c
5. *The exact pentaphase cross-ambiguity support spectrum on the five-cycle*, published mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/16/SCOPE-the-exact-pentaphase-cross-ambiguity-support-spectrum-on-the-fiv--bf80aa47100d
6. *A phase-only ambiguity support gap beyond quadratic chirps*, published mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-phase-only-ambiguity-support-gap-beyond-quadratic-chirps--ccbbfc2c2a80
7. *Exact Gabor lifting ranks and fourth ambiguity moments of quartic prime-field chirps*, published mathematical record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-gabor-lifting-ranks-and-fourth-ambiguity-moments-of-quarti--26ee2b47d69a
