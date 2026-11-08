# A Poisson critical window for commutation of past and future modalities on random frames

## Finding

Fix any \(c\in\mathbb R\). On the labelled loopless vertex set \([n]\), take each directed arc independently with probability
\[
p_n=\sqrt{\frac{2\log n+c}{n}},
\]
for all sufficiently large \(n\) for which this lies in \((0,1)\). Let \(G\) and \(H\) denote universal future and universal past boxes: for a subset \(X\subseteq[n]\),
\[
G(X)=\{u:\forall v\,(R(u,v)\Rightarrow v\in X)\},\qquad
H(X)=\{u:\forall v\,(R(v,u)\Rightarrow v\in X)\}.
\]
For each unordered pair \(\{u,v\}\) with \(u\ne v\), let \(O_{uv}\) denote the absence of a common successor and \(I_{uv}\) the absence of a common predecessor. Set
\[
Z_n=\sum_{\{u,v\}\subseteq[n]}\bigl(\mathbf1_{O_{uv}}+\mathbf1_{I_{uv}}\bigr).
\]
Then
\[
\boxed{Z_n\xrightarrow{\mathrm d}\operatorname{Poisson}(e^{-c}).}
\]
Moreover, the probability that \(G(H(X))=H(G(X))\) holds for *every* subset \(X\subseteq[n]\), equivalently that the tense formula \(G(Hq)\leftrightarrow H(Gq)\) holds at all worlds under *every* Boolean valuation of \(q\), has the exact limit
\[
\boxed{\lim_{n\to\infty}\Pr\bigl(G\circ H=H\circ G\bigr)=\exp(-e^{-c}).}
\]
Thus a single universal modal equation exhibits a nontrivial Gumbel-shaped critical profile in the window \(np_n^2=2\log n+c\). This is an asymptotic law, not a claim that the commuting-operator property is monotone in edge probability over the whole interval.

## Assumptions and scope

The relation is directed, loopless and otherwise unrestricted; opposite directed arcs are independent. The base set is labelled. Quantification over valuations means *all* subsets of the vertex set, not a random assignment. The real parameter \(c\) is fixed before letting \(n\to\infty\). Logarithms are natural. Convergence of the integer-valued variable \(Z_n\) is ordinary weak convergence. No claims are made for directed graphs with dependent arcs or for arbitrary scaling of \(p_n\).

## Proof

**1. Modal commutation as a relation identity.** The successor relation of \(G\circ H\) is the relational product \(R\circ R^{-1}\), since \(G(H(X))\) tests \(X\) at all vertices reached by an \(R\)-arc followed by an inverse \(R\)-arc. Likewise \(H\circ G\) has successor relation \(R^{-1}\circ R\). Universal-box operators on a finite set are equal on all subsets exactly when their relations are equal: if an ordered pair belongs to only one relation, taking the complement of its second coordinate as \(X\) distinguishes the two boxes at its first coordinate. For distinct \(u,v\), the product \(R\circ R^{-1}\) contains \((u,v)\) precisely when \(u,v\) have a common successor. The reverse product records common predecessors. Diagonal entries record the existence of at least one successor versus at least one predecessor for each vertex.

**2. A uniform rare-event intersection estimate.** Write \(M_n=2\binom n2=n(n-1)\) for the number of possible directional pair defects. Fix an integer \(t\ge1\), and choose any \(t\) *distinct* defect events (of type \(O\) or \(I\)). Let \(U\) be the union of their endpoints, so \(|U|\le2t\). For every vertex \(z\notin U\), a common-successor witness to an \(O\)-event requires exactly two particular arcs into \(z\); a common-predecessor witness to an \(I\)-event requires exactly two arcs out of \(z\). Each such witness has probability \(p_n^2\). Two distinct witness conditions at a given outside vertex require at least three distinct arcs and therefore have intersection probability at most \(p_n^3\); conditions of opposite directions in fact use disjoint directed arcs. Finite inclusion–exclusion, with constants depending only on \(t\), gives
\[
\Pr(\text{no selected defect has a witness at }z)
=1-tp_n^2+O_t(p_n^3).
\]
The directed arcs involving different outside vertices are disjoint, hence the corresponding restrictions are independent. Witnesses inside \(U\) use only arcs internal to \(U\), independent of the outside arcs; a union bound makes the probability of *no internal witness* equal to \(1+O_t(p_n^2)\), uniformly over the chosen \(t\) events. Thus
\[
\Pr(E_1\cap\cdots\cap E_t)
=\bigl(1-tp_n^2+O_t(p_n^3)\bigr)^{n-|U|}\bigl(1+O_t(p_n^2)\bigr).
\]
Now \(np_n^2=2\log n+c\), \(np_n^3\to0\), \(np_n^4\to0\), and \(|U|\le2t\). Uniformly over all distinct choices, this last probability is
\[
\boxed{n^{-2t}e^{-tc}(1+o(1)).}
\]
The uniformity includes overlapping pairs and mixed predecessor/successor defect types; no independence of the defects themselves is assumed.

