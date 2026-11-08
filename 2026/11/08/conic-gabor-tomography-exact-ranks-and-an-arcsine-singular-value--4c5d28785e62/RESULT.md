# Conic Gabor tomography: exact ranks and an arcsine singular-value law

## Finding

For every odd prime \(p\), set \(V=\mathbb F_p^2\), \(N=p^2\), \(Q(x)=x_1^2+x_2^2\), and \(S=\{x\in V:Q(x)=1\}\). Write \(g=\mathbf1_S\), and let \(\chi\) be the quadratic character on \(\mathbb F_p\), with \(\chi(0)=0\), and \(\epsilon=\chi(-1)\). Define the complete complex-linear intensity-lifting map \(\mathcal L_g:\mathbb C^{N\times N}\longrightarrow\mathbb C^{N^2}\) by
\[
\mathcal L_g(X)_{a,b}=\operatorname{tr}\!\left(X\,|M_bT_ag\rangle\langle M_bT_ag|\right),\quad
(T_af)(x)=f(x-a),\quad (M_bf)(x)=e^{2\pi i(b\cdot x)/p}f(x).
\]
Then
\[
\boxed{\operatorname{rank}_{\mathbb C}\mathcal L_g=p^2\left(1+\frac{(p-\epsilon)^2}{2}\right),\qquad
\operatorname{nullity}_{\mathbb C}\mathcal L_g=p^4-p^2\left(1+\frac{(p-\epsilon)^2}{2}\right).}
\]
The nullspace is the complex span of all Weyl operators indexed by spatial shifts outside \(S-S\) and arbitrary modulations.

The positive singular values consist of the following **multiset contributions**, where \(r=p-\epsilon\), \(r_1=r\), and \(r_2=r(r-2)/2\):

* \(p\), with multiplicity \(p^2r_1\), from the one-intersection shifts;
* \(2p\), with multiplicity \(pr_2\), and \(2p\cos(\pi j/p)\), with multiplicity \(2pr_2\) for **each** integer \(1\le j\le(p-1)/2\), from the two-intersection shifts;
* \(p\left|\sum_{x\in S}\exp(2\pi i\,b\cdot x/p)\right|\) for each \(b\in V\), with multiplicity counted by this explicit list (\(p^2\) terms), from the zero shift.

These positive contributions are added when values coincide; all remaining singular values are zero. In particular, **no evaluation of the last collection of finite character sums is claimed**. When positive singular values are divided by \(p\) and counted uniformly with multiplicities, their empirical distributions converge weakly, as \(p\to\infty\) through odd primes, to the probability measure with density
\[
\boxed{\frac{2}{\pi\sqrt{4-s^2}}\,\mathbf1_{(0,2)}(s).}
\]
The rank fraction is \(\frac12-\epsilon/p+\frac{3}{2p^2}\). Thus the first correction changes sign with \(p\bmod4\) while the limiting identifiable operator fraction is \(1/2\).

## Assumptions and scope

The underlying additive group is the two-dimensional vector space \(\mathbb F_p^2\) for an **odd prime** \(p\), not the cyclic group of order \(p^2\). The unnormalized indicator window is used; a global nonzero rescaling changes singular values but not their rank or zero pattern. The target matrix space consists of **all complex matrices**, rather than just Hermitian rank-one signal matrices, so linear injectivity and nonlinear pure-signal phase retrieval must not be conflated. Singular values use the standard Hilbert--Schmidt norm on matrices and the Euclidean norm on measurement vectors.

## Proof

**1. Two-point intersection geometry.** For a nonzero shift \(a\in V\) the intersection \(S\cap(S-a)\) satisfies \(Q(x)=Q(x+a)=1\). Subtraction gives \(2a\cdot x+Q(a)=0\). If \(t=Q(a)=0\), the resulting affine line is tangent-free: writing \(x=-a/2+y\) gives \(a\cdot y=0\) and \(Q(y)=1\). In two dimensions, a nonzero isotropic vector spans its own orthogonal line, on which \(Q\) vanishes; hence the intersection is empty. If \(t\ne0\), choose \(Ja=(-a_2,a_1)\). Every solution to the linear equation is \(x=-a/2+uJa\), and \(Q(x)=t/4+tu^2\). Thus its intersection size is exactly
\[
 c(a)=1+\chi\bigl(t(4-t)\bigr),\qquad t=Q(a)\ne0.
\]
Consequently each nonzero shift has zero, one, or two common support points. For \(a=0\), the intersection has \(|S|=p-\epsilon\) points, the standard two-variable quadratic-form count (also obtained by \(\sum_{x\in\mathbb F_p}(1+\chi(1-x^2))\)).

**2. No modulation cancellation on nonempty intersections.** Define the ambiguity coefficient \(A(a,b)=\sum_{x\in S\cap(S-a)}\exp(2\pi i\,b\cdot x/p)\). A sum of one root is nonzero. A sum of two odd-order roots is also nonzero: their quotient cannot be \(-1\). At zero shift the coefficient is the Fourier transform of \(\mathbf1_S\). If it were zero, the number of terms at each \(p\)-th-root exponent would have to be equal, since the cyclotomic polynomial \(1+X+\cdots+X^{p-1}\) is irreducible over \(\mathbb Q\). This would force \(p\mid |S|=p-\epsilon\), impossible. Therefore
\[
 A(a,b)\ne0\quad\Longleftrightarrow\quad a\in S-S,
\]
for every \(b\in V\); the choice \(S\cap(S-a)\) rather than \(S\cap(S+a)\) changes only a reindexing of shifts.

