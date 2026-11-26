# Independent mathematical audit

## correctness

PASS

The original pointwise estimate uses the union of the two localized supports, the maximum of the two normalizers, and common valid centers. Full support makes both localized supports the same open ball B_r(m), all centers valid, and both denominators positive and bounded by r. At a nonisolated x, the center-x cost to every y!=x is positive (for y inside, both kernel and distance are positive; otherwise the term D_x r is positive). The total off-diagonal flow out of or into x is at least the absolute change of its coordinate. Thus the positive minimum of those costs divided by r controls the coordinate change on every link and, by the scalar triangle inequality, on every chain. Conversely, a coupling diagonal on the active sites and arbitrary on the isolated residual mass costs zero at every center: isolated sites are outside all nonsingleton balls and singleton centers contribute zero. Two isolated sites allow a nonzero positive-simplex perturbation with the same active-site coordinates; one isolated coordinate is determined by total mass. This gives exactly r>rho_(2), with equality nonseparating. With at most one isolated site, the l1 difference is bounded by 2(n-1) times the maximum active coordinate difference (also valid when every site is active), giving the stated uniform bound. For TV defined as half l1 the equivalent coefficient is a/(n-1). Independent hand checks gave the Appendix A costs 3/4, 2/9, 1/2 and, on the three-site line {0,1,2}, total degeneracy at r=1 and constants (1,5/3,1) at r=3/2. The numerical script was inspected but not executed; its reported 275 cases are recorded evidence, not independently replayed and not a proof about arbitrary chains. No claim is made for chains through zero weights.

## originality

PASS

The original Appendix A construction and triangle-inequality counterexample are credited. The supported distinct contribution is its exact full-support zero kernel, including the strict nearest-neighbor threshold and a uniform coordinate/TV lower bound. The directly inspected original leaves separation open and its nearby positive metric theorem treats a different transport cost.

## value

PASS

Chain metricization of a useful estimate can identify points that a single link distinguishes, so nondegeneracy cannot be presumed. The result settles the full-support finite case of the motivating separation question, both identifying the invisible masses and furnishing a scale-only test and a quantitative lower bound independent of the measures and chain length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
