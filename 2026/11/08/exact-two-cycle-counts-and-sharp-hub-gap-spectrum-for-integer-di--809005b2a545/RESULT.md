# Exact two-cycle counts and sharp hub-gap spectrum for integer diffusion on \(K_{2,n}\)

## Finding

For integer \(n\ge1\), let \(G=K_{2,n}\) have two individually labelled hubs \(h_1,h_2\) and \(n\) individually labelled leaves. Under synchronous integer diffusion, each vertex sends one chip to every neighbor with a smaller label and receives one from every neighbor with a larger label. Identify configurations differing by a common additive integer. Let \(N_n\) count configurations *already periodic*, including the constant fixed configuration. Then the explicit finite multinomial formulas below determine \(N_n\) and the finer count \(B_d(n)\) with normalized hub gap \(c(h_2)-c(h_1)=d\ge0\):

\[
N_n=B_0(n)+2\sum_{d=1}^{2n+2}B_d(n).
\]

For \(n\ge3\), the positive hub-gap spectrum is exactly \(\{1,2,\ldots,2n-2\}\). In particular,
\[
B_{2n-2}(n)=1,\qquad B_d(n)=0\quad(d>2n-2).
\]
The unique positive-gap extremizer has hub labels \(0,2n-2\) and all \(n\) leaves labelled \(n-1\); reflecting the hubs gives the unique negative-gap extremizer. All initially periodic configurations have period one or two, the constant configuration is the unique fixed point modulo translation, and the number of distinct primitive-two temporal orbits is \((N_n-1)/2\). The initial values for \(n=1,\ldots,10\) are
\[
9,\ 47,\ 299,\ 2915,\ 36455,\ 554933,\ 9943085,\ 204932979,\ 4776325607,\ 124216024753.
\]
The sharp-gap assertion is stated for \(n\ge3\); the small cases have positive supports \(\{1\}\) for \(n=1\) and \(\{1,2\}\) for \(n=2\), with \(B_1(1)=2\) and \(B_2(2)=3\).

## Assumptions and scope

The graph is simple, loopless, finite and labelled. Vertex charges are arbitrary integers, not restricted to nonnegative integers. Fix the unique translation representative with charge \(c(h_1)=0\), and write \(d=c(h_2)\). For a configuration \(c\), define
\[
\sigma_c(v)=\sum_{w\sim v}\operatorname{sgn}(c(v)-c(w)),\qquad F(c)(v)=c(v)-\sigma_c(v),
\]
where \(\operatorname{sgn}(0)=0\). A configuration is initially periodic if \(F^k(c)=c\) for some integer \(k\ge1\). The formulas below describe exactly those states with \(F^2(c)=c\); the cited general periodicity theorem also excludes higher initial periods.

Write \(0^0=1\), \([P]\in\{0,1\}\) for the indicator of a condition, and \(t_+=\max\{t,0\}\). For \(d\ge1\) and \(\alpha,\beta,\gamma,\delta,\varepsilon\ge0\) summing to \(n\), put
\[
U=\gamma+\delta+\varepsilon-\alpha,\qquad V=d+\varepsilon-\alpha-\beta-\gamma.
\]
Define five nonnegative integers
\[
\begin{aligned}
L&=(1-\max\{U,V\})_+,\\
E_0&=[U=1\text{ and }V\le0],\\
I&=(\min\{d-1,U-1\}-\max\{1,V+1\}+1)_+,\\
E_d&=[U\ge d\text{ and }V=d-1],\\
R&=(1+\min\{U,V\}-d)_+.
\end{aligned}
\]
Then
\[
B_d(n)=\!\sum_{\alpha+\beta+\gamma+\delta+\varepsilon=n}
\binom{n}{\alpha,\beta,\gamma,\delta,\varepsilon}
L^\alpha E_0^\beta I^\gamma E_d^\delta R^\varepsilon.
\tag{1}
\]
For the zero gap, let \(\alpha+\beta+\varepsilon=n\), and put \(U=\varepsilon-\alpha\). Then
\[
B_0(n)=\sum_{\alpha+\beta+\varepsilon=n}
\binom{n}{\alpha,\beta,\varepsilon}
(1-U)_+^\alpha [U=0]^\beta (1+U)_+^\varepsilon.
\tag{2}
\]
Here the notation \((1-U)_+^\alpha\) means the \(\alpha\)-th power of the nonnegative integer \((1-U)_+\), including the stated \(0^0\) convention; no negative powers occur.

