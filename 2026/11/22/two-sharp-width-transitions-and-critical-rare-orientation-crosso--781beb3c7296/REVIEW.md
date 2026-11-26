# Independent mathematical audit

## correctness

PASS

Direct support over the five vertices gives a+max(a,h|u_z|), a=|u_x|+|u_y|. Spherical area disintegrates into independent uniform |u_z| and folded azimuth, and imposing both support inequalities gives (2) with the stated angular CDF. The arbitrary convention at t=1 does not affect the integral. Minimization at c=1 for t<1 reduces to the crossing of a decreasing base branch with a concave apex branch or the pole, giving exactly the two candidate values in (3). Strict concavity of the apex branch rules out intervening equal minima. At each pole the width excess is |x|+|y|+O(x²+y²); its tangent diamond has area 2ε². At an oblique minimum use t=t_0+εδ and azimuth displacement εv>=0. The limiting sublevel obeys δ>=h*s_0*v-h/2 and δ<=(1-s_0*v)/(h-1/h); its height at v=0 is h(h²+1)/(2(h²-1)), and its v-intercept is (1+h²)^{3/2}/(2h³). The folded density times the two angular endpoints gives 4/π times the triangular area. These linear excesses control distance from their centers uniformly for h near sqrt(3), since both oblique slopes are nonzero with opposite signs and s_0 stays positive. Compactness excludes all directions outside separated neighborhoods. The lower coefficients add at equality and their ratio is 3:8. For the upper endpoint, width is the support of all directed vertex differences. Near the largest norm only the four length-2sqrt(2) base diagonals or eight length-sqrt(h²+2) apex differences can contribute; the shorter base edges are strictly below threshold. Each qualifying difference gives an exact spherical cap of probability ε/(2M) at its own maximum M. The caps stay disjoint near the transition because the attaining unit directions are separated. This gives (5), the upper split 1:2 and the exact critical coefficient. The competing value gaps have slopes 3/4 and sqrt(3)/2 at the respective switches. In the moving regimes each family uses the positive part of the tolerance after subtracting its gap; the same uniform tangent expansion or exact cap formula applies, and a gap equal to ε at first order gives a vanishing normalized contribution. Thus (6) and (7) hold for every fixed real λ, including clipping boundaries. Read RESULT.md lines 53–81, VERIFICATION.md and verify.py. The documented finite checker is supplemental and was not executed; the localizations and limits were checked analytically.

## originality

PASS

The earlier general pyramid width theorem covers the minimum value, including the switch in its square-base specialization, and that coverage is credited. Exact width results on the cube and circular frustum and a close brightness law on the same square pyramid do not give its line-width CDF or the paired endpoint laws, contact splits and moving-height probability profiles. The pass applies to that distinct probabilistic content.

## value

PASS

The square pyramid is a natural anisotropic five-vertex test body, and widths near its endpoints distinguish geometric contact types rather than merely recovering extremal values. The result gives an exact CDF, characterizes how the optimal contacts exchange dominance, and resolves the competition on the tolerance scale with explicit masses and clipping thresholds. The quadratic lower law and exactly linear upper law are useful together for quantifying rare projection directions; the already-known minimum endpoint alone would not have this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
