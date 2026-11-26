# Independent mathematical audit

## correctness

PASS

RESULT.md lines 5–60: on sorting a triple, the middle absolute deviation is the smaller successive gap, hence in input-edge coordinates it is min(|s|,|t|,|s+t|). Each section is 1-Lipschitz. Varying one internal edge by epsilon changes at most the two incident output entries, by magnitudes at most |epsilon| each. Their adjacent differences have weights v[j-2], v[j-1], v[j] and bounds |epsilon|, 2|epsilon|, |epsilon|. Edge-coordinate telescoping proves the bound for arbitrary real pairs including ties, and a constant input difference changes no MAD. For (d[j-1],d[j],d[j+1])=(-3/2,1,-3), direct evaluation gives changes -epsilon,+epsilon for 0<epsilon<1/2, attaining all three bounds simultaneously; (1,3) on the first edge and its reflection give the stated boundary columns. These perturbations integrate to actual single-step changes of the signal. A single output at n=3 has zero variation. The largest unit-weight columns are 2, 3 and 4 for n=4, n=5, and n>=6. Exact independent replay: python3 -I /workspace/review-work/replay.py 1 evaluated MAD directly for 92,750 step pairs (n=3–6) and recovered every maximum column variation for the tested weight profiles. This is finite corroboration only. The supplied checker was inspected, not executed; in particular line 76 uses a nonzero float tolerance despite rational witness quotients. The exact analytic witnesses do not depend on that tolerance.

## originality

PASS

The supported distinction is the sharp two-input seminorm coefficient for the full-window three-sample minimum-gap scale with independently weighted input/output edges, not MAD itself, Hampel filtering, or the general use of step-column bounds. The closest catalogued filters and primary moving-MAD leads do not show equivalent coverage of this claim in the material available. No claim of historical priority is made.

## value

PASS

The worst-case change of a classical local robust scale is a useful error-propagation invariant distinct from the statistical robustness of each window. The formula gives both a sharp decision under arbitrary edge weighting and explicit witnesses that distinguish genuine amplification from an artifact of separate scalar bounds. The onset at four input samples and ceiling at six or more arise from how neighboring output windows share edges. No extension to general MAD windows or to the replacement filter is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
