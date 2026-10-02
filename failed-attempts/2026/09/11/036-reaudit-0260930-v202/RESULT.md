# Explicit 9-vertex 3-uniform clutter with (τ, ν, reg_Q) = (4, 1, 4)

## Object

Let H be the 3-uniform clutter on vertices {0,...,8} with edges

```text
025 026 127 134 145 158 234 257 367 368 468 478 568 678
```

where, for example, `025` denotes `{0,2,5}`. Let `I(H)` be its squarefree edge ideal. Here `τ(H)` is the vertex-cover number. For `ν(H)` we use the record's explicit induced-matching convention: a pair of disjoint edges is not induced when their union contains a third edge of H. Regularity means `reg_Q(R/I(H))`.

## Exact result

The tuple is

`(τ(H), ν(H), reg_Q(R/I(H))) = (4, 1, 4)`.

This is an explicit finite witness separating the induced-matching lower bound from rational regularity. No extremality or minimality claim is made.

## Certificate

- `τ=4`: `{0,4,7,8}` is a cover. Exhaustion of all 84 three-subsets finds no 3-cover.
- `ν=1`: there are 25 disjoint edge pairs; for every one, a third edge lies inside the six-vertex union. Thus no induced matching of size 2 exists, while any single edge gives `ν>=1`.
- `reg_Q=4`: Hochster's formula is evaluated over Q for every one of the 512 induced vertex sets. The only nonzero reduced H_3 witnesses are masks `511={0,1,2,3,4,5,6,7,8}` and `383={0,1,2,3,4,5,6,8}`, each of dimension 1. No induced subcomplex has reduced homology in dimension >=4. The resulting nonzero Betti entries are

```text
(1,2)=14  (2,2)=15  (2,3)=27  (3,2)=4  (3,3)=47
(4,2)=1   (4,3)=24  (4,4)=1   (5,3)=3  (5,4)=1
```

so `reg=max(j)=4` in the `(i,j)` convention used by the artifacts.

## Reproducibility

The committed exact-rational scripts and certificates independently encode the same edge set and Hochster calculation. An external audit re-enumerated covers, all disjoint pairs, all 512 induced independence complexes, and rational boundary-matrix ranks from scratch.

## Scope and limitations

The result is a single explicit 3-uniform clutter. It does not establish that 9 vertices are minimal, that `(4,1,4)` is extremal in any classification, or that the same regularity holds in every characteristic. The earlier package used the word “extremal” without a proved extremality theorem and its slogan misidentified mask 383 by replacing vertex 6 with vertex 7; both presentation defects are corrected here.

## References

- Hochster's formula for squarefree monomial ideals / Stanley–Reisner rings.
- D. Bolognini, A. Macchia, F. Strazzanti, V. Welker, *Powers of monomial ideals with characteristic-dependent Betti numbers*, arXiv:2201.00571.
