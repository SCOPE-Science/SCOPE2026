# Scientific review: weighted perimeter deviation of a disk

## Correctness
**PASS.** The two boundary-measure differences are derived explicitly from the circle arcs cut by each regular-polygon edge and the lengths of its interior and exterior segments. The one-variable derivative has a single minimum with a sharp \(1+\sec(\pi/n)\) threshold; substituting that stationary point gives the exact two-branch formula. The strict-convexity calculation is reduced to a polynomial whose boundary value is \(2s(2-s)(s+1)^2\ge0\) for \(1<s\le2\) and which increases strictly with the weight beyond the threshold. The classical best-nested regular-polygon perimeter inequalities establish the stated unrestricted nonnesting obstruction. The included independent boundary-sampling program passed its tests. Risks: sampling is numerical and cannot replace the universal analytic proof; the endpoint infinite-weight convention must be applied as defined.

## Originality
**PASS, provisional historical priority.** The closest primary source [1] formulates weighted perimeter deviation as an open Dowker-type approximation problem and does not supply a centered regular-polygon profile or crossing phase boundary. Fodor [2] restates Eggleston's nested optimality for the unweighted deviation, corresponding to the already-known \(p=q=2\) subcase, not all weights. Related published geometric findings on projection-shadow distance [3] and weighted area approximation by disk intersections [4] use distinct functionals and do not imply the result. A full mathematical comparison of object, weight, optimizer, and implication was made; older unindexed weighted geometric approximation work remains a priority risk.

## Mathematical value
**PASS.** The theorem provides a complete exact optimization over a natural symmetry family directly motivated by a published open weighted-perimeter question, a sharp parameter-dependent transition, strict convexity for every polygon order, asymptotic constants, and a rigorous implication for the *unrestricted* approximating family: for an explicit range of finite weights no nested polygon can be globally best. Neither an all-polygon optimization nor the unrestricted convexity conjecture is asserted.

## Closest literature and scope
See [1] Basit–Lángi (arXiv:2307.04026, 2023), especially Section 5 Problem 1; [2] Fodor (DOI 10.1007/s00454-021-00291-7, 2021), Introduction and Theorem 1.1; [3] published disk projection-shadow metric result, distinct deviation; [4] published rotational disk-polygon area approximation result, distinct bodies and deviation. Historical priority is best-knowledge rather than independently certified.

Self-review: passed. Independent audit: not yet performed.
