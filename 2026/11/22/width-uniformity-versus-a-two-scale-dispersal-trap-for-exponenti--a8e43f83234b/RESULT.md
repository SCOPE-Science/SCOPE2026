# Width uniformity versus a two-scale dispersal trap for exponential seed transport

## Finding

An idealized downstream seed-transport problem has two sharply different optimization geometries. If two disjoint suitable habitat bands have **equal physical widths**, their one-seed landing probability is strictly log-concave in the exponential travel-rate parameter, and thus has exactly one globally optimal dispersal scale, however far apart the bands lie. If instead the bands are geometrically similar, \([a,2a]\) and \([La,2La]\), then for **every real \(L\ge 9\)** their landing probability has exactly two strict local maxima separated by one strict local minimum. The local maximum at the smaller travel rate (longer mean travel distance) is the unique global maximum; the other local maximum is strictly suboptimal. For two touching geometrically similar bands (\(L=2\)), the optimum is unique.

These are the full assertions: no claim is made about the exact phase boundary within \(2<L<9\), and a local fitness maximum is not by itself a proof of evolutionary hysteresis.

## Assumptions and scope

Let the single-seed downstream travel distance \(X_\lambda\) have density \(\lambda e^{-\lambda x}\) for \(x\ge0\), with free strategy parameter \(\lambda>0\). A seed is counted as successful exactly when it lands in the union of two indicated closed habitat intervals. Endpoint choices do not affect the continuous probability. There is one dispersal event, identical success per unit of suitable ground, no travel costs except loss in the unsuitable matrix, no density dependence, no overlapping bands, and no further demographic dynamics.

**Equal-width configuration:** for any real \(a,w>0\) and \(b\ge a+w\), let \(H=[a,a+w]\cup[b,b+w]\). The success probability is
\[
P_{\mathrm{equal}}(\lambda)=(1-e^{-w\lambda})(e^{-a\lambda}+e^{-b\lambda}).
\]

**Geometrically scaled configuration:** for any \(a>0\), real \(L\ge2\), let \(H=[a,2a]\cup[La,2La]\), and put \(t=a\lambda\). Then
\[
P_L(\lambda)=F_L(t)=g(t)+g(Lt),\qquad g(t)=e^{-t}-e^{-2t}.
\]
In each configuration the two habitat bands are disjoint in their interiors. \(1/\lambda\) is the mean travel distance.

## Proof

**1. Equal-width bands are strictly log-concave.** Rescale \(t=w\lambda\), and write \(\alpha=a/w>0\) and \(\delta=(b-a)/w\ge1\). With \(F(t)=(1-e^{-t})e^{-\alpha t}(1+e^{-\delta t})\), logarithmic differentiation gives
\[
\psi(t)=\frac{d}{dt}\log F(t)=\frac1{e^t-1}-\alpha-\frac{\delta}{1+e^{\delta t}},
\]
\[
\psi'(t)=-\frac1{4\sinh^2(t/2)}+\frac{\delta^2}{4\cosh^2(\delta t/2)}<0.
\]
The strict inequality follows for every \(x>0\) and \(\delta\ge1\) from \(\cosh(\delta x)>\sinh(\delta x)\ge\delta\sinh x\). The second inequality is convexity of \(\sinh\) with \(\sinh0=0\). Thus \(\log F\) is strictly concave. As \(t\downarrow0\), \(\psi(t)\to+\infty\); as \(t\to\infty\), \(\psi(t)\to-\alpha<0\). There is exactly one zero of \(\psi\), hence a unique global maximizer of \(F\), with no other stationary point.

**2. At most three critical rates in the scaled-band configuration.** Direct differentiation gives
\[
F_L'(t)=-e^{-t}+2e^{-2t}-Le^{-Lt}+2Le^{-2Lt}.
\]
For \(L>2\), its four exponents \(1,2,L,2L\) are distinct. A nonzero linear combination of \(k\) distinct real exponentials has at most \(k-1\) distinct real zeros: divide by the slowest exponential, differentiate, and use Rolle's theorem inductively. Accordingly, \(F'_L\) has at most three positive zeros. This argument bounds the zeros of the derivative analytically, not by finite numerical scanning.

