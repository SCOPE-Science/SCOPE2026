# Exact five-alphabet fourth moments for the punctured square Fourier aperture

## Finding
Let \(\Lambda=\{0,1,2\}^2\setminus\{(1,1)\}\). For each \(q\in\{2,3,4,5,6\}\), put \(\mu_q=\{e^{2\pi i j/q}:j=0,\ldots,q-1\}\), choose arbitrary \(c_{ab}\in\mu_q\) for \((a,b)\in\Lambda\), and define
\[
P_c(z,w)=\sum_{(a,b)\in\Lambda}c_{ab}z^aw^b,\qquad
M(c)=\int_{\mathbb T^2}|P_c(z,w)|^4\,dm(z,w),
\]
where \(m\) is normalized Haar measure. The sharp minimum, complete number of phase-modulation classes of minimizers, and complete number of labeled minimizing coefficient arrays are:

| Alphabet \(q\) | Exact minimum \(M\) | Normalized minimizers | All minimizers |
| --- | ---: | ---: | ---: |
| \(2\) | \(88\) | \(3\) | \(24\) |
| \(3\) | \(96\) | \(36\) | \(972\) |
| \(4\) | \(88\) | \(11\) | \(704\) |
| \(5\) | \(96-4\sqrt5\) | \(4\) | \(500\) |
| \(6\) | \(84\) | \(2\) | \(432\) |

Normalized means \(c_{00}=c_{01}=c_{10}=1\); the five remaining phase exponents are listed completely in `optimizer_catalog.json`. The sixth-root minimum is attained at exactly two normalized five-tuples,
\[
(1,4,5,2,0)\quad\text{and}\quad (5,2,1,4,0),
\]
with the exponent coordinates ordered \((0,2),(1,2),(2,0),(2,1),(2,2)\). For fifth roots the four normalized minimizers are
\[
(1,3,4,1,4),\ (1,4,4,2,1),\ (4,1,1,3,4),\ (4,2,1,4,1).
\]
For every listed \(q\), the maximum fourth moment is \(216\). Every minimum and all equality-case counts are exact, including the irrational fifth-root constant. The same results hold if the Haar integral is replaced by the normalized Fourier average over \(\mu_m\times\mu_n\) for arbitrary integers \(m,n\ge5\).

## Assumptions and scope
The eight coefficients have modulus one and belong to the **specified finite** alphabets. The central coefficient is absent, not zeroed within a nine-unit-modulus array; this distinction changes the autocorrelation relations. There is no assertion about unrestricted continuous phases, alphabets \(q\ge7\), or a general formula in \(q\). Arrays are labeled by the eight specified sites. No reflection, rotation, or conjugation is divided out: only multiplication by \(\lambda\alpha^a\beta^b\), with \(\lambda,\alpha,\beta\in\mu_q\), defines equivalence classes.

## Proof
**1. Aperiodic Fourier identity.** For each integer displacement \(d=(u,v)\), write
\[
R_d(c)=\sum_{\substack{x\in\Lambda\\x+d\in\Lambda}}c_{x+d}\overline{c_x}.
\]
By Fourier character orthogonality,
\[
M(c)=\sum_{d\in\mathbb Z^2}|R_d(c)|^2
=64+2\sum_{d\in D_+}|R_d(c)|^2,
\]
where \(D_+\) is exactly the twelve positive nonzero differences listed by `checker.py`, chosen lexicographically from opposite-sign pairs. Since \(R_0=8\), its squared contribution is \(64\). Independently, writing \(S_s(c)=\sum_{x+y=s}c_xc_y\), the coefficient-convolution identity yields
\[
M(c)=\sum_{s\in\Lambda+\Lambda}|S_s(c)|^2.
\]
Both identities are finite and exact.

**2. Exact orbit reduction.** The phase change \(c_{ab}\mapsto\lambda\alpha^a\beta^bc_{ab}\) multiplies each nonzero displacement autocorrelation by \(\alpha^u\beta^v\), leaving its absolute value unchanged. There is exactly one choice of \((\lambda,\alpha,\beta)\in\mu_q^3\) that makes \(c_{00}=c_{01}=c_{10}=1\): specifically, \(\lambda=c_{00}^{-1}\), \(\alpha=c_{00}c_{10}^{-1}\), and \(\beta=c_{00}c_{01}^{-1}\). Each normalized array therefore has exactly \(q^3\) distinct lifts, and all normalized arrays are obtained by independently assigning five residual exponents in \(\{0,\ldots,q-1\}\). The exact search domain has \(q^5\) cases, not \(q^8\).

**3. Exact arithmetic in every alphabet.** For \(q\in\{2,4\}\), use Gaussian-integer coordinates \(a+bi\) and the norm \(a^2+b^2\). For \(q\in\{3,6\}\), use Eisenstein coordinates \(a+b\omega\), \(\omega=e^{2\pi i/3}\), and norm \(a^2-ab+b^2\). Sixth roots are \(1,1+\omega,\omega,-1,-1-\omega,-\omega\). Thus all fourth moments for these four alphabets are integers computed by addition and multiplication of ordinary integers.

