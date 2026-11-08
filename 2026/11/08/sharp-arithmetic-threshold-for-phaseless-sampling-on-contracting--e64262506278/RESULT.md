# Sharp arithmetic threshold for phaseless sampling on contracting complex spirals

## Finding

Fix a nonzero complex contraction \(\lambda=\rho e^{i\theta}\) with \(0<\rho<1\). Define its angular denominator
\[
q(\theta)=\min\{k\ge1:k\theta\in\pi\mathbb Z\},
\]
with \(q(\theta)=\infty\) when the set is empty. For every integer \(d\ge0\), magnitudes of every polynomial \(p\) of degree at most \(d\) on the geometric spiral \(\{\lambda^n:n\ge1\}\) determine \(p\) up to a constant phase **if and only if** \(d<q(\theta)\). In this regime the *first* \((d+1)^2\) squared magnitudes already reconstruct the complete coefficient outer-product matrix by a nonsingular complex Vandermonde system. This sample count is optimal for linear reconstruction of the full ambient intensity profile, not claimed minimal for nonlinear phase retrieval.

Furthermore, on any connected open domain \(\Omega\) containing \(0\) and the spiral, the infinite set of magnitudes \(\{|f(\lambda^n)|:n\ge1\}\) determines **every holomorphic** \(f\in\mathcal O(\Omega)\) up to constant phase if and only if \(\theta/\pi\) is irrational. Thus the same one-point-per-radius sampling geometry has a sharp rational/irrational uniqueness dichotomy.

## Assumptions and scope

The contraction \(\lambda\) is fixed, \(0<|\lambda|<1\); samples are exact, noiseless, and indexed by consecutive positive integers. Polynomial coefficients and holomorphic functions are complex. The set \(\Omega\subseteq\mathbb C\) is open and connected and contains the origin and all sampling points. All quantifiers include the zero function. Two functions are considered equivalent exactly when \(f=cg\) on \(\Omega\), with \(|c|=1\). For polynomials, equivalence is as polynomials on \(\mathbb C\).

When \(\theta/\pi=a/q\) in lowest terms, the above denominator is exactly \(q\), irrespective of the parity or sign of \(a\); for irrational \(\theta/\pi\), it is infinite. The case \(d=0\) is included.

## Proof

**Exact finite polynomial threshold.** Write \(p(z)=\sum_{a=0}^d c_a z^a\). Its full intensity profile is
\[
|p(z)|^2=\sum_{a,b=0}^d H_{ab}z^a\overline z^{\,b},\qquad H_{ab}=c_a\overline{c_b}.
\]
Put \(N=(d+1)^2\) and \(t_{ab}=\lambda^a\overline\lambda^{\,b}\). The observations \(y_n=|p(\lambda^n)|^2\) satisfy
\[
y_n=\sum_{a,b=0}^d H_{ab}t_{ab}^{n}\quad(1\le n\le N).
\]
Consequently the reconstruction matrix is the Vandermonde matrix \(V_{n,(a,b)}=t_{ab}^{n}\), and its determinant, up to the sign determined by the column ordering, is
\[
\det V=\biggl(\prod_{a,b}t_{ab}\biggr)\prod_{(a,b)<(c,e)}(t_{ce}-t_{ab}).
\]
All nodes are nonzero. If two nodes agree, equality of their absolute values gives \(a+b=c+e\), since \(0<\rho<1\). Equality of phases then becomes
\[
e^{2i(a-c)\theta}=1\quad\Longleftrightarrow\quad (a-c)\theta\in\pi\mathbb Z.
\]
Because \(|a-c|\le d\), the nodes are pairwise distinct precisely when \(d<q(\theta)\). Then \(V\) is invertible and recovers all \(H_{ab}\). If \(H\ne0\), choose an index \(s\) with \(H_{ss}>0\); the coefficients \(\widehat c_a=H_{as}/\sqrt{H_{ss}}\) recover \(p\) up to a common phase. When \(H=0\), necessarily \(p=0\).

The real vector space of Hermitian \((d+1)\)-by-\((d+1)\) matrices has dimension \(N\). Rank-one Hermitian matrices \(cc^*\) span it over \(\mathbb R\), and the map \(H\mapsto\sum H_{ab}z^a\overline z^{\,b}\) is injective as a real-polynomial identity on \(\mathbb C\) (independence of the mixed monomials follows by converting to two real coordinates, or by polar Fourier coefficients). Thus the linear span of complete polynomial intensity profiles has dimension \(N\), so fewer than \(N\) real scalar observations cannot reconstruct **every such profile linearly**. This is not a lower bound on nonlinear phase retrieval from actual rank-one profiles.

If \(q(\theta)\le d\), every sampling point has \((\lambda^n)^q\in\mathbb R\). The two inequivalent degree-\(q\) polynomials
\[
p_+(z)=1+i z^q,\qquad p_-(z)=1-i z^q
\]
have identical magnitudes at **every** spiral point. This proves necessity for all sampling lengths, not just the first \(N\).

