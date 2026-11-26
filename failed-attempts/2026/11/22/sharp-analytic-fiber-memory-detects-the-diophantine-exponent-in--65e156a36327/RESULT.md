# Sharp analytic-fiber memory detects the Diophantine exponent in a dyadic circle skew product

## Finding
Let \(\rho>0\), \(\alpha\in\mathbb R\), and consider the Lebesgue-preserving skew product
\[
T_\alpha(x,u)=(\{2x\},\{u+\alpha x\}),\qquad (x,u)\in[0,1)\times\mathbb T,
\]
where \(\mathbb T=\mathbb R/\mathbb Z\). Introduce the measurable fiber coordinate \(v=\{u-\alpha x\}\). Let \(H_\rho\) be the zero-mean Fourier Hilbert space on \(\mathbb T\) with
\[
\|g\|_\rho^2=\sum_{k\in\mathbb Z\setminus\{0\}}e^{2\rho|k|}|\widehat g(k)|^2.
\]
For \(n\ge0\), define the sharp *stationary analytic-fiber correlation norm*
\[
\mathcal M_\rho(n;\alpha)=\sup_{\substack{g,h\in H_\rho\\\|g\|_\rho=\|h\|_\rho=1}}
\left|\int g\bigl(v(T_\alpha^n(x,u))\bigr)\overline{h(v(x,u))}\,dx\,du\right|,
\qquad A_\rho(n;\alpha)=-\log \mathcal M_\rho(n;\alpha).
\]
Then, for every \(n\ge0\),
\[
\boxed{\mathcal M_\rho(n;\alpha)=\sup_{k\ge1}e^{-2\rho k}|\cos(\pi k\alpha)|^n.}
\]
The supremum is attained by a single Fourier frequency, with the phase of the second observable chosen to match its eigenvalue.

If \(\alpha=p/q\) is rational in lowest terms, then
\[
\boxed{\lim_{n\to\infty}\mathcal M_\rho(n;p/q)=e^{-2\rho q}>0.}
\]
If \(\alpha\) is irrational, \(\mathcal M_\rho(n;\alpha)\to0\), but \(A_\rho(n;\alpha)=o(n)\) and there is no positive uniform exponential correlation rate in this norm. Every irrational \(\alpha\) satisfies \(A_\rho(n;\alpha)=O_{\rho}(n^{1/3})\). More sharply, with \(\|t\|_{\mathbb Z}=\inf_{m\in\mathbb Z}|t-m|\),
\[
\boxed{\inf_{n\ge1}\frac{A_\rho(n;\alpha)}{n^{1/3}}>0
\quad\Longleftrightarrow\quad\inf_{k\ge1}k\|k\alpha\|_{\mathbb Z}>0.}
\]
Consequently a badly approximable irrational parameter has \(A_\rho(n;\alpha)=\Theta_{\alpha,\rho}(n^{1/3})\), and for every non-badly-approximable irrational the quotient \(A_\rho(n;\alpha)/n^{1/3}\) has lower limit zero.

A finer classification holds for *every* irrational, including Liouville numbers. Define its homogeneous approximation exponent
\[
\nu(\alpha)=\limsup_{k\to\infty}\frac{-\log\|k\alpha\|_{\mathbb Z}}{\log k}\in[1,\infty].
\]
With the convention \(1/(1+2\infty)=0\),
\[
\boxed{\liminf_{n\to\infty}\frac{\log A_\rho(n;\alpha)}{\log n}=\frac{1}{1+2\nu(\alpha)}.}
\]
Thus the liminf exponent of the *negative logarithm of an optimal correlation*, rather than any fixed single-mode correlation, recovers the irrationality exponent \(\mu(\alpha)=\nu(\alpha)+1\).

## Assumptions and scope
All integrals use normalized product Lebesgue measure. The base coordinate is on \([0,1)\), so no continuity at the identified endpoint is assumed. Fourier observables are analytic in the measurable coordinate \(v\) in the precise exponential-weighted Hilbert sense; they are **not** claimed to be globally Hölder in the original \((x,u)\) coordinates. The result concerns the stated sharp two-observable operator norm, not total-variation mixing of a singular walk started at one point, nor correlation bounds for every observable on the full skew product.

The fractional-part convention makes all formulas well-defined except at irrelevant dyadic dual-expansion ambiguities, which form a null set. The Hilbert norm is fixed, independent of \(n\), while the maximizing observables may depend on \(n\). The irrationality exponent is a limsup over positive integers; it is at least one for every irrational by Dirichlet approximation.

