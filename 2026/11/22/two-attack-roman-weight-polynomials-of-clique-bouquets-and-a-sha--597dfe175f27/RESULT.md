# Two-attack Roman weight polynomials of clique bouquets and a sharp optimum transition

## Finding
Let \(q\ge 2\), let \(s_1,\ldots,s_q\ge2\) be integers, and let
\[
G=K_1\vee\bigl(K_{s_1}\sqcup\cdots\sqcup K_{s_q}\bigr),\qquad M=\sum_{i=1}^{q}s_i.
\]
The unique universal vertex is called the center, and the \(q\) pairwise anticomplete cliques are petals. A **two-attack Roman function** is a labeling \(f:V(G)\to\{0,1,2\}\) such that for every one- or two-element set \(S\) of zero-labeled vertices, at least \(|S|\) *distinct* vertices labeled \(2\) lie in the union of the open neighborhoods of \(S\). Its weight is \(w(f)=\sum_{v\in V(G)}f(v)\). Let
\[
\mathcal A_G(z)=\sum_{f\text{ feasible}}z^{w(f)}.
\]
Define the following explicit petal polynomials for each integer \(s\ge2\):
\[
\begin{aligned}
A_s(z)&=(1+z+z^2)^s-(1+z)^s+z^s,\\
B_s(z)&=s z^{s-1},\\
C_s(z)&=A_s(z)-s z^2\sum_{j=2}^{s-1}\binom{s-1}{j}z^{s-1-j}.
\end{aligned}
\]
An empty sum is zero. Then **the complete weight polynomial, at every degree**, is
\[
\boxed{\begin{aligned}
\mathcal A_G(z)={}&z^2\prod_{i=1}^{q}A_{s_i}(z)
+z^2\sum_{i=1}^{q}B_{s_i}(z)\prod_{j\ne i}A_{s_j}(z)\\
&+(1+z)\prod_{i=1}^{q}C_{s_i}(z)
-\left(1+\sum_{i=1}^{q}s_i(s_i-1)\right)z^M.
\end{aligned}}
\]
In particular, for the homogeneous bouquet \(G_{q,s}=K_1\vee(qK_s)\) with \(q,s\ge2\), its minimum two-attack Roman weight and the *exact number of minimum functions* are
\[
\boxed{\gamma_{2aR}(G_{q,s})=
\begin{cases}
2q,&s=2,\\
2q+2,&s\ge3,
\end{cases}}
\]
and
\[
\boxed{\#\{f:w(f)=\gamma_{2aR}(G_{q,s})\}=
\begin{cases}
3^q-2q-1,&s=2,\\
63,&s=3,\ q=2,\\
(q+1)3^q,&s=3,\ q\ge3,\\
s^q,&s\ge4.
\end{cases}}
\]
The minimum functions are also classified explicitly in the proof.

A closed total count follows by evaluating at \(z=1\). Put \(a_s=3^s-2^s+1\) and \(c_s=a_s-s(2^{s-1}-s)\). Then
\[
\mathcal A_G(1)=\prod_i a_{s_i}+\sum_i s_i\prod_{j\ne i}a_{s_j}
+2\prod_i c_{s_i}-1-\sum_i s_i(s_i-1).
\]

## Assumptions and scope
All vertices are labelled/distinguished, and colors \(0,1,2\) are fixed numerical labels, not interchangeable. Graphs are finite, undirected and simple. Both the heterogeneous formula and homogeneous optimum classification require at least two petals, each containing at least two vertices. The function definition follows the **two distinct simultaneous zero-vertex attacks** convention, with one label-\(2\) vertex able to defend at most one attack. This is not ordinary Roman domination, Roman \(\{2\}\)-domination, double Roman domination or weak Roman domination.

The coefficient of \(z^t\) counts all feasible functions of weight \(t\), not only inclusion-minimal or minimum-weight functions. The formula is exact for every listed integer parameter; no asymptotic or probabilistic hypotheses are needed.

