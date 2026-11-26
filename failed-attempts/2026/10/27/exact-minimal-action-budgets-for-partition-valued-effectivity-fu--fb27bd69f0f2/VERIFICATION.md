---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Each outcome has one block per agent. With one action of a selected block fixed, reaching every outcome in a cell requires that many distinct completions within the other blocks. This proves the product lower bound, including the uniform and the two-agent coordinatewise inequalities. In the uniform construction the cyclic differences give a bijection on every fixed-coordinate slice: if the last coordinate is fixed, solve each coordinate directly; otherwise its difference determines the last coordinate first. Composing with a surjection to the cell is enough; varying opponent blocks then covers exactly the specified block. For two agents the modular sum on each rectangular cell is onto along every row and column since both dimensions are at least the cell size. Therefore all lower bounds are attained simultaneously, also when a dimension or the whole cell is a singleton. Inspected RESULT.md, VERIFICATION.md and checker.py (small exhaustive frame construction checks, no game-space enumeration for optimality); no script replay was needed. The reported 1,655 admissible inputs also follow by summing B! S(r,B)/prod_i b_i! over positive block counts b_i with B=prod_i b_i<=r, where S(r,B) is a Stirling number of the second kind.

## originality

FAIL

The earlier instance-sensitive chromatic compression theorem already gives the matching upper bound on this subclass and the exact partition optimum is immediate by counting a single cell slice. Its two-agent form also gives the seemingly new block-dependent construction by realizing each cell separately with its two prescribed dimensions and reusing labels for each block. No distinct exact invariant remains after this comparison.

## value

FAIL

Exact action budgets are a useful quantitative refinement of qualitative representability, and cell sizes can be much smaller than |R|. Here, however, the earlier chromatic product bound already sees exactly those sizes, and applying its rectangular case per cell and counting a fixed slice recovers the full two-agent result. A self-contained reformulation does not provide a distinct mathematical gain under the narrow-exact-result standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
