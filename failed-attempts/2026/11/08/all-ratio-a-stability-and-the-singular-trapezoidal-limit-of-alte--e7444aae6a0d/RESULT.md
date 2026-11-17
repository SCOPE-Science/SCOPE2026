# All-ratio A-stability and the singular trapezoidal limit of alternating-step BDF2

## Finding

For the standard variable-step, quadratic-interpolation BDF2 formula on the scalar test equation \(y'=\lambda y\), fix any two positive step lengths \(a,b\) repeated periodically. For every \(\lambda\in\mathbb C\) with \(\operatorname{Re}\lambda\le0\) and \(\lambda\ne0\), the two-step monodromy has **both** characteristic multipliers strictly inside the unit disk, without any restriction on the ratio \(a/b\). Consequently every initial pair of data tends to zero geometrically over periods. At \(\lambda=0\), its multipliers are \(1\) (simple) and \(r/[(2r+1)(r+2)]\), where \(r=a/b>0\).

There is nevertheless a nonuniform stiff-decay effect. With real \(\lambda=-\gamma\), \(\gamma>0\), define the total-period decay parameter \(q=\gamma(a+b)>0\) and the monodromy spectral radius \(\rho(r,q)\). The two limiting multipliers, as \(r\to\infty\) at fixed \(q\), are
\[
\left\{\frac{2-q}{2+q},\;0\right\}.
\]
For every finite fixed \(r>0\), \(\rho(r,q)\to0\) as \(q\to\infty\), whereas
\[
\lim_{q\to\infty}\lim_{r\to\infty}\rho(r,q)=1,
\qquad
\lim_{r\to\infty}\lim_{q\to\infty}\rho(r,q)=0.
\]
Thus arbitrary alternating step ratios preserve the entire closed left-half-plane absolute-stability property, but in an extreme-ratio limit the period map acquires precisely the trapezoidal-rule (Crank--Nicolson) multiplier and loses uniform stiff damping.

## Assumptions and scope

Let \(h_n=t_n-t_{n-1}>0\) be periodic with alternating lengths \(a,b\), let \(s_n=h_n/h_{n-1}>0\), and consider the **standard fully variable-coefficient BDF2** scheme obtained by differentiating the quadratic interpolant through the three newest nodes:
\[
(1+2s_n)y_n-(1+s_n)^2y_{n-1}+s_n^2 y_{n-2}
=h_n(1+s_n)\lambda y_n.
\]
For arbitrary complex starting values \(y_0,y_1\), the associated one-step companion matrices multiply to a fixed two-period matrix after two updates. The theorem concerns its characteristic multipliers (Floquet multipliers), not a uniform one-step Euclidean contraction estimate and not arbitrary/nonperiodic grids. There is no bound imposed on \(a\), \(b\), or \(r=a/b\). The asymptotic statements with \(q\) use real decay \(\lambda=-\gamma<0\); the absolute-stability result allows complex \(\lambda\).

## Proof

Put \(r=a/b>0\), \(z=-\lambda b\), so \(x=\operatorname{Re}z\ge0\) for the closed left-half-plane and \(u=|z|^2\). In the order of an \(a\)-step followed by a \(b\)-step, the companion matrices are
\[
T_a=\begin{pmatrix}
\dfrac{(1+r)^2}{D}&-\dfrac{r^2}{D}\\[3pt]1&0
\end{pmatrix},\quad
T_b=\begin{pmatrix}
\dfrac{(1+r)^2}{r E}&-\dfrac1{r E}\\[3pt]1&0
\end{pmatrix},
\]
where
\[
D=1+2r+r(r+1)z,\qquad E=r+2+(r+1)z.
\]
The monodromy \(M=T_bT_a\) has
\[
\operatorname{tr}M=\frac{P}{W},\qquad\det M=\frac rW,
\quad W=DE,\quad
P=2(r^2+3r+1)-(r+1)(r^2+1)z.
\]
Thus its full characteristic equation, for every \(r>0\), is
\[
W\mu^2-P\mu+r=0.\tag{1}
\]

For \(x\ge0\), the two factors satisfy \(|D|\ge1+2r\) and \(|E|\ge r+2\), whence \(|W|>r\). The strict Schur--Cohn criterion for the roots of (1) to lie in the unit disk is therefore reduced to
\[
|P\overline W-r\overline P|<|W|^2-r^2.\tag{2}
\]
A direct expansion gives the *exact global identity*
\[
(|W|^2-r^2)^2-|P\overline W-r\overline P|^2
=(r+1)^4 A B,\tag{3}
\]
where
\[
\begin{aligned}
A={}&r(r+1)^2u^2+2(r+1)(r^2+4r+1)ux\\
&+4(2r+1)(r+2)x^2+8(r+1)x,\\[3pt]
B={}&r^2 A+(r+1)^2\bigl[12r(r+1)x\\
&\hspace{21mm}+r(r^2+6r+1)u+4(r^2+3r+1)\bigr].
\end{aligned}
\]
If \(z\ne0\), then \(u>0\), so \(A>0\) for all \(r>0\) and \(x\ge0\), and visibly \(B>0\). In (3), positivity of the right side and \(|W|^2-r^2>0\) establish (2) strictly. Both monodromy roots therefore lie strictly inside the unit circle, including for nonzero purely imaginary \(\lambda\). If \(z=0\), (1) factors into \((\mu-1)(((2r+1)(r+2))\mu-r)=0\), and the second root lies strictly inside the unit disk. This proves the all-ratio A-stability assertion and the precise neutral boundary case.

For the singular-ratio limit, set \(\lambda=-\gamma<0\), \(q=\gamma(a+b)>0\), and \(z=q/(1+r)\). From the explicit expressions,
\[
\frac{P}{W}\longrightarrow\frac{2-q}{2+q},\qquad
\frac rW\longrightarrow0\qquad(r\to\infty).
\]
The limiting roots of the monic characteristic polynomial are therefore \((2-q)/(2+q)\) and \(0\), with multiplicity understood at \(q=2\). At fixed finite \(r\), the same formulas show \(P/W=O(q^{-1})\) and \(r/W=O(q^{-2})\), so both roots converge to zero as \(q\to\infty\). Finally the limit of the trapezoidal multiplier's modulus is one as \(q\to\infty\), proving the two different iterated limits. Each step update is well defined throughout since \(D,E\ne0\) in the stated region.

## Verification

The standalone `checker.py` uses the directly defined BDF2 companion matrices to reconstruct the trace and determinant independently at 42 exact parameter pairs (84 assertions), verifies identity (3) as a polynomial in \(r,x,y\), verifies the exact neutral factorization and four symbolic limiting statements, and performs 25 numerical sanity checks of complex characteristic roots: 115 assertions in total. Run `python checker.py` with SymPy available; the recorded output is `checker_output.txt`. The infinite-domain proof is (1)--(3) and the manifestly positive factors, not any finite set of sample computations.

For example, with \(q=6\), equal steps \(r=1\) yield spectral radius \(1/9\). At \(r=100\), equation (1) is exactly \(86508\mu^2+39404\mu+100=0\), yielding spectral radius approximately \(0.45294333\); it approaches \(1/2\) as \(r\to\infty\).

## Relationship to prior work

Classical constant-step BDF2 is A-stable. Wang, Mao, and Wang (2020) analyze variable-step BDF2 for parabolic equations under step-ratio restrictions. Li and Liao (2022) prove arbitrary-grid perturbed stability in a small-maximum-step regime; this does not establish unrestricted absolute stability on a fixed alternating grid for all scalar decay parameters. Dahlquist, Liniger, and Nevanlinna (1983) highlight variable-step difficulties for BDF and construct a different variable-step one-leg method stable for general dissipative problems. Their general variable-coefficient counterexamples do not contradict the constant-coefficient two-periodic theorem proved here. The asserted contribution is the **exact unrestricted two-periodic BDF2 half-plane result coupled with its singular trapezoidal stiff limit**, not the classical BDF2 formula, generic periodic recurrence theory, or small-step stability.

## Limitations

No claim is made for nonperiodic sequences, arbitrary time-dependent \(\lambda(t)\), nonlinear dissipative dynamics, noncommuting matrix-valued coefficient sequences, finite-time transient norm control independent of the step ratio, or energy/positivity preservation. The half-plane result concerns the asymptotic spectral radius of the two-step companion map; individual updates need not contract every norm. Its singular-limit statement does not imply an unstable finite-ratio case: all finite positive ratios remain strictly stable for nonzero \(\operatorname{Re}\lambda\le0\).

## References

- W. Wang, M. Mao, and Z. Wang, *Stability and error estimates for the variable step-size BDF2 method for linear and semilinear parabolic equations*, first public preprint March 7, 2020, https://arxiv.org/abs/2003.03534.
- Z. Li and H.-l. Liao, *Stability of variable-step BDF2 and BDF3 methods*, first public preprint January 3, 2022, https://arxiv.org/abs/2201.00527.
- H.-l. Liao, B. Ji, L. Wang, and Z. Zhang, *Mesh-robustness of an energy stable BDF2 scheme with variable steps for the Cahn--Hilliard model*, first public preprint February 7, 2021, https://arxiv.org/abs/2102.03731.
- G. G. Dahlquist, W. Liniger, and O. Nevanlinna, *Stability of two-step methods for variable integration steps*, SIAM J. Numer. Anal. 20 (1983), 1071--1085, https://doi.org/10.1137/0720076.
