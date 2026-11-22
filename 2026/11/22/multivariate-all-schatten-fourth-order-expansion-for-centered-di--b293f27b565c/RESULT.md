# Multivariate all-Schatten fourth-order expansion for centered Dirichlet–Durrmeyer semigroup powers

## Finding

Let \(M_n\) be the degree-\(n\) Dirichlet Bernstein–Durrmeyer averaging operator on a \(d\)-simplex, with positive Dirichlet parameters whose sum is \(A>0\). Its Jacobi diffusion semigroup is \(H_t=e^{-t\mathcal L}\). Put \(N=n+A/2\) and define the positive, unbounded polynomial \(\mathcal D=\mathcal L(2\mathcal L+((A-1)^2-1)I)/12\) by spectral functional calculus.

**Sharp accelerated limit.** For every \(t>0\) and every Schatten exponent \(0<p\le\infty\), including trace class and the quasi-Banach exponents, one has
\[
0\preceq M_n^{\,tN}\preceq H_t,\qquad
\left\|M_n^{\,tN}-H_t+\frac{t}{N^2}\mathcal D H_t\right\|_{\mathcal S_p}
=O_{t,p,d,A}(N^{-4}),
\]
where \(\mathcal S_\infty\) denotes operator norm. The estimate is uniform for \(t\) in any compact subset of \((0,\infty)\). Therefore
\[
\lim_{n\to\infty}N^2\|H_t-M_n^{\,tN}\|_{\mathcal S_p}
=t\|\mathcal D H_t\|_{\mathcal S_p}>0.
\]
The leading constant is explicit. With \(q_k=k(k+A-1)\), \(D_k=q_k[2q_k+(A-1)^2-1]/12\), and \(m_k=\binom{k+d-1}{d-1}\), it equals
\[
t\|\mathcal D H_t\|_{\mathcal S_p}
=t\left(\sum_{k=1}^{\infty}m_k D_k^p e^{-ptq_k}\right)^{1/p}
\quad(0<p<\infty),
\]
and is \(t\sup_{k\ge1}D_k e^{-tq_k}\) in operator norm.

**Uniqueness of the centered clock.** For every fixed real \(s\), the alternative clock \(n+s\) obeys, in every Schatten \(p\)-norm,
\[
\lim_{n\to\infty}N\big(M_n^{\,t(n+s)}-H_t\big)
=-t(s-A/2)\mathcal L H_t.
\]
Thus \(s=A/2\) is the unique fixed additive time shift eliminating the first-order spectral approximation error at every positive time. In dimension two, for example, the uniform Dirichlet shape \(\boldsymbol\theta=(1,1,1)\) has a sharp trace-norm coefficient \(\sum_{k\ge1}(k+1)D_ke^{-k(k+2)}=0.23683988065255765\ldots\) at \(t=1\). The general theorem simultaneously determines such coefficients for every dimension, Dirichlet shape and Schatten exponent. The unweighted one-dimensional time-one trace-class limit is a previously recorded special case, not a separate novelty claim.

## Assumptions and scope

Fix \(d\in\mathbb N\), \(d\ge1\), and positive real parameters \(\boldsymbol\theta=(\theta_0,\ldots,\theta_d)\). Let \(A=\sum_i\theta_i\). The standard simplex is \(\Sigma_d=\{(x_1,\ldots,x_d):x_i\ge0,\ \sum_i x_i\le1\}\), with \(x_0=1-\sum_i x_i\). Equip it with Dirichlet probability measure
\[
d\rho_{\boldsymbol\theta}(x)=\frac{\Gamma(A)}{\prod_{i=0}^{d}\Gamma(\theta_i)}\prod_{i=0}^{d}x_i^{\theta_i-1}\,dx_1\cdots dx_d.
\]
For a nonnegative integer multi-index \(\boldsymbol\beta=(\beta_0,\ldots,\beta_d)\), \(|\boldsymbol\beta|=n\), set \(B_{n,\boldsymbol\beta}(x)=\frac{n!}{\prod\beta_i!}\prod_i x_i^{\beta_i}\), and define the finite-rank selfadjoint positive contraction on \(L^2(\rho_{\boldsymbol\theta})\) by
\[
M_nf(x)=\sum_{|\boldsymbol\beta|=n}B_{n,\boldsymbol\beta}(x)
\frac{\int f(y)B_{n,\boldsymbol\beta}(y)\,d\rho_{\boldsymbol\theta}(y)}{\int B_{n,\boldsymbol\beta}(y)\,d\rho_{\boldsymbol\theta}(y)}.
\]
Let \(E_k\) denote the orthogonal Jacobi-polynomial subspace of exact total degree \(k\) and \(P_k\) its orthogonal projection. The positive Jacobi diffusion generator is defined on its natural spectral domain by \(\mathcal L=\sum_{k\ge0}q_kP_k\), where \(q_k=k(k+A-1)\). Equivalently, on smooth polynomials,
\[
\mathcal Lf=-\sum_{i,j=1}^{d}x_i(\delta_{ij}-x_j)\partial_i\partial_jf
-\sum_{i=1}^{d}(\theta_i-Ax_i)\partial_if.
\]
The operator \(H_t=e^{-t\mathcal L}\) is trace class for each \(t>0\). Real positive powers of \(M_n\) use its spectral functional calculus, with the zero eigenspace kept at zero; nonintegral powers need not be positivity-preserving Markov kernels. All operator inequalities in this result are Hilbert-space Loewner inequalities, not pointwise inequalities. The theorem holds at fixed \(d\), \(\boldsymbol\theta\) and \(t\), with uniform time estimates on compact positive intervals.

