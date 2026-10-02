# Independent mathematical audit — SCOPE-20260919-7d98f252f0ca

Final disposition: **FAILED**.

## Correctness
**PASS** — The second-order asymptotics are mathematically consistent. In logarithmic radius, normalizing by the common leading power yields an exact equation whose linear part is \(eta y_t+y\) and whose diffusion forcing is \(C_0e^{-qt}\). The primary source's center-manifold system was inspected on the relevant pages and supplies the two stable decay rates corresponding to \(q=L/(p-1)\) and \(h=L/(m-p)=1/eta\). Variation of constants therefore gives the universal forced term when \(q<h\), a \(t e^{-qt}\) resonance when \(q=h\), and the profile-dependent homogeneous mode when \(h<q\). The coefficient \(m r(mr-N+2)\) is exactly the radial Laplacian coefficient, so the harmonic cancellation surface is correct.

## Originality
**FAIL** — A published September 18 record, 'A resonance at m = 2p - 1 controls second-order tails in weighted porous-medium self-similarity', was read in full and states the same three regimes, the same coefficient, the same logarithmic resonance, and the same harmonic cancellation surface for the same Iagar-Munteanu profiles. The assigned September 19 theorem is therefore exact prior duplication, not a new refinement.

### Equivalent formulations
After aligning notation, the two resonance trichotomies and coefficients coincide.

### Broader coverage
The September 18 published theorem strictly covers the September 19 final claim.

### Exact database or table
The exact prior theorem is decisive; no negative database inference is needed.

### Claim versus prior implication
The assigned theorem is fully implied, not merely a special case.

## Value
**FAIL** — The resonance classification itself is mathematically worthwhile, but this assigned record adds no independent scientific value because the identical theorem and mechanism were already published the previous day. Repackaging notation and adding the observation that the harmonic leading power is itself an exact singular solution do not create a distinct motivated result.

## Source inspections
- **A resonance at m = 2p - 1 controls second-order tails in weighted porous-medium self-similarity** (https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-resonant-tail-corrections-weighted-porous-medium--92071aab7bff): complete RESULT.md. Assessment: EXACT_PRIOR_COVERAGE. Evidence: It states the same forced, resonant, and homogeneous-mode regimes and the same radial-harmonic cancellation.
- **A porous medium equation with dominating weighted absorption: three types of self-similar solutions** (https://arxiv.org/abs/2609.20397): complete primary PDF was available; pages 12-13 were visually inspected for the reduced stable-node system and tail recovery. Assessment: PRIMARY_SHARED_INPUT. Evidence: The source establishes the universal leading tail and shows the relevant reduced system is a stable node; it does not rescue originality against the earlier exact SCOPE theorem.

## Residual risks
- No correctness defect is asserted; rejection is exact prior coverage.
