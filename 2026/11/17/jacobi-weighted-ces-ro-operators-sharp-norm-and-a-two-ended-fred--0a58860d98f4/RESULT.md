# Jacobi-weighted Cesàro operators: sharp norm and a two-ended Fredholm phase diagram

## Finding

For parameters \(1<p<\infty\), \(-1<\gamma<p-1\), and \(\delta>-1\), let
\[
X_{p,\gamma,\delta}=L^p((0,1),x^\gamma(1-x)^\delta\,dx;\mathbb C),\qquad
(Cf)(x)=\frac1x\int_0^x\frac{f(t)}{1-t}\,dt.
\]
Put
\[
A=\frac{p-1-\gamma}{p},\quad B=\frac{\delta+1}{p},\quad m=\min(A,B),\quad M=\max(A,B),
\]
and, for \(t>0\), let \(\Gamma_t=\{\lambda\in\mathbb C:|\lambda-1/(2t)|=1/(2t)\}\). Then \(C\) is bounded, has *sharp nonattained norm* \(\|C\|=1/m\), and
\[
\sigma(C)=\{0\}\cup\{\lambda\in\mathbb C\setminus\{0\}:m\le\operatorname{Re}(1/\lambda)\le M\},
\qquad \sigma_{\mathrm{ess},F}(C)=\Gamma_A\cup\Gamma_B,
\]
where \(\sigma_{\mathrm{ess},F}\) denotes the set where \(C-\lambda I\) is not Fredholm.

At a nonzero parameter satisfying \(m<\operatorname{Re}(1/\lambda)<M\):

* If \(A<B\), equivalently \(p<\gamma+\delta+2\), \(C-\lambda I\) is onto with one-dimensional kernel, Fredholm index \(+1\). Its eigenvectors are multiples of
  \[
  f_\lambda(x)=x^{1/\lambda-1}(1-x)^{-1/\lambda}.
  \]
* If \(A>B\), equivalently \(p>\gamma+\delta+2\), \(C-\lambda I\) is one-to-one with closed codimension-one range, Fredholm index \(-1\); its range is exactly the kernel of the continuous nonzero functional
  \[
  \mathcal L_\lambda(h)=\int_0^1 h(x)x^{-1/\lambda}(1-x)^{1/\lambda-1}\,dx.
  \]

At every \(\lambda\notin\sigma(C)\) the operator \(C-\lambda I\) is invertible. At every point of \(\Gamma_A\cup\Gamma_B\), including zero, \(C-\lambda I\) is injective with dense nonclosed range. The equal-endpoint phase \(A=B\) occurs exactly when \(p=\gamma+\delta+2\); then the spectrum and Fredholm essential spectrum coincide in a single circle, with empty point and residual spectra. The unweighted choice \(\gamma=\delta=0\) recovers the familiar phase change at \(p=2\), but other weights independently move the two endpoints and the transition.

## Assumptions and scope

All Banach spaces are complex. Integrals are Lebesgue integrals and the operator is initially defined on compactly supported smooth functions, then extended continuously. The stated \(p,\gamma,\delta\) restrictions ensure that \(A,B\) are strictly positive. The result concerns the kernel \(1/(1-t)\), not the ordinary Hardy averaging kernel. In the case \(A=B\), the two boundary circles are the same circle, rather than the boundary of an annulus of positive width. The Fredholm essential spectrum here is defined by the failure of Fredholmness (not a convention that additionally removes nonzero-index points).

## Proof

