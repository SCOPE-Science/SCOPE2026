# Finite-variable theories of permutation digraphs: the 26-class two-variable boundary

## Finding
Let \(\mathcal P\) be the class of **nonempty finite** structures \((X,R)\) with exactly one binary relation, where \(R(x,y)\) means \(\sigma(x)=y\) for a bijection \(\sigma:X\to X\). Loops encode fixed points. Define \(c_\ell(P)\) as the number of cycles of length \(\ell\) in \(P\). Logical equivalence \(\equiv_{\mathrm{FO}^k}\) means agreement on **all** counting-free first-order sentences using at most \(k\) reusable variable names, with no bound on quantifier depth.

**Theorem.** The equivalences in \(\mathcal P\) have the following complete description.

1. At width one, \(P\equiv_{\mathrm{FO}^1}Q\) if and only if \(P,Q\) agree both on the existence of a fixed point and on the existence of a non-fixed point. Exactly **three** one-variable theories occur.
2. At width two, put \(a(P)=\min(c_1(P),2)\), \(b(P)=\min(c_2(P),2)\), and
   \[
   t(P)=\begin{cases}
   0,&\sum_{\ell\ge3}c_\ell(P)=0,\\
   1,&c_3(P)=1\ \text{and}\ c_\ell(P)=0\ (\ell\ge4),\\
   2,&\text{otherwise}.
   \end{cases}
   \]
   Then \(P\equiv_{\mathrm{FO}^2}Q\) if and only if \((a(P),b(P),t(P))=(a(Q),b(Q),t(Q))\). Exactly **26** two-variable theories occur.
3. For every integer \(k\ge3\),
   \[
   P\equiv_{\mathrm{FO}^k}Q\quad\Longleftrightarrow\quad
   \min(c_\ell(P),k)=\min(c_\ell(Q),k)
   \quad\text{for every integer }\ell\ge1.
   \]

All equivalences are at unrestricted quantifier depth. Every two-variable theory has a unique smallest representative, up to isomorphism, consisting of \(a\) fixed-point cycles, \(b\) two-cycles, and respectively no long cycle, one three-cycle, or one four-cycle according as \(t=0,1,2\). The generating polynomial by the order of this smallest representative is
\[
(1+z+z^2)(1+z^2+z^4)(1+z^3+z^4)-1.
\]
Its maximum exponent is \(10\), attained by one theory; the coefficient sum is \(26\).

For \(k\ge3\), every theory also has a unique smallest representative, with exactly \(\min(c_\ell(P),k)\) cycles of each length. If \(a_k(n)\) counts theories whose smallest representative has \(n\) vertices, then
\[
1+\sum_{n\ge1}a_k(n)z^n
=\prod_{\ell\ge1}(1+z^\ell+\cdots+z^{k\ell})
=\prod_{\substack{r\ge1\\(k+1)\nmid r}}\frac1{1-z^r}.
\]

## Assumptions and scope
The domain is finite and nonempty, the relation is required to be the full graph of **one permutation**, and the language contains equality and \(R\) but no function symbol, order, unary colors, or counting quantifier. All classifications and minimum-representative statements are **relative to** \(\mathcal P\), not over arbitrary directed graphs. A permutation's cycle decomposition is unique up to reordering cycles.

## Proof
**Step 1: one variable.** An atomic formula in one name is either equality of that variable to itself or \(R(x,x)\). Every one-variable formula is consequently determined by the available truth values of \(R(x,x)\). On a nonempty permutation structure there are exactly three possibilities: all elements fixed, none fixed, or both types present. The formulas \(\exists x\,R(x,x)\) and \(\exists x\,\neg R(x,x)\) separate them. Induction on formulas gives the converse, including unbounded quantifier nesting.