For \(q=5\), let \(\zeta=e^{2\pi i/5}\), and suppose a correlation (or a convolution coefficient) consists of \(n_j\) occurrences of \(\zeta^j\). Set \(B=\sum_{j=0}^4n_j^2\), \(A=\sum_{j=0}^4n_jn_{j+1}\), and \(C=\sum_{j=0}^4n_jn_{j+2}\), with cyclic subscripts. The elementary exact cosine values give
\[
\left|\sum_{j=0}^4n_j\zeta^j\right|^2
=B+\frac{\sqrt5-1}{2}A-\frac{\sqrt5+1}{2}C.
\]
Consequently, twice every squared modulus is exactly the pair \((2B-A-C,A-C)\), interpreted as \((2B-A-C)+(A-C)\sqrt5\). All comparisons between pairs \((a,b)\) representing \(a+b\sqrt5\) reduce to signs of integers and of \(a^2-5b^2\); no floating-point comparison is needed.

**4. Finite exhaustive certificate.** The included `checker.py` independently implements both Fourier identities, constructs every one of the \(q^5\) normalized choices for all five alphabets, and verifies equal moments from the autocorrelation and convolution formulas **for every single choice**. It performs \(2^5+3^5+4^5+5^5+6^5=12200\) complete exact tests. Every attained moment is compared using the integer or quadratic-integer order just described. The program computes all minimizers rather than stopping at the first one, compares the sorted normalized minimizer tuples against `optimizer_catalog.json`, and checks the numbers and moments in the table. Thus enumeration covers the entire expressly finite domain. The normalization bijection proves that multiplying the normalized counts by \(q^3\) gives the complete labeled-array counts. This is a finite, reproducible proof and makes no inference about an infinite or continuous search space.

**5. Discrete torus transfer.** The Fourier support of \(P_c^2\) lies in \(\{0,1,2,3,4\}^2\). If \(m,n\ge5\), these coefficient frequencies are pairwise distinct modulo \(m,n\), so discrete character orthogonality reproduces \(\sum_s|S_s(c)|^2\) without aliasing. Hence all sharp values and optimizer classifications transfer unchanged.

**6. Upper endpoint.** In the convolution identity, \(|S_s|\) is at most the number of ordered pairs \((x,y)\in\Lambda^2\) summing to \(s\). Summing these squared cardinalities gives \(216\), and equality holds for the all-one coefficient array. Thus the maximum is \(216\) for every listed alphabet, independently of enumeration.

## Verification
Place `checker.py` beside `optimizer_catalog.json` and execute `python3 checker.py`. The program requires only the Python standard library, checks every normalized case for all five alphabets with exact integer arithmetic, verifies both independently grouped Fourier identities and the complete optimizer catalog, and exits nonzero on any mismatch. The exact output terminates with `HOLLOW_SQUARE_FOURTH_MOMENT_PASS checked=12200 direct_vs_convolution=all`. The catalog records the five-tuple of exponents for each optimizer, not a rounded complex representative. External experiments are not required for the finite theorem.

## Relationship to prior work
Zhang, Fan, and Mesnager (2021, arXiv:2107.11599v1) construct two-dimensional **complementary pairs** with zero-correlation zones: their Theorems 1 and 2 control sums of two arrays' correlations, not the summed squared autocorrelations of one fixed eight-site punctured array. Pai and Chen (2021, arXiv:2102.04043v1) construct two-dimensional Golay complementary **sets**, again without a sharp single-punctured-array minimum. Raei and collaborators (2021, arXiv:2104.03303v1) develop optimization algorithms for phase-only sequence correlation but do not give a complete exact minimizer census on this two-dimensional support.

Two published Fourier fourth-moment calculations for the **full nine-site** square and the **eight-site three-dimensional** binary cube determine different support geometries. Removing the central site does not yield a unit-modulus special case of the full square. The three-dimensional cube has different additive-relations geometry; its continuous optimal moment \(88\) does not cover the sixth-root punctured-plane value \(84\). An equivalent historical specialist classification cannot be excluded merely from a literature search.

## Limitations
Only \(q\in\{2,3,4,5,6\}\) is proved. The fifth-root exact constant is not a claim about arbitrary complex phases. Discrete-grid transfer requires both grid orders at least five. The exhaustive certificate is a proof only for these finite alphabets, with a complete declared loop domain and exact algebra; it is not a heuristic sample. No independent mathematical audit has been performed. Earlier unindexed array-code catalogs remain a bibliographic priority risk.

## References
- C.-Y. Pai and C.-Y. Chen, *Two-Dimensional Golay Complementary Array Sets from Generalized Boolean Functions*, arXiv:2102.04043v1, first public 2021-02-08. https://arxiv.org/abs/2102.04043
- H. Zhang, C. Fan, and S. Mesnager, *New constructions of q-Ary 2-D Z-Complementary Array Pairs*, arXiv:2107.11599v1, first public 2021-07-24. https://arxiv.org/abs/2107.11599
- E. Raei, M. Alaee-Kerahroodi, P. Babu, and M. R. B. Shankar, *Design of MIMO Radar Waveforms based on lp-Norm Criteria*, arXiv:2104.03303v1, first public 2021-04-07. https://arxiv.org/abs/2104.03303
- *Sharp phase-alphabet fourth moments for the nine-mode square Fourier aperture*, publicly available complete result: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-phase-alphabet-fourth-moments-for-the-nine-mode-square-fou--f31c28437f0d
- *Exact fourth-moment rigidity of the eight-mode cubic Fourier aperture*, publicly available complete result: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-fourth-moment-rigidity-of-the-eight-mode-cubic-fourier-ape--486a31ac0a2d
