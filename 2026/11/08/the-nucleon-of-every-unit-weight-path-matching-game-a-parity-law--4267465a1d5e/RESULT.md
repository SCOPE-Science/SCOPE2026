# The nucleon of every unit-weight path matching game: a parity law and an exact second level

## Finding

For the ordinary unit-weight cooperative matching game on the path \(P_n\), the multiplicative nucleon has an explicit complete classification. For every odd \(n=2m+1\ge3\), its unique vector is
\[
x_{2j-1}=0\quad(1\le j\le m+1),\qquad x_{2j}=1\quad(1\le j\le m).
\]
For every even \(n=2m\ge4\), its unique vector is
\[
x_{2j-1}=\frac{j}{m+1},\qquad x_{2j}=\frac{m+1-j}{m+1}\qquad(1\le j\le m).
\]
In the even case the optimal first multiplicative level is \(1\); after removing coalitions whose ratio is fixed at \(1\) throughout that first-stage face, the sharp next level is exactly
\[
\alpha_2=1+\frac{1}{m^2-1}.
\]
The \(m+1\) coalitions attaining the next-level bottleneck force uniqueness. Odd-order paths have a unique core allocation; even-order paths have a nontrivial core but a unique nucleon. For \(n=2\), every nonnegative split of the single matching unit is a nucleon allocation, since no proper coalition has positive worth.

## Assumptions and scope

Let \(P_n\) be the path with vertices \(N=\{1,\ldots,n\}\) and edges \(\{i,i+1\}\) of weight \(1\), with \(n\ge3\). For every coalition \(S\subseteq N\), define its worth \(v(S)\) to be the cardinality of a maximum matching in the induced graph \(P_n[S]\). Its grand worth is \(v(N)=\lfloor n/2\rfloor\). An imputation is a vector \(x\in\mathbb R_{\ge0}^n\) with \(x(N)=\lfloor n/2\rfloor\); write \(x(S)=\sum_{i\in S}x_i\). The nucleon lexicographically maximizes the nondecreasing vector of ratios \(x(S)/v(S)\) over all proper nonempty \(S\) with \(v(S)>0\). Coalitions of worth zero are excluded, and so is the grand coalition. The core consists of imputations satisfying \(x(S)\ge v(S)\) for every coalition. This is the multiplicative nucleon, not the additive nucleolus.

## Proof

**A core test for unit matching games.** A nonnegative efficient vector \(x\) lies in the core exactly when \(x_i+x_{i+1}\ge1\) for every path edge. Necessity follows from the two-vertex coalition. Conversely, for any matching \(M\) contained in \(P_n[S]\), disjointness and nonnegativity give
\[
x(S)\ge\sum_{\{i,i+1\}\in M}(x_i+x_{i+1})\ge |M|.
\]
Taking the maximum over \(M\) proves the converse.

**Odd-order path.** Set every odd-indexed payoff to \(0\) and every even-indexed payoff to \(1\). Every path edge has total payoff \(1\), so the vector is efficient and in the core. To see uniqueness, fix any odd vertex \(2j-1\). Removing it leaves two even-length segments with a matching of \(m\) edges. For any core imputation, the disjoint edge inequalities for this matching sum to at least \(m\), which already equals the total imputation. Nonnegativity forces \(x_{2j-1}=0\). This holds for each odd vertex. Then the edge inequalities force every even payoff to be at least \(1\), and efficiency forces it to equal \(1\). Every nucleon allocation must lie in the nonempty core: the proposed core vector gives minimum positive-coalition ratio at least \(1\), hence the nucleon's first ratio is at least \(1\). Therefore the unique core vector is the unique nucleon vector.

**Even-order path, first stage.** Let \(n=2m\) with \(m\ge2\). The \(m\) disjoint pairs \(B_j=\{2j-1,2j\}\) each have worth \(1\), and their payoffs sum to the grand worth \(m\). Thus no imputation can have minimum positive-coalition ratio greater than \(1\). A core imputation exists, for instance all payoffs \(1/2\), so the optimal first ratio is exactly \(1\) and its optimizing face is the core. On this face every \(B_j\) must be tight, because its payoff is at least \(1\) and their sum is exactly \(m\). Write
\[
x_{2j-1}=a_j,\qquad x_{2j}=1-a_j,\qquad 0\le a_1\le\cdots\le a_m\le1.
\]
The order constraints are exactly the remaining edge inequalities, \(x_{2j}+x_{2j+1}=1-a_j+a_{j+1}\ge1\).

**The \(m+1\) gaps give the upper bound.** Define
\[
g_0=a_1,\quad g_j=a_{j+1}-a_j\ (1\le j<m),\quad g_m=1-a_m.
\]
These are nonnegative and sum to \(1\). Consider the proper coalitions
\[
S_0=N\setminus\{2\},\quad S_j=N\setminus\{2j-1,2j+2\}\ (1\le j<m),\quad S_m=N\setminus\{2m-1\}.
\]
Each has worth exactly \(m-1\): the induced path retains \(m-1\) disjoint edges, while it has at most \(2m-1\) vertices for the endpoint cases and at most \(2m-2\) vertices for interior cases. Their imputed values are exactly \(m-1+g_j\). Consequently
\[
\min_{0\le j\le m}\frac{x(S_j)}{v(S_j)}
=1+\frac{\min_jg_j}{m-1}
\le1+\frac{1}{(m+1)(m-1)}.
\]
Equality forces all \(m+1\) gaps to equal \(1/(m+1)\), hence necessarily \(a_j=j/(m+1)\).

