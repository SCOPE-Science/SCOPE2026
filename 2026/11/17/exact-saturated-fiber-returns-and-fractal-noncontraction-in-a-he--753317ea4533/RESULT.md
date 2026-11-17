# Exact saturated-fiber returns and fractal noncontraction in a heterochaos baker map

## Finding

For the original three-dimensional heterochaos baker map of Saiki, Takahasi and Yorke, let \(L_x=\{x\}\times[0,1]^2\), and let \(\ell_n(x)\) be the length of the third-coordinate projection of \(F^n(L_x)\). Define \(p_n\) as the uniform-Lebesgue probability that \(\ell_n(x)=1\). For every integer \(n\geq0\),

\[
p_n=3^{-n}\sum_{j=0}^{\lfloor n/2\rfloor}2^j\left(\binom nj-\binom n{j-1}\right),\qquad \binom n{-1}:=0.
\]

The complete generating function is

\[
\sum_{n\geq0}3^n p_n z^n
=\frac{2}{1-2z+\sqrt{1-8z^2}},
\]

and the probabilities have **different sharp constants at even and odd times**:

\[
p_n\sim \begin{cases}
12\sqrt{2/\pi}\,n^{-3/2}(2\sqrt2/3)^n,&n\text{ even},\\
16/\sqrt\pi\,n^{-3/2}(2\sqrt2/3)^n,&n\text{ odd}.
\end{cases}
\]

Let \(E_x=\{x\in[0,1]:\ell_n(x)\not\to0\}\), defined away from the countable set of ambiguous ternary expansions, and let \(E=E_x\times[0,1]^2\). Then

\[
\operatorname{Leb}(E)=0,\qquad
\dim_H(E_x)=\frac{\log(2\sqrt2)}{\log3},\qquad
\boxed{\dim_H(E)=2+\frac{\log(2\sqrt2)}{\log3}}.
\]

The dimensions remain the same under any deterministic convention on partition boundaries. This gives a sharp geometric size for the exceptional fibers excluded by almost-everywhere shrinkage, together with a finite-time return law for the *untruncated full vertical extent* of a leaf.

## Assumptions and scope

On the unit cube, split the domain into \(A=[0,1/3)\times[0,1]\times[0,1]\), \(D=[1/3,2/3)\times[0,1]\times[0,1]\), \(B=[2/3,1]\times[0,1]\times[0,1/2)\), and \(C=[2/3,1]\times[0,1]\times[1/2,1]\). Put \(\tau(x)=3x\pmod1\) for \(0\le x<1\), and define

\[
F(x,y,z)=\begin{cases}
(\tau(x),\,2y/3,\,z/2),&A,\\
(\tau(x),\,2y/3,\,(z+1)/2),&D,\\
(\tau(x),\,2/3+y/6,\,2z),&B,\\
(\tau(x),\,5/6+y/6,\,2z-1),&C.
\end{cases}
\]

For ternary-unique \(x\in[0,1)\), write its base-three digits \(d_1,d_2,\ldots\in\{0,1,2\}\). Define \(\xi_j=1\) when \(d_j=2\), and \(\xi_j=-1\) otherwise. Put \(S_0=0\), \(S_n=\sum_{j=1}^n\xi_j\), and \(M_n=\max_{0\le k\le n}S_k\). The quantitative results concern this fixed original map, not arbitrary nonuniformly hyperbolic baker maps. Boundary conventions change at most countably many \(x\)-fibers and hence neither Lebesgue probabilities nor the Hausdorff dimensions asserted here.

## Proof

**1. Exact length cocycle.** The third-coordinate projection of a full leaf remains a dyadic interval. Digits \(0,1\) send its length \(\ell\) to \(\ell/2\). Digit \(2\) sends the length to \(\min\{2\ell,1\}\): for a proper dyadic interval this is the appropriate doubling branch, and a full interval is carried onto a full interval by the two branches. Starting with \(\ell_0=1\), the nonnegative integer \(h_n=-\log_2\ell_n\) obeys the reflected recursion \(h_{n+1}=h_n+1\) on digits \(0,1\) and \(h_{n+1}=\max\{h_n-1,0\}\) on digit \(2\). Equivalently,

\[
\boxed{\ell_n=2^{S_n-M_n}}.
\]

Thus \(\ell_n=1\) if and only if the signed ternary-digit walk is at its running maximum at time \(n\).

**2. Ballot enumeration.** Under uniform \(x\), ternary digits are independent and each has probability \(1/3\). Time reversal of the first \(n\) independent increments transforms the event \(S_n=M_n\) into the event that every prefix partial sum is nonnegative. A nonnegative word with \(j\) downward increments and \(n-j\) upward increments exists only if \(j\le n/2\). Reflection gives \(\binom nj-\binom n{j-1}\) *uncolored* words. Each downward increment has two digit choices, giving weight \(2^j\), while each upward increment has one. Summation yields the stated exact formula.

**3. Generating function and parity constants.** A weighted balanced nonnegative excursion of length \(2m\) has \(2^m C_m\) words, with Catalan number \(C_m=\binom{2m}m/(m+1)\). Its generating function is

\[
D(z)=\sum_{m\ge0}2^m C_m z^{2m}
=\frac{2}{1+\sqrt{1-8z^2}}.
\]

Every nonnegative meander factors uniquely into a concatenation of such excursions separated by unmatched upward steps; hence its generating function is \(D(z)/(1-zD(z))\), which simplifies to the displayed formula for \(\sum3^n p_nz^n\). Set \(r=1/(2\sqrt2)\). Since \(|zD(z)|\le rD(r)=1/\sqrt2<1\) for \(|z|\le r\), the only singularities on the convergence circle are square-root branch points at \(z=\pm r\). Their first nonanalytic terms give the coefficient asymptotic

