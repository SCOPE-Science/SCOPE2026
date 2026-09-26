# Independent audit — 2026/09/09/035

Date: 2026-09-26. Disposition: failed; complete original package archived.

## Correctness — FAIL for the stated separation claim

I independently enumerated all 512 binary (3	imes3) matrices and canonicalized under the six simultaneous row/column permutations. The 104 representatives and orbit histogram (4 of size 1, 2 of size 2, 28 of size 3, 70 of size 6) match. For every representative I separately computed the characteristic polynomial by minors and determinant, six traces by integer matrix multiplication, and coefficients of (1/det(I-tA)) by formal division; all 104 stored rows match. There are 32 distinct polynomials and 32 trace sequences.

However, the headline paragraph asserts that “every characteristic-polynomial collision in this window is separated by its trace-sequence.” This is mathematically impossible: Newton identities determine (operatorname{tr}(A^k)) for every (k) from the characteristic polynomial. The stored data itself supplies a counterexample. The zero matrix and the representative with a single entry (a_{32}=1) are nonisomorphic, both have characteristic polynomial (x^3), and both have trace sequence ((0,0,0,0,0,0)). Six distinct nilpotent classes share it, and 14 characteristic-polynomial groups contain multiple state-relabeling classes. Thus the claimed trace separation is false, even though the computed entropy, trace and zeta table is internally correct. Exact trace/zeta formulas cannot distinguish these classes either.

## Originality — PASS, narrowly

OEIS A000595 already counts the 104 unlabelled three-vertex binary relations, and entropy, trace and zeta formulas are classical. The joined 104-row entropy/trace/zeta numerical table and 18-value grouping were not found in the checked prior references. This is a small finite data compilation; the count and formulas are not new.

## Scientific value — PASS for the corrected scope

The exact table can benchmark three-state symbolic-dynamics software and illustrates entropy collisions and the limited discriminating power of zeta data. Its use must exclude the false claim that traces separate equal characteristic polynomials or nonisomorphic presentations. State relabeling is weaker than shift conjugacy, and nilpotent entries use the explicitly stated entropy convention.

## Sources and independent replay

- OEIS A000595, 104 unlabelled binary relations on three points: https://oeis.org/A000595
- Candidate `artifacts/census.json`; independent complete matrix/orbit, characteristic-polynomial, trace and zeta replay above.
- Newton identities: (det(I-tA)=exp(-sum_{kge1}operatorname{tr}(A^k)t^k/k)), which also follows directly by comparing formal logarithmic derivatives. Consequently identical characteristic polynomials give identical full trace sequences.