**Step 2: two-variable unary categories.** Using only names \(x,y\), define the following mutually exclusive unary predicates, with bound variables renamed locally if needed:
\[
F(x):=R(x,x),\qquad
T(x):=\neg F(x)\land\exists y\,(x\ne y\land R(x,y)\land R(y,x)),\qquad
L(x):=\neg F(x)\land\neg T(x).
\]
They select vertices on cycles of lengths one, two, and at least three respectively. The atomic pair types available from an anchored element have the following exhaustive description. For an \(F\)-anchor there is the anchor, and a distinct unrelated \(F\)-vertex exactly when \(a=2\). For a \(T\)-anchor there is the anchor, its unique mutually related partner, and a vertex from another two-cycle exactly when \(b=2\). For an \(L\)-anchor there is the anchor, its unique distinct successor, its unique distinct predecessor, and a vertex with neither directed edge to the anchor exactly when \(t=2\). The last assertion follows because a single three-cycle is a directed triangle with one edge between every distinct pair, whereas any longer cycle has nonneighbors, and two or more long cycles also supply nonneighbors. Vertices in different categories are unrelated in both directions; each category is present exactly when the corresponding invariant is nonzero.

Hence equal \((a,b,t)\) gives Duplicator a permanent two-pebble winning strategy: after removing the moved pebble, match the next vertex by the anchored unary category and atomic pair type. Every type available on one side is available on the other. Conversely, each component of the invariant is definable: \(a=0,1,2\) from the existence of one or of two distinct \(F\)-vertices; \(b=0,1,2\) from existence of a \(T\)-vertex and from two nonadjacent distinct \(T\)-vertices; and \(t=0,1,2\) from existence of an \(L\)-vertex and from two distinct \(L\)-vertices without an arrow in either direction. All these tests use at most two variable names. Thus the criterion is both necessary and sufficient. Of the \(3^3\) possible triples, only \((0,0,0)\) is excluded by nonemptiness, yielding \(26\). Choosing the smallest realizations of the three independent categories gives the displayed minimum-representative polynomial; the \(t=2\) category first occurs with a four-cycle.

**Step 3: width at least three, distinguishing direction.** For any \(m\ge0\), the relation \(\sigma^m(u)=v\) is expressible by a formula \(\mathrm{Path}_m(u,v)\) using only three reusable names. The construction is by induction: \(\mathrm{Path}_0(u,v)\) is \(u=v\), and for distinct endpoint names \(u,v\), with third name \(w\),
\[
\mathrm{Path}_{m+1}(u,v):=\exists w\,
  (\mathrm{Path}_m(u,w)\land R(w,v)).
\]
The subformula \(\mathrm{Path}_m(u,w)\) may bind the name \(v\) **within that subformula only**; its binding does not capture the independent occurrence of \(v\) in the sibling conjunct \(R(w,v)\). Every recursive instance is hygienically substituted with the appropriate three names. The special case with identical endpoints is obtained by substituting the same free name after constructing the two-endpoint formula. A vertex lies in a cycle of exact length \(\ell\) iff \(\mathrm{Path}_\ell(u,u)\) holds and every \(\mathrm{Path}_j(u,u)\), \(1\le j<\ell\), fails. Two such vertices are on the same \(\ell\)-cycle iff one is reached from the other by one of the \(\ell\) forward paths of length less than \(\ell\). With \(k\ge3\) variable names one can existentially select \(j\le k\) vertices of exact period \(\ell\), require them to lie on pairwise different cycles, and test the requisite path formulas. Whenever such a test uses the third name, it may locally bind a name used by a *different* selected representative, because the representatives it compares remain free within that conjunct. Thus \(\mathrm{FO}^k\) determines \(\min(c_\ell,k)\) for every \(\ell\).

**Step 4: width at least three, equivalence direction.** Assume the truncated multiplicities coincide. Duplicator maintains an injective matching between those cycles containing pebbled vertices, preserving each matched cycle's actual length and a chosen rotation, and maps each pebbled vertex by that rotation. After one pebble is lifted, at most \(k-1\) source cycles are occupied. If Spoiler plays inside one already occupied cycle, use its predetermined rotation. Otherwise choose an unoccupied cycle of the same length: if the number of cycles of that length is below \(k\), the two numbers agree exactly; if it is at least \(k\) on either side, it is at least \(k\) on both sides, and at least one is free. A rotation can send the new vertex to any chosen position. The resulting partial map preserves equality and all positive and negative \(R\)-atoms, forever. The same argument works for either direction of Spoiler's move. By the ordinary counting-free \(k\)-pebble theorem, the two structures agree on all \(\mathrm{FO}^k\) sentences.

