# Interlacing geometric factors and sharp loss budgets in clumsy coupon collection

## Finding
Fix an integer \(m\ge2\). Each round selects one of \(m\) coupon types uniformly. A selected type \(i\) becomes present with probability \(1-p_i\) and absent with probability \(p_i\), independently of its past; other types remain unchanged. Initially all types are absent, and \(T_{\mathbf p}\) is the first round when all are present. Assume \(0\le p_i<1\).

**Theorem (interlacing and sharp loss-budget law).** There are uniquely determined positive numbers \(\lambda_1,\ldots,\lambda_m\), ordered by stage index, such that
\[
T_{\mathbf p}\stackrel d=\sum_{j=1}^m G_{\lambda_j/m}
\]
with independent positive-integer geometric variables. If precisely \(d\) erasure probabilities are strictly positive, then the interlacing is exact:
\[
\boxed{j-1<\lambda_j<j\quad(1\le j\le d),\qquad\lambda_j=j\quad(d<j\le m).}
\]
Thus even with unequal losses and a nonmonotone path, the full first-completion law is an independent geometric sum. Moreover, if \(\mathbf p\) majorizes \(\mathbf v\) (their coordinates have equal sum, and the sorted partial sums of \(\mathbf p\) dominate those of \(\mathbf v\)), then for every \(0<z<1\),
\[
\mathbb E[z^{T_{\mathbf p}}]\le\mathbb E[z^{T_{\mathbf v}}],
\]
with strict inequality unless \(\mathbf p\) is a permutation of \(\mathbf v\). Moreover, \(\mathbb ET_{\mathbf p}\ge\mathbb ET_{\mathbf v}\), again strictly in the nonpermutation case. This is a **probability-generating-function order**, not a claim of usual stochastic order.

At any fixed total clumsiness budget \(P=\sum_i p_i\) in \([0,m)\), the unique (up to identical coordinates) minimizer of expected completion time is the balanced profile \(p_i=P/m\). If \(0<P<1\), the unique maximizers are the permutations of \((P,0,\ldots,0)\). The corresponding sharp range is
\[
\boxed{mH_m+m\sum_{k=1}^{m}\frac1k\binom mk\left(\frac{P}{m-P}\right)^k\ \le\ \mathbb ET_{\mathbf p}\ \le\ mH_m+\frac{mP}{1-P},\quad 0\le P<1,}
\]
where \(H_m=\sum_{j=1}^m1/j\). At \(P=0\) both endpoints coincide. If \(1\le P<m\), the balanced profile still uniquely minimizes the mean, but the supremum of the mean is infinite and is not attained by any admissible profile.

In the concentrated case \(0\le P<1\), an exact distributional factorization holds:
\[
\boxed{T_{(P,0,\ldots,0)}\ \stackrel d=\ G_{(1-P)/m}+\sum_{j=2}^{m}G_{j/m},}
\]
where the summands are independent and \(G_\theta\) is geometric on \(\{1,2,\ldots\}\) with success parameter \(\theta\). Thus concentrating a fixed subunit loss budget changes precisely the slowest geometric component of classical coupon collection.

## Assumptions and scope
All rounds are independent conditional on the selected type, with independent type-specific erasure decisions. The sum \(P\) represents a budget of erasure probabilities, **not** a budget of sampling probabilities. Every \(p_i<1\) is needed to ensure almost-sure finite collection. For the fixed-budget extremizers the admissible domain is \(\{\mathbf p\in[0,1)^m:\sum_i p_i=P\}\), with \(0\le P<m\). Equalities and strict inequalities are for fixed finite \(m\); no limit in \(m\) is assumed.

