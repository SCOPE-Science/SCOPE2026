# Independent mathematical audit

## correctness

PASS

For V(f)=1, the positive and negative Jordan parts of Df have mass 1/2. Their product coupling represents the error as an average of residuals of half-height signed arc indicators. The Hilbert variance identity forces the residuals in an extremizing average to be identical almost surely, and the positive nonzero-frequency residual multiplier makes the operator injective modulo constants. This gives the full single-arc equality classification. Parseval with both signs of k and the normalized half-height at each jump gives the 1/(4π²) positive-frequency factor and the finite Bernoulli-sum formula; at N=1 it gives 1/16 for the squared norm. The scaling q=2πNd gives locally uniform Riemann sums (a bounded panel plus a uniformly integrable t^-2 tail). The sign of q cos q−sin q changes exactly once on (0,2π), and Phi'(0+)>0 while Phi'(2π)<0 by the alternating half-wave integral. Two integrations by parts give the stated O(q^-2) tail envelope. Verified the strict comparison independently: with l=3.14159, u=3.14160 (Machin alternating bounds), upper-bound Si(π) by its terms j=0 through 6, using u for positive terms and l for negative ones. It is <1.8521, yielding 4π²(Phi(π)−Phi_infty)>1+l²/2−u(1.8521)>0.11>l^-2. This excludes every q≥2π. For any finite optimizer, q_N→∞ along a subsequence would kill the weighted cosine sum by Abel summation (bound 1/[N sin(πd_N)]), producing the strictly smaller Phi_infty. A subsequence q_N→0 is excluded by compact Riemann-sum convergence. Thus all optimizing separations converge to the unique peak after rescaling. Independent bisection and sine-series evaluation gave q≈3.34431785947053, Phi(q)≈0.0537105342266452 and q/(2π)≈0.532264718605241.

## originality

PASS

The distinct supported claim is the sharp ordinary Fejér squared L² error over real periodic BV with this variation and indexing, including its optimal arcs and the actual unique limiting separation. The elementary two-atom reduction and the use of Parseval are not by themselves claimed original. This decision is bounded by incomplete access to older direct Fejér literature.

## value

PASS

This determines a sharp approximation invariant for a classical filter. It shows why the optimal uniform BV estimate cannot be obtained by holding jump positions fixed: its two optimal jumps approach at an explicitly selected scale, with a strictly larger coefficient. This is substantive beyond the N^-1/2 rate and the usual single-jump profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