## Proof

**1. An exact edge-reversal criterion.** Give every edge an arbitrary orientation and form its incidence operator \(D\). Let \(s(c)\) be the oriented edge-sign vector, so \(F(c)=c-Ds(c)\). If \(F^2(c)=c\) and \(c'=F(c)\), then \(D(s(c)+s(c'))=0\). Pair this identity with \(c+c'\):
\[
0=\sum_{uv\in E(G)}(s_{uv}(c)+s_{uv}(c'))\big((c_u+c'_u)-(c_v+c'_v)\big).
\]
Each summand is nonnegative. If the sum of the two edge signs is nonzero, those signs agree or one is zero; hence the corresponding summand is *strictly positive*. Therefore every summand vanishes and \(s(c')=-s(c)\) on each edge. Conversely, reversing every edge sign makes \(F^2(c)=c\), since the second update cancels the first. Thus strict edge differences must reverse strictly, and initial ties must remain ties. This is the usual edge-reversal characterization, reproved here for clarity; it is not a priority claim.

**2. A finite exhaustive range.** Every hub has degree \(n\) and every leaf has degree two. If a cross-edge initially has nonzero integer difference \(k\), reversing its sign requires changing the difference by at least \(|k|+1\), whereas a single update can change it by at most \(n+2\). Thus each initial cross-edge difference has absolute value at most \(n+1\). This is also true when the difference is zero. With \(c(h_1)=0\), every leaf label belongs to \([-n-1,n+1]\), and the second hub label belongs to \([-2(n+1),2(n+1)]\). Therefore all sums and direct checks have a rigorously exhaustive finite domain.

**3. The five bands when \(d>0\).** Partition the \(n\) leaves by their labels into \(y<0\), \(y=0\), \(0<y<d\), \(y=d\), and \(y>d\), with respective counts \(\alpha,\beta,\gamma,\delta,\varepsilon\). The two hub charges after one update are precisely \(U\) and \(V\) as above. A leaf updates to \(y+2,y+1,y,y-1,y-2\) in the five respective bands. Strict reversal or tie preservation on *both* incident edges yields the following allowed leaf labels:

- \(y\in[\max\{U,V\}-1,-1]\) in the lower band;
- \(y=0\) only when \(U=1,V\le0\);
- \(y\in[\max\{1,V+1\},\min\{d-1,U-1\}]\) in the interior band;
- \(y=d\) only when \(U\ge d,V=d-1\);
- \(y\in[d+1,\min\{U,V\}+1]\) in the upper band.

The five possible numbers of integers in these bands are exactly \(L,E_0,I,E_d,R\). Given the band populations, the labels of individual leaves are independent within these intervals. Assigning the five types to labelled leaves gives the multinomial factor, proving (1). The hub update depends only on the band populations, so there is no omitted global constraint.

**4. The zero-gap case.** If both hubs initially have label zero, both update to \(U=\varepsilon-\alpha\), where \(\alpha,\beta,\varepsilon\) count negative, zero, and positive leaves. A negative leaf updates to \(y+2\), a zero leaf stays zero, and a positive leaf updates to \(y-2\). Edge reversal permits respectively \((1-U)_+\) negative values, a zero value exactly when \(U=0\), and \((1+U)_+\) positive values. This gives (2). Swapping the two labelled hubs bijects positive and negative gap configurations, which proves the formula for \(N_n\).

**5. Sharp hub-gap spectrum.** Assume \(n\ge3,d>0\) and that a two-cycle exists. When \(\gamma>0\), an interior leaf stays at \(y\) while its two hub inequalities strictly reverse, so \(U\ge y+1>V+1\). Thus \(U-V\ge2\). Because \(U-V=2\gamma+\beta+\delta-d\le2n-d\), necessarily \(d\le2n-2\). When \(\gamma=0\) but \(\beta+\delta>0\), a leaf tied to one hub forces \(U>V\), so \(d\le\beta+\delta-1\le n-1\). When \(\beta=\gamma=\delta=0\), all leaves are outside the hub interval and \(V=U+d\). Lower and upper leaves cannot coexist: lower leaves require \(V\le0\), and upper leaves require \(U\ge d\). If all leaves are below zero, then \(U=-n,V=d-n\) and reversal requires \(d\le n\); the all-above case likewise requires \(d\le n\). Thus \(d\le2n-2\) always.

For \(d=1\), choose all leaves equal to \(-1\). For every \(2\le d\le2n-2\), set all leaves equal to any integer \(y\) satisfying
\[
\max\{1,d-n+1\}\le y\le\min\{d-1,n-1\};
\]
the interval is nonempty, and the two hub updates are \(U=n,V=d-n\), so every incident edge strictly reverses. This proves that all the claimed gaps occur. At \(d=2n-2\), the interior-leaf inequality is sharp, forcing \(\gamma=n\). The allowed interior interval consists only of \(y=n-1\), proving the unique endpoint configuration and \(B_{2n-2}(n)=1\).

**6. Fixed points and temporal orbits.** If \(F(c)=c\), then \(Ds(c)=0\). Pairing with \(c\) yields \(0=\sum_{uv\in E}|c_u-c_v|\), so every connected component is constant; here \(G\) is connected. Consequently exactly one fixed translation class exists. Since every initially periodic state satisfies \(F^2(c)=c\) by the general theorem on diffusion, the other \(N_n-1\) states form disjoint pairs. Two phases of a nontrivial cycle cannot be translates of each other: diffusion conserves total charge, whereas a nonzero common translation changes that total by \(n+2\) times the translation amount. Thus the same pairing holds for translation classes, proving the orbit count.

## Verification

The standalone `count_formula.py` evaluates (1)–(2) using exact integers for \(1\le n\le10\), including the full signed-gap support and endpoint multiplicities. Independently, `direct_check.cpp` exhausts every normalized configuration in the proven range for \(1\le n\le5\), applies the original vertex rule twice, and compares the counts by hub gap. The latter independently examines 9,602,861 configurations. Its totals \(9,47,299,2915,36455\), zero-gap counts \(5,21,135,1269,15603\), and complete positive-gap profiles agree with the formula output. The attached log files contain the exact outputs. Enumeration verifies finite instances only; the proof above establishes the result for all \(n\).

## Relationship to prior work

Duffy, Lidbetter, Messinger and Nowakowski introduced the diffusion game and proved eventual periodicity for complete bipartite graphs, with edge-reversal conditions for two-cycles. Long and Narayanan established eventual period at most two for arbitrary finite graphs. These theorems are used as background, not claimed as new. Previously available recurrent-state counts for complete graphs, cycles and double stars do not imply the present all-\(n\) labelled \(K_{2,n}\) census or its sharp two-hub gap spectrum. The case \(n=2\) is the previously treated four-cycle and is included only as a consistency check; the new parameter range is \(n\ge3\). The core count is not a generic graph reparametrization: the two nonadjacent hubs couple five occupancy classes through two distinct update values, leading to the displayed multinomial sum and sharp gap law.

## Limitations

The formula counts initially periodic translation classes, not all eventual basins, transient times, or configurations at a fixed total chip mass. It is an exact finite sum rather than a short elementary closed form or an asymptotic expansion. No new claim is made for the generic edge-sign reversal condition or the eventual period-one-or-two theorem. Literature and indexed-result comparisons cannot exclude every unindexed historical enumeration; no independent external audit has been performed.

## References

1. C. Duffy, T. F. Lidbetter, M. E. Messinger and R. J. Nowakowski, *A Variation on Chip-Firing: the Diffusion Game*, arXiv:1609.05792, first public version 2016-09-19; particularly Sections 2.3 and 3.1. https://arxiv.org/abs/1609.05792 and https://arxiv.org/html/1609.05792v5 .
2. J. Long and B. Narayanan, *Diffusion on Graphs Is Eventually Periodic*, arXiv:1704.04295, first public version 2017-04-13; particularly Theorem 1.1 and the proof. https://ar5iv.labs.arxiv.org/html/1704.04295 .
