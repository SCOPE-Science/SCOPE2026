# Sharp frame bounds for two-sided exponential Gabor systems at every integer oversampling

## Finding

For each real \(a>0\), integer \(q\ge2\), and two-sided exponential window \(g_a(t)=e^{-a|t|}\), consider the rectangular Gabor family
\[
\mathcal G_{a,q}=\{M_{\ell/q}T_k g_a:k,\ell\in\mathbb Z\},\qquad (M_\nu f)(t)=e^{2\pi i\nu t}f(t),\quad (T_k f)(t)=f(t-k).
\]
With \(r=e^{-a}\) and \(H_q=\sum_{j=0}^{q-1}r^{2j}\), the sharp constants in
\[
A_q(a)\|f\|_2^2\le\sum_{k,\ell\in\mathbb Z}|\langle f,M_{\ell/q}T_k g_a\rangle|^2\le B_q(a)\|f\|_2^2
\]
for every \(f\in L^2(\mathbb R)\) are exactly
\[
\boxed{A_q(a)=\frac{2q(rH_q-qr^q)}{(1+r^q)^2},\qquad B_q(a)=\frac{q((1+r^2)H_q+2qr^q)}{(1-r^q)^2}.}
\]
The lower bound is positive. The sharp Zak multiplier achieves its minimum at \(x=1/2\) and \(q\omega\equiv1/2\pmod1\), and its maximum at \(x\equiv0\pmod1\) and \(q\omega\equiv0\pmod1\). At fixed \(a\), the sharp condition number approaches \(\cosh a\) as integer oversampling \(q\to\infty\).

## Assumptions and scope

Here \(a>0\) is arbitrary, \(q\in\{2,3,\ldots\}\), the translation spacing is one, the modulation spacing is \(1/q\), and the window is not normalized by its \(L^2\)-norm. We use the Zak convention
\[
Zg(x,\omega)=\sum_{n\in\mathbb Z}g(x+n)e^{-2\pi i n\omega}.
\]
At this integer redundancy the Gabor frame operator is diagonalized by the Zak transform, with scalar multiplier
\[
\Phi_q(x,\omega)=\sum_{s=0}^{q-1}|Zg_a(x,\omega+s/q)|^2,
\]
whose essential infimum and supremum are the optimal bounds (the standard integer-oversampling Zak frame identity). The multiplier is continuous on the Zak fundamental cell, including its identified boundary points up to quasi-periodicity.

## Proof

Put \(r=e^{-a}\in(0,1)\), \(t=r^q\), \(v=e^{-2\pi i q\omega}\), and \(y=|1-tv|^2=1+t^2-2t\cos(2\pi q\omega)\). For \(0\le x\le1\), split the Zak series into residue classes modulo \(q\). Root-of-unity orthogonality gives
\[
\Phi_q(x,\omega)=q\sum_{m=0}^{q-1}|C_m(x,\omega)|^2,
\]
where, with \(z=e^{-2\pi i\omega}\), \(p_m=r^{x+m}\), \(n_m=r^{q-m-x}\), and \(p_mn_m=t\), each polyphase sum has the exact convergent form
\[
C_m=z^m\left(\frac{p_m}{1-tv}+\frac{n_m}{v-t}\right)
=z^m\frac{(p_m-tn_m)v+(n_m-tp_m)}{(1-tv)(v-t)}.
\]
(The split comprises the nonnegative indices \(m+qj\), \(j\ge0\), and negative indices \(m+qj\), \(j\le-1\).) Define
\[
U(x)=\sum_{m=0}^{q-1}(p_m^2+n_m^2)=H_q\bigl(r^{2x}+r^{2-2x}\bigr).
\]
Expanding the squared numerator, summing over \(m\), and using \(p_mn_m=t\) yields the **exact rational Zak multiplier**
\[
\Phi_q(x,\omega)=q\left(\frac{U(x)-q(1+t^2)}{y}+\frac{q(1-t^2)^2}{y^2}\right),
\quad (1-t)^2\le y\le(1+t)^2.
\]
For each fixed \(y\), this expression increases strictly with \(U\). The symmetric function \(U(x)=H_q(r^{2x}+r^{2-2x})\) is strictly convex, with its unique minimum \(U(1/2)=2rH_q\) and maximum \(U(0)=U(1)=(1+r^2)H_q\) on \([0,1]\).

