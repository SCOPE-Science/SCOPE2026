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

# Verification of the sharp first-band torus result

The argument in `RESULT.md` is self-contained: its only nontrivial inequality is the sign of a polynomial affine in each cosine variable on the complement of the proposed square. Splitting \(X=\cos(2\pi x)\le-1/3\) at \(X=-1/2\) yields maximum values \(-(X+1)/2\) and \((3X+1)/2\), both nonpositive. The analogous bound holds after exchanging coordinates. Equality gives precisely three cosine pairs and five torus points. The first-harmonic moment equations then force the unique five positive masses stated in the finding. The explicit measure satisfies every one of the nine first rectangular Fourier moments.

`CHECK.py` is a standalone Python 3 program (no external packages). It checks all nine complex Fourier moments in exact \(\mathbb Q(i\sqrt2)\) arithmetic; the total mass; the three equality-contact identities; the affine endpoint inequalities for both rectangles; and the forced moment-weight identities. On preparation it completed without errors and reported 29 assertions, including one approximate printing-value check. Numerical sampling and these finite identities are *not* invoked to prove the universal theorem; the proof includes the required infinite positive-measure support argument.

The proof does not classify higher Fourier bands, alternative metrics, or signed measures. The publication-priority assessment is based on the primary literature described in `RESULT.md` and is not an independent audit.