**Step 5: minimum representatives and generating functions.** For \(k\ge3\), Step 3 distinguishes different truncated multiplicities while Step 4 identifies all realizations of one truncation vector. Choosing each size to be its truncation produces the unique smallest model. The unrestricted product is a formal power-series identity: multiply the finite geometric factors and use \(1+z^\ell+\cdots+z^{k\ell}=(1-z^{(k+1)\ell})/(1-z^\ell)\). Cancellation deletes exactly the factors at indices divisible by \(k+1\). No convergence assumptions are needed.

## Verification
The standalone standard-library program `permutation_probe.py` forms all nonempty integer partitions up to size seven, eight, and six for widths one, two, and three respectively. It constructs the associated looped directed successor graphs, computes atomic colors on \(k\)-tuples, and repeatedly refines those colors by **sets** of one-coordinate extension colors (not multisets). Its independent fixed-point refinement performs \(946\), \(2145\), and \(406\) pairwise comparisons, totaling \(3497\), and reports zero disagreements with the theorem. This is a finite corroboration, not a proof of unrestricted depth in arbitrarily large structures.

The second standard-library program `permutation_spectrum.py` enumerates the \(26\) two-variable signatures and their canonical minimum representatives, derives the exact minimum-order spectrum
\[
(1,2,2,4,4,4,3,3,2,1)\quad\text{at orders }1,\ldots,10,
\]
checks that the largest minimum order is ten, compares the two partition-product coefficient recurrences through degree thirty for widths three through seven, and checks the proposed canonical minimum sizes on \(1860\) pairs of finite cycle types and widths. Recorded output is in the correspondingly named `.out` files. Replay commands: `python3 permutation_probe.py` and `python3 permutation_spectrum.py` from the directory containing all four artifacts. No special package or network access is required.

## Relationship to prior work
Grohe and Otto [1], §2, give the general correspondence between counting-free finite-variable logic and ordinary pebble games; they do not provide the permutation-specific classification or its exceptional width-two spectrum. Albert, Bouvel, and Féray [2], §§2 and 6, study precisely the same **one-bijection binary relational signature**, prove the unrestricted ordinary-FO isomorphism/cycle-type correspondence, and characterize properties jointly definable in their two permutation languages. Their inspected results do not assert the fixed-variable equivalence criterion, the \(26\) width-two classes, or the smallest representative spectrum. The distinction from their full-FO classification is substantive: bounded variables merge many nonisomorphic cycle types at unbounded quantifier depth.

Related work on permutation systems with **unary function symbols** has a different bounded-variable syntax, since arbitrarily iterated function terms are available even in quantifier-free formulas. The class of disjoint unions of finite chains also has a restricted-partition generating function, but its relations and low-width classifications differ. This result does not claim that the classical Euler-product identity is itself new. No exhaustive historical-priority assertion is made.

## Limitations
The result does not extend automatically to counting quantifiers, unary function symbols in place of \(R\), arbitrary functional digraphs with non-cycle trees, additional predicates, or infinite permutation structures. The 26-class number refers to **nonempty finite bijection graphs** and the zero-size empty structure is deliberately excluded. Tests on finite orders support the argument but cannot establish the infinite family. An unlocated general finite-variable composition theorem might imply some of these facts; external independent review has not occurred.

## References
[1] M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990v1 (first public 2012-04-09), §2, DOI: 10.48550/arXiv.1204.1990.

[2] M. H. Albert, M. Bouvel, and V. Féray, *Two first-order logics of permutations*, arXiv:1808.05459v1 (first public 2018-08-16), §§2, 6; *Journal of Combinatorial Theory, Series A* 171 (2020), article 105158, DOI: 10.1016/j.jcta.2019.105158.

[3] I. Pratt-Hartmann, *The two-variable fragment with counting and equivalence*, *Mathematical Logic Quarterly*, DOI: 10.1002/malq.201400102 (2015). A richer counting/equivalence language and satisfiability questions, rather than exact counting-free permutation theories.
