# Exact Dung semantics for one-source chorded directed cycles

## Finding

Let \(n\ge4\), let the arguments be \(V=\{0,1,\ldots,n-1\}\), and take all attacks \(j\to j+1\pmod n\), together with any chosen extra attacks \(0\to k\) for \(k\in K\subseteq\{2,\ldots,n-2\}\). Put \(h=\max(\{1\}\cup K)\). Define the binary word \((b_j)_{j=0}^{n-1}\) by \(b_0=1\) and, for \(1\le j<n\),

\[
b_j=\begin{cases}0,&j=1\text{ or }j\in K,\\1-b_{j-1},&\text{otherwise}.\end{cases}
\]

Write \(B=\{j:b_j=1\}\) and, for even \(n\), \(O=\{1,3,\ldots,n-1\}\). The complete extensions are exactly the empty set, together with \(O\) if \(n\) is even and \(B\) if \(h\equiv n-1\pmod2\). Every nonempty complete extension is stable; the grounded extension is empty. In particular:

* For odd \(n\), there is exactly one preferred extension: \(B\), stable, when \(h\) is even; otherwise the empty set, which is not stable.
* For even \(n\), \(O\) is always stable and preferred, and \(B\) is a second stable/preferred extension exactly when \(h\) is odd; otherwise \(O\) is the only preferred extension.

All these descriptions are exact, including the no-extra-chord boundary \(K=\varnothing\), which reproduces the classical pure-cycle behavior. The substantive classification concerns arbitrary extra chord sets. Among the \(2^{n-3}\) distinct choices of \(K\), the number admitting a stable extension for odd \(n=2r+1\ge5\) is

\[
\frac{4^{r-1}-1}{3}.
\]

For even \(n=2r\ge4\), the number admitting **two** stable extensions is

\[
\frac{2\cdot4^{r-2}+1}{3}.
\]

In both parity regimes, the proportion of chord sets exhibiting the additional stable alternative tends to \(1/3\) as the length grows. The preceding alternative exists in odd order precisely when stability is restored and in even order precisely when the second stable extension survives.

## Assumptions and scope

All argumentation frameworks here are **finite**, **irreflexive**, and have exactly the indicated directed cycle and optional extra arcs, with no reverse arcs. The source of all optional chords is the designated vertex \(0\); all vertices have their mandatory successor attack. This is not a statement about arbitrary chorded cycles, unoriented cycles, or any other argumentation semantics. A set \(S\) is conflict-free if it contains no attack. It defends a vertex when it attacks all of that vertex's attackers. Admissible means conflict-free and defending every member. A complete extension is a conflict-free fixed point of the defense operator, a preferred extension is a maximal admissible set, and a stable extension is a conflict-free set attacking every vertex outside it. The grounded extension is the least complete extension.

## Proof

**1. Complete extensions not containing \(0\).** Suppose \(S\) is a nonempty admissible set with \(0\notin S\). If \(j\in S\), its compulsory attacker is \(j-1\pmod n\), which must be attacked by \(S\). Since the only attackers of \(j-1\) are \(j-2\) and possibly \(0\), and \(0\notin S\), necessarily \(j-2\pmod n\in S\). Thus \(S\) is closed under subtracting two modulo \(n\). If \(n\) is odd this generates all vertices, including \(0\), a contradiction. If \(n\) is even it generates a parity class, and the class containing \(0\) is excluded. Hence \(S\) must contain all odd-indexed vertices. Those vertices form \(O\), a conflict-free stable extension, because each even vertex is attacked by its odd predecessor, including vertex \(0\) from \(n-1\). Therefore the only nonempty admissible set avoiding \(0\) is \(O\), when \(n\) is even.

**2. Complete extensions containing \(0\).** Let \(S\) be complete with \(0\in S\). All vertices in \(\{1\}\cup K\) are attacked by \(0\), and hence must be outside \(S\). Write \(s_j=\mathbf1_{\{j\in S\}}\). For each \(j\ge2\) not in \(\{1\}\cup K\), the only attacker of \(j\) is \(j-1\). If \(s_{j-1}=1\), conflict-freeness forces \(s_j=0\). If \(s_{j-1}=0\), then \(j-1\) is attacked by \(S\): when \(j-1\) is a chord target or \(1\), it is attacked by \(0\); otherwise induction on the previous index gives \(s_{j-2}=1\), and the compulsory attack from \(j-2\) attacks \(j-1\). Therefore completeness forces \(s_j=1\). Starting with \(s_0=1\) and \(s_1=0\), these rules give the unique word \(b\) in the statement.

