# Fibonacci exceedance laws and spatial Rayleigh extremes for jittered interval samples

## Finding

For equally stratified one-dimensional sampling with one independent uniform site per stratum, the entire upper-tail count of near-maximal consecutive gaps has an exact independent-set polynomial. The near-maximal gaps, jointly with their positions, form a Poisson process on the scale of their deficit from twice the mesh spacing. In particular the maximum has a Rayleigh deficit, in contrast to the Gumbel behavior for an unstratified independent uniform sample.

For integers \(n\ge2\) and \(0\le\delta\le1/2\), define \(q=\delta^2/2\). Then

\[\mathbb E[z^{N_n(\delta)}]=\sum_{k=0}^{\lfloor n/2\rfloor}\binom{n-k}{k}q^k(z-1)^k,\qquad \Pr(nM_n\le2-\delta)=\sum_{k=0}^{\lfloor n/2\rfloor}(-q)^k\binom{n-k}{k}.\]

The variance also has the exact formula
\[\operatorname{Var}(N_n(\delta))=(n-1)q-(3n-5)q^2.\]

For the extremal scale, set \(T_{n,i}=\sqrt n\bigl(2-n(X_{i+1}-X_i)\bigr)\). Then
\[\Xi_n=\sum_{i=1}^{n-1}\delta_{(i/n,T_{n,i})}\ \Longrightarrow\ \operatorname{PPP}(ds\,t\,dt)\]

in the vague topology of locally finite point measures on \([0,1]\times[0,\infty)\). In particular,
\[\Pr\bigl(\sqrt n(2-nM_n)>t\bigr)\longrightarrow e^{-t^2/2}\quad(t\ge0).\]

The maximizing internal-gap location, divided by \(n\), converges to an independent uniform \([0,1]\) variable. For every fixed positive integer \(k\), the deficit of the \(k\)-th largest internal gap has survival limit \(e^{-t^2/2}\sum_{j=0}^{k-1}(t^2/2)^j/j!\).

## Assumptions and scope

Take independent \(U_1,\ldots,U_n\sim\operatorname{Uniform}(0,1)\), let \(X_i=(i-1+U_i)/n\), and take \(X_0=0\) and \(X_{n+1}=1\). By construction the observations are already ordered. The maximum \(M_n\) includes both external boundary gaps and all \(n-1\) internal gaps; the count \(N_n(\delta)\) counts only internal gaps. Results for the exact polynomial hold at every integer \(n\ge2\) and every real \(\delta\in[0,1/2]\). Convergence statements hold as \(n\to\infty\), with bounded nonnegative deficit marks and with any fixed order \(k\).

## Proof

**1. Triangular rare-event geometry.** The internal scaled gap is \(G_i=n(X_{i+1}-X_i)=1+U_{i+1}-U_i\). Its near-maximal event \(E_i(\delta)=\{G_i>2-\delta\}\) is the triangle \(\{0<U_i<\delta,\ 1-\delta+U_i<U_{i+1}<1\}\) of area \(q=\delta^2/2\). At \(0\le\delta\le1/2\), the events \(E_i\) and \(E_{i+1}\) are disjoint: their shared jitter variable would need to be simultaneously less than \(\delta\) and greater than \(1-\delta\). Any selection of nonadjacent event indices depends on disjoint pairs of independent jitter variables and hence its events are mutually independent.

**2. Exact exceedance polynomial.** Expand \(z^{N_n}=\prod_{i=1}^{n-1}(1+(z-1)\mathbf1_{E_i})\) by subsets of event indices. Only nonconsecutive subsets contribute. There are exactly \(\binom{n-k}{k}\) subsets of size \(k\) of \(\{1,\ldots,n-1\}\) without neighboring indices. Their intersection probability is \(q^k\); this proves the generating function. Substituting \(z=0\) gives the probability that no internal gap exceeds \((2-\delta)/n\). Since the boundary gaps are at most \(1/n\), they cannot exceed this threshold. Thus the same probability is exactly \(\Pr(nM_n\le2-\delta)\). Differentiating the generating function at \(z=1\) yields the stated mean \((n-1)q\) and variance \((n-1)q-(3n-5)q^2\).

