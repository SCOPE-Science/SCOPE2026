# Sharp centered-cell Bernstein comparison and its parity-dependent minimax constants

## Finding

Fix an integer \(n\ge 1\). For \(x\in[0,1]\), put \(b_{n,j}(x)=\binom nj x^j(1-x)^{n-j}\) and
\[
(B_nf)(x)=\sum_{j=0}^n b_{n,j}(x)f(j/n).
\]
Let \(\nu_x\) be a Borel probability measure on \([0,1]\), weakly continuous in \(x\), with \(\int u\,d\nu_x(u)=x\). Its centered one-cell refinement is
\[
(Q_{n,\nu}f)(x)=\sum_{j=0}^n b_{n,j}(x)
  \int_{[0,1]}f\bigl((j+u)/(n+1)\bigr)\,d\nu_x(u).
\]
It is a positive linear map \(C[0,1]\to C[0,1]\) reproducing constants and affine functions.
For every \(x\in[0,1]\), the exact pointwise norm of the difference on real 1-Lipschitz functions is
\[
\sup_{\operatorname{Lip}(f)\le1}|(B_n-Q_{n,\nu})f(x)|
=\frac1{n+1}\sum_{j=0}^n b_{n,j}(x)\int\bigl|j/n-u\bigr|\,d\nu_x(u).
\tag{1}
\]
A single explicitly defined 1-Lipschitz polygonal function, depending only on \(n\), attains the positive signed equality in (1) for *all* \(x\) and *all* choices of the measures, even without the centering constraint.

Among all centered kernels, the pointwise minimum is
\[
\frac{M_n(x)}{n+1},\qquad
M_n(x)=\mathbb E\bigl|J/n-x\bigr|,\quad J\sim\operatorname{Bin}(n,x),
\tag{2}
\]
attained simultaneously for all \(x\) by \(\nu_x=\delta_x\). Consequently the exact minimax problem, with the infimum taken over *weakly continuous families* \((\nu_x)_{0\le x\le1}\) of mean \(x\), has solution
\[
\inf_{\nu}\sup_{x\in[0,1]}\sup_{\operatorname{Lip}(f)\le1}
|(B_n-Q_{n,\nu})f(x)|=\frac{D_n}{n+1},\quad D_n=\max_{x\in[0,1]} M_n(x).
\tag{3}
\]
The maximizers and exact \(D_n\) are parity-sensitive. If \(n=2r+1\), the unique maximizing argument is \(x=1/2\), and
\[
D_{2r+1}=\frac{\binom{2r}{r}}{2^{2r+1}}.
\tag{4}
\]
If \(n=2r\), \(r\ge1\), the **only** maximizing arguments are \(x=r/(2r+1)\) and \(x=(r+1)/(2r+1)\), and
\[
D_{2r}=2\binom{2r-1}{r-1}
\left(\frac r{2r+1}\right)^r
\left(\frac{r+1}{2r+1}\right)^{r+1}.
\tag{5}
\]
In both cases
\[
\frac{D_n}{n+1}\sim \frac{1}{\sqrt{2\pi}\,n^{3/2}}\quad(n\to\infty).
\tag{6}
\]
For interior \(x\) with \(nx\notin\mathbb Z\), **all** pointwise-optimal \(\nu_x\) are exactly the mean-\(x\) probability measures supported on the unique consecutive grid interval \([\lfloor nx\rfloor/n,(\lfloor nx\rfloor+1)/n]\). When \(nx\in\mathbb Z\), the pointwise-optimal law is uniquely \(\delta_x\). This classification includes the endpoints and does not require \(\nu_x\) to be finitely supported.

## Assumptions and scope

All functions are real and 1-Lipschitz on the Euclidean interval \([0,1]\); constants are irrelevant to the difference. All kernel measures are Borel probabilities on \([0,1]\). Weak continuity is imposed on the family so that \(Q_{n,\nu}\) acts on \(C[0,1]\); formula (1) and the pointwise classifications hold without this global continuity requirement. Each measure is independent of the binomial index \(j\), but is permitted to depend on the evaluation argument \(x\). The mean condition \(\int u\,d\nu_x(u)=x\) is exactly preservation of the affine test function \(t\mapsto t\), since \(\mathbb E[(J+U)/(n+1)]=(nx+\mathbb EU)/(n+1)\).