For any \(x\), arithmetic–geometric mean gives \(U(x)=\sum_m(p_m^2+n_m^2)\ge2qt\). Consequently
\[
U-q(1+t^2)\ge-q(1-t)^2.
\]
Differentiate the rational multiplier with respect to \(y\):
\[
\frac{\partial\Phi_q}{\partial y}=-\frac{q}{y^3}\Bigl([U-q(1+t^2)]y+2q(1-t^2)^2\Bigr).
\]
The term in parentheses satisfies
\[
[U-q(1+t^2)]y+2q(1-t^2)^2\ge-q(1-t)^2(1+t)^2+2q(1-t^2)^2=q(1-t^2)^2>0.
\]
Thus \(\Phi_q\) **strictly decreases with \(y\)** throughout the full parameter range. It is therefore minimized at \(U=2rH_q\) and \(y=(1+t)^2\), and maximized at \(U=(1+r^2)H_q\) and \(y=(1-t)^2\). Substitution yields respectively
\[
\min\Phi_q=\frac{2q(rH_q-qt)}{(1+t)^2},\qquad
\max\Phi_q=\frac{q((1+r^2)H_q+2qt)}{(1-t)^2},
\]
which are the asserted **optimal** bounds and precisely specify all extremal coordinate classes.

To see that the lower bound is positive, write \(rH_q=\sum_{m=0}^{q-1}r^{2m+1}\). Its \(q\) summands have geometric mean \(r^q\), and they are not all equal for \(q\ge2\). Strict arithmetic–geometric mean gives \(rH_q>qr^q\).

Finally, when \(a>0\) is fixed and \(q\to\infty\), \(r^q\to0\), \(qr^q\to0\), and \(H_q\to(1-r^2)^{-1}\). Hence
\[
\lim_{q\to\infty}\frac{A_q(a)}q=\frac{2r}{1-r^2},\qquad
\lim_{q\to\infty}\frac{B_q(a)}q=\frac{1+r^2}{1-r^2},\qquad
\lim_{q\to\infty}\frac{B_q(a)}{A_q(a)}=\frac{1+r^2}{2r}=\cosh a.
\]
This completes the proof.

## Verification

`CHECK.py` performs independent truncated Zak-series evaluations (not using the polyphase rational identity), compares the resulting fiber multipliers with the proposed formulas at the extrema and at interior coordinates for several decay rates and redundancy integers, checks sample-grid inequalities, and confirms convergence of the condition number to \(\cosh a\). These finite tests corroborate rather than replace the proof for all real \(a>0\) and all integer \(q\ge2\). Run `python CHECK.py` with Python 3 and no third-party dependencies.

## Relationship to prior work

De Dios Pont, Gröchenig, Liehr, Shafkulovska, and Taylor (2026, arXiv:2608.04992v1) prove that every continuous integrable totally positive window gives a Gabor frame precisely below critical lattice area; their result covers *frame existence* for the present two-sided exponential but does not give the specific sharp constants above. Kloos and Stöckler (2013, arXiv:1311.7359v1, Section 5 and Theorem 5.6) give explicit **valid lower frame bounds** for symmetric exponentials over a wider range of lattices, but do not state the sharp integer-oversampling formulas in this manuscript. The Zak-transform characterization of optimal constants at integer redundancy is classical and is used as a known starting point, not presented as new.

A.J.E.M. Janssen's 1996 paper on Weyl–Heisenberg frame-bound calculations is directly relevant by its abstract, which describes exact calculations for several windows at integer oversampling. Its complete text could not be inspected here, and it is not known from the accessible abstract whether its examples include the specific sharp formulas above. **This is a material residual publication-priority risk**, and the present note does not claim certified precedence over that paper or any unavailable source.

## Limitations

The result is restricted to the symmetric two-sided exponential, unit translation spacing, and integer oversampling \(q\ge2\). The exact sharp constants do not by themselves give new qualitative frame-set coverage: existence is already known. No claims are made for arbitrary rational/irrational lattice areas, other windows, sampling noise, or finite-sample performance. The originality comparison is limited by the inaccessible 1996 source, and independent validation has not been performed.

## References

1. J. de Dios Pont, K. Gröchenig, L. Liehr, I. Shafkulovska, M. A. Taylor, *Gabor Frames of Totally Positive Functions: A Complete Characterization*, arXiv:2608.04992v1 (first public August 5, 2026), https://arxiv.org/abs/2608.04992 .
2. T. Kloos, J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359v1 (2013), https://arxiv.org/abs/1311.7359 .
3. A.J.E.M. Janssen, *Some Weyl-Heisenberg frame bound calculations*, Indagationes Mathematicae 7 (1996), 165–183, DOI:10.1016/0019-3577(96)85088-9.
