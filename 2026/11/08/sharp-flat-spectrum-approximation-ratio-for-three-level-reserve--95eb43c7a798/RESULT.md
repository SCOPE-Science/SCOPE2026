# Sharp flat-spectrum approximation ratio for three-level reserve-greedy integer bit allocation

## Finding

Fix three permitted integer bitwidths \(2\le \ell<m<H\). Define the integer-quantization error coefficient

\[
c(w)=\frac{1}{2^{w-1}-1}+\frac{1}{4(2^{w-1}-1)^2},
\qquad a=c(\ell),\quad b=c(m),\quad h=c(H).
\]

Consider any positive integer rank \(r\) with equal positive singular weights, normalized to \(\sigma_j=1\), and a certificate budget \(B^{\mathrm q}=re\). The optimization problem is to minimize \(\sum_{j=1}^r w_j\) over \(w_j\in\{\ell,m,H\}\) subject to \(\sum_j c(w_j)\le re\). Let \(G_r(e)\) denote the payload chosen by the three-level *reserve-greedy allocator* of Carson--Chen--Khan, Algorithm 1, and let \(O_r(e)\) be the minimum feasible payload. These are component-bit sums; the common factor-row dimension multiplier cancels in their ratio.

For every \(e\in[h,a]\), set

\[
\mathcal G(e)=H-(H-\ell)\frac{e-h}{a-h},
\]

and

\[
\mathcal O(e)=
\begin{cases}
H-(H-m)\dfrac{e-h}{b-h},&h\le e\le b,\\[5pt]
m-(m-\ell)\dfrac{e-b}{a-b},&b\le e\le a.
\end{cases}
\]

Then \(G_r(e)/r\to\mathcal G(e)\) and \(O_r(e)/r\to\mathcal O(e)\), **uniformly across the entire feasible nontrivial budget interval** \([h,a]\). Consequently the exact sharp worst-budget asymptotic ratio is

\[
\boxed{\lim_{r\to\infty}\ \sup_{h\le e\le a}
\frac{G_r(e)}{O_r(e)}
=\frac{H-(H-\ell)\dfrac{b-h}{a-h}}{m}>1.}
\]

The unique maximizing limiting budget is \(e=b\), where uniform \(m\)-bit assignment is the **unique** finite-rank optimal assignment for every \(r\). For any fixed \(\ell<m\), increasing the maximum available bitwidth \(H\) makes the sharp ratio diverge linearly:

\[
\lim_{H\to\infty}\frac{1}{H}
\left[\lim_{r\to\infty}\sup_{h\le e\le a}\frac{G_r(e)}{O_r(e)}\right]
=\frac{1-c(m)/c(\ell)}{m}>0.
\]

As a concrete certificate-level instance, with \((\ell,m,H)=(8,12,32)\), rank \(r=64\) and \(B^{\mathrm q}=64c(12)\), reserve-greedy assigns respectively \((3,15,46)\) components to the three widths, for payload \(1676\). All \(64\) components at \(12\) bits are optimal, with payload \(768\). Thus the *exact finite-rank ratio* is \(419/192\approx2.1822917\); the limiting sharp worst-budget ratio for these widths is approximately \(2.5428114\). For a rank-64 partial identity block with \(\|T\|_{\max}=1\), the prescribed certificate budget is \(64c(12)\approx0.0312691\), about \(3.13\%\) of its max norm. This is a claim about the **sufficient error-certificate allocation objective**, not observed quantization error.

## Assumptions and scope

The claim applies to the exact real-arithmetic singular-value-weighted certificate \(E_{\mathrm{cert}}=\sum_j\sigma_jc(w_j)\), to the precise low-to-high reserve test in Algorithm 1 of the cited source, to exactly three available bitwidth levels, and to equal strictly positive singular weights. All rank values \(r\ge1\), all triples of integers \(2\le\ell<m<H\), and all real normalized budgets \(h\le e\le a\) are covered. Budgets below \(h\) are infeasible; budgets at or above \(a\) make all-\(\ell\) allocation feasible and optimal, so the ratio is one. A common positive singular weight can be absorbed into the budget.

The payload excludes fixed scale metadata, precision-map metadata, and dense-block storage, exactly as in the source's local allocation optimization. The theorem does not compare actual reconstruction errors or assert failure of the source's feasibility guarantee.

## Proof

**1. Strictly convex coefficient.** Extend \(c(w)\) to real \(w>1\). With \(t=2^{w-1}\) and \(z=t-1>0\), direct differentiation gives

\[
c''(w)=(\log2)^2\frac{t}{z^4}\left(z^2+3z+\frac32\right)>0,
\qquad c'(w)<0.
\]

Thus \(a>b>h>0\), and strict convexity places the middle coefficient below the chord between the two extreme widths. Equivalently,

\[
\rho:=\frac{b-h}{a-h}<\frac{H-m}{H-\ell},
\]

so the stated sharp ratio is greater than one.

**2. Exact reserve-greedy counts.** At the first bitwidth, the reserve test accepts a new component only when the committed \(\ell\)-bit errors plus the cost \(h\) of assigning every remaining component \(H\) bits fit the budget. Therefore the number of \(\ell\)-bit components is exactly

\[
k_r=\left\lfloor r\frac{e-h}{a-h}\right\rfloor.
\]

At the second width the available slack over the all-\(H\) reserve is \(r(e-h)-k_r(a-h)\). Hence the number assigned \(m\) bits is exactly

\[
q_r=\min\left\{r-k_r,\left\lfloor
\frac{r(e-h)-k_r(a-h)}{b-h}\right\rfloor\right\},
\]

