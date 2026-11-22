# The exact modal staircase of the type-I generalized discrete half-logistic law

## Finding

For the survival-preserving type-I generalized discrete half-logistic count law of Barbiero and Hitaj, the entire shape-parameter modal phase diagram is a strictly ordered staircase. Fix any \(\theta>0\) and write
\[
 a_j=\tanh(j\theta/2),\qquad
 p_j(\alpha,\theta)=a_{j+1}^{\alpha}-a_j^{\alpha}
 \quad(j=0,1,2,\ldots;\ \alpha>0),
\]
where \(a_0=0\). For each integer \(k\ge0\), there exists a **unique** \(\alpha_k(\theta)>1\) such that
\[
 a_{k+2}^{\alpha_k}-2a_{k+1}^{\alpha_k}+a_k^{\alpha_k}=0.
\]
These thresholds are strictly increasing and unbounded:
\[
 1<\alpha_0<\alpha_1<\alpha_2<\cdots\longrightarrow\infty.
\]
For \(0<\alpha<\alpha_0\), the unique mode is zero. For each \(k\ge1\), if \(\alpha_{k-1}<\alpha<\alpha_k\), the **unique** mode is \(k\). At \(\alpha=\alpha_k\), the **only** two modes are adjacent indices \(k\) and \(k+1\). Thus there are never three modes or nonadjacent tied modes.

The first boundary is explicit:
\[
 \alpha_0(\theta)=\frac{\log2}{\log\bigl(\tanh\theta/\tanh(\theta/2)\bigr)}.
\]
Put \(q=e^{-\theta}\in(0,1)\). Define \(r_q\) as the unique solution in \((0,1)\) of
\[
 1-2r+r^{1+1/q}=0
\]
(the other solution \(r=1\) is excluded), and set
\[
 C_q=\frac{-\log r_q}{2q(1-q)}.
\]
For fixed \(\theta>0\), the high-index boundaries obey the **sharp asymptotic**
\[
 \boxed{\ \alpha_k(\theta)e^{-k\theta}=C_q+O_{\theta}(e^{-2k\theta})\ },
 \qquad k\to\infty.
\]
In particular, the modal index at large \(\alpha\) equals \((\log\alpha)/\theta+O_{\theta}(1)\).

## Assumptions and scope

The distribution has full nonnegative-integer support, fixed unit-length sampling bins \([j,j+1)\), \(\theta>0\) and continuous shape parameter \(\alpha>0\). The underlying continuous cdf is \(F_{\alpha,\theta}(x)=\tanh(\theta x/2)^\alpha\) for \(x\ge0\), and the discrete law is that of \(\lfloor X\rfloor\). The limit theorem fixes \(\theta\) and sends the modal threshold index \(k\) to infinity; it does not assert a uniform estimate as \(\theta\to0\) or \(\theta\to\infty\). A mode is a global maximizer of the probability mass, not merely a local maximizer.

## Proof

**1. Monotone small-shape regime.** Write \(B(x)=\tanh(\theta x/2)\). The density of the underlying continuous law is
\[
 f_{\alpha}(x)=\alpha B(x)^{\alpha-1}\,\frac{\theta}{2}\operatorname{sech}^2(\theta x/2),\quad x>0.
\]
When \(0<\alpha\le1\), each of the nonconstant positive factors depending on \(x\) is decreasing: \(B^{\alpha-1}\) is nonincreasing and the squared hyperbolic secant is strictly decreasing. Hence \(f_\alpha\), and therefore its equal-length interval masses \(p_j=\int_j^{j+1}f_\alpha(x)\,dx\), are strictly decreasing. In particular \(p_{k+1}(1)<p_k(1)\) for every \(k\ge0\).

**2. Strict log-concavity when \(\alpha\ge1\).** For \(u=\theta x/2>0\), direct differentiation gives
\[
 \frac{d^2}{du^2}\log f_\alpha(2u/\theta)
 =-\frac{4(\alpha-1)\cosh(2u)}{\sinh^2(2u)}-2\operatorname{sech}^2u<0.
\]
The strict log-concavity of the **interval masses** has an elementary direct proof, so no unproved preservation theorem is required. For \(s,t\in(0,1)\), the two arguments \(k+1+s\) and \(k+1+t\) are strictly between \(k+s\) and \(k+2+t\), and their sum is the same as the sum of those outer arguments. Strict concavity of \(\log f_\alpha\) therefore implies
\[
 f_\alpha(k+1+s)f_\alpha(k+1+t)
 >f_\alpha(k+s)f_\alpha(k+2+t).
\]
Integrating over \((s,t)\in(0,1)^2\) yields
\[
 p_{k+1}^2>p_kp_{k+2}\quad(k\ge0,\ \alpha\ge1).
\]
Thus successive mass ratios strictly decrease with the index, excluding more than two tied global modes.

**3. Strict crossing in the shape parameter.** If \(\beta>\alpha>0\), the pointwise density ratio is
\[
 \frac{f_\beta(x)}{f_\alpha(x)}=\frac{\beta}{\alpha}B(x)^{\beta-\alpha},
\]
strictly increasing in \(x>0\). Integrating the resulting strict inequality for every \(x\in(k,k+1)\) and \(y\in(k+1,k+2)\) proves that \(p_{k+1}(\alpha)/p_k(\alpha)\) is **strictly increasing** in \(\alpha\). Its value is below one at \(\alpha=1\). On the other hand, as \(\alpha\to\infty\) for fixed \(k\), \(p_k\sim a_{k+1}^{\alpha}\) and \(p_{k+1}\sim a_{k+2}^{\alpha}\), whence their ratio tends to infinity. Continuity and the strict monotone crossing yield exactly one \(\alpha_k>1\) with \(p_{k+1}=p_k\).

