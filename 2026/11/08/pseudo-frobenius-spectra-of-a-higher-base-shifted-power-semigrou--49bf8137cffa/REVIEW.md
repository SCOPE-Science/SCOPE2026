# Independent mathematical audit

## correctness

PASS

The weights for offsets 1,u,v are h,h²,h³. Replacing u unit coins lowers cost, so the 1,u optimum is H(M)=h² floor(M/u)+h(M mod u). Since v=hu+t and u−t=h, H(M+v)−H(M) is h³+ht before the residue wrap and h³ after it. This proves, without assuming strict improvement, that the maximum number of v-coins is optimal, giving O(M)=h³ floor(M/v)+H(M mod v). Coprimality makes offset classes bijective and a=mv gives O(r+ja)=O(r)+jmh³, so the minimal representative at residue dr is aO(r)+dr. For a generator ca+db, adding it to W_r−a requires O(r+b)−O(r)≤c−1 when unwrapped, and O(r+b−a)≤O(r)+c−1+d when wrapped. The first tests for v and then u exclude everything except the last u positions; the unit test excludes the nonboundary positions except s=hu−1 in the last v-block. The right endpoint s=v−1 also survives. Both have H(s)=2h²(h−1). Their u-steps wrap to h−1 and u−1, whose H values are lower; the v-steps wrap to s itself with sufficient cost, and the unit boundary step wraps to zero. Their offsets differ by t, giving F−dt and F, including the nonminimal m=1 case. Summing the block cost and the d-weighted residues yields the displayed genus. An independent integer Dijkstra/Apéry test on the 36 coprime triples with 3≤h≤6, 1≤m≤3, 1≤d≤4 matched PF and genus, including {895,899} and 504. Replay paths: branches/f1a4b85c-c28d-40ff-b434-61b3481dc1cc/record4_independent_check.py and record4_independent_box.txt. The frozen verifier, recorded 300-case log and notes were inspected, not executed; finite tests do not prove the general claim.

## originality

PASS

The weighted family and Apéry framework are established, and the m=1 restriction is covered by an earlier three-generator result because the fourth generator is redundant. The supported distinct contribution is the explicit PF/genus/F classification when the new offset v is a proper divisor of a, i.e. m≥2. No inspected statement gives or mechanically subsumes that range.

## value

PASS

Alignment of a with the top offset is the natural regime where the weighted cost is exactly periodic and the Apéry problem separates into blocks. The resulting type-two formula and exact gap between the PF numbers solve the terminal-divisible subfamily of a previously posed weighted Frobenius family, with an actual additional generator for m≥2. The simultaneous formulas for PF and genus are more than a finite recomputation or a redundant-generator restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
