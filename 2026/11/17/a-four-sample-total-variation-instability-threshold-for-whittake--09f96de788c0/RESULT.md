# A four-sample total-variation instability threshold for Whittaker smoothing

## Finding
Let \(n\ge2\), \(x\in\mathbb R^n\), and define the unweighted path-variation seminorm
\[
V_n(x)=\sum_{i=1}^{n-1}|x_{i+1}-x_i|.
\]
For \(p=1,2\) and \(n>p\), let \(D_p\) be the usual forward finite-difference matrix of order \(p\), and put
\[
S_{p,\lambda}=(I_n+\lambda D_p^{\mathsf T}D_p)^{-1},\qquad \lambda>0.
\]
Its sharp variation quotient norm is \(L_{p,n}(\lambda)=\sup_{V_n(h)>0}V_n(S_{p,\lambda}h)/V_n(h)\). The following complete boundary dichotomy holds.

For every \(n\ge2\) and \(\lambda>0\), \(L_{1,n}(\lambda)<1\). For second differences, \(L_{2,3}(\lambda)=1\), while
\[
L_{2,n}(\lambda)>1\quad\text{for every }n\ge4\text{ and every }\lambda>0.
\]
More strongly, for each \(n\ge4\) and \(\lambda>0\), there is a single monotone binary jump \(h=(0,\ldots,0,1,\ldots,1)\) satisfying \(V_n(S_{2,\lambda}h)>V_n(h)=1\). At the first unstable dimension the exact sharp norm is
\[
\boxed{L_{2,4}(\lambda)=\frac{1+12\lambda}{1+10\lambda}}
\]
and the sharp value is attained by \(h=(0,0,1,1)\).

The core mechanism is a more general obstruction: for \(n\ge4\), any **symmetric** linear map \(S:\mathbb R^n\to\mathbb R^n\) which fixes every affine sequence and has precisely the affine sequences as fixed vectors must satisfy \(\|S\|_{V_n\to V_n}>1\). This statement includes all resolvents \(S=(I_n+K)^{-1}\) of symmetric positive-semidefinite penalty matrices \(K\) with exactly the affine sequences as their kernel.

## Assumptions and scope
All vector entries are real. The matrices \(D_1\) and \(D_2\) have rows \((-1,1)\) and \((1,-2,1)\), respectively, positioned at consecutive sites, with no periodic wrapping or weights. The smoothing operator is the unique minimizer map for
\[
\sum_{i=1}^n(z_i-x_i)^2+\lambda\sum_{i=1}^{n-p}(D_pz)_i^2.
\]
Variation is the sum of absolute first differences, not the squared second-difference penalty, signal range, or an \(\ell^2\) norm. For a linear map fixing constants, the one-input quotient norm equals its two-input Lipschitz modulus with respect to \(V_n\). The claim excludes \(p\ge3\), weighted fidelity and weighted difference penalties, and non-symmetric maps. All formulas use the penalty normalization above.

## Proof
Let \(B=D_1\) be the \((n-1)\)-by-\(n\) signed path-gradient matrix. Let \(R:\mathbb R^{n-1}\to\mathbb R^n\) be the step reconstruction
\[
(Ru)_1=0,\qquad (Ru)_i=\sum_{j<i}u_j\quad(2\le i\le n).
\]
Then \(BR=I_{n-1}\), and every \(x\) is \(x_1\mathbf1+RBx\). Since every \(S_{p,\lambda}\) fixes constants, its induced gradient matrix \(A=BS_{p,\lambda}R\) satisfies \(BS_{p,\lambda}x=A Bx\). Consequently the sharp variation norm is the largest absolute column sum of \(A\).

**First-difference case.** The resolvent identity is
\[
B(I_n+\lambda B^{\mathsf T}B)^{-1}=(I_{n-1}+\lambda BB^{\mathsf T})^{-1}B.
\]
Write \(T=(I_{n-1}+\lambda BB^{\mathsf T})^{-1}\). Here \(BB^{\mathsf T}\) is the Dirichlet tridiagonal matrix with diagonal \(2\) and nearest off-diagonal \(-1\). Thus \(T\) is symmetric and strictly positive entrywise (irreducible nonsingular \(M\)-matrix inverse). If \(m=n-1\), then \(BB^{\mathsf T}\mathbf1\) is the sum of the two endpoint indicators for \(m\ge2\) and equals \(2\) for \(m=1\). Since
\[
\mathbf1-T\mathbf1=\lambda TBB^{\mathsf T}\mathbf1>0
\]
componentwise, every column sum of \(T\) is strictly below one. As \(T\) is entrywise positive, the induced gradient norm, which equals the largest column sum, is strictly below one.

**Self-adjoint affine obstruction.** Let \(n\ge4\), and suppose \(S=S^{\mathsf T}\) fixes \(\mathbf1=(1,\ldots,1)\) and \(r=(1,2,\ldots,n)\), with fixed space exactly their span. As above, \(A=BSR\). Because \(Br=\mathbf1_{n-1}\), we have \(A\mathbf1_{n-1}=\mathbf1_{n-1}\): the sum of the entries of \(A\) is \(n-1\). Let
\[
c_j=\sum_{i=1}^{n-1}A_{ij}=(SRe_j)_n-(SRe_j)_1.
\]
If every \(c_j\le1\), their sum \(n-1\) forces every \(c_j=1\). Put \(\delta=e_n-e_1\). We would have \(\delta^{\mathsf T}S R=\delta^{\mathsf T}R\); also \(\delta^{\mathsf T}S\mathbf1=\delta^{\mathsf T}\mathbf1=0\). The columns of \((\mathbf1,R)\) form a basis, so \(\delta^{\mathsf T}S=\delta^{\mathsf T}\). By symmetry, \(S\delta=\delta\). But \(\delta=(-1,0,\ldots,0,1)\) is not affine when \(n\ge4\), contradicting the fixed-space hypothesis. Hence some \(c_j>1\). The monotone binary step \(h=Re_j\) has \(V_n(h)=1\), whereas
\[
V_n(Sh)\ge |(Sh)_n-(Sh)_1|=|c_j|>1.
\]
This proves both noncontractivity and the promised binary witness, without a finite-dimension enumeration.

