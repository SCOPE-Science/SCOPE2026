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

The coefficient normalization and valuation identity in RESULT.md lines 5–9 and 38–41 exactly agree with Amdeberhan–Manna–Moll, Eq. (1.1) and Theorem 1.1. With w=2ell the centered quantity is a window sum of nu_2-1. For fixed nonnegative offsets bounded by b, second-moment tails of nu_2(n+j) at cutoff M, averaged over 1<=n<=N, are bounded by (1+b/N) times the sum of d^2/2^d for d>=M, by counting multiples up to N+b. Cauchy–Schwarz gives convergence of the product tails, justifying the Haar computation for consecutive averages. In the double divisibility expansion, terms with smaller exponent k are compatible precisely if 2^k divides the shift, and their total weight is 3*2^(-k), yielding the stated kernel and finite triangular sum. At every dyadic modulus q, window residue counts have a constant part and a single arc of length w mod q; the overlap is minimized at shift w. Parity reduction gives Var(F_2w)=Var(F_w), so the minimum covariance is -Var(F_w)/2; the variance is positive since the window sum is unbounded on positive-measure cylinders. Intersecting minimum overlap conditions at P and P/2 leaves exactly +/-w mod P, including a singleton when w=P/2. These residues minimize all smaller scales by symmetry and have no higher-scale collisions because no index difference of magnitude less than w can represent them modulo P. Zero shift maximizes each overlap; any fixed positive shift has a strict deficit at a sufficiently large scale. At 2^j the first j overlaps agree with zero shift and the remaining weighted tail tends to zero. An independent bounded integer check of 2*C_w(h)+C_w(0), using the displayed kernel with denominator 4P, confirmed the minimum and equality for w=2,4,6,8,10,22,30,32,34,64,66 over 0<=h<3P; this is corroboration only. Frozen CHECK.py and VERIFICATION.md were inspected, not run; the former's reported exact checks do not establish the universal result.

## originality

PASS

Credit the known valuation and binary digit-sum variance theory, which already implies an exact way to evaluate every covariance and the value at h=w. The supported distinct claim is the global sharp anticorrelation bound with the complete set of equality shifts. The inspected single-increment and valuation laws do not directly give the all-lag inequality or its equality arithmetic.

## value

PASS

The minimum correlation and all equality residues are exact invariants for a mathematically natural family of arithmetic sequences. They determine the strongest opposing lags without search or enumeration; the distinct dyadic near-recurrence at maximal correlation clarifies the behavior at the opposite end. The established value is the extremal classification, not merely evaluating known digit-sum moments under another name.

The dated certificate retains the supplied scientific assessment, sources and limitations.
