# Independent mathematical audit

## correctness

PASS

A quotient fixed point has all coordinate updates equal modulo 2π. Each update has magnitude at most 2h, and the updates sum to zero, so all vanish. Current is therefore constant. The Hessian acts on edge differences with sum zero, and its norm is at most 4. Thus strict attraction is exactly positive definiteness there. Two negative cosines give a negative two-edge test; one negative ordinary cosine and one positive ordinary cosine give an exact zero of the form by equality of magnitudes. An ordinary zero cosine forces all cosines to vanish. Hence any attracting winding-one state has m equal acute ordinary increments. Current balance and winding give the asserted f_m. Its logarithmic derivative has a single zero: with t=π−β, the derivative of tan t−m tan((π+t)/m) changes sign once, from negative to positive at π/(m−1), and the function goes from negative to positive infinity. The constrained form then has m−1 positive directions and remaining sign cos α+mw cos β, opposite to f_m'. The fold null vector has strong-edge differences 1 and weak-edge difference −m; the w derivative of the potential gradient paired with it is −m sin β, and the directional cubic is (m³−m)sin α. Both are nonzero, establishing map saddle-node nondegeneracy together with the simple neutral multiplier. Reflection handles negative winding. The implicit equation gives an O(m⁻²) shift of t from t_*; stationarity of (π+t)/sin t at t_* makes that shift contribute only at O(m⁻⁵) to w, leaving precisely the stated cubic coefficient.

## originality

FAIL

A distinct same-date Resultary record, 806535c3bca9, already gives the central sharp finite-size onset, using the same f_m, its same unique nondegenerate minimizer, Hessian inertia criterion, stable branch and saddle, and the same leading large-cycle constant. This is statement-level coverage irrespective of relative priority. The step bound transfers the stability signs directly to the discrete map. The comparator does not explicitly state the full interval through w=1 or the cubic coefficient; these refinements are not evidence that the advertised onset itself is distinct.

## value

FAIL

The sharp onset for circulating states is a worthwhile object, but the reviewed contribution cannot claim that onset beyond the exact existing result. The additional multiplier translation, monotone continuation of the same scalar equation on the all-acute interval, and one Taylor coefficient of the known minimum are routine refinements here. No separate scientific need for the cubic coefficient or substantive new phenomenon is supplied that would make a surviving narrower claim valuable enough for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
