# Scientific review: The nine-point counting-logic threshold for two commuting idempotent maps

## Correctness — PASS

The decomposition into fibers of the common idempotent \(h=fg=gf\) follows directly from the two named idempotence laws. Every fiber has a canonical common fixed point, \(p\) other \(f\)-fixed points, \(q\) other \(g\)-fixed points, and a nonnegative integer matrix recording the complete multiplicity of each remaining point type. Every such matrix defines commuting idempotents; its isomorphisms are precisely independent permutations of the positive-index rows and columns and swaps within the cells. Unordered multisets of fibers therefore classify all structures without omission. The exact verifier enumerates all these representatives through nine points, uses the complete directed binary atomic types in a *shared* palette for full \(C^2\) refinement, and checks exact counts at all sizes; independently, a labeled brute-force program agrees through six points and independently checks isomorphism-orbit counts through five. The explicit nonisomorphic nine-point pair is checked by all \(9!\) bijections and by its logical invariant. Standard finite-model-theory equivalence of \(C^2\) and full relational counting refinement is supplied by Kiefer–Schweitzer–Selman [1]. A reproducible computer census is a finite proof only insofar as the complete generator and code can be checked; it is not formal or independent certification.

## Originality — PASS (with residual priority risk)

The closest general logic source is Kiefer–Schweitzer–Selman [1], especially the definitions of \(C^2\) and full color refinement and classification of structures identified *absolutely* by counting logic. The specific first collision order and number of exceptional pairs within the commuting-idempotent transformation variety are not stated in the inspected material and are not obtained merely by applying an absolute-identification theorem. Dolinka–East [2] studies semigroup variants and idempotent transformations but not this finite-model-theory threshold. Actual semantic database searches covered commuting projections, two unary transformations, aliases involving bipartite incidence matrices, and first logical collisions; no dominating entry was returned. The archive of accessible earlier results was checked for overlapping claims. Lack of a retrieved covering result is not proof of historical uniqueness: a less-indexed finite automata or semilattice-action census could still subsume the claim.

## Mathematical value — PASS

The finding answers the natural exact question of how much weakening from arbitrary two-map transition systems to **two commuting retractions** postpones the first failure of \(C^2\)-identification. It produces an entire complete finite classification to the sharp obstruction, not a parameter-renamed exercise. The unique obstruction has a transparent structural explanation: two doubled opposite cells versus four single incidence cells; both have matching local counts but different global incidence. The normal form and full counting atomic-type treatment are reusable in higher-order classifications. No claim of a paper-sized downstream theorem is needed.

## Boundaries and comparison

The theorem does not apply to binary relation pairs that fail totality/idempotence/commutation, to the language with genuine function symbols, or to orders above nine. Two-map arbitrary-system collisions at five points do not cover or imply the new *commuting idempotent* subclass threshold of nine. Priority outside inspected material remains a risk, and all verification was carried out without an independent audit.

## References

[1] S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792v1, 2015-03-30, §§2–3 and §5, https://arxiv.org/abs/1503.08792.

[2] I. Dolinka, J. East, *Variants of finite full transformation semigroups*, arXiv:1410.5253v1, 2014-10-20, https://arxiv.org/abs/1410.5253.

Self-review: passed. Independent audit: not yet performed.
