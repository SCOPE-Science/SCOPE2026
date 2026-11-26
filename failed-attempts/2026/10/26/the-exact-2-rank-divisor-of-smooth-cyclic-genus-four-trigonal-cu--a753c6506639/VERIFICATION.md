---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The tame degree-three cover branches at the five simple zeros and infinity, giving genus four. The pole orders of x and y at infinity are 3 and 5; dx has order -4, so the four basis forms have orders 1, 6, 3 and 0 there, and are regular at finite branch points by tame ramification. They are independent by the different y powers and the linear independence of 1,x,x^2. Write f=A^2+xB^2 with B=sqrt(a1)+sqrt(a3)x+x^2. Extracting the odd coefficient part in B and pulling out the square (y/f)^2 yields C(dx/y)=B dx/y^2. Pulling out (y^2/f)^2 gives the three other asserted images. The image has dimension 2 and is spanned by omega0 and v=C(omega0); C(v)=a3^(1/4) omega0. This restricts to a semilinear bijection if a3!=0, and otherwise C^3=0 but C^2(omega2)=v!=0. The reduced rank-zero locus is the indicated hyperplane intersected with the smooth open of coefficient space; squarefree witnesses exist on and off it. Independently reproduced the witness zeta numerators through degree 8 using gcds in F2[x] with x^q-x and f^((q-1)/3)-1 for the even extension degrees, and the bijective cube map in odd degrees. No frozen program was executed. The proof, not these examples, establishes the family-wide result.

## originality

FAIL

The full paper by Sohn (2025), not just its abstract, gives the coefficient matrix for this same y^3=f(x), deg(f)=5 family. Its Eq. (6), read using the action in Eq. (4), directly specializes at p=2 to the four frozen Cartier identities. The stable-rank, exact nilpotence index and hyperplane assertions are immediate from its two off-diagonal blocks. The printed scalar a-number theorem in that paper is inconsistent with its matrix and is not being cited as a correct scalar result. There is also a distinct indexed Resultary record with explicitly equivalent rank stratification, but its later dated path is not evidence of earlier priority. The older exact matrix and its direct implication are sufficient for the decision.

## value

FAIL

The coefficient divisor is a natural parameter-space invariant and the computation is correct, but its only defining condition and the nilpotence index follow by reading and iterating the already available two-block matrix at p=2. Hyperplane smoothness and elementary witness squarefreeness do not supply a distinct result, and the frozen claim adds no invariant beyond those mechanical consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
