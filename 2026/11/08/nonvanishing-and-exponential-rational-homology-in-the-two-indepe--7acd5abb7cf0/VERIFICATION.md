---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Reconstructed the 16-state four-bit transfer automaton exactly from cyclic five-bit vertex tests for Ind_2(C_n^2). Independent SymPy characteristic polynomial is x^11(x^5-x^4+x^2-x-1); direct subset enumeration n=5..12 agrees with trace, initial Z_5..Z_16 are [6,10,8,1,-2,6,23,34,27,8,3,33]. The factor (x²+x+1)P(x)=x^7-(x+1)² gives the stated exact 7-step recurrence. Positivity for Z10..Z16 plus recurrence proves all later terms positive, with the sole negative Z9. The dominant real root rho is simple and strictly larger in modulus than all other quintic roots via the equality case of triangle inequality; Euler–Poincaré yields exponential lower growth of total reduced rational Betti numbers. Finite examples were not used as infinite proof.

## originality

PASS

An infinite family nonvanishing theorem and exact signed growth for 2-independence of graph squares is not implied by accessible ordinary-cycle, clique/Rips, or different circular-ladder signed enumeration. The signed quintic recurrence is an independent parameter-specific calculation, with residual dissociation-table risk.

## value

PASS

A natural graph-power higher-independence family has a complete all-n nonvanishing result and explicit positive exponential growth obstruction. The transfer recurrence identifies an actual topological phenomenon and leaves degreewise Betti/homotopy questions open; the graph-power choice is canonical rather than arbitrary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
