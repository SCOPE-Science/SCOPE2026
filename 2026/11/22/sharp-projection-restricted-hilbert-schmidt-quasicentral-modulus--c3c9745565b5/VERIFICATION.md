---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits

The proof supplies three independent analytical identities: the finite-projection trace inequality, the exact dyadic-arc commutator energy of a bilateral shift, and the single boundary-crossing energy of a unilateral coordinate cutoff. Together they prove the universal lower and matching upper bounds for every finite pair of multiplicities, with a monotone sequence. The Schatten-two perturbation limit is proved via finite-rank approximation; no finite simulation is used to infer convergence for arbitrary operators.

Run `python checks/check_projection_modulus.py` for deterministic finite-dimensional exact-rational and dyadic-step consistency tests. Expected success prefix: `PROJECTION_QUASICENTRAL_DIAGNOSTIC_OK`. These tests are diagnostic only. The standard positive-contraction modulus uses the unnormalized Hilbert–Schmidt norm and an explicit diagonal linear taper.

The index-sign convention is \(\operatorname{ind}(S)=-1\), hence \(\operatorname{ind}(T_{p,q}+K)=q-p\). The result is not claimed for arbitrary compact perturbations or arbitrary essentially unitary Fredholm operators. Independent mathematical validation has not been performed.
