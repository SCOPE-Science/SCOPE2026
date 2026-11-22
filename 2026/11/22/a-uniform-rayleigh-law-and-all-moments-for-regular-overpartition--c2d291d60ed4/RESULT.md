# A uniform Rayleigh law and all moments for regular-overpartition excludants

## Finding
Fix an integer \(\ell\ge2\). Uniformly select an \(\ell\)-regular overpartition of \(n\), namely an overpartition having no part divisible by \(\ell\). Let \(M_{\ell,n}\) be the smallest positive integer not divisible by \(\ell\) that occurs **no times as a nonoverlined part** (an optional overlined occurrence does not count). Define
\[
\rho_\ell=1-\frac1\ell,\qquad
\mu_\ell=\frac{\pi^2\rho_\ell}{4},\qquad
a_\ell=\frac{\pi\rho_\ell^{3/2}}4.
\]
Then, for each fixed real \(x\ge0\),
\[
\boxed{\lim_{n\to\infty}\Pr(M_{\ell,n}>x n^{1/4})=e^{-a_\ell x^2}.}
\]
This is a Rayleigh distributional limit on the \(n^{1/4}\) scale. More strongly, for **every fixed real \(s>0\)**,
\[
\boxed{\lim_{n\to\infty}n^{-s/4}\mathbb E[M_{\ell,n}^s]
=\Gamma(1+s/2)a_\ell^{-s/2}.}
\]
Thus, without restrictions on the fixed integer \(\ell\ge2\),
\[
\mathbb E[M_{\ell,n}]\sim\rho_\ell^{-3/4}n^{1/4},\qquad
\operatorname{Var}(M_{\ell,n})\sim\left(\frac4\pi-1\right)\rho_\ell^{-3/2}n^{1/2}.
\]
The aggregate first moment \(\sigma_\ell(n)=\sum_{\pi\in\overline{\mathcal P}_\ell(n)}\overline{\mathrm{mex}}_\ell(\pi)\) therefore satisfies the all-index asymptotic
\[
\boxed{\sigma_\ell(n)\sim\frac{\exp(\pi\sqrt{\rho_\ell n})}{2\sqrt{2(\ell-1)n}}.}
\]
The two cases \(\ell=2,3\) agree with the previously published first-moment formulas; the all-index formula and the full limiting law and positive-real moments are the new assertions.

There is also an exact finite-size survivor identity, valid for all integers \(n,t\ge0\): let \(u=\lfloor t/\ell\rfloor\), and
\[
S_\ell(t)=\sum_{\substack{1\le j\le t\\\ell\nmid j}}j
=\frac{t(t+1)}2-\frac{\ell u(u+1)}2.
\]
Writing \(\bar p_\ell(k)\) for the \(\ell\)-regular overpartition count, and zero for \(k<0\),
\[
\boxed{\Pr(M_{\ell,n}>t)=\frac{\bar p_\ell(n-S_\ell(t))}{\bar p_\ell(n)}.}
\]

## Assumptions and scope
An overpartition permits at most one overlined copy of each distinct positive part and arbitrarily many nonoverlined copies. The uniform measure gives equal mass to each overpartition of weight \(n\). Every positive admissible size \(j\) with \(\ell\nmid j\) may occur repeatedly. The integer \(\ell\ge2\) and real moment exponent \(s>0\) are fixed before \(n\to\infty\). The probability statement holds for each fixed \(x\ge0\). No claim of uniformity when \(\ell\), \(s\) or \(x\) grows with \(n\), no local limit theorem and no rate of convergence are made. The empty overpartition at \(n=0\) has mex \(1\).

## Proof
**1. Exact survivor bijection.** The event \(M_{\ell,n}>t\) means each admissible integer \(j\le t\) occurs at least once as a *nonoverlined* part. Remove exactly one nonoverlined copy of each such \(j\). The remaining object is an arbitrary \(\ell\)-regular overpartition of weight \(n-S_\ell(t)\): removing/reinserting nonoverlined occurrences does not affect the optional overline on any size. The operation is a bijection, including when some size also has an overlined occurrence. This proves the exact tail formula and the displayed elementary sum for \(S_\ell(t)\).