and the remaining \(r-k_r-q_r\) components receive \(H\) bits. Since the slack lies in \([0,a-h)\), we have \(0\le q_r\le(a-h)/(b-h)\) uniformly in rank and budget. Substituting the counts into the payload gives

\[
G_r(e)=\ell k_r+m q_r+H(r-k_r-q_r)
=r\mathcal G(e)+O_{\ell,m,H}(1)
\]

uniformly over \(e\in[h,a]\). The exact lower and upper rounding errors follow directly from \(0\le rt-k_r<1\) and the displayed bound on \(q_r\).

**3. The exact continuous optimum and finite-rank limit.** The three points \((h,H)\), \((b,m)\), and \((a,\ell)\) form a strictly convex lower envelope when payload is graphed against allowed error. A supporting affine line to either adjacent segment shows that every feasible allocation with average error no more than \(e\) has average payload at least \(\mathcal O(e)\). Equivalently, this is the two-constraint linear-programming relaxation of the three possible bitwidth counts. For \(h\le e\le b\), assign \(\lfloor r(e-h)/(b-h)\rfloor\) components width \(m\), the rest width \(H\); for \(b\le e\le a\), assign \(\lfloor r(e-b)/(a-b)\rfloor\) components width \(\ell\), the rest width \(m\). Each assignment is feasible and its payload is at most \(r\mathcal O(e)+\max\{H-m,m-\ell\}\). Consequently

\[
r\mathcal O(e)\le O_r(e)\le
r\mathcal O(e)+\max\{H-m,m-\ell\}
\]

uniformly. Since \(\mathcal O(e)\ge\ell>0\), the ratio \(G_r(e)/O_r(e)\) converges uniformly to \(\mathcal G(e)/\mathcal O(e)\).

**4. Sharp maximization and boundary.** On either side of \(e=b\), the ratio of the two strictly positive affine functions is a fractional-linear function with derivative of constant sign. At \(e=h\) and \(e=a\), both continuous payloads agree (ratio one). At \(e=b\), strict coefficient convexity gives \(\mathcal G(b)>\mathcal O(b)=m\). It follows that the ratio strictly increases on \([h,b]\), strictly decreases on \([b,a]\), and has the asserted unique maximum. Uniform ratio convergence lets the supremum commute with the rank limit.

At the critical budget \(e=b\), strict Jensen convexity gives

\[
c\left(\frac1r\sum_jw_j\right)
\le\frac1r\sum_jc(w_j)\le c(m).
\]

Because \(c\) is strictly decreasing, \(r^{-1}\sum_jw_j\ge m\). Equality forces all widths to equal \(m\) by strict convexity. Thus \(O_r(b)=mr\) uniquely for every finite \(r\). Finally \(h=c(H)\to0\) as \(H\to\infty\), giving the stated positive linear growth coefficient.

## Verification

The standalone `verify.py` requires Python 3 standard library only. It implements the source's reserve test with exact rational numbers independently of the derived floor formulas, exhaustively enumerates the three-width payload optimum for all ranks up to \(12\) across four different permitted palettes, and tests all budget values attainable from three-level count configurations. It also checks continuous lower envelopes, analytic rounding bounds, and the explicit 64-component case. Command:

```
python verify.py
```

On the packaged script the run prints `PASS 17723 exact-rational checks` together with the 64-component allocation \((3,15,46)\). These are reproducibility checks; the uniform all-rank and all-budget statements rest on the proof, not enumeration.

## Relationship to prior work

Carson, Chen and Khan (2026), Section 2.2, equations (2.60)--(2.69), provide the exact coefficient, certificate-constrained integer payload problem, the reserve-greedy algorithm and its feasibility guarantee. Their Remark 28 acknowledges that the greedy allocation is not generally storage optimal; Section 4.2, Section 4.3 and Supplement B report finite empirical comparisons with a dynamic-programming optimum, including flat spectra. They do **not** state the all-budget sharp asymptotic ratio for every three-level palette, its critical-budget maximizer or its unbounded maximum-precision law. The present analysis retains their same allocation objective and reserve rule, rather than comparing to a different heuristic.

Classical resource-allocation and mixed-precision quantization methods, such as Wei (2021) and Satoki et al. (2021), study related discrete allocation problems and different algorithms; generic linear-program convexification supplies one ingredient of the proof. The new claim is confined to the particular certificate and reserve-greedy rule, not the invention of knapsack convexification or greedy counterexamples generally.

## Limitations

The allocation ratio is **not** a bound on actual matrix approximation error and does not show that the quantized matrices fail their prescribed certificate. Actual errors may be much smaller than the certificate, including zero on matrices whose balanced factors quantize exactly. For the example the high-precision fallback uses 32-bit integers under the source's mathematical coefficient model; real hardware integer support may differ. Fixed metadata and overall hierarchical-matrix storage can attenuate the local payload gap. The sharpness statement is restricted to exactly three permitted bitwidths and flat singular weights; no claim is made for arbitrary spectra or larger palettes. Historical priority versus all earlier approximation-algorithm literature has not been independently established.

## References

1. E. Carson, X. Chen, R. Khan, *Integer-Quantized Hierarchical Matrices with Adaptive Bit Allocation*, arXiv:2610.40134v1, first public 29 October 2026. Full text: https://arxiv.org/html/2610.40134v1. In particular Section 2.2 and Algorithm 1, Section 4, and Supplement B.
2. A. Wei, *BitAllocation: A Resource Allocation Algorithm For Fixed-Point Quantization*, January 2021. https://adamwei.com/publication/bitallocation/.
3. T. Satoki et al., *Greedy Search Algorithm for Mixed Precision in Post-Training Quantization of Convolutional Neural Network Inspired by Submodular Optimization*, Proceedings of Machine Learning Research 157, 2021. https://proceedings.mlr.press/v157/satoki21a.html.