**1. Exact logistic similarity.** Set
\[
 y=\log\frac{x}{1-x},\qquad x=\frac{e^y}{1+e^y},\qquad (Uf)(y)=x f(x),
 \qquad \rho(y)=e^{-pAy}(1+e^y)^{p(A-B)}.
\]
Since \(dx=x(1-x)\,dy\), direct substitution gives
\[
 \int_0^1|f(x)|^p x^\gamma(1-x)^\delta\,dx
  =\int_{\mathbb R}|Uf(y)|^p\rho(y)\,dy.
\]
Thus \(U\) is an onto isometry into \(Y=L^p(\mathbb R,\rho(y)\,dy)\). Moreover, \(dt=t(1-t)\,ds\) in the kernel, so
\[
 (UCU^{-1}g)(y)=\int_{-\infty}^y g(s)\,ds=:Hg(y).
\]
Writing \(v=\rho^{1/p}\), the two endpoint forms are
\[
 v(y)=e^{-Ay}(1+e^y)^{A-B}\quad(y\le0),\qquad
 v(y)=e^{-By}(1+e^{-y})^{A-B}\quad(y\ge0).
\]
Consequently \(Y\) is equivalent, with fixed positive constants, to exponential \(L^p\) weights \(e^{-pAy}\) on the negative half-line and \(e^{-pBy}\) on the positive half-line. Also
\[
 -\frac{d}{dy}\log v(y)=A+(B-A)\frac{e^y}{1+e^y}\in[m,M].
\]

**2. Sharp bound, including nonattainment.** Let \(R_tg(y)=g(y-t)\), for \(t\ge0\). Its operator norm on \(Y\) is exactly
\[
 \|R_t\|=\sup_s\frac{v(s+t)}{v(s)}=e^{-mt}.
\]
The upper inequality follows from the last logarithmic-derivative bound. Equality as a supremum follows on a sufficiently far left or right tail where the derivative approaches \(m\). Hence \(H=\int_0^\infty R_t\,dt\), initially on a dense subspace and then as a Bochner integral, satisfies \(\|H\|\le1/m\).

For a lower bound, choose a smooth bump supported on an interval of length \(L\) entirely in the tail where \(v(y)\) approaches a constant times \(e^{-my}\). After conjugating by \(v\), \(H\) approaches convolution with \(e^{-mt}\mathbf1_{t\ge0}\). Testing on increasingly long, almost constant plateau functions, with its support subsequently translated farther into that tail, gives ratio tending to \(\int_0^\infty e^{-mt}dt=1/m\). This proves equality.

If \(A\ne B\), the strict inequality \(v(s+t)/v(s)<e^{-mt}\) holds for every finite \(s\) and every \(t>0\), so \(\|R_t g\|<e^{-mt}\|g\|\) for every nonzero \(g\); integrating the strict inequality proves nonattainment. If \(A=B\), conjugation by \(v\) makes \(H\) a positive one-sided convolution on ordinary \(L^p(\mathbb R)\). Equality in its Minkowski bound would force almost every translate of the input to be a positive scalar multiple of the same vector. That would give a nonzero translation eigenfunction in \(L^p(\mathbb R)\), which is impossible. Thus the norm is never attained.

