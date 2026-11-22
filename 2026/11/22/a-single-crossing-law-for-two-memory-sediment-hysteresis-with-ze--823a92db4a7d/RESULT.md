# A single-crossing law for two-memory sediment hysteresis with zero net loop area

## Finding

For a normalized one-peak storm hydrograph and two competing exponential sediment-supply memories, there is a **sharp, rating-law-independent interval of source-strength ratios** in which the sediment–discharge trace forms exactly two oppositely oriented lobes. At one unique strength ratio in this interval, its rise-minus-fall signed area vanishes **despite the two nonzero lobes**. For an explicit linear discharge rating, this cancellation can occur even when the discharge and sediment response each have exactly one maximum, attained at the same instant. The result is an exact statement about a specified ideal model, not an inference about actual measured storm sediment sources.

## Assumptions and scope

Normalize storm duration and peak excess discharge so that, for real time \(0\le t\le2\),
\[
Q(t)=\begin{cases}t,&0\le t\le1,\\2-t,&1\le t\le2.\end{cases}
\]
Let \(g:[0,1]\to[0,\infty)\) be continuous, with \(g(0)=0\) and \(g(q)>0\) for \(0<q\le1\). Let \(a>0\), \(A>0\), \(B>0\), and rates \(k>h>0\). Define the excess sediment response (e.g. an idealized excess turbidity or excess concentration proxy)
\[
C(t)=g(Q(t))\bigl[a+A e^{-kt}+B(1-e^{-ht})\bigr].
\]
The \(A\)-term represents a rapidly exhausting near-channel supply, and the \(B\)-term a more slowly activating delayed contribution. Their interpretation is phenomenological; no source-transport equation or field calibration is assumed. The factor \(g\) is an otherwise arbitrary positive discharge-rating factor. Both \(Q\) and \(C\) vanish at the event endpoints.

Write \(b=B/A\). Let \(C_{\uparrow}(q)=C(q)\) and \(C_{\downarrow}(q)=C(2-q)\), \(0\le q\le1\), denote the rising and falling responses at matched discharge. Define clockwise contrast to be positive when \(C_{\uparrow}(q)>C_{\downarrow}(q)\), and the **rise-minus-fall signed contrast area**
\[
\mathcal A=\int_0^1[C_{\uparrow}(q)-C_{\downarrow}(q)]\,dq=\oint C\,dQ.
\]
This orientation convention is deliberately explicit; it is the negative of the conventional counterclockwise \(\oint Q\,dC\).

Set the exact positive thresholds
\[
b_{\rm peak}=e^{h-k}\frac{k}{h},\qquad
b_{\rm foot}=e^{h-k}\frac{\sinh k}{\sinh h}.
\]
They satisfy \(0<b_{\rm peak}<b_{\rm foot}\). The complete classification is:

1. If \(0<b\le b_{\rm peak}\), then \(C_{\uparrow}(q)>C_{\downarrow}(q)\) for every \(0<q<1\); there is one clockwise lobe and no interior branch intersection.
2. If \(b_{\rm peak}<b<b_{\rm foot}\), there is exactly one \(q_*(b)\in(0,1)\) with \(C_{\uparrow}(q_*)=C_{\downarrow}(q_*)\). The crossing is transverse; the rise exceeds the recession for \(0<q<q_*\), while the recession exceeds the rise for \(q_*<q<1\). There are exactly two oppositely oriented lobes. The crossing \(q_*(b)\) is strictly decreasing in \(b\), from \(1\) to \(0\) at the interval boundaries.
3. If \(b\ge b_{\rm foot}\), then \(C_{\uparrow}(q)<C_{\downarrow}(q)\) for every \(0<q<1\); there is one counterclockwise lobe and no interior branch intersection.

For every allowed rating law \(g\), the unique zero-area strength ratio is
\[
b_g=\frac{\int_0^1 g(q)[e^{-kq}-e^{-k(2-q)}]dq}
{\int_0^1 g(q)[e^{-hq}-e^{-h(2-q)}]dq},
\qquad b_{\rm peak}<b_g<b_{\rm foot}.
\]
Indeed \(\mathcal A>0\), \(=0\), or \(<0\) precisely when \(b<b_g\), \(b=b_g\), or \(b>b_g\), respectively. Thus zero net area is necessarily a genuine two-lobe event in this model.