**3. Poisson point process with spatial marks.** For every fixed bounded interval of deficit marks \((a,b]\subset[0,\infty)\), and all sufficiently large \(n\),
\[\Pr(a<T_{n,i}\le b)=\frac{b^2-a^2}{2n}.\]
Indeed \(\{T_{n,i}\le t\}=E_i(t/\sqrt n)\). Events associated with neighboring indices and bounded deficit marks are mutually exclusive once the maximal deficit cutoff divided by \(\sqrt n\) is less than \(1/2\). Events at pairwise nonneighboring indices are independent. For any fixed finite collection of disjoint spatial-mark rectangles, expand all mixed falling factorial moments of their counts as sums over distinct index tuples. Tuples containing neighboring indices vanish. Tuples with all indices at mutual distance at least two contribute products of the exact single-index probabilities. Their number differs from the unrestricted tuple count by \(O(n^{r-1})\) for a factorial moment of fixed total order \(r\). Since every individual rare-event probability is \(O(1/n)\), these excluded tuples contribute only \(O(1/n)\) to the unrestricted asymptotic factorization. The limiting factorial moments are therefore those of independent Poisson variables with mean \((b-a)\int_c^d t\,dt\) on a spatial interval \((a,b]\) and deficit interval \((c,d]\). Tightness of bounded-window counts follows from their bounded expectations, and the point-process convergence follows from the resulting Laplace functionals on bounded-support continuous test functions.

**4. Extreme gaps and location.** The limiting Poisson process has mean \(t^2/2\) on \([0,1]\times[0,t]\). Its least deficit exceeds \(t\) if and only if that region is empty; this gives survival \(e^{-t^2/2}\). The process has a.s. a unique smallest mark and its corresponding spatial coordinate is independent \(\operatorname{Uniform}(0,1)\), because intensity factors as Lebesgue space measure times \(t\,dt\). Its fixed order-statistic void/count law is \(e^{-t^2/2}\sum_{j=0}^{k-1}(t^2/2)^j/j!\). Boundary gaps are bounded above by \(1/n\), while the largest internal gap exceeds that level with probability tending to one, so the largest-gap asymptotics and its location are not changed by including the endpoints. More precisely, independent disjoint pairs give \(\Pr(\max_i G_i\le1)\le2^{-\lfloor n/2\rfloor}\).

## Verification

The accompanying `checker.py` recomputes every nonadjacent-subset coefficient exactly for \(2\le n\le15\); checks rational polynomial identities, the exact variance, and recurrence; independently integrates the sequential uniform density for selected sizes and thresholds; computes large-size Rayleigh survival via the equivalent second-order recurrence; and compares a seeded simulation against the exact finite formula. It reports 316 passed assertions. Computations are finite consistency checks; the proof of all-size identities and convergence is in the preceding steps.

## Relationship to prior work

Pausinger and Steinerberger (arXiv:1510.00251, first posted 1 October 2015) study exactly the underlying jittered-sampling construction, principally through multidimensional discrepancy and a partition principle. Their full text discusses one-dimensional star-discrepancy at order \(1/n\) but does not derive the maximum-gap exceedance polynomial or spatial extremal process. Mijatović and Vysotsky (arXiv:1508.00944, first posted 5 August 2015) analyze maximal spacings of *unstratified independent uniform points*, for which the normalized maximum has a Gumbel rather than Rayleigh limit. Watson's 1954 theory of extremes of dependent sequences offers relevant general background, but does not itself supply the exact finite triangular-event polynomial for this stratified model. The specific combination of a sharp finite probability law with spatially marked extreme gaps is the contribution assessed here.

## Limitations

Uniformity and independence of one point inside each equally sized stratum are essential for the simple triangular probability and nonadjacent independence. The exact polynomial is claimed only for deficits \(\delta\le1/2\). The marked process is an asymptotic statement on bounded deficit scales and does not describe every gap simultaneously at macroscopic deficits. The checker is a reproducibility aid, not a substitute for the proof. An equivalent statement could exist in older perturbed-lattice or scan-statistic literature not identified by the searches; independent historical priority and independent mathematical audit remain unestablished.

## References

- F. Pausinger and S. Steinerberger, *On the Discrepancy of Jittered Sampling*, arXiv:1510.00251 (first submitted 2015-10-01), https://arxiv.org/abs/1510.00251 .
- A. Mijatović and V. Vysotsky, *On the Weak Limit Law of the Maximal Uniform k-Spacing*, arXiv:1508.00944 (first submitted 2015-08-05), https://arxiv.org/abs/1508.00944 .
- G. S. Watson, *Extreme Values in Samples from m-Dependent Stationary Stochastic Processes*, Annals of Mathematical Statistics **25** (1954), 798–800, https://doi.org/10.1214/aoms/1177728670 .
