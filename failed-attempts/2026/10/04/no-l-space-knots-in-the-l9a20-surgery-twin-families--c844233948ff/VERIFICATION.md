---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The exclusion is mathematically correct. Kegel--Schmalian print the one-variable Alexander polynomials for both \(L9a20\) twist families. In the noncollision ranges \(|m|\ge3\), \(n\ge4\), and \(n\le-5\), the displayed coefficient \(-7\) survives. Independent collection of coincident exponents in the eleven exceptional parameters reproduces the stated maximum absolute coefficients \(7,13,9,7\) for \(m=-2,-1,1,2\) and \(7,7,5,13,9,7,7\) for \(n=-4,-3,-2,-1,1,2,3\). Since an \(L\)-space knot in \(S^3\) has normalized Alexander polynomial with all nonzero coefficients equal to \(\pm1\), every nonzero family member is excluded.

## originality

FAIL

The same primary paper already prints the exact Alexander polynomials for the two \(L9a20\) surgery-twin families and separates the same noncollision ranges from the same finite exceptional parameter set. The audited conclusion is obtained by reading a coefficient of absolute value greater than one from those published formulas, collecting the finitely many collisions, and applying the classical \(L\)-space-knot Alexander-coefficient obstruction. Under an implication-based originality standard this is a direct corollary of stronger same-object published data, even though Kegel--Schmalian do not state the \(L\)-space-knot classification.

## value

FAIL

The classification is convenient, but its proof is only a standard coefficient obstruction applied to explicit same-paper Alexander polynomials, plus eleven elementary substitutions. It introduces no new Floer-theoretic mechanism, knot-family structure, or difficult exact invariant beyond the already published formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
