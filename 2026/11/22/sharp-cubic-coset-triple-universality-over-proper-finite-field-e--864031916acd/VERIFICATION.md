---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

To reproduce all finite computations, run `python3 verify.py` alongside `certificate.json`. The code has no nonstandard dependencies; it constructs the fields for all nine odd-characteristic proper prime powers with \(q<841\) and \(q\equiv1\pmod3\). It proves the supplied polynomial for each field is irreducible by trial division by every possible monic polynomial of degree at most half the extension degree, enumerates all nonzero cube cosets, and cross-checks its cubic-character colors. It evaluates all admissible starts in each field and emits one certificate per field, including missing words and explicit first witnesses for realized words. Exactly seven are complete. At \(q=49\), the minimum positive count is \(2\), as recorded in `certificate.json`. Expected final message: `VERIFY_OK 9 extension fields checked, 7 complete; 9 irreducible polynomials; cubic-coset cross-check; 27 candidate words per field`.

For the unbounded part, check the symbolic identity \(27N_t(q)=\sum_x\prod_j Q_{t_j}(x+j)-E_t\), and verify the six one-supported character sums vanish, the twelve two-supported terms each satisfy \(\lvert S\rvert\le\sqrt q\), and the eight three-supported terms each satisfy \(\lvert S\rvert\le2\sqrt q\), with \(0\le E_t\le27\). Thus \(27N_t(q)\ge q-28\sqrt q-27>0\) at all \(q\ge841\). The full theorem depends on the standard Weil multiplicative-character bound; finite calculations alone do not establish this infinite case.

The checker and certificate are not a formal verification project and do not by themselves constitute an external or independent mathematical audit.
