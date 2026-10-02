# Exact forced-colouring polynomials of paths

## Status and provenance

The path theorem below is mathematically correct. An independent audit on 29 September 2026 found, however, that its original standalone originality claim must be corrected. The broader SCOPE record

`2026/09/17/forced-three-colouring-max-degree-two--2226d8f07ffd`

was committed at 2026-09-17 23:56:20 UTC and already contains exactly the same path coefficient formula as part of a path-and-cycle maximum-degree-two theorem. This focused path record was committed later, at 2026-09-19 08:44:58 UTC. It is therefore retained as a focused alternate proof and corollary package, not as a separate discovery of the coefficient law.

## Path theorem

For n>=2,
\[
\boxed{FCGP_3(P_n,x)=3\sum_{j=0}^{\lfloor(n-1)/2\rfloor}
2^{n-j-1}\binom{n-1-j}{j}x^{n-j}.}
\]
Equivalently,
\[
\boxed{fcol(P_n,n-j;3)=3\,2^{n-j-1}\binom{n-1-j}{j}.}
\]
Hence
\[
\boxed{FC_3(P_n;p)=3\sum_j 2^{n-j-1}\binom{n-1-j}{j}p^{n-j}(1-3p)^j.}
\]

A successful partial 3-assignment cannot leave an endpoint uncoloured and cannot initially omit adjacent vertices. Thus the omitted set U is an independent subset of the n-2 internal vertices. Writing a proper 3-colouring by its initial colour and edge differences epsilon_i in {+1,-1} subset Z_3, an omitted vertex is forceable exactly when the adjacent differences agree. Because U is independent these constraints are disjoint, so a fixed omitted j-set admits 3*2^(n-1-j) compatible full colourings. There are C(n-1-j,j) possible omitted sets, proving the formula.

## Corollaries retained in this focused record

Writing G_n(x)=FCGP_3(P_n,x),
\[
G_2=6x^2,\quad G_3=6x^2+12x^3,\quad
G_n=2x(G_{n-1}+G_{n-2})\quad(n>=4).
\]
The probability polynomial obeys
\[
F_n=2pF_{n-1}+2p(1-3p)F_{n-2}.
\]
The minimum forcing-domain size is
\[
\boxed{\left\lceil\frac{n+1}{2}\right\rceil,}
\]
with exactly 3t2^t minimum-domain assignments for n=2t and 3*2^t for n=2t+1. At x=1 the total count grows on the exponential scale (1+sqrt(3))^n.

Together with the established lambda=2 and lambda>=4 branches, this determines the forced-colouring function of every path for every positive integer number of colours.

## Correction of the three-vertex display

For P_3=K_{1,2}, direct counting gives six successful assignments with two initially coloured vertices and twelve full proper colourings, so
\[
\boxed{FC_3(P_3;p)=6p^2(1-p).}
\]
This agrees with the earlier SCOPE maximum-degree-two theorem and with the chromatic specialization at p=1/3.

## Verification

Independent enumeration during the audit reproduced the coefficient formula for P_n through n=6. The committed verifier checks further small orders. Finite computation is supporting evidence only.

## Literature context and limitations

Farr and Farr--Morgan supply the general forced-colouring framework and the previously known two-colour/high-colour branches. The central path coefficient theorem is not claimed as a separate September 19 discovery because it already appears in the earlier SCOPE record identified above.

The scientific value of this record is its focused proof and the path-specific recurrence, minimum-domain and growth corollaries. It remains restricted to paths.

## References

1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108 (2026).
2. G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746; Springer (2025).
3. SCOPE record `2026/09/17/forced-three-colouring-max-degree-two--2226d8f07ffd`, committed 2026-09-17 23:56:20 UTC.
