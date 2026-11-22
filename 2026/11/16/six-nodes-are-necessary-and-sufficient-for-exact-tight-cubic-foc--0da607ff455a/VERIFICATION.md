---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

PASS: Polarization reduces the norm identity to 16 exact complex bidegree moments sum w z^j zbar^k=j!delta_jk for 0<=j,k<=3. At N<=5, a nonzero real quadratic Q vanishes on all nodes. Integrating Q,Qz,Q zbar and Q(|z|²-1) through those 16 moments forces the coefficients of |z|², z,zbar,constant to zero, leaving a nonzero harmonic quadratic whose zero set is two perpendicular lines. On each line, three odd moments and <=3 occupied sites force a single equal-weight antipodal pair; from second and fourth moments each line has radius²=2 and contributes sixth moment 2, summing 4 instead of required 6. Thus no-five-node impossibility is analytic, not numerical. At six sites ±sqrt((5±sqrt17)/2), ±i sqrt2 with claimed weights, independently checked all sixteen symbolic moments exactly using SymPy. In the centrally symmetric case, three distinct squared radii and the two even off-diagonal moments force opposite axes and the middle radius²=2; the remaining two-atom real radial moments force roots of s²-5s+2 and unique positive masses, while Vandermonde odd moments force equal within antipodal pairs. Unrestricted six-node uniqueness not claimed.

## originality

PASS

PASS best-of-knowledge: prior quadratic-Fock exact four-node result concerns degree two, and one-radius sampling rigidity excludes multi-radius designs. General Fock Marcinkiewicz–Zygmund inequalities and Gaussian quadrature theory do not, in inspected parts, give the exact cubic mixed-bidegree six-node minimality with central symmetry classification; older Gaussian cubature tables remain material priority risk.

## value

PASS

PASS: A natural fixed-degree complex Gaussian Fock quadrature problem gets a sharp global minimal positive node count, an explicit algebraic rule, and a rigidity theorem within central symmetry; lower bound via a constrained zero-set argument is a useful structural obstruction for exact complex sampling, not a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