**2. Base counting asymptotic.** The Euler product for \(\ell\)-regular overpartitions is
\[
\bar P_\ell(q)=\prod_{\substack{m\ge1\\\ell\nmid m}}\frac{1+q^m}{1-q^m}
=\frac{(q^2;q^2)_\infty(q^\ell;q^\ell)_\infty^2}{(q;q)_\infty^2(q^{2\ell};q^{2\ell})_\infty}.
\]
From \((e^{-bt};e^{-bt})_\infty\sim\sqrt{2\pi/(bt)}e^{-\pi^2/(6bt)}\), for every fixed positive \(b\), direct cancellation of the four Euler factors gives
\[
\bar P_\ell(e^{-t})\sim\ell^{-1/2}\exp(\mu_\ell/t)\quad(t\downarrow0).
\]
The coefficient sequence \(\bar p_\ell(n)\) is nonnegative and nondecreasing, since adjoining a nonoverlined part of size \(1\) is injective. Ingham's coefficient Tauberian theorem (as stated in the primary source's Lemma 2.3) yields
\[
\bar p_\ell(n)\sim\frac{\mu_\ell^{1/4}}{2\sqrt{\pi\ell}}n^{-3/4}
\exp(2\sqrt{\mu_\ell n}).\tag{1}
\]
For any \(D_n=O(\sqrt n)\) with \(D_n/\sqrt n\to d\ge0\), equation (1) implies
\[
\frac{\bar p_\ell(n-D_n)}{\bar p_\ell(n)}\longrightarrow e^{-\sqrt{\mu_\ell}d}.\tag{2}
\]
For \(t_n=\lfloor x n^{1/4}\rfloor\), the exact sum has
\[
S_\ell(t_n)=\frac{\rho_\ell}{2}x^2\sqrt n+O_{\ell,x}(n^{1/4}+1).
\]
Insert this into (2). Since \(\rho_\ell\sqrt{\mu_\ell}/2=a_\ell\), the Rayleigh survivor follows. For \(x=0\), the exact event has probability one, consistent with the formula.

**3. Entire moment generating series for every real exponent.** Enumerate the admissible sizes increasingly as \(b_1=1<b_2<\cdots\), and put \(T_j=\sum_{i=1}^j b_i\). Then
\[
b_j=\frac{j}{\rho_\ell}+O_\ell(1),\qquad
T_j=\frac{\rho_\ell b_j^2}{2}+O_\ell(b_j),\qquad
1\le b_{j+1}-b_j\le2.
\]
For every real \(s>0\), the pointwise telescoping identity
\[
M^s=1+\sum_{j\ge1}(b_{j+1}^s-b_j^s)\mathbf1_{\{M>b_j\}}
\]
and the exact survivor bijection prove the formal power-series identity
\[
F_{\ell,s}(q):=\sum_{n\ge0}\sum_{\pi\in\overline{\mathcal P}_\ell(n)}M(\pi)^s q^n
=\bar P_\ell(q)H_{\ell,s}(q),
\]
where
\[
H_{\ell,s}(q)=1+\sum_{j\ge1}(b_{j+1}^s-b_j^s)q^{T_j}.\tag{3}
\]
To determine its singular size, set \(y_j=\sqrt t\,b_j\). On every compact \(y\)-interval, the displayed estimate for \(T_j\) gives \(tT_j=\rho_\ell y_j^2/2+o(1)\), uniformly, and the mesh \(\sqrt t(b_{j+1}-b_j)\) tends to zero. The sum in (3), multiplied by \(t^{s/2}\), is consequently a Stieltjes Riemann sum for
\[
\int_0^\infty e^{-\rho_\ell y^2/2}\,d(y^s)
=\Gamma(1+s/2)\left(\frac2{\rho_\ell}\right)^{s/2}.\tag{4}
\]
For tail control, the bound \(T_j\ge c_\ell b_j^2\) for sufficiently large \(j\), together with bounded successive gaps, dominates the scaled tails by the convergent Gaussian integral \(\int_K^\infty sy^{s-1}e^{-c_\ell y^2}dy\), uniformly in small \(t\). Taking the compact interval large makes that error arbitrarily small, justifying (4) for all real \(s>0\). Thus
\[
F_{\ell,s}(e^{-t})\sim
\frac{\Gamma(1+s/2)}{\sqrt\ell}
\left(\frac{2}{\rho_\ell}\right)^{s/2}
 t^{-s/2}\exp(\mu_\ell/t).\tag{5}
\]
**4. Tauberian transfer and normalization.** The coefficients of \(F_{\ell,s}\) are nonnegative and nondecreasing for **every real \(s>0\)**. Indeed, adding one nonoverlined part of size \(1\) injects the weight-\(n\) objects into weight-\(n+1\) objects and can only preserve or increase their mex, so it can only increase \(M^s\). Apply the same Ingham theorem to (5):
\[
\sum_{\pi\in\overline{\mathcal P}_\ell(n)} M(\pi)^s
\sim\frac{\Gamma(1+s/2)}{2\sqrt{\pi\ell}}
\left(\frac2{\rho_\ell}\right)^{s/2}
\mu_\ell^{(1-s)/4}n^{(s-3)/4}
 e^{2\sqrt{\mu_\ell n}}.\tag{6}
\]
Divide (6) by (1) to get the full positive-real moment limit:
\[
\mathbb E[M_{\ell,n}^s]\sim
\Gamma(1+s/2)\left(\frac{2}{\rho_\ell\sqrt{\mu_\ell}}\right)^{s/2}n^{s/4}
=\Gamma(1+s/2)a_\ell^{-s/2}n^{s/4}.
\]
At \(s=1\), (6) simplifies exactly to the stated all-\(\ell\) aggregate first-moment coefficient \(1/(2\sqrt{2(\ell-1)})\). At \(s=2\), subtracting the square of the \(s=1\) mean yields the variance constant \((4/\pi-1)\rho_\ell^{-3/2}\). Both constants are strictly positive for every integer \(\ell\ge2\).

