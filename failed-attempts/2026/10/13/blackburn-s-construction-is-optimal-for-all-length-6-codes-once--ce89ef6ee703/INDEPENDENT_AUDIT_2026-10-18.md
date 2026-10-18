# Independent mathematical audit

## correctness

PASS

Starting from the Stanovnik–Moškon–Mraz exact SQN integer recurrence, fix a=x1≤b=y1 and relax x2,x3,x4 to r,s,t∈[0,1]. The normalized objective F is a rational polynomial with multidegree (6,3,2,1). Independently constructed its exact Bernstein transforms: 168 coefficients of p(1-p)^5-F on p∈[0,1/5], all nonnegative (min0); eight halfboxes of (r,s,t) for 1024/15625-F on p∈[1/5,1/2], all 168 coefficients nonnegative (all mins≥0). Independently expanded integer q=5k+j, k≥2, j=0..4, and verified every polynomial coefficient of 15625*k*(4k+j)^5-1024*(5k+j)^6 after k=h+2 is ≥0. This is an exact rational polynomial proof for ALL q≥10, not a finite sample. Original certificate.json/verify.py and RESULT.md checked.

## originality

FAIL

A previously published October 4, 2026 Resultary finding states EXACTLY S(q,6)=max_{1≤l<q} l^5(q-l) for every integer q≥10; the complete earlier RESULT.md was fetched and read. The prior proof is independent algebraic analysis of the same Stanovnik recurrence. The submitted formulation is mathematically equivalent with identical hypotheses, threshold, and conclusion; a second Bernstein route cannot make the same theorem original.

## value

FAIL

The purported substantive gap—eventual Blackburn optimality at n=6 starting q=10—was already filled exactly by the earlier published theorem. The new proof format may be an alternative verification argument, but neither a new boundary, distinct structural classification, nor another mathematically motivated non-implied invariant survives in the final claim. A known theorem with a different certificate does not meet the research-value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
