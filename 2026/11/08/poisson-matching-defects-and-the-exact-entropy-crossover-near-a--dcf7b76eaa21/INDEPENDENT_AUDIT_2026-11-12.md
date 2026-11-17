# Independent mathematical audit

## correctness

PASS

PASS: Each missing edge is an antipodal-arc event of probability q=lambda/n^2. Pairwise independence holds even for edges sharing one vertex; matching failure has expected overlapping-edge pairs O(1/n). All finite factorial moments converge to Pois(lambda/2) by bounding nonmatching union types using spanning forests. Exchangeable labelled matchings are uniform conditional on the defect count. For the entropy constant, bad graphs contribute o(1) entropy using E[M 1_bad]=O(n^-1/2); log N(n,m)=2m log_2 n-m-log_2 m!+O(m^2/n), and Poisson entropy cancellation yields lambda log_2 n+(lambda/2) log_2(e/lambda)+o(1). Direct rational-grid checks validated conditional incident edge independence and matching enumeration, not the asymptotic statement.

## originality

PASS

PASS, best of knowledge: Vippathalla–Coon–Badiu (2026) studies fixed radius hard geometric graphs on cubes and tori and leading n log n entropy, not a shrinking antipodal defect arc with q=lambda/n^2 nor the constant entropy term. A later fixed-radius geometric entropy release similarly does not establish this window. Standard rare-pattern Poisson convergence covers some defect-count mechanism, but neither total-variation approximation on growing graph alphabets nor pairwise independence alone gives this sharp entropy correction; the submission proves the needed uniform integrability and exceptional-graph bounds. Residual historical risk: older near-diameter circular geometric graph and coding literature not fully indexed.

## value

PASS

PASS: The n^-2 window is the canonical order-one missing-edge threshold of nearly complete geometric graphs. The exact graph entropy to constant order is a natural operational invariant for lossless encoding and establishes an independently useful comparison between geometrically dependent defects and Erdos-Renyi rare-edge graphs; it requires nontrivial exceptional-event entropy control beyond a routine Poisson count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
