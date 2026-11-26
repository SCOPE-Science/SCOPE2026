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

For n>=5 the five positions in one cyclic window are distinct. A window with three ones must be 10101, corresponding to two consecutive unit zero-gaps. Counting pairs by their order within a window gives 3 starts at distance two, 2 at distance three and 1 at distance four. The last category is either one gap of length three or two unit gaps, so summing pair counts gives b+3t=3p+2q+r+t. This counts oriented offset occurrences, so it is valid also at n=5 and for periodic inputs. The weighted count of one-occurrences equals 5w. The observation coordinates are integer weight and counts (equivalently the gap counts and h must be integers; t is a window count). For nonempty inputs, assigning the length surplus E to the h long gaps accounts for all nonnegativity conditions, including E=0 when h=0. In a nonconstant pattern of unit gaps there are k=p-t unit runs and as many non-unit runs; both lengths can be composed into k positive parts exactly on the claimed interval. The two compositions, choice of the labeled starting slot and division by k count labeled cyclic patterns, and gap-type multinomial assignment and stars and bars complete the count. Pointing to any one of the w indexed ones bijects with a labeled gap list and one of n starting indices, giving n/w without a primitivity assumption. The all-zero word is separate. Independently, a four-symbol context automaton with allowed shifts has transition monomial s^b_new y^[windowweight=2] z^[windowweight=3] for appended bit b_new. Its closed walks of length n at fixed index biject with the indexed words. Its exact determinant det(I-xM) is (1-x)D, so the trace-log derivative confirms every claimed coefficient for n>=5, not only the finite direct checks. Literal support sizes n=5,...,19 also agree. Replay: python -B branches/independent_reproductions.py 5 from /workspace (SymPy). The zero-error optimum is one word per nonempty fiber, not a noisy-channel bound or a necklace count.

## originality

PASS

Pass the explicit all-length feasibility and indexed fiber formula using unit-gap adjacency and its two-state compression. Generic cyclic finite-state walk enumeration already gives rationality and an uncompressed enumerator; neither is a novelty claim by itself. The closest inspected shorter-window and ordered-profile results do not give the pooled five-window feasibility interval or evaluated fiber multiplicities for indexed legal words.

## value

PASS

Five is the first window length in this source that can see three ones and thereby adjacent unit gaps, which shorter composition or even ordered four-gram counts miss. The explicit realization test and full indexed fiber law, not just short tables or a generic finite-state enumeration, answer natural inverse and noiseless coding questions for all lengths and preserve the effect of periodic words.

The dated certificate retains the supplied scientific assessment, sources and limitations.
