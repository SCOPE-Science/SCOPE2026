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

For nonempty ordered rung columns, each consecutive pair forces a rail cut in its gap; edge count permits exactly one there and no others. Conversely, the uncut rail in each gap connects the bounding rungs, and both portions of the cut rail reach a bounding rung; tails are intact. Thus the multiplicity is the product of twice each gap length. Summing over the two boundary offsets and positive gaps gives 2^(k−1) binom(n+k−1,2k−1). At c=t/n² the masses multiplied by n tend to 2^(k−1)t^k/(2k−1)!, dominated by 2^(3k−2)t^k/(2k−1)!. Normalization yields the stated odd-Poisson, total variation convergence, pgf and mean. The conditional position weights give the product-of-gaps density by midpoint Riemann sums, normalized by the Dirichlet integral. Independent uniform discrete cuts in each gap couple to independent uniform continuum cut positions, with independent fair rail labels. Equivalently, conditional on k, the ordered unlabelled rungs and cuts alternate as 2k−1 uniform order statistics. The antisymmetric rail sector gives the weighted rung kernel 2c(L+2cI)^−1. Its normalized midpoint cosine modes give the stated Neumann kernel: after step embedding the bounded mode functions converge for fixed m and the summable O(m^−2) bound controls the kernel tails uniformly. The Fredholm series for the step-kernel process therefore converges to that for the limiting kernel; rounding points in the cells to their midpoints shifts positions by at most 1/n. The count eigenvalues give the two sharp-scale ends by a vanishing nonconstant-mode sum or by any fixed number of modes tending to certainty, respectively. Independent edge-subset checks at n≤6 agree with all rung-set multiplicities.

## originality

PASS

Credit the joint, open-boundary critical marked limit, including its different parity and boundary-gap parameters, not the known finite kernel, finite enumerator or generic fair-cut mechanism. In isolation the Neumann spectral limit and count asymptotics are direct consequences of known finite inputs after the critical scaling calculation; the evidence supports distinct content in identifying the full boundary-sensitive geometry and its crossover, not new transfer-current or count techniques.

## value

PASS

The critical-scale result tells when this finite connected model has a nontrivial finite rung process and specifies a complete boundary-sensitive spatial law, including the positions and rails of missing edges. These are not determined by a count distribution alone. The difference between open-interval odd interlacing and cyclic even interlacing is a meaningful geometric effect. The value is the joint scaling description, not recomputing the known finite kernel or applying a Poisson identity in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
