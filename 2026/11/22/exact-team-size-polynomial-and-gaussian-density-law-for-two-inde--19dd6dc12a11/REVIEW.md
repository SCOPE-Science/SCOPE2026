# Independent mathematical audit

## correctness

PASS

On two variables an independence team is exactly a rectangle (or empty); lax union means Boolean rank at most two, not a disjoint cover. A two-rectangle cover has nonempty row patterns among A,B,A union B. Zero, one or two distinct patterns always work; three work exactly with incomparable A,B and their union, and the minimal two patterns identify the pair without overcounting. Inclusion–exclusion applies to using every distinct nonzero pattern across labelled rows, even if their sizes coincide. The four atom sizes of A,B give the stated multinomial regrouping. In the independent factor model both exclusive column codes and all four row codes occur off an exceptional set of probability at most 6(3/4)^N. On this event the three nonzero patterns determine the factors up to exactly two ordered encodings; every other coverable matrix has an encoding in the exceptional set. This bounds the exceptional mass under both laws and proves the TV transfer. For the symmetric kernel the conditional means on 00,10,01,11 are 0,1/2,1/2,3/4; hence mean 7/16 and projection variance 19/256. Orthogonality of the zero-conditional-mean remainder (even when two terms share one index) gives variance 25/(256N^2); the two projections contribute 38/(256N), leading to the stated Gaussian limit by the i.i.d. CLT and the TV bound. The exact finite moments are for the factor model only. Independent row enumeration, positive multinomial counting and direct rectangle unions agree at all 16 sizes 1<=m,n<=4, including totals 356 and 8776. Exhaustion of order-four encodings confirms moment values 7/16 and 177/4096 and multiplicity two on every output with three distinct nonzero row patterns. Replay: python3 /workspace/reviews/reproduce.py 2; /workspace/reviews/reproduce-output.txt. Frozen code was inspected, not executed; the run does not establish the asymptotic theorem.

## originality

PASS

The square unweighted counts and generic factor uniqueness are genuine prior material. The strongest uniqueness theorem, read in DeSantis et al.'s OA arXiv copy, already gives rank-two factor uniqueness in the presence of a 2x2 permutation submatrix; the frozen generic event ensures such a submatrix. No inspected source supplies the weighted polynomial for labelled rectangular alphabets or the probabilistic result on distinct matrices. The latter needs an additional measure comparison controlling the exceptional outputs, and evaluation of the fluctuations, neither of which follows as a specialization of the deterministic uniqueness statement. The article experiments with rank-five planted identity blocks, not a uniform law on distinct rank-two teams.

## value

PASS

The size distribution refines a known unweighted class on arbitrary labelled rectangular domains, and the square limit answers a natural observable of uniform distinct covers. Distinguishing distinct outputs from factor encodings matters: the proof controls the multiplicity bias rather than assuming it away. Together the explicit coefficient formula and quantified Gaussian law supply useful size-resolved information not present in known totals or deterministic uniqueness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