## Proof
**1. Exact transform.** Set \(q_i=1-p_i\) and \(r_i=p_i/q_i\). Embed the discrete chain into a rate-one Poisson process with iid uniform labels, so each coordinate has an independent rate-\(1/m\) refresh clock. Let \(\tau\) be the continuous-time first all-present hitting time. Starting with every type absent, the probability of being all present at time \(t\) is
\[
A(t)=\prod_{i=1}^m q_i(1-e^{-t/m}).
\]
Starting instead from all present, the probability of being all present at time \(t\) is
\[
B(t)=\prod_{i=1}^m(q_i+p_i e^{-t/m}).
\]
The strong Markov property at \(\tau\) yields the renewal identity \(A(t)=\int_{[0,t]}B(t-v)\,\Pr(\tau\in dv)\). Taking Laplace transforms, with \(u=e^{-t/m}\), gives for every \(s>0\)
\[
\mathbb E[e^{-s\tau}]
=\frac{\int_0^1u^{ms-1}(1-u)^m\,du}
{\int_0^1u^{ms-1}\prod_{i=1}^m(1+r_i u)\,du}.
\]
Conditional on \(T_{\mathbf p}\), the time \(\tau\) is the sum of \(T_{\mathbf p}\) iid unit-rate exponentials, hence \(\mathbb E[e^{-s\tau}]=\mathbb E[(1+s)^{-T_{\mathbf p}}]\). Setting \(s=(1-z)/z\) proves the exact generating transform for \(0<z<1\).

**2. Universal geometric-sum factorization and spectral interlacing.** Let \(e_k\) be the \(k\)-th elementary symmetric polynomial in \((r_1,\ldots,r_m)\), with \(e_0=1\), and let \(d\) be the number of strictly positive \(r_i\). Put \(v=ms\). Evaluating the two integrals in step 1 gives
\[
\mathbb E[e^{-s\tau}]=\frac{m!}{Q(v)},\qquad
Q(v)=\sum_{k=0}^d e_k\prod_{\substack{0\le\ell\le m\\\ell\ne k}}(v+\ell).
\]
The polynomial \(Q\) has degree \(m\), positive leading coefficient \(\sum_ke_k\), and \(Q(0)=m!\). For each integer \(0\le j\le m\), direct substitution shows
\[
Q(-j)=(-1)^j j!(m-j)!\,e_j,
\]
with \(e_j=0\) for \(j>d\). Thus \(Q\) changes sign between \(-j\) and \(-j+1\) for every \(1\le j\le d\), and has a root at every \(-j\) for \(d<j\le m\). These \(m\) distinct roots exhaust its degree and imply the stated uniquely indexed \(\lambda_j\). By \(Q(0)=m!\),
\[
\mathbb E[e^{-s\tau}]=\prod_{j=1}^m\frac{\lambda_j}{v+\lambda_j}.
\]
Finally substitute \(v=m(1-z)/z\) to recognize each factor as the probability-generating function of a positive geometric variable with parameter \(\lambda_j/m\). Since \(0<\lambda_j\le j\le m\), all parameters are valid. The factorization follows from uniqueness of PGFs, including the classical no-loss case \(d=0\).

**3. Strict majorization.** For fixed \(0<u<1\), put \(g_u(x)=1+ux/(1-x)\), \(0\le x<1\). Its logarithm satisfies
\[
\frac{d^2}{dx^2}\log g_u(x)
=\frac{1}{(1-x)^2}-\frac{(1-u)^2}{[1-(1-u)x]^2}>0.
\]
The last inequality follows from \(1-(1-u)x>(1-u)(1-x)\). Strict convexity and the elementary majorization inequality show that \(\prod_i g_u(p_i)>\prod_i g_u(v_i)\) at every \(0<u<1\) unless the vectors agree up to permutation. The positive denominator integral in step 1 therefore strictly increases with majorization, whereas its numerator is independent of the profile. This proves the generating-function inequality.

**4. Exact mean and pair-balancing cost.** For \(s\downarrow0\), subtracting the common \(1/(ms)\) pole from the two integrals in step 1 yields
\[
\mathbb ET_{\mathbf p}
=m\int_0^1\frac{\prod_i(1+r_i u)-(1-u)^m}{u}\,du
=mH_m+m\sum_{\varnothing\ne S\subseteq[m]}\frac{\prod_{i\in S}r_i}{|S|}.
\]
The derivative and integral are legitimate because the finite-state chain has an exponential hitting-time tail: any specified \(m\)-round sequence of successful refreshes has positive probability. Strict convexity of the product integrand gives the strict order of means as well.

For a pair of erasure probabilities \(a,b\) and their midpoint \(c=(a+b)/2\), the exact identity
\[
 g_u(a)g_u(b)-g_u(c)^2
 =\frac{u(a-b)^2[2-a-b+(a+b-1)u]}
 {(1-a)(1-b)(2-a-b)^2}
\]
gives the positive balancing penalty
\[
\begin{aligned}
&\mathbb ET_{(a,b,\mathbf d)}-\mathbb ET_{(c,c,\mathbf d)}\\
&=\frac{m(a-b)^2}{(1-a)(1-b)(2-a-b)^2}
\int_0^1[2-a-b+(a+b-1)u]\prod_{j\in\mathbf d}(1+r_j u)\,du>0
\end{aligned}
\]
whenever \(a\ne b\), where \(\mathbf d\) lists the other coordinates. The bracket is strictly positive for \(0\le u\le1\), so no equality is hidden at a boundary.

