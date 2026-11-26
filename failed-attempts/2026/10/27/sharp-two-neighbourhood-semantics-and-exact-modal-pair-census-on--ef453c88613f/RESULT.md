# Sharp two-neighbourhood semantics and exact modal-pair census on finite intuitionistic chains

## Finding

Let \(n\geq 1\). For the \(n\)-point intuitionistic chain with the continual constructive-neighbourhood semantics defined below, every frame has a modally equivalent frame on the same ordered worlds whose neighbourhood family at each world has **at most two members**. This is the least possible uniform bound for \(n\geq2\); one member suffices for \(n=1\).

More precisely, the number \(T_n\) of **distinct ordered pairs of unary box and diamond operations on the full Heyting algebra of upsets**, realized by all such continual frames, is

\[
T_n=1+\binom{2n}{n-1}+\sum_{\ell=1}^{n}\left[\binom{n+\ell-1}{\ell}^{2}+\binom{n+\ell-2}{\ell-1}\left(\binom{n+\ell-1}{\ell-1}-1\right)\right].
\]

Its first eight values are \(3,22,224,2634,33462,444987,6097086,85331650\), for \(n=1,\ldots,8\). Equality of these operation pairs is equivalent to agreement of every modal formula, at every world, under every hereditary atomic valuation. These are *semantic quotient counts*, not counts of raw neighbourhood assignments or isomorphism classes.

## Assumptions and scope

Fix the chain \(W=\{0<1<\cdots<n-1\}\). For each \(t\in\{0,\ldots,n\}\), set \(U_t=\{t,t+1,\ldots,n-1\}\), where \(U_n=\varnothing\). These are exactly the \(n+1\) upsets. A constructive-neighbourhood frame is an arbitrary map \(N:W\to\mathcal P(\mathcal P(W))\). It is **continual** when \(i\le j\) and \(N(i)\ne\varnothing\) imply \(N(j)\ne\varnothing\). No supplementation, finite-intersection closure, or other neighbourhood axiom is assumed.

An intuitionistic valuation sends propositional letters to upsets, conjunction and disjunction to intersection and union, and implication to the Heyting implication of upsets. For every upset \(U\), define the two modal operations by

\[
\begin{aligned}
 i\in\mathcal B_N(U)&\iff (\forall j\ge i)(\exists A\in N(j))\ A\subseteq U,\\
 i\in\mathcal D_N(U)&\iff (\forall j\ge i)(\forall A\in N(j))\ A\cap U\ne\varnothing.
\end{aligned}
\]

These are the persistent constructive-neighbourhood clauses of the cited logical semantics. The empty neighbourhood family and the family containing the empty subset are **different**, and both are allowed. The claim concerns all finite chain sizes and all modal formula depths, but only this frame class and these clauses.

## Proof

**1. Local two-endpoint lemma.** For a neighbourhood family \(\mathcal F\subseteq\mathcal P(W)\), define a pair of *local thresholds* \((b(\mathcal F),d(\mathcal F))\) as follows:

\[
(b,d)=\begin{cases}
(-1,n),&\mathcal F=\varnothing,\\
(n,-1),&\varnothing\in\mathcal F,\\
\left(\max_{A\in\mathcal F}\min A,\ \min_{A\in\mathcal F}\max A\right),&\text{otherwise}.
\end{cases}
\]

In the last case the family is nonempty and every one of its members is nonempty, so both extrema exist in \(\{0,\ldots,n-1\}\). For any \(t\in\{0,\ldots,n\}\), direct inspection gives

\[
(\exists A\in\mathcal F)\ A\subseteq U_t\iff t\le b(\mathcal F),\qquad
(\forall A\in\mathcal F)\ A\cap U_t\ne\varnothing\iff t\le d(\mathcal F).
\]

For the empty family the existential is false and the universal is true; for a family containing \(\varnothing\), the existential is true and the universal is false. For regular families, containment depends only on the minimum member of each nonempty set, while intersection with an upper interval depends only on its maximum.

Every possible local pair has an explicit representative of size at most two:

\[
\begin{array}{c|c}
(b,d)&\text{representative family}\\\hline
(-1,n)&\varnothing\\
(n,-1)&\{\varnothing\}\\
0\le b\le d<n&\{\{b,d\}\}\\
0\le d<b<n&\{\{b\},\{d\}\}.
\end{array}
\]

