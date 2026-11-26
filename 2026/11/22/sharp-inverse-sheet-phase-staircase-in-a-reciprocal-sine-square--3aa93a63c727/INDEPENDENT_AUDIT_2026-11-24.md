# Independent mathematical audit

## correctness

PASS

For fixed positive a,b and an interior target, each positive second phase ζ≤a+bπ uniquely determines the segment y=(ζ-ax)/(bπ), on x in (0,1] intersected with [(ζ-bπ)/a,ζ/a]. On it the first phase divided by π is a/x+ζ/π²−ax/π², strictly decreasing. Each of the two distinct first-phase progressions crosses it at most once per integer, equivalently at the unique positive quadratic root. The inverse labels are injective because the actual phases fix both labels. Exactly the phases 0<ζ≤bπ have segments reaching x=0, including equality where y=1−ax/(bπ). Their two disjoint second-phase progressions give the stated floors. Counting integers on each truncated phase interval gives a/ε+O(1) per first-phase progression on an edge-reaching segment and a bounded count elsewhere. The smallest phase is arcsin(sqrt(v)), giving the if-and-only-if threshold, including equality when b<1/2. The phase Jacobian determinant is −ab(1+π²/x²), and the two sine derivatives are nonzero at interior targets. For K>0, each edge-reaching segment has weight 1/K+O(ε); its transverse distance to ζ/(bπ) is ax/(bπ), with x=a/m+O(m⁻²). Summing the distances gives a harmonic logarithm, while exceptional segments and weight rebalancing cost O(ε). This proves the stated W1 upper bound without uniformity near target endpoints or staircase jumps. VERIFICATION.md and checks/verify_inverse.py were inspected; the finite floating-point diagnostics were not run and are not needed for exhaustion or threshold equality.

## originality

PASS

The map, ordinary critical-set framework and similar counting mechanisms are prior. The distinct claim supported here is the fixed-interior-target finite-phase staircase, its exact leading valence, the sharp parameter threshold, and the quantitative transverse empirical law on the given one-step domain. No checked comparator covers this combination or implies it by specialization.

## value

PASS

Inverse multiplicity is a natural invariant of this already studied noninvertible map. Even in a bounded source, regular preimages can be infinite; the exact threshold and phase-dependent leading count distinguish target heights for which this occurs, and the atomic law identifies where the multiplicity resides. The usefulness is for one-step inverse geometry, not forward chaos or security.

The dated certificate retains the supplied scientific assessment, sources and limitations.