## Proof

**1. A common sharp Lipschitz witness.** Partition \([0,1]\) into \(I_j=[j/(n+1),(j+1)/(n+1)]\), \(0\le j\le n\). The point \(a_j=j/n\) lies in \(I_j\). Define the continuous piecewise-affine function \(s_n\) by \(s_n(0)=0\), and, on \(I_j\), slope \(+1\) to the left of \(a_j\) and slope \(-1\) to its right. At \(j=0\) and \(j=n\), one of these pieces has zero length. Its slopes have modulus at most one, so \(\operatorname{Lip}(s_n)\le1\). For every \(u\in[0,1]\),
\[
s_n(a_j)-s_n((j+u)/(n+1))=
|a_j-(j+u)/(n+1)|=|j/n-u|/(n+1).
\]
The Lipschitz triangle inequality bounds each summand of \((B_n-Q_{n,\nu})f(x)\) in absolute value by the same right-hand side. Summing nonnegative weights yields the upper bound in (1); \(f=s_n\) yields equality for every index, every \(x\), and every law. Equivalently, the natural ordered-cell coupling is exactly Wasserstein-1 optimal, not just a bound.

**2. Optimal centering and all equality cases.** For \(J\sim\operatorname{Bin}(n,x)\), write \(\nu=\nu_x\). If \(\mathbb E_\nu U=x\), Jensen's inequality gives
\[
\sum_j b_{n,j}(x)\mathbb E_\nu|j/n-U|
\ge\sum_j b_{n,j}(x)|j/n-x|=M_n(x).
\]
Taking \(\nu_x=\delta_x\) realizes equality for every \(x\). This choice is weakly continuous, so it proves both sides of the global minimax equality (3), including simultaneous attainability of the outer supremum by \(s_n\).

For \(0<x<1\), every binomial weight is positive. Equality thus requires equality in the Jensen inequality separately at *each* grid point \(j/n\). For the convex absolute-value function, equality under mean \(x\) holds precisely when \(U\) stays on one side of the grid point almost surely (or \(U=x\) if that grid point equals \(x\)). Intersecting these constraints forces support between the consecutive grid neighbors of \(x\); conversely such support makes all absolute values affine in \(U\), proving equality. If \(nx\) is integral, its matching grid point forces \(\mathbb E|U-x|=0\), hence \(U=x\) a.s. At \(x=0,1\), mean centering by itself forces the corresponding Dirac mass.

**3. Exact finite maximizers.** The classical De Moivre identity for binomial mean absolute deviation, divided by \(n\), states that on the interval \(k/n\le x\le(k+1)/n\) with \(k=0,\ldots,n-1\),
\[
M_n(x)=2\binom{n-1}{k}x^{k+1}(1-x)^{n-k}.
\tag{7}
\]
One may also derive (7) directly: if \(k\le nx\le k+1\), zero mean of \(J-nx\) makes \(\mathbb E|J-nx|=2\mathbb E[(J-nx)_+]\); the standard binomial recursion \(j\binom nj=n\binom{n-1}{j-1}\) telescopes the upper tail to (7). At a grid boundary the adjacent formulae coincide by continuity. Differentiating the logarithm of (7) shows that its unique maximum on the indicated interval is attained at \(x=(k+1)/(n+1)\), which lies strictly inside it.

Put \(N=n+1\) and \(m=k+1\). At that interval maximizer, the value is
\[
\frac{2}{N^N}\binom{N-2}{m-1}
 m^m(N-m)^{N-m}
=\frac{2(N-2)!}{N^N}h(m)h(N-m),\quad
h(s)=\frac{s^{s+1}}{s!}.
\tag{8}
\]
For positive integers \(s\), the successive ratio is
\[
\frac{h(s+1)}{h(s)}=\left(1+\frac1s\right)^{s+1},
\]
which is *strictly decreasing* in \(s\) because the derivative of its logarithm, continuously interpolated to positive real \(s\), equals \(\log(1+1/s)-1/s<0\). Thus \(h\) is strictly log-concave. The symmetric product \(h(m)h(N-m)\) is strictly larger as \(m\) approaches \(N/2\), except that the two nearest integer values tie when \(N\) is odd. Therefore for odd \(n\) there is exactly one global maximizing cell and for even \(n\) exactly two; substituting these integer arguments gives (4) and (5). Strict concavity and strict within-cell maxima exclude all other points.

