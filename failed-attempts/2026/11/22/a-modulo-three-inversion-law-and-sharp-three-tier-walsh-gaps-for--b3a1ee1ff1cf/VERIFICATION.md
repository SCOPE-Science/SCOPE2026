---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

On the full Boolean edge group the normalized Walsh characters diagonalize the counting convolution, with eigenvalues the unnormalized signed matching sums. Cutting at used rungs forces identical horizontal matchings on the remaining row paths; no-rung matchings give just the two coincident and two opposite alternating tilings at even circumference. Factoring out all rung signs gives the stated cycle transfer trace and, in even length, the two opposite-offset products U,V with UV=product(y_i). Flipping the upper and lower signs together at one column preserves all y_i while flipping both U and V, which justifies all attaining choices. The all-positive count is Lucas plus two in even length, and its parity excludes zeros off multiples of three. The single plus among otherwise negative y_i gives trace zero by B(-1)^3=-I and trace(B(-1)^2 B(1))=0; at even multiples the odd number of minus signs cancels U+V. At 6|n both the total and every signed sum are divisible by four: the count is 0 modulo four by the sixth power of B(1), and rung and horizontal usage counts F_n and F_(n-1)+1 are even (remove the occupied columns to obtain path tilings, plus one mixed matching for each horizontal edge). All-negative y_i gives trace 2 cos(n pi/3), giving magnitude one in the nonresonant odd case, one with U+V=2 in the nonresonant even case, two at odd multiples of three, and four at even multiples with U+V=2. The trivial character attains the triangle-inequality maximum, including n=3. The deposited verifier transforms every mode through n=7; its separate formula comparison is exhaustive only through n=5 and uses 2,000 test entries at each of n=6,7. Independent edge-subset enumeration and exact transforms confirmed counts 4,9,11,20,29, positive gaps 2,1,1,4,1, and nullities 192,0,0,124928,0 for n=3..7. Replay: python /workspace/branches/90d33f67-8f9c-4545-9567-17f2317df09a/prism_independent_check.py. Finite results corroborate, not prove, the all-length theorem.

## originality

FAIL

The earlier November 16 Resultary record covers the same unnormalized edge-incidence convolution, the entire pointwise signed multiplier formula, the invertibility boundary, and the sharp 1/2/4 positive singular-value law. It actually gives more information on zero multiplicities. The particular compact witness and choice of trigonometric evaluation in the November 22 proof do not produce a new claimed spectral invariant. The newer condition-number wording is an immediate consequence of the prior gap and the prior exact count via the trivial frequency.

## value

FAIL

The prism inversion and gap law is a natural exact invariant, but this record presents it again with only immediate reformulations (the maximal singular value and ratio) and a convenient alternative attainment proof. It identifies no new family, quantitative stability phenomenon, independently needed certificate, or improvement on the earlier zero-mode result. A correct reproduction is useful as a check, not a distinct finding. No genuinely new valuable corrected claim was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
