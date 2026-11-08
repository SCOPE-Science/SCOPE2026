# Sharp dilogarithmic stationary-tail prefactor under weak partial resetting

## Finding

For Brownian diffusion with Poissonian partial resetting, the stationary position admits an explicit non-Gaussian large-displacement law with its **sharp probability prefactor**, not merely a logarithmic rate. Let \(X_h\) be the stationary position in the model specified below and put \(\ell=\sqrt{D/r}\). For \(y>0\), let \(t_y\in(0,1)\) be the unique solution of

\[
-\frac{2\log(1-t_y^2)}{t_y}=y.
\]

Define

\[
\Lambda(t)=\operatorname{Li}_2(t^2),\quad
I(y)=yt_y-\Lambda(t_y),\quad
\Lambda''(t)=\frac{4}{1-t^2}+\frac{2\log(1-t^2)}{t^2}.
\]

Then, as \(h\downarrow0\),

\[
\boxed{\mathbb P\!\left(X_h\ge \frac{\ell y}{h}\right)
= \frac{\sqrt h}{t_y\sqrt{2\pi(1-t_y^2)\Lambda''(t_y)}}
\exp\!\left(-\frac{I(y)}h\right)(1+o(1)).}
\]

The error is uniform when \(y\) ranges over any fixed compact subset of \((0,\infty)\). Reflection symmetry gives the identical left-tail statement. The strictly convex rate function has the transitions

\[
I(y)=\frac{y^2}{4}-\frac{y^4}{64}+O(y^6)\quad(y\downarrow0),
\qquad I(y)=y-\frac{\pi^2}{6}+e^{-y/2}(1+o(1))\quad(y\to\infty).
\]

Thus its near-origin Gaussian quadratic approximation does not extrapolate to the rare-displacement linear tail; the leading multiplicative \(\sqrt h\) factor and its exact coefficient are fixed by the endpoint contribution to the geometric product.

## Assumptions and scope

Let \(D,r>0\) be fixed. Between independent rate-\(r\) reset events the one-dimensional process obeys \(dX_t=\sqrt{2D}\,dB_t\); each reset maps the pre-reset location \(x\mapsto ax\), where \(a=e^{-h/2}\in(0,1)\). The system is observed in its unique stationary distribution, whose existence and independent-Laplace decomposition are established in [1]. The weak-contraction parameter is \(h=-2\log a\downarrow0\), not the Poisson resetting rate. The theorem applies at physical displacement \(X_h\ge\ell y/h\) for fixed positive \(y\), uniformly on positive compact \(y\)-sets. It does not assert uniformity when \(y\downarrow0\) or \(y\to\infty\) jointly with \(h\downarrow0\).

By [1], with independent standard symmetric Laplace variables \(L_j\) of density \(e^{-|u|}/2\),

\[
W_h:=X_h/\ell\ \overset d=\ \sum_{j=0}^{\infty} e^{-hj/2}L_j.
\]

All analytic statements below use this exactly specified stationary distribution.

## Proof

**1. Exact transform and Euler--Maclaurin.** For \(|t|<1\), independence and the standard Laplace moment-generating function give

\[
M_h(t)=\mathbb E e^{tW_h}=\prod_{j=0}^{\infty}(1-t^2e^{-hj})^{-1}.
\]

For \(0<t<1\), set \(f_t(u)=-\log(1-t^2e^{-u})\), a smooth, exponentially decaying function together with all derivatives when \(t\) stays in a compact subinterval of \((0,1)\). The Euler--Maclaurin endpoint formula yields, with errors uniform together with the first two \(t\)-derivatives,

\[
K_h(t):=\log M_h(t)
=\frac1h\int_0^\infty f_t(u)\,du+\frac12 f_t(0)+O(h)
=\frac{\Lambda(t)}h-\frac12\log(1-t^2)+O(h).
\]

The second identity follows from the absolutely convergent expansion

\[
\int_0^\infty-\log(1-t^2e^{-u})\,du
=\sum_{k=1}^\infty\frac{t^{2k}}{k^2}=\operatorname{Li}_2(t^2).
\]

