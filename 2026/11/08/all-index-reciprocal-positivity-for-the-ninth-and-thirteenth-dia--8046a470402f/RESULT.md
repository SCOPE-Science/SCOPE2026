# All-index reciprocal positivity for the ninth and thirteenth diagonal Padé denominators

## Finding
For each \(m\in\{9,13\}\), let
\[
q_m(z)=\sum_{j=0}^m(-1)^j\binom mj\frac{(2m-j)!}{(2m)!}z^j,
\qquad \frac1{q_m(z)}=\sum_{n=0}^{\infty}c_{m,n}z^n.
\]
Then **\(c_{m,n}>0\) for every integer \(n\ge0\)**. The ninth and thirteenth diagonal orders are particularly relevant because both occur in the standard scaling-and-squaring algorithm for matrix exponentials, with order thirteen its high-norm branch [3].

The proof is a finite exact-arithmetic certificate for infinitely many coefficients, not a sample-based extrapolation. The two specific cutoffs are \(N_9=44\) and \(N_{13}=105\): the coefficient recurrences prove strict positivity before the cutoff, and a rigorous pole/residue comparison proves it at and after the cutoff.

## Assumptions and scope
The normalized polynomial is the denominator of the \([m/m]\) Padé approximant of \(e^z\), evaluated symbolically over rational coefficients. The conclusion concerns scalar Taylor coefficients of the reciprocal about zero, for exactly \(m=9\) and \(m=13\). The variable \(z\) is complex, and coefficients are defined in the analytic Taylor germ at zero. All computations in the accompanying certificate use arbitrary-precision integer/rational arithmetic and elementary integer square roots. No floating-point root enclosure is assumed.

## Proof
**1. An exhaustive root isolation.** For each degree \(m\), form \(q_m\) from the displayed factorial formula. The accompanying `positivity_certificate.py` contains a rational center for one real root and for each root in the open upper half-plane. Add conjugate centers for the lower-half-plane roots. For a center \(a\), expand exactly
\[
q_m(a+w)=\sum_{j=0}^m b_j w^j,\qquad r=10^{-3}.
\]
The code verifies the strict rational bound
\[
|b_0|+\sum_{j=2}^m |b_j|r^j<|b_1|r.
\]
Here each complex modulus on the left is safely *upper*-bounded by the sum of absolute rational real and imaginary parts, while \(|b_1|\) on the right is *lower*-bounded by the floor of the exact squared modulus square root to \(10^{-18}\) rational precision. Thus the strict check is stronger than the displayed inequality. Rouché's theorem gives exactly one root (counted with multiplicity) in each disk. The rational checks also establish pairwise disjointness of all \(m\) disks, so all roots have been located, are simple, and include exactly one real positive root \(R\). The real derivative is proved strictly negative throughout that root's disk by a separate rational Taylor-derivative estimate.

