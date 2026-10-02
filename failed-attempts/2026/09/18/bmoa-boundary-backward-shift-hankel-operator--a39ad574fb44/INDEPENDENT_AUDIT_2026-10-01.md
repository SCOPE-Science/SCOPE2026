# Independent audit — 2026-10-01

## Final claim

The backward-shift orbit-synthesis formula is a Hankel matrix with the classical BMOA boundedness and VMOA compactness thresholds, and the displayed \(H^2\) power-law symbol gives a concrete failure of universal \(H^2\) well-definedness.

## Correctness — PASS

The coefficient identity makes the orbit-synthesis map the Hankel matrix \((\alpha_{j+k})\). Classical Hankel theory gives boundedness at the BMOA threshold and compactness at the VMOA threshold; coordinatewise continuity plus the closed-graph theorem shows that an everywhere-defined map cannot evade boundedness. For \(\alpha_m=(m+1)^{-3/4}\), both input sequences are square-summable while the output coefficients satisfy a constant-times \(j^{-1/2}\) lower bound, so the output is not in \(H^2\); the finite sections also grow like \(N^{1/4}\). The mathematical counterexample and threshold are therefore correct.

## Originality — FAIL

Originality fails for the final mathematical claim. After the elementary coefficient identification, the boundedness and compactness thresholds are direct special cases of classical Nehari--Fefferman/Hartman theory, and the explicit counterexample is a routine witness to being outside that bounded class. The fact that this exposes an error in a very recent preprint is scientifically useful but does not make the underlying theorem original under the required implication-based standard.

### Equivalent formulations

Backward-shift orbit synthesis and the Hankel matrix are equivalent formulations by direct coefficient expansion.

### Broader coverage

The final BMOA/VMOA threshold is a special case of stronger prior theory.

### Exact database or table

The novelty of noticing a new paper's error does not overcome mathematical coverage of the stated operator theorem.

### Claim versus prior implication

Prior stronger theorems mechanically imply the central mathematical conclusion.

### Source inspections

Classical Hankel boundedness/compactness criteria were checked as the dominating prior theorem. The target 2026 preprint was only available at abstract/bibliographic level in this run; that access limitation does not affect the decisive classical-coverage conclusion.

Checked sources: Classical Nehari--Fefferman bounded Hankel operator criterion and Hartman compactness criterion; M. dos Santos Ferreira and J. M. Ribeiro do Carmo, Projections and minimal invariant subspaces in the Hardy space over the bidisk, arXiv:2609.19311v1 (2026); Resultary searches including later 2026-09-19 Hankel/BMOA correction records

Residual risks: The target preprint's full text was not retrievable in this run, so the exact downstream dependency beyond the quoted lemma is not independently re-audited. Later Resultary records independently corroborate the same Hankel obstruction but are subsequent to the assigned record.

## Scientific value — PASS

Identifying that a recently used orbit-synthesis lemma fails on all of \(H^2\), giving an explicit counterexample and pinning the exact regularity boundary is a motivated and useful correction. The value axis passes even though originality fails under the stricter implication standard.

## Conclusion

The finding is scientifically rejected because all three C/O/V axes must pass and originality fails. The correctness and value evidence is preserved.
