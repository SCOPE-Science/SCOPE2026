# Independent mathematical audit

## correctness

PASS

The partials of the specified quartic cannot vanish projectively at a point with a zero coordinate; at a point with nonzero coordinates their product comparison gives 1=−27 (characteristic 3 also has no such zero). Thus the model is smooth in the stated range. S preserves F by the three weight congruences, T cyclically permutes its terms, and F restricted to X+Y+Z=0 is −(X²+XY+Y²)². Recomputed U's pullback and determinant over Q[z]/Φ7, then built the 28 integral normalized rows from four seeds using S and cyclic rotation, without running the supplied verifier. Independently tested all rows by the quartic coefficient equations. Exact substitutions z↦z^k gave fixed counts (28,1,1,1,1,4); the cyclic subgroup lattice forces orbit sizes 1,3,6,6,6,6. The row (1,z^3,z) forces the common field to be Q(z); the length-three points have precisely the real cubic field. Recomputed all 378 pair norm gcds and residue common-polynomial gcds: only p=2 and p=7 have any collisions (84 and 231 pairs); 29,43,71, the other candidates, do not. In the good range U remains invertible, the initial square and pullbacks persist, and 28 distinct lines exhaust the odd-theta bitangents. The cyclotomic Frobenius then yields exactly the claimed rational-line counts. Equidistribution uses the prime number theorem in arithmetic progressions for the stated natural densities relative to primes, not merely infinitude in each progression. An independent direct count at eleven primes confirmed the three cases; it tests a scalar multiple of a square, not whether the leading scalar is itself a square in the ground field.

## originality

FAIL

Elkies's earlier exact description of both the bitangent set and the coefficient Galois action mechanically gives the frozen arithmetic law in the same rational model. He identifies each bitangent Galois-equivariantly with a Sylow 3-subgroup of G=PSL2(F7), and gives the cyclotomic Galois action on G in the Klein model: σ_k sends the 7-cycle g to g^k and fixes the order-three normalizer generator h. With g a translation and h a nontrivial dilation on P¹(F7), the corresponding element of Aut(G)=PGL2(F7) must centralize h, hence is diagonal, and conjugating g to g^k forces the dilation x↦kx. Each Sylow 3-subgroup has an unordered pair of distinct F7 eigenpoints, giving the equivariant bijection with the 28 two-subsets of P¹(F7). The dilation has just two fixed points for k≠1, 0 and ∞, and admits a two-cycle only when k=−1, when there are three such pairs. Thus the fixed-point law, orbit sizes and faithfulness are immediate; individual fields follow from stabilizers. Smooth odd-characteristic specialization preserves the bitangents and their Frobenius action by the standard theta-characteristic correspondence and étaleness of Jacobian 2-torsion. Smoothness for this fixed model is just the displayed Jacobian check. The later indexed all-prime classification is an exact dominating overlap but is not treated as earlier on the evidence of its date. The decisive historical evidence is Elkies's actual statements, not that later record or the known real count alone.

## value

FAIL

The arithmetic invariant is natural and the integral calculation credible, but the frozen field classifications and prime count law extract fixed pairs directly from the known Galois-equivariant Klein construction. Good odd specialization is standard. No independent new invariant or mathematically necessary additional case analysis remains; an exact orbit and norm computation is a reproducible alternate derivation, not by itself an advance over that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