The limiting curvature \(\Lambda''(t)=\sum_{k\ge1}(4k^2-2k)t^{2k-2}/k^2>0\), while \(\Lambda'(t)\) increases continuously from zero to infinity as \(t\uparrow1\). Consequently each \(y>0\) has a unique saddle \(t_y\).

**2. Uniform tilted local limit.** Fix any compact \(T\subset(0,1)\), and tilt by

\[
\frac{d\mathbb P_{h,t}}{d\mathbb P_h}(W_h)
=e^{tW_h-K_h(t)}\qquad(t\in T).
\]

The tilted mean and variance are

\[
K_h'(t)=\Lambda'(t)/h+t/(1-t^2)+O(h),\qquad
K_h''(t)=\Lambda''(t)/h+O(1).
\]

Let \(\phi_{h,t}(s)=M_h(t+is)/M_h(t)\). For a single index with \(b=e^{-hj}\), elementary modulus comparison gives

\[
\left|\frac{1-bt^2}{1-b(t+is)^2}\right|
\le\frac{1}{1+bs^2}.
\]

For \(0\le j\le\lfloor1/h\rfloor\), \(b\ge e^{-1}\). The full product therefore obeys

\[
|\phi_{h,t}(s)|\le(1+e^{-1}s^2)^{-\lfloor1/h\rfloor},
\]

uniformly for \(t\in T\). This bound makes each tilted distribution continuously differentiable, provides a global density bound \(\sup_x f_{h,t}(x)=O(\sqrt h)\), and permits dominated Fourier inversion after the change \(s=\sqrt h\,z\). Specifically, Taylor expansion of \(K_h\) at any fixed \(t\in T\) shows that, uniformly over \(t\in T\) and bounded \(u\),

\[
f_{h,t}(\Lambda'(t)/h+u)=
\sqrt{\frac{h}{2\pi\Lambda''(t)}}(1+o(1)).
\]

The constant shift between \(\Lambda'(t)/h\) and the actual tilted mean is bounded on \(T\) and becomes negligible compared with the tilted standard deviation of order \(h^{-1/2}\). The frequency-majorant also bounds the tails of the inversion integral uniformly, proving the stated density approximation rather than merely convergence in distribution.

**3. Exact tail identity and prefactor.** Choose \(t=t_y\), for which \(\Lambda'(t)=y\). Exponential tilting gives the identity

\[
\mathbb P(W_h\ge y/h)
=e^{K_h(t)-ty/h}\int_0^\infty e^{-tu} f_{h,t}(y/h+u)\,du.
\]

For each bounded \(u\), Step 2 supplies the local density asymptotic. The global density bound from Step 2 and the integrable weight \(e^{-tu}\) allow dominated convergence on the half-line, uniformly for \(t_y\) in compact subsets of \((0,1)\). Therefore

\[
\int_0^\infty e^{-tu}f_{h,t}(y/h+u)\,du
=\frac{\sqrt h}{t\sqrt{2\pi\Lambda''(t)}}(1+o(1)).
\]

Step 1 gives

\[
e^{K_h(t)-ty/h}=(1-t^2)^{-1/2}\exp[-I(y)/h](1+O(h)).
\]

Multiplying yields exactly the boxed statement. Uniformity on compact \(y\)-sets follows from the stated uniformity on compact \(t\)-sets and continuity/strict monotonicity of the saddle map.

**4. Rate geometry and endpoint expansions.** The Legendre identity gives \(I'(y)=t_y\) and \(I''(y)=1/\Lambda''(t_y)>0\). Near zero, \(\Lambda(t)=t^2+t^4/4+O(t^6)\), so inversion yields the displayed quadratic-quartic expansion. For large \(y\), the saddle equation implies \(1-t_y^2=e^{-yt_y/2}\) and \(t_y=1-\tfrac12 e^{-y/2}(1+o(1))\). Using \(\operatorname{Li}_2(1-s)=\pi^2/6+s\log s-s+O(s^2|\log s|)\) establishes the displayed linear-tail refinement. These are sequential endpoint expansions of the fixed-\(y\) rate, not claims of joint uniformity with the weak-resetting limit.

## Verification

Run `python3 checks/verification.py` with NumPy and SciPy. The standalone checker evaluates the exact geometric-transform identity, Euler--Maclaurin endpoint term, saddle curvature, near-zero and far-tail expansions, and a tilted Fourier inversion of the **exact** stationary transform. Its 48 deterministic assertions passed. For fixed \(y=1\), the ratio of the exact Fourier-integral tail to the predicted sharp asymptotic was approximately \(0.75729\), \(0.84567\), \(0.90698\) at \(h=0.25,0.12,0.06\); for \(y=2\), the ratios were \(0.90114\), \(0.94534\), \(0.97039\). These finite comparisons are checks, not proofs of the infinite-dimensional or asymptotic statements; the proof is the four-step argument above.

## Relationship to prior work

The exact stationary geometric-Laplace decomposition, the transition from Laplace toward Gaussian stationary shapes, and the diffusion model itself are prior results of Tal-Friedman, Roichman and Reuveni [1]; they are not new claims here. General large-deviation theory for kernel-weighted sums appears in Vysotsky [2], but its stated theorem gives logarithmic large-deviation rates, rather than the full local sharp tail factor for the present infinite geometric array. Saulis and Deltuvienė [3] study the **same geometric weighting** in a general distribution family and establish discounted normal/moderate-deviation estimates; the present fixed-positive-displacement large-deviation scaling lies outside their displayed moderate range. Aurzada's general infinite weighted-sum theorem [4] concerns nonnegative stretched-exponential summands and does not directly apply to symmetric exponential Laplace summands. Classical saddlepoint techniques inform the proof; the contribution assessed here is the explicit dilogarithmic stationary **rate together with the sharp \(\sqrt h\) prefactor**, with a proof for this model and stated uniformity.

## Limitations

No priority or independent novelty certification is claimed. The precise full asymptotic may be derivable as a special case of an unidentified strong, general sharp-large-deviation theorem for triangular arrays, and the stationary transform is already known. The result holds at fixed positive \(y\), uniformly only on compact positive sets, and for the symmetric zero-drift diffusive model; it does not cover position-dependent resetting, non-Poisson clocks, general noise, or a joint \(y,h\) scaling at either endpoint. The numerical checker uses finite truncation and finite precision and cannot replace the proof.

## References

[1] O. Tal-Friedman, Y. Roichman, S. Reuveni, “Diffusion with Partial Resetting,” arXiv:2205.03363 (first posted 2022-05-06); *Physical Review E* 106, 054116 (2022). https://arxiv.org/abs/2205.03363 ; https://doi.org/10.1103/PhysRevE.106.054116 .

[2] V. Vysotsky, “Contraction principle for trajectories of random walks and Cramér's theorem for kernel-weighted sums,” *ALEA* 18 (2021), theorem 6.1. https://alea.impa.br/articles/v18/18-42.pdf ; https://doi.org/10.30757/ALEA.v18-42 .

[3] L. Saulis and D. Deltuvienė, “The discounted local limit theorems for large deviations” (2008), theorem 2, for geometric discounted sums. https://journals.vu.lt/LMR/en/article/download/18152/17326/30771 .

[4] F. Aurzada, “Large deviations for infinite weighted sums of stretched exponential random variables” (2019), arXiv:1907.07386. https://arxiv.org/abs/1907.07386 .
