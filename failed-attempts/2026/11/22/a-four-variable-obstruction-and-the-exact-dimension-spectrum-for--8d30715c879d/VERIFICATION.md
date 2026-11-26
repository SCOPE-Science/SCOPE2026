---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The four-dimensional alternating 3-form is contraction of a volume form with a unique nonzero vector, so its radical is that vector's line. Use it as the fourth basis direction; D_3 then fixes the only cubic term to be u_1u_2u_3. If the cross-quadratic lambda is zero, the radical row is empty and some other row is nonempty because an identically zero D_2 would force additivity. If lambda is nonzero, preserve the volume form while taking lambda=u_1. For r=e_4 and x=e_2+(a+c)e_4, D_2(r,z)=w_1 and D_2(x,z)=w_1w_3 for c=0 or w_1+w_3+w_1w_3 for c=1. Their supports give the claimed strict cardinality pairs. The ternary indicator at h=(1,1,1) has six distinct supports {h,h+x} and one six-point support excluding h, making an antichain. Nondegenerate quadratic blocks separate since distinct nonzero polar linear functionals are independent over F_2. For a direct sum, if a differing block has x_i nonzero, that block supplies (1,0), with all other witnesses zero; if the available differing block has x_i=0,y_i!=0, use another nonzero x-block to realize the first bit and the differing block to cancel the second bit. This verifies the odd and even constructions, including n=3 and n=6; degree three is impossible below n=3 and persists in sums on disjoint variables. A fresh exact replay checked all 15,360 four-variable cubic ANFs including linear parts, the normalized strict nesting examples, and all 42 and 3,906 ordered pairs in the two seed dimensions respectively. Replay: python3 /workspace/branches/bbb177e2-3050-4f2a-9d22-a0491b9656bb/replay.py. The replay does not prove all-dimensional extension; the block argument does.

## originality

FAIL

The claimed new universal four-variable obstruction, including the stated strict support sizes, is a direct finite readout of an earlier complete rank-four nonassociative code-loop classification. The rest of the spectrum is a direct consequence of the credited positive constructions and the degree bound. The frozen proof is a concise table-free derivation, but the exact mathematical finding is covered; no priority claim is made about the wording of the witness or this specific proof.

## value

FAIL

The exact dimension question is natural, and the compact coordinate calculation provides pedagogical explanation. As framed, however, the proposed contribution is the exact dimension fact and nested sizes already mechanically readable from the exhaustive prior characteristic-vector table plus established constructions. No further new obstruction, broader class, or consequence is established, so a cleaner proof is not a surviving novel exact finding here. No repaired claim is proposed as validated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
