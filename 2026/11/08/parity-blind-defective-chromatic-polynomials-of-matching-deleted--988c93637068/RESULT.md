# Parity-blind defective chromatic polynomials of matching-deleted cliques

## Finding

Let \(n\geq2\), \(0\leq t\leq\lfloor n/2\rfloor\), and \(d\geq0\) be integers. Let \(G_{n,t}=K_n-M_t\), where \(M_t\) is a matching of \(t\) edges, and let \(\chi_d(G;k)\) count assignments of \(k\) named vertex colours such that each vertex has at most \(d\) same-colour neighbours. Unused colours are permitted. Put
\[
E_b(x)=\sum_{j=0}^{b}\frac{x^j}{j!},\qquad
B_b(N,k)=N!\,[x^N]E_b(x)^k.
\]
When \(d\) is odd, **every matching deletion is invisible to the defective chromatic polynomial**:
\[
\chi_d(G_{n,t};k)=\chi_d(K_n;k)=B_{d+1}(n,k).
\]
When \(d=2h\) is even, put \(s=h+1\). For every nonnegative integer \(k\),
\[
\boxed{\chi_{2h}(G_{n,t};k)=\sum_{r=0}^{\lfloor t/s\rfloor}
\binom{k}{r}\frac{t!}{(s!)^r(t-rs)!}
B_{2h+1}(n-2sr,k-r).}
\]
As polynomial identities in \(k\), the formula is valid for all real or complex \(k\) when the coefficient-extraction definition of \(B_b(N,k)\) is used. For integer \(k\geq0\), terms with \(r>k\) are zero and need not be evaluated.

There is a sharp equality and leading-term criterion:
\[
\chi_d(G_{n,t};k)=\chi_d(K_n;k)
\quad\Longleftrightarrow\quad
\bigl(d\text{ odd}\bigr)\ \text{or}\ \bigl(d=2h\text{ even and }t\leq h\bigr),
\]
where equality means identical polynomials in \(k\). If \(d=2h\) and \(t\geq h+1\), the nonzero difference has degree exactly \(n-d-1\) with leading coefficient \(\binom{t}{h+1}\):
\[
\chi_d(G_{n,t};k)-\chi_d(K_n;k)
=\binom{t}{h+1}k^{n-d-1}+O(k^{n-d-2})
\]
(the remainder is zero when the exponent would be negative). Thus at fixed even defect the first coefficient distinguishing a matching deletion counts subsets of \(h+1\) deleted edges.
For example, the cocktail-party graph on six vertices (\(n=6,t=3\)) has exactly the same \(1\)-defective polynomial as \(K_6\), whereas
\[
\chi_2(K_6-M_3;k)-\chi_2(K_6;k)=3k(k-1)^2.
\]

## Assumptions and scope

Graphs are finite, simple, and have named vertices; the deleted matching is fixed. A colour class is the fibre of one of the \(k\) named colours. Defect counts neighbours in the original graph, not merely monochromatic connected components or nonadjacent same-colour vertices. The sum permits \(t=0\), \(d=0\), and defects larger than every graph degree. A zero-vertex residual graph has one empty colouring; in particular \(B_b(0,k)=1\). For \(k=0\) with \(n\geq1\), both sides count zero colourings.

## Proof

Fix a colour class \(S\subseteq V(G_{n,t})\) of size \(a\). Each vertex in \(S\) is adjacent to every other vertex of \(S\) except possibly its unique partner in the deleted matching. Hence its monochromatic degree is \(a-1\) if its deleted partner is not in \(S\), and \(a-2\) if that partner is in \(S\).

If \(a\leq d+1\), every vertex has monochromatic degree at most \(d\). If \(a\geq d+3\), every vertex has degree at least \(a-2\geq d+1\), so the class is forbidden. At the only intermediate size, \(a=d+2\), the class is permitted precisely if every member has its deleted partner in \(S\). Equivalently, \(S\) must be a union of \(s=(d+2)/2\) entire deleted matching edges. This can occur only when \(d\) is even and \(t\geq s\).

