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

If N>D, the squared weights decrease strictly to one, violating the weighted-shift hyponormality necessary for subnormality. The diagonal has Berger measure delta_1. For N<D, contractive subnormal Schur powers have Hausdorff moment sequence gamma_n^s, where gamma_n is the product of squared weights. Divide the order-r+1 Hausdorff inequality by s and let s decrease to zero: the constant term vanishes and Delta log gamma_n=-h_n, yielding (-1)^r Delta^r h_n>=0. The log series gives h_n as moments of the finite signed measure sum c_k delta_(q^k), with |c_k|<=2rho^k/k for rho=max(|N|,|D|)<1. Polynomials are dense on [0,1], so this finite signed measure is the unique one with those moments and must be positive. For any real q=1/p in (0,1) its atoms are distinct, so c_2=(N^2-D^2)/2>=0 forces N<0 and N<D<=-N. There all even coefficients are nonnegative by absolute-value comparison, all odd ones positive by order of the parameters; at equality precisely the even coefficients vanish. The b_k=c_k/(1-q^k) are summable by 1-q^k>=1-q, and summing h_j over j<n gives log gamma_n=-sum b_k(1-q^(kn)). Independent Poisson counts of means sb_k have finite total count almost surely; evaluating their generating function at z=q^n gives exactly gamma_n^s. The Berger criterion and Hausdorff determinacy prove existence and uniqueness, and the constant coefficient is e^(-sB). Independent replay: python3 -I -B /workspace/reproduce.py 2 tested three rational bases, 84 fractional-power moments from a generating-function coefficient recursion with a bounded numerical truncation used as corroboration, and six exact nonpositivity certificates by rational tail bounds on t^30(t-q)^2. The uploaded checker was inspected only. The arguments above, not these examples, handle the real parameter range.

## originality

PASS

The general logarithmic criterion, MID sufficiency in Sectors I and II, ordinary subnormality in Sector III and the ordinary (s=1) Berger measure are prior coverage. The remaining result gives the conjectured full nontrivial MID boundary for individual shifts and an explicit compound-Poisson description for all positive Schur exponents. In particular the entire forbidden portion is excluded without restrictions on p. Inspected later quotient and signed-charge passages treat different criteria and do not settle those statements. This is a bounded comparison, not a historical priority guarantee.

## value

PASS

The theorem settles an explicit boundary question within a standard weighted-shift family: ordinary subnormality and divisibility of the moment sequence separate throughout the full adjoining sector. A single signed logarithmic atom detects the separation uniformly in the base. The constructive all-power law supplies normalized masses, the atom at one and the boundary jump parity, rather than just an existence statement or a finite positivity test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
