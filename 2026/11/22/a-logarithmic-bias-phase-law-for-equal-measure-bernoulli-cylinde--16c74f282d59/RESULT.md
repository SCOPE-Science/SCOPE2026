# A logarithmic-bias phase law for equal-measure Bernoulli cylinder holes

## Finding

Let \(k\ge3\) be an integer. In the one-sided binary Bernoulli shift with probability \(p\in(0,1)\) of symbol \(1\), compare the two length-\(2k+2\) cylinder holes defined by
\[
U_k=0^k11 0^k,\qquad V_k=1 0^{2k}1.
\]
Their measures agree identically: \(\mu_p([U_k])=\mu_p([V_k])=p^2(1-p)^{2k}\). Write \(\gamma_U(p)\) and \(\gamma_V(p)\) for the exponential escape rates under repeated application of the left shift.

**Theorem.** For each \(k\ge3\), there is exactly one \(p_k\in(0,1)\) at which these escape rates agree. It is algebraic and is specified without an eigenvalue calculation: \(t_k\) is the unique root in \((0,1)\) of
\[
2t^k-1=t^{3k}(1-t),
\]
and
\[
p_k=\left(1+\sum_{j=0}^{k-1}t_k^{-j}\right)^{-1}.
\]
The complete sharp ordering is
\[
\gamma_U(p)>\gamma_V(p)\quad(0<p<p_k),\qquad
\gamma_U(p)<\gamma_V(p)\quad(p_k<p<1).
\]
Moreover,
\[
1-2^{-1/k}<p_k<\frac1{k+1},\qquad
p_k=\frac{\log2}{k}-\frac{(\log2)(1+2\log2)}{8k^2}+O(k^{-3}).
\]
In particular, \(k p_k\to\log2\). Values for \(k=3,4,8\) are approximately \(0.207974786333\), \(0.160272787980\), and \(0.083391007392\), respectively.

The case \(k=2\), whose two words are \(001100\) and \(100001\), was already exhibited as a crossover example by Bonanno, Cristadoro and Lenci (2022, Remark 3.7). It is not asserted to be a new example. The present claim is the all-parameter classification for the growing family \(k\ge3\), its exact unique algebraic thresholds, and the logarithmic two-term asymptotic law.

## Assumptions and scope

The probability law is iid on \(\{0,1\}^{\mathbb N}\), with \(\Pr(1)=p\) and \(\Pr(0)=q=1-p\), for fixed \(p\in(0,1)\). If \(w\) is a finite word, set \(H_w=[w]\) and let
\[
\gamma_w(p)=-\lim_{n\to\infty}\frac1n\log \mu_p\{x:\sigma^j x\notin H_w\text{ for all }0\le j<n\}.
\]
The limit is the negative logarithm of the Perron root of the finite forbidden-word prefix automaton. Equivalently it is the logarithm of the smallest positive zero of the weighted autocorrelation denominator below. The words are distinct, have the same length and the same Bernoulli measure for every \(p\), and each has a nontrivial border.

For a word \(w\) of length \(N\), define its weighted autocorrelation polynomial
\[
C_w(z)=1+\sum_{\substack{1\le d<N\\w_{[0,N-d)}=w_{[d,N)}}}\left(\prod_{i=N-d}^{N-1}\Pr(w_i)\right)z^d.
\]
Let \(a_j\) be the probability that an iid word of length \(j\) has no copy of \(w\). The standard single-word avoidance/first-hit identity says that its length-indexed generating series \(A_w(z)=\sum_{j\ge0}a_j z^j\) is \(C_w(z)/D_w(z)\) with
\[
D_w(z)=(1-z)C_w(z)+\mu_p([w])z^N.
\]
Survival for \(n\) shift times as defined above has probability \(a_{n+N-1}\), including \(n=0\) since \(a_{N-1}=1\). Its generating series is \(z^{-(N-1)}\bigl(A_w(z)-\sum_{j=0}^{N-2}z^j\bigr)\), so the shift in indexing does not change the positive pole or escape rate. The least positive zero of \(D_w\) is \(r_w=e^{\gamma_w}>1\). All comparisons below concern these least positive zeros, not arbitrary algebraic zeros.

## Proof

