# Rank-one site drift and sharp parameter extremizers for Ewens triple patterns

## Finding

Let \(n\ge4\) and \(\theta>0\). Sample a permutation \(\Pi\) of \(\{1,\ldots,n\}\) with Ewens cycle-weighted law
\[
\Pr_\theta(\Pi=\pi)=\frac{\theta^{c(\pi)}}{\theta(\theta+1)\cdots(\theta+n-1)},
\]
where \(c(\pi)\) is the number of cycles. For every middle site \(2\le i\le n-1\), let \(p_{n,i}^{\theta}(\sigma)\), \(\sigma\in S_3\), be the probability that the ordered triple \((\Pi(i-1),\Pi(i),\Pi(i+1))\) has relative-order pattern \(\sigma\). Define
\[
B=\binom{n-1}{3},\quad H=\binom{n-2}{2},\quad
D=(\theta+n-1)(\theta+n-2)(\theta+n-3).
\]
The exact six probabilities are \(p_{n,i}^{\theta}(\sigma)=N_\sigma/D\), where

| \(\sigma\) | \(N_\sigma\) |
|---|---|
| \(123\) | \(B+H\theta+(n-3)\theta^2+\theta^3\) |
| \(132\) | \(B-(n-i-1)+\frac{n(n-3)}2\theta+(n-i)\theta^2\) |
| \(213\) | \(B-(i-2)+\frac{n(n-3)}2\theta+(i-1)\theta^2\) |
| \(231\) | \(B+(n-i-1)+(H+1)\theta+(i-2)\theta^2\) |
| \(312\) | \(B+(i-2)+(H+1)\theta+(n-i-1)\theta^2\) |
| \(321\) | \(B+\frac{n(n-3)}2\theta+\theta^2\) |

In pattern order \((123,132,213,231,312,321)\), the complete difference between any two local laws has rank one:
\[
\bigl(p_{n,i}^{\theta}(\sigma)-p_{n,j}^{\theta}(\sigma)\bigr)_{\sigma\in S_3}
=\frac{(i-j)(\theta^2-1)}{D}(0,-1,1,1,-1,0).
\]
Consequently their total variation distance is exactly
\[
\operatorname{TV}\bigl(p_{n,i}^{\theta},p_{n,j}^{\theta}\bigr)
=\frac{2|i-j|\,|\theta^2-1|}{D}.
\]
For fixed \(n\) and \(\theta\ne1\), the most separated sites are precisely the first and last middle sites, \(i=2\) and \(j=n-1\).

A sharp size-dependent transition governs maximization over all \(\theta>0\) and site pairs. For \(n=4\), the supremum is \(1/3\), approached only as \(\theta\downarrow0\); it is not attained for positive \(\theta\). For each \(n\ge5\), the maximum is uniquely attained by the two extreme middle sites and a finite \(\theta=\theta_n>1\), where \(\theta_n\) is the unique positive root of
\[
-\theta^4+(s_2+3)\theta^2+2(s_3+s_1)\theta+s_2=0,
\quad s_1=3n-6,\quad s_2=3n^2-12n+11,\quad s_3=(n-1)(n-2)(n-3).
\]
The extremal parameter and largest separation satisfy
\[
\frac{\theta_n}{n}\longrightarrow2,
\qquad
\max_{\theta>0,\,2\le i,j\le n-1}
\operatorname{TV}\bigl(p_{n,i}^{\theta},p_{n,j}^{\theta}\bigr)
\longrightarrow\frac8{27}
\quad\text{as }n\longrightarrow\infty.
\]

## Assumptions and scope

The law is for complete permutations with cycle weight \(\theta>0\), not an independent-coordinate model. Every site is a **consecutive triple of source positions**; the six patterns label the relative ranks of the three image values. Total variation on the finite six-pattern space uses the convention \(\frac12\sum_\sigma|p(\sigma)-q(\sigma)|\). The finite extremum concerns every positive real \(\theta\); the limiting single-cycle model at \(\theta=0\) is not included.

## Proof