## Proof

**Step 1: exact joint diagonalization.** Dirichlet integration of monomials gives, for every \(k\le n\),
\[
M_n\big|_{E_k}=\lambda_{n,k}I_{E_k},\qquad
\lambda_{n,k}=\frac{n(n-1)\cdots(n-k+1)}{(n+A)(n+A+1)\cdots(n+A+k-1)},
\]
with \(\lambda_{n,0}=1\); for \(k>n\), \(M_n\big|_{E_k}=0\). Indeed, averaging any degree-\(k\) monomial against the beta/Dirichlet posterior yields a polynomial whose top homogeneous coefficient is the displayed ratio. The symmetric kernel implies selfadjointness; orthogonal complements of successive polynomial-degree filtrations are therefore invariant. Each \(E_k\) has dimension \(m_k=\binom{k+d-1}{d-1}\). Hence \(M_n\) and \(\mathcal L\) have a common complete orthogonal basis.

**Step 2: exact centered product and positive spectral defect.** Write \(c=A/2\) and \(N=n+c\). For \(0\le k\le n\),
\[
\lambda_{n,k}=\prod_{j=0}^{k-1}\frac{N-(j+c)}{N+(j+c)}.
\]
All fractions lie strictly between zero and one, and the logarithm gives the exact identity
\[
-N\log\lambda_{n,k}
=2N\sum_{j=0}^{k-1}\operatorname{arctanh}\left(\frac{j+c}{N}\right)
\ge2\sum_{j=0}^{k-1}(j+c)=q_k.
\]
The last identity is elementary. Exponentiating proves \(0\le\lambda_{n,k}^{tN}\le e^{-tq_k}\); at \(k>n\) the lower eigenvalue vanishes, so the Loewner inequality holds in the full space.

**Step 3: exact cubic coefficient.** For \(k\le n/2\), uniformly for sufficiently large \(n\), the arguments of the inverse hyperbolic tangent are at most \(3/4\). The uniformly convergent odd-power expansion gives
\[
-N\log\lambda_{n,k}
=q_k+\frac{D_k}{N^2}+R_{n,k},\qquad
0\le R_{n,k}\le\frac{C_A(k+1)^6}{N^4},
\]
where
\[
D_k=\frac23\sum_{j=0}^{k-1}(j+c)^3
=\frac{q_k\big(2q_k+(A-1)^2-1\big)}{12}.
\]
The sum of cubes identity follows by expansion of \(\sum j^3,\sum j^2,\sum j\), and shows \(D_k>0\) for every \(k\ge1\); \(D_0=0\). In particular, \(D_k\) is exactly the eigenvalue of \(\mathcal D\) on \(E_k\).

**Step 4: uniform remainder in every Schatten ideal.** Fix \(0<\delta\le t\le T<\infty\). For \(k\le n/2\), the scalar inequality \(|e^{-v}-1+v|\le v^2/2\) for \(v\ge0\), with \(v=t(D_k/N^2+R_{n,k})\), yields
\[
\left|\lambda_{n,k}^{tN}-e^{-tq_k}+\frac{tD_k}{N^2}e^{-tq_k}\right|
\le \frac{C_{A,\delta,T}}{N^4}(k+1)^8e^{-\delta q_k}.
\]
One may first apply \(|e^{-v}-1+v|\le v^2/2\) and then separate the \(tR_{n,k}\) error; since \(D_k=O_A((k+1)^4)\), the displayed bound follows. For \(k>n/2\), use \(0\le\lambda_{n,k}^{tN}\le e^{-tq_k}\) and \(D_k=O_A((k+1)^4)\) to obtain the coarser bound \(\big(2+T D_k/N^2\big)e^{-\delta q_k}\), including all \(k>n\). As \(q_k\ge c_A k^2\) for a fixed positive \(c_A\), the tail \(k>n/2\), with multiplicity \(m_k=O_d((k+1)^{d-1})\), is exponentially small and in particular \(O(N^{-4})\) in every \(\mathcal S_p\). The low-frequency bound is summable in the same ideals: for \(p<\infty\), take the \(p\)-th power and sum against \(m_k\), using \(\sum_{k\ge0}m_k(k+1)^{8p}e^{-p\delta q_k}<\infty\); for \(p=\infty\), take the supremum. Thus the displayed \(O(N^{-4})\) operator remainder holds for all \(0<p\le\infty\) without invoking a Banach triangle inequality at \(p<1\).

