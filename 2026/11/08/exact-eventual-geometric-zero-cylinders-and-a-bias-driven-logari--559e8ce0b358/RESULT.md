# Exact eventual geometric zero cylinders and a bias-driven logarithmic edge transition

## Finding

For the stationary signed-digit process of the independent random symmetric doubling maps of Dajani, Kalle and Maggioni, **every sufficiently long consecutive-zero cylinder has exactly geometric continuation rate one-half**. The geometric prefactor is explicit for every map parameter and every strictly positive Bernoulli bias, including parameters where the usual matching condition fails. As the map parameter approaches its singular endpoint, the prefactor has a logarithmic correction at balanced switching and a different, log-periodically modulated power law at biased switching.

Specifically, let \(1<\alpha\leq2\), \(0<p<1\), \(a=\alpha-1\), and \(q=1-p\). Define
\[
J=\left\lceil\log _2(1/a)\right\rceil,
\qquad b_j=\min\{1/2,2^{j-1}a\}\quad(0\leq j\leq J),
\]
and set
\[
C(a,p)=\frac{2}{1+a}\left[a+\sum_{j=1}^{J}(b_j-b_{j-1})(p^j+q^j)\right]. \tag{1}
\]
The sum is empty if \(J=0\). For the successive digits \(d_1,d_2,\ldots\), every integer \(n\geq\max\{1,J\}\) satisfies
\[
\boxed{\mathbb P(d_1=\cdots=d_n=0)=2^{-n}C(a,p).} \tag{2}
\]
In particular, for all such \(n\), the conditional probability of one more zero equals \(1/2\). Furthermore, \(0<C(a,p)\leq1\), with equality \(C=1\) precisely when \(\alpha\geq3/2\). In the latter range, (2) holds for *every* \(n\geq1\).

For the edge \(a\downarrow0\), put \(\vartheta=2^Ja\in[1,2)\). At balanced switching, \(p=q=1/2\), the exact prefactor is
\[
\boxed{C(a,1/2)=\frac{a}{1+a}\left(J+\frac{2}{\vartheta}\right)
=a\log_2(1/a)+O(a).} \tag{3}
\]
At any fixed biased value \(p\ne1/2\), write \(s=\max\{p,q\}\in(1/2,1)\) and \(\delta=-\log_2s\in(0,1)\). Then
\[
\boxed{C(a,p)=a^\delta F_s(\vartheta)+O_p(a),\qquad
F_s(v)=v^{-\delta}\left[1+\frac{1-s}{2s-1}v\right].} \tag{4}
\]
The amplitude \(F_s\) is positive and not constant on \([1,2]\), and \(F_s(1)=F_s(2)\); hence (4) exhibits genuine logarithmic-periodic modulation of the normalized zero-block tail. The balanced logarithmic law and the biased power law are different endpoint regimes.

## Assumptions and scope

Let \(\alpha\in(1,2]\) and independently at each time choose map \(T_{\alpha,0}\) with probability \(p\in(0,1)\), or map \(T_{\alpha,1}\) with probability \(q=1-p\). On \([-1,1]\), the maps, up to boundary conventions of zero stationary probability, are
\[
T_{\alpha,0}(x)=
\begin{cases}2x+\alpha,&x\leq(1-\alpha)/2,\\
2x,&(1-\alpha)/2<x\leq1/2,\\
2x-\alpha,&x>1/2,
\end{cases}
\]
\[
T_{\alpha,1}(x)=
\begin{cases}2x+\alpha,&x<-1/2,\\
2x,&-1/2\leq x<(\alpha-1)/2,\\
2x-\alpha,&x\geq(\alpha-1)/2.
\end{cases}
\]
The digit \(d_k\in\{-1,0,1\}\) records the additive term \(-\alpha d_k\) in the selected branch. The initial position is distributed according to the unique absolutely continuous stationary probability \(\mu_{\alpha,p}\); the future map choices have their independent Bernoulli law. This is a stationary *annealed cylinder probability*, not a claim about all deterministic initial conditions. Since \(J\) is determined by \(a\), the cutoff \(\max\{1,J\}\) is finite for each fixed \(\alpha>1\); no uniform cutoff is asserted as \(\alpha\downarrow1\).