## Proof
**Step 1: exact Bernoulli conjugacy.** Write \(b(x)=\lfloor2x\rfloor\in\{0,1\}\). Since \(\{2x\}=2x-b(x)\), direct substitution gives the identity on the circle
\[
\begin{aligned}
v(T_\alpha(x,u))
&=\{u+\alpha x-\alpha(2x-b(x))\}\\
&=\{v(x,u)+\alpha b(x)\}.
\end{aligned}
\]
The map \((x,u)\mapsto(x,v)\) preserves product Lebesgue measure, because on each base fiber it is a circle translation. The digits \(b(\{2^j x\})\), \(j\ge0\), are independent fair Bernoulli bits under uniform \(x\), independent of uniform \(v\). Thus, almost surely,
\[
v(T_\alpha^n(x,u))=\left\{v(x,u)+\alpha\sum_{j=0}^{n-1}b(\{2^jx\})\right\}.
\]
For the character \(e_k(v)=e^{2\pi i kv}\), this yields the eigenvalue
\[
\mathbb E\bigl[e_k(v_n)\overline{e_k(v_0)}\bigr]
=\left(\frac{1+e^{2\pi i k\alpha}}2\right)^n
=e^{\pi i n k\alpha}\cos(\pi k\alpha)^n.
\]

**Step 2: exact sharp analytic norm.** Fourier orthogonality in uniform \(v_0\) eliminates all different-frequency terms. The absolute correlation is bounded by
\[
\left(\sup_{k\ne0}e^{-2\rho|k|}|\cos(\pi k\alpha)|^n\right)
\left(\sum_{k\ne0}e^{2\rho|k|}|\widehat g(k)|^2\right)^{1/2}
\left(\sum_{k\ne0}e^{2\rho|k|}|\widehat h(k)|^2\right)^{1/2}.
\]
Choosing matching single characters at a maximizing frequency attains equality. The factor \(e^{-2\rho|k|}\) is essential: both observables are normalized in the analytic Hilbert norm. Since \(e^{-2\rho k}\to0\), the supremum is a maximum. Equivalently,
\[
\boxed{A_\rho(n;\alpha)=\inf_{k\ge1}\{2\rho k+n\,c_k\},\qquad c_k=-\log|\cos(\pi k\alpha)|,}
\]
allowing \(c_k=+\infty\) at a zero of the cosine.

**Step 3: rational and irrational alternatives.** If \(\alpha=p/q\) in lowest terms, precisely the frequencies divisible by \(q\) have \(|\cos(\pi k\alpha)|=1\). Every other residue class has eigenvalue magnitude uniformly below one. The smallest surviving positive frequency is \(q\), hence the limit is \(e^{-2\rho q}\). If \(\alpha\) is irrational, each \(c_k>0\). A fixed finite set of frequencies decays exponentially, while the contribution of all \(k>K\) is at most \(e^{-2\rho K}\). This proves \(\mathcal M_\rho(n;\alpha)\to0\). Density of \(\{k\alpha\}\) implies \(\inf_k c_k=0\), and \(A_\rho(n;\alpha)\le2\rho k+n c_k\) for each fixed \(k\). Therefore \(A_\rho(n;\alpha)/n\to0\): no positive uniform exponential rate is possible.

**Step 4: arithmetic variational comparison.** Put \(\delta_k=\|k\alpha\|_{\mathbb Z}\in[0,1/2]\). There exists a universal \(c>0\) such that
\[
 c\delta_k^2\le-\log|\cos(\pi k\alpha)|,
\]
including the infinite value when \(\delta_k=1/2\). For \(\delta_k\le1/4\), there is also a universal \(C\) with the reverse inequality. Hence the infimum in Step 2 is controlled by balancing linear frequency cost with quadratic small divisors.

Dirichlet's pigeonhole theorem supplies, for every integer \(Q\ge1\), some \(1\le k\le Q\) with \(\delta_k\le1/Q\). Taking \(Q=\lceil n^{1/3}\rceil\) proves \(A_\rho(n;\alpha)\le2\rho Q+CnQ^{-2}=O_\rho(n^{1/3})\) for large \(n\). If \(\alpha\) is badly approximable, \(\delta_k\ge d/k\) for all \(k\), with \(d>0\), and
\[
A_\rho(n;\alpha)\ge\inf_{k\ge1}\left(2\rho k+cd^2\frac n{k^2}\right)\ge c_{\rho,d}n^{1/3}.
\]
Conversely, if \(\alpha\) is irrational but not badly approximable, choose increasing \(k_j\) with \(k_j\delta_{k_j}\to0\). Set \(n_j=\lfloor k_j\delta_{k_j}^{-2}\rfloor\). For large \(j\), \(\delta_{k_j}\le1/4\) and
\[
A_\rho(n_j;\alpha)\le2\rho k_j+Cn_j\delta_{k_j}^2\le C_\rho k_j,
\qquad n_j^{1/3}\asymp k_j(k_j\delta_{k_j})^{-2/3}.
\]
It follows that \(A_\rho(n_j;\alpha)/n_j^{1/3}\to0\), proving the if-and-only-if.