\[
3^np_n=\sqrt{\frac2\pi}\,(2\sqrt2)^n n^{-3/2}
\left((1-1/\sqrt2)^{-2}+(-1)^n(1+1/\sqrt2)^{-2}\right)
+O((2\sqrt2)^nn^{-5/2}).
\]

The identities \((1-1/\sqrt2)^{-2}=6+4\sqrt2\) and \((1+1/\sqrt2)^{-2}=6-4\sqrt2\) yield the two constants claimed.

**4. Upper Hausdorff bound.** If \(\ell_n(x)\not\to0\), the integer heights \(h_n=M_n-S_n\) are at most some fixed \(H\) for infinitely many \(n\). Since \(M_n\ge0\), these times have \(S_n\ge-H\). Let \(N_n(H)\) be the number of ternary words of length \(n\) with \(S_n\ge-H\). Weighting upward increments by \(\sqrt2\) and downward increments by \(2/\sqrt2\) shows directly that

\[
N_n(H)\le2^{H/2}(2\sqrt2)^n.
\]

Indeed, for any such word, \(1\le2^{(S_n+H)/2}\), and summing the latter weights over all ternary words gives \(2^{H/2}(\sqrt2+2/\sqrt2)^n\). Cover each fixed-height limsup set by the indicated length-\(3^{-n}\) ternary cylinders. For every \(s>\log(2\sqrt2)/\log3\), the sums of their \(s\)-diameter powers converge. The countable union over \(H\) has Hausdorff dimension at most \(\log(2\sqrt2)/\log3\).

**5. Matching lower bound.** Fix an integer \(m\ge1\). Choose any length-\(2m\) ternary word whose signed walk is nonpositive at every prefix and returns to zero. There are exactly \(2^m C_m\) choices. Append digit \(2\) to each word, and concatenate these blocks indefinitely. At the end of each block the walk attains a new running maximum, hence \(\ell_{(2m+1)k}=1\) for every positive integer \(k\). This gives a uniform-ratio self-similar ternary Cantor subset of \(E_x\) of dimension

\[
\frac{\log(2^mC_m)}{(2m+1)\log3}.
\]

As \(m\to\infty\), Stirling's formula \(C_m\sim4^m/(\sqrt\pi m^{3/2})\) makes these lower bounds tend to \(\log(2\sqrt2)/\log3\). Thus equality holds. The cube exceptional set is the Cartesian product of \(E_x\) with a two-dimensional unit square, giving the announced additive dimension. Finally, the strong law gives \(S_n/n\to-1/3\) for almost every \(x\), forcing \(h_n\to\infty\) and therefore \(\ell_n\to0\); hence \(\operatorname{Leb}(E)=0\).

## Verification

The standalone script `check_fiber_law.py` tests every ternary cylinder through length nine by independent rational interval dynamics and by the reflected-walk formula. Its saturation counts are \(1,1,3,5,15,29,87,181,543,1181\) for lengths zero through nine. It independently enumerates weighted nonpositive Dyck excursions through length twelve and confirms the Catalan block counts. These finite checks confirm computations but do not substitute for the all-length proofs above. The full coefficient asymptotics and Hausdorff bounds are proved analytically.

## Relationship to prior work

Saiki, Takahasi and Yorke introduce this precise map and establish coexistence of periodic points with different unstable dimensions and almost-everywhere shrinkage of leaves; in particular, their Proposition 12 supplies the one-step length rules used as a starting point here. Their paper does not give the all-time full-length return probabilities, parity-specific exponential amplitudes, or the Hausdorff dimension of the exceptional set of nonshrinking leaves. The later survey by Saiki, Takahasi, Yamamoto and Yorke discusses invariant measures, periodic points, Lyapunov exponents and mixing for generalized heterochaos baker maps, not these three exact geometric statistics. The reflection principle, Catalan enumeration, singularity transfer and Cantor-dimension argument are standard methods; their application together to this specific full-leaf return and exceptional-set geometry is the claimed advance.

## Limitations

The result describes the projections of *complete initial leaves*, not the trajectory separation of arbitrary initially nearby points with possibly differing ternary base coordinates. It assumes the exact original affine branches; it does not establish perturbation stability. The exceptional-set dimension is Hausdorff dimension, not positive volume. Some published papers on related generalized maps give stopping-time tail bounds and neutral-center mixing rates; these are different observables and do not by themselves supply the present two parity constants or nonshrinking-leaf dimension. Publication-priority uncertainties remain for unindexed studies of this precise saturated-leaf observable. No independent mathematical validation has been performed.

## References

1. Y. Saiki, H. Takahasi and J. A. Yorke, *Piecewise linear maps with heterogeneous chaos*, arXiv:1811.01009, initially posted 2018-11-02; *Nonlinearity* 34 (2021), 5744–5761. Exact map: Section 1.3; leaf contraction: Proposition 12.
2. Y. Saiki, H. Takahasi, K. Yamamoto and J. A. Yorke, *The dynamics of the heterochaos baker maps*, arXiv:2401.00836, initially posted 2024-01-01; revised version 2024-09-13. Sections 2 and 3.
3. H. Takahasi and K. Yamamoto, *Heterochaos baker maps and the Dyck system: maximal entropy measures and a mechanism for the breakdown of entropy approachability*, arXiv:2209.04905, initially posted 2022-09-11. Symbolic coding context.
