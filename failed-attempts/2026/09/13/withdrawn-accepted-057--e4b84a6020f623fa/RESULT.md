# Rank-3 ordinary Drinfeld volcano obstruction: split cubic orders branch, with a certified double-neighbour vertex

## Context

For elliptic curves and rank-2 Drinfeld modules, ordinary l-isogeny components are classical volcanoes: quadratic endomorphism orders form a chain over l, so each vertex below the crater has at most one ascending edge. The target asked whether the same law holds for ordinary rank-3 non-CM Drinfeld modules. This record reports the verified emergent obstruction found on that attack path: the order-theoretic uniqueness mechanism already fails for cubic orders, plus an explicit ordinary rank-3 vertex with two distinct rational l-neighbours.

## Definitions

Let A = F_2[T], l = T^2+T+1 (monic prime of degree 2, residue field A/l = F_4), and L = GF(4) = F_2[z]/(z^2+z+1) of A-characteristic P = (T) via gamma(T) = 0. A rank-3 Drinfeld module is given by phi_T = gamma(T) + g_1 tau + g_2 tau^2 + g_3 tau^3 with g_3 != 0; it is ordinary iff its height is 1, i.e. g_1 != 0. An l-neighbour of phi is a quotient psi = phi/D by a monic quadratic right divisor D of phi_l in the Ore ring L{tau}, satisfying the Velu identity D * phi_T = psi_T * D (Ore multiplication). For the order model, let K be a split cubic algebra with O_K/lO_K = F_4^3 and O/lO_K equal to the diagonal F_4; intermediate over-orders of index N(l) = 4 correspond to 16-element (F_2-dimension 4) subrings W with diagonal F_4 <= W <= F_4^3 that are stable under diagonal multiplication.

## Result

(a) Branching lemma. The split cubic order model admits exactly three distinct minimal over-orders of index N(l) = 4, explicitly listed in the certificate, with zero smaller (size-8) intermediates; hence all three are minimal. Each is a partial diagonal: {(a,a,*)} , {(a,*,a)}, {(*,a,a)} over a in F_4 in the respective free coordinate.

(b) Double-neighbour witness. The ordinary rank-3 module phi_T = tau^3 + z tau^2 + z^2 tau over GF(4) (coefficient vector T = [0,1,2,1], z^2+z+1 = 0, g_1 = 1 != 0) has exactly two distinct rational l-isogeny neighbours with Velu-verified quotients: D_1 = tau^2+1 -> psi^(1)_T = [0,1,2,1], and D_2 = tau^2+z^2 tau+1 -> psi^(2)_T = [0,1,3,1] with the stated j-pairs. The full 48-module census over GF(4) with g_3 != 0 gives rational-neighbour distribution {0: 18, 1: 24, 2: 6}.

(c) Mechanism reading. The triple branching falsifies the unique-minimal-over-order mechanism on which any classical rank-3 volcano law must rest: a module with End = O would have three ascending directions, not at most one.

## Proof / evidence

Order count: exhaustive enumeration over all 64^2 generator pairs in F_4^3 with componentwise subring-closure checks, F_4-stability checks, and a minimality check confirming no size-8 subring intermediate; independently re-verified from scratch (0 size-8, 3 size-16 rings, element-for-element match with the certificate). Neighbour census: enumeration over all 48 modules, Ore right-division remainder test of phi_l by every monic quadratic D, brute-force Velu solve over GF(4)^3 with the asserted identity omul(D,T) == omul(P,D); independently re-verified (same distribution, same example, both identities hold). Ordinariness is by height (g_1 = 1 != 0 at P = (T)).

## Limitations

Ascending-ness of the two explicit neighbours is not certified: no computed inclusions End(phi) < End(psi_i) with conductor valuations, and no realization of O = A + l O_K as End(phi) via Honda-Tate/Yu theory. The over-order count is proved in the split-residue local model, not as a global endomorphism-ring computation. Ordinariness is by height without full Frobenius Weil-number or CM-discriminant checks. The record therefore claims the branching lemma plus the double-neighbour witness and the mechanism reading, not a fully certified TARGET counterexample with crater/depth numbers.

## Reproducibility

Pure-Python stdlib scripts only. The consolidation script regenerates the neighbour census and order data; the JSON certificates record the explicit rings and the example quotients. An independent stdlib re-enumeration reproduces the size-8/size-16 counts and both Velu identities deterministically.

## References

- Chien-Hua Chen, CM Drinfeld Modules, Self-isogenous Modular Polynomials, and Volcano Structure, arXiv:2511.21329 (2025): nearest prior work; its unique-ascent theorem is restricted to CM modules in the uniform-level subgraph, and its T^2+T+1 material concerns modular-polynomial bounds, not this order lattice or vertex.
- Caranay, Computing Isogeny Volcanoes of Rank Two Drinfeld Modules, Univ. of Calgary thesis (2018): rank-2 volcano scope whose chain mechanism contrasts with the cubic branching proved here.
- Certificates: overorders_F4.json (n_size8 = 0, n_size16 = 3, n_minimal = 3 with explicit 16-element rings); consolidation.json (48-module census {0:18, 1:24, 2:6} and the example vertex with two Velu quotients).
