# Independent mathematical audit

## correctness

PASS

Diagonal scaling gives r=C y and the relaxed update on i gives r_i'=(1−ω)r_i, r_j'=r_j−ω c r_i. The objective decrease of a step is ω(2−ω)r_i²/2. The first-step expectations agree, so the gap is ω(2−ω)/8 times the sum over first indices i of (r_j−ω c r_i)²−(1−ω)²r_i². Expanding recovers the stated formula. The smaller eigenvalue of its bracket is (1−|c|)[2−ω(1+|c|)]; the larger is positive, and all r are attainable. This verifies equality at the threshold and both signs above it, including the no-reversal case c=0 in 0<ω<2. For c=1/2 and ω=3/2, substitution gives −9/256 and 135/256 in the two modes. κ refers only to the normalized Hessian. The supplied script was inspected, not executed; the proof and exact spot checks are independent of its finite enumeration.

## originality

FAIL

The distinct Resultary record 1370f23f939c proves the identical all-starts objective-gap identity and frontier under the same budgets and relaxation range, in normalized energy coordinates and with an optional linear term. This is demonstrated mathematical coverage, not a claim about authorship or priority inferred from a date.

## value

FAIL

The two-coordinate reversal is a meaningful phenomenon, but the submission's exact gap and sharp boundary are already available in the covered theorem. The conditional-expectation presentation, normalized condition-number notation and different rational witnesses yield no distinct cutoff or consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
