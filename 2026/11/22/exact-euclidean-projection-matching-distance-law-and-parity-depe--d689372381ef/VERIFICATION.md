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

In the unscaled coordinate norm for s>=3, ell>0 and a_i>=2ell, a positive defect requires x_i>a_i-ell>=ell and x_(i+1)<ell, so positive edges are a matching even when a_i=2ell. Correcting each by d_i/2 leaves its tail >=a_i-ell and its head <=ell, both in the box. If a neighboring correction raises the tail of an inactive link, that tail is <=ell<=a_j-ell; if it lowers the head, that head is >=ell and the tail is <=a_j. Either bound suffices even when the link is flanked by two active edges. The residual is a nonnegative combination of tight normals, proving the unique minimizer, and disjoint supports give squared norm sum(d_i^2)/2. Equality at the sharp bound requires a maximum matching with every matched pair at (a_i,0); the two perfect matchings for even s and the unique matching leaving each prescribed vertex unmatched for odd s prove the complete locus. The expansion over a matching uses inclusive joint violations, not independence conditional on the exact active set. The deficit density on a violated pair is 2(ell-u)/ell^2, giving the stated Laplace factor, first moment and zero atom. Independent rational feasibility/tightness checks use record5() in /workspace/branches/frozen_metric_replay.py; these sample four rational grids, not all inputs. The analytic argument supplies universality. Frozen numerical tests were read, not run.

## originality

PASS

The known chainlink corner exclusions and matching volume trace cover the zero-distance atom exactly, as credited. The box-to-body projection, associated parity-dependent maximizing locus and full squared-distance law are distinct from the inspected section and vertex-shell results. This is a bounded best-of-knowledge judgment.

## value

PASS

The exact nearest feasible point is useful in its own right: it turns a cyclic quadratic projection problem into a single coordinate pass. The sharp Hausdorff gap and isolated-versus-segment parity locus describe how the body departs from its generating box. The full error distribution refines the existing volume fraction, rather than merely restating it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