**3. Counting admissible shifts.** The number of \(a\in V\) for which \(Q(a)=t\ne0\) is \(p-\epsilon\), independent of \(t\), by the same quadratic-form count. The quadratic-character identity
\[
\sum_{t\in\mathbb F_p}\chi(t(4-t))=-\epsilon
\]
counts solutions to a separable quadratic and follows, for example, by substituting \(u=t-2\) and counting \(u^2+v^2=4\). Since exactly one \(t\ne0\) has \(t=4\), the number of nonzero norm values having \(\chi(t(4-t))\ge0\) is \((p-\epsilon)/2\). Hence
\[
\lvert S-S\rvert=1+\frac{(p-\epsilon)^2}{2}.
\]
There are \(r_1=r=p-\epsilon\) nonzero shifts with one-point intersection and \(r_2=r(r-2)/2\) with two-point intersection. These sum with the zero shift to the stated support size.

**4. Weyl diagonalization and exact spectral bands.** The \(N^2\) time-frequency Weyl matrices form a Hilbert--Schmidt orthogonal basis. Conjugation by the Weyl group diagonalizes the complete orbit of the rank-one projector \(|g\rangle\langle g|\). The resulting measurement matrix is a Fourier transform on the phase-space group times diagonal multipliers \(A(a,b)\); with the present unnormalized conventions, its singular values are exactly \(\sqrt N\,|A(a,b)|=p|A(a,b)|\). Thus the rank counts nonzero ambiguity coefficients and the nullspace is precisely the Weyl span of the vanishing ones.

For a one-point intersection, \(|A|=1\) at all \(p^2\) frequencies. In a two-point intersection \(\{x,y\}\), write \(d=x-y\ne0\). As \(b\) varies, the value \(b\cdot d\) takes each element of \(\mathbb F_p\) exactly \(p\) times, and
\[
|A(a,b)|=|1+e^{2\pi i(b\cdot d)/p}|=2|\cos(\pi(b\cdot d)/p)|.
\]
The value \(2\) occurs at zero argument, and the remaining positive values \(2\cos(\pi j/p)\), \(1\le j\le(p-1)/2\), occur twice per full set of \(p\) residues. This proves every multiplicity displayed. The zero-shift Fourier magnitudes are nonzero by Step 2, but remain explicitly unevaluated.

**5. Limiting singular-value law.** For each two-point shift, the frequencies give a uniform grid of \(p\) residue classes. The grid \(\{2|\cos(\pi k/p)|:0\le k<p\}\) converges in empirical distribution to the pushforward of uniform Lebesgue measure on \([0,\pi]\), which has density \(2/(\pi\sqrt{4-s^2})\) on \((0,2)\). The total weight of the \(p^2\) zero-shift singular values and the \(p^2r_1=O(p^3)\) one-point singular values, divided by the total positive rank \(R_p=\Theta(p^4)\), tends to zero. Bounded continuous test functions therefore yield the claimed weak limit. This argument does not require tight bounds for the unevaluated zero-shift Fourier magnitudes; their total probability mass vanishes.

## Verification

Run `python3 checks/verify.py` with Python 3; NumPy is needed only for its separate direct lifting-SVD comparison at \(p=3\). The checker enumerates all shifts and modulations for primes \(3,5,7,11\), tests the geometric intersection law and nonvanishing, and confirms the respective ranks \(81,225,1617,8833\). The independent \(81\times81\) complex lifting matrix at \(p=3\) has its entire singular spectrum compared to the ambiguity formula. Finite numerical zero tests use a tolerance and are **not** proofs of the universal nonvanishing result, which follows exactly from cyclotomic irreducibility and odd-order root arithmetic in Step 2.

## Relationship to prior work

Iosevich and Koh [1] study Fourier transforms and extension estimates for finite-field spheres; the inspected paper's sphere Fourier formulas do not give the above operator lifting rank or limiting singular law. Bojarovska and Flinth [2] establish Weyl/Gabor phase-retrieval and frame machinery, but do not calculate this conic window's specific spectral distribution. The closely related hyperbolic quadratic-shell result [3] gives exact rank for a different quadratic form in dimensions \(2r\ge4\) and explicitly excludes dimension two; it also does not state the present two-dimensional conic arcsine law. The proof here uses similar basic Fourier/Weyl machinery, so a stronger unlocated general theorem might subsume the calculation. The theorem makes no unconditional priority assertion.

## Limitations

This is a result for unweighted two-dimensional quadratic-circle indicators over odd prime fields. It does not establish the same assertion over nonprime fields, for weighted windows, for arbitrary conic types, or for higher-dimensional shells. The zero-shift singular values are given as finite character sums, **not** evaluated individually or classified into equality bands; thus the positive spectrum is expressed as a complete parameterized multiset rather than a fully simplified distinct-value table. In particular, no exact positive condition number is asserted. The finite checker is corroborative, not an infinite certificate; a separate independent mathematical audit has not been performed.

## References

1. A. Iosevich and D. Koh, *Extension Theorems for Spheres in the Finite Field Setting*, arXiv:0712.1627v1, publicly posted December 11, 2007, https://arxiv.org/abs/0712.1627.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1, publicly posted March 19, 2015, https://arxiv.org/abs/1503.05800.
3. *Exact Gabor tomography rank for hyperbolic quadratic shells over odd finite fields*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-gabor-tomography-rank-for-hyperbolic-quadratic-shells-over--b9e240edb677.