**Holomorphic uniqueness.** Suppose \(\theta/\pi\) is irrational and \(f,g\in\mathcal O(\Omega)\) have the same magnitudes at every spiral point. If either vanishes identically, the identity theorem shows both do. Otherwise, comparing their zero orders at the accumulation point \(0\), using the modulus equality and \(\lambda^n\to0\), shows that the zero orders are equal. Divide off the common power of \(z\) and form the holomorphic quotient \(h\) near \(0\). Then \(|h(\lambda^n)|=1\) and \(|h(0)|=1\).

If \(h\) is not constant near \(0\), let \(k\ge1\) be the degree of its first nonconstant Taylor term: \(h(z)=c_0+c_k z^k+O(z^{k+1})\), with \(|c_0|=1\), \(c_k\ne0\). Expanding the squared modulus yields
\[
0=|h(\lambda^n)|^2-1=2\rho^{kn}\operatorname{Re}(\overline{c_0}c_k e^{ikn\theta})+O(\rho^{(k+1)n}).
\]
After division by \(\rho^{kn}\), this requires \(\operatorname{Re}(\overline{c_0}c_k e^{ikn\theta})\to0\). But \(k\theta/(2\pi)\) is irrational, so its rotation orbit is dense on the circle, and the nonzero cosine function cannot converge to zero along that orbit. Contradiction. Hence \(h\) is constant of modulus one near \(0\), and the identity theorem extends the relation to \(\Omega\). If \(\theta/\pi\) is rational, the same polynomials \(1\pm iz^q\) give a counterexample, proving necessity.

## Verification

A standalone exact-arithmetic checker (`verify_spiral.py`) tests the nonresonant bases for degrees up to four at the algebraic contraction \((2+i)/5\), verifies three rational angular threshold examples, and exactly reconstructs a quadratic coefficient outer product by a nine-by-nine Vandermonde inversion. For \(\lambda=(2+i)/5\), the ratio \(\lambda/\overline\lambda=(3+4i)/5\) lies in \(\mathbb Q(i)\) but is not among its only roots of unity \(\{1,-1,i,-i\}\); hence its argument divided by \(\pi\) is irrational. Run `python verify_spiral.py` with Python 3 and SymPy. The finite computations check examples and are not substitutes for the proofs of the universal assertions.

## Relationship to prior work

Perez, *A Note on the Phase Retrieval of Holomorphic Functions* (arXiv:2009.02061, first public September 4, 2020), proves uniqueness from two intersecting line segments with irrational intersection angle. Chalendar and Partington, *Phase retrieval on circles and lines* (arXiv:2403.16255, first public March 24, 2024), prove related two-segment and sequential two-fixed-ray assertions; their Corollary 2.5 requires infinitely many observations on **each** of two fixed rays. The present spiral with irrational turning angle contains at most one point on each ray through its accumulation point, so those hypotheses cannot be applied to it. This result also gives an exact **finite-degree** angular denominator threshold and a consecutive-prefix Vandermonde reconstruction not provided by those assertions.

Liehr, *Arithmetic progressions and holomorphic phase retrieval* (arXiv:2308.05722, first public August 10, 2023), characterizes phase-retrieving unions of parallel full lines in an entire-function setting; it does not supply the contracting-spiral criterion. Grohs, Liehr and Rathmair, *Phase retrieval in Fock space and perturbation of Liouville sets* (arXiv:2308.00385, first public August 1, 2023), treats separated/unbounded multi-set sampling configurations in Fock space; these do not imply the accumulation-point spiral criterion. Generic finite polynomial phase-retrieval results can use fewer samples than \(N\); the novelty claimed here is the arithmetic iff criterion and exact full-profile reconstruction on a prescribed geometric progression, not an optimal general measurement count.

## Limitations

No noise stability, quantitative conditioning, or polynomial-degree-uniform reconstruction bounds are proved. The Vandermonde condition number can be very large for clustered spiral nodes. A finite sample prefix cannot determine arbitrary unrestricted holomorphic functions. Historical priority remains provisional: a broader published real-analytic uniqueness-set theorem might imply the spiral result even if it does not mention phase retrieval or spirals explicitly. The fixed-geometry iff classification and proof do not assert independent verification.

## References

1. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255, first public 2024-03-24, especially Theorem 2.1 and Corollary 2.5.
2. R. Perez III, *A Note on the Phase Retrieval of Holomorphic Functions*, arXiv:2009.02061, first public 2020-09-04, especially Theorem 2.1.
3. L. Liehr, *Arithmetic progressions and holomorphic phase retrieval*, arXiv:2308.05722, first public 2023-08-10, Theorem 1.1.
4. P. Grohs, L. Liehr, and M. Rathmair, *Phase retrieval in Fock space and perturbation of Liouville sets*, arXiv:2308.00385, first public 2023-08-01, especially Theorem 2.4.
