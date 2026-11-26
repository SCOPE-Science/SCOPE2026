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

Generic suffix maximizers give exactly the composition endpoints; every cut set is realized by giving its ordered endpoints decreasing heights and giving other positions lower heights. Support before n distinguishes cut sets. Adjacent-block merges preserve ||v||^2+2a·v=T^2 because a_s-a_t is the mass of the right block. The simplex projection of -a gives c and the stated consecutive breakpoints, including k=n where the upper condition holds automatically. The nondecreasing c satisfies prefix sums <=jT/n<=prefix supply. Allocating destinations in increasing order therefore gives a feasible supply allocation from sources h<=i and proves c∈Q_n. For vertices, the squared-radius deficit is 2(c+a)·(v-c)>=0. The vertices attaining equality constitute an exposed face containing c; averaging squared distances using their barycentric weights then adds exactly the squared center shift for any competitor, proving uniqueness and minimality. The eligible coordinates are a_i<=lambda, not just a_i<lambda, and give b-1 free cuts. Single-cut differences span the face, which has the known cubical combinatorial type. Successive differences verify the squared-binomial sum, and the breakpoints give k~b~(3/2)^(1/3)n^(2/3). A separate exact replay generated vertices from all objective orders at n=2..8 and checked the radius and contact counts; a scan through n=1000 found no ties, so the tie rule is justified analytically, not by observed ties.

## originality

PASS

The supported distinct claim is the minimum enclosing Euclidean ball and exact terminal contact face for the canonical (0,n) weighted suffix sum. The published construction, cubical type, routine simplex projection, and general minimum-ball convex-hull certificate are not new. None of the compared statements establishes the family-specific smallest-ball formula and contact law. Closest full-text priority remains provisional.

## value

PASS

The canonical skew cube has exponentially many vertices, but its exact minimum Euclidean ball selects a single exposed face with dimension asymptotic to (3/2)^(1/3)n^(2/3). This geometric screening phenomenon is not measured by combinatorial type or the all-vertex sphere; the exact radius and contact formulas give concrete comparisons for canonical embeddings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
