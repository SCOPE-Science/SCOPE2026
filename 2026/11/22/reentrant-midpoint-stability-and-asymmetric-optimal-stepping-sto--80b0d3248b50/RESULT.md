# Reentrant midpoint stability and asymmetric optimal stepping-stone placement for two dispersal scales

## Finding

A one-dimensional, one-intermediate-habitat connectivity model with **two** independent movement scales can make equal gap spacing a strict *local* optimum for a weighted geometric mean of two species' successful two-hop passage probabilities, even when the *unique global optima up to reflection* are strongly asymmetric. With one species and one scale, this locally stable-but-globally-inferior midpoint is impossible.

More precisely, for two species with distance scales \(\ell_1=1\), \(\ell_2=10\), and weights \(w_1=1/10\), \(w_2=9/10\), let total separation be \(L>0\). The midpoint \(x=L/2\) changes from a strict local maximum to a strict local minimum of the community passage objective and back to a maximum and then a minimum as \(L\) increases, with exactly **four** open stability intervals separated by three distinct positive critical lengths. The squared half-lengths \(u_j=(L_j/2)^2\) are the three roots, in increasing order, of
\[
-10u^3+683u^2-8009u+10900=0.
\]
They lie in \((1,2)\), \((12,14)\), and \((53,55)\); numerically \(L_j\approx2.502053700189,\ 7.196816206216,\ 14.667841142285\). On the four open length intervals separated by these lengths the midpoint is, respectively, a strict local maximum, strict local minimum, strict local maximum, and strict local minimum of passage success. **At the three boundary lengths the quadratic stability test vanishes; no boundary classification is asserted.**

At the exact length \(L=14\), the midpoint \(x=7\) is a strict local maximum but not a global maximum. Exactly three strict local maxima of passage success occur, at \(x=7\) and at the symmetric pair
\[
x_\pm=7\pm\sqrt{u_*},
\qquad 10u_*^3-351u_*^2-4259u_*+81852=0,
\qquad 40<u_*<41.
\]
The pair \(x_\pm\approx0.626292211822,13.373707788178\) are the **only global maximizers**. The other two stationary points (local minima of passage success) correspond to the unique root of the same cubic in \((11,12)\).

## Assumptions and scope

There is a source habitat at coordinate \(0\), a destination at \(L>0\), and exactly one perfectly usable stepping-stone habitat at \(x\in[0,L]\). A successful journey requires **two independent stage successes**: reach the intermediate habitat across distance \(x\), then restart from there and reach the destination across distance \(L-x\). No competing routes, predation, demographic dynamics, settlement deficits, or intervention costs are included. The model assigns a species-specific stage success probability
\[
s_\ell(d)=\frac{1}{1+(d/\ell)^2}\qquad(d\ge0,\ \ell>0),
\]
which is a valid nonincreasing survival function for a nonnegative flight-capability distance. It is a Burr XII / log-logistic tail with parameters \(c=2\), \(k=1\); **the biological applicability of this choice is an assumption, not an empirical inference**.

Species \(i\) has two-stage success \(P_i(x)=s_{\ell_i}(x)s_{\ell_i}(L-x)\). The community objective is the positive weighted geometric mean
\[
G_L(x)=P_1(x)^{1/10}P_2(x)^{9/10}.
\]
All maximizers and extrema below refer to this precise fixed-distance, two-stage objective. The single-species comparison replaces \(G_L\) by \(P_\ell\), with one arbitrary fixed \(\ell>0\).

## Proof

**1. Reduction.** Set \(h=L/2\), \(z=x-h\), \(u=z^2\in[0,h^2]\). Maximizing passage success is equivalent to minimizing the log-loss
\[
\Phi_L(x)=-\log G_L(x)
=\sum_{i=1}^2w_i\log\left[(1+(x/\ell_i)^2)(1+((L-x)/\ell_i)^2)\right].
\]
For any \(\ell>0\), the numerator of the corresponding product is
\[
Q_{\ell,h}(u)
=(\ell^2+(h+z)^2)(\ell^2+(h-z)^2)
=u^2+2(\ell^2-h^2)u+(\ell^2+h^2)^2>0.
\]
Hence the only dependence on the sign of \(z\) is through reflection, and
\[
\frac{d}{du}\Phi_L
=\sum_i w_i\frac{2(u+\ell_i^2-h^2)}{Q_{\ell_i,h}(u)}.
\]
The factors \(\ell_i^{-4}\) in the passage denominators add constants to \(\Phi_L\) and do not change its optimizers.

