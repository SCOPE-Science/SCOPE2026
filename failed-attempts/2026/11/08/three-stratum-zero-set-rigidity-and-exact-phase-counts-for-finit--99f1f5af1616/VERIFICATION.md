---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The p- and 2^s-cyclotomic fields are linearly disjoint, so Φ_p is irreducible over Q(ζ_{2^s}); a Fourier zero forces equality of p grouped sums, and proper support supplies an empty group. For a≠0 the fibers of ax²+bx are fixed point c=-b/(2a) plus pairs {c±t}; a vanishing sum forces equal-exponent opposite coefficients in each occupied pair, and no nonzero linear frequency has a zero. A nonempty proper R has at most one reflection centre, proving empty/origin/L_c trichotomy. At (0,0), Φ_{2^s}(T)=T^{q/2}+1 forces matching opposite phase occupancies n_j=n_{j+q/2}; their multinomial count is A_{q,r}. Unique symmetric supports number p*C((p-1)/2,r), with q^r line assignments each. The q=4 simplification is Vandermonde: A_{4,r}=C(2r,r)^2. Independent sympy-cyclotomic quotient checks reproduced every actual Fourier zero for 2,100 cases at (p,q)=(5,4) with 1≤k≤4, 938 cases at (7,2) with 1≤k≤4, and 256 assignments on R=(0,1,3,5) at (7,4), all matching the predicted zero geometry and class counts. The original CHECK.py was read and its stated total 45,188 cases and 1,528,052 Fourier evaluations are arithmetically consistent, but its full run was not repeated. The infinite claim rests on the proof, not those checks.

## originality

FAIL

The exact geometry follows by direct specialization of Lam–Leung (1995), Theorem 3.3(2): any zero sum of k<p p·2^s-th roots is a union of opposite pairs; the quadratic fibers force precisely the stated reflection line. The origin balance and all supportwise/global multiplicities are immediate multinomial/reflection-orbit counting. Moreover the q=2 instance, including its exact counts, was published as the 2026-10-18 rational-data theorem. The q>2 formulas were not found printed identically, but no independent mathematical theorem or nonroutine enumeration remains after stronger prior coverage.

## value

FAIL

The exact-zero question is natural in polyphase Fourier/MUB sampling, but this particular claimed advance is a routine application of the existing comprehensive two-prime-factor root-of-unity vanishing-sum theorem to a quadratic fiber map, followed by elementary phase occupancy and reflection-pair counting. Its q=2 classification/counts are published already, while the remaining q>=4 extension introduces no motivated new structural lemma or irreducible combinatorial computation. Thus correctness and reproducibility do not supply a new valuable mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
