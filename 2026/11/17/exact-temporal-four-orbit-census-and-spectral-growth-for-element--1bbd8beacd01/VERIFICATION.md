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

Rule 54 local Boolean rule is f(a,b,c)=(54>>(4a+2b+c))&1 with periodic ring n>=3. A temporal-p periodic cylinder corresponds bijectively to a length-n closed walk in the finite directed graph of overlapping p-bit spacetime columns; the local rule checks all p phases. Strongly connected cyclic components for p=1 and 3 are one zero loop, for p=2 loop plus four-cycle, and for p=4 these plus two isospectral 10-state 14-edge components. Each ten-state component has characteristic polynomial (x+1)(x^4-x^3-1)(x^5+x^3+x+1)=x^10-x^6-2x^4-2x^3-x^2-2x-1. Consequently R1=R3=1, R2=1+4[4|n], and R4=R2+2b_n where b_n=tr(B^n), and primitive four-cycle orbits equal (R4-R2)/4=b_n/2. Cyclic closed walks of lengths 4,6,7,8,9 through one vertex and closure with a four-cycle prove sharp support n=4 or n>=6; primitivity and spectral factor x^4-x^3-1 prove growth alpha^n/2, alpha≈1.380277569. Independently rebuilt the explicit 10-vertex 14-edge matrix, factored its characteristic polynomial exactly, and directly ran the ORIGINAL Rule54 synchronous update on all 2^n indexed configurations for each n=3,...,14: every returned count and b_n/2 agrees. The all-n theorem rests on complete finite-state transfer and Perron proof; finite brute force is corroboration, not infinity proof.

## originality

PASS

PASS on material read: pre-existing 2014 extended de Bruijn diagrams identify primitive gliders and periodic ether, but neither give the all-circumference labelled primitive temporal-four count, tenth-order recurrence, sharp set of allowed n, or growth constant. The 2026-11-02 period-preserving preimage-image theorem for Rule54 concerns one-step maps rather than the temporal-four cycle locus. Common automaton representations and motifs are credited, without claiming their invention.

## value

PASS

Exact all-length temporal orbit census and sharp first-occurrence gaps for a canonical elementary rule with known complex gliders is a natural complete finite-state invariant. The characteristic polynomial, period-four support semigroup, and entropy root quantify dynamics not furnished by individual pattern examples; a complete rational enumeration is mathematical value even if proof uses finite-state algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
