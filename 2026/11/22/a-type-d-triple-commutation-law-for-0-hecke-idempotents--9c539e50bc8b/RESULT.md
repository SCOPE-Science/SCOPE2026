# A type-D triple-commutation law for 0-Hecke idempotents

## Finding

Let \(H_D(n)\) and \(H_A(n)\) denote the 0-Hecke monoids (Demazure monoids) of finite Coxeter types \(D_n\), \(n\ge4\), and \(A_n\), respectively. Let \(d_n\) and \(a_n\) count **ordered triples** of pairwise-commuting idempotents of these monoids, including repeated idempotents and the identity. Then

\[
\sum_{n\ge4}d_n z^{n-4}
=\frac{1420-3582z+2992z^2-508z^3}{1-8z+16z^2-12z^3+2z^4},
\]

and the *difference between Coxeter types of the same rank* has the compact rational form

\[
\sum_{n\ge4}(d_n-a_n)z^{n-4}
=\frac{30-54z+36z^2}{1-8z+16z^2-12z^3+2z^4}.
\]

In particular \(d_4=1420\), whereas \(a_4=1390\), although the ordered commuting-pair count for both monoids at rank four is \(164\). Thus the rank-only universality of **pair** counts from Berenstein–Greenstein–Li first fails for triples at branching rank four. Further values are \((d_5,d_6,d_7,d_8,d_9)=(7778,42496,232052,1266976,6917372)\).

## Assumptions and scope

The standard type-\(A_n\) graph is a path on \(n\) vertices. For \(D_n\), take a path from vertex \(0\) through \(n-3\) and attach the two leaves \(n-2,n-1\) to vertex \(n-3\). Use the usual 0-Hecke multiplication, with each simple Coxeter generator idempotent. Every idempotent is the longest parabolic element \(w_J^\circ\) for a unique subset \(J\) of graph vertices. Idempotent commutation is in the 0-Hecke monoid, **not** the Coxeter group. No field, characteristic, or representation is involved. All counts concern ordered triples, so permutations of the triple positions are counted separately.

## Proof

**1. Component criterion.** In finite type, Berenstein–Greenstein–Li, Proposition 3.33, proves that \(w_J^\circ\) and \(w_K^\circ\) commute precisely when each connected component of the induced graph on \(J\) and each connected component on \(K\) are either nested or orthogonal (disjoint and with no edge between them). This is equivalent to saying that every connected component of the induced graph on \(J\cup K\) is wholly contained in \(J\) or wholly contained in \(K\). For the forward implication take maximal components in the nested/orthogonal family; different maximal ones are orthogonal and partition the union. For the reverse implication a pair of nonorthogonal support components lies in one union-component, which is covered by one support and hence by its unique connected component there. The equivalence applies independently to each of the three pairs of supports.

**2. Rooted-tree states.** Color each vertex with three membership bits, one for each of the three supports. For pair indices \((1,2),(1,3),(2,3)\), project each three-bit color to a two-bit mask in \(\{0,1,2,3\}\), where the mask bits indicate which supports of the pair contain the vertex. In a valid colored rooted subtree, store for each pair the intersection of the nonzero projected masks in the union-component containing the root; store \(0\) when the root does not belong to that pair-union. Each nonzero stored mask must be nonempty. A one-vertex tree has the state given by the three pairwise projections of its color.

On attaching child subtrees with states \(s^{(j)}\) to a new root of color \(b\), for each pair start with the projection \(p(b)\). If this is \(0\), the new status is \(0\). Otherwise intersect it bitwise with every *nonzero* status for this pair among the children, and reject the coloring if any resulting intersection is \(0\). Validity follows exactly from the component criterion in Step 1: a union-component can satisfy the criterion only if at least one of the two support bits is present throughout that component. The rule is necessary and sufficient and allows all three pairs simultaneously.

With three pair positions in the order above, iterative closure of the one-vertex states under adjoining a single child gives exactly the following \(17\) states:

```
(0,0,0) (0,2,2) (1,1,0) (1,1,1) (1,1,2) (1,1,3)
(1,2,2) (1,3,2) (2,0,1) (2,1,1) (2,2,1) (2,2,2)
(2,2,3) (2,3,1) (3,1,1) (3,2,2) (3,3,3)
```

