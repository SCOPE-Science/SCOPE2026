# Arithmetic resonance law for one-site amplitude repairs of cubic Gabor chirps

## Finding

Fix a prime \(p\ge5\), put \(\zeta=\exp(2\pi i/p)\), and set \(g_t(0)=t\) and \(g_t(j)=\zeta^{j^3}\) for \(j\in\mathbb F_p^\times\), with real \(t\ge0\). The \(p^2\) rank-one Gabor projectors of \(g_t\) are linearly informationally complete (their complex linear span is the entire \(p\times p\) matrix space) if and only if \(t\ne1\) and the finite arithmetic exception below is avoided.

When \(p\equiv3\pmod4\), **there are no nontrivial exceptional amplitudes**: every \(t\ge0\) except \(1\) works. When \(p\equiv1\pmod4\), put \(h_{a,b}=ab/2\pmod p\), choose its integer representative in \(\{0,\ldots,p-1\}\), and define \(S_{a,b}=2\cos(2\pi h_{a,b}/p)\). For each \(a\in\mathbb F_p^\times\) and \(b\in\mathbb F_p\) satisfying

\[
b^2+9a^4\equiv0\pmod p,\qquad \chi(3a)S_{a,b}<0,
\]

remove the single real amplitude

\[
t_{a,b}=1-\frac{\chi(3a)\sqrt p}{S_{a,b}}\;>1.
\]

Here \(\chi\) is the quadratic character. The exceptional set is finite and explicitly computable from modular arithmetic and real cosines. The cases \(p=5\) and \(p=13\) have no such positive exceptions; \(p=17\) has a failure at

\[
t_*=1+\frac{\sqrt{17}}{2\cos(\pi/17)}\approx3.09726269566458.
\]

The result concerns *linear injectivity on matrices*, which is stronger than phase retrieval for pure vectors. At an exceptional amplitude the matrix-analysis map has a nonzero kernel; no claim is made that pure-vector phase retrieval necessarily fails there.

## Assumptions and scope

All indices are in \(\mathbb F_p\). Let \(T_a f(j)=f(j-a)\) and \(M_b f(j)=\zeta^{bj}f(j)\). Put \(P_{a,b}=(M_bT_a g_t)(M_bT_a g_t)^*\). Linear informational completeness means that the map \(X\mapsto(\operatorname{tr}(XP_{a,b}))_{a,b}\) is injective on the complex vector space of \(p\times p\) matrices (equivalently, on its Hermitian real subspace). No normalization of \(g_t\) is imposed; a nonzero common scaling does not affect the classification. The case \(t=0\) is included, as is every boundary amplitude.

## Proof

Define the self-ambiguity coefficient in a convenient sign convention by

\[
A_t(a,b)=\sum_{j\in\mathbb F_p}g_t(j+a)\overline{g_t(j)}\zeta^{bj}.
\]

The Weyl operators form an orthogonal Hilbert--Schmidt basis. Covariance makes them eigenvectors of the Gabor-projector frame operator, with eigenvalues \(p|A_t(a,b)|^2\), up to relabeling and conjugation of \((a,b)\). Consequently the full projector family spans the matrix algebra exactly when every \(A_t(a,b)\) is nonzero.

For \(a=0\), the coefficients are

\[
A_t(0,0)=p-1+t^2,\qquad A_t(0,b)=t^2-1\quad(b\ne0).
\]

They are all nonzero precisely when \(t\ne1\) in the prescribed nonnegative real domain.

For \(a\ne0\), the unmodified Alltop chirp contributes the quadratic polynomial phase

\[
(j+a)^3-j^3+bj=3aj^2+(3a^2+b)j+a^3.
\]

Only the two indices \(j=0,-a\) involve the modified entry. Thus the *exact* formula is

\[
A_t(a,b)=\zeta^{a^3}\left[\varepsilon_p\chi(3a)\sqrt p\,\zeta^{-C_{a,b}}+(t-1)(1+\zeta^{-ab})\right],
\]