**1. Exact overlap polynomials.** The proper borders of \(U_k\) are precisely \(0^j\), for \(1\le j\le k\); the sole proper border of \(V_k\) is \(1\). With \(N=2k+2\) and \(m=p^2q^{2k}\), the preceding definition gives
\[
C_U(z)=1+\sum_{j=1}^{k}p^2q^{2k-j}z^{N-j},\qquad
C_V(z)=1+pq^{2k}z^{N-1}.
\]
Consequently
\[
C_U(z)-C_V(z)=pq^{2k}z^{N-1}
\left(\frac pq\sum_{\ell=0}^{k-1}(qz)^{-\ell}-1\right).
\]
Call the parenthetical factor \(H_k(p,z)-1\).

**2. The isolated root for \(V_k\).** Substitute the explicit \(C_V\) in \(D_V\). It simplifies exactly to
\[
D_V(z)=1-z+pq^{2k}z^{2k+1}(1-qz).
\]
Put \(t=qz\). For \(q<t<1\), the zero equation is
\[
G(p,t):=t-q-p t^{2k+1}(1-t)=0.
\]
We have \(G(p,q)<0\) and \(G(p,1)>0\). Moreover,
\[
\partial_tG=1-p\,t^{2k}((2k+1)-(2k+2)t)>0.
\]
Indeed the maximum of the subtracted factor \(t^{2k}((2k+1)-(2k+2)t)\) on \([0,1]\) occurs at \(t=k/(k+1)\) and equals \((k/(k+1))^{2k}<1\). Thus there is a unique zero \(t(p)\in(q,1)\). Since \(D_V(z)>0\) on \([0,1]\), this zero corresponds to \(r_V=t(p)/q\), the first positive denominator zero. Implicit differentiation gives
\[
\partial_pG=1-t^{2k+1}(1-t)>0,
\]
so \(t'(p)<0\).

**3. Unique possible crossing.** At an actual equality \(r_U=r_V\), the common factor \(m z^N\) in the two denominators cancels. As \(r_V>1\), the equality implies \(C_U(r_V)=C_V(r_V)\), hence
\[
H_k(p):=\frac pq\sum_{\ell=0}^{k-1}t(p)^{-\ell}=1.
\]
Since \(p/q\) strictly increases and \(t(p)\) strictly decreases, \(H_k(p)\) strictly increases. Its limits as \(p\downarrow0\) and \(p\uparrow1\) are \(0\) and \(+\infty\), respectively. Therefore the equation has exactly one parameter \(p_k\).

We next prove that an *actual* crossing occurs. If \(p<1-2^{-1/k}\), then for every \(1\le z<1/q\),
\[
H_k(p,z)\le\frac pq\sum_{\ell=0}^{k-1}q^{-\ell}=q^{-k}-1<1.
\]
Thus \(C_U<C_V\). Evaluating \(D_V\) at the first zero \(r_U\) gives \(D_V(r_U)<0\), so \(r_V<r_U\) and \(\gamma_V<\gamma_U\). If \(p>1/(k+1)\), then \(H_k(p,z)\ge kp/q>1\) throughout the same interval; evaluating \(D_U\) at \(r_V\) yields \(r_U<r_V\) and \(\gamma_U<\gamma_V\).

For completeness, both first roots lie strictly between \(1\) and \(1/q\). Their denominators are positive at \(1\); \(D_V(1/q)=-p/q<0\), and
\[
D_U(1/q)=-\frac{p}{q^3}(q^2-pq+kp^2)<0.
\]
The last quadratic is positive for \(k\ge2\) because \(q^2-pq+kp^2=1-3p+(k+2)p^2\) has negative discriminant. The smallest zeros depend continuously on \(p\), by Perron–Frobenius continuity for the primitive finite prefix automata. Since the two orderings differ at the displayed endpoint ranges, continuity forces at least one equality; the uniqueness of a possible equality proves that equality occurs only at \(p_k\), with precisely the asserted strict inequalities elsewhere.

**4. Algebraic equation and bounds.** At \(p=p_k\), write \(t=t(p_k)\) and \(S=\sum_{\ell=0}^{k-1}t^{-\ell}\). The crossing equation is \(q=pS\), hence \(p=(1+S)^{-1}\). Substituting into \(G(p,t)=0\) gives
\[
t(1+S)-S=t^{2k+1}(1-t).
\]
The finite-geometric identity \((1-t)S=t^{1-k}-t\) then yields
\[
2t^k-1=t^{3k}(1-t).
\]
Conversely the equation and the formula for \(p\) reverse these steps, so this is an exact specification. The function
\[
J_k(t)=2t^k-1-t^{3k}(1-t)
\]
is strictly increasing for \(0<t<1\): its derivative is \(t^{k-1}[2k-t^{2k}(3k-(3k+1)t)]\); the subtracted function has maximum at most \(3k/(2k+1)<2k\). Since \(J_k(0)=-1\) and \(J_k(1)=1\), its root is unique.

Because \(t>q\), the crossing equality gives \(1=H_k(p_k)<q^{-k}-1\), hence \(p_k>1-2^{-1/k}\). Since \(t<1\) and \(k\ge2\), \(S>k\), yielding \(p_k<1/(k+1)\).

**5. Two-term large-\(k\) expansion.** Put \(c=\log2\) and \(t_k=e^{-y_k/k}\). The algebraic equation becomes
\[
2e^{-y_k}-1=e^{-3y_k}(1-e^{-y_k/k}).
\]
The positive right-hand side implies \(0<y_k<c\), and it is bounded above by \(c/k\), forcing \(y_k\to c\). Expansion by the ordinary implicit-function theorem at \((y,1/k)=(c,0)\) gives
\[
y_k=c-\frac{c}{8k}+O(k^{-2}),\qquad
 t_k=\exp\!\left(-\frac c k+\frac{c}{8k^2}+O(k^{-3})\right).
\]
The equivalent exact formula obtained from \(G=0\),
\[
p_k=\frac{1-t_k}{1-t_k^{2k+1}(1-t_k)},
\]
then gives
\[
p_k=\frac c k-\frac{c(1+2c)}{8k^2}+O(k^{-3}),
\]
as claimed.

## Verification

Run `python3 CHECK.py` using Python 3's standard library. It constructs finite prefix-matching automata directly from each forbidden word and independently constructs the weighted self-overlap generating-function denominators. Across \(2\le k\le8\) and four exact rational symbol probabilities, it compares 1,848 survival-probability coefficients using exact fractions, checks 630 structural overlap and phase comparisons, and numerically checks algebraic threshold values through \(k=40\). These are reproducibility diagnostics, not a proof for the infinite parameter set. The analytic proof above establishes all parameters \(k\ge3\) and \(p\in(0,1)\).

## Relationship to prior work

Bonanno, Cristadoro and Lenci (2022), Proposition 2.4, supply the weighted-autocorrelation escape denominator. Their Remark 3.7 already exhibits the *single* pair \(001100\) and \(100001\) at \(k=2\) and reports a crossover approximately; the phenomenon at \(k=2\) is not new. Their inspected statement does not supply a unique crossover formula or an all-\(k\) phase theorem for \(0^k11 0^k\) against \(10^{2k}1\). Chandgotia, Marcus, Richey and Wu (first preprint 2024) give general symbolic-dynamical structure for one-forbidden-word systems, including their unweighted self-overlap invariants. Bóna, Maga and Richey (first preprint 4 June 2026) examine the analogous border-polynomial dependence of letter frequencies; their study motivates the equal-composition question but does not establish this biased escape-rate phase law. The present theorem's new content is the infinite parametric family \(k\ge3\), unique bias threshold, exact polynomial parameterization, and \(\log2/k\) law with sharp next correction. These conclusions are conditional only on the standard explicitly credited denominator identity.

## Limitations

This theorem concerns iid binary sources, the two precisely specified length-matched cylinder holes and their escape exponents; it does not rank other holes or prove an optimal crossover among all words. Although the computed algebraic thresholds are unique for these pairs, no claim is made of a general uniqueness theorem for arbitrary forbidden words. Priority remains provisional; general weighted-overlap techniques in earlier work could allow an alternative derivation.

## References

1. C. Bonanno, G. Cristadoro, M. Lenci, *Maximal escape rate for shifts*, Discrete and Continuous Dynamical Systems 42 (2022), 6007–6029, arXiv:2112.14248, Proposition 2.4 and Remark 3.7. https://arxiv.org/html/2112.14248v2
2. N. Chandgotia, B. Marcus, J. Richey, C. Wu, *Shifts of Finite Type Obtained by Forbidding a Single Pattern*, arXiv:2409.09024, first public 13 September 2024. https://arxiv.org/abs/2409.09024
3. M. Bóna, B. Maga, J. Richey, *Letter frequency in shifts of finite type with one forbidden word*, arXiv:2606.06655, first public 4 June 2026. https://arxiv.org/abs/2606.06655
