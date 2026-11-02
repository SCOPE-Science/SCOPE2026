---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

The actual frozen six-blob Git tree reconstructed exactly to 120fe93f0b866193a1f20b763b71f89815d1f3cf and main returned identical six blob IDs. For the real norm N(x,y)=[|x|^3+((|x|+|y|)/2)^3]^(1/3), the analytic global quadratic comparison with H(x,y)^2=x^2+3^(-4/3)y^2 reduces, including both coordinate axes, to F(t)=[(8+(1+t)^3)/8]^(2/3)/(1+3^(-4/3)t^2) for t>=0. Its endpoint values both equal m=3^(4/3)/4; d(log F)/dt/2 has sign of R(t)-3^(-4/3) where R(t)=(1+t)^2/[t((1+t)^2+8)]. Symbolic differentiation independently confirms R'(t)=-(t+1)(t^3+3t^2-5t+9)/[t^2(t^2+2t+9)^2], and t^3+3t^2-5t+9=t(t-1)^2+5(t-3/5)^2+36/5>0. There is one positive critical point tau, a global maximum M; Hilbert Ptolemy and mH^2<=N^2<=MH^2 give C_Pt<=M/m. Take nonzero distinct x=(-1,0), y=(0,-tau), z=x+y=(-1,-tau): by absolute norm, N(x-y)=N(z)=N(1,tau), while denominator N(x)^2+N(y)^2=[3^(4/3)+tau^2]/4, giving the exact M/m lower bound. Independent 60-digit root/ratio calculation gives tau=2.7667398800787011390685370499587 and C_Pt=1.29958204360103898476109693949. Thus the exact claim and equality witness are correct, with no finite-sample-to-infinite inference.

## originality

FAIL

The 2026-10-04 published exact Banach–Mazur result for precisely the same real norm has the identical tau equation, exact scalar D=[8+(1+tau)^3]^(2/3)/(3^(4/3)+tau^2), and an optimal Hilbert norm H with sharp LOWER contacts on both coordinate axes and sharp UPPER contact at (1,tau). Its proof establishes these global inequalities for all directions, not merely a numerical value. Zuo 2012, Lemma 2.5, supplies the standard norm-comparison upper bound C_Pt<=D. For the old result's axis vectors a=(1,0), b=(0,tau), the defining norm is absolute, so N(a+b)=N(a-b); the old contact equalities force N(a+b)^2/[N(a)^2+N(b)^2]=D. Writing the admissible Ptolemy triple (-a,-b,-a-b) gives C_Pt>=D. This exact prior package plus Zuo's general inequality implies the submitted cubic Ptolemy formula and witness directly, despite the different invariant in the earlier headline. The assigned theorem is therefore a short corollary of published earlier mathematics, not independently original; no weaker title-overlap search is used to make that decision. A same-October-11 Hilbert-distance paper independently writes the same contacts, but same-day chronology is not needed for the rejection. Zuo's 2012 Example 2.10 alone is p=2 and does not directly state the cubic value.

## value

FAIL

The two-dimensional Cesaro section and Ptolemy constant are natural geometric objects, and the submitted calculation is mathematically correct. However, before this submission the exact same norm's optimal quadratic sandwich, algebraic tau, ratio D, and all axis/mixed equality directions had already been proved in the 2026-10-04 Euclidean distance record. The submitted result adds only the standard Hilbert Ptolemy comparison (already in Zuo Lemma 2.5) and the immediate choice z=x+y for the old sharp contact vectors. This is a mechanical corollary, not an independently unknown exact invariant or a motivated new structure beyond the existing strong result. The distinct invariant label and an explicit witness do not by themselves constitute substantive mathematical value at the stated research bar. It is suitable as a short expository observation, not a separate accepted research finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