**3. Factorial moments.** The \(t\)-th falling-factorial moment of \(Z_n\) sums precisely over ordered lists of \(t\) distinct defect events. Consequently
\[
\mathbb E(Z_n)_t=(M_n)_t n^{-2t}e^{-tc}(1+o(1))\longrightarrow e^{-tc}
\]
for every fixed positive integer \(t\). These are the factorial moments of the Poisson law with mean \(e^{-c}\), and the factorial-moment criterion for nonnegative integer-valued random variables gives \(Z_n\Rightarrow\operatorname{Poisson}(e^{-c})\). In particular, \(\Pr(Z_n=0)\to\exp(-e^{-c})\).

**4. Diagonal entries do not affect the limit.** A diagonal discrepancy can occur only at a vertex with no outgoing arc or no incoming arc. For each vertex, either zero-degree event has probability \((1-p_n)^{n-1}\). Hence the union bound gives
\[
\Pr(\text{some diagonal discrepancy})
\le2n(1-p_n)^{n-1}\le2n\exp(-(n-1)p_n)\longrightarrow0,
\]
because \(np_n\asymp\sqrt{n\log n}\). When no diagonal discrepancy occurs, the relation products coincide if and only if no off-diagonal directional defect occurs, that is, \(Z_n=0\). Combining with Step 3 proves the asserted limit for commutation of tense boxes.

## Verification

The accompanying standalone `checker.py` uses only the Python standard library. Running `python3 checker.py` enumerates every loopless labelled directed relation with one through four vertices, explicitly evaluates \(G(H(X))\) and \(H(G(X))\) on **all** vertex subsets, and confirms equality precisely when the two relational products agree. It independently counts absent common predecessors and successors, comparing their total with the exact finite-\(n\) first-moment identity
\[
\mathbb E Z_n=n(n-1)(1-p^2)^{n-2}
\]
at \(p=\tfrac12\). It also verifies the exact probability that one pair simultaneously lacks both kinds of common neighbor. The expected terminal line is `TENSE_COMMON_NEIGHBOR_EXHAUSTIVE_OK`. The infinite asymptotic conclusion follows from the preceding analytic factorial-moment proof, not the finite checker.

## Relationship to prior work

Figallo, Sarmiento and Pezzini (2026, arXiv:2610.01547v1) investigate tense Boolean algebras, their past/future operators and an algebraic completeness theorem for Kashima's calculus. Their examined introduction, algebraic definitions and conclusions concern proof theory, not random relations or probability distributions for modal commutation. The present theorem uses precisely the conjugate past/future relation but asks a different probabilistic question. Rodionov and Zhukovskii (2018, arXiv:1804.04430) prove a Gumbel-type result for the *maximum* number of common neighbors in an undirected binomial random graph; that theorem does not supply the joint *zero-codegree*, two-direction Poisson count of the present model. The general factorial-moment method and graph common-neighbor thresholds are classical; novelty is asserted only for the explicitly combined joint law and its tense-operator consequence. An earlier formulation in random binary relation or directed-codegree literature could exist and remains a priority risk.

## Limitations

Only the fixed-\(c\) window and the limit law are proved. No quantitative convergence rate, wider phase diagram, correlated-arc extension or claim of global monotonicity is established. Exhaustive computations stop at four vertices and are supporting checks only. Independent mathematical audit and independent historical-priority assessment have not been conducted.

## References

1. M. Figallo, J. Sarmiento, L. Pezzini, *Tense Logic via Truth Degrees: An Algebraic Completeness Result for Kashima's Calculus*, arXiv:2610.01547v1, first public 2026-10-01. https://arxiv.org/abs/2610.01547
2. I. Rodionov, M. Zhukovskii, *The distribution of the maximum number of common neighbors in the random graph*, arXiv:1804.04430v1, 2018. https://arxiv.org/abs/1804.04430
