# Sharp cut-boundary amplification of local cyclic averages

## Finding

Let \(n\ge2\), let \(S:\mathbb R^n\to\mathbb R^n\) be the cyclic forward shift \((Sx)_i=x_{(i+1)\bmod n}\) for \(0\le i<n\), and measure *open-path* total variation by
\[
V_n(x)=\sum_{i=0}^{n-2}|x_{i+1}-x_i|.
\]
This seminorm differs from cycle variation because the closing edge is omitted. The following is one sharp cut-boundary stability theorem, with two consequences.

**Local-support mass law.** For any integers \(1\le m\le n/2\) and any probability vector \(p=(p_0,\ldots,p_{m-1})\), allowing zero entries, the cyclic convolution \(T_p=\sum_{s=0}^{m-1}p_sS^s\) satisfies
\[
\sup_{V_n(x)>0}\frac{V_n(T_px)}{V_n(x)}=2-p_0.
\]
The supremum is attained by the explicit one-jump signal \(x_i=\mathbf 1_{\{i<m\}}\); thus **all interior kernel weights cancel from the sharp value** whenever the original and wrapped jump zones can be separated.

**Complete uniform-window phase diagram.** For every \(n\ge2\) and \(1\le m\le n\), the ordinary cyclic length-\(m\) boxcar average \(B_{n,m}=m^{-1}\sum_{s=0}^{m-1}S^s\) has exact sharp norm
\[
C_{n,m}=\sup_{V_n(x)>0}\frac{V_n(B_{n,m}x)}{V_n(x)}=
\begin{cases}
2-1/m,&2m\le n,\\
2(n-m)/m,&2m>n.
\end{cases}
\]
For every \(m\), an explicit one-jump signal attains the norm. The boxcar average is open-path variation-nonexpansive **exactly** for \(m=1\) or \(m\ge\lceil 2n/3\rceil\). In particular, the first genuine two-tap amplification occurs at \(n=4\), where the sharp coefficient is \(3/2\), despite contraction of periodic variation.

**Transient reversal under repeated averaging.** Put \(A_n=(I+S)/2\). For every \(r\ge0\) with \(n\ge2r+2\),
\[
\sup_{V_n(x)>0}\frac{V_n(A_n^rx)}{V_n(x)}=2-2^{-r}.
\]
Thus the sharp coefficient grows strictly with each of the first \(\lfloor(n-2)/2\rfloor\) averaging steps, even though \(A_n^r\) converges to constant averaging and its variation operator norm tends to zero as \(r\to\infty\) for each fixed \(n\).

## Assumptions and scope

The signals and weights are real, the shift acts modulo \(n\), and the input/output metric is the adjacent-variation seminorm on the *path*, not cycle variation. The operator preserves constants, so it acts on the quotient by constant signals. All supremums are over inputs of nonzero path variation and equal sharp two-input Lipschitz coefficients by linearity. All formulas include \(m=1\), \(m=n\), and \(n=2\). The local-support formula assumes \(n\ge2m\); the uniform-window formula has no such restriction. The power formula assumes \(n\ge2r+2\) only for the stated initial-time equality, not for the separately asserted fixed-dimensional convergence.

## Proof

**Step reduction.** For each \(1\le k<n\), put \(h^{(k)}_i=1\) when \(0\le i<k\), and zero otherwise. Every real signal has the exact identity
\[
x=x_{n-1}\mathbf1+\sum_{k=1}^{n-1}(x_{k-1}-x_k)h^{(k)},
\qquad V_n(x)=\sum_{k=1}^{n-1}|x_{k-1}-x_k|.
\]
Any constant-preserving linear operator \(T\) therefore satisfies
\[
\|T\|_{V\to V}=\max_{1\le k<n}V_n(Th^{(k)}),
\]
with an actual step input attaining the maximum. This proves the necessary norm reduction, not merely a lower bound.

**Local-support upper bound and matching witness.** Let \(V_n^{\rm cyc}(x)=V_n(x)+|x_0-x_{n-1}|\). The triangle inequality gives \(V_n^{\rm cyc}(x)\le2V_n(x)\). For any nonzero cyclic shift, \(V_n(S^sx)\le V_n^{\rm cyc}(x)\le2V_n(x)\), whereas \(V_n(S^0x)=V_n(x)\). Convexity of the seminorm yields
\[
V_n(T_px)\le[p_0+2(1-p_0)]V_n(x)=(2-p_0)V_n(x).
\]
For the step \(h^{(m)}\), consider the adjacent differences of its images. The identity-shift term has a negative jump at edge \(m-1\). For each \(1\le s<m\), the shift creates a negative jump at edge \(m-s-1\) and a positive jump at edge \(n-s-1\). When \(n\ge2m\), all negative jumps lie in the disjoint range of edges \(0,\ldots,m-1\) and all positive jumps in \(n-m,\ldots,n-2\). There can be no cancellation of nonnegative shift weights. Their total absolute mass is \(\sum_{s=0}^{m-1}p_s+\sum_{s=1}^{m-1}p_s=2-p_0\). This simultaneously proves sharpness for every permitted probability vector, including degenerate ones.

