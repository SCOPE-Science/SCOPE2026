# Optimal singleton rainbow deployments on crown graphs: a sharp counting transition

## Finding
Let \(n,k\) be integers with \(n\ge2\) and \(k\ge2\). The labelled **crown graph** \(\mathrm{Cr}_n\) has vertices \(a_1,\dots,a_n,b_1,\dots,b_n\), with \(a_i\) adjacent to \(b_j\) exactly when \(i\ne j\). A singleton rainbow \(k\)-dominating function assigns each vertex one of \(0,1,\dots,k\), where \(0\) means uncolored and every vertex labelled \(0\) must have neighbors of *all* the named colors \(1,\dots,k\). Its weight is the number of nonzero labels. Let \(\widetilde\gamma_k(\mathrm{Cr}_n)\) be the minimum weight and \(N_{n,k}\) the number of labelled minimum-weight functions (with colors distinguished).

**Theorem.** The minimum weight and its exact multiplicity are
\[
\widetilde\gamma_k(\mathrm{Cr}_n)=2\min\{n,k\},
\]
\[
N_{n,k}=\begin{cases}
k^{2n},&2\le n\le k,\\
\displaystyle\binom nk(k!)^2+2\binom k{2k-n}\frac{n!\,k^{2k-n}}{2^{n-k}},&k<n\le2k,\\
\displaystyle\binom nk(k!)^2,&n>2k.
\end{cases}
\]
All optimal functions have the following **unique structural classification**:

* If \(n\le k\), every vertex is colored, with arbitrary named colors.
* If \(n>k\), a **matched-support configuration** chooses exactly \(k\) indices \(T\subseteq\{1,\dots,n\}\), colors \(a_i,b_i\) precisely for \(i\in T\), and uses each of the \(k\) colors exactly once on each side (the two permutations are independent).
* Additionally, if \(k<n\le2k\), a **one-side-full configuration** colors all \(n\) vertices on one side, assigns exactly \(s=2k-n\) singleton-occurrence colors and \(k-s\) double-occurrence colors on that side, and colors exactly the \(s\) opposite vertices aligned with the singleton occurrences, arbitrarily with the \(k\) named colors. All remaining vertices are uncolored. The orientation of the full side is chosen in two ways.

For \(n>2k\), matched-support configurations are the *only* minima. In contrast, the complete bipartite graph \(K_{n,n}\) has \(\binom nk^2(k!)^2\) minimum singleton rainbow \(k\)-dominating functions in this range. Thus removing a perfect matching retains the optimum weight \(2k\) but reduces the exact number of optimal labelled deployments by the factor \(\binom nk\).

## Assumptions and scope
Graphs are finite, simple and undirected; the crown includes the disconnected case \(n=2\). The labels \(1,\ldots,k\) are **singletons**, never arbitrary color subsets, and no color must be used when all vertices are colored. Uncolored vertices alone must see all \(k\) colors in their **open** neighborhoods. The count distinguishes every vertex, side, and named color. A multiple-label (ordinary \(k\)-rainbow) domination model is different.

## Proof
Let \(A=\{a_1,\dots,a_n\}\), \(B=\{b_1,\dots,b_n\}\), and write \(x\) and \(y\) for the numbers of colored vertices in \(A\) and \(B\). The crucial observation is that an uncolored \(a_i\) sees every required color if and only if, after deleting the label at \(b_i\), the \(n-1\) labels on \(B\) still contain all \(k\) colors. The symmetric condition holds for each uncolored \(b_i\). In particular, when \(A\) has a blank, every color occurs on \(B\), and any color occurring at exactly one vertex \(b_j\) forces \(a_j\) to be colored.

If \(n\le k\), each vertex has degree \(n-1<k\), so no vertex may be uncolored. Therefore the unique support is all \(2n\) vertices, with \(k^{2n}\) assignments.

Now assume \(n>k\). If both \(A\) and \(B\) contain uncolored vertices, each side must carry all \(k\) colors and so \(x+y\ge2k\). For equality \(x=y=k\), each color appears exactly once on each side. Let \(T_A,T_B\) be the respective colored index sets. If \(i\in T_B\setminus T_A\), then \(a_i\) is blank but cannot see the unique color of \(b_i\), a contradiction. Thus \(T_B\subseteq T_A\); symmetrically \(T_A\subseteq T_B\). Hence \(T_A=T_B\), and equality configurations are precisely the matched-support family. Conversely every such family works because a blank index lies outside the shared support. Its count is \(\binom nk(k!)^2\).