For \(S_{2,\lambda}\), the matrix \(D_2^{\mathsf T}D_2\) is positive semidefinite and has kernel exactly the affine sequences, since \(D_2x=0\) precisely when all adjacent slopes agree. Because \(\lambda>0\), the fixed space of \(S_{2,\lambda}\) is exactly this kernel. The obstruction therefore proves \(L_{2,n}(\lambda)>1\) for every \(n\ge4\).

**The exact small-dimensional boundary.** For \(n=3\), the induced gradient matrix is
\[
A_{2,3}=\frac1{1+6\lambda}\begin{pmatrix}1+3\lambda&3\lambda\\3\lambda&1+3\lambda\end{pmatrix}.
\]
All columns are nonnegative and sum to one, giving \(L_{2,3}=1\).

For \(n=4\), let \(q=(1+2\lambda)(1+10\lambda)\). Directly inverting \(I+\lambda D_2^{\mathsf T}D_2\) gives
\[
A_{2,4}=\begin{pmatrix}
(6\lambda^2+9\lambda+1)/q&4\lambda/(1+10\lambda)&\lambda(6\lambda-1)/q\\
3\lambda/(1+10\lambda)&(4\lambda+1)/(1+10\lambda)&3\lambda/(1+10\lambda)\\
\lambda(6\lambda-1)/q&4\lambda/(1+10\lambda)&(6\lambda^2+9\lambda+1)/q
\end{pmatrix}.
\]
Its middle column has absolute sum \((1+12\lambda)/(1+10\lambda)\). Either outer column has a strictly smaller absolute sum: subtracting the middle sum yields \(-\lambda(18\lambda+1)/q\) for \(0<\lambda\le1/6\), and \(-3\lambda/(1+10\lambda)\) for \(\lambda\ge1/6\). This proves the exact formula and the attaining central step \((0,0,1,1)\).

## Verification
Run `python check.py` with Python 3 and SymPy installed. It checks the displayed \(n=3,4\) gradient formulas and both outer-column comparison identities symbolically for a positive indeterminate \(\lambda\). Independently, exact rational Gaussian elimination checks the claimed norm regimes and the existence of a monotone step with endpoint span larger than one for dimensions \(2\) through \(12\) at five rational smoothing strengths. The full-dimensional theorem is proved analytically in the preceding section; finite checks do not substitute for the fixed-space argument. Expected terminal lines are recorded in `VERIFICATION.md`.

## Relationship to prior work
Second-difference quadratic penalization is the standard Hodrick–Prescott/Whittaker–Henderson smoother. McElroy (2008) derives exact filter coefficients in an infinite-time-series representation; Paige and Trindade (2010) relate the HP filter to penalized splines. Cornea-Madeira's deposited 2016 full text derives exact finite-sample smoother weights. These coefficient formulas and model equivalences are prior work, but they do not themselves state the total-variation contraction obstruction, monotone binary witness for all finite sample sizes, or the sharp four-point variation factor. A public 2026 mathematical finding classifies *range preservation* across Whittaker difference orders, and shows that the second-difference smoother can undershoot at three points. This does not imply the present TV-norm boundary: the three-point smoother has TV norm exactly one despite that range-preservation failure. Periodic biharmonic smoothing results concern different boundary conditions. The exact first-order TV-contraction proof and affine-fixed-space argument are supplied here rather than inferred from signs of coefficient matrices.

## Limitations
The sharp formula \((1+12\lambda)/(1+10\lambda)\) is established only for four samples; for larger dimensions the theorem proves strict amplification and exhibits a finite prescription for an attaining **amplifying** binary step, not the exact operator norm. The general structural obstruction assumes self-adjointness and the exact affine fixed space. Historical coefficient formulas may contain information from which particular examples are derivable. An inaccessible plausible 2016 primary source on finite-sample HP weights was not fully compared; the originality assessment is best-knowledge, not an exhaustive literature certificate. 

## References
1. T. McElroy, *Exact formulas for the Hodrick–Prescott filter*, Econometrics Journal 11 (2008), 209–217, DOI: 10.1111/j.1368-423X.2008.00230.x; first published online 2008-01-17.
2. R. Paige and A. A. Trindade, *The Hodrick–Prescott Filter: A Special Case of Penalized Spline Smoothing*, Electronic Journal of Statistics 4 (2010), 856–874, DOI: 10.1214/10-EJS570.
3. A. Cornea-Madeira, *The Explicit Formula for the Hodrick–Prescott Filter in Finite Sample*, Review of Economics and Statistics (2017); publicly deposited manuscript 2016-04-06, https://eprints.whiterose.ac.uk/id/eprint/97954/1/HP_ACM.pdf, DOI: 10.1162/REST_a_00594.
4. R. M. de Jong and N. Sakarya, *The Econometrics of the Hodrick–Prescott Filter*, Review of Economics and Statistics 98 (2016), 310–317, DOI: 10.1162/REST_a_00523.
5. G. Frasso and P. H. C. Eilers, *L- and V-curves for optimal smoothing*, Statistical Modelling 15 (2015), 91–111, DOI: 10.1177/1471082X14549288; first published online 2014-11-14.
6. *Only first-difference Whittaker–Henderson smoothing is universally range-preserving*, public mathematical report (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-only-first-difference-whittaker-henderson-smoothing-is-universal--b1f399ec57e6.