**Uniform window at arbitrary widths.** Telescoping gives
\[
(B_{n,m}x)_{i+1}-(B_{n,m}x)_i=
\frac{x_{(i+m)\bmod n}-x_i}{m},\qquad 0\le i<n-1.
\]
For the circular step \(h^{(k)}\), the sets of starting indices on which the two terms differ have total size
\[
2\min\{k,n-k,m,n-m\}.
\]
Indeed, if \(A=\{0,\ldots,k-1\}\) and \(A-m\) is its translate modulo \(n\), then \( |A\cap(A-m)|=(k-m)_+ +(k-(n-m))_+\), where \(u_+=\max\{u,0\}\). Subtracting twice this overlap from \(2k\) gives precisely the displayed minimum, in each ordering of \(k,m,n-k,n-m\). Of the \(n\) possible cyclic adjacent positions, the excluded position \(i=n-1\) contributes exactly \(\mathbf1_{\{k\ge m\}}\), since \(h^{(k)}_{n-1}=0\) and \(h^{(k)}_{m-1}=1\) precisely in that case. Consequently the exact finite step response is
\[
V_n(B_{n,m}h^{(k)})=\frac{2\min\{k,n-k,m,n-m\}-\mathbf1_{\{k\ge m\}}}{m}.
\]
If \(2m\le n\), every response is at most \((2m-1)/m\): obtaining the full \(2m\) circular transitions forces \(k\ge m\), hence subtraction of one, while smaller values give at most \(2m-2\). The step \(k=m\) attains the upper bound. If \(2m>n\), every response is at most \(2(n-m)/m\), and \(k=n-m<m\) attains it with no excluded transition. Step reduction proves the complete formula, and elementary comparison with \(1\) proves the stated precise nonexpansivity criterion.

**Iterates and fixed-dimensional limit.** The binomial theorem gives
\[
A_n^r=2^{-r}\sum_{s=0}^r\binom rs S^s.
\]
If \(n\ge2r+2\), this is a positive convolution supported on \(r+1\) consecutive shifts. Its zero-shift mass equals \(2^{-r}\). The local-support theorem applies, yielding the exact, strictly increasing coefficient \(2-2^{-r}\). For fixed \(n\), the nonconstant Fourier eigenvalues of \(A_n\) are \((1+e^{2\pi i j/n})/2\), \(1\le j<n\), all of modulus strictly less than one. Hence \(A_n^r\to n^{-1}\mathbf1\mathbf1^\top\), and the induced norm on the finite-dimensional constant quotient converges to zero. No monotonicity at later steps is asserted.

## Verification

The accompanying standalone `verify.py` uses only exact rational arithmetic and Python's standard library. It independently constructs the cyclic convolution and measures the variation of every step signal. It checks every boxcar width for dimensions 2 through 30; 6,488 local-support probability cases including zero weights; all initial binomial powers through dimension 39; and 21,321 direct ternary signals. It also checks a finite long-time mixing sample. All checks passed. Finite checks do not replace the preceding infinite-family arguments.

Run with `python verify.py` from the extracted two-file scientific package. No external input, floating-point tolerance, private library or external certificate is required.

## Relationship to prior work

Nochetto and Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069, treat continuous finite-element interpolation using *different boundary-adjusted operators* on periodic and nonperiodic domains; Section 3 and Section 4 respectively prove variation contraction under their matched geometries. Carneiro, Finder and Sousa, *On the variation of maximal operators of convolution type II*, arXiv:1512.02715, prove continuous periodic variation-diminishing statements for convolution-type maximal operators. Neither identifies the operator norm obtained by retaining a *periodic averaging operator* while measuring output in the **open-path** variation that deletes exactly one closing edge. Published exact studies of Gini variation for cyclic boxcar averaging concern a distinct complete-pair seminorm, and the corresponding cyclic variation contraction does not control this open-path coefficient. The new formulas isolate the effect of the deliberately mismatched boundary convention.

## Limitations

The local-support universality law is not claimed when the support and its wrapped jump zones overlap. The complete arbitrary-width classification is confined to *uniform* consecutive shift weights. Arbitrary nonlocal cyclic probability laws can behave differently. The exact binomial formula is an initial-time statement under \(n\ge2r+2\); the later finite-dimensional coefficient is not classified. No priority claim is made relative to inaccessible or unindexed historical results; no independent review has been performed.

## References

1. R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, first posted 2012-11-05, https://arxiv.org/abs/1211.1069 (especially Sections 3–4).
2. E. Carneiro, R. Finder and M. Sousa, *On the variation of maximal operators of convolution type II*, first posted 2015-12-09, https://arxiv.org/abs/1512.02715 (especially Sections 1.1, 1.3, and 3).
