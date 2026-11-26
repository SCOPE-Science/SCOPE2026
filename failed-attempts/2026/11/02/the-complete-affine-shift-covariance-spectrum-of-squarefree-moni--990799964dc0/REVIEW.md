# Independent mathematical audit

## correctness

FAIL

The centered counts and the frequencies assigned to those counts are correct. The Finding first correctly defines the covariance as Δ_q/q³, but then asserts in its frequency paragraph that the nonzero values −1, 2q, and −q are covariances. They are centered counts; the covariances are −1/q³, 2/q², and −1/q². For example over F₇ every nonzero-slope shift has covariance −1/343, not −1. The same error is in the slogan. For the underlying count, each nonsquarefree cubic determines a unique repeated root r, and two repeated roots r and s for the two translates must differ because a nonzero affine shift cannot have a double root. Write f=(T−r)²(T−s+b) and d=s−r. Vanishing of the value and derivative at s determines b=−h(s)/d² and gives d³=2h(s)−ud=u(s+r)+2v, with a unique inverse for every solution. For odd q, (d,s+r) are independent coordinates: a nonzero slope gives q−1 solutions, and a constant shift gives q times the number of cube roots of 2v. For even q the equation becomes d²=u with d≠0, giving q solutions for u nonzero and none otherwise. This covers characteristic three too. Both marginal nonsquarefree counts are q², so Δ_q is the joint nonsquarefree count minus q. Direct independent cubic-discriminant enumeration of every shift for q=2,3,5,7,13 agreed with the centered-count formulas (replay: /workspace/branches/independent-checks/record4.py); the frozen verifier was read but not executed and tests counts, not the mislabelled covariance. Correcting the numerical labels alone leaves the originality and value failures below, so no repair is delivered.

## originality

FAIL

The closest distinct Resultary record states results for exact quadratic shifts in odd characteristic, but its proof already derives the general repeated-root incidence identity before any quadratic substitution. The entire frozen affine spectrum follows from projecting that identical incidence over the field; the characteristic-two branch is immediate from the same unspecialized equations. This is demonstrable coverage in a distinct indexed record, not a claim of priority inferred from the shared date.

## value

FAIL

Exact low-degree squarefree-pair benchmarks for asymptotic theory are a natural object. Here the numerical affine spectrum is the routine linear/cube-map/Frobenius case split of a general cubic incidence already explicitly derived in the closest result. The covariance relabeling is only a normalization correction. There is no distinct substantive mathematical remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
