# Independent mathematical audit

## correctness

PASS

The frozen RESULT.md proof was independently reconstructed with the normalizations ⟨u_i,u_j⟩=-1/d, sum u_i=0, sum u_i u_i^T=(d+1)I/d. The analysis y_i=⟨u_i,x⟩ maps the unit sphere bijectively to sum y_i=0, sum y_i²=(d+1)/d, with inverse x=(d/(d+1))sum y_i u_i. For h=min|y_i|>0, b=y/h has |b_i|≥1 and two nonempty sign groups of sizes p and q=m-p. Let positive mass s=negative mass≥max(p,q). Cauchy gives sum b_i²≥s²(1/p+1/q)≥m max(p,q)/min(p,q). Thus h²≤min(p,q)/(d max(p,q)), optimized by balanced p,q. Equality requires constant sign-group magnitudes, larger group magnitude 1, smaller group magnitude max/min; b from RESULT.md realizes equality. Hence the formulas tau_d²=1/d for odd d and 1/(d+2) for even d, with exact equality direction vectors, antipodal line counts, and zero-sum reconstruction, are correct for all integers d≥2. Covering the ball follows by radial contraction from sphere; t<tau leaves the equality unit vector uncovered. Angular distance to normal great subsphere equals arcsin|y_i| and full zone width is 2 arcsin tau. An independent bounded exact-Fraction checker verified the sign-size rational optimization, Gram normalization and equality witnesses for d=2..100 and tested 19,000 Gaussian-sampled zero-sum directions at d=2..20; these finite diagnostics do not prove the infinite dimension quantifier.

## originality

FAIL

A directly relevant, genuinely earlier primary mathematical source was missed in the original comparison: Har-Peled–Robson (2023), Lemmas 1.2–1.3, derives the same balanced two-level projection vectors, precise magnitudes and parity split as the proposed extremizers. A separately published related regular-simplex result writes the same balanced subset-sum norm exactly. The submitted fixed-plank objective is not literally the prior simplex-width objective, but its entire threshold, equality set, and binomial line counts are routine algebraic consequences of that known balanced subset-sum geometry: for sign groups of sizes p,q, sum_{positive} <u_i,x>=s>=max(p,q) h while s<=||sum_{positive}u_i||=sqrt(pq/d). Therefore h<=sqrt(min(p,q)/(d max(p,q))) with equality for precisely the known balanced two-level subset-sum directions. The maximum gives h=1/sqrt(d) for odd d and 1/sqrt(d+2) for even d, with all equality directions and their counts. This provides demonstrated mathematical coverage of the claimed higher-even novelty, not merely similar wording or a failed search. The difference in optimization vocabulary is acknowledged; the older sources do not state this named covering threshold verbatim.

## value

FAIL

The threshold of centrally positioned equal planks for fixed regular-simplex normals is a natural geometric number, and its zone interpretation is valid. However, the entire claimed higher-even contribution—the balanced unequal two-level directions, exact angular cutoff and line counts—is a short normalization/corollary of published regular-simplex width optimizer geometry and the published subset-sum norm identity. The only additional step is s>=max(p,q)h<=||sum_P u_i|| with a trivial balanced cardinality optimization; the paper supplies no independent structural lemma, unknown invariant beyond those prior optimizer coordinates, or new covering phenomenon. Under the shared mathematical-value standard this is an informative reference corollary, but a routine deduction from known work rather than a separately valuable new research finding. This is not a rejection for finite dimension, lack of a downstream theorem, or mathematical incorrectness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
