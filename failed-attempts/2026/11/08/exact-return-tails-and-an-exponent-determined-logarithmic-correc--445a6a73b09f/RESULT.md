# Exact return tails and an exponent-determined logarithmic correction for a doubly intermittent map

## Finding

For every \(0<\ell<1\), the symmetric two-branch full-branch map
\[
T_\ell(x)=\begin{cases}
x+(1+x)^{1+\ell},&-1\le x<0,\\
x-(1-x)^{1+\ell},&0\le x\le1
\end{cases}
\]
has an exactly computable first-return survival law on its natural central crossing set. Let \(c_\ell\in(0,1)\) be the unique solution of \(c_\ell=(1-c_\ell)^{1+\ell}\), put \(H_\ell=(-c_\ell,0)\cup(0,c_\ell)\), and let \(r(x)=\min\{n\ge1:T_\ell^n(x)\in H_\ell\}\). Initial points are distributed by normalized Lebesgue measure on \(H_\ell\). Set \(Q_\ell(n)=\Pr(r>n)\).

Define the increasing maps \(\phi_\ell(z)=z+z^{1+\ell}\) and \(g_\ell(x)=1+x-(1-x)^{1+\ell}\), and the inverse sequence \(\delta_0=1-c_\ell\), \(\phi_\ell(\delta_j)=\delta_{j-1}\) for \(j\ge1\). Then, **for every integer \(n\ge1\)**,
\[
\boxed{Q_\ell(n)=\frac{g_\ell^{-1}(\delta_{n-1})}{c_\ell}.}
\]
Here \(g_\ell^{-1}\) is the inverse of \(g_\ell:(0,c_\ell)\to(0,1)\). In particular, the tail is not merely comparable to a power law: it has the following three-term asymptotic with a nonzero logarithmic correction:
\[
\boxed{Q_\ell(n)=C_\ell n^{-1/\ell}\left[1+B_\ell\frac{\log n}{n}+D_\ell\frac1n+O_\ell\!\left(\frac{(\log n)^2}{n^2}+n^{-1/\ell}\right)\right],}
\]
where
\[
C_\ell=\frac{\ell^{-1/\ell}}{(2+\ell)c_\ell},\qquad
B_\ell=\frac{1+\ell}{2\ell^2},\qquad
D_\ell=\frac{\ell-K_\ell}{\ell^2},
\]
and the well-defined, finite constant \(K_\ell\) is specified by the convergent parabolic-orbit limit
\[
K_\ell=\lim_{m\to\infty}\left[\delta_m^{-\ell}-\ell m+\frac{1+\ell}{2}\log m\right].
\]
In particular, for \(\ell=1/2\), one has
\[
Q_{1/2}(n)=\frac{8}{5c_{1/2}}n^{-2}+\frac{24}{5c_{1/2}}\frac{\log n}{n^3}+O(n^{-3}).
\]

## Assumptions and scope

The map is defined on \([-1,1]\) with the indicated branch convention at \(x=0\). Endpoint/branch-boundary ambiguities are null sets for the conditional Lebesgue law. The exponent range is \(0<\ell<1\); all asymptotic constants and remainders may depend on a fixed \(\ell\), and **no uniformity is asserted as \(\ell\to0\) or \(\ell\to1\)**. The return time is to the **union** of the two open central branches and not to a single-sided inducing interval; probabilities refer to normalized *Lebesgue* measure, not to the invariant density of the induced map. The source family belongs to the one-dimensional full-branch interval-dynamics classification \(37E05\).

The equation for \(c_\ell\) has exactly one root in \((0,1)\), because its left-hand side is strictly increasing while the right-hand side is strictly decreasing. Since \((1-c_\ell)^{1+\ell}=c_\ell\), the neutral-endpoint increment obeys \(\phi_\ell(1-c_\ell)=1\).

## Proof

**1. Exact first-exit partition.** The map is odd away from the branch origin and each side maps monotonically onto the full interior. For \(x\in(0,c_\ell)\), the first image lies in \((-1,0)\); writing it as \(-1+z\) gives \(z=g_\ell(x)\). While an excursion remains outside \(H_\ell\) on the negative side, \(z\) evolves by \(z\mapsto\phi_\ell(z)\). Because \(\phi_\ell(1-c_\ell)=1\), an excursion cannot jump from \([-1,-c_\ell]\) across the open central set. Thus, up to endpoint equalities of zero Lebesgue measure,
\[
r(x)>n\quad\Longleftrightarrow\quad \phi_\ell^{n-1}(g_\ell(x))\le1-c_\ell
\quad\Longleftrightarrow\quad 0<x\le g_\ell^{-1}(\delta_{n-1}).
\]
Odd symmetry gives the same interval length on the negative half of \(H_\ell\). Divide the total survivor length by \(2c_\ell\) to obtain the displayed exact formula. Since \(\phi_\ell(z)>z\) for positive \(z\), the inverse sequence is strictly decreasing to zero; consequently all except a null set of central initial states return in finite time.