For the natural linear excess-discharge rating \(g(q)=q\), define
\[
J(r)=\frac{1-2r e^{-r}-e^{-2r}}{r^2}>0,\qquad
b_g=\frac{J(k)}{J(h)}.
\]
If additionally \(a>Ak+Bh\), then both \(Q\) and \(C\) increase strictly on \((0,1)\) and decrease strictly on \((1,2)\). In particular, their unique peaks are synchronized at \(t=1\), even when \(b=b_g\) yields a transverse interior crossing and zero signed area.

## Proof

At equal discharge \(q\), subtraction cancels the baseline and common terms:
\[
\Delta(q):=C_{\uparrow}(q)-C_{\downarrow}(q)
=A g(q)\bigl[f_k(q)-b f_h(q)\bigr],
\quad f_r(q)=e^{-rq}-e^{-r(2-q)}=2e^{-r}\sinh(r(1-q)).
\]
For \(0<q<1\), \(f_h(q)>0\). Hence the sign of \(\Delta(q)\) is that of \(R(q)-b\), where
\[
R(q)=\frac{f_k(q)}{f_h(q)}=e^{h-k}\frac{\sinh(k(1-q))}{\sinh(h(1-q))}.
\]
For \(u>0\), the derivative of \(\log(\sinh(ku)/\sinh(hu))\) is \(k\coth(ku)-h\coth(hu)>0\). To prove this strict inequality, note that \(x\mapsto x\coth x\) has derivative
\[
\frac{\sinh x\cosh x-x}{\sinh^2x}>0\qquad(x>0),
\]
since the numerator vanishes at zero and has strictly positive derivative \(2\sinh^2x\). As \(u=1-q\) strictly decreases in \(q\), \(R(q)\) strictly decreases in \(q\). Its limits at \(q=1\) and \(q=0\) are exactly \(b_{\rm peak}\) and \(b_{\rm foot}\). The three regimes and uniqueness follow, including endpoint equalities (which cannot produce an *interior* intersection). At an interior root, \(\Delta'(q_*)=A g(q_*)f_h(q_*)R'(q_*)<0\), so the branch intersection is transverse. Inverse strict monotonicity of \(R\) proves the direction and endpoint limits of \(q_*(b)\).

Since \(g(q)f_h(q)>0\) on \((0,1)\), \(b_g\) is a strictly positive weighted average of \(R(q)\) over this interval. Strict monotonicity therefore gives \(b_{\rm peak}<b_g<b_{\rm foot}\), with no appeal to finite sampling. Directly \(\mathcal A=A(\int g f_k-b\int g f_h)\) gives all area signs. At \(b=b_g\), the sign of \(\Delta\) changes exactly once, so the two separated signed lobe areas are individually nonzero and cancel exactly.