## Proof
**1. One petal with a locally supported zero.** A petal labeling is type \(A\) if it either has no zeros (all vertices are labelled \(1\) or \(2\)), or has at least one label \(2\). This excludes exactly the labelings that use only \(0,1\) and contain a zero. Subtracting the latter from all ternary labelings gives \(A_s(z)\). A petal with precisely one zero, all other labels \(1\), and no label \(2\), has polynomial \(B_s(z)=s z^{s-1}\). Call such a petal *weak*.

A type-\(C\) petal is a type-\(A\) petal with one further family removed: those having exactly one vertex labelled \(2\) and at least two zeros. Indeed, choose the \(2\) in \(s\) ways, choose \(j\ge2\) zeros among the remaining \(s-1\) vertices, and label all others \(1\). The weight is \(2+s-1-j\), giving the displayed sum for \(C_s\).

**2. Center label \(2\).** Every peripheral zero sees the center. Such a zero also sees a second defender exactly when its own petal contains a label \(2\). Two peripheral zeros that lack their own petal defenders have only the center as a common available defender, so the two-attack condition fails. Conversely, if at most one peripheral zero lacks a petal defender, every zero has one defender, and any pair of zeros has at least two distinct defenders: a pair containing two locally defended zeros sees the center and a petal defender; a pair containing the unique weak zero sees the center and a local defender for the other zero. Thus either every petal is type \(A\), or exactly one petal is weak and all others are type \(A\). These cases contribute
\[
z^2\prod_i A_{s_i}(z)+z^2\sum_i B_{s_i}(z)\prod_{j\ne i}A_{s_j}(z).
\]

**3. Center label \(1\).** Every peripheral zero must see a label \(2\) within its own petal. If two zeros lie in the same petal, they need at least two distinct local defenders; in different petals, their local defenders are automatically distinct. Therefore a labeling is feasible if and only if every petal is type \(C\), giving \(z\prod_i C_{s_i}(z)\).

**4. Center label \(0\).** Every peripheral zero again needs a local defender. Two zeros in the same petal need two local defenders, while zeros in different petals see distinct local defenders. Thus each petal must be type \(C\). In addition, a pair consisting of the center and a peripheral zero has available defenders equal to *all* label-\(2\) peripheral vertices. It therefore requires at least two such vertices. If there are no peripheral zeros, the center merely requires at least one peripheral \(2\). Among the products of type-\(C\) petals, the only invalid configurations are: (i) the all-ones assignment, with no defender, of weight \(M\); and (ii) precisely one defender and one peripheral zero, in the same petal, with all other peripherals labelled \(1\). For (ii) there are exactly \(\sum_i s_i(s_i-1)\) assignments, again all of weight \(M\). Everything else counted by the product is feasible. This gives
\[
\prod_i C_{s_i}(z)-\left(1+\sum_i s_i(s_i-1)\right)z^M.
\]
The four center cases and subcases are disjoint and exhaustive. Adding them proves the polynomial identity. Substitution at \(z=1\), using \(A_s(1)=a_s\), \(B_s(1)=s\), and \(C_s(1)=c_s\), proves the total-count formula.

**5. Homogeneous minimum and all optimizers.** For \(s=2\), the least-degree terms of both \(A_s\) and \(C_s\) are \(3z^2\). The center-zero case therefore has minimum degree \(2q\), with coefficient \(3^q-1-2q>0\) for \(q\ge2\); the other center cases have larger minimum degree. Exactly these minimum functions label the center \(0\), assign every edge-petal one of \((1,1),(2,0),(0,2)\), and choose the latter two types in at least two distinct petals. This gives \(3^q-2q-1\) assignments.

For \(s=3\), \(A_s\) starts with \(3z^2\), \(B_s=3z^2\), and \(C_s\) starts with \(7z^3\). Thus the center-two case has least degree \(2q+2\) with coefficient \((q+1)3^q\). Its optimizers put either one \(2\) and two zeros in each petal, or put one weak petal of type \((0,1,1)\) and the one-defender pattern in every other petal. The center-one case starts above this degree. The center-zero case starts in degree \(3q\), so it ties only at \(q=2\), when its degree-six coefficient equals \(7^2-(1+2\cdot3\cdot2)=36\). Those 36 extra optimizers have center \(0\) and in both petals a permutation of \((0,1,2)\). Hence the coefficient is \(27+36=63\) at \(q=2\); otherwise it is \((q+1)3^q\).

