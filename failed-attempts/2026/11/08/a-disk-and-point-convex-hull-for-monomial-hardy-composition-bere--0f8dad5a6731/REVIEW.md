# Independent mathematical audit

## correctness

PASS

For H² composition f→f(z^m), m≥2, normalized Szegő kernels give B(z)=(1-r²)/(1-r^{m+1}e^{i(m-1)theta}). All phases occur and give center c=(1-r²)/(1-r^{2m+2}) and radius rho=c r^{m+1}. Setting left edge alpha=c-rho, a containing interpolation disk of radius (1-alpha)/(m+1) exists exactly when sum_{j=0}^{m-1}r^{2j}≥m r^{m-1}, strict AM–GM for 0<r<1. Thus all nonzero-r fibers are inside the proposed hull, while r→1 approaches every boundary point of the limiting disk and r=0 gives 1. Tangent geometry gives h(theta)=max(cos theta,(1+cos theta)/(m+1)), t±=1/m±i sqrt(m²-1)/[m(m+1)], area [pi-arccos(1/m)+sqrt(m²-1)]/(m+1)², perimeter the two tangent lengths plus major arc. Strict disk containment gives boundary intersection exactly {1}. The checks.py rational/geometry diagnostics were inspected; infinite proof is AM–GM and geometry.

## originality

FAIL

FAIL: previously published Resultary P2 proves the *same* exact all-integer monomial Berezin closed convex hull, support function, both area/perimeter formulas, support attainment and boundary. Earlier P3 goes further, proving this envelope for every analytic disk selfmap with a zero of order at least m, with monomials simultaneously sharp and exactly the same tangent points/geometry. Both full primary RESULT.md texts were read; P3 strictly dominates the assigned result, not just a matching title.

## value

PASS

The closed convex hull and sharp support for the natural composition isometry C_{z^m}, with its planar geometry and boundary attainment, constitute a natural computable operator invariant; as an original contribution it is already known, so despite intrinsic value this package must be rejected on O.

The dated certificate retains the supplied scientific assessment, sources and limitations.
