# Independent mathematical audit

## correctness

PASS

The arithmetic table is correct for all coprime q>5 and counts linear pairs. For n≤4(q−1)<5q, the coefficient is the semigroup-membership difference B(n)−B(n−1). At a junction n=jq the new stage adds only the residue of jq, so testing the current stage at n−1 gives exactly the previous stage's membership there. This validates the periodic support pattern even at the stage start. The first three stages have length q, and the last has length q−3. In the four base words at q=6,7,8,9 each stage has at least two support sites (counts per stage are (3,2,2,2), (4,6,5,2), (4,7,6,2), (4,4,4,3)). Increasing q by five adds one period to each stage; its first and last internal gaps and its adjoining bridge gaps are unchanged. The new internal adjacent-pair counts are one cyclic pass per stage, giving the stated increments and no wraparound. The independent truncated-series reproduction `python /workspace/branches/audit_arithmetic_reproduction.py 5` matched all dictionaries at 396 parameters. The submitted verifier was inspected, not executed. The finite checks are corroboration, not the proof.

## originality

FAIL

The uniform table is mechanically implied by Cafure–Cesaratto's earlier compact coefficient-word theorem (not merely by computing the polynomial separately at each q). At p=5 the theorem gives the very four five-periodic stages of the claimed proof, their affine lengths and their phases; a fixed local statistic of the blocks returns the claimed affine table. The composite-q range also follows from the same published word derivation with the elementary truncated rational identity. No independent novelty attaches to the fact that the earlier paper does not print this particular table.

## value

FAIL

Consecutive gaps are a natural statistic, and the table can save manual reading. But for fixed conductor five the claimed addition is a bounded local count of already published explicit five-letter blocks and fixed splices. The stated rigidity for r=2,3 is immediate from those same blocks. No separate nonmechanical result survives this coverage comparison; no repair is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
