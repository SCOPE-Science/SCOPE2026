# Balanced two-ray phase retrieval from \(4d\) intensities with sharp angular resonance

## Finding

**Theorem.** Let \(d\ge1\) and \(0<\theta<\pi\), and suppose
\[
\sin(m\theta)\ne0\qquad(1\le m\le d).
\]
Choose arbitrary *distinct positive* numbers \(r_{0,1},\ldots,r_{0,2d}\) on the first ray and distinct positive numbers \(r_{1,1},\ldots,r_{1,2d}\) on the second ray. Assume the two radial products are unequal:
\[
\prod_{j=1}^{2d}r_{0,j}\ne\prod_{j=1}^{2d}r_{1,j}.
\]
Then the \(4d\) real numbers
\[
\bigl|p(r_{0,j})\bigr|^2,\qquad
\bigl|p(r_{1,j}e^{i\theta})\bigr|^2\qquad(1\le j\le2d)
\]
determine **every** complex polynomial \(p\) of degree at most \(d\), including zero and polynomials with missing endpoint coefficients, up to multiplication by a unit complex number.

More strongly, they recover *linearly* the two entire real polynomials \(P_0(t)=|p(t)|^2\) and \(P_1(t)=|p(te^{i\theta})|^2\), each of degree at most \(2d\). The number \(4d\) is optimal for linear recovery of the **two whole profiles** from point evaluations (not claimed optimal for arbitrary nonlinear phase retrieval designs).

The angular condition is sharp independent of the radial nodes: if \(\sin(m\theta)=0\) for some \(1\le m\le d\), distinct degree-at-most-\(d\) polynomials have equal magnitudes at every point of both entire rays. In particular, the explicit design \(\theta=\pi/(d+1)\), \(r_{0,j}=j/(4d+2)\) and \(r_{1,j}=(j+1)/(4d+2)\), \(1\le j\le2d\), meets all hypotheses with positive radii below one.

## Assumptions and scope

The origin is the intersection of the two rays, but it need not be sampled. The angle is oriented and lies strictly between zero and \(\pi\). A degree bound is fixed in advance; the true degree may be smaller. The nonresonance condition is equivalent to saying that \(\theta/\pi\) is irrational or, in lowest rational terms, has denominator greater than \(d\).

All intensities are ideal exact numbers. No uniform numerical condition bound is asserted as \(d\) grows, as two nodes coalesce, as the radial products approach each other, or as an angular resonance is approached.

## Proof

**1. Exact simultaneous intensity-profile interpolation.** For \(i\in\{0,1\}\), let \(\alpha_0=0\), \(\alpha_1=\theta\) and let \(I_i\) be the unique real polynomial of degree at most \(2d-1\) taking the measured intensities at the \(2d\) distinct radii on ray \(i\). Let
\[
V_i(t)=\prod_{j=1}^{2d}(t-r_{i,j}).
\]
Because \(P_i\) has degree at most \(2d\), there is a real constant \(c_i\) such that \(P_i=I_i+c_iV_i\). Its leading coefficient equals \(\lvert a_d\rvert^2\), where \(p(z)=\sum_{j=0}^{d}a_jz^j\), independently of the ray. Thus \(c_0=c_1=c=\lvert a_d\rvert^2\). Both profiles also have common constant coefficient \(\lvert a_0\rvert^2\). Evaluating at zero gives
\[
I_0(0)+cV_0(0)=I_1(0)+cV_1(0),\qquad
c=\frac{I_1(0)-I_0(0)}{V_0(0)-V_1(0)}.
\]
Since \(2d\) is even, \(V_i(0)=\prod_jr_{i,j}\), so the denominator is nonzero by assumption. This determines both complete profiles explicitly, with a linear dependence on the measured squared intensities. No leading-coefficient or nonvanishing assumption on \(p\) was required.

**2. Two-ray uniqueness at a bounded degree.** Suppose \(p,q\) have the same profiles. If \(p=0\), the profile of \(q\) vanishes everywhere and \(q=0\). Otherwise, equality of the profiles near zero shows that \(p\) and \(q\) vanish to the same order \(\nu\) at zero. Hence \(h=q/p\) is holomorphic and nonzero in a sufficiently small neighbourhood of zero, and \(|h|=1\) on both short radial segments. Write \(h(z)=c_0+c_kz^k+O(z^{k+1})\), with \(|c_0|=1\) and \(c_k\ne0\), if \(h\) is not constant. Because \(q-c_0p=p(h-c_0)\) is a nonzero polynomial of degree at most \(d\), its vanishing order at zero is \(\nu+k\le d\); therefore \(1\le k\le d\).

The order-\(k\) term of \(\lvert h(te^{i\alpha})\rvert^2-1\) is \(2\operatorname{Re}(\overline{c_0}c_ke^{ik\alpha})t^k\). It must vanish for \(\alpha=0\) and \(\alpha=\theta\). A nonzero complex coefficient can satisfy both real equations only if \(\sin(k\theta)=0\), contrary to assumption. Therefore \(h=c_0\) and \(q=c_0p\) everywhere.

