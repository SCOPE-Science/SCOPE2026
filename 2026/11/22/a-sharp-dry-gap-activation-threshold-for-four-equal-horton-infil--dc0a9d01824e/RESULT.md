# A sharp dry-gap activation threshold for four equal Horton infiltration bursts

## Finding

Consider four prescribed wet bursts of equal duration \(w>0\), separated by three independently chosen dry gaps \(d_1,d_2,d_3\geq0\) with \(d_1+d_2+d_3=D>0\). Suppose the soil's instantaneous capacity during wet exposure decays exponentially toward a lower capacity, and during genuinely dry, unponded gaps it recovers exponentially toward its initial capacity, as specified below. Every wet burst has enough precipitation to saturate the infiltration rate throughout.

**Sharp four-burst law.** Define
\[
a=e^{-kw},\qquad D_c=\frac{\log(1+a)}{r},\]
where \(k,r>0\) are the wet-capacity decay and dry-capacity recovery rates. Exactly one feasible gap vector maximizes cumulative infiltrated volume:

- For \(0<D\leq D_c\), it is \((d_1,d_2,d_3)=(0,D,0)\). All available recovery time is concentrated between the second and third bursts.
- For \(D>D_c\), it is \((d_1,d_2,d_3)=(x,D-2x,x)\), where \(x\in(0,D/2)\) is uniquely determined by
\[
e^{rD}=e^{2rx}\bigl(e^{rx}+a\bigr).\]
  The interior gaps satisfy \(d_2>d_1=d_3>0\). Furthermore,
\[
d_2-d_1=\frac{1}{r}\log\bigl(1+a e^{-rx}\bigr)>0,\]
  and this difference tends to zero as \(D\to\infty\).

Thus the middle recovery gap is **strictly longer than either outer gap at every finite positive total-gap budget**; equal spacing is never optimal. The positive outer gaps activate together at exactly \(D_c\), and this support transition does not exist for two or three equal wet bursts. The transition is exact, not based on a discretized search.

A supporting structural statement applies to arbitrary \(n\ge2\) wet bursts of positive, possibly unequal durations: for the same wet/dry capacity law with initial full recovery, cumulative infiltration is strictly concave in the \(n-1\) dry-gap durations. Consequently any positive fixed total dry-time budget has a unique maximizing gap allocation.

## Assumptions and scope

Let \(f_{\min}\ge0\), \(\Delta>0\), \(k>0\), \(r>0\), and \(w>0\). Instantaneous infiltration capacity is \(f(t)=f_{\min}+\Delta y(t)\), with normalized capacity excess \(y(t)\in[0,1]\). At the start of the first burst, \(y(0)=1\). Each wet burst has uniform duration \(w\); supplied rainfall intensity is always at least \(f_{\min}+\Delta\), so actual infiltration equals the current capacity and excess rainfall runs off immediately without ponding. On wet intervals, \(\dot y=-ky\). On dry intervals, precipitation and ponded water are absent and \(\dot y=r(1-y)\). Dry periods contribute zero infiltration. Exactly four wet blocks and three possibly zero-length intervening dry blocks are permitted. No switching overhead, plant water uptake, surface storage limit, infiltration hysteresis, evaporation-dependent recovery, or inter-burst change of model parameters is included. The total wet exposure \(4w\) and total dry budget \(D\) are fixed.

The objective is total infiltrated water \(I=\int_{\mathrm{wet}}f(t)\,dt\). Since total rainfall is the same for every permitted schedule, maximizing \(I\) also minimizes total immediate infiltration-excess runoff under the stipulated high-rainfall assumption.

## Proof

Write \(a=e^{-kw}\in(0,1)\) and \(u=1-a>0\). Starting a wet interval at normalized capacity \(y\), the capacity at its end is \(ay\), and the integrated infiltration in that wet interval is \(f_{\min}w+(\Delta/k)uy\). Starting a dry gap of length \(d\) at capacity \(z\), the capacity at its end is \(1-(1-z)e^{-rd}\).