For \(s\ge4\), the lowest-degree term of \(A_s\) is \(s z^2\); \(B_s\) begins at degree at least three, while \(C_s\) begins at degree four. Since \(q\ge2\), the unique minimum regime has the center labelled \(2\) and exactly one labelled \(2\) in each petal, with every other vertex labelled \(0\). Its weight is \(2q+2\), and it has \(s^q\) choices. All competing center regimes have strictly greater weights. This proves every claimed minimum and completes the classification.

## Verification
`verify_attack.py` independently enumerates all ternary vertex labelings on ten parameter tuples, checks every one- and two-vertex zero attack directly against graph adjacency, and compares every weight coefficient with an independently expanded version of the displayed formula. This checks 215,298 assignments, including heterogeneous petal sizes and the exceptional triangular two-petal case.

`verify_independent.cpp` performs a second direct ternary enumeration using a distinct base-three counter and bit-mask implementation. It checks seven homogeneous parameter pairs, including \((q,s)=(3,4)\), which has \(3^{13}=1,594,323\) possible labelings, and confirms each claimed minimum coefficient. Both programs were executed successfully on the supplied sources. Instructions and sample output are recorded in `CHECKS.txt`.

These finite checks stress-test the formulas; the proof for unbounded petal sizes and number of petals is the symbolic classification above.

## Relationship to prior work
Koch and Shank (first public arXiv version 25 May 2023) defined the two-attack Roman invariant and developed structural, extremal and general algorithmic results; their full accessible 16-page preprint treats complete graphs, stars, paths, cycles and general bounds, but gives neither this bouquet weight polynomial nor its optimizer classification. Their general extremal machinery does not itself count all functions of any prescribed weight.

Earlier published descriptions of clique bouquets concern *different* domination predicates. The accessible complete proofs of the ordinary Roman, total Roman, and weak Roman weight polynomials of windmills count different function sets: in ordinary Roman domination, the center labelled \(2\) permits arbitrary peripheral zeros; for two attacks it permits at most one zero without a separate local defender. Likewise, a center labelled \(1\) and a petal with a single defender plus multiple zeros can be Roman but fails the simultaneous-attack condition. Neither a polynomial for the larger Roman function class nor one for weak/total Roman functions determines the subset enumerated here.

Research-record and web searches for two-attack Roman domination, `2aRD`, simultaneous Roman defense, friendship graphs, generalized windmills, heterogeneous clique bouquets, and the explicit join description found no source stating or implying the complete formula. This is **not** a claim that missing search results establish worldwide priority.

## Limitations
The formulas assume clique petals of size at least two, with at least two petals. The result does not address higher-attack thresholds or arbitrary graphs with cut vertices. Novelty remains provisional because no search can exclude an unindexed historical equivalent. The computational tests cover bounded orders and do not substitute for the all-parameters proof. No independent mathematical audit has been performed.

## References
1. G. Koch and N. Shank, *On the k-Attack Roman Dominating Number of a Graph*, arXiv:2305.16256, first version 25 May 2023, https://arxiv.org/abs/2305.16256 (full preprint https://arxiv.org/pdf/2305.16256).
2. *Roman domination polynomial of generalized windmill graphs*, publicly accessible published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-roman-domination-polynomial-of-generalized-windmill-graphs--60695442a75b.
3. *Weak Roman domination polynomial of heterogeneous windmills*, publicly accessible published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-weak-roman-domination-polynomial-of-heterogeneous-windmills--e0942c187585.
4. *Total Roman domination polynomial of heterogeneous windmills*, publicly accessible published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-total-roman-domination-polynomial-of-heterogeneous-windmills--5959e7c34d61.
