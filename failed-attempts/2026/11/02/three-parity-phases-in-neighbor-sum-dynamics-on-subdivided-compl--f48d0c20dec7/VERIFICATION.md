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

In characteristic two the incidence columns span the zero-total-sum space U by connectedness (a path's column sum gives the two endpoint vectors). The transpose kernel is the constant line. Thus rank B=n-1, rank B^t B=n-1 minus the indicator that n is even. For L=BB^t, write shore vectors (u,v) and sums S,T. In the two-even case L sends them to (T1,S1), with rank 2 and rank on U equal to 1; L^2=0 and LB is constant, giving F^4=0. In the two-odd case L sends them to (u+T1,v+S1), with kernel the constants, rank on U=n-2, and L^2+L the all-ones matrix killing B. Thus F^5=F^3. In mixed parity with the even shore first, L sends (u,v) to (u+T1,S1). Both rank L and rank on U are e (choose any first component, whose sum is S, and impose T=S when restricting to U). Here L^3=L and F^7=F^3. The successive doubled off-diagonal ranks and diagonal ranks give exactly the stated zero-primary lengths by rank subtraction. The kernels of L+I and L^2+I have dimensions (n-2,n-2) for two odd shores and (e-1,e) for mixed parity. B and its transpose intertwine the unit spaces of the two incidence products, giving the doubled fixed dimensions for F^2 and F^4. In mixed parity the e-1 unit blocks are all at least length 2 from the two-step dimension, and only two extra dimensions remain. A pair of length 3 would give the same first, second and fourth fixed dimensions as one length 4, so those dimensions alone do not force the advertised type (the sentence at RESULT.md line 81 omits this step). The missing distinction follows from rank of the shifted cube: L+I acts nontrivially on the unit space, since its fixed dimension there is e-1 of e. Hence (F+I)^2=F^2+I has two J_2(0) blocks on the unit space, which still permits either candidate. Directly, choose v supported on one old even-shore vertex and w=F^3v, which is periodic. Substitution gives (F+I)^3 w equal to the all-ones vector on the even shore and on all inserted vertices, and zero on the odd shore. Thus a length-4 block must occur and the others are length 2. The nilpotent kernels and unit return spaces then give the exact entry and orbit counts, including o=1 and a=b=1. The unsubdivided mixed case is nilpotent since its square has one all-ones block of even order. An independent dense binary elimination on 121 graphs (1<=a,b<=11) checked ranks of F^j and nullities of (F+I)^j for j=1 through 5 (1,210 comparisons); notably the shifted cube check distinguishes the mixed candidates. This corroborates the symbolic proof over characteristic two. Packaged replay: check.py and verification_output.txt, read and distinguished from the fresh dense elimination. The packaged first/second/fourth shifted-rank checks do not themselves resolve the two candidate mixed block profiles.

## originality

FAIL

A distinct exact catalogue result gives the same core theorem on both shore sizes at least two, including the three Jordan partitions and transient and primitive-period counts, and even individual orbit-basin sizes. Its path is dated November 22, later than the frozen November 2 path. The verdict is on demonstrable coverage in the currently inspected corpus, not historical priority, attribution, or an allegation of derivation from that record. The only domain left, one shore of size one, is mechanically included by the same rank and shifted-block calculation with the boundary multiplicities allowed to vanish.

## value

FAIL

The graph-operation recurrence contrast and all-parity classification are mathematically useful, but that substantive content is covered. The remaining shore-one endpoint is a direct degeneracy of the same incidence calculation, not a justified standalone new invariant or obstruction; no distinct valuable repair remains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