**3. Necessity of the angular condition.** If \(\sin(m\theta)=0\) for some \(m\in\{1,\ldots,d\}\), define \(p(z)=1+iz^m\) and \(q(z)=1-iz^m\). For any positive \(t\), both \(t^m\) and \(t^me^{im\theta}\) are real. Thus \(\lvert p(t)\rvert=\lvert q(t)\rvert\) and \(\lvert p(te^{i\theta})\rvert=\lvert q(te^{i\theta})\rvert\). The two polynomials are not global-phase multiples. No finite or infinite collection restricted to these rays can repair this obstruction.

**4. Optimality within linear recovery of the whole profile pair.** Every pair \((P_0,P_1)\) lies in the real \(4d\)-dimensional vector space
\[
\mathcal V_d=\{(F_0,F_1):\deg F_i\le2d,\ F_0(0)=F_1(0),\ [t^{2d}]F_0=[t^{2d}]F_1\}.
\]
We show that the *real linear span* of actual intensity-profile pairs equals \(\mathcal V_d\). Write \(P_i(t)=\sum_{j,\ell=0}^dH_{j\ell}e^{i(j-\ell)\alpha_i}t^{j+\ell}\), with \(H=aa^*\) Hermitian. Since real linear combinations of rank-one Hermitian matrices exhaust all Hermitian matrices, it suffices to analyze the resulting linear map in \(H\). The diagonal entries \(H_{00}\) and \(H_{dd}\) independently give the common constant and leading coefficients. For each intermediate degree \(k\in\{1,\ldots,2d-1\}\), choose \((j,\ell)=((k+1)/2,(k-1)/2)\) if \(k\) is odd, and \((j,\ell)=(k/2+1,k/2-1)\) if \(k\) is even. These indices lie between zero and \(d\). Changing the real and imaginary parts of \(H_{j\ell}\) produces arbitrary prescribed coefficients of \(t^k\) in both profiles because the corresponding determinant is a nonzero multiple of \(\sin((j-\ell)\theta)\), with \(j-\ell\in\{1,2\}\subseteq\{1,\ldots,d\}\) whenever the even case exists. All other degrees are unchanged. Thus the span is all of \(\mathcal V_d\). Any linear reconstruction of every full profile pair from scalar evaluations needs at least \(\dim\mathcal V_d=4d\) measurements, and the construction meets this bound.

Indeed, for the specified balanced \(2d+2d\) sampling topology, unequal radial products are exactly the condition for invertibility of this **linear profile-space evaluation map**: if the products agree, the nonzero pair \((V_0,V_1)\in\mathcal V_d\) is annihilated by every sample. This final equivalence concerns profile-space linear invertibility, not necessarily nonlinear phase retrieval when products agree.

## Verification

The self-contained `verify.py` implements Lagrange interpolation and the common leading/constant-coefficient formula, compares both reconstructed complete polynomial profiles with direct coefficient expansions, tests all lower angular resonances through degree eight, and includes an exact-rational degree-one identity. Execute with `python verify.py`; Python 3 and `mpmath` are required. High-precision arithmetic is used because naive floating-point interpolation at clustered radii can be ill-conditioned. The completed run printed `TWO_RAY_PROFILE_CHECKS_PASS 5355 degrees 1..6 plus resonant boundaries 1..8`.

The exhaustive analytical arguments in the Proof section, not the bounded computational tests, establish the universal quantifiers and endpoint cases.

## Relationship to prior work

Perez (2020) and Chalendar–Partington (2024) establish phase uniqueness for analytic functions from **continuous data** on two intersecting lines at irrational angle. Their statements do not give a finite balanced two-ray sampling design or the bounded-degree rational-angle threshold. Bodmann–Hammen (2013) prove a \(4d\)-measurement existence construction for degree-at-most-\(d\) polynomials on **two intersecting circles** (also using a conformal transformation to lines); the explicit distribution in their theorem differs from balanced radial samples, and their result does not state arbitrary unequal-product radial designs or sharp rational-angle classification. The total \(4d\) budget alone is not claimed as new. Pohl–Li–Boche (2017) give another two-circle finite design. The new statement isolates an exact algebraic sampling criterion and a full-profile linear reconstruction of two *rays*.

## Limitations

Historical priority for the particular balanced radial sampling theorem is provisional; it could be subsumed by an unidentified general theorem on polynomial-frame phase retrieval. This result proves no universal lower bound for the number of **nonlinear** phaseless measurements and no noise-uniform condition number. The inverse interpolation map becomes badly conditioned when radial nodes cluster or when the two radial products nearly coincide. The necessity of unequal products is shown for the linear full-profile interpolation method, not for arbitrary nonlinear phase retrieval from the same points.

## References

1. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (first posted 2024-03-24), Section 2.1. https://arxiv.org/abs/2403.16255
2. R. Perez III, *A Note on the Phase Retrieval of Holomorphic Functions*, arXiv:2009.02061 (2020), Theorem on two intersecting segments. https://arxiv.org/abs/2009.02061
3. B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487 (2013), Lemma 2.2 and Theorem 2.3. https://arxiv.org/abs/1302.5487
4. V. Pohl, F. Li, and H. Boche, *Phase retrieval in spaces of analytic functions on the unit disk*, 2017; two-circle finite sampling construction (https://doi.org/10.1109/SAMPTA.2017.8024411).
