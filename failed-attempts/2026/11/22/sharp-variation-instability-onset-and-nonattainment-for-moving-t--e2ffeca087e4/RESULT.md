# Sharp variation-instability onset and nonattainment for moving three-sample standard deviation

## Finding
For each integer \(n\ge3\), let \(S_n:\mathbb R^n\to\mathbb R^{n-2}\) map each input to its **population** standard deviations over successive contiguous triples. With the discrete path-variation seminorm \(V_m(z)=\sum_{i=1}^{m-1}|z_{i+1}-z_i|\), its sharp two-input sensitivity is
\[
K_n=\sup_{V_n(x-y)>0}\frac{V_{n-2}(S_nx-S_ny)}{V_n(x-y)}=
\begin{cases}
0,&n=3,\\
1/\sqrt2,&n=4,\\
5\sqrt2/6,&n=5,\\
\sqrt2,&n\ge6.
\end{cases}
\]
Thus instability begins at five samples, and full dimension-independent amplification begins at six. For every \(n\ge4\), the positive sharp coefficient is **not attained** by any finite pair of distinct input signals; an explicit one-step perturbation family approaches it. The nonattainment is part of the claim, not a numerical assertion.

## Assumptions and scope
Inputs are arbitrary real vectors and windows are the \(n-2\) **full**, non-wrapping, consecutive triples. For a triple \((a,b,c)\), population standard deviation means \(\sqrt{((a-m)^2+(b-m)^2+(c-m)^2)/3}\), where \(m=(a+b+c)/3\); do not replace the denominator by two. Output variation is taken only along its \(n-2\) window centers. Both numerator and denominator are total variations of **differences between two signals**, not differences of their separate variation magnitudes. Constant inputs cause no ambiguity because the map is translation-invariant. For \(n=3\), output variation is zero by convention.

## Proof
Write \(d_i=x_{i+1}-x_i\) for \(1\le i<n\). Then \(V_n(x)=\|d\|_1\), and direct expansion of the triple variance gives
\[
(S_nx)_i=c_0F(d_i,d_{i+1}),\quad c_0=\sqrt2/3,\quad F(a,b)=\sqrt{a^2+ab+b^2},\quad 1\le i\le n-2.
\]
Every difference vector occurs from an input, so the desired norm is exactly the Lipschitz norm of \(d\mapsto c_0(F(d_i,d_{i+1}))_i\) from \(\ell_1^{n-1}\) to the path-variation seminorm on \(\mathbb R^{n-2}\).

At any point where all relevant pairs are nonzero, differentiate in one difference coordinate \(d_j\). Its only possibly nonzero output derivatives are two adjacent values \(c_0a,c_0b\), where
\[
a=\frac{d_{j-1}+2d_j}{2F(d_{j-1},d_j)},\qquad b=\frac{2d_j+d_{j+1}}{2F(d_j,d_{j+1})}.
\]
A missing window at either boundary is omitted. At interior indices, the path-variation norm of this derivative column is
\[c_0(|a|+|b-a|+|b|).\]
If one of the three adjacent output-variation edges is missing, its corresponding term is simply omitted. If \(d_j>0\), direct squaring, with sign checking, proves \(-1/2<a\le1\) and \(-1/2<b\le1\); if \(d_j<0\), their negatives lie in the same interval. Indeed \(|u+2v|\le2F(u,v)\) follows from \(4F(u,v)^2-(u+2v)^2=3u^2\), and for \(v>0\) the case \(u+2v<0\) satisfies \(|u+2v|<F(u,v)\), since \(F(u,v)^2-(u+2v)^2=-3v(u+v)>0\). At \(d_j=0\), when the derivatives exist they have magnitudes at most \(1/2\). Thus \(|a-b|\le3/2\), and the sharp upper bounds on complete, two-edge, and one-edge derivative columns are respectively \(3c_0\), \(5c_0/2\), and \(3c_0/2\), with outer isolated columns bounded by \(c_0\). Specifically, \(n=4\) has only a two-center difference, giving at most \(3c_0/2\); \(n=5\) has a three-center output and at most \(5c_0/2\); and \(n\ge6\) contains a full three-edge column, giving at most \(3c_0\). For \(n=3\) there is no output edge. Piecewise differentiation along any line segment and integration of the derivative extend each upper bound to all input pairs, including those crossing nonsmooth pairs.

