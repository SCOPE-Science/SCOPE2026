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

PASS. In a three-state GH system, any state fixed under U_theta^3 decomposes sitewise into inactive all-zero vertices and vertices rotating 0->1->2->0. For the active set S on a connected 2r-regular simple graph, each active vertex needs theta successor-color neighbors; since an induced edge contributes to at most one successor count, theta|S| <= sum_{v in S}d^+(v) <= e(S) <= r|S|. Thus theta>r excludes nontrivial period3. At theta=r all inequalities force S=V and a proper three-coloring with r neighbors in each other color. It is also sufficient, and the cube-root-coordinates condition A u=-r u follows exactly, with converse from real/imaginary parts; the eigenvalue alone is insufficient. For C_n^2 n>=5 consecutive vertex triples are triangles, forcing three-spatial-period color sequences, hence exactly six when 3 divides n and zero otherwise; theta>=3 has none. Concatenating m independent 012/021 blocks and three global phase choices gives >=3*2^m rotating configurations for theta=1 when n=3m>=6. Independently enumerated literal three-step updates on all 3^n configurations for n=5,...,9 and thresholds 1,2,3: counts [150,0,0],[270,6,0],[588,0,0],[1548,0,0],[4092,6,0]; this corroborates but does not prove arbitrary n.

## originality

PASS

Best-of-knowledge original exact contact-threshold rigidity theorem for period-three Greenberg–Hastings states on *every* finite connected even-regular graph, plus a sharp squared-cycle threshold collapse and exponential constructed family below half-degree. The elementary directed-edge counting mechanism yields a nontrivial structural equivalence to balanced proper three-colorings and cube-root-coordinate adjacency eigenvectors; its actual finite graph and threshold-r assertion was not found in the inspected 1995 one-dimensional infinite-line work or the 2018 threshold-one finite-graph activity paper. This is a mathematically motivated natural threshold boundary, not an arbitrary small census. Historical priority remains qualified by older threshold-model writings not all read in full.

## value

PASS

The half-degree rigidity θ=deg/2 is a natural exact boundary for wave persistence on finite regular networks, and the theorem gives a complete structural iff characterization rather than just a search output. The squared-cycle specialization proves a sharp 3->2->1 contact-threshold phase collapse and exponential-versus-constant initial period-three populations, providing a genuinely motivated classification and transparent spectral obstruction. Exact all-graph characterization and constructive family are useful even without a full count of threshold-one states or all transients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
