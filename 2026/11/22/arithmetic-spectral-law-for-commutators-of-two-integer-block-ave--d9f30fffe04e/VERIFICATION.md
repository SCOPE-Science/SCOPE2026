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

After ordering p,q (reversal only negates the commutator), tensoring with the rank-one constants projection on g coordinates gives the gcd reduction. For coprime m<n both projections are identical from cell to cell of length mn. On the n-block range in a cell, the squared defect from E_m is a sum over the distinct m-blocks straddling the boundaries jn. In each such block the two values have multiplicities r_j and m−r_j and are scaled by 1/√n, giving L/n exactly. The path has kernel the constants and simple eigenvalues by the first-row tridiagonal recurrence; independently, the weights are at most m/4 and the sum of squared nearest-neighbor differences is at most 4‖u‖², so μ_max≤m<n. For t=1−μ/n in (0,1), a unit range vector v of the compressed projection and (E_m v−tv)/√(t(1−t)) give one two-dimensional block, whose commutator eigenvalues are ±i√(t(1−t)). The other directions commute and constants ensure zero occurs. Repetition gives infinite multiplicities and essential norm equal to the finite-block norm. For n≡±1, the finite differences on degree k have leading coefficient k(k+1)/m, giving the stated spectrum; maximizing in the indicated scale regime uses monotonicity up to η=1/2. At fixed residue the same path works for every n, so the limit follows directly. The verification record, check.py and NumPy dependency were inspected; the finite diagnostics were not executed.

## originality

PASS

The distinct contribution is the residue-weighted path reduction for arbitrary coprime aligned widths, its modulus-only dependence, the full ±1 congruence families beyond adjacency, and the resulting residue-wise scale-separation law. The generic principal-angle law, the finite cross-Gram spectral prescription, its adjacent-base specialization and the underlying Hahn eigenvalues are not credited as distinct results. In particular, the different operator in the strongest same-day comparison does not make the overlap disappear.

## value

PASS

The residue path is useful for understanding relative position of these canonical block averages. In particular it separates the residue from a scalar 1/n, exposes the large-width decay constant without recomputing growing overlap arrays, and gives sharp norms throughout two residue classes, not just adjacent lengths. Value lies in this structural reduction and its consequences, not in recomputing a Hahn table or merely applying the generic projection norm formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
