# Independent mathematical audit

## correctness

PASS

Itô isometry and independent Gaussian errors give the frozen quadratic risk; Gaussian conditional expectation makes the joint minimization over linear weights exact. The optimized precision penalty is at least (total jump variation)^2/P by Cauchy–Schwarz, with equality by allocating in proportion to absolute weights. Merging coincident jumps and ignoring the measure-zero endpoint at reversed time x=1 can only lower that variation. Clipping into [0,1] and sorting step levels in increasing order reduce risk, strictly for a genuine inversion, and do not increase the jump budget counting an initial positive jump. For distinct sorted levels from 0 up to a top level q, the best boundaries are their pairwise midpoints. If the positive increments are δ_j, direct integration across those midpoints gives squared error Σδ_j³/12 + (1-q)³/3. For fixed q>0 and k increments, strict Jensen uniquely minimizes the first term at δ_j=q/k, and using n increments strictly improves over k<n. Equivalently the global reduced objective is q³/(12n²)+(1-q)³/3+q²/P on [0,1]; the endpoint derivatives have opposite strict signs and the objective is strictly convex there. Its critical equation is (1-q)²-q²/(4n²)=2q/P. This gives q=nd_{n,P}, the interior distinct sites, weights d_{n,P}, and equality in the noise inequality only at equal precisions. All n distinct jumps are essential, ruling out repetitions, inactive sensors and endpoint observations. At fixed P the cubic term strictly decreases with n at the previous optimum q>0. The displayed limits follow from the scalar root and uniform-grid Riemann sums; the limit equation gives the alternate form of the limiting risk. In particular the no-sensor step q=0 is excluded even though the frozen refinement argument describes a first positive jump only for k>0.

## originality

PASS

The exact finite-n array, risk and equal weights on the homoscedastic slice are materially covered by Resultary ad44ca256f44. The supported distinct claim is that no other precision allocation under the same budget can tie or improve the design. The fixed-budget terminal-window limit follows from the equal-noise formula on that slice, so it is not counted as an independently original formula; the new global allocation result makes that limit optimal over the full allowed design class.

## value

PASS

When accuracy is a freely allocable cost, knowing the best sites for equally noisy sensors does not justify buying equal precision. The result resolves that resource decision globally, with strict exclusion of replicated, inactive, unequal-precision and endpoint competitors. The exact loss and terminal exclusion region are interpretable consequences for a concrete Gaussian model even as sensor count increases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
