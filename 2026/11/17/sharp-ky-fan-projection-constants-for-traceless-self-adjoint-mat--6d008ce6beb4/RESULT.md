# Sharp Ky Fan projection constants for traceless self-adjoint matrices

## Finding
For every integer \(n\ge 2\), every integer \(1\le k\le n\), and either the real vector space of real symmetric \(n\times n\) matrices or the real vector space of complex Hermitian \(n\times n\) matrices, equip the space with the Ky Fan \(k\)-norm \(\|A\|_{(k)}=\sum_{j=1}^{k}\sigma_j(A)\), where the singular values are arranged in nonincreasing order. The least norm of a **real-linear** projection onto the trace-zero self-adjoint subspace equals the norm of trace-centering \(\mathcal C(A)=A-\operatorname{tr}(A)I/n\), and its exact value is
\[
\boxed{\min_{Q^2=Q,\,\operatorname{ran}Q=\{A:\operatorname{tr}A=0\}}\|Q\|_{(k)\to(k)}
=\|\mathcal C\|_{(k)\to(k)}
=\max\left\{2-\frac{2k}{n},\ 1+\frac{k-2}{n}\right\}.}
\]
The two terms coincide exactly when \(n=3k-2\). When \(n>3k-2\), a two-level sign spectrum is an extremizer; when \(n<3k-2\), a rank-one spectral spike is an extremizer; both are extremizers at equality. The projection is nonexpansive exactly for \((n,k)=(2,1),(2,2),(3,2),(4,2)\). In particular, for every \(n\ge5\), **all** Ky Fan ranks yield expansion; choosing the best rank gives an asymptotic least norm of \(4/3\) as \(n\to\infty\).

## Assumptions and scope
The matrix space consists of self-adjoint (symmetric or Hermitian) matrices treated as a **real** Banach space. Real-linearity is essential when specifying projections. The trace is real. The norm is the unnormalized sum of the \(k\) largest singular values. Integers satisfy \(n\ge2\), \(1\le k\le n\). The operator norm is over all nonzero self-adjoint matrices; the infimum runs over every bounded real-linear projection onto the trace-zero hyperplane, not merely orthogonal projections.

## Proof
**1. Reduction to spectral mean-centering.** By the spectral theorem, every self-adjoint \(A\) has real eigenvalues \(x_1,\ldots,x_n\). Its Ky Fan \(k\)-norm is \(N_k(x)=\sum_{j=1}^k|x|_{(j)}\). Trace-centering replaces \(x\) with \(Fx=x-\bar x\mathbf1\), where \(\bar x=n^{-1}\sum_jx_j\). Thus its matrix operator norm equals \(\|F\|_{N_k\to N_k}\); diagonal matrices realize every spectral vector.

**2. Dual polytope.** The dual of \(N_k\) is
\[
N_k^*(y)=\max\left\{\|y\|_\infty,\frac{\|y\|_1}{k}\right\}.
\]
Indeed, the unit ball of this dual norm is the intersection of the coordinate cube with the \(\ell_1\)-ball of radius \(k\), and its support function is the sum of the top \(k\) absolute coordinates. Since \(k\) is integral, the vertices of the dual unit ball have exactly \(k\) entries in \(\{-1,1\}\) and all remaining entries zero. To see this, any unsaturated \(\ell_1\) constraint leaves a fractional coordinate free; when saturated, two fractional coordinates can be perturbed oppositely, whereas precisely one fractional coordinate is incompatible with integral \(k\). The formula also includes \(k=1\) and \(k=n\).

Since \(F=F^{\mathsf T}\), duality gives
\[
\|F\|_{N_k\to N_k}=\max_{b\in\operatorname{vert}(B_{N_k^*})}N_k^*(Fb).
\]
For such a vertex, change its global sign if needed and write its coordinate sum as \(d\ge0\), where \(d\in\{0,\ldots,k\}\), \(d\equiv k\pmod2\). It has \((k+d)/2\) positive entries, \((k-d)/2\) negative entries, and \(n-k\) zeros. The centered entries are respectively \(1-d/n\), \(-1-d/n\), and \(-d/n\). Hence
\[
\frac{\|Fb\|_1}{k}=1+\frac{d(n-k-d)}{nk}.
\]
The maximum of \(\|Fb\|_\infty\) over these vertices is \(1+(k-2)/n\): for \(k\ge2\) choose exactly one negative entry among the \(k\) nonzeros, and for \(k=1\) use a single sign (yielding \(1-1/n\)). The all-positive-vertex \(d=k\) gives \(\|Fb\|_1/k=2-2k/n\).

