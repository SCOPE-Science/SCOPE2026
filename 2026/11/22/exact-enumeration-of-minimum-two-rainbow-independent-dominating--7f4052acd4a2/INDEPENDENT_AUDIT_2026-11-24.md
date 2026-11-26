# Independent mathematical audit

## correctness

PASS

Checked the local constraints and reconstructed the all-n equality structure. A middle column 00 forces its two neighbours to be complementary double columns (12 and 21), since the two horizontal labels in each row must be 1 and 2. Its reduced cost is zero. A singleton middle column has reduced cost zero. A double middle column contributes one unless it follows an empty one, when it contributes zero. Thus reduced costs are nonnegative and telescope, and weight n occurs exactly when all double columns follow an empty one. An empty column then forces its predecessor double and the column before that empty, so iterating around the cycle forces alternating empty and double columns. The doubles must alternate 12/21, yielding four indexed functions if 4 divides n and none otherwise. With no empty column there are only singletons. Encode their four types by (row, colour) in F_2^2. Adjacent types must be distinct, and each type must have its simultaneous row-and-colour flip on at least one side. Equivalently consecutive nonzero increments d_j around the cycle have no adjacent pair avoiding c=(1,1), and their sum is zero. Character filtering for that parity condition cancels the four choices of starting type against the factor 1/4. For a character with values u,v on (1,0),(0,1) and w=uv on c, the weighted increment matrix with rows (0,0,w),(0,0,w),(u,v,w) has characteristic polynomial t(t^2-wt-w(u+v)). The four choices of character yield trace sum 2^n+3(-1)^n+u_n, giving the stated correction after adding the alternating family. Counts are positive at 4 and 5 and bounded below by 2^n-3-2(√2)^n>0 for n>=6, so weight n is indeed attained. This proof counts indexed columns and named colours. Independently, review-evidence/prisms.py rebuilt the 35 states, histogram 46 tight and 24 slack arcs, characteristic polynomial, two nontrivial components, and all displayed sample traces. Uploaded supporting files and test claims were inspected; no uploaded programs were executed. The proof and scope here are n>=4.

## originality

PASS

The distinction is the exact labelled multiplicity and its decomposition. The underlying weight n and a minimum-weight transfer treatment of the very same graph are established prior work, as the Finding's relationship section expressly acknowledges. No inspected statement was found that gives or directly entails the number of optima.

## value

PASS

The cyclic prism is a natural narrow product family for which the energy/weight minimum alone leaves the multiplicity unresolved. The exact count shows exponentially many optima, resolves the subleading colour–row constraint and the separate periodic family, and supplies a reusable labelled benchmark for optimum multiplicities (equivalently smallest maximal independent sets on the width-four torus). The value is the full optimum structure and tie count, not recovery of the known weight.

The dated certificate retains the supplied scientific assessment, sources and limitations.
