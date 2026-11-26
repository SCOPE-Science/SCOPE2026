# Sharp geometric stability of the fourth-moment comparison for Hilbert martingales

## Finding

For a finite real-Hilbert-space martingale with deterministic increment lengths, the fourth-moment deficit relative to the matching independent Rademacher sum is exactly an accumulated squared transverse increment. Furthermore that deficit is comparable, with **optimal universal constants**, to the energy-weighted squared distance of each increment from the two signed radial directions. This classifies all equality cases, including changes of direction after returns to the origin.

Let \(H\) be a real Hilbert space, \((\mathcal F_k)_{k=0}^{n}\) a filtration, and \((M_k)_{k=0}^{n}\) an adapted martingale with \(M_0=0\). Write \(X_k=M_k-M_{k-1}\) and assume \(\|X_k\|=a_k\) almost surely for deterministic \(a_k\ge0\). Let \(\varepsilon_k\) be independent fair signs, \(S_n=\sum_{k=1}^n a_k\varepsilon_k\), and

\[
D_n=\mathbb E S_n^4-\mathbb E\|M_n\|^4.
\]

For \(M_{k-1}\ne0\) and \(a_k>0\), put \(u_{k-1}=M_{k-1}/\|M_{k-1}\|\), \(c_k=|\langle u_{k-1},X_k\rangle|/a_k\), and \(d_k=\min_{\sigma\in\{-1,1\}}\|X_k-\sigma a_ku_{k-1}\|\). Set \(c_k=d_k=0\) on the other events, and define \(R_n=\sum_{k=1}^n\mathbb E[\|M_{k-1}\|^2d_k^2]\).

The exact defect identity and sharp two-sided stability law are

\[
D_n=4\sum_{k=1}^n\mathbb E\!\left[a_k^2\|M_{k-1}\|^2-\langle M_{k-1},X_k\rangle^2\right]
=2\sum_{k=1}^n\mathbb E\!\left[(1+c_k)\|M_{k-1}\|^2d_k^2\right],
\]

\[
\boxed{\frac{D_n}{4}\le R_n\le\frac{D_n}{2}.}
\]

Both constants are optimal uniformly over real Hilbert spaces of dimension at least two and over all positive deterministic length vectors. Also \(D_n=0\) **if and only if** each \(X_k\) is parallel to \(M_{k-1}\) almost surely on \(\{a_k>0,M_{k-1}\ne0\}\). On that event its conditional law given \(\mathcal F_{k-1}\) must be the uniform two-point law on \(\{\pm a_ku_{k-1}\}\). At zero-valued previous states there is no directional restriction beyond conditional centering and fixed length.

## Assumptions and scope

The martingale is finite-horizon, has its initial state fixed at zero, and takes values in any real Hilbert space. The filtration may be arbitrary; increments need not be independent, conditionally symmetric, or supported on a fixed line. Their **lengths**, not merely upper bounds, are deterministic. All moments exist automatically because the increments are bounded. Sharpness of both universal comparison factors uses the Euclidean plane and two increments. At \(a_k=0\) the increment is identically zero.

## Proof

Write \(V=M_{k-1}\), \(X=X_k\). The martingale property gives \(\mathbb E[X\mid\mathcal F_{k-1}]=0\); the fixed-length hypothesis gives \(\|X\|^2=a_k^2\) almost surely. Expanding the exact quartic polynomial,

\[
\|V+X\|^4=(\|V\|^2+a_k^2)^2+4(\|V\|^2+a_k^2)\langle V,X\rangle+4\langle V,X\rangle^2.
\]

After conditional expectation and then ordinary expectation,

\[
\mathbb E\|M_k\|^4-\mathbb E\|M_{k-1}\|^4
=a_k^4+2a_k^2\mathbb E\|M_{k-1}\|^2+4\mathbb E\langle M_{k-1},X_k\rangle^2.
\]

The predictable quadratic recursion likewise gives \(\mathbb E\|M_{k-1}\|^2=\sum_{i<k}a_i^2\). For \(S_k=\sum_{i\le k}a_i\varepsilon_i\), independence and sign symmetry instead give

