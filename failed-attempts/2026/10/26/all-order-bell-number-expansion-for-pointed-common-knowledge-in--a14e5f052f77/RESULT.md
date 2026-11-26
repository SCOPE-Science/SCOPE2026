# All-order Bell-number expansion for pointed common knowledge in random S5 frames

## Finding

Fix an integer \(r\geq 2\), a truth density \(p\in(0,1)\), and a positive integer \(K\). On \([n]=\{1,\ldots,n\}\), choose \(r\) equivalence relations independently and uniformly among all \(B_n\) set partitions, and mark each world as satisfying a unary proposition \(P\) independently with probability \(p\). The distinguished world is \(1\). Let \(Q_n(p,r)\) be the probability that the epistemic formula \(CP\) (common knowledge of \(P\)) holds at world \(1\).

Define \(a_{0,r}=0\) and, for \(s\geq 1\),
\[
a_{s,r}=B_s^{r}-\sum_{j=1}^{s-1}\binom{s-1}{j-1}a_{j,r}B_{s-j}^{r}.
\]
Here \(a_{s,r}\) counts ordered \(r\)-tuples of partitions of an \(s\)-set whose equivalence-relation join has just one class. For all \(n\geq1\), there is the **exact identity**
\[
Q_n(p,r)=\sum_{s=1}^{n}\binom{n-1}{s-1}a_{s,r}p^{s}\left(\frac{B_{n-s}}{B_n}\right)^{r}.
\]
For **every fixed** \(K\geq1\), as \(n\to\infty\),
\[
Q_n(p,r)=\sum_{s=1}^{K}\binom{n-1}{s-1}a_{s,r}p^{s}\left(\frac{B_{n-s}}{B_n}\right)^{r}
+O_{r,p,K}\!\left(n^{K}\left(\frac{B_{n-K-1}}{B_n}\right)^{r}\right).
\tag{1}
\]
The formula applies once \(n>K\). In particular, because \(a_{1,r}=1\) and \(a_{2,r}=2^r-1\),
\[
Q_n(p,r)=p\left(\frac{B_{n-1}}{B_n}\right)^r
+(2^r-1)p^2(n-1)\left(\frac{B_{n-2}}{B_n}\right)^r
+O_{r,p}\!\left(n^2\left(\frac{B_{n-3}}{B_n}\right)^r\right).
\tag{2}
\]
Thus \(Q_n(p,r)\sim p(W(n)/n)^r\), where \(W\) is the positive Lambert W function. The second term is of relative order \(W(n)^r/n^{r-1}\). **Bell ratios must remain exact in (2):** replacing the leading ratio by its first-order Lambert W approximation loses the stated second-order precision.

## Assumptions and scope

The integer \(r\geq2\), the truth probability \(p\in(0,1)\), and the truncation order \(K\) are fixed independently of \(n\). Every equivalence relation is sampled independently from the **uniform** measure on labelled set partitions, not from a fixed-block-count partition ensemble. Different worlds' truth values of \(P\) are independent of one another and of the equivalence relations. No independence between knowledge events is assumed. There is no nontrivial intuitionistic information order: the underlying order is equality, so these are finite classical S5 models and also a special case of the birelational common-knowledge semantics. The result makes no assertion for varying \(r\), varying \(p\), or nonuniform partition distributions.

An equivalence-relation join is the least equivalence relation containing the union. Its class of world \(1\), written \(J(1)\), consists of all worlds reachable by a finite path of epistemic steps. Thus \(CP\) at \(1\) is exactly \(J(1)\subseteq\{v:P(v)\}\).

## Proof

**Exact component formula.** Fix a subset \(S\subseteq[n]\) of cardinality \(s\) containing \(1\). The event \(J(1)=S\) is equivalent to: each of the \(r\) partitions respects the cut \(S\mid([n]\setminus S)\), and the restrictions of their partitions to \(S\) jointly connect \(S\). The latter restrictions admit \(a_{s,r}\) ordered choices, and the independent complement restrictions admit \(B_{n-s}^{r}\) choices. Of the \(B_n^{r}\) equiprobable global tuples, exactly \(a_{s,r}B_{n-s}^{r}\) realize this event. There are \(\binom{n-1}{s-1}\) possible sets \(S\), proving
\[
\Pr(|J(1)|=s)=\binom{n-1}{s-1}a_{s,r}\left(\frac{B_{n-s}}{B_n}\right)^r.
\]
Given \(|J(1)|=s\), the chance that all \(s\) worlds satisfy \(P\) is \(p^s\), proving the exact expression for \(Q_n\). To obtain the recurrence for \(a_{s,r}\), classify all \(B_s^{r}\) ordered partition tuples according to their rooted join-component \(S\); the term with \(|S|=s\) is \(a_{s,r}\) and the other terms are the indicated sum.

**Uniformly summable bound.** Put
\[
U_s=\binom{n-1}{s-1}p^s\left(\frac{B_sB_{n-s}}{B_n}\right)^r\quad(1\le s\le n).
\]
Since \(a_{s,r}\le B_s^r\), the size-\(s\) summand in \(Q_n\) is at most \(U_s\). Write \(u_m=B_{m+1}/B_m\) for \(m\ge0\). Then for \(2\le s<n/2\),
\[
\frac{U_{s+1}}{U_s}=p\frac{n-s}{s}\left(\frac{u_s}{u_{n-s-1}}\right)^r.
\tag{3}
\]
We use two classical Bell-number estimates: \(u_m\le m+1\) (insert one labelled element into any of the existing blocks or make a singleton), and \(u_m=\frac{m}{W(m)}(1+o(1))\) as \(m\to\infty\). The latter is uniform whenever \(m\) ranges above a lower bound tending to infinity.

