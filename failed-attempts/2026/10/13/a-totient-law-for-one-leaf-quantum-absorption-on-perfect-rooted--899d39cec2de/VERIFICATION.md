---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The site-generated cyclic space and its orthogonal complement both reduce the loss generator, with Hermitian dynamics on the complement. For an eigenvector u of K in the bright space, Im(lambda)||u||^2=-gamma|<v,u>|^2. A real eigenvalue would force orthogonality to v and then to every A^k v since J is real and nonzero, which contradicts brightness. Jordan blocks do not alter decay to zero on the finite bright space. Hence I/N gives capture rank/N, not the capture of a coherent uniform vector or an arbitrary localized state. Schur complementation gives the root determinant ratio P_(h+1)/P_h and the full product with P_k exponents (b-1)b^(h-k) for 1<=k<=h; no size disappears for b>=2. The Chebyshev roots are indexed by j/(k+1), with cos injective on (0,pi); reduction gives each reduced denominator 2 through h+2 exactly once per reduced fraction. No eigenvector can vanish on all leaves, by the eigen-equations inducting inwards. Rooted automorphism transitivity then gives nonzero projector diagonal at a fixed leaf for each eigenspace, so the leaf cyclic rank counts distinct eigenvalues, never multiplicities. Uniform level vectors give a Jacobi block with nonzero off-diagonals sqrt(b) and cyclic first vector at the root. This yields both ranks, independent of positive loss rate, and the standard summatory-totient estimate gives the claimed depth asymptotic. For the star h=1 the ranks are 3 and 2, respectively. There is no parameter-uniform finite-time assertion.

## originality

FAIL

The exact operative leaf-rank claim is demonstrably covered, not merely suggested by neighboring Cayley-tree spectra. In the distinct indexed two-leaf result 2026/11/2/SCOPE-two-leaf-coherent-capture-on-complete-branching-trees-an-exact-t--5d10e1c82c34, proof steps 1–2 explicitly count the same reduced-angle spectrum and prove every eigenvalue visible from one leaf; the proof states the exact single-leaf rank D(L). Its two-leaf increment needs b>=3, but its one-leaf steps only use b-1>0, the level Jacobi blocks and transitivity, and work unchanged for b=2. Novo et al.'s general single-trap projection principle converts that evaluated rank immediately to capture D(h)/N for I/N; the same work already treats root reduction to a path for the binary case, and replacing sqrt(2) by sqrt(b) gives the arbitrary-b root rank without further spectral work. The asymptotic is the classical summatory-totient estimate. Thus the corpus covers the leaf result itself and the remaining assertions follow directly, rather than the original result being established only by a generic formula with an unevaluated site measure. This is a statement-coverage determination, not an inference of historical priority or dependence from record dates.

## value

FAIL

Absorption placement in a homogeneous quantum tree and its bright-rank invariant are well motivated. But the exact leaf invariant is already established in the inspected corpus and the root contrast follows from the radial path and division by the same N. The binary endpoint is covered by the same single-leaf proof without the two-leaf increment restriction. There is no independently useful exact remainder in this specific claim once that overlap is credited; extending to other trap placements would be a different question, not a repair of this finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
