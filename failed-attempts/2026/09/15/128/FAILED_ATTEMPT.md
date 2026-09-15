# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This record documents an unsuccessful SCOPE investigation. Its proposed claim
> is not an established finding and must not be cited as one.

## Attempt

- **Title:** Boij-Soderberg decomposition and cone-membership classification for multigraded Betti tables of toric edge ideals of complete bipartite graphs
- **Round:** 2026-09-14-hands-on-first-light-01
- **Lane:** 20373
- **Disposition:** NO_RESULT
- **Domain:** Commutative Algebra
- **Method:** Boij-Soderberg decomposition and combinatorial commutative algebra

## Problem

Let m<=n, S_{m,n}=k[e_{ij}: 1<=i<=m, 1<=j<=n] with standard Z-grading, and let I_{K_{m,n}}=ker(k[e_{ij}]->k[x_i,y_j], e_{ij}|->x_i y_j) be the toric edge ideal of the complete bipartite graph K_{m,n}, i.e. the ideal of 2x2 minors of the generic m x n matrix. Equip S_{m,n} with the fine Z^m+Z^n-grading deg(e_{ij})=(u_i,v_j). Determine for every (m,n): (i) the exact set of degree sequences delta with nonzero coefficient a_delta in the Boij-Soderberg decomposition beta(S_{m,n}/I_{K_{m,n}})=sum_delta a_delta pi_delta; (ii) a closed combinatorial formula for each a_delta as a function of (m,n); (iii) the minimal face of the Boij-Soderberg cone containing beta(S_{m,n}/I_{K_{m,n}}) as (m,n) vary; (iv) the fine-graded Betti numbers beta_{i,a}(S_{m,n}/I_{K_{m,n}}) and how their Z-graded collapses distribute across the pure summands pi_delta in (i).

## Attempted claim

Let m<=n, S_{m,n}=k[e_{ij}: 1<=i<=m, 1<=j<=n] with standard Z-grading, and let I_{K_{m,n}}=ker(k[e_{ij}]->k[x_i,y_j], e_{ij}|->x_i y_j) be the toric edge ideal of the complete bipartite graph K_{m,n}, i.e. the ideal of 2x2 minors of the generic m x n matrix. Equip S_{m,n} with the fine Z^m+Z^n-grading deg(e_{ij})=(u_i,v_j). Determine for every (m,n): (i) the exact set of degree sequences delta with nonzero coefficient a_delta in the Boij-Soderberg decomposition beta(S_{m,n}/I_{K_{m,n}})=sum_delta a_delta pi_delta; (ii) a closed combinatorial formula for each a_delta as a function of (m,n); (iii) the minimal face of the Boij-Soderberg cone containing beta(S_{m,n}/I_{K_{m,n}}) as (m,n) vary; (iv) the fine-graded Betti numbers beta_{i,a}(S_{m,n}/I_{K_{m,n}}) and how their Z-graded collapses distribute across the pure summands pi_delta in (i).

## Research outcome

Target blocked on parts (ii) and (iv): greedy elimination over Lascoux tables has no uniform closure and fine-graded fibers are wild contingency enumerations. Attempted routes (Hilbert regularity window, m=2 Eagon-Northcott peeling, Lascoux symbolic elimination, toric fiber homology) match target_exit.json; CLEAN_EXIT with no emergent finding.

## Why this attempt failed

Failed axes: no independent audit (NO_RESULT).

No complete classification is claimed: general-m Boij-Soderberg support and coefficient formulas, the varying minimal cone face, and fine-graded Betti numbers with their distribution across pure summands all remain open. Evidence is limited to the classical m=2 Eagon-Northcott subcase and small-case Hilbert-numerator and chain-count numerics in output/artifacts/.

## Conditions for a legitimate retry

introduce a materially new method or a justified, still-valuable revised claim; address the recorded limitation: No complete classification is claimed: general-m Boij-Soderberg support and coefficient formulas, the varying minimal cone face, and fine-graded Betti numbers with their distribution across pure summands all remain open. Evidence is limited to the classical m=2 Eagon-Northcott subcase and small-case Hilbert-numerator and chain-count numerics in output/artifacts/.

## Epistemic status

This is negative research memory, retained to prevent accidental repetition and
to make future recovery attempts more informed. It is intentionally segregated
from validated SCOPE findings. Similarity to this record is not a permanent ban:
a future attempt may proceed only when it records a material change that addresses
the failure above.
