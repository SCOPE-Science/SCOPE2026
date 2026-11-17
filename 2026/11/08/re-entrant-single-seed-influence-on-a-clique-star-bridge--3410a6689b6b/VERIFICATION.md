---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The fixed undirected graph joins K_q to the center u of a q-leaf star by a single edge uv. Independent bond retention with common p makes the expected open component sizes I_u=1+qp+p c_q and I_v=c_q+p(1+qp), c_q=1+(q-1)r_q, where r_q is two-terminal Erdos–Renyi clique reliability. Every leaf is strictly inferior to u by a samplewise monotonicity argument, and each unmarked clique vertex is strictly inferior to v since r_q<1; thus no hidden optimizer exists. The difference equals p(1-p)[q-(q-1)r_q/p], positive at p near 0 and 1. At p=1/2, direct plus independent two-hop paths give r_q>=23/32 for q>=4; hence I_v-I_u>0. The q=2,3 formulas exclude reversal. For q=4, conditioning on the fourth clique edge yields r_4=p+2p^2-7p^4+7p^5-2p^6, hence the quintic f=1-6p+21p^3-21p^4+6p^5. Under t=p/(1-p) its sign sequence has exactly two variations; f(0)>0,f(1/2)<0,f(1)>0 give precisely two interior zeros. An independent SymPy exact expansion and numerical isolation gave 0.184923052630605, 0.709331740669178. Neither an unbounded number of switches for q>4 nor a general SIR model is claimed.

## originality

PASS

The result targets a single homogeneous independent-bond one-seed *mean component size* ranking on an explicit graph family. The older epidemic-centrality papers establish regime-dependent spreader rankings but the accessible material does not give the exact two-switch theorem for the balanced clique–star bridge, the sharp q=4 onset within this family, or both algebraic thresholds. A directly plausible original 2011/2013 Šikić et al. paper was found through its actual arXiv identifier, but its full PDF could not be acquired, so possible overlap is retained as a specific historical risk rather than misreported as not covering. Nearby clique–star SIS threshold bridge-placement results use adjacency Green functions and a different dynamical target.

## value

PASS

Global optimal seed reversals are a natural and nontrivial objective-selection phenomenon in homogeneous bond percolation. The construction demonstrates two re-entrant changes between adjacent high-degree gateway candidates despite a strict degree ordering, supplies the first member of the balanced family, and rigorously identifies both phase boundaries there. This is more than repackaging the known clique connectivity polynomial; it resolves a motivated exact network-ranking question. It does not assert smallest among arbitrary graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
