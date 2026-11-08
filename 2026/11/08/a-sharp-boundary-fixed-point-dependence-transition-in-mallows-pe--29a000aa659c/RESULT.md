# A sharp boundary fixed-point dependence transition in Mallows permutations

## Finding

Let \(\Pi_n\) follow the Kendall-inversion Mallows law with \(n\ge3\) and \(q>0\), and let \(I_j=\mathbf 1\{\Pi_n(j)=j\}\). Define \([m]_q=1+q+\cdots+q^{m-1}\). Then
\[
\operatorname{Cov}(I_1,I_2)=\frac{q+q^2-q^n}{[n]_q^2[n-1]_q},\qquad
\operatorname{Cov}(I_1,I_n)=\frac{q^{n-1}}{[n]_q^2[n-1]_q}>0.
\]
Thus neighboring fixed points at the left boundary are positively correlated for \(0<q<r_n\), independent at \(q=r_n\), and negatively correlated for \(q>r_n\), where \(r_n>1\) is the unique solution of \(r_n^{n-1}=1+r_n\). In contrast, opposite boundary fixed points are positively correlated for every \(q>0\). The sequence \(r_n\) strictly decreases to \(1\) and satisfies
\[
n\log r_n=\log2+\frac{3\log2}{2n}+O(n^{-2}).
\]
In the critical Mallows scaling \(q=e^{\beta/n}\), writing \(L(\beta)=(e^\beta-1)/\beta\) for \(\beta\ne0\) and \(L(0)=1\),
\[
\lim_{n\to\infty}n^3\operatorname{Cov}(I_1,I_2)
=\frac{2-e^\beta}{L(\beta)^3},\qquad
\lim_{n\to\infty}n^3\operatorname{Cov}(I_1,I_n)
=\frac{e^\beta}{L(\beta)^3}.
\]
The covariance sign changes at the sharp critical value \(\beta=\log2\). More precisely, with \(q=\exp((\log2+t/n)/n)\) for fixed real \(t\),
\[
\lim_{n\to\infty}n^4\operatorname{Cov}(I_1,I_2)
=\frac{3\log2-2t}{L(\log2)^3}.
\]
The smallest permutation size permitting negative fixed-point covariance is \(3\): at size \(2\), the two indicators coincide and have covariance \(q/(1+q)^2>0\).

## Assumptions and scope

