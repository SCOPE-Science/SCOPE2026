---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-20.md",
      "INDEPENDENT_AUDIT_2026-11-20.json"
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

The claim is mathematically correct. For row generators Q with off-diagonal rates >=0, Q1=0 and spec(Q) in Re z<=0; the Radau denominator zeros 2±i√2 are excluded so r(hQ) exists, and r(0)=1 preserves row sums. Exact expansion r(z)=1+z+z²/2+z³/6+z⁴/36−z⁵/108+O(z⁶) implies each reachable off-diagonal entry has a positive leading term a_d(Q^d)_{ij}h^d at shortest path length d<=4 in n<=5; unreachable entries vanish identically and diagonals start at 1. For the given six-state absorbing birth chain, independently reconstructed nilpotent Jordan functional calculus yields all five candidate c_0..c_4 expressions and all five absorbing b_1..b_5 identities, with b5=h5 P(h)/D(h)^5. All c_0..c_4 and b_1..b_4 are nonnegative on [0,3]; P is strictly increasing for h>0 and has unique positive zero alpha in (1/4,13/50). For (0,alpha), b5<0, for [alpha,3] all entries nonnegative, and for h>3 c0=2(3−h)/D<0. Independent SymPy exact simplification and independent rational 6x6 inversion at h=1/10,1/4,13/50,1,3,4 confirm the identities, row sums, signs, and alpha≈0.253946561637298. No finite extrapolation is used for universal n<=5 or exact interval.

## originality

FAIL

Decisive prior coverage. The 2026-10-27 published RESULT explicitly proves the identical universal CTMC n<=5 small-step positivity statement and the identical sharp minimal dimension six for r(z)=(6+2z)/(z²-4z+6), with a different six-state witness. The 2026-10-13 published RESULT proves the exact same absorbing homogeneous six-state birth-chain set {0} ∪ [eta,3], where eta is the same unique root of h^5+30h^4+180h^3+360h²+180h-72; it also proves the n<=5 hierarchy. On 2026-11-02 a stronger published birth-chain feasibility theorem repeats that exact n=6 interval and treats all n>=2. Together the October 27 and October 13 statements imply every scientific assertion in this November 8 claim. This is not merely matching titles or parameters, or later coverage. The previous package originality comparison missed these direct predecessors.

## value

FAIL

The sharp state count for loss of small-step Markov positivity and the exact re-entrant safe-step set for a canonical absorbing birth chain are mathematically natural and intrinsically meaningful. However this submission adds no new classification, boundary case, structural lemma or unknown invariant: the exact interval and polynomial already appeared 2026-10-13 and were restated in a stronger birth-chain result 2026-11-02, while the entire universal five-state guarantee and six-state sharpness appeared 2026-10-27. As a new result it is a recomputation/combined restatement of already published exact facts, with no substantive mathematical gap remaining. Correct algebra and reproducibility do not make a covered repetition scientifically valuable as an independent finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
