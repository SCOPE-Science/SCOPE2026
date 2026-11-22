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

The original directed successor-only three-state map gives F^2_i=2a_i+m_i and F^3_i=2m_i+m_{i+1}, with m_i identifying 001/201 triples. Marker exclusion within distances 1 and 2 forces separated 12-pulses. On this entire image F=S; translation equivariance proves F^4=SF^3 and sharp entry cutoff three with explicit witnesses, all n>=3. The 3-state suffix transfer matrix Q(z) has characteristic polynomial lambda^3-3lambda^2+2-2z and a unique closed itinerary per cyclic word. Its z=0 roots 1,1±sqrt3 give E_n exactly and the primitive period count follows from binary gap-3 shift and Möbius inversion. Independent direct enumeration of all 3^n inputs for n=3..8 reproduced pulse histograms and trace at z=0,1,2,3 (E_3=21, E_8=3105), with witnesses at each n; inspected check_exact.py and check_direct.cpp. Finite checks corroborate but the local identities, cyclic matrix trace and Möbius argument prove the all-length statements.

## originality

PASS

Best-of-knowledge originality: the exact claim is not mechanically implied by inspected primary or published related theorems. Previously established GH pulse motion or the existence of spatial periodic objects does not determine how each of 3^n initial words maps after precisely three steps, nor the transfer polynomial. Conversely the present pulse-marker reconstruction explicitly supplies that missing map, not merely a rewording of ordinary wave periodicity. See explicit access and indexing risks; unsuccessful search is not proof of priority.

## value

PASS

A sharp uniform three-update synchronization cutoff and exact initial-state-to-pulse transfer/cubic extinction law give nontrivial dynamical and enumerative invariants of a natural directed excitable ring. The full basin count and pulse-frequency polynomial are neither a generic GH definition nor merely the count of already-periodic trains; they can be used to compare relaxation and survival laws across networks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
