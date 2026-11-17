---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The positive-speed implicit equation Phi(u,v)=uv(v-u)/(u+v)=t and three sine kicks with zero sum yield the exact identity sum_cyclic Phi = -(x-y)(x-z)(y-z)(xy+xz+yz)/((x+y)(x+z)(y+z)). Independently verified symbolically in SymPy; positivity forces repeated speed and hence a zero sine kick. This restricts initial angles to multiples pi/3. With a=sqrt3|P|/2, the positive quadratic root ratio satisfies q²-(1+t/u²)q-t/u²=0. Its negative-kick plus branch is defined exactly for t/u²>=-(3-2sqrt2), and inverse step after a positive kick selects this branch precisely when entering w²>=a. In the opposite order, negative first requires w²>=(3+2sqrt2)a. Both inclusive endpoints are double quadratic roots. The rotating angle has least period three, and the proof covers all positive speeds and P !=0. Finite source verifier is consistency evidence, not universality.

## originality

PASS

Khandelwal–Mukherjee (2024) introduced the same map and gives sufficient lattice angles for periodicity, but its publicly accessible abstract does not by itself decide whether all angle possibilities or sharp plus-root branch thresholds were already proved in the complete manuscript. arXiv HTML/PDF and OA full-text attempts failed and authorized institutional tool reported VPN disconnected. With the explicit factored necessity proof and new exact branch thresholds not implied by the verified abstract or known general periodicity, best-of-knowledge originality is retained with a substantial named source-access risk, not falsely reported as full-text NOT_COVERING.

## value

PASS

Branch choices and endpoint folds matter to the exact periodic point set of a physically motivated nonlinear angular map. An all-phase necessity classification plus two asymmetrical sharp speed thresholds completes an exact natural three-step case; it is not an arbitrary tiny numerical exception.

The dated certificate retains the supplied scientific assessment, sources and limitations.
