# A six-vertex counterexample to path minimality for the first two greedy colour classes

## Finding

Let \(G\) be a finite tree. Choose a uniformly random permutation of its vertices, and perform *first-fit colouring*: at each vertex in this order, assign the least positive integer absent from its previously coloured neighbours. Let \(X(G)\) count the vertices receiving colours \(1\) or \(2\).

Let \(P_6\) be the path with edge set
\[
E(P_6)=\{(0,1),(1,2),(2,3),(3,4),(4,5)\},
\]
and let \(T_6\) be the tree with edge set
\[
E(T_6)=\{(0,1),(1,2),(0,3),(3,4),(0,5)\}.
\]
Thus \(T_6\) has one vertex of degree three and arms of lengths \(2,2,1\).

**Theorem (minimal counterexample).** The expected first-two-colour counts satisfy
\[
\mathbb E X(P_6)=\frac{397}{72},\qquad
\mathbb E X(T_6)=\frac{131}{24},\qquad
\mathbb E X(P_6)-\mathbb E X(T_6)=\frac1{18}>0.
\]
For every \(1\le n\le5\) and every \(n\)-vertex tree \(T\), one has \(\mathbb E X(T)\ge\mathbb E X(P_n)\). Hence six is the minimum possible order of a counterexample to path minimality for the first two random greedy colour classes.

## Assumptions and scope

Graphs are finite, simple, undirected trees. Vertices are distinguishable and their arrival ordering is uniformly distributed over all \(n!\) permutations. The colouring is ordinary first-fit, using a single permutation, with no rerandomization between colour classes. The expectation is over the vertex order only. The statement is a *counterexample and finite minimum-order certificate*, not a claim about all larger orders or an exact extremizer for each size.

## Proof

For an ordering \(\sigma=(v_1,\ldots,v_n)\), set \(c(v_i)\) to the least positive integer outside \(\{c(v_j):j<i,\ v_jv_i\in E(G)\}\). This recursion uniquely specifies every resulting colouring and provides a finite exhaustive computation with no probabilistic approximations.

At six vertices, there are precisely \(6!=720\) equally likely orderings. The exhaustive counts for vertices of colour at least three, listed in vertex order \(0,1,2,3,4,5\), are

| Tree | Counts at individual vertices | Sum |
| --- | --- | ---: |
| \(P_6\) | \(0,71,104,104,71,0\) | 350 |
| \(T_6\) | \(174,108,0,108,0,0\) | 390 |

The equivalent full output-size distributions are

| Tree | \(\#\{X=4\}\) | \(\#\{X=5\}\) | \(\#\{X=6\}\) |
| --- | ---: | ---: | ---: |
| \(P_6\) | 0 | 350 | 370 |
| \(T_6\) | 30 | 330 | 360 |

Each row sums to 720. Since every vertex belongs to the first two classes exactly when its colour is at most two, linearity gives
\[
\mathbb E X(P_6)=6-\frac{350}{720}=\frac{397}{72},\qquad
\mathbb E X(T_6)=6-\frac{390}{720}=\frac{131}{24}.
\]
This establishes the strict inequality, independently of any asymptotic approximation.

For minimality, enumerate all labelled trees on \(n\le5\) vertices by Prüfer sequences. For \(n\ge2\), the classical Prüfer correspondence lists all \(n^{n-2}\) labelled trees exactly once (with the single-vertex tree handled separately). For each tree, apply the same first-fit recursion to each of its \(n!\) orders. The minima and path values coincide:

| \(n\) | Labelled trees evaluated | Minimum of \(\mathbb E X\) | Value for \(P_n\) |
| ---: | ---: | ---: | ---: |
| 1 | 1 | \(1\) | \(1\) |
| 2 | 1 | \(2\) | \(2\) |
| 3 | 3 | \(3\) | \(3\) |
| 4 | 16 | \(15/4\) | \(15/4\) |
| 5 | 125 | \(14/3\) | \(14/3\) |

The table is a complete finite census because the Prüfer encoding is bijective and every ordering is evaluated exactly. It excludes every counterexample on fewer than six vertices and completes the proof.

## Verification

The supplied `verify.py` uses standard-library integer arithmetic only. It computes the two six-vertex distributions by two independently implemented methods: direct iteration through all permutations and a dynamic program merging identical partial colour states while preserving multiplicities. It asserts exact agreement and the displayed integer tables. Separately, it generates **all** Prüfer sequences at orders \(3\), \(4\), and \(5\), enumerates all vertex orders and verifies the minimum against each path. Run from the directory containing the files:

```bash
python3 verify.py
```

No simulation, floating-point numerical tolerance, or external data are involved. The proof uses a finite exhaustive certificate, which is sufficient for a claim about these finitely many tree orders; no larger-order conclusion is inferred.

## Relationship to prior work

Krivelevich, Mészáros, Michaeli and Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216 (first posted 16 July 2019), establish that paths minimize the expected size of the **first** greedy colour class on trees (Theorem 1.4). Their Section 9, “The second colour,” expressly asks whether paths also minimize the total in the **first two** colour classes. The counterexample above answers that different question negatively. Their first-colour result does not imply a two-colour result or the present strict reversal.

Beaudou and collaborators, *Connected greedy colourings of perfect graphs and other classes: the good, the bad and the ugly*, arXiv:2110.14003 (2021), study extremal colour counts for restricted connected arrival orders, not expectations of two colour-class sizes under a uniform unrestricted order. The problems and their quantifiers differ.

## Limitations

This is an exact finite-order counterexample, not a classification of minimizing trees for all \(n\), nor a quantitative asymptotic improvement. The phenomenon pertains to first-fit sequential colouring with one uniformly random order; it is not a statement about separate independent greedy independent-set runs for each colour. The literature comparison does not establish absolute historical uniqueness, and independent validation has not been performed.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216, first posted 2019-07-16, Section 9 and Theorem 1.4. https://arxiv.org/abs/1907.07216
2. L. Beaudou, C. Brosse, O. Defrain, F. Foucaud, A. Lagoutte, V. Limouzy, L. Pastor, *Connected greedy colourings of perfect graphs and other classes: the good, the bad and the ugly*, arXiv:2110.14003, first posted 2021-10-26. https://arxiv.org/abs/2110.14003
