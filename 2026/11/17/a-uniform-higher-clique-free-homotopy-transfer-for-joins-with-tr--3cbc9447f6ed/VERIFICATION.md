---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Reproducible checks

Run `python3 verify_transfer.py` with Python 3 and no third-party packages. It constructs each qualifying graph, enumerates its forbidden-clique-free faces without using the decomposition from the proof, computes augmented simplicial boundary matrices over the two-element field by integer-bitset Gaussian elimination, and compares reduced Betti numbers with those predicted from an independently constructed independence complex. The saved run in `verify_output.txt` reports 675 successful cases: 470 at the claimed forbidden-clique orders \(t\geq5\) (including \(t=7,8\) examples), plus 205 comparisons at \(t=4\) to independently check the previously published boundary case, including triangle-free graphs with disconnected independence complexes and cycle-six instances.

## Mathematical scope and limitations

The finite checks do not prove an arbitrary-order homotopy statement or integral torsion-freeness. The full nonequivariant, integral homotopy equivalence instead follows from the explicit three-subcomplex decomposition, quotient by a nonempty contractible simplex-join, a wedge decomposition of relative pieces, and the connectivity of iterated suspensions. An independent mathematical audit has not been performed.
