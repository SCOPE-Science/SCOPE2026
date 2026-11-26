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

The counting ℓ¹ generator norm is twice the largest column exit rate q. For q=0 the generator vanishes. Normalize q=1, write the other exits b,c and t=b+c, and factor the characteristic polynomial of −Q as x times f(x)=x²−(1+t)x+p. The principal two-by-two minors give p=t+bc−∑_{i<j}Q_ij Q_ji≤t+t²/4. For t≥1/2 the mean of the two real parts is at least 3/4; for 0≤t≤1/2 one can independently see f(3/4)≤(2t−1)(2t+3)/16≤0, so there is a real root at least 3/4. This allows zero or repeated eigenvalues and reducible chains. Spectral mapping and norm domination of spectral radius give the logarithmic bound. For the explicit irreducible cycle at (1,1/4,1/4), exact arithmetic gives characteristic polynomial x(x−3/4)², stationary projection P and N=−Q0−(3/4)(I−P) with PN=NP=N²=0 and norm 4/3. Hence the inverse exponential at scaling h grows as e^{3h/4}h(4/3+o(1)) and the ratio tends to 8/3. In two states the nonzero spectral rate is r+s and the exit norm is 2 max(r,s). For exits h,0 the inverse norm is 2e^h−1, proving sharpness of 2; the one-state generator is zero. Replay: python3 /workspace/branches/frozen_math_reproductions.py 2 (SymPy); checks the threshold polynomial and computes the exact cycle projection from the nullspace, nilpotent, characteristic polynomial and norms. The uniform inequalities and scaling limits come from the proof, not the uploaded checker or numerical samples. The uploaded code was inspected, not run.

## originality

PASS

The logarithmic inverse-semigroup problem and even the defective cycle used as witness have existing coverage. Pass the sharp universal three-state coefficient and its sharp largest-real-part form, not the example as a standalone new result, a general M-matrix claim, or an absolute historical-priority assertion. The closest full passages establish different extrema or a weaker logarithmic coefficient.

## value

PASS

The optimal coefficient is a natural extremal invariant for a pre-existing Markov inverse growth problem. It drops the general trace-based coefficient from 6 to the sharp 8/3 in the first dimension where 2 fails, including irreducible examples. The uniform upper estimate for all three-state rate allocations, rather than the already known cycle spectrum, supplies the substantive value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
