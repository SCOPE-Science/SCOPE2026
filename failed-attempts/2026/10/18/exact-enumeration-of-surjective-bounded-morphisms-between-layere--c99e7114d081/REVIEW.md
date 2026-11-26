# Independent mathematical audit

## correctness

PASS

The up-cone equality implies monotonicity and maps source maxima to target maxima. For a nonsingleton last target level, an earlier point mapped to a maximal v would force the last source level to map constantly to v, and then every earlier point, being below the last level, has image at most v. This last inference rules out attaining a different maximal value even on the same earlier level. Consequently the last source level alone covers the last target level, and lower back witnesses all stay in the lower prefix. An optional extra value encodes omitted elements of a truncated last level, giving the T weight. For a singleton top v above a nonempty target prefix, the last source level is all v and the last source level with a non-v image is some t<i. Restrict to that level's non-v points and all earlier levels; this preserves all lower back witnesses. Extension by v is inverse and every retained point sees a later v witness. A one-point target and the virtual empty-prefix cases give the stated bases. Prefix sums give the stated complexity in the specified arithmetic model. The frozen artifacts/check_pmorph.py exists; reading it confirms it compares the tables against the exact up-cone definition, but the recorded 687-case output was not counted as independent replay. A separate implementation checked 65 small vector pairs by exhaustive function enumeration and checked the two W(3,3) examples by 729 functions each, obtaining 12 and 6. This is bounded corroboration, not the universal proof.

## originality

FAIL

A distinct indexed exact transfer counts the same labeled surjective bounded morphisms including singleton levels, with the same O(hk) transition complexity once weights are available. Its transitions recover the F/G factors by grouping singleton stays before the next advance and distinguishing the optional already-covered singleton. This is demonstrable scientific equivalence, not a chronological priority or copying claim. The simpler all-monotone and homotopy counts do not themselves cover this result.

## value

FAIL

The counting problem is well motivated and the singleton phenomenon is mathematically useful, but the alternate table decomposition neither extends the exact transfer's domain nor improves its order of transition complexity. Its auxiliary table is exactly the transfer's optional-singleton step summed over retained labels. No independently useful uncovered invariant survives that equivalence in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