For sharpness, take a difference baseline with one selected coordinate \(d_j=1\), vary only \(d_j\) by an infinitesimal positive amount, and arrange the two neighboring differences as follows. If \(n=4\), take \(j=2\), \(d_{j-1}=0\), \(d_{j+1}=-R\). If \(n=5\), take \(j=2\), \(d_{j-1}=-R\), \(d_{j+1}=0\). If \(n\ge6\), take \(j=3\), \(d_{j-1}=0\), \(d_{j+1}=-R\), with the remaining differences any fixed nonzero values. For \(R\to\infty\), the two derivatives tend to the extremal pair \((1,-1/2)\) or \((-1/2,1)\), and the induced output variation tends respectively to \(3c_0/2\), \(5c_0/2\), or \(3c_0\). Choose the positive increment after choosing a sufficiently large finite \(R\) to obtain real finite input pairs arbitrarily close to the bound.

Finally, equality at any positive sharp bound would require the derivative column to attain both \(1\) and \(-1/2\) with the same nonzero \(d_j\), because the listed column sums are strictly smaller otherwise. The value \(-1/2\) is only a limit as a neighboring difference diverges, never a finite differentiable value; at \(d_j=0\), derivatives cannot achieve the needed endpoint \(1\). Hence the Jacobian norm is strictly below the relevant sharp constant at every differentiability point. Along a finite segment the output is absolutely continuous and differentiable almost everywhere, so integration makes every nontrivial two-input ratio strictly smaller. This proves nonattainment for \(n\ge4\).

## Verification
Execute \(\texttt{python3 checker.py}\) from the extracted package. It verifies the finite column formulas and exact candidate constants numerically against 6,000 reproducible randomly selected input pairs, and approaches each sharp bound using a controlled large-neighbor contrast. These checks support, but do not establish, the all-dimensional analytical proof.

## Relationship to prior work
Local mean and variance processing was developed by Lee (1980), while Herbert et al. (2016) study high-speed windowed standard-deviation evaluation for time-series data. Neither source's inspected mathematical content establishes a two-input path-variation perturbation coefficient or its boundary-size and nonattainment structure. Existing indexed two-input variation results for moving medians and window extrema concern different nonsmooth scalar order-statistic operators. The present operator is the Euclidean norm of two coupled first differences; the finite-length transition depends on the derivative-column overlap of consecutive variance windows.

## Limitations
This is a sharp Lipschitz **supremum**, not an attained maximum, for \(n\ge4\). It does not cover unbiased sample standard deviation, cyclic windows, boundary-padded windows, longer window sizes, multidimensional images, or local variance without the square root. No statistical performance or denoising claim follows directly. Historical novelty cannot be certified by a finite search of the literature.

## References
1. J.-S. Lee, *Digital Image Enhancement and Noise Filtering by Use of Local Statistics*, IEEE Transactions on Pattern Analysis and Machine Intelligence **PAMI-2** (1980), 165–168. DOI: https://doi.org/10.1109/TPAMI.1980.4766994 . Full available text: https://www.sci.utah.edu/~gerig/CS7960-S2010/materials/Perona-Malik/Lee%20filter%20Digital%20image%20enhancement%20and%20noise%20filtering%20by%20using%20local%20statistics.pdf .
2. J. Herbert, S. Wilson, A. D. Rakic and T. Taimre, *FPGA implementation of a high-speed, real-time, windowed standard deviation filter*, Electronics Letters **52** (2016), 22–23. DOI: https://doi.org/10.1049/el.2015.2407 .