The density \(f_{\alpha,p}\) of \(\mu_{\alpha,p}\) satisfies
\[
f_{\alpha,p}(x)=\frac1\alpha\quad\text{for a.e. }|x|\leq\alpha-1. \tag{5}
\]
Equation (5) is an explicit premise whose justification is essential: Lemma 3.8 of Dajani--Kalle--Maggioni gives it at strong-matching parameters, which are of full Lebesgue measure by their Theorem 3.5; the proof of their Lemma 3.11 establishes local \(L^1\)-continuity of the invariant density in \(\alpha\) for fixed \(p\) on \((1,3/2)\). Approximation by matching parameters and restriction to a compact interior subinterval of the moving plateau therefore yield (5) for *every* interior parameter. Their treatment of \(\alpha\geq3/2\) supplies (5) there. This passage uses more than continuity of just the single-digit frequency.

## Proof

**1. Zero-branch reduction.** Write \(c=a/2\) and define the single-step probability of choosing the zero digit at position \(x\):
\[
g(x)=\begin{cases}
1,&|x|<c,\\
p,&c<x<1/2,\\
q,&-1/2<x<-c,\\
0,&|x|>1/2.
\end{cases} \tag{6}
\]
Values at finitely many endpoints are irrelevant. If the first \(n\) digits are zero, the first \(n\) positions equal \(x,2x,\ldots,2^{n-1}x\). Necessarily \(|x|\leq2^{-n}\), and conversely the product \(\prod_{k=0}^{n-1}g(2^kx)\) gives the exact Bernoulli-averaged indicator of this event. For \(n\geq J\), \(2^{-n}\leq a\), so (5) applies throughout the integration domain. Consequently
\[
\mathbb P(0^n)=\frac1{1+a}
\int_{-2^{-n}}^{2^{-n}}\prod_{k=0}^{n-1}g(2^kx)\,dx. \tag{7}
\]

**2. Finite level decomposition.** Rescale \(u=2^{n-1}x\), so that \(u\in[-1/2,1/2]\), and the product is \(\prod_{j=0}^{n-1}g(u/2^j)\). For each \(j\geq J\), the factor is one, since \(|u|/2^j\leq2^{-J-1}\leq a/2=c\). The product is therefore independent of \(n\) once \(n\geq J\). On \(0<u<c\) it is one; on each interval \(b_{j-1}<u<b_j\), \(1\leq j\leq J\), it equals \(p^j\). By reflection the corresponding negative-side factor is \(q^j\). Since the interval \([-c,c]\) has length \(a\),
\[
\int_{-1/2}^{1/2}\prod_{j=0}^{n-1}g(u/2^j)\,du
=a+\sum_{j=1}^J(b_j-b_{j-1})(p^j+q^j). \tag{8}
\]
Equations (7)--(8) give (1)--(2), including the \(J=0\) case after taking \(n\geq1\). As \(p^j+q^j\leq1\) for each \(j\geq1\), with strict inequality for \(j\geq2\), the integral is at most \(a+(1/2-a/2)=(1+a)/2\). When \(a\geq1/2\), \(J\leq1\) and equality holds. When \(a<1/2\), \(J\geq2\) and the final interval has strictly positive length, forcing strict inequality. This proves the equality criterion and the geometric continuation property.

**3. Balanced switching.** For \(a\in(0,1)\), write \(\vartheta=2^Ja\in[1,2)\). All nonterminal increments satisfy \(b_j-b_{j-1}=a2^{j-2}\) for \(1\leq j<J\), while \(b_J-b_{J-1}=1/2-\vartheta/4\). If \(p=q=1/2\), the sum in (1) becomes
\[
\sum_{j=1}^J(b_j-b_{j-1})2^{1-j}
=\frac{a(J-1)}2+\frac{a}{\vartheta}-\frac{a}{2}
=\frac{a(J-2)}2+\frac{a}{\vartheta}.
\]
Adding the initial \(a\) gives the integral \(aJ/2+a/\vartheta\), hence (3). Since \(J=\log_2(1/a)+\log_2\vartheta\) and \(1\leq\vartheta<2\), the error is \(O(a)\).