**Step 5: sharpness and clock uniqueness.** The preceding bound proves Schatten convergence of \(N^2(H_t-M_n^{tN})\) to \(t\mathcal D H_t\) in every stated ideal. The limit is nonzero since \(D_1=A^3/12>0\), so convergence of each Schatten norm gives the exact leading constant. Replacing \(tN\) by \(t(n+s)=tN(1+(s-c)/N)\) in Step 3 produces
\[
\lambda_{n,k}^{t(n+s)}
=e^{-tq_k}\left(1-\frac{t(s-c)q_k}{N}+O_{A,s,\delta,T}\big(N^{-2}(k+1)^8\big)\right)
\]
on the Gaussian window. The same tail domination as in Step 4 proves the \(N\)-rescaled first-order limit in every Schatten ideal. Since \(\mathcal L H_t\ne0\), that limit vanishes if and only if \(s=c=A/2\). This proves uniqueness in the class of fixed additive shifts.

## Verification

A standalone `VERIFY.py` uses independent rational Dirichlet moments to construct Gram-matrix traces of the finite operator and compares them exactly with its spectral trace and squared trace at several one-, two- and three-dimensional parameter choices. It also checks the closed cubic coefficient and positive fifth-order residual for multiple parameter choices and verifies numerical fourth-order scaling in fixed low spectral modes. The script passes 10 rational trace checks and 108 analytic expansion cross-checks. These tests are finite corroborations, not proofs of the infinite-dimensional Schatten limits: the exact product and the Gaussian tail argument above establish those limits.

## Relationship to prior work

Abel–Berdysheva (2010) and earlier Bernstein–Durrmeyer eigenstructure literature supply the exact spectral data used here. An earlier exact unweighted interval theorem already proves the optimal integer clock \(n+1\), a one-sided trace-class second-order limit and uniqueness among integer shifts at time one. That restricted result is expressly not claimed anew here. Altomare (2019) studies Jacobi-weighted Durrmeyer iterate approximations to diffusion semigroups qualitatively; Gonska–Heilmann–Raşa (2009) give \(C^2\)-type estimates for related ultraspherical and genuine operator variants. Those are closer antecedents than generic functional-calculus results. The genuinely extended assertions concern arbitrary-dimensional, anisotropic Dirichlet parameters, general positive times, every Schatten exponent, the higher-order corrected remainder and the exact shape-dependent clock. The one-dimensional order, time-one leading term and basic clock idea are already covered by the earlier theorem and the known eigenstructure. The related spectral-power trace analysis of Dirichlet Bernstein–Durrmeyer operators studies fixed exponents and growing-rank trace asymptotics; it does not imply this increasing-exponent, fixed-time semigroup limit. These comparisons do not constitute a claim of exhaustive historical priority.

## Limitations

The parameters, simplex dimension and positive diffusion time must be fixed; the constants are not uniform down to \(t=0\), at which \(H_0=I\) is not trace class. The unique-shift statement concerns fixed additive shifts \(n+s\), not all possible nonlinear time recalibrations or Richardson extrapolations. Fractional powers of \(M_n\) are asserted to be positive semidefinite selfadjoint operators, not necessarily pointwise Markov operators. The initial eigenvalue formula, generic semigroup convergence, and the one-dimensional optimal-clock trace-class theorem are known ingredients. A few historically relevant articles could be inspected only at abstract level, leaving a residual priority risk.

## References

1. F. Altomare, *Iterates of Markov Operators and Constructive Approximation of Semigroups*, Constructive Mathematical Analysis 2 (2019), 22–39, DOI: 10.33205/cma.491601. Available online 4 January 2019. https://doi.org/10.33205/cma.491601
2. U. Abel and E. E. Berdysheva, *Complete asymptotic expansion for multivariate Bernstein–Durrmeyer operators and quasi-interpolants*, Journal of Approximation Theory 162 (2010), 201–220. DOI: 10.1016/j.jat.2009.04.004. https://doi.org/10.1016/j.jat.2009.04.004
3. H. Gonska, M. Heilmann, and I. Raşa, *Convergence of iterates of genuine and ultraspherical Durrmeyer operators to the limiting semigroup: \(C^2\) estimates*, Journal of Approximation Theory 160 (2009), 243–255. DOI: 10.1016/j.jat.2008.11.002. https://doi.org/10.1016/j.jat.2008.11.002
4. E. E. Berdysheva and K. Jetter, *Multivariate Bernstein–Durrmeyer operators with arbitrary weight functions*, Journal of Approximation Theory 162 (2010), 576–598. DOI: 10.1016/j.jat.2009.11.005. https://doi.org/10.1016/j.jat.2009.11.005
