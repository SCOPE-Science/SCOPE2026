# Sharp bounded-variation cost of fourth-order Keys cubic convolution

## Finding

The classical **six-tap, fourth-order Keys cubic-convolution interpolant** has the following exact, attained discrete-to-continuous total-variation norm:

\[
\boxed{\sup_{V_d(y)>0}\frac{\operatorname{Var}_{\mathbb R}(I_4y)}{V_d(y)}
=\frac{1790+43\sqrt{43}}{1458}
=1.421104154008906\ldots.}
\]

Its sharp two-input Lipschitz coefficient in the corresponding variation seminorm is the same. The single-step data \(y_j={\bf 1}_{\{j\ge1\}}\) attain equality. For comparison, the four-tap, third-order Keys (Catmull--Rom/Karup--King) cubic-convolution interpolant has sharp coefficient \(35/27\); the exact excess due to the specified fourth-order kernel is

\[
\frac{43\sqrt{43}-100}{1458}=0.1248078577\ldots>0.
\]

This is a stability comparison of two **particular classical kernels**, not a minimax claim over all possible fourth-order interpolation schemes. The polynomial approximation orders and both interpolation kernels are earlier published facts; only the sharp variation analysis is asserted here.

## Assumptions and scope

For a real bi-infinite sequence \(y=(y_j)_{j\in\mathbb Z}\), set \(V_d(y)=\sum_{j\in\mathbb Z}|y_{j+1}-y_j|\). Assume \(V_d(y)<\infty\); such a sequence is bounded and has a left limit. Continuous total variation is \(\operatorname{Var}_{\mathbb R}(f)=\int_{\mathbb R}|f'(x)|\,dx\) for the continuously differentiable interpolants below.

Define the even compactly supported kernel \(\phi_4:\mathbb R\to\mathbb R\) using \(u=|x|\):

\[
\phi_4(x)=\begin{cases}
1-\frac73u^2+\frac43u^3,&0\le u\le1,\\
\frac52-\frac{59}{12}u+3u^2-\frac7{12}u^3,&1\le u\le2,\\
-\frac32+\frac74u-\frac23u^2+\frac1{12}u^3,&2\le u\le3,\\
0,&u\ge3.
\end{cases}
\]

Let \((I_4y)(x)=\sum_{j\in\mathbb Z}y_j\phi_4(x-j)\). At each \(x\), the sum has at most six nonzero terms. The kernel is \(C^1\), interpolatory at integers, has partition of unity \(\sum_{j\in\mathbb Z}\phi_4(x-j)=1\), and reproduces cubic polynomial data. The latter reproduction property is not needed in the norm proof but motivates comparison with the order-three scheme.

The four-tap comparison operator \(I_3\) uses the even kernel

\[
\phi_3(x)=\begin{cases}
1-\frac52u^2+\frac32u^3,&0\le u\le1,\\
2-4u+\frac52u^2-\frac12u^3,&1\le u\le2,\\
0,&u\ge2.
\end{cases}
\]

All knots are the uniform integer grid; no boundary extrapolation, finite-interval end rule, or higher-dimensional tensor-product variation is covered.

## Proof

**Step decomposition and sharpness reduction.** Write \(d_k=y_{k+1}-y_k\) and \(\ell=\lim_{j\to-\infty}y_j\). Absolute convergence yields
\(y_j=\ell+\sum_{k<j}d_k\). Since \(\phi_4\) reproduces constants, for the unit-step response \(S(x)=\sum_{j\ge1}\phi_4(x-j)\),

\[
(I_4y)(x)=\ell+\sum_{k\in\mathbb Z}d_kS(x-k).
\]

The derivative \(S'\) is compactly supported and integrable. Termwise differentiation in \(L^1\), or a limit of finite sums, gives

\[
\operatorname{Var}_{\mathbb R}(I_4y)\le\sum_k|d_k|\,\|S'\|_{L^1}=V_d(y)\operatorname{Var}_{\mathbb R}(S).
\]

For the single-step data, \(V_d(y)=1\) and \(I_4y=S\); thus the inequality is sharp, without an appeal to a finite experiment. Linearity proves the identical two-input seminorm bound by applying it to \(y-z\).

**Five exact cubic pieces.** The compact support implies \(S=0\) on \(( -\infty,-2]\) and \(S=1\) on \([3,\infty)\). Direct substitution of the published kernel on its three radial intervals gives, with \(0\le t\le1\),

\[
\begin{aligned}
S(-2+t)&=\frac{t^2(1-t)}{12},\\
S(-1+t)&=\frac{t(t-1)(6t+1)}{12},\\
S(t)&=\frac{t(7+15t-10t^2)}{12}.
\end{aligned}
\]

Evenness of \(\phi_4\) and its partition of unity show \(S(1-x)=1-S(x)\), determining the pieces on \([1,2]\) and \([2,3]\) and giving equal variations on paired cells.

On \([-2,-1]\), the first displayed cubic is nonnegative with zero endpoints and a unique maximum \(1/81\) at \(t=2/3\). Its variation is \(2/81\). On \([-1,0]\), the second cubic is nonpositive with zero endpoints and a unique minimum at

\[
r_* =\frac{5+\sqrt{43}}{18},\qquad
S(-1+r_*)=-\frac{260+43\sqrt{43}}{5832}=-A.
\]

Its variation is \(2A\). The central derivative satisfies

\[
\frac d{dt}S(t)=\frac{7+30t-30t^2}{12}>0\quad(0\le t\le1),
\]

so central variation equals one. By symmetry, the remaining two cells contribute \(2A\) and \(2/81\). Therefore

\[
\begin{aligned}
\operatorname{Var}_{\mathbb R}(S)&=\frac4{81}+4A+1\\
&=1+\frac4{81}+\frac{260+43\sqrt{43}}{1458}\\
&=\frac{1790+43\sqrt{43}}{1458}.
\end{aligned}
\]

**The four-tap comparator.** For \(\phi_3\), the centered-Hermite representation uses endpoint derivatives \((y_{j+1}-y_{j-1})/2\). Its response to a unit step has two symmetric outer cubic lobes, each of height \(2/27\), and a monotone central cell of variation one. Each outer cell traverses a lobe and returns to its endpoint value, contributing \(4/27\). Hence \(\operatorname{Var}(I_3y)\le(1+8/27)V_d(y)=(35/27)V_d(y)\), sharply for a step. Subtracting gives exactly \((43\sqrt{43}-100)/1458>0\), since \(43\sqrt{43}>100\).

## Verification

The accompanying `checker.py` reconstructs all five response-cell polynomials directly from the three pieces of \(\phi_4\), verifies partition of unity and reflection symmetry, differentiates the cubics, checks the two nontrivial stationary values and radical identity exactly with SymPy, and corroborates the variation bound on 125 pseudorandom finite-jump sequences by numerical quadrature. Execute `python checker.py` with Python 3 and SymPy installed. The numerical stress test is not an infinite-domain proof; the preceding step-decomposition argument is.

## Relationship to prior work

Keys (1981) defines the four-tap third-order and six-tap fourth-order cubic kernels and their accuracy properties. Meijering and Unser (2003) establish their equivalence to older Karup--King and Henderson osculatory formulas, respectively: no new interpolation method or historical priority for these kernels is claimed. Malgouyres and Guichard (2001) analyze linear image zooming, direction preservation and total-variation-based nonlinear restoration. That material does not give an exact one-dimensional discrete-BV to continuous-BV operator norm for the six-tap Keys kernel. Previously recorded results on the global cardinal cubic spline interpolant and local nonlinear cubic Hermite slope selectors apply to different interpolation operators. The decisive novelty question is the exact sharp radical for this particular fourth-order six-tap operator, with its attained step extremizer and comparison to the four-tap operator.

## Limitations

The exact conclusion applies only to the classical even support-three Keys kernel, not every order-four cubic, parametric reconstruction, nonuniform knot scheme or a two-dimensional image-TV norm. Old literature on 1D oscillatory interpolation might contain an equivalent radical under other terminology; the accessible records and full-text sections inspected did not identify one. The 1981 origin is documented to month precision; the independently day-verified publicly released archival lead used for chronological metadata is Malgouyres--Guichard's electronic publication of 2001-02-21, not an assertion that the kernel originated then.

## References

1. R. G. Keys, *Cubic Convolution Interpolation for Digital Image Processing*, IEEE Trans. Acoustics, Speech, Signal Processing 29 (1981), 1153--1160, DOI: https://doi.org/10.1109/TASSP.1981.1163711. Lawful public reading copy: https://ncorr.com/download/publications/keysbicubic.pdf. Kernel definition and fourth-order construction on pp. 1154 and 1160.
2. E. Meijering and M. Unser, *A Note on Cubic Convolution Interpolation*, IEEE Trans. Image Processing 12 (2003), 477--479, DOI: https://doi.org/10.1109/TIP.2003.811493. Accessible author preprint: https://bigwww.epfl.ch/preprints/meijering0301p.pdf.
3. F. Malgouyres and F. Guichard, *Edge Direction Preserving Image Zooming: A Mathematical and Numerical Analysis*, SIAM J. Numer. Anal. 39 (2001), 1--37, DOI: https://doi.org/10.1137/S0036142999362286. Electronically published 2001-02-21, per first-page colophon. Full text: https://www.math.univ-toulouse.fr/~fmalgouy/download/CMLA9930.pdf.