## Verification
The standalone `verify_mex.py` builds \(\bar p_\ell(n)\) from two independent Euler-factor stages, computes first and second moment coefficients from (3), and independently enumerates every admissible overpartition of \(n\le15\). It checks \(126\) exact brute-force/finite-asymptotic cases over \(2\le\ell\le8\), verifies monotonicity of the first two moment coefficients through weight \(500\), and compares scaled moments at weights \(200\) and \(500\) against the derived constants. Run `python3 verify_mex.py`; the test terminates with `MEX_REGULAR_OVERPARTITIONS_FINITE_OK 126 exact brute and asymptotic spot checks`. Finite data verify arithmetic consistency, **not** the infinite asymptotic. The proof of the latter is the exact bijection, Euler-product estimate, Gaussian Stieltjes limit, and Ingham transfer above.

## Relationship to prior work
Bhowmick and Meher, arXiv:2611.18129v1 (first posted 2026-11-13), **define exactly this regular-overpartition/nonoverlined mex**, obtain its general first-moment generating function (Theorem 1.3, Equation 3.21) and prove a weighted-sum asymptotic for \(\ell=2\) and \(\ell=3\) only (Theorems 1.5–1.6). These coefficients are pre-existing results, and we do not present them as discoveries. The present assertion adds the explicit fixed-\(\ell\) probability law, arbitrary positive-real moments, variance and the first-moment asymptotic for every fixed \(\ell\ge4\); the bivariate generating function itself is not claimed as new. The paper's injection also supplies the monotonicity idea, which is applied here to every real moment weight.

Wagner (2011), Theorems 1 and 3, establishes Rayleigh/Weibull laws for ordinary multiplicity-based partitions, including a general \(\Lambda\)-part scheme. Its objects have unrestricted part multiplicities and **do not include the optional single overlined copy per admissible size with a statistic that ignores overlines**. The specific constants and overpartition all-moment coefficient law here are not an application of Wagner's stated theorems without an additional equivalence proof. Two closely related published-finding corpus studies, *Joint least-multiplicity-gap laws for regular partitions* and *Joint Rayleigh running-minimum law and universal coincidence probabilities for overpartition least gaps*, separately treat ordinary \(\ell\)-regular partitions and unrestricted overpartitions; neither is an all-\(\ell\) law for their intersection, \(\ell\)-regular overpartitions. The less closely related *A Rayleigh limit law for the least absent odd part of an overpartition* counts absent sizes including overlined occurrences and has a distinct observable and rate. We compared these claims and source texts, not merely titles, and found no directly covering statement in the checked sources. This is not a claim of globally established priority.

## Limitations
Only fixed \(\ell\), \(s>0\) and fixed tail thresholds are treated; no finite-size convergence rate, uniform large-\(\ell\) limit or local lattice probability is proved. The exact survivor subtraction, eta asymptotic and Ingham theorem are classical or elementary inputs, not individually novel. The stronger distribution/moments are derived from the primary paper's regular-overpartition framework and not independently audited. A broader unindexed theorem for multiplicity-constrained colored partitions might recover them; no literature search proves global uniqueness.

## References
- S. Bhowmick and N. K. Meher, *The minimal excludant of \(\ell\)-regular overpartitions*, arXiv:2611.18129v1, first public 2026-11-13, https://arxiv.org/html/2611.18129v1, especially Theorems 1.3–1.6, Lemma 2.3, Equation 3.21.
- T. Priya, S. Bhowmick and N. K. Meher, *The minimal excludant and the least \(r\)-gaps of \(\ell\)-regular partitions*, arXiv:2611.07871, first public 2026-11-05, https://arxiv.org/abs/2611.07871.
- N. K. Meher, *The Minimal excludant of \(\ell\)-regular partition*, arXiv:2611.06072, first public 2026-11-04, https://arxiv.org/abs/2611.06072.
- S. Wagner, *Limit distributions of smallest gap and largest repeated part in integer partitions*, Ramanujan Journal 25 (2011), pp. 229–246, https://www.finanz.math.tugraz.at/~wagner/limitdist.pdf, especially Theorems 1 and 3.
- *Joint least-multiplicity-gap laws for regular partitions*, https://github.com/published-finding corpus/2026.
- *Joint Rayleigh running-minimum law and universal coincidence probabilities for overpartition least gaps*, https://github.com/published-finding corpus/2026.
- A. E. Ingham, *A Tauberian theorem for partitions*, Annals of Mathematics 42 (1941), pp. 1075–1090.