Let \(y_j\) be the initial normalized capacity of wet burst \(j\), and put \(z_j=1-y_j\), its capacity deficit. The initial condition gives \(z_1=0\), and consecutive wet and dry updates imply
\[
z_{j+1}=e^{-rd_j}\bigl(u+a z_j\bigr),\qquad 1\le j\le3.\]
Expanding these recurrences gives
\[
\begin{aligned}
z_2&=u e^{-rd_1},\\
z_3&=u e^{-rd_2}+au e^{-r(d_1+d_2)},\\
z_4&=u e^{-rd_3}+au e^{-r(d_2+d_3)}+a^2u e^{-rD}.
\end{aligned}
\]
Since \(I=4f_{\min}w+(\Delta u/k)\sum_{j=1}^4(1-z_j)\), maximizing it is exactly equivalent to minimizing
\[
L(d_1,d_2,d_3)=e^{-rd_1}+e^{-rd_2}+e^{-rd_3}
+a\left[e^{-r(d_1+d_2)}+e^{-r(d_2+d_3)}\right]+a^2e^{-rD}.
\]
Indeed \(I=4f_{\min}w+(\Delta/k)(4u-u^2L)\). The three individual exponential terms make \(L\) strictly convex on all of \(\mathbb R^3\), while the other two nonconstant terms have positive-semidefinite Hessians. Thus a unique global minimizer exists on the compact simplex \(d_j\ge0\), \(\sum d_j=D\). (The constant \(a^2e^{-rD}\) does not affect convexity on this simplex.)

