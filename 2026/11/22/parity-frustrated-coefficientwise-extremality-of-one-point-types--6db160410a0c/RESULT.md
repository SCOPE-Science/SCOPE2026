# Parity-frustrated coefficientwise extremality of one-point types over oriented cycles

## Finding
For each integer \(n\ge4\), take any orientation \(D_\epsilon\) of the simple cycle with its \(n\) vertices individually named in the countable homogeneous oriented graph forbidding the transitive triangle. Let \(P_\epsilon(z)\) enumerate complete nonalgebraic one-point types by the number of named vertices joined by an arc to the new point.

Write \(\epsilon_i=+1\) when the old arc is \(v_i\to v_{i+1}\), and \(\epsilon_i=-1\) for the reverse, with subscripts modulo \(n\). Its *directed-through defect set* is \(B_\epsilon=\{i:\epsilon_{i-1}=\epsilon_i\}\). For \(S\subseteq\mathbb Z/n\mathbb Z\), let \(s(S)\) be the number of vertices of \(S\) with neither cyclic neighbour in \(S\). Then the entire graded type polynomial is
\[
P_\epsilon(z)=\sum_{S\subseteq\mathbb Z/n\mathbb Z}2^{s(S)}z^{|S|}\prod_{i\in B_\epsilon}\left(1-\mathbf1_{\{i-1,i,i+1\}\subseteq S}\right).
\]
In particular, changing the orientation without changing the defect set leaves the polynomial unchanged.

The coefficientwise minimum is attained **only** by the two consistently directed cycles. The coefficientwise maximum is attained **only** by the two alternating source/sink orientations when \(n\) is even, and **only** by the \(2n\) orientations having exactly one directed-through defect when \(n\) is odd. Every other orientation differs strictly at the cubic coefficient. Indeed
\[
[z^0]P_\epsilon=1,\quad [z^1]P_\epsilon=2n,\quad [z^2]P_\epsilon=2n^2-5n,
\]
\[
[z^3]P_\epsilon=n+2n(n-4)+\frac{4}{3} n(n-4)(n-5)-|B_\epsilon|.
\]
This sharp odd-cycle parity obstruction makes the maximizers necessarily imperfect alternations. Their complete polynomials, as well as the minimizing polynomials, admit the exact matrix formulas in the proof. Total maximum/minimum type counts differ exponentially with \(n\).

## Assumptions and scope
An oriented graph has at most one of the arcs between any two distinct vertices. The forbidden transitive triangle is the acyclic three-vertex tournament; a directed three-cycle is permitted. The class of finite oriented graphs omitting the transitive triangle has free amalgamation and hence a countable homogeneous Fraïssé limit with the finite extension property. The old parameter graph is an *induced* orientation of \(C_n\), with no old arcs except its cycle edges, and each old vertex is fixed by a name. The specified one-point types are nonalgebraic, with the new vertex distinct from every old vertex. Homogeneity and finite relational quantifier elimination identify them with allowed arc/nonarc vectors. All assertions hold for every integer \(n\ge4\), every labeled orientation and all polynomial coefficients, not just in the large-size limit.

## Proof
**1. One-point relation states.** For the relation of the new point \(x\) to each old vertex \(v_i\), use state \(0\) for no arc, \(+\) for \(x\to v_i\), and \(-\) for \(v_i\to x\). On a forward old arc \(v_i\to v_{i+1}\), the only permitted pair with two nonzero states is \((+,-)\), which makes the three arcs a directed cycle. On a reverse old arc the only permitted nonzero pair is \((-,+)\). Every state pair involving \(0\) is permitted. Every forbidden triple involving \(x\) contains one old cycle edge, so these constraints are necessary and sufficient. Every permitted word has one complete nonalgebraic type and has infinitely many realizations by free amalgamation.

**2. Support decomposition.** Fix the support \(S\) of the nonzero states. Each singleton component of the cycle induced on \(S\) has two choices of sign. On a component with at least two vertices, its first edge fixes both endpoint signs and every subsequent edge fixes the next sign. Adjacent edges can both be satisfied at an interior vertex exactly when their directions alternate along the original cyclic indexing. Thus a component with at least two vertices has exactly one valid labeling unless it includes the three consecutive selected vertices centered at some \(i\in B_\epsilon\), in which case it has none. For \(S\) equal to the full cycle, the same argument applies at every vertex: there is one labeling if \(B_\epsilon=\varnothing\), otherwise none. Therefore the number of words with support \(S\) is exactly \(2^{s(S)}\) if no forbidden centered triple is contained in \(S\), and zero otherwise. Summing over all supports proves the displayed polynomial identity, including the full-support boundary case.

**3. Orientation parity and extremizers.** The number of changes between successive signs \(\epsilon_i\) while going once around the cycle is even. Thus \(|B_\epsilon|\equiv n\pmod2\). Every prescribed subset \(B\) with this parity occurs: choose the first edge direction freely and propagate, changing direction exactly outside \(B\); the parity condition closes the cycle. There are exactly two orientations realizing any admissible \(B\).