**2. One scale cannot be metastable at the midpoint.** For one species,
\[
\frac{d}{du}\log Q_{\ell,h}(u)
=\frac{2(u+\ell^2-h^2)}{Q_{\ell,h}(u)}.
\]
If \(h\le\ell\), this is positive for every \(u>0\); the midpoint is the unique global success maximizer. If \(h>\ell\), the unique minimizing value of \(u\) is \(u=h^2-\ell^2>0\), and exactly two reflected off-center locations are global success maximizers, while the midpoint is a strict local *minimum* of success. Thus **the midpoint cannot be a strict local success maximum without being globally optimal** for any single scale. Equality \(h=\ell\) has a flat quartic at the unique central optimum.

**3. Three midpoint-stability switches for two scales.** The midpoint's second derivative of log-loss is
\[
\Phi_L''(h)=4\left[\frac{\frac1{10}(1-h^2)}{(1+h^2)^2}
+\frac{\frac9{10}(100-h^2)}{(100+h^2)^2}\right].
\]
Put \(v=h^2\). After multiplication by a strictly positive denominator, its sign equals the sign of
\[
P(v)=(1-v)(100+v)^2+9(100-v)(1+v)^2
=-10v^3+683v^2-8009v+10900.
\]
Direct exact integer substitutions give \(P(1)=3564>0\), \(P(2)=-2466<0\), \(P(12)=-4136<0\), \(P(14)=5202>0\), \(P(53)=16200>0\), and \(P(55)=-27270<0\). Therefore \(P\) has one real root in each of \((1,2)\), \((12,14)\), \((53,55)\). A cubic has no other roots. As \(P(0)>0\) and its leading coefficient is negative, the signs alternate \(+,-,+,-\). Where \(\Phi_L''(h)>0\), the midpoint is a strict local *maximum* of \(G_L\), and where it is negative, a strict local minimum. This proves the complete three-switch statement on the open intervals.

**4. Complete stationary-point classification at \(L=14\).** Here \(h=7\), and
\[
Q_{1,7}(u)=u^2-96u+2500,\qquad
Q_{10,7}(u)=u^2+102u+22201.
\]
The derivative of log-loss with respect to \(u\) is
\[
\frac{d\Phi_{14}}{du}
=\frac{(2u-96)Q_{10,7}(u)+9(2u+102)Q_{1,7}(u)}{10Q_{1,7}(u)Q_{10,7}(u)}
=\frac{H(u)}{5Q_{1,7}(u)Q_{10,7}(u)},
\]
where \(H(u)=10u^3-351u^2-4259u+81852\). Both denominators are strictly positive for \(0\le u\le49\). Exact integer evaluations give \(H(0)=81852>0\), \(H(11)=5842>0\), \(H(12)=-2520<0\), \(H(40)=-10108<0\), \(H(41)=6412>0\), and \(H(49)=206900>0\). There are thus two positive roots in \((11,12)\) and \((40,41)\). Descartes' rule of signs permits at most two positive roots for the sign sequence \((+,-,-,+)\), so they are the only ones. As \(u\) increases, \(\Phi_{14}\) increases, then decreases, then increases. On the \(x\)-interval this yields precisely three strict local minima of log-loss, namely at the midpoint and the two reflected positions with \(u=u_*\); the remaining two stationary points are strict local maxima of log-loss. The endpoints cannot minimize log-loss because its derivative in \(x\) at \(x=0\) is strictly negative and at \(x=14\) strictly positive.