The objective and constraint are invariant under reversal \((d_1,d_2,d_3)\mapsto(d_3,d_2,d_1)\). By uniqueness, the minimizer must have \(d_1=d_3=x\), \(d_2=D-2x\), with \(0\le x\le D/2\). The reduced loss is
\[
\ell(x)=2e^{-rx}+e^{-r(D-2x)}+2ae^{-r(D-x)}+a^2e^{-rD}.
\]
It is strictly convex and has derivative
\[
\ell'(x)=2r\left[-e^{-rx}+e^{-r(D-2x)}+ae^{-r(D-x)}\right].
\]
At the lower endpoint, \(\ell'(0)=2r[(1+a)e^{-rD}-1]\), which is nonnegative exactly when \(D\le D_c=r^{-1}\log(1+a)\). Strict convexity then makes \(x=0\) the unique minimizer, including equality. If \(D>D_c\), this derivative is strictly negative, while \(\ell'(D/2)>0\). Hence a unique interior zero exists. Multiplying \(\ell'(x)=0\) by \(e^{rD+rx}\) yields
\[
e^{rD}=e^{3rx}+ae^{2rx},
\]
the displayed determining equation. Its right side strictly increases with \(x\), and \(D>2x\) at the root. Taking logarithms gives
\[
D=3x+\frac{1}{r}\log(1+ae^{-rx}),
\]
so \(d_2=D-2x=x+r^{-1}\log(1+ae^{-rx})>x\). As \(D\to\infty\), the root \(x\to\infty\); the displayed positive difference therefore tends to zero.

For three equal wet bursts, the analogous deficit loss is proportional, after fixing total dry time \(D\), to \(e^{-rd_1}+e^{-rd_2}+ae^{-rD}\), whose unique minimizer is \((D/2,D/2)\) for every \(D>0\). For two bursts only one dry gap exists. Therefore four wet bursts are the smallest number permitting the stated support-activation transition.

Finally, for unequal wet durations \(w_1,\ldots,w_n>0\), set \(a_j=e^{-kw_j}\), \(u_j=1-a_j\). Expansion of the deficit recurrence gives the exact cumulative-infiltration formula
\[
I= f_{\min}\sum_{i=1}^n w_i+\frac{\Delta}{k}\left[\sum_{i=1}^n u_i
-\sum_{1\le i<j\le n} u_i u_j
\left(\prod_{i<m<j}a_m\right)
\exp\left(-r\sum_{m=i}^{j-1}d_m\right)\right].
\]
Every pair coefficient is positive. Each negative exponential is concave as a function of the gap vector; the neighboring pairs \(j=i+1\) contribute \(-u_i u_{i+1}e^{-rd_i}\), whose joint Hessian is strictly negative definite because every diagonal coefficient is positive. Thus \(I\) is strictly concave in all gap variables; a unique maximizer on any nonempty compact fixed-sum simplex follows.

## Verification

The accompanying standalone `checker.py` uses only Python's standard library. Run `python3 checker.py` in the directory containing the file. It separately evaluates the wet/dry state recurrence and the pairwise-loss expansion, checks 2,400 exact-rational polynomial identities with independent wet/dry multipliers, and compares the analytically specified optimum with 48,000 randomly selected admissible four-burst allocations. It makes 51,770 supplementary assertions; all passed during preparation. These finite checks support, but do not replace, the analytic infinite-parameter proof above.

For \(w=k=r=1\), \(D_c=\log(1+e^{-1})=0.31326168751822286\ldots\). At \(D=0.2\), the maximizing vector is \((0,0.2,0)\). At \(D=1\), it is approximately \((0.249305396174,0.501389207652,0.249305396174)\). The result is invariant under the baseline infiltration rate and the capacity scale as long as \(\Delta>0\).

## Relationship to prior work

The Horton infiltration law and exponential dry recovery are established engineering approximations rather than new mechanisms. Rossman and Huber's *Storm Water Management Model Reference Manual, Volume I: Hydrology* (revised January 2016), chapter 4, gives wet capacity decay, dry capacity recovery, and their empirical limitations. Dunkerley (2015) records the prevalence of intra-event rain/no-rain intervals; Dunkerley (first published 16 August 2016) demonstrates recovery during rain interruptions and uses affine Horton descriptions. Assouline (2019), in a freely readable full paper, treats irrigation rate and duration using infiltration-capacity curves, not redistribution of a prescribed total dry-gap duration among four wet blocks.

Karmeli and Peri (1974) study pulse-irrigation design, including wet/rest cycle selection. Their accessible abstract describes cycle number and operating-pattern choices, but their original article was not fully accessible in this review; it is a historical-priority risk and is **not** asserted to be completely noncovering. Published mathematical findings on Green–Ampt rain-intensity ordering or finite-capacity runoff stores have different state dynamics and objectives; those results do not directly imply the strict-concavity and four-burst threshold established here. No assertion of universal literature novelty or independent validation is made.

## Limitations

This is a theorem for a fully specified empirical infiltration-capacity model under high, constant wet rainfall. In particular, it does not extend automatically to low-intensity rainfall, ponding, Green–Ampt or Richards dynamics, time-varying wet intensity, infiltration-limited supply, evaporation-controlled drying, soil heterogeneity, initial capacity below the dry equilibrium, unequal wet-burst durations in the four-burst closed-form threshold, or arbitrary operational switching penalties. Although general strict concavity holds for unequal wet durations, the stated threshold and symmetry formula require four equal bursts and initial normalized capacity one. The zero-gap optimizer in the short-budget regime requires allowing adjacent wet blocks to merge without switching overhead. Priority relative to inaccessible older pulse-irrigation works remains provisional.

## References

1. D. Dunkerley, “Intra-event intermittency of rainfall: an analysis of the metrics of rain and no-rain periods,” *Hydrological Processes* 29 (2015), 3294–3305, DOI: https://doi.org/10.1002/hyp.10454; first published 2015-02-02.
2. D. Dunkerley, “An approach to analysing plot scale infiltration and runoff responses to rainfall of fluctuating intensity,” *Hydrological Processes* 31 (2017), 191–206, DOI: https://doi.org/10.1002/hyp.10990; first published online 2016-08-16.
3. L. A. Rossman and W. C. Huber, *Storm Water Management Model Reference Manual, Volume I: Hydrology (Revised)*, US EPA, EPA/600/R-15/162A, January 2016, ch. 4, https://nepis.epa.gov/Exe/ZyPDF.cgi/P100NYRA.PDF?Dockey=P100NYRA.PDF.
4. S. Assouline, “A Simple Method to Design Irrigation Rate and Duration and Improve Water Use Efficiency,” *Water Resources Research* 55 (2019), 6295–6301, DOI: https://doi.org/10.1029/2019WR025221.
5. D. Karmeli and G. Peri, “Basic Principles of Pulse Irrigation,” *Journal of the Irrigation and Drainage Division* 100 (1974), 309–319, DOI: https://doi.org/10.1061/JRCEA4.0000988; full text not inspected.
6. S. W. Bauer, “A Modified Horton Equation for Infiltration During Intermittent Rainfall,” *Hydrological Sciences Bulletin* 19 (1974), 219–225, DOI: https://doi.org/10.1080/02626667409493900; full text not inspected.