**2. Parabolic coordinate.** Put \(w_m=\delta_m^{-\ell}\). The inverse relation \(\delta_{m-1}=\delta_m(1+\delta_m^\ell)\) is equivalent to
\[
w_m-w_{m-1}=w_m\left[1-(1+w_m^{-1})^{-\ell}\right]
=\ell-\frac{\ell(1+\ell)}{2w_m}+O_\ell(w_m^{-2}).
\]
As \(w_m\to\infty\), increments tend to \(\ell\); hence \(w_m\sim\ell m\). Summing the displayed difference first yields \(w_m=\ell m+O_\ell(\log m)\). Therefore
\[
\sum_{j=1}^m\frac1{w_j}=\frac1\ell\log m+O_\ell(1),
\]
because \(1/w_j-1/(\ell j)=O_\ell((\log j)/j^2)\) is summable. This gives \(w_m=\ell m-\tfrac{1+\ell}{2}\log m+O_\ell(1)\).

For the sharper constant, write \(a=(1+\ell)/2\) and \(v_m=w_m-\ell m+a\log m\) for \(m\ge2\). The preceding estimate and the Taylor expansion imply
\[
v_m-v_{m-1}=O_\ell\!\left(\frac{\log m}{m^2}\right).
\]
The series of these differences converges absolutely, proving \(v_m\to K_\ell\) and the quantitative remainder
\[
w_m=\ell m-a\log m+K_\ell+O_\ell\!\left(\frac{\log m}{m}\right).
\]
In particular, substituting \(m=n-1\) and expanding the negative \(1/\ell\)-power gives
\[
\delta_{n-1}=(\ell n)^{-1/\ell}\left[1+\frac{1+\ell}{2\ell^2}\frac{\log n}{n}
+\frac{\ell-K_\ell}{\ell^2 n}
+O_\ell\!\left(\frac{(\log n)^2}{n^2}\right)\right].
\]

**3. From endpoint distance to the conditional return law.** Taylor expansion at zero yields \(g_\ell(x)=(2+\ell)x+O_\ell(x^2)\), and the inverse-function theorem gives \(g_\ell^{-1}(z)=z/(2+\ell)+O_\ell(z^2)\) as \(z\downarrow0\). Substitute the preceding expansion of \(\delta_{n-1}\) into the exact survivor identity. The inverse-function correction has *relative* order \(O_\ell(\delta_{n-1})=O_\ell(n^{-1/\ell})\), proving the claimed remainder. Because \(0<\ell<1\), this is \(o(n^{-1})\) and cannot mask either the logarithmic coefficient or the constant at order \(1/n\). At \(\ell=1/2\), \(C_\ell=8/(5c_\ell)\) and \(B_\ell=3\), giving the stated specialization. No finite experiment is used to justify the infinite asymptotic.

## Verification

The *computational spot checks* in the accompanying `CHECK.py` use exact symbolic binomial coefficients and high-precision arithmetic. They confirm the inverse-parabolic expansion for three rational exponents, both sides of the exact return-time threshold for many finite times, and bounded residuals after subtracting the predicted logarithmic term. Run `python CHECK.py` with Python 3 and the `mpmath` and `sympy` packages. The executable program tests finite examples only; the preceding proof supplies the quantifiers and convergence.

## Relationship to prior work

Coates, Luzzatto and Muhammad introduced the relevant broad class of doubly intermittent full-branch maps and derived leading return-time tails, with an \(o(n^{-1/\beta-\gamma})\) remainder for any \(\gamma<1\) in their Proposition 2.6, and leading preimage laws in Proposition 3.5. Their paper does not state the logarithmic coefficient at relative order \((\log n)/n\) for normalized central-interval Lebesgue returns. Bansard-Tresse and Freitas applied inducing techniques and recalled leading return tails in their Proposition 4.4; Muhammad and Schindler extended the framework to regularly varying neutral branches, principally for invariant-measure and correlation conclusions. The exact finite-time threshold identity and the three-term subprincipal expansion here apply to an explicit symmetric subfamily and a specified central section, not to arbitrary maps in those broader families. The existence of generic parabolic-coordinate expansions does not by itself identify the stated crossing section, distributional normalization, or coefficient; conversely this theorem does not improve the general maps' mixing theorems.

## Limitations

This is a complete calculation for one natural symmetric subfamily and for normalized Lebesgue initialization on one explicit crossing set. It is **not** a second-order tail theorem for arbitrary asymmetric maps or for invariant inducing measures. Constants are fixed-parameter quantities; no uniform perturbation theorem is claimed. Equivalent formulas in unindexed parabolic iteration or renewal literature remain a publication-priority risk. In particular, the exact analytical correction is a subleading feature of the source family's standard neutral power law, not a claimed new universality class. Independent mathematical audit has not been performed.

## References

1. D. Coates, S. Luzzatto and M. Muhammad, *Doubly Intermittent Full Branch Maps with Critical Points and Singularities*, arXiv:2209.12725, first publicly posted 2022-09-26, especially Sections 1.1, 2.2, 3.2 and 4.1; published in *Communications in Mathematical Physics* 402 (2023), 1845–1878. https://arxiv.org/abs/2209.12725
2. D. Bansard-Tresse and J. Milhazes Freitas, *Inducing techniques for quantitative recurrence and applications to Misiurewicz maps and doubly intermittent maps*, arXiv:2303.17320 (2023), especially Section 4 and Proposition 4.4. https://arxiv.org/abs/2303.17320
3. M. Muhammad and T. I. Schindler, *Doubly intermittent maps with critical points, unbounded derivatives and regularly varying tail*, arXiv:2211.15648 (2022), especially Sections 1 and 4. https://arxiv.org/abs/2211.15648
