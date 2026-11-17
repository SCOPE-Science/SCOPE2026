---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The seven weight-3 Hamming codewords correspond to Fano lines; their weight-4 complements pair with them. For a line with t=0,1,2 internal edges of the cyclic order, pair weights are 6-t and 7-t. Each of seven cycle edges belongs to one Fano line, so b0=b2=a and b1=7-2a; Fano intersection forces a<=2. Counting all 360 unoriented 7-cycles: first incidence 7*72=504 and pair-line incidence 21*8=168, giving N0,N1,N2=(24,168,168). GL3(F2) of order168 identifies equivalent parity-check lists, giving 30 indexed codes distributed (2,14,14) and the advertised exact weight polynomials. Independently enumerated all 360 cycles and all 5040 column permutations, directly generated all 16 codewords for each and found exactly the three enumerators with multiplicities 2,14,14.

## originality

PASS

Best-of-knowledge survival of precise final claim after source-by-source implication comparison, with listed risks; no worldwide priority certification. A single known MDS cyclic presentation establishes existence only, not multiplicity 2/30 nor complete three-polynomial distributions. Length-eight extended-Hamming enumerator classes do not map to length-seven cyclic pair enumerators via naive puncturing because adjacent pairs are rewired.

## value

PASS

Exact complete classification of all distinct interleavings of the smallest perfect binary Hamming code under cyclic symbol-pair read metric; identifies exactly which two indexed code presentations attain the Singleton-optimal pair distance five. The Fano-cycle incidence census is a meaningful finite geometric invariant, not an arbitrary partial slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
