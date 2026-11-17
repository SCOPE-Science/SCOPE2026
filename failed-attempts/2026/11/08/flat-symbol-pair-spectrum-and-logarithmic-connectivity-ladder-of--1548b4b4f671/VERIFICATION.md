---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

PASS. In numerical binary-integer order, each nonconstant affine RM(1,m) word has Hamming weight n/2 and cyclic pair weight n/2+T/2, where T is the number of bit transitions. Successor carries toggle prefix parities s_j=a_0+...+a_j mod 2, giving T/2=sum_{j=0}^{m-2}2^{m-j-2}s_j+s_{m-1}. All 2^m prefix vectors map bijectively and have generating function (1+z)^2 product_{j=1}^{m-2}(1+z^{2^j})=1+2sum_{r=1}^{n/2-1}z^r+z^{n/2}; accounting for affine constant choices gives 1+4sum_{r=1}^{n/2-1}z^{n/2+r}+3z^n. The allowed r>=1 prefix-coordinate weights 1,1,2,4,... show gamma_m(alpha)=min(m+1,3+floor(log2(alpha-n/2))) above n/2; Cayley-component count 2^(m+1-gamma), connected at 3n/4. Inspected pinned check_rm_pair.py and independently enumerated full cyclic pair weights of affine truth tables m=2..6, exactly matching the formula. All-m proof uses carry algebra, not finite tests. m=2 endpoint checked.

## originality

FAIL

FAIL. Full published 2026-10-13 result Complete pair-generation profile of lexicographically ordered first-order Reed–Muller codes establishes **identical** code, binary numerical ordering, cyclic wrap-around pair metric, entire enumerator 1+4Σz^(n/2+r)+3z^n, every intermediate rank formula, component counts, sharp connectedness 3n/4 and disconnect threshold 3n/4-1. Read the complete earlier RESULT.md and verified its equations match after simplifying its 1+min(m,2+floor log2 r). A second published 2026-10-13 complete cyclic b-symbol-window enumerator covers the identical b=2 enumerator as a special case. Neither changed title nor proof method rescues originality.

## value

PASS

FAIL. These exact natural Reed–Muller pair invariants are mathematically useful in isolation, but their evaluated formulas and sharp connectivity classification are already published verbatim for the identical parameters and ordering. The submitted finding is a known result/table recomputation, without a distinct correct original invariant or new structural extension, and therefore no surviving new scientific value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