**Step 5: all irrationality exponents.** Suppose first that \(\nu=\nu(\alpha)<\infty\). For each \(\varepsilon>0\), eventually \(\delta_k\ge k^{-(\nu+\varepsilon)}\), and the finitely many excluded positive frequencies have a strictly positive \(c_k\). Thus
\[
A_\rho(n;\alpha)\ge c_{\varepsilon,\alpha,\rho}\,n^{1/(1+2\nu+2\varepsilon)}
\]
for all sufficiently large \(n\), by minimizing \(2\rho k+cnk^{-2(\nu+\varepsilon)}\). Conversely, by the definition of a limsup, for each \(\varepsilon>0\) there are arbitrarily large \(k\) with \(\delta_k\le k^{-(\nu-\varepsilon)}\). For \(n_k=\lfloor k\delta_k^{-2}\rfloor\), Step 4 yields \(A_\rho(n_k;\alpha)=O_\rho(k)\), whereas \(\log n_k\ge(1+2\nu-2\varepsilon)\log k+o(1)\). Taking logarithms and sending \(\varepsilon\downarrow0\) proves the displayed liminf identity. If \(\nu=\infty\), the same upper-subsequence argument works for arbitrarily large finite approximation exponents, giving a liminf no greater than zero. The reverse inequality follows from \(A_\rho(n;\alpha)\ge2\rho>0\), so \(\log A_\rho(n;\alpha)/\log n\ge-o(1)\).

## Verification
The standalone `CHECKER.py` reproduces the Bernoulli character formula by direct enumeration of every binary word up to length eight for three rational parameters, verifies the coordinate conjugacy with exact rational arithmetic on a dyadic grid, and compares finite-frequency variational expressions. In total 307 finite checks passed when run using Python 3. These checks test algebraic normalizations and implementation, not the infinite arithmetic assertions; the latter follow from the inequalities and quantifiers in Steps 3–5. The checker uses only the Python standard library.

## Relationship to prior work
Berkes and Borda, *Random walks on the circle and Diophantine approximation* (first published 2023-05-06), study general lattice-step circle walks, including Fourier covariance identities in their equation (22), discrepancy, and probabilistic limit laws. Their Fourier identity is essential prior art for the diagonal step, and no originality is claimed for it or for Bernoulli digit independence. The result here instead specifies a deterministic skew product and an analytic *two-observable operator norm*, then gives a sharp all-irrational arithmetic classification: a universal one-third envelope, the exact badly-approximable if-and-only-if, and recovery of every homogeneous approximation exponent. Those three quantitative norm conclusions are not asserted in the inspected sections of that work, and estimates for Kolmogorov discrepancy do not directly imply the variational norm statements.

Butterley, *Exponential mixing for singular skew-products* (arXiv:2308.13618, initial public version 2023-08-25), proves exponential mixing under an induced non-cohomology condition. The present fiber cocycle is explicitly cohomologous to the locally constant digit function, so that theorem's hypothesis is inapplicable. This family supplies a complementary arithmetic mechanism for slow analytic-fiber mixing; no contradiction with exponential mixing under non-cohomology is claimed.

Related results on small-divisor smoothing and random symmetrization have exponent one-third in their *different* operators, but do not identify the present stationary correlation norm or its Diophantine phase diagram. Coincidence of an exponent is not evidence of a reduction between the underlying systems.

## Limitations
The novelty comparison is limited to the examined literature and indexed summaries; an unindexed source proving these specific analytic operator-norm assertions could exist. The result is not a statement of complete topological or spectral mixing for the full skew product. A measurable conjugacy and a supremum over changing observables are used. The constants in the \(\Theta\) classification depend on \(\rho\) and on the Diophantine constant; no leading coefficient for a fixed irrational is claimed. No independent audit has been performed.

## References
1. I. Berkes and B. Borda, *Random walks on the circle and Diophantine approximation*, Journal of the London Mathematical Society **108** (2023), 409–440. Initial publication 2023-05-06. https://doi.org/10.1112/jlms.12749 (especially Section 3, equation (22)).
2. O. Butterley, *Exponential mixing for singular skew-products*, arXiv:2308.13618, initial public version 2023-08-25, later Nonlinearity **37** (2024), 115018. https://arxiv.org/abs/2308.13618 (especially Theorem 1 and Definition 2.6).
3. Classical Dirichlet pigeonhole approximation theorem and standard continued-fraction characterization of badly approximable irrationals (used in the proof in their explicit elementary forms).