**3. Differential inverse and resolvent.** Define \(Dg=g'\) on the weighted Sobolev domain
\[
 \mathcal D(D)=\{g\in Y:g\text{ has a locally absolutely continuous representative and }g'\in Y\}.
\]
The exponential endpoint bounds imply that each such \(g\) satisfies \(g(y)=\int_{-\infty}^y g'(s)ds\): for instance, the difference is a constant function, and constants do not lie in \(Y\) because \(A>0\) at the negative endpoint. Hence \(H:Y\to\mathcal D(D)\) is bijective with \(DH=I_Y\) and \(HD=I_{\mathcal D(D)}\). It follows that, for \(\lambda\ne0\) and \(\zeta=1/\lambda\),
\[
 H-\lambda I=-\lambda(D-\zeta I)H.
\]
Because \(H:Y\to\mathcal D(D)\) is an isomorphism for the graph norm, this identity preserves kernel dimension, range, cokernel and Fredholm index.

If \(\operatorname{Re}\zeta<m\), the bounded inverse of \(D-\zeta\) is
\[
 (D-\zeta)^{-1}F(y)=\int_{-\infty}^y e^{\zeta(y-s)}F(s)\,ds.
\]
After conjugation by \(v\), the integral kernel is dominated by \(e^{-(m-\operatorname{Re}\zeta)(y-s)}\) for \(y\ge s\), so Young's inequality applies. If \(\operatorname{Re}\zeta>M\), the inverse is
\[
 (D-\zeta)^{-1}F(y)=-\int_y^\infty e^{\zeta(y-s)}F(s)\,ds,
\]
with analogous kernel decay \(e^{-(\operatorname{Re}\zeta-M)(s-y)}\). Thus all points strictly outside the reciprocal closed strip are in the resolvent.

**4. Positive-index phase.** Suppose \(A<B\) and \(A<\operatorname{Re}\zeta<B\). The homogeneous equation has solution \(g=e^{\zeta y}\), which lies in \(Y\) exactly in this open strip, by the two exponential tails. Every \(F\in Y\) has a solution
\[
 g(y)=e^{\zeta y}\int_0^y e^{-\zeta s}F(s)\,ds.
\]
On the negative half-line, this is a backwards integral bounded by \(e^{-(\operatorname{Re}\zeta-A)(s-y)}\); on the positive half-line, it is a forward integral bounded by \(e^{-(B-\operatorname{Re}\zeta)(y-s)}\). Equivalence of the endpoint weights with their pure exponentials and Young's convolution inequality show \(g,g'\in Y\). Hence \(D-\zeta\) is onto with a one-dimensional kernel. Transforming the homogeneous function back to \(X_{p,\gamma,\delta}\) gives the displayed eigenvector; its \(p\)-th power norm is the finite beta integral
\[
 \|f_\lambda\|_{X}^p
 =\mathrm B\bigl(p(\operatorname{Re}\zeta-A),p(B-\operatorname{Re}\zeta)\bigr).
\]

**5. Negative-index phase and exact range.** Suppose \(A>B\) and \(B<\operatorname{Re}\zeta<A\). The homogeneous exponential lies in neither allowed two-tail combination, so the kernel is zero. The linear functional
\[
 L_\zeta(F)=\int_{\mathbb R}e^{-\zeta s}F(s)\,ds
\]
is bounded and nonzero on \(Y\), since on the negative half-line its dual kernel decays as \(e^{(A-\operatorname{Re}\zeta)s}\) and on the positive half-line as \(e^{(B-\operatorname{Re}\zeta)s}\). Integration by parts implies \(L_\zeta((D-\zeta)g)=0\) for all \(g\in\mathcal D(D)\), first by cutoff and then continuity.

If \(L_\zeta(F)=0\), define the solution on the negative half-line by the \(-\infty\) integral and on the positive half-line by the \(+\infty\) integral:
\[
 g(y)=\begin{cases}
 \displaystyle\int_{-\infty}^y e^{\zeta(y-s)}F(s)ds,&y\le0,\\
 \displaystyle-\int_y^\infty e^{\zeta(y-s)}F(s)ds,&y\ge0.
 \end{cases}
\]
The two values at zero agree exactly because \(L_\zeta(F)=0\). Each half is a bounded one-sided convolution in its corresponding exponential weight (decay rates \(A-\operatorname{Re}\zeta\) and \(\operatorname{Re}\zeta-B\)). Thus \(g,g'\in Y\) and the range equals \(\ker L_\zeta\), which is closed of codimension one. Under \(U\), the identity \(L_\zeta(Uh)=\int_0^1h(x)x^{-\zeta}(1-x)^{\zeta-1}dx\) gives the claimed range functional for \(C-\lambda I\).

**6. Boundary and zero.** On a boundary line \(\operatorname{Re}\zeta=A\) or \(B\), take a smooth compactly supported plane-wave cutoff of length \(L\) centered at an endpoint that escapes faster than \(L\). Conjugation by \(v\) changes \(D-\zeta\) into \(d/dy-v'/v-\zeta\); choosing the oscillatory phase \(e^{i\operatorname{Im}\zeta y}\) and normalizing gives unit-norm test functions whose image tends to zero as \(L\to\infty\), with cutoff error \(O(1/L)\) and exponentially vanishing endpoint-potential error. The kernel of \(D-\zeta\) is zero on both boundary lines. Therefore its range is nonclosed. Its annihilator is zero there: the only possible dual solution is proportional to \(e^{-\zeta y}\), which fails dual integrability at at least one endpoint. The range is consequently dense, and the operator is non-Fredholm.

Finally, \(H\) itself is injective with dense range \(\mathcal D(D)\), which is not closed. For an explicit lack-of-closed-range test, let \(g_n=e^{iny}\chi(y)\) with fixed nonzero compactly supported smooth \(\chi\); then \(\|g_n\|_Y=\|\chi\|_Y\), whereas \(\|Dg_n\|_Y\to\infty\). The vectors \(F_n=Dg_n/\|Dg_n\|_Y\) satisfy \(\|F_n\|_Y=1\) but \(\|HF_n\|_Y\to0\). Hence zero is continuous spectrum and non-Fredholm. Combining the interior and boundary cases yields every spectral and Fredholm assertion.

## Verification

The independent algebraic parameter identities, tail asymptotics, and representative endpoint integrability conditions have been checked by running the included standalone `CHECKER.py` with Python 3: 181 finite assertions passed. In particular, the formulas reduce to the unweighted exponents \(A=1-1/p\), \(B=1/p\), and verify the predicted movement of the phase transition under nonzero Jacobi weights. All infinite-dimensional statements above are proved analytically; the finite checks are diagnostics, not exhaustion or proofs of a Fredholm property.

## Relationship to prior work

Belli, Gül, Ross, and Siskakis identify the norm and crescent spectral set for the **unweighted** real-variable operator. Their semigroup representation supplies the motivating setting, but it neither treats the two independent Jacobi powers in the ambient norm nor establishes the weighted phase boundary and its weighted codimension-one range functional. Related work of Abadías, Mahillo, and Miana concerns a different Cesàro–Hardy kernel and unweighted \(L^p[0,1]\) spaces. The logistic-coordinate argument connects this problem to classical exponential dichotomies for first-order differential operators; that general framework should not itself be represented as new. The claim here is the complete sharp specialization to this concrete two-parameter weighted Cesàro family.

## Limitations

The theorem is for \(1<p<\infty\) and the stated strict admissibility conditions, not the boundary cases \(\gamma=p-1\) or \(\delta=-1\) where the integral need not act boundedly. There is no claim about weighted invariant subspaces, cyclicity, compact perturbations beyond the Fredholm index, or other Hardy kernels. Generic exponential-dichotomy Fredholm theorems may independently imply part of the classification; direct coverage by a prior weighted-integral theorem remains a priority risk, not resolved merely by unsuccessful searches. No independent mathematical audit has been performed.

## References

1. A. Belli, U. Gül, W. T. Ross, A. G. Siskakis, *Crescents and the real variable Cesàro operator*, arXiv:2606.08600v1 (public June 7, 2026); *Integral Equations and Operator Theory* **98**, article 42 (2026), DOI:10.1007/s00020-026-02865-7. https://arxiv.org/abs/2606.08600
2. A. Belli, U. Gül, W. T. Ross, A. G. Siskakis, *The Cesàro operator on* \(L^2(0,1)\), arXiv:2604.19691v2 (April 23, 2026). https://arxiv.org/abs/2604.19691
3. L. Abadías, A. Mahillo, P. J. Miana, *Cesàro–Hardy operators on* \(L^p[0,1]\): *fine spectrum, weighted Koopman semigroups and invariant subspaces*, arXiv:2604.20408v1 (April 22, 2026). https://arxiv.org/abs/2604.20408