For defect sets \(B\subseteq B'\), each support allowed by \(B'\) is allowed by \(B\), with the same nonnegative weight. Hence \(P_{B'}\preceq P_B\) coefficientwise. The largest possible defect set is the full cycle, realized only by the two consistent orientations, giving the minimum. For even \(n\), the empty set is admissible and gives the maximum; for odd \(n\), the smallest admissible sets are singletons. All singleton defects are equivalent under rotation, so have the same polynomial. Any admissible odd defect set contains a singleton, giving the stated maximum. The unique conditions for equality and the exact numbers of orientations follow once strictness at degree three is established in step 4.

**4. Sharp cubic diagnostic.** On three selected old vertices there are three support shapes: three consecutive (\(n\) choices, weight \(1\)), exactly one adjacent pair (\(n(n-4)\) choices, weight \(2\)), and no adjacent pair (\(n(n-4)(n-5)/6\) choices, weight \(8\)). These formulas also hold in the boundary cases \(n=4,5\) with zero independent triples. Thus the hypothetical unrestricted cubic coefficient is \(n+2n(n-4)+\frac{4}{3} n(n-4)(n-5)\). Each defect forbids exactly its own distinct consecutive triple of size three, of weight \(1\). Because these triples are distinct for \(n\ge4\), the coefficient falls by exactly \(|B_\epsilon|\). This proves the cubic formula and proves strictness whenever an orientation fails to have the minimum or maximum possible number of defects. The orientations achieving those extrema are therefore exactly those named in the theorem. The constant, linear and quadratic coefficients follow from the same support classification.

**5. All-order exact extremal polynomials and growth.** In state order \((0,+,-)\), define weighted edge-transfer matrices
\[
M(z)=\begin{pmatrix}1&z&z\\1&0&z\\1&0&0\end{pmatrix},\qquad
N(z)=\begin{pmatrix}1&z&z\\1&0&0\\1&z&0\end{pmatrix}.
\]
Every row corresponds to the state at \(v_i\), every column to the state at \(v_{i+1}\), and the column weight is \(z\) exactly for a nonzero state. Closing the state word gives the trace of the cyclic product. Consequently the exact minimum polynomial is \(\operatorname{tr}(M(z)^n)\), while the maximum is
\[
P_n^{\max}(z)=\begin{cases}
\operatorname{tr}((M(z)N(z))^{n/2}),&n\text{ even},\\
\operatorname{tr}((M(z)N(z))^{(n-1)/2}M(z)),&n\text{ odd}.
\end{cases}
\]
At \(z=1\), the characteristic polynomials of \(M(1)\) and \(M(1)N(1)\) are respectively \(\lambda^3-\lambda^2-2\lambda-1\) and \(\lambda^3-6\lambda^2+5\lambda-1\). The first matrix is primitive, and the second is strictly positive. Perron–Frobenius theory therefore gives positive leading terms with exponential bases \(\alpha=2.1478990357\ldots\) and \(\beta=\sqrt{5.0489173395\ldots}=2.2469796037\ldots\). Thus along both parity subsequences the maximum/minimum ratio grows as a positive constant times \((\beta/\alpha)^n\).

## Verification
A standalone Python checker `check.py` has three distinct finite implementations: exhaustive direct enumeration of ternary one-point relation words, an independent support/defect enumerator, and a cyclic state-transfer dynamic program. All labeled orientations through eight old vertices passed all three, comprising 502 direct comparisons. All 4,080 labeled orientations from four through eleven old vertices passed defect-versus-transfer comparison, the cubic identity, coefficientwise bounds, the parity restriction, and the exact counts of both kinds of extremizers. Direct enumeration also checked the two extremes at nine, ten and eleven old vertices. Running `python3 check.py` with the standard library reproduces `verification_output.txt`. The universal statement is proved above, not inferred from the finite checks.

## Relationship to prior work
Cherlin's treatment of homogeneous directed graphs and Fraïssé amalgamation provides the existence and extension framework, not cycle-specific graded type counts. Kühn, Osthus, Townsend and Zhao analyze global typical and extremal structure of finite oriented graphs omitting transitive tournaments; their 2014 preprint's Theorem 1.2 concerns almost-all graphs of a given order, not named-parameter singleton types. A related path-shaped one-type switching result establishes a numerical strict switch law for oriented paths; it does not cover the closing edge, cyclic parity obstruction, full graded coefficientwise order, or exact cubic defect count proved here. No stronger covering statement was identified in the cited literature/record comparisons, but an equivalent earlier transfer-matrix or cyclic-word formulation is an unresolved historical-priority possibility.

## Limitations
This theorem is specific to induced cycle parameter bases in the transitive-triangle-free homogeneous *oriented* graph and to complete nonalgebraic singleton types. It does not establish analogous extremality for arbitrary oriented graphs, other forbidden tournaments, or tuple arities greater than one. A failed literature search is not a proof of novelty; historical priority is provisional and independent audit has not been performed.

## References
1. G. L. Cherlin, *Infinite homogeneous directed graphs*, relevant construction in §2.1.3–2.1.4, https://ow3.math.rutgers.edu/~cherlin/Paper/1992Digraph.pdf. See also *The Classification of Countable Homogeneous Directed Graphs and Countable Homogeneous n-tournaments*, Memoirs of the AMS 131 (1998), no. 621, https://doi.org/10.1090/memo/0621.
2. D. Kühn, D. Osthus, T. Townsend and Y. Zhao, *On the structure of oriented graphs and digraphs with forbidden tournaments or cycles*, first posted 2014-04-24, arXiv:1404.6178, https://arxiv.org/abs/1404.6178; especially Theorem 1.2 and its hypotheses.