For \(g(q)=q\), elementary integration gives
\[
\int_0^1q[e^{-rq}-e^{-r(2-q)}]dq
=\frac{1-2re^{-r}-e^{-2r}}{r^2}=J(r)>0.
\]
Finally set \(U(t)=a+Ae^{-kt}+B(1-e^{-ht})\). We have \(U(t)\ge a\) and \(|U'(t)|\le Ak+Bh\). With \(g(q)=q\), \(C(t)=Q(t)U(t)\). On the rising branch \(C'=U+QU'\ge a-(Ak+Bh)>0\); on the falling branch \(C'=-U+QU'\le-a+(Ak+Bh)<0\). Thus both peaks are unique and simultaneous, completing the proof.

## Verification

A dependency-free Python checker, `CHECKER.py`, independently evaluates the branch formula against direct time-domain values, tests strict threshold ordering and ratio monotonicity over many positive rate pairs, samples all three sign regimes and the unique crossing, verifies the area formula by Simpson quadrature, and tests the synchronized-peak certificate for a representative instance. The analytic proof above, not the finite checker, establishes the continuum and all-parameter statements.

For \(k=2\), \(h=1\), \(A=1\), \(g(q)=q\), let \(B=J(2)/J(1)\) and \(a=4\). Then
\[
b_{\rm peak}\approx0.7357588823,\qquad
b_g\approx0.8540017412,\qquad
b_{\rm foot}\approx1.1353352832,
\]
and the sole interior crossing is \(q_*\approx0.4403936787\). The two lobes have strictly opposite orientations while \(\mathcal A=0\) exactly. Here \(a=4>2+b_g\), so both peak at \(t=1\) with no secondary time peak.

Run `python3 CHECKER.py` from any directory with Python 3.9+ and standard library only.

## Relationship to prior work

Williams (1989) classified sediment concentration–discharge hysteresis into straight, clockwise, counterclockwise, mixed, and figure-eight forms, and stressed branch comparisons. Mather and Johnson (2014) fit event loops using an exponential supply component and an independent discharge-slope component, demonstrating that combinations of mechanisms can reproduce complex loops. Landers and Sturm (2013) documented additional hysteresis in sediment-versus-turbidity calibration arising from particle sizes. Perks and colleagues (2015) measured figure-eight sediment and phosphorus responses and identified fast and slow delivery pathways without deriving the present exact two-memory criterion. A later synthesis (2024) discusses the limitations of scalar hysteresis indices on complex event loops.

The present contribution is **not** the existence of figure-eight loops, the known limitations of scalar loop indices, or the elementary fact that two phenomenological mechanisms can oppose each other. It is the exact necessary-and-sufficient *two-rate parameter classification*, the rating-independent one-crossing theorem, the unique cancellation ratio lying strictly inside the two-lobe interval, and the simultaneous-single-peak construction for this specifically defined two-memory storm response. None of these exact results was located in the accessible primary texts or indexed results checked; that is a provisional literature conclusion rather than a proof of historical priority.

## Limitations

The hydrograph is deliberately triangular and uses normalized excess discharge, not observed total discharge. The sediment response is a phenomenological two-memory product model, not a derivation from a mass-conserving transport PDE; the multiplying rating factor does not imply physical sediment conservation. The rates are constant and positive with \(k>h\); results do not extend as stated to arbitrary source histories or multimodal storms. The uniqueness argument concerns branch intersections, not general smooth-flow bifurcations. Finite checks do not constitute an infinite proof. Williams (1989) was available as a published abstract/record but not as inspected full text, and related historical-priority risk remains. No independent audit has been performed.

## References

- Williams, G. P. (1989), “Sediment concentration versus water discharge during single hydrologic events in rivers,” *Journal of Hydrology* **111**, 89–106. DOI: https://doi.org/10.1016/0022-1694(89)90254-0. Published abstract inspected; original article full text unavailable.
- Landers, M. N., and T. W. Sturm (2013), “Hysteresis in suspended sediment to turbidity relations due to changing particle size distributions,” *Water Resources Research* **49**, 5487–5500. https://doi.org/10.1002/wrcr.20394. Full HTML article inspected.
- Mather, A. L., and R. L. Johnson (2014), “Quantitative characterization of stream turbidity-discharge behavior using event loop shape modeling and power law parameter decorrelation,” *Water Resources Research* **50**, 7766–7779. https://doi.org/10.1002/2014WR015417. First public online publication 2014-08-21; full HTML article, including methods and discussion, inspected.
- Perks, M. T., et al. (2015), “Dominant mechanisms for the delivery of fine sediment and phosphorus to fluvial networks draining grassland dominated headwater catchments,” *Science of the Total Environment* **523**, 178–190. https://doi.org/10.1016/j.scitotenv.2015.03.008. Author-accepted full PDF inspected.
- “A Review of Suspended Sediment Hysteresis” (2024), *Water Resources Research*. https://doi.org/10.1029/2024WR037216. Full HTML synthesis inspected as contextual comparison; not an archive-period motivating source.
