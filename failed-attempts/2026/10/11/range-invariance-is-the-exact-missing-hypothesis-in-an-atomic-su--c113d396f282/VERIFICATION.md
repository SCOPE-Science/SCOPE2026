---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The printed Theorem 4.6 of Ghosh–Samanta claims every positive invertible U preserves g-atomic subspaces for fixed K. With H=R², K=diag(1,0), W=H, v=1, Λ=K*, the one-component family has frame operator KK* and is Parseval relative to K. U=[[1,1/2],[1/2,1]] has eigenvalues 1/2 and 3/2. For A=I+U and f=(1,−4), Af=(0,−15/2), KAf=0 but K*f=e1, contradicting every positive lower K-bound. The exact universal preservation criterion R(K)⊆R(AK) follows from Douglas: source S≥αKK* gives transformed AS A*≥αAKK*A*; uniform lower bound requires and is implied by KK*≤cAKK*A*, with necessity witnessed by the Parseval source S=KK*. Direct source page images confirm its incorrect unsupported AS A*≥S step and that a neighboring theorem explicitly assumed commutation. I independently recomputed the matrices with exact rational arithmetic.

## originality

FAIL

A published broader positive-transform result on ordinary Hilbert K-frames already proves EXACT universal condition R(K)⊆(I+U)R(K), shows positivity does not suffice with a 2×2 counterexample, and gives an optimal lower-bound multiplier. A K–g-fusion frame, after choosing orthonormal bases in coefficient spaces, is an ordinary K-frame with identical quadratic form and frame operator. The source theorem’s entire corrected transport criterion is therefore an immediate special case of that earlier general result; the new source-specific name and witness do not add an original mathematical assertion.

## value

FAIL

The specific source erratum has pedagogical and bibliographic usefulness, but its mathematical content—positive noncommuting transform failure, exact range repair, and its operator domination proof—is already an immediate specialization of the stronger published general K-frame theorem. Renaming the frame type and selecting a different 2D matrix witness does not constitute a motivated new mathematical gap or independent exact invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
