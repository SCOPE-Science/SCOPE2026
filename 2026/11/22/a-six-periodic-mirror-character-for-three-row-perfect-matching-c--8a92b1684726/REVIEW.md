# Scientific review

## Correctness — PASS
For row interchange, a reflection-invariant face cannot contain a vertical-edge pair because the two edges share a vertex. All remaining selected orbits are independent labels for top/bottom horizontal pairs and middle horizontal edges, with a \(-1\) signed Euler factor for each chosen orbit. A seven-state determinization of the three-row domino transfer counts extendable selections exactly once. The explicitly listed matrix satisfies \(M^8=M^2\), checked by `CHECK.py`, so the signed counts recur for every even strip length; initial values \(0,-1,1,0\) settle all residue classes. The augmented simplicial Lefschetz formula and the independently credited homotopy concentration theorem then prove the homology trace and quotient ranks. The checker also constructs all perfect matchings directly at the first six half-widths and cross-checks the complete invariant-face sums. The argument is all-order, not sample-based.

## Originality — PASS
The full text of Chandrakar–Chau–Goyal–Karki–Subhash, arXiv:2611.18058v1, proves the nonequivariant Fibonacci wedge but not the reflection trace. The closest published full text, *A five-cycle core and signed reflection homology for the three-by-four perfect-matching complex*, proves only the \(n=2\) sign. The eight-column boundary comparison proves finitely many nonequivariant cases, not the periodic equivariant statement. Published ordinary matching-complex reflection results concern different complexes. Search of aliases and reduction routes found no covering theorem. Residual risk: unindexed equivalent work.

## Mathematical value — PASS
The exact mirror character is a natural symmetry invariant not encoded by nonequivariant wedge counts. Its nontrivial period-six sign law gives the complete rational \(C_2\)-module and all positive-degree rational homology of genuine reflection quotients of a natural infinite family, including the first surviving quotient class at \(n=4\). Handling symmetric faces that admit only nonsymmetric tiling extensions is a substantive structural obstacle addressed by the determinized automaton.

## Scope and limitations
Only top/bottom row reflection is treated; the orthogonal reflection, full Klein-four module, integral symmetry lattice and integral quotient homotopy are not classified. The preprint's nonequivariant theorem is an explicitly credited input. An unindexed equivalent priority claim remains possible.

Self-review: passed. Independent audit: not yet performed.