At \(\alpha=\alpha_k\), strict log-concavity gives \(p_{k+2}<p_{k+1}=p_k\). The strict shape-ratio monotonicity then implies \(\alpha_{k+1}>\alpha_k\). Every \(\alpha\) lies between consecutive thresholds once their divergence is established below; adjacent comparisons have opposite signs on the two sides of that index, proving the complete phase diagram. At the first crossing \(a_2^{\alpha_0}=2a_1^{\alpha_0}\), which gives the stated closed form.

**4. Threshold scaling and divergence.** Fix \(q=e^{-\theta}\). Since
\[
 a_j=\frac{1-q^j}{1+q^j},\qquad
 \log a_j=-2q^j+O(q^{3j})\quad(j\to\infty),
\]
write \(\alpha=\gamma q^{-k}\) with fixed \(\gamma>0\). The signed adjacent-mass difference becomes
\[
 H_k(\gamma)=a_{k+2}^{\gamma q^{-k}}-2a_{k+1}^{\gamma q^{-k}}+a_k^{\gamma q^{-k}},
\]
with \(H_k(\gamma)=H(\gamma)+O_{\theta,\gamma}(q^{2k})\), uniformly on compact positive \(\gamma\)-intervals, where
\[
 H(\gamma)=e^{-2\gamma q^2}-2e^{-2\gamma q}+e^{-2\gamma}.
\]
Set \(r=e^{-2\gamma q(1-q)}\). Then \(H(\gamma)=e^{-2\gamma q^2}[1-2r+r^{1+1/q}]\). The bracketed function of \(r\in(0,1]\) is strictly convex, equals one at zero and zero at one, and has positive derivative at one. Therefore it has exactly one additional root \(r_q\in(0,1)\), crossed with strictly negative derivative. Equivalently, \(H(\gamma)\) changes from negative to positive at the unique positive \(\gamma=C_q\), with \(H'(C_q)>0\).

Choose fixed \(0<c_-<C_q<c_+\). For all sufficiently large \(k\), \(H_k(c_-)<0<H_k(c_+)\); these are comparisons at \(\alpha=c_\pm q^{-k}>1\). The already-proved unique crossing traps \(\gamma_k=\alpha_kq^k\) inside \((c_-,c_+)\). Uniform convergence and uniqueness imply \(\gamma_k\to C_q\). The displayed error bound plus the simple derivative \(H'(C_q)>0\) sharpen this to \(\gamma_k=C_q+O_\theta(q^{2k})\). In particular \(\alpha_k\to\infty\), completing the preceding classification and yielding the modal-index estimate.

## Verification

The included `checker.py` uses Python's decimal arithmetic at 95-digit precision to evaluate the exact CDF differences, bisect each threshold, test both signs around each root, verify the strict threshold ordering and nearby discrete log-concavity, and compare high-index thresholds against the independently defined limiting root. It reports 484 passing finite numerical diagnostics over four fixed \(\theta\)-values; these checks support arithmetic and normalization only. The general theorems, uniqueness and asymptotic error are proved in the preceding four steps, not inferred from finite experiments.

At \(\theta=1\), example values are \(\alpha_0=1.387417158997\ldots\), \(\alpha_1=3.481731105673\ldots\), \(\alpha_2=9.329757571126\ldots\), and \(C_{e^{-1}}=1.259769565418\ldots\). The published example \(\alpha_0\) agrees with the first threshold.

## Relationship to prior work

Barbiero and Hitaj (2024, Sect. 4) define these mass probabilities and show by example that the first two bins can tie, providing the first crossing at \(\theta=1\). They do not provide the ordered thresholds for every mode, strict global classification for all positive parameters, or the large-index transition constant and error. Their Sect. 3 proves log-concavity only for the one-parameter case \(\alpha=1\), and Sect. 4 notes that log-concavity fails for some \(\alpha<1\). The second Barbiero–Hitaj (2024) construction uses normalized sampled **density** values rather than unit-bin integrals of the exponentiated cdf; it is not the same law. Classical likelihood-ratio ordering and log-concavity are ingredients, not claimed here as new general theorems. Similar modal-staircase results for other probability families do not imply the specific strict thresholds and \(C_q\) asymptotic for this one.

## Limitations

This is a mathematical description of global modes, not a power comparison of fitted count models, estimator-consistency theorem, hazard-phase classification or claim of optimal discretization. At \(\alpha\in(0,1)\), the masses are strictly decreasing but need not be log-concave. The \(O_{\theta}\)-bound is pointwise in fixed positive \(\theta\). Literature comparisons establish no claim of comprehensive historical priority; independent review is still required.

## References

1. A. Barbiero and A. Hitaj, *Discrete half-logistic distributions with applications in reliability and risk analysis*, Annals of Operations Research 340 (2024), 27–57. First public online date 2024-01-19. https://doi.org/10.1007/s10479-023-05807-3 (especially Sections 3, 4 and 9).
2. A. Barbiero and A. Hitaj, *A Discrete Version of the Half-Logistic Distribution Based on the Mimicking of the Probability Density Function*, Journal of the Indian Society for Probability and Statistics 25 (2024), 373–394. https://doi.org/10.1007/s41096-024-00185-w (especially Section 5; distinct discretization).
3. G. M. Cordeiro, M. Alizadeh and P. R. D. Marinho, *The type I half-logistic family of distributions*, Journal of Statistical Computation and Simulation 86 (2016), 707–728. https://doi.org/10.1080/00949655.2015.1031233 (continuous-family context).