**The upper bound is attained and isolates the second level.** Put \(a_j=j/(m+1)\) and denote the resulting vector by \(x^*\). Every coordinate is positive. Every base edge \(B_j\) has payoff \(1\); every cross edge \(\{2j,2j+1\}\) has payoff \(1+1/(m+1)\). The matching argument from the core test shows \(x^*(S)\ge v(S)\). Moreover equality for a positive-worth coalition holds only if the coalition is a union of complete base pairs: any unmatched vertex has positive payoff, and any selected cross edge has payoff strictly exceeding \(1\). Conversely each union of base pairs has payoff equal to its matching value, namely the number of included pairs. Every nonempty proper union of base pairs has ratio \(1\) for *every* first-stage core allocation, not merely for \(x^*\). No other coalition payoff is fixed on this face: its expression in the free coordinates \(a_1,\ldots,a_m\) has a nonzero coefficient for a pair containing exactly one member of the coalition, and the order polytope \(0<a_1<\cdots<a_m<1\) has nonempty interior. Thus these and only these base-pair unions have ratios fixed at the first stage.

For every other proper coalition \(S\) of positive worth, the difference \(x^*(S)-v(S)\) is a strictly positive integer multiple of \(1/(m+1)\); in particular it is at least \(1/(m+1)\). Because \(S\ne N\), its maximum matching has at most \(m-1\) edges. Thus
\[
\frac{x^*(S)}{v(S)}\ge1+\frac{1}{(m+1)(m-1)}=1+\frac{1}{m^2-1}.
\]
The coalitions \(S_0,\ldots,S_m\) attain equality. On the first-stage face, maximizing the next nonfixed ratio is therefore equivalent to maximizing the least ratio over coalitions outside the fixed base-pair unions. The universal upper bound above is tight at \(x^*\) and equality forces all gaps equal, so this second stage has the unique maximizer \(x^*\). Hence the complete lexicographic nucleon is the claimed singleton.

## Verification

The standalone `verify.py` uses only the Python 3 standard library. It evaluates induced-path maximum matching worth by a separate dynamic program, forms exact `fractions.Fraction` payoffs and coalition ratios, tests every positive-valued proper coalition for \(3\le n\le16\), and separately optimizes the second level over the complete rational core grid of denominator \(m+1\) for \(n=4,6,8,10\). It checks the claimed tight witness coalitions and unique rational-grid maximizer. Run with `python3 verify.py`. In the completed execution, all \(124293\) positive-coalition tests and \(633\) rational-grid candidates passed. These finite checks corroborate but do not replace the proof for all orders.

## Relationship to prior work

Aziz and Csáji (2026), *Computing the Nucleon of Matching Games*, establish a polynomial-time combinatorial algorithm for the nucleon of every ordinary weighted matching game and describe the complete nucleon via compact stages. Their Section 4 works with general stage constraints and includes a weighted four-vertex path example (weights \(5,4,2\)). The present result is therefore **not** a new general-purpose polynomial-time algorithm and does not challenge that earlier computational coverage; it instead evaluates the entire infinite unit-path family symbolically, proves a parity dichotomy and identifies an exact second lexicographic level. Those explicit formulas and the forced-gap proof were not found in the inspected general algorithm. Faigle, Kern, Fekete and Hochstättler (1998) introduced the nucleon and gave an earlier algorithm for matching games; the inspected account likewise supplies general computability rather than the all-order unit-path formulas. This distinction is one of mathematical statements, not of titles. A separate known nucleon analysis for a one-edge-augmented complete-bipartite graph concerns a different graph family and does not directly yield this path formula.

## Limitations

The theorem applies only to **ordinary** unit-weight paths with one vertex per player and unconstrained transfers. It does not classify weighted paths, cycles, trees, \(b\)-matching games, or the additive nucleolus. The classification is an explicit specialization of an already algorithmically computable class, not a new complexity result. The full claims of all possible unindexed prior works cannot be excluded; independent external verification has not been performed. Finite exhaustive checks through sixteen vertices are evidence for implementation correctness, not a proof of the infinite statement.

## References

1. H. Aziz and G. Csáji, *Computing the Nucleon of Matching Games*, arXiv:2610.29731v1, first posted 21 October 2026, https://arxiv.org/abs/2610.29731 . Material checked: Sections 2–4 (definitions, matching-game algorithm, and the weighted four-vertex path example).
2. U. Faigle, W. Kern, S. P. Fekete and W. Hochstättler, *The Nucleon of Cooperative Games and an Algorithm for Matching Games*, Mathematical Programming 83 (1998), 195–211, https://www.ibr.cs.tu-bs.de/users/fekete/hp/publications/PDF/1998-The_Nucleon_of_Cooperative_Games_and_an_Algorithm_for_Matching_Games.pdf . Material checked: definitions, matching-game algorithm and illustrative calculations.