\[
\mathbb E S_k^4-\mathbb E S_{k-1}^4
=a_k^4+6a_k^2\sum_{i<k}a_i^2.
\]

Subtracting and summing proves the first exact defect formula. Each summand is nonnegative by Cauchy--Schwarz. When both \(a_k\) and \(\|M_{k-1}\|\) are positive, elementary Hilbert geometry gives

\[
d_k^2=2a_k^2(1-c_k),\qquad
 a_k^2\|M_{k-1}\|^2-\langle M_{k-1},X_k\rangle^2=a_k^2\|M_{k-1}\|^2(1-c_k^2).
\]

Thus the summand multiplied by four is exactly \(2(1+c_k)\|M_{k-1}\|^2d_k^2\). This also holds on the zero events, where both expressions vanish. Since \(0\le c_k\le1\), the sharp universal inequalities follow. Vanishing of the sum of nonnegative transverse defects is equivalent to radial alignment on every nonzero-state event. Conditional centering forces the two signs to have probability \(1/2\) each given the past. The converse is immediate; when the preceding state is zero, the weighted angular term is identically zero regardless of direction.

For sharpness, take \(H=\mathbb R^2\), \(n=2\), \(a_1=a_2=1\), \(X_1=\varepsilon_1e_1\) and \(X_2=\varepsilon_2(\cos\theta\,e_1+\sin\theta\,e_2)\), with independent fair signs and \(0<\theta\le\pi/2\). Direct computation gives \(D_2=4\sin^2\theta\), \(R_2=2(1-\cos\theta)\), and \(R_2/D_2=1/[2(1+\cos\theta)]\). The endpoint \(\theta=\pi/2\) attains the factor \(1/2\); letting \(\theta\downarrow0\) proves the factor \(1/4\) cannot be increased. This completes the theorem.

## Verification

Run `python3 CHECK.py` using Python 3's standard library. The checker exhaustively enumerates exact rational two-step and adaptive three-/four-step finite sign trees; it tests the exact quartic identity and the two-sided bounds, both sharp-factor constructions, and an equality example in which the direction resets after a zero state. The analytic proof above covers every horizon and real Hilbert space; the finite checker is corroborative, not an infinite proof.

## Relationship to prior work

Juškevičius and Šileikis, *Concentration inequalities for vector-valued martingales*, arXiv:2610.31449v1, Theorem 3 and Lemma 6, establish comparison with a weighted Rademacher sum under the broader assumption of bounded (rather than fixed) increment lengths and a class of convex functions, including the fourth power. That theorem already supplies \(D_n\ge0\); its collinear one-step extremizer is also acknowledged. The claim here is **not** the fourth-moment inequality itself. It is the exact accumulated transverse-defect identity, the sharp two-sided comparison with geometric distance, and the complete equality description permitting direction changes at returns to zero. The cited work does not explicitly provide this stability law.

Pinelis, *Optimum bounds for the distributions of martingales in Banach spaces*, Annals of Probability 22 (1994), supplies important classical vector-valued martingale concentration and moment inequalities; those broader inequality results are not presented as new here.

## Limitations

The exact identity uses deterministic fixed increment lengths and is not asserted for general norm upper bounds or random predictable lengths. The stability distance is weighted by \(\|M_{k-1}\|^2\): small deficit need not impose a chosen direction immediately following a visit to zero. No universal unweighted trajectory-distance result, maximal-tail stability theorem, or claim of independent validation follows. Existing broader martingale-stability theory may encode the same equality and defect formulas in a different language; priority should be checked independently before publication.

## References

1. T. Juškevičius and M. Šileikis, *Concentration inequalities for vector-valued martingales*, arXiv:2610.31449v1 (first posted October 22, 2026), https://arxiv.org/html/2610.31449v1.
2. I. Pinelis, *Optimum bounds for the distributions of martingales in Banach spaces*, Annals of Probability 22 (1994), 1679--1706, DOI:10.1214/aop/1176988477, https://arxiv.org/abs/1208.2200.