**3. No hidden mixed-sign maximizer.** If \(n\ge3k-2\), the displayed quadratic in \(d\) is nondecreasing as \(d\) ranges by steps of two up to \(k\): the last increment is \(2(n-3k+2)/(nk)\ge0\). Its maximum is then \(2-2k/n\), which also dominates \(1+(k-2)/n\). If \(n\le3k-2\), every \(0\le d\le k-2\) obeys
\[
d(n-k-d)\le d(2k-2-d)\le k(k-2),
\]
where the last inequality follows since the quadratic increases on \([0,k-2]\). Thus the \(\ell_1/k\) branch is bounded by \(1+(k-2)/n\); the remaining \(d=k\) term is \(2-2k/n\), also no larger in this regime. These cases establish the exact norm, including the endpoints \(k=1,n\).

**4. Explicit primal equality.** A rank-one diagonal matrix \(A=\operatorname{diag}(1,0,\ldots,0)\) has \(\|A\|_{(k)}=1\), and trace-centering has \(k\)-norm \((n-1)/n+(k-1)/n=1+(k-2)/n\). In the regime \(n\ge3k-2\), take a diagonal matrix with \(k\) eigenvalues \(+1\) and \(n-k\) eigenvalues \(-1\). Here \(n\ge2k\) and its centered \(k\)-norm is \(2k(n-k)/n\) against input norm \(k\), giving \(2-2k/n\). These verify sharpness of the larger branch. (When \(n=k\), only the spike branch is needed.)

**5. Minimality among all projections.** Given an arbitrary real-linear projection \(Q\) onto traceless self-adjoint matrices, conjugate it by every orthogonal/unitary matrix and average over the compact group. The averaged map \(\widehat Q\) is another projection onto the same hyperplane and \(\|\widehat Q\|\le\|Q\|\), because Ky Fan norms are invariant under conjugation. Every conjugate fixes traceless matrices, so \(\widehat Q\) does too. Equivariance forces \(\widehat Q(I)\) to be a scalar matrix, while its trace vanishes, so \(\widehat Q(I)=0\). Decomposing each input into traceless plus scalar parts shows \(\widehat Q=\mathcal C\). Thus \(\mathcal C\) minimizes the norm among **all** projections.

The nonexpansivity list follows by requiring simultaneously \(2-2k/n\le1\), i.e. \(k\ge n/2\), and \(1+(k-2)/n\le1\), i.e. \(k\le2\). Minimizing the decreasing and increasing terms over integral \(k\) places the best rank nearest \((n+2)/3\), and the minimized constant tends to \(4/3\).

## Verification
Run `python3 check_kyfan.py` using Python's standard library. It enumerates all sign-support vertices of the dual Ky Fan unit ball for \(2\le n\le10\), \(1\le k\le n\), with exact rational arithmetic; compares the resulting norms with both analytical branches; checks explicit primal extremizers; and tests the nonexpansivity list through dimension \(15\). The output is recorded in `VERIFICATION.md`. These finite checks corroborate, but do not replace, the proof for arbitrary \(n,k\).

## Relationship to prior work
Foucart's *Computation of Minimal Projections and Extensions* establishes that trace-centering is norm-minimizing for unitarily invariant matrix norms, obtains the exact Schatten endpoint values \(2-2/n\), and supplies only the uniform Ky Fan \(k\)-bound \(2-2/n\) (Corollary 4). The present result computes the **rank-dependent exact value** on the self-adjoint subspace, which is generally strictly smaller for intermediate \(k\), together with explicit extremizers and the crossover \(n=3k-2\). The classical Ky Fan variational principle explains the spectral norm terminology but does not by itself yield this two-branch operator constant. The self-adjoint domain is narrower than the full matrix domain in Foucart's corollary; no exact formula for non-self-adjoint input matrices is claimed.

## Limitations
Only self-adjoint real symmetric or complex Hermitian matrices are covered; for complex Hermitian matrices, projections are real-linear. The formula does not assert the same constant on all real or complex square matrices, nor on noninteger interpolation of Ky Fan ranks or on arbitrary weighted singular-value gauges. The literature priority search cannot rule out earlier equivalent results phrased in finite symmetric-gauge or Lorentz sequence-space language. Independent audit has not been performed.

## References
1. Simon Foucart, *Computation of Minimal Projections and Extensions*, **Numerical Functional Analysis and Optimization** 37(2), 159–185 (2016), DOI: `10.1080/01630563.2015.1091014`, author full text: `https://foucart.github.io/publi/CompMinExt.pdf` (Section 4.2, especially Theorem 1, Theorem 3 and Corollary 4); publisher online date 2016-01-29.
2. Rajendra Bhatia, *Matrix Analysis*, Springer, 1997, Chapter IV (background on unitarily invariant norms and Ky Fan norms, as referenced by Foucart). This source was not independently inspected in full.
