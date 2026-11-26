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

Independently reconstruct the cover. Encode each coloring by f(0) and its r minus edges. A nontrivial recoloring requires equal neighboring colors, swaps the two opposite steps, and contributes +2 to f(0) precisely for a positive crossing of the cut (−2 in reverse). Any active coordinate has at most two colors and two adjacent active coordinates would require a K2,2 in C_n; thus the cubes are exactly simultaneous moves along disjoint closed particle edges. Projection forgetting f(0) is a covering: every move and every independent family of moves lifts uniquely locally from its starting coloring, with the color of 0 changing only for a cut move. Rotation does not stabilize a cell nontrivially (a two-color coordinate has separation 2 and n≥5). For an independent check of the primitive coordinate, lift the ordered particle positions to integers x_1<...<x_r<x_1+m, extend periodically by x_{i+r}=x_i+m, and take the unit cubes whose vertices all obey these inequalities. This covers the quotient particle complex by retaining the cyclic labeling and its unwrapped starting position; all lifts differ by T(x)=(x_2,...,x_r,x_1+m). For comparable feasible x≤y a positive unit path exists: a coordinate still below y that is blocked by its successor at spacing one forces that successor also below y; a full cycle of blocked spacings is impossible because m>r. Two possible first moves can be made in either order and span a square; induction via such diamonds makes all ascending paths with fixed endpoints homotopic. A finite loop admits a common feasible coordinatewise upper bound for all its vertices (a sufficiently large translate of one vertex), and is null by replacing each edge with the paths to that bound. The lifted complex is connected by the same path construction and simply connected. Since sum(Tx)−sum(x)=m, a primitive quotient loop has signed displacement m and one net cut crossing. It preserves target color after L=n/gcd(n,2) repetitions; cover components are the monodromy orbits. Each signed edge contributes ±1, so winding q in a component costs at least |q|mL. A monotone path x→Tx has exactly m moves from any basepoint; repeat and reverse as needed. This checks existence, integer powers, optimality, and parity independently of the bundled finite diagnostic or the cited discretization theorem.

## originality

PASS

Pass concerns the exact metric for all admissible nonextreme sectors and all powers, not the circle topology, target evaluation parity, or cycles in already computed special cases. Known topological/evaluation invariants constrain the possible displacement but do not by themselves provide an optimal monotone realization for every sector. Comparisons with the closest distinct indexed records and cited papers are bounded by the explicit access limits below.

## value

PASS

Single-vertex recoloring is the natural adjacency operation in this complex. The exact filtration by edge length of the fundamental-group classes is not supplied by the rank of that group. An optimal signed circulation resolves every sector, exhibiting why particle density does not enter and why target parity does; this is useful to anyone interested in shortest essential walks rather than only component topology.

The dated certificate retains the supplied scientific assessment, sources and limitations.
