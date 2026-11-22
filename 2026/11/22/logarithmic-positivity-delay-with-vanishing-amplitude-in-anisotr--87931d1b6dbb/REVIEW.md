# Self-review

## Correctness — PASS

The weighted four-cycle is the Cartesian product of two weighted edges. The four Boolean characters give exactly the eigenvalues \(0\), \(2a\), \(2b\), and \(2(a+b)\); inverse Fourier transformation yields the four kernel-entry formulas. The two original edge-transition types are strictly positive. Subadditivity of the scalar power for \(\alpha\le1\) establishes positive opposite-corner transfer. For \(\alpha>1\), the derivative of the remaining exponential polynomial, multiplied by \(e^{Ct}\), is strictly increasing from a negative value to infinity, proving a unique negative trough and one recovery crossing. The row-sum norm formula follows from the row-stochastic identity, even when one coefficient is negative. The elementary decreasing integral \(\varphi(u)=\int_0^1e^{-su}ds\) proves the strict recovery-time bracket. Taylor expansion and uniform weak-edge bounds prove both asymptotic regimes, including the coupled limit. The standalone numerical checker passed 348 supplementary cases; no infinite conclusion depends on those finite tests.

## Originality — PASS, with historical uncertainty

Benzi–Bertaccini–Durastante–Simunec (arXiv:1912.07288, 2019) and Benzi–Simunec (arXiv:2012.08389, 2020) develop general fractional graph dynamics and numerical approximation; their inspected positivity results concern the classical subunit-order regime and do not contain the exact \(\alpha>1\) alternating-weight square recovery threshold. The closest published published-finding corpus record on noncomplete complete multipartite graphs covers the equal-weight \(a=b\) four-cycle as an unweighted special case; that special case is not claimed original. Its stated unweighted theorem does not imply the unequal-weight recovery formula, logarithmic duration/vanishing amplitude separation, or coupled order/anisotropy crossover. A published study of two-timescale amplification/recovery for fourth-order heat on unbalanced unweighted complete bipartite graphs has a similar qualitative separation but different graph parameters and asymptotic rates. An earlier independent derivation in the theory of weighted Boolean cubes or exponential polynomials remains possible; the relevant published-finding corpus full text could not be inspected through the available access, and the negative search is not a proof of historical priority.

## Mathematical value — PASS

The endpoint pair of an anisotropic four-cycle is the smallest nontrivial Boolean product for which an order-greater-than-one spectral heat filter can temporarily generate a negative non-neighbor transfer. A collapsing edge rate creates a singular boundary: the violation lasts arbitrarily long, although the maximum violation becomes arbitrarily small. The exact global positivity frontier, the strict dimensionless bracket, the unique norm-amplification peak, and the joint-order crossover give a precise stability diagnostic near graph disconnection. This is a structural finite-network boundary phenomenon, not merely recalculation of the unweighted graph's known threshold.

## Closest literature and limitations

- Benzi et al., *Nonlocal network dynamics via fractional graph Laplacians*, arXiv:1912.07288, first available 2019-12-16. General subunit-order fractional positivity and decay, not an exact weighted superunit-order crossing law.
- Benzi and Simunec, *Rational Krylov methods for fractional diffusion problems on graphs*, arXiv:2012.08389, first available 2020-12-15. Computational treatment of fractional graph diffusion and M-matrix positivity, not the present classification.
- Published published-finding corpus record, *A sharp positivity transition for fractional graph heat on complete multipartite networks*, 2026-10-26. Its unweighted special case is subsumed, not novel here; the metadata available did not state the anisotropic result.
- Published published-finding corpus record, *Two timescales of transient amplification and positivity recovery on unbalanced bipartite graphs*, 2026-10-26. Size-imbalance asymptotics in a different graph family do not imply the fixed-four-vertex conductance-collapse law.

The finding concerns only the alternating two-weight four-cycle and the ordinary matrix exponential of a spectral graph-Laplacian power. An arbitrary four-cycle, time-fractional diffusion, or infinite lattice is outside scope. The published record's complete file was not available for material comparison, and priority must remain qualified.

Self-review: passed. Independent audit: not yet performed.
