# Independent mathematical audit

## correctness

PASS

The probability and uniqueness assertion is true. Independently, S=B^T B−B since B_ii=1. In row i, each term from k≠i is zero if B_ki=0 and otherwise counts two forced entries plus Bin(n−2,p). In column i the same term has just one forced entry, while row k=i contributes Bin(n−1,p) independently. This gives exactly the two moment-generating functions and K_R,K_C bounds in RESULT.md, including n=2 and p=1. Markov/union and ||S||_2≤sqrt(||S||_1||S||_∞) give the asserted norm event. The uniqueness criterion is Theorem 3.3 of Cheng–Deng–Ma's accessible proceedings text, not the cited Theorem 3.6 (equivalence of games); concavity of the clipped benefit plus c_0-strong convexity of cost gives the required c=c_0, and L_0=2b. The paper's older random threshold is Theorem 4.2, not 4.3. Its proof's one-sided norm inference is invalid in this model: B with rows (1,1,0,1),(1,1,1,0),(0,0,1,0),(0,0,0,1) gives ||S||_∞=3 but ||S(2,2,1,0)^T||²=82>9·9. The frozen argument does not make this error. A second proof of the equilibrium bound is the exact best-reply reduction below.

## originality

FAIL

The frozen uniqueness result is mechanically implied, with a strictly better explicit sufficient threshold, by an existing diagonal-dominance result after exact best-reply reduction. Different payoffs do not imply different equilibrium equations here. The two-sided overlap-norm route does repair a defect of the older paper's route, but no overlap-norm theorem is separately claimed in the Finding.

## value

FAIL

As a Nash-uniqueness finding, the claimed improvement is a looser sufficient condition than the one obtained by substituting the exact best-reply map into an existing directed-network criterion and taking a single binomial exponential-moment bound. The exact overlap constants are conservative proof intermediates, with no independent use or sharpness established in the Finding. Correcting theorem numbering or adding finite tests would not restore the purported contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
