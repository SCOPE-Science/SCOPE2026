# Explicit Borromean Rédei triple {5,29,181} with a hand-checkable Frobenius certificate

## Context

Rédei triple symbols give an arithmetic analogue of triple linking. This repaired record certifies one explicit triple, {5,29,181}. It does not claim that the triple is new in the literature, that it is smallest under any ordering, or that an exhaustive census below 5000 has been completed.

## Result

The primes 5, 29, and 181 are all 1 mod 4 and have pairwise Legendre symbols +1. For the normalized Rédei extension attached to the base pair (5,29), the symbol [5,29,181] is -1. Rédei reciprocity gives the same value in all permutations. Thus {5,29,181} is an explicit Borromean Rédei triple in the standard sense; in the restricted arithmetic-topology Galois setting where the Rédei/Massey correspondence applies, the associated triple invariant is nontrivial.

## Certificate

For (5,29), (x,y,z)=(7,2,1) satisfies

7^2 - 5*2^2 - 29*1^2 = 0,

y is even, x-y=5=1 mod 4, and beta=7+2*sqrt(5) has norm 29 and is totally positive. If t^2=beta then t has polynomial

f(T)=T^4-14T^2+29.

Modulo 3, f is irreducible. To distinguish the dihedral case from a cyclic quartic possibility, note the explicit factorization

f(T)=(T-2)(T+2)(T^2+1) mod 11.

The quadratic factor is irreducible mod 11, so the Frobenius cycle type is 1+1+2. Such a transposition-type cycle does not occur in a cyclic C4 subgroup acting on four roots; together with irreducibility and the reducible cubic resolvent this identifies the splitting group as D4.

At 181, 27^2=5 mod 181. The two conjugates of beta reduce to 61 and 134, and

61^90 = 134^90 = -1 mod 181.

Hence the primes over 181 are inert in the quadratic step of the Rédei extension and [5,29,181]=-1. The normalized conic solutions (11,2,1) for (29,5) and (35,6,1) for (29,181) supply independent reciprocity/order cross-checks.

## Repair of the original record

The original package called the example “new” and “the smallest below 5000” while simultaneously disclaiming a completed certified census; its supplied search script did not reproduce the claimed census totals. Those claims have been withdrawn. The original Galois-group proof also said that a nonsquare quartic discriminant excludes C4, which is not a valid distinction; the mod-11 factorization above repairs that step.

## Originality boundary

Published arithmetic-topology literature contains other explicit Borromean prime triples, for example (5,41,61), and general theory/density results explain how such examples arise. A targeted exact-triple search did not locate {5,29,181}, but this repair does not infer or advertise novelty from that absence. Its validated content is the explicit, reproducible symbol certificate.

## Limitations

No exhaustive search below 5000 is claimed. The Rédei-symbol-to-Massey interpretation relies on the cited restricted Galois-group theory; this record certifies the arithmetic symbol directly and uses that theory for the cohomological interpretation.

## Reproducibility

Run `python3 artifacts/redei_search.py`. The repaired script checks the pairwise Legendre conditions, normalized conic, mod-3 irreducibility, the mod-11 D4-vs-C4 witness, and the Frobenius computation at 181. `artifacts/certificate.json` records the same finite data without unsupported scan totals.

## References

- J. Gärtner, Rédei symbols and arithmetical mild pro-2-groups, arXiv:1303.2608.
- Y. Ishida, A. Kuramoto, D. Zheng, The Density of Borromean Primes, arXiv:2403.17957.
- D. Vogel, dissertation examples on Rédei symbols and Borromean primes (including the explicit triple (5,41,61)), https://d-nb.info/970188277/34.