where \(C_{a,b}=(3a^2+b)^2/(12a)\pmod p\) and \(\varepsilon_p=1\) if \(p\equiv1\pmod4\), while \(\varepsilon_p=i\) if \(p\equiv3\pmod4\). This uses the standard complete quadratic Gauss sum with the positive-exponential convention for \(\zeta\); division inside exponents means multiplication by the modular inverse.

Set \(h_{a,b}=ab/2\pmod p\). The identity \(1+\zeta^{-ab}=\zeta^{-h_{a,b}}S_{a,b}\) has real nonzero \(S_{a,b}=\zeta^{h_{a,b}}+\zeta^{-h_{a,b}}\) (it cannot vanish for an odd prime). A zero at a real amplitude would therefore require

\[
\varepsilon_p\zeta^{h_{a,b}-C_{a,b}}\in\mathbb R.
\]

For \(p\equiv3\pmod4\), this is impossible: \(i\zeta^k\) is never real for odd \(p\). For \(p\equiv1\pmod4\), the only real \(p\)-th root of unity is \(1\), so the phase condition is \(C_{a,b}=h_{a,b}\), equivalently \(b^2+9a^4=0\pmod p\). At such pairs the remaining scalar equation is \(\chi(3a)\sqrt p+(t-1)S_{a,b}=0\), giving the displayed list. Because \(\sqrt p/|S_{a,b}|>1\), its nonnegative solutions occur only when \(\chi(3a)S_{a,b}<0\), and necessarily have \(t>1\). This proves the complete classification.

For the stated \(p=17\) example take \(a=3,b=6\). Then \(b^2+9a^4\equiv0\pmod{17}\), \(\chi(9)=1\), \(h=9\), and \(S=2\cos(18\pi/17)=-2\cos(\pi/17)\), so \(A_{t_*}(3,6)=0\). The \(p=5,13\) assertions follow by directly exhausting the at most \(2(p-1)\) modular phase candidates; the included checker performs this finite ancillary verification. No assertion for all larger primes is derived from that census.

## Verification

Run `python3 check_alltop.py` with Python's standard library. It directly evaluates both the finite ambiguity sum and the Gauss-sum expression over ten primes and five amplitudes, checks all listed resonances, and tests the special \(p=17\) cancellation. Its finite computations are checks of the formulas and small examples, **not** proofs of the all-prime theorem. The all-prime proof is the displayed exact Gauss-sum evaluation plus its phase argument. The checker needs no external datasets.

## Relationship to prior work

Bojarovska and Flinth (arXiv:1503.05800, §§2.2--2.4) prove that nonvanishing self-ambiguity is sufficient for general Gabor phase retrieval, and explicitly identify the unimodular Alltop sequence as unsuitable for recovering arbitrary signals. Li (arXiv:2609.09614, §§2--3 and §5) obtains algebraic Gabor regularizations and a distinct quadratic-character-modulated cubic-chirp construction with quantitative gaps. Those results supply the foundational criterion and motivation, but neither analyzed construction gives the present *exact real one-site amplitude-exception locus*, its quadratic-residue congruence, or the modulus-four all-amplitude dichotomy. The present result does not claim full spark, optimum conditioning, or global failure of pure-state phase retrieval at a rank-defect amplitude.

## Limitations

The classification is for prime lengths at least five, a cubic phase, and a single **real nonnegative** amplitude replacement at index zero. It does not cover complex replacements, composite cyclic lengths, additional changed coordinates, noise stability near exceptional parameters, or pure-state injectivity at a rank defect. Originality is assessed against inspected literature and database matches, not against all possible unindexed work. The finite checker uses ordinary floating-point arithmetic and does not independently certify an infinite family of Gauss-sum identities.

## References

1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800 (first public version 2015-03-19), §§2.2--2.4.
2. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614 (first public version 2026-09-09), §§2--3, 5.
3. W. O. Alltop, *Complex sequences with low periodic correlations*, IEEE Trans. Inform. Theory **26** (1980), 350--354, DOI:10.1109/TIT.1980.1056185 (historical construction; original full text not inspected in this study).
