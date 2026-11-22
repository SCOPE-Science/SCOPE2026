# Independent mathematical audit

## correctness

PASS

For a positive length vector h with only h_0=r !=1, direct hat integration gives 6G diagonal 2(h_{j-1}+h_j), offdiagonal h_j. On even cycles, alternating-sign conjugation yields Stieltjes B whose normalized off-diagonal row sums are precisely 1/2; the convergent Neumann series has exponential distance decay uniformly in N for each fixed r. Kernel values alternate and the integral on a cell is 3h(u²+v²)/(u+v). Convexity localizes norm maximization to knot evaluations. Full-line Green recurrence at k=0 yields a=(2r+sqrt3)/((r+sqrt3)(3r+sqrt3)), b=r/((r+sqrt3)(3r+sqrt3)); at k=2 yields t=r/(2r+sqrt3), H=2(r+1)-rt, v=1/((2+sqrt3)H-1). Independent SymPy simplification reproduces E_-, E_+ and limit (10-2sqrt3)/3, while positive factors give strictness for r<1 and r>1. Coercive Neumann bounds plus rank-two resolvent show local Green rows converge and distant rows tend to uniform value 2, establishing existence of Lambda(r). Independent direct cyclic matrix inversions for N=12,30,90,150 and r=0.15,0.5,0.95,1,1.2,2,8 matched both limiting witnesses at N=150 to about 1e-9; finite checks only corroborate, not prove infinite quantifiers. r fixed positive, N even >=6, L∞ real spline norm, and E values are lower witnesses, not exact overall norm.

## originality

FAIL

Full original theorem is correct but not an original mathematical contribution: an earlier publicly recorded full-line single-defect spline theorem gives EXACTLY the same two local witness functions, both strict sign ranges and the uniform-mesh threshold. Both expressions were independently reduced symbolically and matched identically. The new periodic N-even formulation converges to the corresponding bi-infinite localized Green problem by the familiar row-1/2 Neumann decay and rank-two resolvent comparison; adding this routine finite-circle exhaustion does not leave an unknown strict-threshold law. Earlier uniform-periodic and two-periodic spline results fix the reference and contrast. The 2004 general formula is credited and is not alone the decisive covering work.

## value

FAIL

Isolated exceptional interval amplification is a motivated structural phenomenon, but the complete claimed sign threshold and both parameter-dependent witnesses already appear in the earlier same-object full-line theorem. The present restriction to finite even periodic approximants followed by N->infinity is an expected local finite-size approximation with no new sharp constant, cutoff, classification or independent mathematical content. The methodological contrast with alternating two-periodic meshes is already explicit in earlier work. A known result plus routine periodization is not an independently unknown exact invariant; therefore independent mathematical value fails despite valid and reproducible computations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