Here the outer braces are the neighbourhood family, and inner braces are subsets of \(W\). Thus replacing every \(N(i)\) by its representative preserves whether that family is empty and therefore preserves continuality.

**2. Global thresholds and full modal equivalence.** Let \((b_i,d_i)\) be the local thresholds at world \(i\), and put

\[
B_i=\min_{j\ge i}b_j,\qquad D_i=\min_{j\ge i}d_j.
\]

The modal clauses and the local lemma give

\[
i\in\mathcal B_N(U_t)\iff t\le B_i,\qquad
 i\in\mathcal D_N(U_t)\iff t\le D_i.
\]

Hence the ordered pair of modal operations is determined exactly by the two nondecreasing sequences \((B_i)\) and \((D_i)\). Conversely, evaluating the two operations on all \(U_t\) recovers each threshold from the largest true \(t\), with the sentinel value \(-1\) when no \(t\) works. Thus distinct pairs \((B,D)\) yield distinct operation pairs. The previous replacement leaves both operations on *every* upset unchanged. Induction on the structure of formulas, using unchanged Heyting propositional operations and hereditary atomic upsets, proves truth agreement for arbitrarily nested formulas.

**3. Shape of the threshold profiles.** Continuality gives a unique \(k\in\{0,\ldots,n\}\) such that the first \(k\) families are empty and all later families are nonempty. When \(k=n\), the unique profile is \(B_i=-1\), \(D_i=n\) everywhere. For \(k<n\), put \(\ell=n-k\), the length of the nonempty suffix. The sequence \(B\) equals \(-1\) before \(k\) and takes nondecreasing values on the suffix. The sequence \(D\) equals \(D_k\) before \(k\). The position \(k\) can be recovered exactly as the first index with \(B_k\ge0\).

If the *last* family contains the empty set, the suffix of \(D\) is constantly \(-1\), while \(B\) is any nondecreasing length-\(\ell\) sequence in \(\{0,\ldots,n\}\) ending in \(n\). Conversely, every such \(B\) is achieved by putting \(\{\varnothing\}\) at the last world, putting a singleton family \(\{\{B_i\}\}\) at earlier nonempty-suffix positions with \(B_i<n\), and putting \(\{\varnothing\}\) wherever \(B_i=n\).

Otherwise the last family contains no empty set. On the suffix, \(B\) is any nondecreasing sequence with entries in \(\{0,\ldots,n-1\}\), and \(D\) is a nondecreasing sequence with entries in \(\{-1,0,\ldots,n-1\}\) and a nonnegative last entry, subject to just one compatibility rule: **if \(D\) jumps from \(-1\) to a nonnegative value between consecutive indices \(i\) and \(i+1\), then \(B_i=B_{i+1}\)**. Necessity follows because a last local family containing \(\varnothing\) at index \(i\) forces its local box threshold to equal \(n\), and therefore \(B_i=\min(n,B_{i+1})=B_{i+1}\).

For sufficiency, let the first nonnegative entry of \(D\) on the suffix occur at index \(t\). If it begins immediately, realize every local pair \((B_i,D_i)\) by the two-set construction from Step 1; coordinatewise nondecreasing global thresholds then result. If it begins later, use \(\{\varnothing\}\) at index \(t-1\), use regular representatives realizing \((B_i,D_i)\) from index \(t\) onwards, and use regular representatives with box threshold \(B_i\) and any regular diamond threshold at earlier nonempty-suffix positions. The forced equality at the jump gives the required box suffix minima, and the family containing \(\varnothing\) at \(t-1\) forces precisely the required initial diamond threshold \(-1\). This realizes **every** profile satisfying the stated rule. The empty-family prefix is then added unchanged.

**4. Exact count.** For each \(\ell\in\{1,\ldots,n\}\), the case with the last family containing \(\varnothing\) has

\[
\binom{n+\ell-1}{\ell-1}
\]

profiles: choose the first \(\ell-1\) weakly increasing box thresholds from the \(n+1\) available symbols. Summing over \(\ell\) gives \(\binom{2n}{n-1}\) by the hockey-stick identity.

In the other case, if all \(\ell\) diamond thresholds are nonnegative, the box and diamond suffixes can be chosen independently as weakly increasing sequences of length \(\ell\) over \(n\) symbols. This gives \(\binom{n+\ell-1}{\ell}^{2}\) profiles.