**4. Biased switching.** Define \(A_z=c+\sum_{j=1}^{J}(b_j-b_{j-1})z^j\), so that \(C=2(A_p+A_q)/(1+a)\). For any fixed \(z>1/2\), finite geometric summation gives
\[
A_z=\frac{z^J}{2}\left[1+\vartheta\frac{1-z}{2z-1}\right]+O_z(a). \tag{9}
\]
For \(0<z<1/2\), the same sum is \(O_z(a)\). Take \(z=s=\max\{p,q\}\), with the other probability below \(1/2\). Then \(s^J=(a/\vartheta)^\delta\) and \(1/(1+a)=1+O(a)\), proving (4). Finally,
\[
F_s'(v)=v^{-\delta-1}\left[-\delta+(1-\delta)\frac{1-s}{2s-1}v\right].
\]
The affine expression in brackets is not identically zero, so \(F_s\) is nonconstant. The identity \(s=2^{-\delta}\) yields \(F_s(1)=F_s(2)\), making the leading modulation continuous across dyadic parameter boundaries.

## Verification

The accompanying `CHECK.py` independently partitions the original-position cylinder into exact rational branch cells and integrates the independent map-choice weights without using formula (1). It checks 423 finite exact-rational identities and inequalities over 40 parameter pairs and eight consecutive block lengths beyond their cutoffs. This is a finite numerical/algebraic cross-check only: the parameter-uniform statement, the matching-to-all-parameters passage, and the two endpoint asymptotics are justified in the analytic proof above.

## Relationship to prior work

Dajani--Kalle--Maggioni (2020 preprint, 2021 journal), Section 3, define the random maps and digits; their Theorem 3.5 and Lemmas 3.8 and 3.11 provide matching, the plateau, and density continuity. Their Theorem 3.12 concerns **one-digit** zero frequency and does not state the consecutive-zero cylinders or edge scaling. The earlier deterministic symmetric doubling analysis by Dajani--Kalle (2017) investigates matching words in the itinerary of a distinguished boundary orbit, and one-digit frequencies for a different deterministic process; it does not furnish a stationary **random** zero-cylinder law. Kalle--Maggioni (2018) gives a general method for invariant densities. Formula (2) uses the established density as input but supplies a new explicit long-cylinder calculation and its singular small-parameter dichotomy.

The exact relationship to broader word-frequency or renewal literature has not been certified exhaustively. An equivalent theorem outside the inspected sources would supersede any originality inference made from the limited comparisons.

## Limitations

The statement excludes \(\alpha=1\) and switching endpoint probabilities \(p=0,1\). Error constants in (4) may diverge as \(p\to1/2\); thus (4) is not uniform in a simultaneous bias-and-parameter limit. Formula (2) does not assert independent digits, a Markov property for the entire signed-digit process, or a memoryless run law before its parameter-dependent cutoff. No result about nonzero signed-word cylinders is claimed. The stationarity and density premises are literature results, not re-proved here from first principles. The finite checker does not certify infinite statements. Independent audit and publication-priority verification remain outstanding.

## References

1. K. Dajani, C. Kalle and M. Maggioni, *Matching for random systems with an application to minimal weight expansions*, arXiv:2008.04398 (first posted 2020-08-10), *Nonlinearity* 34 (2021), 3676--3708, DOI:10.1088/1361-6544/abebc6. https://arxiv.org/abs/2008.04398 . See specifically Sections 3.1--3.4 and Lemmas 3.8, 3.11.
2. K. Dajani and C. Kalle, *Invariant measures, matching and the frequency of 0 for signed binary expansions*, arXiv:1703.06335 (2017). https://arxiv.org/abs/1703.06335 .
3. C. Kalle and M. Maggioni, *Invariant densities for random systems of the interval*, arXiv:1805.11430 (2018). https://arxiv.org/abs/1805.11430 .