Let \(T\) be the integer \(17\)-by-\(17\) matrix in this state order: \(T_{s,t}\) is the number of root colors \(b\in\{0,\ldots,7\}\) for which attaching a child in state \(t\) produces state \(s\). Let \(\ell_s\) count one-vertex colors of state \(s\), and let \(h_s\) count colorings of a three-vertex two-leaf star with root state \(s\), computed by the same attachment rule. Writing \({\bf1}\) for the all-ones row,

\[
a_n={\bf1}T^{n-1}\ell\quad(n\ge1),\qquad
d_n={\bf1}T^{n-3}h\quad(n\ge4).
\]

The second identity follows by growing the type-\(D_n\) diagram along its spine from the initial two-leaf hub, attaching one new root for each further spine vertex.

**3. Exact finite-state identity.** Direct integer evaluation of these explicitly defined \(17\) states and \(T\) establishes the row identity

\[
{\bf1}\,(T^4-8T^3+16T^2-12T+2I)=0.
\]

This is a finite exact integer equality, not a numerical eigenvalue approximation: the accompanying standard-library checker constructs every entry and checks every coordinate of the row. Multiplication by subsequent powers of \(T\) and the respective initial column vectors yields for both counting sequences

\[
c_{n+4}=8c_{n+3}-16c_{n+2}+12c_{n+1}-2c_n
\]

whenever the indices are in the stated domains. Directly evaluating the initial vectors gives

\[
\begin{aligned}
(a_4,a_5,a_6,a_7)&=(1390,7592,41452,226316),\\
(d_4,d_5,d_6,d_7)&=(1420,7778,42496,232052).
\end{aligned}
\]

With \(Q(z)=1-8z+16z^2-12z^3+2z^4\), multiplication of the two sequences' generating series by \(Q(z)\) and use of the first four terms yields the first numerator \(1420-3582z+2992z^2-508z^3\) and the difference numerator \(30-54z+36z^2\). This proves both displayed formulas for all \(n\ge4\).

## Verification

The file `verify_triples.py` constructs every state, transfer entry and root vector from the eight possible vertex colors, checks the exact all-seventeen-coordinate row certificate, the fourth-order recurrence through rank twenty-three, and both rational numerators. An **independent route** in the same checker enumerates all ordered three-subset tuples directly using induced connected components (without transfer states) on type \(A_n\) for \(2\le n\le6\) and type \(D_n\) for \(4\le n\le6\). It also verifies the rank-universal ordered commuting-pair numbers \(164,560,1912\) at ranks \(4,5,6\). The exact certificate and the mathematical transfer argument—not any finite truncation of the output sequence—establish the infinite formulas.

## Relationship to prior work

Berenstein, Greenstein and Li, *Hecke monoids, their homomorphisms and parabolicity* (first public version May 10, 2026), provide the idempotent identification, the complete **pairwise compatibility criterion** (Proposition 3.33), homomorphism interpretation of commuting tuples (Corollary 3.35), and the rank-universal **commuting-pair** count (Proposition 3.37). Those are the premise of Step 1, **not** claims of novelty here. The new assertion is the evaluated all-rank ternary type-\(D\) law and the exact rational difference from type \(A\). Xuhua He's 2009 work treats the commutative submonoid of distinguished parabolic products \(w_J^\circ w_I^\circ\), a different object, without an explicit type-\(D\) count of commuting idempotent triples. Related enumeration of triples of predecessor-projection idempotents in classical Catalan transformation monoids is on a different monoid; a coincident path-indexed count does not imply the new branching-graph enumeration.

## Limitations

The result is only for finite Coxeter types \(A_n\) and \(D_n\); no statement is made for arbitrary Coxeter diagrams, higher tuple arities, or conjugacy of tuples. The finite-state identity has a deterministic elementary verification supplied as code rather than a printed \(17\)-by-\(17\) matrix. Originality relies on the inspected literature and available indexed claims; unidentified prior equivalents cannot be excluded. The finding has not been independently audited.

## References

1. A. Berenstein, J. Greenstein, J.-R. Li, *Hecke monoids, their homomorphisms and parabolicity*, arXiv:2605.09761 (first public version 2026-05-10), especially Corollary 2.14, Proposition 3.33, Corollary 3.35, Proposition 3.37. https://arxiv.org/abs/2605.09761
2. X. He, *A subalgebra of 0-Hecke algebra*, arXiv:0904.1786 (2009), Theorem 1. https://arxiv.org/abs/0904.1786