**5. The asymmetric minima are globally better.** At \(x=1\) and \(x=7\), their exact single-species passage-denominator ratios are
\[
\frac{D_1(1)}{D_1(7)}=\frac{340}{2500},\qquad
\frac{D_{10}(1)}{D_{10}(7)}=\frac{27169}{22201},
\]
where \(D_\ell(x)=(1+(x/\ell)^2)(1+((14-x)/\ell)^2)\). Exact integer arithmetic establishes
\[
\frac{340}{2500}\left(\frac{27169}{22201}\right)^9<1.
\]
Consequently \(\Phi_{14}(1)<\Phi_{14}(7)\); the center is not globally optimal. The only other local minima are the two reflected ones already classified, and their values agree by reflection. They are therefore precisely the two global passage maximizers. All inequalities are strict and persist under sufficiently small perturbations of the positive scales, weights, and total distance.

## Verification

`CHECK.py` is a standalone Python 3 standard-library checker. Run `python3 CHECK.py`. It recomputes the relevant cubic coefficients and exact integer signs, checks the exact strict rational comparison, verifies the critical derivative identity on a rational grid, checks the one-scale inequality over a supplementary rational grid, and numerically brackets the real roots to report approximate optimizers. It prints `ASSERTIONS_PASSED 1169`. Its finite grids and numerical root estimates **supplement**, but do not replace, the analytical derivations above; the polynomial sign, degree, and positivity arguments prove the claims for continuous ranges.

## Relationship to prior work

Gracanin and Mikac (2023) evaluate a corridor for eight arboreal species and highlight limitations of multispecies corridor suitability, but do not optimize this two-stage log-logistic crossing objective. Hodgson et al. (2012) explicitly analyze locations of stepping stones for population range-shift speed under different colonization dynamics; they find central placement usually best but address a different movement kernel, response, and single-species dynamical objective. Saura, Bodin and Fortin (2013) investigate long-distance population expansion through stepping-stone networks using reproductive establishment thresholds, not a two-scale geometric-mean optimization law. Melià et al. (2016) motivate aggregating species-specific connectivity indicators using a geometric mean, but do not derive the three stability switches or asymmetric global maximizers here. Exact public mathematical records on spectral spacing neutrality under exponential transport and on habitat-area allocation also concern other model classes. No claim is made that the cited sources prove the present result or that absence from inspected sources establishes universal historical priority.

## Limitations

The model assumes two independent successful stages and full use of the intermediate habitat after stage one. It omits patch area, intermediate reproduction time, mortality beyond the chosen survival law, alternative routes, spatial dimensionality, imperfect establishment, and stochastic environment. Its weighted objective and log-logistic kernel are explicit stylized choices and are not estimated from field data. The three critical lengths classify **local stability of central placement**, not all global optimizer switches as length varies. The precise locations at \(L=14\) are implicit algebraic roots, not elementary radicals. Biological or economic improvements cannot be inferred from the illustrative probability difference. The claim has not received independent external audit, and historical priority remains subject to wider literature review.

## References

- A. Gracanin and K. M. Mikac, *Evaluating modelled wildlife corridors for the movement of multiple arboreal species in a fragmented landscape*, Landscape Ecology 38 (2023), 1321–1337; first published 2023-03-15. https://doi.org/10.1007/s10980-023-01628-8
- J. A. Hodgson, C. D. Thomas, C. Dytham, J. M. J. Travis and S. J. Cornell, *The Speed of Range Shifts in Fragmented Landscapes*, PLOS ONE 7 (2012), e47141. https://doi.org/10.1371/journal.pone.0047141
- S. Saura, Ö. Bodin and M.-J. Fortin, *Stepping stones are crucial for species' long-distance dispersal and range expansion through habitat networks*, Journal of Applied Ecology 51 (2014), 171–182; first published 2013-10-01. https://doi.org/10.1111/1365-2664.12179
- P. Melià et al., *Looking for hotspots of marine metacommunity connectivity: a methodological framework*, Scientific Reports 6 (2016), 23705. https://doi.org/10.1038/srep23705
