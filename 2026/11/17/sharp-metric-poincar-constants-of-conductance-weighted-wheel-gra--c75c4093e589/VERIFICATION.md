---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS: For r>=4, A,B>0, any hub-outside indicator cut with s proper rim vertices has crossing conductance As+B times at least 2 rim transitions, with equality exactly a contiguous arc; full rim has Ar. For arbitrary metrics dihedral averaging preserves energies; hub spoke average a and rim neighbor b give t=b/a in [0,2], and c_k<=min(2a,min(k,r-k)b). The resulting affine-fractional ratio is maximal at t=0 or t=2/s; each endpoint is realized by rotation average of an arc cut, proving metric target equality to maximal cut. Direct comparison yields threshold B/A>=floor(r²/4)/2; cross multiplication gives staircase and expansion yields 4-8sqrt(2/r)+O(1/r). Independent rational enumeration checked 28 wheel/conductance instances.

## originality

PASS

No known source supplies the universal metric=real L1=scalar sharp weighted-wheel formula, exact optimal arcs and full-rim threshold; the close wheel projection theorem uses a different functional.

## value

PASS

PASS: Natural wheel family with two continuous positive conductance parameters; universal equality of arbitrary metric and L1 extremizers is nontrivial in view of target separation on other graphs. Exact arc/full-rim phase boundary and asymptotic make the theorem useful beyond a single constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
