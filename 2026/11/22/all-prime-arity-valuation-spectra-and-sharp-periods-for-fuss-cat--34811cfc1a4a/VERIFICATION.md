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

For p dividing n, tn+1 is a unit and removing the common p-power from the two Kummer summands gives column m=n/p^v_p(n). Otherwise the identity C_t(n)=binom((t+1)n,n-1)/n gives column m=n-1. The input is respectively mt or nt+1, with unit slope in both cases. For a fixed column the outgoing carry after j digits occurs exactly when the uniform j-digit residue of the input is at least p^j-(m mod p^j). This independently yields the stated digit-sum expectation by summing the carry probabilities. The two-state weighted transition counts p-d-c noncarry choices and d+c carry choices for input carry c; beyond the last nonzero digit the surviving carry continues with probability 1/p, giving the claimed geometric factor. Exact-value events are finite residue conditions, so the Haar calculations are natural densities, and B is nonzero because the top digit can start a carry. For threshold k, an outgoing carry at position L+k-2 already forces at least k carries. Conversely set all lower digits below the top nonzero column digit to zero. At k=1 vary that top digit across the carry threshold; at k>=2 start a carry there, continue it for k-2 digits, and vary the digit at L+k-2, which toggles whether the count reaches k. This rules out period p^(L+k-2) and hence any smaller period, since a minimal period divides the known p-power period. A unit-slope input preserves the decisive nonconstant cyclic digit function. The n=6,p=2 generating function also checks by direct multiplication of two carry matrices. The verification source was inspected but not run; evidence for all n,p,k is the proof, not its finite regressions.

## originality

PASS

Credit the known general binary column density framework, the complete prime-power-column case, and the precise Lu–Tsai least period for the full binomial residue. The distinct supported claim is the uniform arbitrary-digit, all-prime valuation law and sharpness for the coarser cap, with both reductions needed for the fixed-size Fuss–Catalan arity sequence. Neither the known period for the finer statistic nor the existing restricted column laws establish that combination.

## value

PASS

Fixing size and varying arity is a natural direction in the Fuss–Catalan family. The theorem gives an exact sampling modulus at every divisibility threshold and the entire distribution with the mean and tail, rather than just a parametrized congruence or an upper bound. The sharpness matters precisely because much finer residue information could in principle repeat on a longer period than divisibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
