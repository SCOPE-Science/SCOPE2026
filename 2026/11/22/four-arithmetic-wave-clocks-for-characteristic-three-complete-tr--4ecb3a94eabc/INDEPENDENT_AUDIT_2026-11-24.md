# Independent mathematical audit

## correctness

PASS

Partwise summation S is surjective and replication U injective for all positive sizes; with D=SU, A=UMS gives rank 3 and rank(A^j)=rank((DM)^(j−1)) because M is invertible in characteristic three. For zero or one nonzero residue this gives zero Jordan lengths (2,2,2) or (3,2); for two it gives one zero length-2 block and the two simple roots of x²−ab. The other zero blocks are singletons. For three nonzero residues the constant sector has cubic x³−(ab+ac+bc)x−2abc, with lengths 2,1 at the repeated eigenvalue for 111/222 and simple linear/quadratic factors for 112/122. On a cyclic adjacency block of length s, T+T⁻¹ applies A to both layers, and a block generator and its inverse time-shift generate both layers. Thus the cyclic wave annihilator is (z²−λz+1)^s, with one doubled block in the resonant case. Its roots have orders 4, 1/2, 8, 10 or 5 as appropriate. At a root occurring in z^k−1 the multiplicity is 3^ν₃(k); taking gcd degrees gives the table, and the lcm gives the periods. The triangle alone has no order-four sector in the 111 class and has order 9. For K_{1,1,2}, exact period 60 requires the nonzero order-four sector, a nonfixed length-2 block at 1, and the nonzero order-ten sector, so (9−1)(9−3)(81−1)=3840 states or 64 orbits over F₃. Möbius inversion gives the rest. The proof table's so-called elementary divisors should be read as cyclic sector factors, split further into primary factors as needed: z⁴+1 is already reducible over F₃, and other factors can split over extensions. This nomenclature does not affect the Finding. The independent direct matrix replay /workspace/branches/2a805a18-707c-4808-a967-3b804978220b/direct_tripartite_check.py passed 6,720 comparisons (56 size triples and times 1–120), order checks, and direct enumeration for K_{1,1,1} and K_{1,1,2}. That is finite corroboration; the factorization and multiplicity proof give the all-size, all-extension result. The frozen verification note and both supplied scripts were inspected, not executed.

## originality

PASS

Pass for the complete characteristic-three tripartite residue classification and exact orbit census, not for its update rule or its previously covered examples. The K_{1,1,2} check, including 64 period-sixty orbits, is exactly the K₄ minus one edge example of Resultary b56c5a6d84e7; the triangle is covered by 13302e527b48. The nearest broader graph-family record addc32219e63 is in characteristic two. The bipartite ternary law and edge-defect laws do not provide the nilpotent ranks and cyclotomic sectors across three arbitrary positive part sizes. The complete-multipartite characteristic polynomial alone does not determine the required modular block lengths.

## value

PASS

A natural next family after bipartite graphs exhibits qualitative changes that a list of adjacency eigenvalues misses. The result explains which congruence patterns give 24, 36 and 60 steps through root orders and modular block lengths, and determines all shorter orbit populations over every finite field of characteristic three. This makes the complete classification and not merely the known period-sixty witness a usable exact benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
