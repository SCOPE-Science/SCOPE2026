# Sharp anisotropic lower bound and diamond rigidity for the Cartesian numerical radius

## Finding

Let \(T=H+iK\) be a bounded operator on a nonzero complex Hilbert space, with \(H=H^*\), \(K=K^*\), and \(r=\|H\|\), \(s=\|K\|\). Its squared \(L^2\)-Cartesian numerical radius is
\[
Q_2(T)^2=\frac1{2\pi}\int_0^{2\pi}\|H\cos\theta+K\sin\theta\|^2\,d\theta.
\]
For \(r>0\), the sharp, jointly norm-constrained inequality is
\[
\boxed{Q_2(T)^2\ge \frac{r^2}{2}+\frac{rs+(s^2-r^2)\arctan(s/r)}{\pi}.}
\]
For \(r=0\), the right sharp bound is \(s^2/2\). The formula is symmetric in \(r,s\), although displayed asymmetrically. In particular, with \(r>0\) fixed and \(s\downarrow0\), the optimal excess is
\[
\frac{4s^3}{3\pi r}+O\!\left(\frac{s^5}{r^3}\right).
\]
Define the compact central symmetrization of the numerical range by
\[
C_T=\operatorname{conv}\big(\overline{W(T)}\cup-\overline{W(T)}\big)\subset\mathbb C,
\quad W(T)=\{\langle Tx,x\rangle:\|x\|=1\}.
\]
**Complete equality criterion:** equality holds precisely when
\[
C_T=\operatorname{conv}\{r,-r,is,-is\}.
\]
All pairs \(r,s\ge0\) occur as equality cases. A universal extremizer is \(T=\operatorname{diag}(r,-r,is,-is)\); unused repeated entries may be omitted when one parameter is zero.

## Assumptions and scope

There is no normality, commutativity, finite-dimensionality, compactness, or invertibility hypothesis. The underlying Hilbert space is complex and nonzero. Operator norms are the usual induced Hilbert-space norms. For \(r,s>0\), the equality diamond is two-dimensional; the degenerate cases \(r=0\) or \(s=0\) reduce to a segment. The extremal normal diagonal example demonstrates optimality **among all operators**, including nonnormal ones.

## Proof

**Symmetric numerical support.** View \(\mathbb C\) as \(\mathbb R^2\). Since the numerical range is bounded, its closure is compact. The convex set \(C=C_T\) is compact and centrally symmetric. Its support function
\[
h_C(\theta)=\sup_{z\in C}\operatorname{Re}(e^{-i\theta}z)
=\|H\cos\theta+K\sin\theta\|
\]
is nonnegative and continuous. The equality follows because the absolute quadratic-form maximum of a self-adjoint operator equals its norm. Therefore \(Q_2(T)^2=(2\pi)^{-1}\int h_C(\theta)^2d\theta\). Its horizontal and vertical support radii are exactly \(r,s\).

**Symmetrization without loss.** Let \(\overline C=\{\overline z:z\in C\}\) and form the Minkowski average \(D=(C+\overline C)/2\). Its support satisfies
\[
h_D(\theta)=\tfrac12\big(h_C(\theta)+h_C(-\theta)\big).
\]
Pointwise convexity of the square gives
\[
\frac1{2\pi}\int h_D^2\le \frac1{2\pi}\int h_C^2.
\]
The set \(D\) is compact, centrally symmetric, and invariant under both coordinate reflections. Because \(C\) has an extreme point with real part \(r\), averaging it with its conjugate puts \(r\in D\); central symmetry gives \(-r\in D\). Likewise, if \(x+is\in C\), average it with \(-x+is\in\overline C\) to obtain \(is\in D\), and similarly \(-is\in D\). Hence
\[
E_{r,s}=\operatorname{conv}\{r,-r,is,-is\}\subseteq D,
\quad h_D(\theta)\ge h_{E_{r,s}}(\theta)=\max\{r|\cos\theta|,s|\sin\theta|\}.
\]
Combining these two inequalities gives the claimed bound as the squared support integral of the diamond.

**Exact integral and endpoints.** For \(r>0\), integration on one quadrant with crossover angle \(\arctan(r/s)\) yields
\[
\frac2\pi\int_0^{\pi/2}\max\{r^2\cos^2\theta,s^2\sin^2\theta\}\,d\theta
=\frac{r^2}{2}+\frac{rs+(s^2-r^2)\arctan(s/r)}\pi.
\]
The limiting cases \(s=0\) or \(r=0\) follow directly from the elementary trigonometric average. Taylor expansion of \(\arctan(s/r)\) gives the cubic coefficient and its stated remainder.

**Rigidity.** If equality holds in the integrated chain, then strict convexity of the real square, applied to the nonnegative continuous support functions, forces \(h_C(\theta)=h_C(-\theta)\) for every angle. Therefore \(C=\overline C=D\). The second inequality can be equality only if \(h_D=h_{E_{r,s}}\) at every angle, since both are continuous and nonnegative, and \(h_D\ge h_{E_{r,s}}\). By uniqueness of support functions, \(C=D=E_{r,s}\). Conversely, that equality of convex sets makes both inequalities equalities. The indicated four-point diagonal normal operator has exactly this central numerical-range hull and attains the bound.

## Verification

The proof reduces the universal operator assertion to two elementary facts: the support function of a Minkowski average is the average of support functions, and support determines a compact convex set. The complete crossover integral can be checked by differentiating the displayed antiderivative and evaluating at \(\arctan(r/s)\). The companion `verify.py` checks several exact limiting identities and bounded numerical quadratures; numerical experiments are not a proof of the universal inequality.

## Relationship to prior work

Audeh, Kittaneh, Moradi and Sahoo [1] introduced the angular \(L^2\)-Cartesian numerical radius, proved the sharp global \(\omega(T)/\sqrt2\) comparison, and gave general upper and lower estimates. Those estimates do not specify the **sharp joint dependence** on both Cartesian operator norms or characterize all equality numerical-range shapes. A related published result [2] proves a cubic stability inequality relative to phase-self-adjoint operators and computes the same cubic asymptotic on one four-dimensional diagonal example. That particular example and its asymptotic are explicitly prior evidence, not separately claimed as novel. Its general stability estimate does not yield the present exact two-parameter minimum or the universal diamond rigidity: the latter follows from the independent Minkowski-support symmetrization above.

## Limitations

The equality criterion characterizes the centrally symmetrized **numerical range**, not the operator up to unitary similarity. The formula is orientation dependent: it fixes the given real and imaginary parts and is not invariant under arbitrary phase rotations of \(T\). No stronger assertion about Schatten distances, non-Hilbert Banach spaces, or arbitrary Cartesian moment exponents is made. Priority remains subject to a broader convex-support inequality possibly being recorded in older literature under geometric terminology. Independent validation has not been performed.

## References

[1] W. Audeh, F. Kittaneh, H. R. Moradi, S. Sahoo, *The \(L^2\)-Cartesian Numerical Radii of Hilbert Space Operators*, arXiv:2610.04844v1, publicly submitted 4 October 2026; https://arxiv.org/abs/2610.04844.

[2] *Cubic operator-norm stability for the \(L^2\)-Cartesian numerical radius*, publicly available mathematical record dated 11 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cubic-operator-norm-stability-for-the-l-2-cartesian-numerical-ra--ffd07fee0727.