Suppose next that \(B\) is fully colored and \(A\) has a blank. Let \(q\) be the number of colors occurring **exactly once** on \(B\). All \(k\) colors occur there, since an uncolored vertex of \(A\) must see them all. Every singleton-occurrence index of \(B\) must be colored in \(A\), so \(x\ge q\). Each other color occurs at least twice, giving
\[
n\ge q+2(k-q)=2k-q,\qquad q\ge\max\{0,2k-n\}.
\]
Thus the weight is \(n+x\ge n+\max\{0,2k-n\}\ge2k\). Equality can hold only when \(n\le2k\), with \(q=x=s=2k-n\). There is then no slack in either inequality: exactly \(s\) colors appear once on \(B\), each other color exactly twice; and the colored vertices in \(A\) are exactly those aligned with the singleton occurrences. Their colors are unconstrained, since every vertex on \(B\) is already colored. Conversely all such assignments are valid. Their number for a fixed orientation is
\[
\binom{k}{s}\frac{n!}{2^{k-s}}\,k^s
=\binom{k}{2k-n}\frac{n!\,k^{2k-n}}{2^{n-k}}.
\]
When \(A\) is fully colored and \(B\) has a blank, interchange the sides. If both sides are fully colored, the weight \(2n>2k\), so these cannot be minima.

Matched-support assignments always exist when \(n>k\), attaining weight \(2k\). The preceding cases prove the sharp minimum, exhaustive disjoint classification, and counting formula, including the boundary \(n=2k\), where the opposite side of a one-side-full assignment is completely blank.

Finally, for \(n>2k\), a minimum in \(K_{n,n}\) must have blanks on both sides: a wholly colored side alone costs \(n>2k\). Each side of an optimum therefore contains exactly \(k\) colored vertices, one of each color; unlike the crown graph, the two support index sets are arbitrary and independent. This gives \(\binom nk^2(k!)^2\) complete-bipartite minima and the stated ratio. QED.

## Verification
The standalone reproducibility script `artifacts/verify.py` uses literal open-neighborhood tests, not the structural criterion, to enumerate every assignment of weight at most the asserted optimum in selected nontrivial cases. It checks that no lighter assignment works, that all attaining assignments fall in the theorem's described types, and that their number agrees with the closed formula. Exhaustive checks cover \(k=2\) with \(2\le n\le8\) and \(k=3\) with \(3\le n\le6\). It additionally checks integer identities over \(2\le k\le15\) and \(k<n\le5k\). Replay from the packaged script reports `VERIFY_OK`. The infinite theorem is proved above, not inferred from these finite checks.

## Relationship to prior work
Lange's 2026 analysis studies **singleton** rainbow \(k\)-domination, deriving bounds and exact scalar values for regular families including cycles, prisms and Möbius ladders; its text does not give the number or structure of optimum configurations on the crown graph, viewed as a bipartite double cover of a complete graph. Rao, Udupa and Prathviraj study two-service domination under joins, Cartesian products, coronas and splitting graphs; the crown is instead a **tensor product** \(K_n\times K_2\). Related published work on complete multipartite graphs counts **ordinary two-rainbow functions with multilabel vertices** on a different graph family. None of these cited claims implies the closed optimum-deployment count or matched-index rigidity here. This comparison is about mathematical implications, not merely matching titles. A potentially relevant early 2026 dual-server foundational article was available only in bibliographic/abstract form; historical priority must therefore be treated as provisional.

## Limitations
This result enumerates only minimum-weight functions, not the full weight polynomial. It does not apply unchanged to ordinary set-valued rainbow functions, nonuniform palettes, arbitrary deleted matchings, or general bipartite graphs. No claim of independent external validation is made. Priority comparisons cannot exclude all unindexed earlier material, especially studies under the synonym "dual-server domination."

## References
1. P. Lange, *Complexity, Bounds, and Exact Algorithms for Rainbow \(k\)-Domination in Regular Graphs*, arXiv:2610.06906v1, first public 2026-10-01, https://arxiv.org/html/2610.06906.
2. S. L. Rao, S. Udupa N. V. and Prathviraj N, *The Dual-Server Domination Number of Some Graph Operations*, arXiv:2608.14690v1, first public 2026-08-07, https://arxiv.org/abs/2608.14690.
3. M. Chellali, T. W. Haynes and S. T. Hedetniemi, *Dual-server domination in graphs*, Discrete Applied Mathematics 387 (2026), 251--259, DOI:10.1016/j.dam.2026.03.017 (full text not inspected).
4. *All 2-rainbow dominating functions of complete multipartite graphs*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-all-2-rainbow-dominating-functions-of-complete-multipartite-grap--7f7bcd9e9b58 (RESULT.md inspected; explicitly set-valued labels).
