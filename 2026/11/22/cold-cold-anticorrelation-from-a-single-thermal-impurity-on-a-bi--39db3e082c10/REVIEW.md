# Independent mathematical audit

## correctness

PASS

The per-edge rate is one and each site's independent refresh rate is g. All-site refresh with no edge rings over a fixed interval gives a uniform regeneration component: the skeleton is a total-variation contraction with a unique invariant law, which is invariant for the full semigroup by commutation. With W the total energy, exchange conserves W and the refresh generator satisfies L(W²)≤−gW²+2gW∑T_i+2g∑T_i², using ∑X_i²≤W². This gives bounded second moments from a finite-energy initialization and in the invariant law by convergence and truncation. The first moments solve the stated graph-Laplacian equation. An independent centered reconstruction uses C_ij=E[X_iX_j]/(1+δ_ij)−m_im_j: at an edge incident to both coordinates of a moment, the homogeneous update is the average of the three normalized moment coordinates (the two diagonal ones and their cross moment). Subtracting first-moment products gives source +(m_i−m_j)²/3 on either diagonal and −(m_i−m_j)²/6 on the edge cross moment. A refresh at i gives the diagonal source g(T_i−m_i)², and no cross-moment source; updates involving just one coordinate of a distinct pair give a homogeneous averaging term. Thus the sources scale by Δ² and are independent of T. The orbit equations obtained this way agree with the displayed determinant and rational covariance formulas. In addition to exact full-vertex solves at (n,g)=(3,5) and (4,2), checked on independently written code (reconstruct_record4.py and direct_check.txt under /workspace/branches/9ab69628-1e33-4b09-95d3-9e6b14f234eb/), I checked the centered eight-orbit determinant and the three formula identities by exact modular elimination at every n=3,…,20 and g=1,…,18. Multiplying the system by 6 and the centered unknowns by [2(g+n)(2g+n)]² gives integer coefficient entries of degree at most 1 and source entries of degree at most 5. Cramer's numerator determinants have degree at most 12; all cross-multiplied identities therefore have degree at most 17. On this grid coefficient magnitudes are below 500 and source magnitudes below 3·10^9, so the integer identity residuals, by the determinant expansion and formula factors, have magnitude below 10^45. All residues vanished for eleven distinct primes above 100000, with no singular modular system. This suffices for integer equality on the grid and hence polynomial equality by interpolation; the finite full-vertex solves by themselves are only checks. The supplied symbolic and numeric scripts were inspected but not executed. Descartes' rule, the endpoint signs and the positive denominators prove the sign transition; strict positivity of the cross-pair numerator and the same-shore identity settle the other classes. Scaling the unique root is justified by sign brackets around (1+√3)/2 in the limiting factored quartic.

## originality

PASS

The specific cold–cold sign reversal on the far shore, the all-rate separation of the three cold-pair classes, and the threshold scaling are supported as distinct to the best of current knowledge. Uniform energy splitting, second-moment closure, and the mixture framework are established techniques. The nearest same-day result shares the refresh generator on a different graph and has a different sign-changing class; its result does not imply the biclique classification.

## value

PASS

The covariance sign change concerns two identically cold vertices with no direct bond to one another, not simply an imbalance involving the hot vertex. A single impurity in a canonical two-shore mixing network separates two nonadjacent cold-pair classes. Exact all-rate signs and a threshold on the natural scale set by the degree n distinguish this from a single numerical example or a known one-dimensional estimate. The result answers a concrete finite-network question and imposes no unsupported claims about currents, higher cumulants or other geometries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
