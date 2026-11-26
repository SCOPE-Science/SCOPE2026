# Independent mathematical audit

## correctness

PASS

For independent arclength sampling there are 6, 24, and 6 ordered coincident, adjacent, and disjoint edge pairs. For a direct coordinate check use the four sign vectors (1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1) scaled by 1/(2 sqrt(2)). Edges meeting at a vertex have inner product 1/2 between unit directions. Opposite unit directions are perpendicular and their midpoint displacement is normal to both, with squared length 1/2. This gives the three unit-square quadratic forms in the finding. Coincident edges give 2r-r^2. The adjacent change of coordinates (u-v/2,sqrt(3)v/2) gives a 120-degree sector and area factor 2/sqrt(3); its two clipping lines have distance sqrt(3)/2 from the origin. For r<=1 each exterior cap is in the wedge, since u>=1 and v<0 imply u^2+v^2-uv>=1, and the two exterior regions do not overlap within the disk because u,v>=1 give (u-v)^2+uv>=1. The opposite form is the disk of squared radius r^2-1/2 in a centered square of side 1, clipped by four nonoverlapping side caps when the radius exceeds 1/2. A disk cap at distance d has area D(R,d)=R^2 arccos(d/R)-d sqrt(R^2-d^2). Substituting yields each displayed branch, continuous at the thresholds and with total CDF one at r=1. At h only the opposite branch supplies the derivative jump (1/6)*2*pi*h. Writing delta=R^2-d^2, the cap is also the integral from 0 to delta of sqrt(delta-s)/sqrt(d^2+s) ds, giving (2/(3d))*delta^(3/2)+O(delta^(5/2)). This gives per-cap coefficients 8/9 after the adjacent Jacobian and 4/3 for the opposite cap, hence -56/27 in the mixture. Near r=1, the leading inward linear deficits at the three adjacent maximizing corners have coefficients (2,1),(1,2),(1,1); at all four opposite corners they are (1,1). The deficit cutoff is 2 epsilon+O(epsilon^2), giving conditional tail coefficients 4 and 8, in addition to the exact coincident coefficient 1. Weighting gives 25/6. Independently, the sampled point has mean zero in the sign-vector coordinates and expected squared norm 3/8-E[U(1-U)]=5/24; independence gives E[R^2]=5/12.

## originality

PASS

Pass for the complete ambient arclength-pair law on this canonical wireframe and its combined transition/endpoint structure, not for the same-segment component or the elementary circular segment formulas. The strongest related Resultary comparisons either change the measure to surface area or volume, or choose one line through a fixed point rather than two independently sampled points. The most relevant general-distance search returned planar polygon-region laws and a coincident-line formula, not a statement for two skew or vertex-adjacent fixed unit segments covering all clips. No earlier whole-mixture formula or demonstrated specialization was found in the available statements; this is not a claim of absolute priority.

## value

PASS

The regular tetrahedral wireframe is a natural symmetric embedded metric graph, the first regular simplex skeleton with disjoint skew edges. Its full two-point law separates the contributions from touching and disjoint edges and quantifies two qualitatively different interior events: a density jump at the shortest opposite-edge separation and a shared higher-order clipping onset. The exact cusp and diameter-tail coefficients and nontrivial mean square make it an independently useful benchmark for arclength sampling on geometric networks, not just an elementary same-segment calculation or a numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
