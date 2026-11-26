# Independent mathematical audit

## correctness

PASS

Translate a run of length R to offsets 0 through R-1. For a shift h the same-letter positions are the beginning of that run up to offset R-h (exclusive) and its end starting at offset p-h (inclusive), clipped to the run. For s<t the earlier shift supplies the larger beginning interval and the later shift supplies the larger ending interval. Thus the bad offsets are exactly the integers in [max(0,R-s),min(R,p-t)), giving the frozen sum after clipping the length at zero. For positive s and u=p-t, the gap is empty exactly when s+u<=R. Summing over all runs gives the shortest-run rule. For the budget impose p-B<=u<=r-1 and sum r-u over these integers, including an empty range if r=1 or B<p-r+1; at the first nonempty budget only u=r-1 and s=1 qualify. The single occurrence per cycle of the ordered a0-to-a1 boundary proves primitivity, and the admissible positions in P^k include all residues since kp-t>=p for k>=2 and t<p. In (00101)^omega the shifts 2 and 3 reach the starting symbol at every residue, confirming the distinct-run qualification is needed.

## originality

FAIL

The frozen claim includes a complete pseudoperiod classification, parametrization and total count that match a distinct indexed result under the very same assumptions. The budget and least-delay formulas are immediate consequences of that result. The exact nonzero defect counts are not stated in the inspected comparison; failure is not a claim that the complete defect formula was previously printed. Displayed path dates do not resolve priority but do not erase the overlap.

## value

FAIL

The class and sharp delay question are natural, but the classification is already represented, the budget just truncates the known triangle, and the finite-copy criterion is a direct check of residues. The only supported distinct remainder is the number of integers between two clipped endpoints in each run. No separate approximate-pseudoperiod problem, structural feature of the nonzero spectrum or mathematical use of these magnitudes beyond their already classified vanishing is established. On this evidence there is no motivated nonroutine surviving claim to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