**2. Unique dominant pole and certified residue bounds.** From each root disk the code computes rational bounds \(L_j<|\zeta_j|<U_j\) and \(D_j^-<|q_m'(\zeta_j)|<D_j^+\); all inequalities are conservative. It checks \(L_j>U_0\) for every nonreal root, where \(\zeta_0=R\), so \(R\) is the unique pole of smallest modulus. By partial fractions,
\[
\frac1{q_m(z)}=\sum_{j=0}^{m-1}\frac{B_j}{1-z/\zeta_j},
\quad B_j=-\frac1{\zeta_jq'_m(\zeta_j)},
\quad c_{m,n}=\sum_{j=0}^{m-1}B_j\zeta_j^{-n}.
\]
Because \(q_m'(R)<0\), the dominant residue \(B_0\) is positive. Put \(a_0=(U_0 D_0^+)^{-1}\), \(a_j=(L_jD_j^-)^{-1}\), and \(r_j=U_0/L_j<1\) for each nonreal root. Then for every integer \(n\ge0\),
\[
c_{m,n}\ge U_0^{-n}\left(a_0-\sum_{j=1}^{m-1}a_j r_j^n\right).
\]
The exact-rational certificate checks \(\sum_{j\ge1}a_jr_j^{44}<a_0\) for degree nine and \(\sum_{j\ge1}a_jr_j^{105}<a_0\) for degree thirteen. Since all \(r_j<1\), the inequality remains strict at every larger index.

**3. Exact finite prefix.** The coefficient identity \(q_m(z)\sum_n c_{m,n}z^n=1\) gives
\[
c_{m,0}=1,\qquad c_{m,n}=-\sum_{j=1}^{\min(m,n)}[z^j]q_m(z)\,c_{m,n-j}.
\]
The script computes these as exact rational fractions and checks all indices \(0\le n<44\) for degree nine and \(0\le n<105\) for degree thirteen. These strict finite checks and Step 2 cover every nonnegative index. QED.

## Verification
Run `python3 positivity_certificate.py` using a standard Python 3 installation. The script verifies each rational root enclosure, disk disjointness, derivative sign, spectral separation, strict residue dominance at the cutoff, and each rational prefix coefficient. Successful execution prints `CERTIFICATE_OK` after two PASS lines. The printed tail ratios are **diagnostic decimal displays only**; the assertions establishing all signs use exact rational inequalities. The displayed ratios are approximately \(0.99937837\) at \(m=9,n=44\) and \(0.99425975\) at \(m=13,n=105\). Each strictly below one is an exact-arithmetic theorem in the certificate.

## Relationship to prior work
Fasi and Higham [1] formulated positivity for the reciprocal Padé denominator coefficients as Conjecture 3.2, noting that positivity could simplify a forward-error bound. Scardino [2], in sections 1–2 and 8, proved conditional eventual positivity from the strictly dominant positive pole, and furnished counterexamples to the unrestricted off-diagonal conjecture; Scardino explicitly left the diagonal case open. The present proof verifies that pole condition *and every finite index* for two specified algorithmically relevant diagonal orders. It does not assert that the prior conditional tail theorem alone implies the claimed all-index statement. Al-Mohy and Higham [3] document both orders as standard in scaling-and-squaring, with degree thirteen important when scaling is needed.

## Limitations
The result does not settle every odd diagonal degree, arbitrary numerator degrees, numerical floating-point error, or validity of any implementation without its other assumptions. It establishes a sign property that can justify the positivity-dependent step in the error-bound analysis for the two specified degrees; it does not by itself prove an overall runtime reduction or a matrix-function error estimate. Although the cited 2026 paper identifies the full diagonal case as open, no literature search can exclude every unpublished or unindexed equivalent finite-degree proof. Independent mathematical review has not been performed.

## References
1. Massimiliano Fasi and Nicholas J. Higham, *An Arbitrary Precision Scaling and Squaring Algorithm for the Matrix Exponential*, SIAM Journal on Matrix Analysis and Applications **40** (2019), 1233–1256, Conjecture 3.2. https://doi.org/10.1137/18M1228876 ; open manuscript https://eprints.maths.manchester.ac.uk/2691/1/fahi19.pdf
2. Francesco Scardino, *On a positivity conjecture of Fasi and Higham for Padé approximants to the matrix exponential*, arXiv:2610.39051v1 (first public 2026-10-28), especially Theorem 8.2, Proposition 8.3, and the discussion of the diagonal case. https://arxiv.org/abs/2610.39051
3. Awad H. Al-Mohy and Nicholas J. Higham, *A New Scaling and Squaring Algorithm for the Matrix Exponential*, SIAM Journal on Matrix Analysis and Applications **31** (2009), 970–989, sections 3–5 and Algorithm 5.1. https://doi.org/10.1137/09074721X ; open manuscript https://eprints.maths.manchester.ac.uk/1300/1/alhi09a.pdf
