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

The repair makes only the second maximum a contribution, over fixed positive shifts not powers of p for each odd prime, with cyclic indexing and Pearson normalization. Splitting the units digit under addition gives the raw product-sum carry recurrence, and the squared-mean/second-moment ratio [3(p+1)/(2(2p+1))]^L decays to zero. At lag one the recursion contracts, and larger fixed shifts use smaller arguments, so the rational limit is the Pearson limit. Dividing a shift by an exact factor of p preserves the limit. For reduced one-digit shifts, exact integer and square sums give C_2, C_1-C_2>0 and C_2-C_p(a)>0 for 3<=a<p; its comparison polynomial decreases to p-2>0 (empty range for p=3). For a reduced multidigit shift both input lags are positive, so the known first-tier bound gives C<=C_1(U_1+V_1)/B. The gap to C_2 is strictly positive, with numerator 3(p^2+p+6) over the stated positive denominator. All remaining equality cases are exactly 2p^k. Replay python3 /workspace/branches/reproduce_pascal.py (SymPy) independently checked the seven polynomial identities and reconstructed all exact raw and centered cyclic correlations from actual modular Pascal rows for (p,L)=(3,5),(5,3),(7,2); those examples corroborate the proof but do not establish it. No finite-length ranking or growing-shift claim is made. The original checker remains applicable.

## originality

PASS

The repaired statement credits the previously covered carry kernel and first tier and isolates the sharp runner-up with all its equality cases. No inspected comparator states or gives this all-shift extremum as a special case of a stronger theorem. Knowing the recursive function lets one evaluate C_p(2), but does not by itself establish its rank among infinitely many shifts.

## value

PASS

The runner-up quantifies the strict gap from the principal resonance and identifies every shift attaining the next level, using a uniform comparison of all remaining digit patterns. This strengthens a natural dependence question for Pascal rows; simply evaluating the single lag 2 would not supply that information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