Finally, Stirling's factorial asymptotic in (4) and (5) gives \(D_n\sim1/\sqrt{2\pi n}\), yielding (6).

**4. Comparison with conventional cell jitter.** The uniform jitter \(\nu_x=\operatorname{Unif}[0,1]\) is the classical Bernstein–Kantorovich averaging (not centered except at \(x=1/2\)); (1) gives its sharp pointwise comparison
\[
\frac{1/2-(1-1/n)x(1-x)}{n+1},
\]
so its Lipschitz-to-uniform discrepancy is \(1/[2(n+1)]\). The centered two-point jitter \(\nu_x=(1-x)\delta_0+x\delta_1\) yields exactly \(B_{n+1}\) and discrepancy \(2x(1-x)/(n+1)\), which is a previously established special case. The present result concerns the *optimal centered interpolation family*, its full equality classification, and sharp \(n^{-3/2}\) minimax law; it does not claim those special cases as new.

## Verification

The standalone script `verify_jitter.py` uses exact rational arithmetic. It checks the claimed universal spline against an independent 1-dimensional transport calculation by integrating the signed CDF difference, with binomial and non-binomial weights, deterministic and nontrivial discrete jitter laws. It also checks De Moivre's formula, all finitely many cell-maximizer candidates through degree 54, and parity-specific maxima. Stirling asymptotics are tested numerically for selected larger degrees only as corroboration. The finite tests do **not** prove the general theorem; the analytical steps above do.

## Relationship to prior work

The Bernoulli mean absolute deviation identity (7) is classical and is *not* claimed as new; the 2013 paper by Berend and Kontorovich gives a sharp uniform parameter-dependent analysis of that quantity. The 2016 work by Altomare, Cappelletti Montano, Leonessa, and Raşa provides a broad construction and approximation theory for Bernstein–Kantorovich-type kernels, including fixed mixing measures, but the inspected results do not give the centered-kernel Lipschitz minimax problem, its optimizer classification, or (3)–(6). Gonska, Piţul, and Raşa (2006) and the survey by Acu, Hodiş, and Raşa (2018) study estimates for differences between positive linear operators; the inspected comparison bounds do not imply this exact constrained optimum. The previously established successive-degree Bernstein coefficient corresponds to the particular Bernoulli mixing law and is not an originality claim here. Priority remains qualified where older related primary sources were inaccessible or did not expose their exact statements.

## Limitations

Only real Lipschitz functions, classical univariate Bernstein binomial weights, and one extra cell-valued random variable independent of the binomial index are treated. The centering constraint is essential to the stated minimax problem. Other constraints on the jitter distribution, different target regularities, higher-dimensional simplices, or a kernel depending jointly on both \(j\) and \(x\) are outside scope. The displayed rate is sharp in the claimed class, not a general lower bound for all possible approximation operators. Independent mathematical validation has not been performed.

## References

1. D. Berend and A. Kontorovich, *A sharp estimate of the binomial mean absolute deviation with applications*, Statistics & Probability Letters **83** (2013), 1254–1259, DOI: 10.1016/j.spl.2013.01.023; first online 2013-01-23. Author-accessible full text: https://www.cs.bgu.ac.il/~karyeh/sharp-mad.pdf.
2. F. Altomare, M. Cappelletti Montano, V. Leonessa, and I. Raşa, *A generalization of Kantorovich operators for convex compact subsets*, arXiv:1605.06768, version 1 dated 2016-05-22. https://arxiv.org/abs/1605.06768.
3. H. Gonska, P. Piţul, and I. Raşa, *On differences of positive linear operators*, Carpathian J. Math. **22** (2006), 65–78.
4. A. M. Acu, S. Hodiş, and I. Raşa, *A Survey on Estimates for the Differences of Positive Linear Operators*, Constructive Mathematical Analysis **1** (2018), 113–127, DOI: 10.33205/cma.478408.
5. A. M. Acu and I. Raşa, *New estimates for the differences of positive linear operators*, Numerical Algorithms **73** (2016), 775–789, DOI: 10.1007/s11075-016-0117-8 (full-text comparison limited).
