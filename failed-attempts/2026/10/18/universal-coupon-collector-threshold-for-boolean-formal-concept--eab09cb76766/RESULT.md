# Universal coupon-collector threshold for Boolean formal-concept lattices

## Finding
Let \(r\geq 1\) labeled objects and \(m\geq 0\) labeled attributes form a formal context whose \(rm\) incidences are independent Bernoulli variables with success probability \(p\in(0,1)\). Write \(N\) for the number of formal concepts and \(t=p^{r-1}(1-p)\). Then
\[
\Pr\{N=2^r\}=\sum_{j=0}^r(-1)^j\binom rj(1-jt)^m.
\]
In the regime \(r\to\infty\), allow the incidence probability \(p=p_r\) to vary arbitrarily in \((0,1)\), and put \(t_r=p_r^{r-1}(1-p_r)\). If the integer attribute count \(m_r\) satisfies \(m_rt_r-\log r\to c\in\mathbb R\), the number of missing distinct coatom columns converges in distribution to \(\mathrm{Poisson}(e^{-c})\); in particular,
\[
\Pr\{N=2^r\}\longrightarrow \exp(-e^{-c}).
\]
If \(m_rt_r-\log r\to+\infty\), the probability tends to one; if it tends to \(-\infty\), it tends to zero. These assertions require no uniform lower/upper bound on \(p_r\).

## Assumptions and scope
A formal context consists of disjoint finite sets \(G,M\) and an incidence relation \(I\subseteq G\times M\). For \(B\subseteq M\), its extent is \(B'=\{g\in G: (g,a)\in I\text{ for every }a\in B\}\), including \(\varnothing'=G\). An extent is any such intersection of columns; extents are in bijection with formal concepts. Thus \(N\le 2^r\), where \(|G|=r\). Empty attribute families are permitted. There is no assumption that the incidence matrix has distinct rows or columns.

## Proof
For each object \(i\in G\), call an attribute a *coatom witness* for \(i\) if its set of incident objects is exactly \(G\setminus\{i\}\). The concept extents comprise every subset of \(G\) if and only if every \(i\) has a coatom witness. Indeed, if every witness exists, any \(S\subseteq G\) is the intersection of the witness columns for \(i\notin S\), with the empty intersection equal to \(G\). Conversely, if \(G\setminus\{i\}\) is an extent, it is an intersection of columns containing all objects other than \(i\), and at least one chosen column excludes \(i\); such a column must be exactly \(G\setminus\{i\}\). This proves necessity, including the cases \(r=1\) and \(m=0\).

A specified column is the coatom witness for a specified \(i\) with probability \(t=p^{r-1}(1-p)\). These \(r\) types are pairwise disjoint. For any \(j\) specified types, the probability all are absent from \(m\) independent columns is \((1-jt)^m\). Inclusion–exclusion yields the stated exact formula. Let \(U\) be the number of absent coatom types. Its factorial moments are
\[
\mathbb E(U)_k=(r)_k(1-kt)^m,\quad 0\le k\le r,
\]
where \((r)_k=r(r-1)\cdots(r-k+1)\).

Because the types are disjoint, \(0<t_r\le 1/r\). In the critical window \(m_rt_r=\log r+c+o(1)\), one has \(m_rt_r^2\le (\log r+O(1))/r\to0\). For every fixed positive integer \(k\),
\[
(r)_k(1-kt_r)^{m_r}=\exp(-kc+o(1)).
\]
These are the factorial moments of \(\mathrm{Poisson}(e^{-c})\). The factorial-moment convergence theorem (or inclusion–exclusion with Bonferroni truncation) gives \(U\Rightarrow\mathrm{Poisson}(e^{-c})\), and hence \(\Pr(U=0)\to\exp(-e^{-c})\).

Above the window, \(\mathbb E U=r(1-t_r)^{m_r}\le r e^{-m_rt_r}\to0\), so Markov's inequality gives \(\Pr(U>0)\to0\). Below the window, \(m_rt_r\le\log r\) eventually and \(m_rt_r^2=o(1)\), hence \(\mathbb E U=r(1-t_r)^{m_r}\to\infty\). Missing-type indicators have nonpositive covariance because \((1-2t_r)^{m_r}\le(1-t_r)^{2m_r}\), so \(\mathrm{Var}(U)\le\mathbb E U\). Chebyshev's inequality yields \(\Pr(U=0)\le1/\mathbb E U\to0\).

## Verification
The accompanying `verify.py` independently enumerates all incidence matrices in small dimensions, computes extents from intersections of selected columns, and compares their maximum-size counts to the exact inclusion–exclusion integers. It additionally checks numerical evaluations of the critical-window probability. The asymptotic theorem is proved by the factorial-moment and variance arguments above, not by these finite computations.

## Relationship to prior work
Formal concept extents as fixed points of the two-sorted Galois connection, and their modal presentation, are developed by Howlader and Liau (2023). The random-incidence model and expected concept counts are treated by Sakurai (2021). The relation between contranominal scales and maximal concept lattices is classical; a 2020 null-model study discusses their frequency. The contribution here is the precise coatom-witness criterion together with the finite inclusion–exclusion law and a universal, incidence-probability-independent Poisson critical window for *maximal* Boolean concept lattices. It is not a new definition of formal concepts, contranominal scales, or coupon-collector methods.

## Limitations
The result addresses saturation \(N=2^r\), not the full distribution or typical growth of \(N\). Attribute incidences must be independent and homogeneous within each \(r\), though \(p_r\) may vary with \(r\). This is an internally reviewed mathematical result; an independent external audit has not been performed. Equivalent occupancy formulas may appear in specialized formal-concept or random-incidence literature that was not fully searchable.

## References
- P. Howlader and C.-J. Liau, *Two-sorted Modal Logic for Formal and Rough Concepts*, arXiv:2309.04115, first submitted 2023-09-08, Sections 1–3. https://arxiv.org/html/2309.04115v1
- T. Sakurai, *On Formal Concepts of Random Formal Contexts*, arXiv:2101.11023, first submitted 2021-01-26, Sections 2–5. https://arxiv.org/pdf/2101.11023
- F. Dürrschnabel et al., *Null Models for Formal Contexts*, Information 11 (2020), 135, doi:10.3390/info11030135. https://doi.org/10.3390/info11030135
- A. Albano and B. Chornomaz, *Why concept lattices are large: extremal theory for generators, concepts, and VC-dimension*, International Journal of General Systems 46 (2017), 440–457, doi:10.1080/03081079.2017.1354798.