**1. Partial-map identity.** Fix distinct sources \(a,b,c\) and distinct images \(u,v,w\). Denote by \(r\) the number of closed directed cycles among the three forced arrows \(a\mapsto u\), \(b\mapsto v\), \(c\mapsto w\). The Ewens partial-permutation identity gives
\[
\Pr_\theta\{\Pi(a)=u,\Pi(b)=v,\Pi(c)=w\}=\frac{\theta^r}{D}.
\]
To see the identity, remove the forced closed cycles and contract each remaining forced directed path. The remaining \(n-3\) free units form a weighted permutation of total weight \(\theta(\theta+1)\cdots(\theta+n-4)\), while the removed closed cycles contribute \(\theta^r\). Dividing by the full Ewens normalization proves the formula, including overlapping source/image labels. This is the classical partial-image identity, not a new lemma.

**2. Exhaustive cycle-configuration count.** Set \((a,b,c)=(i-1,i,i+1)\). For each pattern \(\sigma\), enumerate the \(\binom n3\) ordered output triples with that relative order; let \(r\in\{0,1,2,3\}\) be the closed-cycle count for the three arrows. Define
\[
S_m(\sigma)=\sum_{1\le u<v<w\le n}\binom{r_\sigma(u,v,w)}m,
\qquad m\in\{0,1,2,3\},
\]
where the output assigned to source position \(t\) is the \(\sigma_t\)-th smallest of \(u,v,w\). Then \(S_0(\sigma)=\binom n3\) for all \(\sigma\), and
\[
N_\sigma=\sum_{m=0}^3S_m(\sigma)(\theta-1)^m.
\]
For \(S_1\), count every possible singleton loop, two-cycle, and directed three-cycle. If a loop is imposed at source \(s\), whose image has rank \(h\in\{1,2,3\}\), its number of compatible triples is exactly
\[
\binom{s-1}{h-1}\binom{n-s}{3-h}.
\]
A two-cycle contributes according to the allowed third output: for example, the transposition \(a\leftrightarrow b\) supplies \(n-i\) triples of pattern \(213\) and \(i-2\) of pattern \(321\). The two possible directed three-cycles give patterns \(231\) and \(312\), one each. For \(S_2\), count disjoint pairs of directed cycles: either two singleton loops or a two-cycle and a disjoint loop. The latter contributes one each to patterns \(132\), \(213\) and \(321\). Three disjoint cycles are possible only for the identity triple, producing pattern \(123\). Summing these elementary cases gives the complete table:

| \(\sigma\) | \(S_1\) | \(S_2\) | \(S_3\) |
|---|---|---|---|
| \(123\) | \(\binom n2\) | \(n\) | \(1\) |
| \(132\) | \(\frac{n(n-3)}2+2(n-i)\) | \(n-i\) | \(0\) |
| \(213\) | \(\frac{n(n-3)}2+2(i-1)\) | \(i-1\) | \(0\) |
| \(231\) | \(H+2i-3\) | \(i-2\) | \(0\) |
| \(312\) | \(H+2n-2i-1\) | \(n-i-1\) | \(0\) |
| \(321\) | \(\frac{n(n-3)}2+2\) | \(1\) | \(0\) |

Substitute this table into the displayed expansion in \(\theta-1\). Direct expansion gives all six numerator polynomials in the finding. Their sum is exactly \(D\); hence they form a normalized probability distribution for every \(n\ge4\), \(\theta>0\).

**3. One-dimensional positional drift.** Only the four mixed patterns carry an \(i\)-dependent term. Subtracting their respective polynomial expressions at sites \(i,j\) gives the rank-one vector. Taking its \(\ell^1\)-norm and dividing by two yields the total-variation identity. It is strictly positive for distinct sites exactly when \(\theta\ne1\), and the maximal site separation is \(n-3\).

