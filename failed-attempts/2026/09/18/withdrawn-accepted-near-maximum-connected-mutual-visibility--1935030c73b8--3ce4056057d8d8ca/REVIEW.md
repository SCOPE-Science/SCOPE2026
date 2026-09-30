# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**Assessment: PASS.**

The near-maximum characterization is exact. If
\(S=V(G)\setminus\{x\}\) is a connected mutual-visibility set, every non-edge
inside \(S\) must use the only outside vertex \(x\) as the internal vertex of its
avoiding geodesic. Hence both endpoints are adjacent to \(x\). This immediately
forces every non-neighbour of \(x\) to be universal in \(G-x\). The converse
reverses the same implication: every non-edge of \(G-x\) then has both endpoints
adjacent to \(x\), so it has the length-two geodesic through \(x\). Connectivity
of \(G-x\) supplies the connectedness requirement.

The complement formulation was checked in both directions. The condition that
every non-neighbour of \(x\) is universal in \(G-x\) is exactly the statement
that every neighbour of \(x\) in \(\overline G\) has no complement-neighbour
other than \(x\), so the complement component containing \(x\) is a star
centered at \(x\).

For the co-connected corollary, a witness for \(\mu_c(G)=n-1\) would force the
connected complement itself to be a star; its complement has an isolated
vertex, contradicting connectedness of \(G\). Thus both \(G\) and \(\overline G\)
have connected mutual-visibility number at most \(n-2\).

The sharpness family was checked structurally. For \(n\ge5\), the graph formed
from \(K_{2,n-3}\) by attaching one leaf has blocks \(K_{2,n-3}\) and \(K_2\),
so the source paper's block theorem and complete-bipartite formula give
\(\mu_c=n-2\). Its complement is \(K_{n-2}\) with a pendant path of length two
attached at a clique vertex; its blocks give the same value. The \(n=4\) case is
\(P_4\), which is self-complementary and has value \(2\).

## Originality

**Assessment: PASS, to the best of our knowledge.**

The directly relevant primary source is Tonny K B and Shikhi M,
*Connected Mutual-Visibility in Graphs*, arXiv:2609.18877 (2026). Its full
available text was inspected. The paper proves the general Nordhaus--Gaddum
bounds \(2n-3\) and \((n-1)(n-2)\), and its proof excludes only the simultaneous
case \((n-1,n-1)\). It does not state the star-component characterization of a
single graph with \(\mu_c=n-1\), nor the sharper bounds under the hypothesis
that both complementary graphs are connected.

Exact and synonymous searches were made for connected mutual visibility with
the terms \(n-1\), near-maximum, co-connected, connected complement, complement
star/star component, Nordhaus--Gaddum, \(2n-4\), and \((n-2)^2\). No source
covering the stated characterization or sharpened bounds was found.

The main residual originality risk is temporal: connected mutual visibility is
a newly introduced parameter and the primary paper is very recent, so parallel
or not-yet-indexed work could exist. No highly relevant inaccessible paper was
identified that specifically threatens the result.

## Value

**Assessment: PASS.**

The result identifies the complete structure immediately below the trivial
maximum of a newly introduced graph invariant. It then converts that structure
into a strict and sharp improvement of both Nordhaus--Gaddum bounds on the
natural class of co-connected graphs. The sharpness construction works for
every order \(n\ge4\), so the improved constants cannot be strengthened under
co-connectedness alone.

## Limitations

- The \(\mu_c=n-2\) level is not characterized.
- Equality cases of the sharpened co-connected inequalities are not classified.
- The result concerns connected mutual visibility, not the classical, total,
  outer, dual, mobile, or game variants.
- Originality is to the best of our knowledge, with residual risk from very
  recent or unindexed parallel work.
- Independent audit has not been performed.
