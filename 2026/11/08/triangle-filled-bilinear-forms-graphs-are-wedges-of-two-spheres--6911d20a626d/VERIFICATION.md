---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

For each finite field F_q (including extensions) and a,b>=2, the edge-path group of the triangle-filled rank-one Cayley graph is ker(P→H), where H=(F_q^(a*b),+) and P has generators x_R and precisely backtrack/triangle relations. Rank-one generators sharing a row/column factor commute. For independent left and right factors write C=uy^T, D=xv^T, A=uv^T, B=xy^T and W=(u+x)(v+y)^T; two valid triangle decompositions of W give x_A x_C x_D x_B=x_A x_D x_C x_B, so x_C and x_D commute without assuming characteristic or ordering. Expanding each rank-one generator by coordinate units along shared-factor rank-one partial sums gives a surjective additive map H→P that splits the evaluation P→H. Therefore P≅H and pi1(T)=1. Each graph vertex has d=(q^a-1)(q^b-1)/(q-1) neighbors and each edge λ=q^a+q^b-q-2 common neighbors, so V=q^(ab), E=Vd/2, F=Vdλ/6. Connectedness, free H2 and the Hurewicz/Whitehead homology equivalence give T≃∨^(V-E+F-1) S^2 integrally. Its triangles exist and no nontrivial reduced cycle shorter than 3, yielding Lewis second girth 3. Independently authored exact checker verified mod-two boundary ranks for (q,a,b)=(2,2,2),(2,2,3),(3,2,2), plus rank-one face and commutation-identity tests for extension field q=4,a=b=2. The proof, not these finite cases, establishes the universal claim. All eight actual Git blob identities were read and the eight-entry Git tree was independently reconstructed, matching frozen SHA c57d62baa234f5c4643ed5896a100a8f4eb1ef49.

## originality

PASS

Best-of-knowledge originality of the all-prime-power, all-matrix-shape simple-connectivity and integral two-sphere-wedge statement. The exact published Resultary hit is the very same submitted record, not an independent earlier theorem. Lewis (1996) supplies only a general essential-length-six bound for relevant Q-polynomial distance-regular graphs, and the 2026 Burkey–Martin–Oulon abstract identifies Johnson, Hamming, folded Johnson/cube and halved cube cases, not the bilinear-forms rank-distance family. Cioabă–Mim concerns first clique homology over fields, which cannot imply trivial nonabelian pi_1, and only its strongly regular part could cover a=b=2. The known bilinear-forms intersection parameters determine E and F but not pi_1. No predecessor with a matching all-parameter implication was located; inaccessible potentially relevant full texts and unindexed finite geometry remain explicit risks.

## value

PASS

The rank-one-difference bilinear-forms graphs are a canonical q-analogue of Hamming graphs and a standard distance-regular family. The exact all-size, all-prime-power integral homotopy type of their triangle-filled two-skeleton is a natural structural invariant. The matrix-factor commutation identity resolves a nonabelian edge-path gap that standard eigenvalue/intersection arrays and field H1 vanishing cannot settle. The result distinguishes the second girth 3 from Hamming graph second girth 4 and supplies explicit two-sphere multiplicities relevant to finite geometry and low-dimensional graph topology. It is not just a numerical face count, arbitrary finite slice or routine substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