Otherwise the diamond suffix has exactly \(s\) initial entries \(-1\), for a unique \(1\le s<\ell\). The nonnegative remainder has \(\binom{n+\ell-s-1}{\ell-s}\) choices, while the forced equality of two adjacent box thresholds leaves \(\binom{n+\ell-2}{\ell-1}\) choices for the entire box suffix. Thus this subcase gives

\[
\binom{n+\ell-2}{\ell-1}\sum_{s=1}^{\ell-1}\binom{n+\ell-s-1}{\ell-s}
=\binom{n+\ell-2}{\ell-1}\left(\binom{n+\ell-1}{\ell-1}-1\right).
\]

Adding these disjoint cases and the single all-empty frame yields the stated formula for \(T_n\). There is no overcount: \(k\) and every threshold are recoverable from the actual modal operations.

**5. Sharpness of two neighbourhoods.** Let \(n\ge2\), make every family empty below the top world, and at the top world use exactly the two singleton neighbourhoods \(\{0\}\) and \(\{n-1\}\). This frame is continual. Its top local (hence global) thresholds are \((B_{n-1},D_{n-1})=(n-1,0)\). A family consisting of *at most one* subset gives either one of the two exceptional pairs \((-1,n)\), \((n,-1)\), or a regular pair satisfying \(b\le d\), because the minimum of a single nonempty subset cannot exceed its maximum. It therefore cannot reproduce the two top thresholds. Since these can be read directly from the two operations on upsets, no equivalent one-neighbourhood-per-world frame exists. For \(n=1\), every regular local pair has equal endpoints, so the construction from Step 1 uses at most one member everywhere. This proves optimality.

## Verification

The accompanying `checker.py` is a standalone Python 3 program using only the standard library; execute `python3 checker.py`. It exhaustively inspects **all raw continual neighbourhood assignments** on one and two worlds (not merely canonical representatives), confirming exactly \(3\) and \(22\) operation pairs. It separately enumerates all canonical local endpoint types through four worlds, obtaining \(3,22,224,2634\). It checks \(18{,}000\) randomly generated nested formulas on larger small frames against the compressed frames and tests the sharp witness for each chain size from two through eight. Every test passed. These calculations diagnose the proof; they are **not** an infinite proof and do not certify priority.

## Relationship to prior work

Dalmonte and de Groot (2026) introduce and investigate the relevant constructive-neighbourhood semantics and continual frames, with completeness, proof calculus and decidability results. Dalmonte (2022) previously studied persistent constructive modal clauses, while de Groot (2025) developed a related intuitionistic neighbourhood account via translation. Those semantic foundations are **prior work**, not newly introduced here. The contribution proved above is the uniform two-member compression **simultaneously for the two operators**, its sharpness, and the exact all-chain cardinality of the resulting semantic-operation quotient.

Published studies of finite-chain birelational frames and of finite-chain KI confluence use **relational frame conditions** and enumerate raw relations rather than the paired unary operations of continual constructive-neighbourhood frames. Results on instantial neighbourhood *arity* concern a different kind of expressive resource and do not imply this two-member compression. The prior-work searches and source-inspection record are described in `AUDIT.json`; no absence-of-prior-art claim follows merely from a search with no hit.

## Limitations

The count is for labelled, linearly ordered worlds, and distinguishes operation pairs, **not** presentations of the same operations by different families. Nothing here counts arbitrary finite posets or asserts preservation of added frame axioms such as supplementation, intersection closure, or special modal reduction principles under compression. An equivalent classification may exist under an older predicate-transformer, ordered-algebra, or neighbourhood-model formulation; independent literature review and independent mathematical audit have not been performed.

## References

1. T. Dalmonte and J. de Groot, *Intuitionistic Monotone Modal Logic: Proof Theory and Semantics*, arXiv:2606.31870v1, 30 June 2026. https://arxiv.org/abs/2606.31870
2. T. Dalmonte, *Wijesekera-style constructive modal logics*, arXiv:2210.09937v1, 18 October 2022. https://arxiv.org/abs/2210.09937
3. J. de Groot, *Intuitionistic monotone modal logic via translation*, arXiv:2507.13746v1, 18 July 2025. https://arxiv.org/abs/2507.13746
