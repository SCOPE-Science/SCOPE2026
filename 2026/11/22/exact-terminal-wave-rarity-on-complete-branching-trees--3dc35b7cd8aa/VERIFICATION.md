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

With b>=2 and the exact synchronous 0->1->2->0 threshold rule, traceback from an excitation at time t branches at least b ways. Excitations at the same site cannot be two ticks apart, so backwards paths never immediately retrace an edge; on a tree they are simple and siblings' branches cannot meet. A height-t witness therefore takes at least (b^(t+1)-1)/(b-1) vertices. This forces t<=h, and a height-h witness spans and is rooted at the true root (any other vertex is farther than h from a leaf in a different first-generation branch). Its time labels force bottom states 1,0,{0,2}. Conversely the first two updates produce the waves as stated (the parent alone cannot stimulate a nonleaf with b>=2). If all children fire at j-1, none fires at j-2 or j-3. For j>=3 their parent cannot fire at either j-2 or j-1; it must be at rest at j-1 regardless of the initial state and external parent trajectory. It fires at j. The last excitation at h is nonzero through h+1 and is gone by h+2; if no excitation occurs at h, extinction is by h+1. The product count, probability and h=0,1 cases follow directly. My independent simulator checked both extinction time and the predicted extremizer predicate coordinatewise for every enumerated initial state, including all 3^15 binary height-three states (12 maximizers), all 3^13 ternary height-two states (2), and the ternary height-three slice with leaves fixed (24). Replay: python3 /workspace/reviews/reproduce.py 4 full (NumPy); /workspace/reviews/reproduce-output.txt. The height-three ternary slice is not full enumeration; the proof covers all parameters. Frozen C++/Python and saved outputs were inspected, not executed.

## originality

PASS

Pass only for the sufficient as well as necessary characterization and exact attainment of the shell probability on perfect trees. The old tree traceback, worst-case bound, existence of a standard attaining configuration, bottom-layer necessity, and product upper bound are not distinct contributions. The inspected overlapping statements do not force all admissible higher-layer initial colors to work; the local refractory-time argument establishes that missing assertion.

## value

PASS

The census resolves whether the known worst-case clock is reached on a whole product class or only on special witnesses. The iff condition pins exactly the three bottom layers and explains why the probability of the maximal event is doubly exponentially small in height. Exact attainment despite arbitrary parent feedback is the useful additional structural fact, not the specialization of the old clock.

The dated certificate retains the supplied scientific assessment, sources and limitations.
