# Exact census of the e=0 alternating 4-tangle Montesinos subfamily at 16-18 crossings, with a proved scale obstruction to pairwise commensurability classification

## Context

The admitted target asks for a complete pairwise-certified PSL(2,C)-commensurability partition of F*, the hyperbolic alternating Montesinos knots with exactly four rational tangles at crossing numbers 16, 17, or 18. Such a partition requires enumerating F* and then deciding every distinct pair with either a rigorous incommensurability certificate or an explicit common finite cover. This record reports the target's own first necessary step, completed as an emergent finding: an exact, cross-validated enumeration of the large normalized e=0 subfamily of F*, and the proved pair-load corollary that blocks the complete pairwise strategy in a single-session pass. No pre-approved fallback existed for this target-only topic, and the finding is judged on its own merits.

## Definitions

- A rational tangle is written canonically as [0;a_1,...,a_k] with all a_i >= 1 and a_k >= 2; its crossing weight is c = a_1 + ... + a_k and its fraction p/q lies in (0,1) with gcd(p,q) = 1.
- The e=0 subfamily means all four tangles are proper fractions in (0,1) under the standard normalization; nonzero-Euler-parameter (e != 0) alternating 4-tangle diagrams are excluded, so counts here lower-bound the full family F*.
- Ordered tuples count ordered 4-tuples of tangles whose weights sum to the crossing number C and whose Montesinos closure is a knot (one component).
- Dihedral-orbit-distinct means distinct up to the D4 row-permutation action (rotation and reversal of the ordered 4-tuple), decided by the exact canonical minimum over the 8 dihedral images of the ordered 4-tuple of fractions.
- The pair load is N(N-1)/2 for N distinct knots, counting the distinct pairs each needing a rigorous certificate under the target contract.

## Result

Theorem (census). Let E(C) be the set of dihedral-orbit-distinct alternating 4-tangle Montesinos knots with Euler parameter e=0 and crossing number C, as defined above. Then |E(16)| = 1900 from 13752 ordered knot tuples, |E(17)| = 5304 from 38784 ordered knot tuples, and |E(18)| = 14022 from 104160 ordered knot tuples, for a total of 21226 distinct knots in the e=0 subfamily alone.

Corollary (scale obstruction). The e=0 subfamily alone determines 21226 x 21225 / 2 = 225260925 distinct pairs. At an optimistic 1 second per rigorous pairwise certificate this is about 7.1 years of compute (about 428 years at 60 s per certificate; about 81 days even with 32-way parallelism at 1 s per pair). Since the full target family F* also includes all nonzero-Euler-parameter alternating 4-tangle diagrams, the true pair count is strictly larger. Hence a complete pairwise-certified commensurability partition of F* is infeasible in any single-session pass and requires a fundamentally different strategy, such as coarse invariants that separate classes without pairwise work.

## Proof and evidence

The enumeration is stdlib-only, exact, and cross-validated; both scripts exit 0 with every self-check passing.

1. Tangle census. All canonical proper rational tangles of crossing weight c are enumerated by integer composition; counts verify exactly 2^(c-2) for every c = 2..12, which covers every tangle that can appear in a 4-tuple summing to C = 16, 17, or 18.
2. Knot-versus-link decision. Each tangle's endpoint pairing is computed by a recursive tangle-arithmetic calculus (integer tangle plus 90-degree rotation plus tangle sum via union-find); the 4-tangle Montesinos closure wiring is then applied and components counted. This is cross-validated against an independent strand model on all twist (pretzel) columns m = 2..14 with zero mismatches in both column pairings and full closure component counts.
3. Pairing theorem check. The computed pairing is verified constant on each (p mod 2, q mod 2) parity class of the fraction p/q; exactly the three coprime parity classes occur.
4. Orbit reduction. Distinctness is decided by exact canonical representatives (minimum over the 8 dihedral images). Because the Bonahon/Boileau-Siebenmann classification gives fiber at most 8, ordered-knot-tuples / 8 is already a rigorous lower bound; the exact canonical computation tightens it to the stated orbit counts.
5. Reproduction. Run `python3 artifacts/census_scratch.py` for the ordered-tuple census and all self-checks, then `python3 artifacts/orbits_scratch.py` for the exact dihedral-orbit reduction and pair-load arithmetic. Both require only the Python 3 standard library and run in minutes. The independent audit re-executed both scripts and reproduced every headline number exactly.

## Limitations

- The count covers the e=0 subfamily only; nonzero-Euler-parameter diagrams and non-alternating projections are excluded, so 21226 lower-bounds |F*|.
- The census counts distinct Montesinos diagrams up to dihedral symmetry; residual diagram duplication (for example flypes or tangle identities beyond D4) can only merge orbits, and the fiber bound caps merging at a factor of 8, so the pair-load conclusion is robust: even collapsing by the maximum factor leaves at least 19587 knots and over 1.9e8 pairs.
- No hyperbolic invariant (canonical cellulation, cusp field or shape, Bloch invariant, cusp density, horoball symmetry) and no commensurability certificate for any pair is claimed; the finding is combinatorial, and its commensurability content is the proved scale of the target problem.
- Twist-only (pretzel) subfamily note: at even crossing numbers no twist 4-tuple closes to a knot (all-even parity gives links), consistent with zero twist-knot tuples at C = 16, 18 and 80 at C = 17.

## Reproducibility

Artifacts: `artifacts/census_scratch.py`, `artifacts/orbits_scratch.py`, `artifacts/census_result.json`. Commands:

```
python3 artifacts/census_scratch.py
python3 artifacts/orbits_scratch.py
```

## References

- F. Bonahon and L. Siebenmann, New geometric splittings of classical knots and the classification and symmetries of arborescent knots (Montesinos classification; fiber bound for diagram redundancy).
- O. Goodman, D. Heard, and C. Hodgson, commensurability census of Montesinos knots and cusped census manifolds to 12 crossings (the prior census this window lies beyond).
- W. Reid and G. Walsh, and A. Macasieb and T. Mattman, infinite commensurable families of knot complements (family results distinct from this crossing-window census).
- A. Hatcher and U. Oertel, Boundary slopes for Montesinos knots (background Montesinos theory).
- J. Hoste, M. Thistlethwaite, and J. Weeks, the Hoste-Thistlethwaite-Weeks prime knot tables (general tables to 16 crossings, without this Montesinos orbit partition).
- M. Boileau and B. Zimmermann, Symmetries of nonelliptic Montesinos links (symmetry background; lists to 10 crossings).
- SnapPy census interfaces and the Melbourne Snap commensurability data pages (official databases consulted; knot-complement commensurability tables stop at 12 crossings).