Therefore every permissible colouring has uniquely defined **exceptional colours** whose fibres have size \(d+2=2s\), each consisting of exactly \(s\) deleted matching edges. All other colour fibres have size at most \(d+1\). The exceptional fibres are disjoint, so if their number is \(r\), their \(r\) colour names can be chosen in \(\binom{k}{r}\) ways. Assigning distinct matching edges to these \(r\) named fibres gives
\[
\frac{t!}{(s!)^r(t-rs)!}
\]
possibilities: each selected name receives exactly \(s\) disjoint missing edges. The remaining \(n-2sr\) vertices may receive any of the other \(k-r\) colours, provided each fibre has size at most \(d+1\). That count is \(B_{d+1}(n-2sr,k-r)\) by the exponential generating function for allocations of labelled vertices to named bins. Summing by the unique number of exceptional colours proves the even-defect formula. For odd defect no exceptional fibre exists, proving the equality with \(K_n\).

For \(d=2h\) and \(t\geq s=h+1\), the term with \(r=1\) is nonzero. Its maximal-degree contribution occurs when each of the \(n-2s\) residual vertices receives a distinct one of the remaining colours. Choosing the exceptional missing-edge subset gives \(\binom{t}{s}\) options, and then choosing injective colours gives \((k)_{n-2s+1}\), whose leading coefficient is one. Residual repeated colours yield lower-degree terms. For any \(r\geq2\), the number of used colours is at most \(n-r(2s-1)=n-r(d+1)<n-d-1\), so those contributions also have strictly lower degree. All terms count colourings and are nonnegative on positive integers, so no cancellation can erase the leading coefficient. This proves the sharp difference degree and the equality criterion. For \(t<s\), there are no exceptional classes and only \(r=0\) remains, as claimed.

## Verification

The accompanying `verify.py` independently constructs the adjacency matrix of \(K_n-M_t\) and tests the literal at-most-\(d\) same-colour-neighbour condition for every map to palettes of sizes \(1,2,3,4\), all \(2\leq n\leq8\), all \(0\leq t\leq\lfloor n/2\rfloor\), and all \(0\leq d\leq n\). The 608 resulting parameter profiles agree exactly with a separate dynamic-programming evaluation of the formula. Further tests check the parity equality and leading coefficient through \(n=10\). Invoke `python verify.py` with Python 3 and no external dependencies. The proof above, not these finite tests, establishes the theorem for all parameters.

## Relationship to prior work

Asgarli, Whitehead McGinley, and Xue (arXiv:2605.05550, first submitted May 7, 2026) formalize defective chromatic polynomials, show a contraction expansion for arbitrary graphs (Theorem 2.1), and study how much structural information the entire defective family carries. Their general contraction expansion implies an algorithmic expression for the present graph family but does not state or directly simplify to the exceptional-fibre classification, the all-defect closed formula, or the parity-blindness and sharp leading-coefficient results. The present theorem is an explicit specialization and structural refinement, not a claimed improvement to the universal contraction identity.

Humpert's earlier degree-chromatic formulation uses a shifted defect index. Work on defective and clustered colourings, including Wood's survey, focuses chiefly on existence and minimum palettes rather than exact named-colour counting. The cocktail-party graph is the perfect-matching case \(t=n/2\). A prior published acyclic-orientation enumeration for matching-deleted cliques concerns a different invariant. No matching result was identified in the inspected references and targeted searches; absence from these searches is not proof of global priority.

## Limitations

The deleted edges must form a matching; arbitrary deleted subgraphs need not have the one-partner fibre structure. The formula counts named colourings, not colourings modulo graph automorphisms or colour permutations. The explicit specialization follows from elementary counting and is compatible with previously known universal expansions. Mathematical priority is provisional pending independent literature assessment. The finite verifier is corroboration, not certification of the infinite theorem.

## References

1. S. Asgarli, T. Whitehead McGinley, N. Xue, *Defective chromatic polynomials*, arXiv:2605.05550 (initial submission 2026-05-07), https://arxiv.org/abs/2605.05550; HTML version https://arxiv.org/html/2605.05550v1.
2. B. Humpert, *A quasisymmetric function generalization of the chromatic symmetric function*, Electron. J. Combin. 18 (2011), P31; https://doi.org/10.37236/518.
3. D. R. Wood, *Defective and Clustered Graph Colouring*, Electron. J. Combin. DS23 (2018), https://doi.org/10.37236/7406.
