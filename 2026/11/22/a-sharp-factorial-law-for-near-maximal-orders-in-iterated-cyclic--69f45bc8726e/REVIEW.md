# Review of the sharp fixed-defect extreme-order law

## Correctness — PASS
The semidirect-product order rule gives the exact finite-depth CDF recursion, including nonidentity top rotations and the identity boundary. The fixed-defect complement recurrence is then exact. The key bound \(B_p(x)=x+O_p(x^2)\) is uniform on \([0,1]\), so summing its normalized errors is justified by geometric convergence, and the induction yields the claimed sharp factorial coefficient. Actual exhaustive permutation-order checks matched the recurrence over all cited finite groups. The numerical large-depth check is not treated as an infinite proof.

## Originality — PASS, qualified
The 2002 Abért–Virág full text concerns the typical-order exponent and bounded-variance asymptotics; its branching-random-walk framework is acknowledged. The Schlage-Puchta full text gives a distinct conjugacy-class sampling law and cites the typical-element result. Pólya's cycle-index composition formula, reproduced in Renteln (2024), determines every finite order count in principle; those counts and their immediate recursion are explicitly excluded as claims of novelty. The surviving contribution is the sharp fixed-defect factorial prefactor as depth grows, which requires separate rare-tail analysis and is not displayed in the inspected results. Priority risk: an equivalent higher-order asymptotic may exist in earlier probability/group literature or could be extracted from the general cycle index.

## Value — PASS
Element-order frequencies in Sylow groups are natural invariants of finite groups. The proven factorial hierarchy describes a highly atypical near-exponent region where the known typical-order law gives no sharp scale, and it quantifies how successive extreme orders become polynomially more common while their total proportions remain exponentially small. The all-fixed-defects theorem spans every prime and unbounded wreath depth; it is not an isolated small-group computation.

Self-review: passed. Independent audit: not yet performed.