As \(n-1\notin\{1\}\cup K\), the last bit is \(b_{n-1}=0\) exactly when \(n-1-h\) is even. This is necessary: if \(b_{n-1}=1\), the arc \(n-1\to0\) contradicts conflict-freeness. Conversely, if \(b_{n-1}=0\), the recursively constructed \(B\) is conflict-free. For every excluded vertex, either it is in \(\{1\}\cup K\) and is attacked by \(0\), or it follows an included predecessor and is attacked by that predecessor. Thus \(B\) attacks every exterior vertex, so it is stable and therefore complete. In particular, there is exactly one complete extension containing \(0\), if the parity condition holds, and none otherwise.

**3. Complete, preferred and grounded semantics.** Every vertex has an attacker (the preceding vertex on the mandatory cycle), so the empty set defends no vertex and is complete. Steps 1 and 2 exhaust all complete extensions. Every preferred extension is complete, every stable extension is preferred, and the empty set is a strict subset of each nonempty extension. Therefore the nonempty extensions listed are exactly the preferred/stable ones if any exist; without such an extension the empty set is preferred. The empty set is always the grounded extension.

**4. Exact chord census.** For each \(k\in\{2,\ldots,n-2\}\), precisely \(2^{k-2}\) chord sets have largest target \(k\); the empty chord set has \(h=1\). For odd \(n=2r+1\), the stability condition says the largest target is even; summing over \(k=2,4,\ldots,2r-2\) gives \(\sum_{j=1}^{r-1}4^{j-1}=(4^{r-1}-1)/3\). For even \(n=2r\), the second stable extension exists for empty \(K\) or largest target odd; summing gives \(1+\sum_{j=1}^{r-2}2\cdot4^{j-1}=(2\cdot4^{r-2}+1)/3\). The limiting ratios follow by dividing by \(2^{n-3}\).

## Verification

The standalone Python 3 checker `verify.py` independently enumerates every subset of arguments and computes conflict-free, admissible, complete, preferred, and stable semantics directly from attack relations, without using the structural recurrence for the direct semantic computation. It checks every chord set for every \(4\le n\le12\), totaling \(1022\) frameworks, and separately checks the closed-form chord enumerators for \(4\le n\le24\). Invocation: `python verify.py`. Observed output: `VERIFY_OK 1022 complete/preferred/stable cases; enumerator census through n=24`. This finite test corroborates but does **not** replace the proof for all \(n\).

## Relationship to prior work

The even/odd parity behavior of an *unmodified* directed cycle is classical; see Bench-Capon (2013). The exact full extension classification for arbitrary one-source shortcut subsets, its dependence only on the last shortcut's parity, and the count of stable-admitting perturbations are the claims assessed here. Zhang and Liu (2026) give broad **sufficient** path-based agreement conditions and a general criterion for stable existence involving admissible sets hitting odd cycles. Their statements do not supply this parameter-level formula: the present class always has its original directed Hamiltonian cycle, and many cases retain both odd and even directed cycles, so the absence-of-cycle hypotheses cannot settle its parity threshold. Elaroussi (2025) obtains tractability under bounded in-/out-degree and general uniqueness if there are no even cycles; the class here may have unbounded outdegree at its hub and both even and odd cycles, so those bounds do not give its exact complete-extension census. A published bidirected-cycle result found through published-finding corpus concerns a different symmetric attack relation; the full text of that record was not accessible for inspection, and this is a stated priority risk, not proof of novelty.

## Limitations

Only chords departing from one designated vertex are allowed; the statement does not cover reverse chords or multiple chord sources. The pure-cycle subcase is already classical. The probability statements refer to uniform choice of a labeled chord subset for a **fixed** source; they do not describe unlabeled isomorphism classes or independent-edge random digraphs. Formal computer-assisted exhaustive checks end at the sizes stated. Priority is qualified by the accessible literature and semantic-implication comparisons, not asserted as globally certified. No independent audit has been performed.

## References

1. Yan Zhang and Kehan Liu, *When Stable and Preferred Semantics Agree: A Path-Based Approach*, arXiv:2610.30176, first public version 2026-10-19, https://arxiv.org/abs/2610.30176 .
2. Mohammed Elaroussi, *Analyzing the impact of bounded degree constraints on computational complexity of argumentation frameworks*, *Argument & Computation* (online 2025-02-14), https://doi.org/10.1177/19462174241306715 .
3. T. J. M. Bench-Capon, *Dilemmas and Paradoxes: Cycles in Argumentation Frameworks*, 2013, https://livrepository.liverpool.ac.uk/3004007/1/TBCLoopsFinal.pdf .
4. P. M. Dung, *On the Acceptability of Arguments and Its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games*, *Artificial Intelligence* **77** (1995), 321–357.
