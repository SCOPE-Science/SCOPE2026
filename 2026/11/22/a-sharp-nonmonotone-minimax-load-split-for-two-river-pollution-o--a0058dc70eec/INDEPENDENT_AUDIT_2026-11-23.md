# Independent mathematical audit

## correctness

PASS

Solving the linear BOD and deficit equations on each reach and imposing continuity of D at the downstream outfall gives the stated delayed kernel with D/L as the normalization. With z=e^(−u), the upstream quadratic is w(z−z²), the downstream one is Az−Bz² with A=w+(1−w)/q and B=w+(1−w)/q². At z=q/(1+q) the two responses agree, giving the bound q/(1+q)² for every allocation. The derivative at this interior point vanishes only for w=1/(1+q), making the bound strict for any other split. At this split the downstream vertex attains the bound and w/4≤q/(1+q)² exactly for q≥1/3. For q<1/3 the upstream vertex is available. Equating its height with the downstream vertex factors the resulting equation as (1−w)(1−2(1−q)w)=0; w=1 is extraneous for that vertex calculation. The candidate w=1/[2(1−q)] puts the downstream vertex at q/[2(1−q)]<q. Any larger w raises the fixed upstream peak; any smaller w raises the deficit at the fixed downstream vertex because the delayed response there exceeds the first by (1−3q)/[4(1−q)]. Hence the two branch formulas and all-strict uniqueness hold including q=1/3 via the derivative certificate. Both open-reach maxima are active at and below the seam and are distinct there; above it only the downstream vertex is global. q=e^(−kd) reverses orientation, giving strict rise then fall with sole maximum 3/4 at log 3 and endpoint limits 1/2; coincident and infinitely separated outfalls are not part of the domain. Frozen verify.py was inspected, not executed; the proof does not use its finite enumeration.

## originality

PASS

The classical kernel and the directly related same-kernel local-maxima theorem are credited. The supported distinct result is an exact global fixed-budget minimax classification, including strict uniqueness, nonmonotonicity and the global active set. The local-maxima decision and classical critical-deficit convexity do not imply its two exact branches or active-set threshold. Unavailable historical portions remain explicit risks, not negative evidence.

## value

PASS

A fixed load split minimizing worst oxygen depletion is a natural global objective distinct from counting local sags. At the tractable ratio 2, the benchmark shows that the optimal upstream fraction can reverse direction as spacing grows and that a second local maximum can precede its becoming globally binding. The exact peak tradeoff and uniqueness supply a useful benchmark for more general models without implying calibrated field guidance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