For \(2\le s\le n^{2/3}\), the lower bound \(u_{n-s-1}\ge c n/\log n\) and the elementary upper bound on \(u_s\) make (3) \(O_r((\log n)^r n^{-(r-1)/3})=o(1)\), uniformly. For \(n^{2/3}<s\le n/4\), the uniform Bell-ratio asymptotic and \(W(n)/W(n^{2/3})\to3/2\) give
\[
\limsup_{n\to\infty}\sup_{n^{2/3}<s\le n/4}\frac{U_{s+1}}{U_s}
\le p\frac{(3/2)^r}{3^{r-1}}\le\frac{3p}{4}<1.
\]
For \(n/4<s<n/2\), \(W(n-s-1)/W(s)=1+o(1)\) uniformly, and \(s/(n-s)\le1\). Therefore the limsup of (3) over this interval is at most \(p<1\). Consequently a constant \(\delta\in(0,1)\), depending on \(r,p\), satisfies \(U_{s+1}\le\delta U_s\) for every \(2\le s<n/2\) once \(n\) is large. Thus for fixed \(K\),
\[
\sum_{K<s\le n/2}U_s=O_{r,p,K}(U_{K+1}).
\tag{4}
\]

**Large-component tail.** For each integer \(1\le t<n/2\), symmetry of the Bell products gives the exact relation
\[
\frac{U_{n-t}}{U_t}=\frac{n-t}{t}\,p^{n-2t}.
\tag{5}
\]
For \(1\le t\le n/3\), (5) contributes at most \(n p^{n/3}\sum_{t\le n/3}U_t=O(np^{n/3}U_1)\): the ratio \(U_2/U_1\to0\), and all subsequent ratios up to half-size are bounded by \(\delta\). For \(n/3<t<n/2\), (5) and the geometric bound imply a total \(O(n^2\delta^{n/3}U_1)\). The case \(s=n\) contributes \(U_n=p^n\). Each of these bounds is exponentially small compared with \(U_{K+1}\), which for fixed \(K\) is a power of \(n\) times powers of \(W(n)\). Combining with (4) yields
\[
\sum_{s>K}\binom{n-1}{s-1}a_{s,r}p^s\left(\frac{B_{n-s}}{B_n}\right)^r=O_{r,p,K}(U_{K+1}).
\]
For fixed \(K\), the definition of \(U_{K+1}\) gives
\[
U_{K+1}=O_{r,p,K}\!\left(n^K\left(\frac{B_{n-K-1}}{B_n}\right)^r\right),
\]
which proves (1). The values \(B_1=1\), \(B_2=2\), and \(a_{2,r}=2^r-1\) give (2). Lastly \(B_{n-j}/B_n\sim(W(n)/n)^j\) for each fixed \(j\), so the leading term and the order of the correction follow.

## Verification

A standalone exact-rational checker accompanies the proof. It enumerates every labelled set partition and every ordered pair of partitions for sizes \(1\) through \(6\), and ordered triples through size \(4\). It independently computes each root component with a union–find procedure and compares its histogram with the recurrence-derived formula. For density \(p=1/2\), both methods give the exact probabilities \(5/16\) at \((n,r)=(2,2)\), \(43/200\) at \((3,2)\), and \(9/32\) at \((2,3)\). These finite checks validate the enumeration and normalization but do not establish the asymptotic statement; the proof above supplies that step.

To reproduce, run `python checker.py` using Python 3 and no external packages.

## Relationship to prior work

Zenger (2026) studies intuitionistic common-knowledge logic, including the S5 case and the semantics \(C\varphi\) through the reflexive–transitive closure of the union of accessibility relations. The present work uses the classical equality-order subcase and asks a quantitative question about random valuations and frames rather than logic completeness, proof systems, or complexity.

Pittel (2000), Theorem 5, establishes that the join of independently sampled uniform set partitions is one block with probability tending to one, with an explicit upper bound on failure. That result concerns global connectivity and does **not** determine the probability that a fixed randomly marked proposition is common knowledge at a specified world, nor the local all-order coefficients and tail remainder. In particular, global-connectivity high probability does not by itself give the polynomially small probability studied here.

Collevecchio and LiCalzi (2012) analyze whether **some** nontrivial commonly known event exists for independently sampled information partitions and study a different random-allocation model. Their uniform-partition result is a zero limit for existence of such an event, deduced from Pittel. Here the event is fixed in advance by an independent Bernoulli valuation, the world is pointed, and the output is an exact finite identity plus an all-fixed-order expansion. The counting recurrence is the standard connected-component decomposition; its use is acknowledged, not represented as a new general enumerative principle.

## Limitations

The expansion assumes fixed \(r\), fixed \(p\in(0,1)\), and fixed truncation order \(K\). It does not cover the sparse-marking regime where \(p\to0\), the near-certain-marking regime where \(p\to1\), or arbitrary dependence among agents' partitions. The estimates are asymptotic and do not supply optimal uniform constants for small \(n\). Previously unknown equivalent formulations may exist in the wider literature on weighted decomposable combinatorial classes or random common knowledge. No independent verification of originality or correctness has been performed.

## References

1. Lukas Zenger, *Intuitionistic Common Knowledge*, first arXiv version dated 2026-05-01, arXiv:2605.00523. https://arxiv.org/html/2605.00523
2. Boris Pittel, *Where the Typical Set Partitions Meet and Join*, Electronic Journal of Combinatorics 7 (2000), R5, Theorem 5. https://doi.org/10.37236/1483
3. Andrea Collevecchio and Marco LiCalzi, *The Probability of Nontrivial Common Knowledge*, March 2012 version. https://www.unive.it/web/fileadmin/user_upload/dipartimenti/DMAN/pubblicazioni_scientifiche/working_papers/2011/2011wp6.pdf