The sample space is the symmetric group \(S_n\) of permutations of \(\{1,\ldots,n\}\), with \(\Pr(\Pi_n=\pi)=q^{\operatorname{inv}(\pi)}/Z_n(q)\), \(Z_n(q)=\prod_{k=1}^{n}[k]_q\), and \(\operatorname{inv}(\pi)=\#\{(i,j):i<j,\pi(i)>\pi(j)\}\). No asymptotic theorem is needed for the exact covariance identities. The limiting assertions hold for every fixed \(\beta,t\in\mathbb R\), with the indicated \(q\) depending on \(n\). Throughout, \(n\ge3\) except in the explicitly stated size-two comparison.

## Proof

By the standard inversion enumerator, \(Z_n=\prod_{k=1}^n[k]_q\). If \(\Pi_n(1)=1\), deleting the first entry leaves an arbitrary \(S_{n-1}\) permutation without changing inversion count. The same holds for \(\Pi_n(n)=n\). If both the first and second positions are fixed, or both first and last are fixed, deleting the fixed entries leaves an arbitrary \(S_{n-2}\) permutation. Consequently,
\[
\Pr(I_1=1)=\Pr(I_n=1)=\frac1{[n]_q},\qquad
\Pr(I_1I_2=1)=\Pr(I_1I_n=1)=\frac1{[n]_q[n-1]_q}.
\]
To calculate the middle marginal, impose \(\Pi_n(2)=2\). If the first entry is \(1\), the remaining inversion weight is \(Z_{n-2}\). If instead its value is \(k\in\{3,\ldots,n\}\), the first entry makes \(k-1\) inversions and the second makes one additional inversion with the still-unplaced value \(1\); the remaining \(n-2\) entries contribute \(Z_{n-2}\). Thus
\[
\Pr(I_2=1)=\frac{1+\sum_{k=3}^n q^k}{[n]_q[n-1]_q}.
\]
Subtracting products of these marginals from the two joint probabilities gives
\[
\operatorname{Cov}(I_1,I_2)
=\frac{[n]_q-1-\sum_{k=3}^n q^k}{[n]_q^2[n-1]_q}
=\frac{q+q^2-q^n}{[n]_q^2[n-1]_q},
\]
and
\[
\operatorname{Cov}(I_1,I_n)
=\frac{[n]_q-[n-1]_q}{[n]_q^2[n-1]_q}
=\frac{q^{n-1}}{[n]_q^2[n-1]_q}.
\]
For \(n\ge3\), \(q^n>q+q^2\) is equivalent to \(q^{n-1}>1+q\). The function \(q\mapsto q^{n-1}/(1+q)\) increases strictly on \((0,\infty)\), is below one at \(q=1\), and tends to infinity. Hence there is exactly one sign-change root \(r_n>1\). At that root, \(r_n^{n}>r_n^{n-1}=1+r_n\), so the root for \(n+1\) is smaller. For any fixed \(q>1\), \(q^{n-1}>1+q\) eventually, implying \(r_n\downarrow1\).

Put \(h_n=\log r_n\). Taking logarithms yields \((n-1)h_n=\log(1+e^{h_n})\). Since \(h_n\to0\), use \(\log(1+e^h)=\log2+h/2+O(h^2)\) to obtain \((n-3/2)h_n=\log2+O(h_n^2)\), and therefore the asserted \(n\log r_n\) expansion. For fixed \(\beta\), \([n]_{e^{\beta/n}}/n\to L(\beta)\) and \([n-1]_{e^{\beta/n}}/n\to L(\beta)\) by Riemann sums. The covariance numerators tend respectively to \(2-e^\beta\) and \(e^\beta\), proving the cubic-scaled limits. Finally, with \(\beta_n=\log2+t/n\), expand \(e^{\beta_n/n}+e^{2\beta_n/n}-e^{\beta_n}=(3\log2-2t)/n+O(n^{-2})\); the fourth-power limit follows. The size-two case is immediate because both fixed-point indicators are equal.

## Verification

The included standalone `verify.py` enumerates all permutations for sizes \(3\) through \(7\) at seven rational Mallows parameters each, computing weights as exact fractions and comparing the five marginals/joints and two covariances with their claimed expressions. It also numerically checks the unique roots and asymptotic scaling. The exact assertions are finite cross-checks; the proof above establishes every \(n\ge3\) and \(q>0\).

To reproduce: run `python3 verify.py` with a standard Python 3 interpreter from the same directory. No third-party packages are required.

## Relationship to prior work

The Mallows distribution, its inversion partition function, and its use in random stable matching are classical; Angel, Holroyd, Hutchcroft and Levy [1] give the stable-matching interpretation. He, Müller and Verstraaten [2] establish fixed-parameter cycle-count limit laws and distinguish the regimes \(q<1\) and \(q>1\). Johnson, Leader and Long [3] prove correlation inequalities for permutation up-sets under Mallows-type measures; individual position-fixed events are not strong Bruhat up-sets, and that theory does not give the signed formulas here. Mukherjee [4] derives first-order fixed-point and cycle-count limits in a scaling near uniformity; those do not determine this third-order boundary covariance or its fourth-order crossover. The precise new claim is the exact two-pair covariance comparison, its finite-size sign threshold, and the critical scaling, not the general Mallows measure or its first-order limit behavior.

## Limitations

This result concerns only the two specified pairs of fixed-point indicators and does not classify all positional fixed-point correlations. It makes no assertion about independent validation or a comprehensive historical priority guarantee. The critical asymptotic statements concern bounded fixed scaling parameters and do not address arbitrary varying parameter sequences.

## References

[1] O. Angel, A. E. Holroyd, T. Hutchcroft and A. Levy, *Mallows permutations as stable matchings*, first publicly available 2018-02-20, https://arxiv.org/abs/1802.07142.

[2] J. He, T. Müller and T. W. Verstraaten, *Cycles in Mallows random permutations*, first publicly available 2022-01-27, https://arxiv.org/abs/2201.11610.

[3] J. R. Johnson, I. Leader and E. Long, *Correlation for permutations*, first publicly available 2019-09-09, https://arxiv.org/abs/1909.03770.

[4] S. Mukherjee, *Fixed points and cycle structure of random permutations*, first publicly available 2015-09-15, https://arxiv.org/abs/1509.04552.