**4. Exact optimization and exceptional size.** Write
\[
g_n(t)=\frac{|t^2-1|}{(t+n-1)(t+n-2)(t+n-3)},\qquad t>0.
\]
On \(0<t<1\), \(g_n\) decreases strictly and has unattained limiting supremum \(1/[(n-1)(n-2)(n-3)]\). On \(t>1\), differentiation of \((t^2-1)/D(t)\) has numerator
\[
Q_n(t)=-t^4+(s_2+3)t^2+2(s_3+s_1)t+s_2.
\]
For \(n\ge4\), all \(s_1,s_2,s_3\) are positive, so Descartes' rule of signs gives exactly one positive root. Since \(Q_n(1)>0\) and \(Q_n(t)\to-\infty\), the root \(\theta_n>1\) is the unique maximizer on \(t>1\). At \(n=4\), the high-side expression simplifies to \((t-1)/[(t+2)(t+3)]<1/6\) because \((t+2)(t+3)-6(t-1)=t^2-t+12>0\); thus the smaller-parameter limit uniquely determines the global supremum.

For all \(n\ge5\), the explicit witness \(t=n\) beats the lower-side limit. Indeed the numerator after cross-multiplication is
\[
(n-1)\bigl(n^4-5n^3-3n^2+21n-12\bigr),
\]
and, putting \(m=n-5\ge0\), the second factor equals
\[
m^4+15m^3+72m^2+116m+18>0.
\]
Therefore the unique global maximizer has \(t=\theta_n>1\) for every \(n\ge5\).

Finally, divide \(Q_n(cn)\) by \(n^4\) for fixed \(c>0\). It tends to
\[
-c^4+3c^2+2c=-c(c-2)(c+1)^2.
\]
The unique positive root consequently satisfies \(\theta_n/n\to2\). In the total-variation formula, substitute \(\theta_n/n\to2\) and the extremal site gap \(n-3\): the limit is \(2\cdot4/27=8/27\). This completes the all-size classification.

## Verification

Run `python verify.py` with Python 3 and no third-party dependencies. It independently enumerates full permutations with Ewens cycle weights at several positive rational parameters through size eight, enumerates all three-arrow partial injections through size twelve, and checks the six probability polynomials, normalization, total variation identity and explicit parameter witness. This version completed **1,270 exact assertions**. Exhaustive finite checks corroborate the algebra; the all-size statements rely on the proof above, not on bounded enumeration.

## Relationship to prior work

Féray's partial-image identity and asymptotic dashed-pattern results supply a classical enumeration tool and limiting context, but do not state the present finite six-law table, the rank-one positional contrast, or its sharp parameter optimization. The Diaconis–Fulman–Holmes peak/cycle-type generating function (Corollary 3.8) and subsequent work treat **aggregated** peak counts, not the six-pattern law at individually labeled sites; the aggregate peak identity is not claimed as new here. Later studies of conjugacy-invariant permutation pattern counts concern global/asymptotic count statistics rather than this finite sitewise classification. Results on fixed-point covariance under the **uniform** permutation law concern a different tilt statistic from Ewens cycle weighting. The contributions assessed here are specifically the combined exact local six-law structure, rank-one total-variation identity and size-dependent global parameter extremum.

## Limitations

The theorem concerns consecutive three-site ordinal patterns, not longer windows, joint laws across several windows or all conjugacy-invariant measures. It does not claim the Ewens partial-image identity, peak generating functions or general asymptotic pattern limit theorems as new. The historical priority of explicit reductions from general cycle-type generating functions has not been completely resolved.

## References

- P. Diaconis, J. Fulman and S. Holmes, *Analysis of casino shelf shuffling machines*, arXiv:1107.2961, first posted July 14, 2011, https://arxiv.org/abs/1107.2961. Corollary 3.8 supplies the joint generating function for total peak count and permutation cycle type.
- V. Féray, *Asymptotic behavior of some statistics in Ewens random permutations*, arXiv:1201.2157, first posted January 10, 2012, https://arxiv.org/abs/1201.2157. Theorem on dashed patterns and Lemma 2.1 on partial image events.
- J. Fulman, G. B. Kim and S. Lee, *Central limit theorem for peaks of a random permutation in a fixed conjugacy class of \(S_n\)*, arXiv:1902.00978, first posted February 3, 2019, https://arxiv.org/abs/1902.00978. Its introduction discusses the earlier aggregate peak-cycle generating function of Diaconis, Fulman and Holmes.
- V. Dubach, *A geometric approach to conjugation-invariant random permutations*, arXiv:2402.10116, first posted February 15, 2024, https://arxiv.org/abs/2402.10116. Section 2.4 concerns global permutation pattern counts.
