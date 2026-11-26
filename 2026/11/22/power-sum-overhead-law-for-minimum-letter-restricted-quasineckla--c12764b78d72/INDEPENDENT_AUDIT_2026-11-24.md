# Independent mathematical audit

## correctness

PASS

A nonconstant candidate has a unique initial zero run of length L and successor t; each remaining nonzero finishes a block with 0 through L zeros, and a block with L zeros has s-t+1 possible successors instead of s. The product counts literal words without either a missing cyclic boundary condition (the last letter is nonzero) or overcounting ties. For m=0 the sole word is all zero; for m=1 the empty product forces L=r. The bivariate identity follows by a formal geometric sum. In Burnside's count a rotation of order d fixes d repeats of a block and requires d to divide both counts. At fixed r and s, L=1 contributes binom(m-1,r-1)s^(m-r) times the power sum; L>=2 leaves only r-2 or fewer zeros to distribute and is O(m^(r-2)s^m). The identity rotation has leading term m^(r-1)s^m/r! and the others have at most s^(m/2) times a polynomial at fixed r. This proves the stated limiting ratio, ternary specialization, and growth after the m-limit. The L=1,2 terms give the exact two-zero law. Independent tuple/run classification and orbit-set enumeration matched the formulas on 72 slices and 86,870 words for s=2,3 and total lengths 1–8 (python3 /workspace/branches/independent-replay.py 3).

## originality

PASS

The exact binary prior is credited, not reclaimed. No inspected source gives the nonbinary fixed-zero enumerator and conditional power-sum ratio; the primary global theorem neither fixes this count nor implies a conditional bound. This is a best-of-current-knowledge decision, not a claim of historical priority.

## value

PASS

The slice corresponds to a natural constraint when generating necklace representatives. The exact rule shows which candidate counts are inflated by ties, and the precise unbounded r/s growth after the m-limit exhibits a failure of uniform conditional overhead despite a global constant bound. It is useful as a benchmark for filtering, not a lower bound on every generator's runtime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
