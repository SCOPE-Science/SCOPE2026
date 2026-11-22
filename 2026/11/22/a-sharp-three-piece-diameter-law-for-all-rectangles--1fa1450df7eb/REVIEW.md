# Review: three-piece diameter of a rectangle

## Correctness
**PASS.** The claimed value is attained by a T-shaped three-rectangle cut for \(1\le\lambda\le3/2\) and equal full-height strips above the threshold. For the lower bound, pigeonhole on four corners forces a convex cell to contain an entire side. A two-case boundary-interval argument shows that, whenever the maximum diameter is below the candidate, the other parts contradict one of two sharp diameter inequalities. The horizontal-side possibility is ruled out independently, including the narrow aspect-ratio interval up to \(\sqrt{(5+2\sqrt{13})/12}\). Exact identities and cutoff calculations are checked in `verify.py`. The continuous proof is the geometric lemma, not finite experimentation.

## Originality
**PASS at available-source priority resolution.** The \(\lambda=1\) square result is credited to Wenceslas and Lipman (1958), as documented by Chaidee and Wichiramala (2016); it is not presented as new. Cañete, Fernández and Márquez (2023, Section 3.1) show general min–max diameter bounds and existence but do not determine the three-piece rectangular profile. Fekete et al. (2023) and Heppes–Melissen (1997) study three congruent disks covering a rectangle. Sharp disk-covering radii cannot on their own give this lower bound for arbitrary convex pieces, because their circumradius can exceed half their diameter. Comparisons with related published assertions did not disclose a theorem covering this claim. The full 1997 primary paper was not read, so an earlier duplicate statement remains a priority risk; an unavailable related paper is not asserted to be noncovering by full-text inspection.

## Mathematical value
**PASS.** The theorem gives the complete aspect-ratio dependence for a natural minimum-maximum-diameter functional, and exactly identifies a global change of optimal construction at \(\lambda=3/2\) for all convex three-piece partitions. Its bound is not a renaming of the square endpoint or a mere optimization over rectangular tilings: the lower bound rules out oblique, polygonal, and curved convex parts alike. It does not classify all equality partitions or more general covering models.

## Verification and limits
Twelve exact SymPy identities plus additional strict-region checks and construction identities have passed. They supplement, and do not replace, the complete analytic lower-bound proof. Earlier disk-cover literature is not interchangeable with convex-diameter partitions; unindexed duplicate priority remains possible.

Self-review: passed. Independent audit: not yet performed.
