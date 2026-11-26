# Independent mathematical audit

## correctness

PASS

The inverse-face condition makes every double fibre a centre–leaf edge, so there is at most one. If it maps to the centre, rank must be one (otherwise a target edge pulls back to at least three points); if it maps to a leaf, the other inputs and outputs form a partial bijection on the two remaining (m−1)-leaf sets. An injective map must map image edges to domain edges under its inverse: a leaf-only image imposes no restriction, while with centre in the image the possibilities are centre fixed, a singleton, or a rank-two edge swap. These cases reproduce the total and rank-specific counts. An fgf=f witness on the image is a section; restriction preserves continuity since a subset of a face is still a face. A noninjective map with leaf image admits a leaf-only section (use the leaf of the doubled fibre), and a singleton image always does. For injective maps the inverse is the only section and fails continuity exactly when a domain centre–leaf edge goes to two leaves. Such maps have rank at least two; counting their domain and image gives binom(m,k−1)binom(m,k)k!. Idempotence is equivalent to fixing every image point, recovering the partial identities and the two possible collapses with fixed image. For uniform partial bijections the deficiency weights have ratio (m−j)/(j+1)^2. Comparing at the ends of an inner band of width proportional to sqrt(m) gives outside-tail bounds O(m exp(−c sqrt(m))) for every fixed fractional-width outer band, hence mean deficiency asymptotic to sqrt(m). Multiplying each rank term by its deficiency proves mJ_m=I_m E[D_m], where J_m counts partial injections from m into m−1 points. Substituting in the exact counts gives both inverse-square-root laws and the joint regular-singular law. Independent direct inverse-face and semigroup-equation enumeration for m=2,3,4 agreed with all formulas, including individual regularity and rank counts. Replay: python3 /workspace/reproductions/star_monoids.py. The uploaded script was inspected, not run.

## originality

FAIL

Distinct indexed records already give the exact star regularity criterion and nonregular/idempotent census, and a finer bivariate domain–rank distribution. The asymptotic contrast is not rescued by its different wording: the same enumerators reduce the three rates to a normalized, previously documented partial-bijection deficiency mean by a one-line coefficient identity. Thus no distinct mathematical remainder is established for the stated census and first-order laws. This is a statement-level coverage decision, not a finding about derivation or historical priority.

## value

FAIL

The typical-versus-global regularity contrast is mathematically pertinent, not an arbitrary numerical example. But as an additional finding, the exact invariant is already present in finer counts, and the proposed extra first-order rates follow directly from them and the standard deficiency statistic. No new structural obstruction, asymptotic regime, or independently useful unknown invariant remains after crediting that coverage; the concise reformulation is useful exposition, not a separate valuable result under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