**5. Sharp extrema and the budget threshold.** At fixed \(P\), the equal vector is majorized by every feasible profile. For \(0<P<1\), the concentrated vector \((P,0,\ldots,0)\) majorizes every feasible profile. Strictness gives precisely the claimed unique minimizer and maximizers. Substituting \(r_i=P/(m-P)\) at the equal point and \((r_1,r_2,\ldots)=(P/(1-P),0,\ldots)\) at the concentrated point into step 4 produces both endpoint formulas. If \(1\le P<m\), admissible vectors with \(p_1\uparrow1\) exist while keeping the total fixed; the waiting time until the first successful refresh of type 1 is geometric with mean \(m/(1-p_1)\), and is bounded above by \(T_{\mathbf p}\). Thus the mean has infinite supremum although every individual admissible mean is finite.

**6. Exact one-defect law.** For \(\mathbf p=(P,0,\ldots,0)\), \(0\le P<1\), the integral ratio of step 1 simplifies algebraically to
\[
\mathbb E[z^{T_{\mathbf p}}]
=\frac{(1-P)/m}{(1-P)/m+(1-z)/z}
\prod_{j=2}^{m}\frac{j/m}{j/m+(1-z)/z}.
\]
Each factor is the generating function of a positive-integer geometric variable with its indicated success parameter. Uniqueness of probability generating functions proves the independent-sum law.

## Verification
The attached self-contained `checker.py` reconstructs the absorbing Markov chain on all proper subsets and solves its linear equations over `fractions.Fraction`, independently of the Poissonization derivation. It compares the exact expected hitting time and the generating function at three rational arguments with the integral expansions for twelve heterogeneous profiles on two, three, and four types. It also checks exact balanced and concentrated bounds, the one-defect factorization, and the defining polynomial’s alternating-sign interlacing certificate, including nonzero and zero loss budgets. Run `python3 checker.py`; it reports **405 independent exact-rational assertions passed**. These finite checks do not prove the all-size inequalities; the strict convexity argument above does.

For example, at \(m=3\) and \(P=1/2\), the balanced mean is \(936/125\), the sharp concentrated maximum is \(17/2\), and the gap is \(253/250\).

## Relationship to prior work
Attrill and Garoni [1] analyze the clumsy collector with one common erasure probability, and Long [2] treats fixed common erasure in a broader stationary-entry framework. Their results do not compare vectors of **type-specific** erasure probabilities at a fixed total erasure budget. The general heterogeneous finite generating-transform identity is not claimed as new: it is a starting identity also derivable from an earlier heterogeneous finite waiting-time transform. The result here is the full interlacing independent-geometric factorization for all type-specific loss profiles together with strict all-argument majorization, complete sharp budget extrema, an explicit balancing penalty, and the budget-one unboundedness threshold. Kleiner [3] proves a separate majorization theorem for **sampling probabilities** in a pre-discovery-deadline model; that success event differs from repeatedly refreshing already observed coupons in this theorem. Fixed heterogeneous sampling weights, rather than uniform type selection, are outside the present scope.

## Limitations
Generating-function comparison alone does not establish ordinary stochastic domination of \(T_{\mathbf p}\). Only the objective of first simultaneous presence is treated; coupon multiplicities and nonuniform type-selection rates are not. Literature-priority uncertainty remains for broad random-scan product-chain comparison theorems not indexed under coupon-collection terminology. The standalone exact computations cover finite state spaces and do not constitute infinite-family certification. Independent validation has not been performed.

## References
[1] L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem*, arXiv:2605.14206v1, publicly posted 14 May 2026. https://arxiv.org/html/2605.14206v1

[2] C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511v1, publicly posted 14 May 2026. https://arxiv.org/html/2605.14511v1

[3] *The Fragile Coupon Collector: Random Deadlines, Critical Fragility, and Optimal Sampling*, *Mathematics* **14** (2026), article 3729. https://www.mdpi.com/2227-7390/14/20/3729