**3. There are three, with alternating strict-extremum types, for every \(L\ge9\).** Write \(g'(t)=2e^{-2t}-e^{-t}\). Four analytic sign tests locate the zeros:
\[
F'_L(0)=1+L>0,\qquad F'_L(1/L)<0,\qquad F'_L(1/2)>0,\qquad F'_L(\log2)<0.
\]
For the second sign, note that \(g'(0)=1\) and \(g''(u)=e^{-u}-4e^{-2u}<-2\) on \(0\le u\le1/9\); the bound follows from \(e^{-2u}\ge1-2u\). Hence \(g'(1/L)<1-2/L\). Let \(c=e^{-1}-2e^{-2}=(e-2)/e^2>3/32\), using \(8/3<e<4\) and monotonicity of \((v-2)/v^2\) for \(2<v<4\). We obtain
\[
F'_L(1/L)=g'(1/L)-Lc<1-\frac2L-\frac{3L}{32}<0 \quad(L\ge9).
\]
The last expression is already negative at \(L=9\) and strictly decreases thereafter.

For the third sign, \(g'(1/2)=2/e-e^{-1/2}>129/1100\), using \(27/10<e<11/4\). Also \(g'(L/2)\ge-e^{-L/2}\) and, because \(Le^{-L/2}\) decreases for \(L\ge9\),
\[
F'_L(1/2)\ge g'(1/2)-Le^{-L/2}>\frac{129}{1100}-\frac{11}{100}>0.
\]
Here \(9e^{-9/2}<11/100\) follows directly from \(e>27/10\). Lastly, \(g'(\log2)=0\) and \(g'(L\log2)<0\) for \(L>1\). As \(0<1/L<1/2<\log2\), continuity gives one critical point in each of the three disjoint intervals \((0,1/L)\), \((1/L,1/2)\), and \((1/2,\log2)\). The upper bound in Step 2 proves there are exactly these three and that they are strict maximum, minimum, maximum in that order. Denote them \(t_1,t_2,t_3\).

**4. The longer-range maximum is globally unique.** At the rightmost maximum \(1/2<t_3<\log2\), compare \(F_L(t_3/L)\) with \(F_L(t_3)\):
\[
F_L(t_3/L)-F_L(t_3)=g(t_3/L)-g(Lt_3).
\]
Since \(1-e^{-u}\ge ue^{-u}\) for \(u>0\),
\[
g(t_3/L)\ge\frac{t_3}{L}e^{-2t_3/L}>\frac1{4L},
\]
where \(e^{-2\log2/L}>1/2\) for \(L\ge9\). But \(g(Lt_3)<e^{-L/2}<1/(4L)\), using \(Le^{-L/2}\le9e^{-9/2}<11/100<1/4\). Thus \(F_L(t_3/L)>F_L(t_3)\); the rightmost local maximum cannot be global. The function tends to zero both as \(t\downarrow0\) and as \(t\to\infty\), and \(t_1,t_3\) are its only local maxima. Therefore \(t_1\) is the unique global maximizer, corresponding to the longer mean dispersal distance.

**5. Touching bands.** When \(L=2\), the union is simply \([a,4a]\), and \(F_2(t)=e^{-t}-e^{-4t}\). Its only maximizer is \(t=(\log4)/3\). Hence a pair of separated, width-heterogeneous bands is sufficient to create the double-peak geometry, whereas neither a single band nor a pair of equal-width bands can do so in this model.

## Verification

The standalone \(VERIFY.py\) checks the exact rational sign bounds, evaluates high-precision signs for several values of \(L\ge9\), verifies the distinct stationary points and the global comparison for the natural example \(L=9\), and counts the positive roots in \((0,1)\) of the exact derivative polynomial for integer \(L=9\) using Sturm theory. These calculations check the proof but are not substituted for its universal quantifiers.

For \(L=9\), numerical critical values \(t_1\approx0.102195\), \(t_2\approx0.405091\), and \(t_3\approx0.641803\) give probabilities approximately \(0.327430\), \(0.247558\), and \(0.252397\), respectively. The globally best low-rate strategy and the suboptimal high-rate strategy are separated by a strict fitness valley.

## Relationship to prior work

The ecological motivation is the openly accessible study of de Jager and Soons, first posted as a 2022 bioRxiv preprint and subsequently published in 2023; it numerically explores evolutionary hysteresis under nonlinear colonization, seed-size costs and a many-cell fragmented landscape. The present claim is **not** the previously reported general qualitative occurrence of hysteresis. Its different result is the analytic strict log-concavity theorem for arbitrary two equal-width bands, contrasted with a proved two-local-maxima regime and global ranking for two scaled bands under a one-seed exponential kernel. Treep et al. (2021) instead simulate competition between power-law kernels on dynamic landscapes; Finand et al. (2023/2024) model competition/colonization and aggregation. Their reported simulation results do not directly entail these precise derivative and optimizer assertions. The exponential-polynomial zero-counting lemma is a classical mathematical tool, not claimed as an original contribution.

## Limitations

The \(L\ge9\) threshold is a **proved sufficient separation condition, not the exact onset** of bimodality. Behavior within \(2<L<9\) is not classified by this result. The scaled bands differ in absolute length, so the comparison does not isolate geometric distance from habitat area. Establishment probability for one seed is not a saturated recruitment function, population fitness, evolutionary stable strategy, or stochastic establishment process. Multigenerational hysteresis, mutation, seed-production costs, repeated dispersal, and field validation are not proved. Broader historical priority beyond the inspected sources has not been independently certified.

## References

1. de Jager, M. and Soons, M. B., *Critical transitions and evolutionary hysteresis in movement: Habitat fragmentation can cause abrupt shifts in dispersal that are difficult to revert*, bioRxiv preprint, October 2022, DOI: https://doi.org/10.1101/2022.10.10.510956; *Ecology and Evolution* 13 (2023), e10147, https://doi.org/10.1002/ece3.10147.
2. Treep, J. et al., *Seed dispersal as a search strategy: dynamic and fragmented landscapes select for multi-scale movement strategies in plants*, *Movement Ecology* 9 (2021), 4, https://doi.org/10.1186/s40462-020-00239-1.
3. Finand, B. et al., *Evolution of dispersal and the maintenance of fragmented metapopulations*, *Oikos* (first published 5 December 2023), https://doi.org/10.1111/oik.10490.
