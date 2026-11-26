---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The cyclic rule is right-permutive. Distinct colliding inputs cannot have consecutive matches or a shared 1. If a shared 0 occurs, the equation forces shared zeros at distance two, so the inputs are single-parity; with no shared zeros the mismatched pairs must alternate 01,10, again single-parity. The output-zero parity equations show that mixed-parity inputs stay mixed, hence that sector is a permutation. On single-parity words the dynamics swaps support parity and is a shift times D=I+S. The exact multiplicity h of z+1 in z^m-1 gives rank(D^t)=m-min(t,h); D^h=I+S^h has the stated residue-class even-sum image. Combining the two half-images with their shared zero and the mixed sector gives the rank formula; successive rank drops give the stated exact Jordan census. At n=2, 00 and 11 are fixed and both other states map to 00, as predicted. Independent replay: python3 -B /workspace/branches/independent_checks.py 2; all 5,460 states at six even lengths matched periodic membership, ranks and block counts. This is finite corroboration only.

## originality

FAIL

The October 26 Resultary finding explicitly gives the identical all-t image/rank formula, zero multiplicity, zero Jordan counts and maximal transient height throughout the overlapping even-ring range. Reflection i↦−i conjugates its update to the frozen one and preserves parity classes. The earlier proof gives the same mixed/single-parity decomposition and the single-parity stable image of (I+S)^h; the residue-sum test is a direct expression of that image, and the two-site boundary is a four-state truth-table check. The central claim is covered, irrespective of inaccessible literature.

## value

FAIL

The all-size hierarchy has intrinsic mathematical utility, but it is already established for the same automaton up to reflection. The only stated differences are the immediate stable-image parity test and the degenerate four-state boundary; neither supplies an independently substantial mathematical increment in this record. No surviving repair is justified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
