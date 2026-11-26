# Independent mathematical audit

## correctness

PASS

In RESULT.md lines 37–60, the centroidal core is exactly {λ_i≥t} in barycentric coordinates. On two different sides the side parameters are independent uniforms. For u≥v and t>0, feasibility requires u>t and λ∈[t/v,1−t/u]; the remaining coordinate is maximized at the upper endpoint. This gives lower v=tu/(u−t), upper v=min(u,(1−2t)u/(u−t)), and the switch at u=1−t, with u≥2t. Integrating twice the resulting widths yields all three logarithms with the stated coefficients. At r=0 the region has area zero; as r→1 the conditional probability tends to one, but same-side chords never hit for r<1 and all hit at r=1. Continuity of the distinct-side law excludes further atoms. The shape bounds follow from 1/3≤Σp_i²<1/2, attained on the first side exactly at equal lengths and approached on the second at (1/2,1/2,0). At r→0 the first integral is O(r²) and the derivative of the second is 2∫_(2/3)^1 u/(u−1/3)du=2(1+log 2)/3; the displayed expression also gives 1−2t+O(t²|log t|) at the other end. The checker and VERIFICATION.md were inspected; recorded Monte Carlo runs corroborate finite instances only and were not rerun or used as proof.

## originality

FAIL

An earlier distinct indexed result states exactly the same all-scale CDF under the same law of endpoints and gives the same endpoint atom. Expanding its log ratios recovers the present expression term by term. The added arbitrary side weights follow directly by reweighting the already common ordered distinct-side conditional law; the sharp bounds and expansions follow from the earlier closed form and shape factor.

## value

FAIL

The core-hit law is meaningful as geometry, but as a contribution this record rederives the existing exact law and shape dependence. Endpoint Taylor expansions and mixing already known per-pair laws with new side-selection probabilities give no substantive additional invariant or classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
