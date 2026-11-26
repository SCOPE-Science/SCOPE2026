---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The principal-minor expansion of det(nI-J+t diag(z)) gives each nonempty root-set multiplicity k n^(n-k-1), including the empty determinant at k=n. Inserting Boolean signs and expanding the rank-one term gives exactly the three multiplier formulas without division by n-t. At t=n the terms at weights 0 and 1 survive, so the rank is n+1, including n=2. Off that activity only the linear factor in a middle shell can vanish, precisely at t=n-2j with binomial nullity. At t=1, putting a=n-1 and b=n+1, the magnitudes decrease on the positive branch (with the top at weight zero). On the negative branch the ratio is (d+2)a/(db) with d=2s+1-n>0; it is >=1 up to the terminal step since d<=a, and the terminal boundary has equal magnitude. The first negative shell beats the last positive middle shell by a/b (even) or (a/b)^2 (odd). The small cases have weight spectra (3,-1,-1) and (16,0,-4,-4), agreeing with the claimed gaps. The positive total mass is the maximum magnitude by the triangle inequality. Orthogonal Walsh diagonalization gives the inverse or pseudoinverse norm and restricted condition number. The supplied check_root_spectrum.py was inspected, not executed; python3 check_root_spectrum.py replays the reported finite checks. The proof, not the finite test, covers real activity and arbitrary n.

## originality

PASS

Credit the known fixed-root law and its generic determinant evaluation. The signed generating formula and the zeros it directly exposes are consequences of that law, not independent originality grounds. The supported distinct claim is the sharp all-order smallest nonzero absolute Walsh multiplier at unit activity, with exact Hilbert-space recovery conditioning even in the singular parity. This uses a discrete minimization across the sign change. The compared sources do not establish this sharp minimization for the vertex root profiles of K_n. The assessment is to the best of current knowledge, not a priority finding.

## value

PASS

The root set is the natural Boolean observable. Knowing the exact smallest nonzero multiplier determines best possible stability of Hilbert-space recovery, on the whole space for even n and on the recoverable subspace for odd n. This requires locating the worst shell, not merely evaluating a root count or detecting a zero. The activity analysis also separates a high-nullity point from the isolated single-shell losses, without needing to treat those formula corollaries as original.

The dated certificate retains the supplied scientific assessment, sources and limitations.
