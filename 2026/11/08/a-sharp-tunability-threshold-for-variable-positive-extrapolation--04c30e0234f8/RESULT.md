# A sharp tunability threshold for variable positive-extrapolation composition splitting

## Finding

Consider the triangular splitting map introduced for the coupled inclusion
\[0\in Hx+A(Bx)-b.\]
Let \(A,B\) be maximally monotone operators on a real Hilbert space, with respective strong-monotonicity moduli at least \(\mu_A,\mu_B>0\), and let \(H\) be \(L\)-Lipschitz. For \(\alpha,\beta>0\) and \(0\le\theta\le1\), write
\[
 y^+=J_{\alpha A}(y-\alpha Hx+\alpha b),\qquad
 x^+=J_{\beta B}\bigl(x+\beta[(1+\theta)y^+-\theta y]\bigr).
\]
The exact threshold for the existence of steps that guarantee a **common strict contraction for all** \(\theta\in[0,1]\), uniformly over every such admissible problem, is
\[\boxed{\mu_A\mu_B>L.}\]
More precisely, if this inequality holds, every \(\beta>0\) admits some \(\alpha>0\) and a weighted block-maximum norm such that every map in the entire extrapolation family is strictly contractive with a single factor smaller than one and has the same unique fixed point. Consequently, for **any** sequence \(\theta_k\in[0,1]\), the nonautonomous iteration converges globally and R-linearly to that fixed point. If \(\mu_A\mu_B\le L\), no fixed positive steps give such a universal strict-contraction guarantee, even for any one prescribed \(\theta\): scalar positive linear factors and negative scalar feedback supply a counterexample.

A quantitative refinement of the source's gain matrix underlies the theorem. If \(Q=J_{\alpha A}\) is firmly nonexpansive and \(q\)-Lipschitz, \(0\le q\le1\), then, for \(0\le\theta\le1\),
\[
 \operatorname{Lip}\bigl((1+\theta)Q-\theta I\bigr)
 \le c_\theta(q):=\sqrt{\theta^2+(1-\theta^2)q^2}.
\]
This is the **sharp universal bound under these two operator assumptions**, attained by a planar skew resolvent for every \(q\in(0,1]\). The original triangle-inequality bound was \((1+\theta)q+\theta\). The refined bound implies the common small-gain matrix and the tunability theorem below; the matrix condition itself is not claimed necessary at fixed steps.

## Assumptions and scope

A real Hilbert space \(\mathcal H\) is arbitrary, including infinite dimensional. Operators \(A,B:\mathcal H\rightrightarrows\mathcal H\) are maximally monotone and respectively \(\mu_A\)- and \(\mu_B\)-strongly monotone: for \((u,a),(v,a')\in\operatorname{gra} A\), \(\langle u-v,a-a'\rangle\ge\mu_A\|u-v\|^2\), and analogously for \(B\). These assumptions ensure their ordinary resolvents are everywhere defined, single-valued and Lipschitz. The map \(H:\mathcal H\to\mathcal H\) is everywhere defined and \(L\)-Lipschitz, with \(L\ge0\). The offset \(b\in\mathcal H\) is arbitrary. Every step size is a positive real number; all extrapolation weights belong to \([0,1]\). The fixed point is a pair \((y_*,x_*)\) satisfying \(b\in Ay_*+Hx_*\) and \(y_*\in Bx_*\), so \(x_*\) solves the stated composition inclusion.

The term *uniform* refers to all admissible operators sharing these moduli and Lipschitz bounds, not to a convergence factor bounded away from one independently of the step sizes or \(\mu_A\mu_B-L\). The common contraction norm may depend on the numerical parameters and bounds, but not on \(\theta\) or the individual operators. The negative part concerns universal strict contraction/unique-solution guarantees, not convergence to some member of a non-singleton solution set.

## Proof

**1. Firm-resolvent transfer.** Put \(u=v-w\) and \(z=Qv-Qw\). Firm nonexpansiveness gives \(\langle z,u\rangle\ge\|z\|^2\), while \(\|z\|\le q\|u\|\). Therefore
\[
\begin{aligned}
\|(1+\theta)z-\theta u\|^2
&=(1+\theta)^2\|z\|^2+\theta^2\|u\|^2-2\theta(1+\theta)\langle z,u\rangle\\
&\le(1-\theta^2)\|z\|^2+\theta^2\|u\|^2\\
&\le[\theta^2+(1-\theta^2)q^2]\|u\|^2.
\end{aligned}
\]
The last step uses \(0\le\theta\le1\). Sharpness: on \(\mathbb R^2\) let \(S\) be a ninety-degree skew rotation and set \(A=\nu S/\alpha\), \(\nu=\sqrt{q^{-2}-1}\). Then \(Q=(I+\nu S)^{-1}\) is the complex multiplier \(q^2-iq\sqrt{1-q^2}\), with \(\|Q\|=q\) and \(\operatorname{Re}Q=q^2\). Both inequalities above are equalities on every nonzero vector. For \(q=1\), take \(A=0\); for \(q=0\), the constant resolvent of a normal cone to \(\{0\}\) attains the remaining bound. These constructions establish sharpness **only for the isolated transfer**.

**2. New nonnegative gain matrix.** Set
\[
 q=(1+\alpha\mu_A)^{-1},\quad s=(1+\beta\mu_B)^{-1},\quad
 c_\theta=\sqrt{\theta^2+(1-\theta^2)q^2}.
\]
For two states write \(\Delta y,\Delta x\) for their differences, and \(\Delta y^+,\Delta x^+\) for the output differences. Resolvent contraction immediately gives
\[\|\Delta y^+\|\le q\|\Delta y\|+\alpha qL\|\Delta x\|.\]
To bound the transmitted intermediate difference, first hold \(x\) fixed when varying \(y\). Step 1 bounds this difference by \(c_\theta\|\Delta y\|\). Then hold \(y\) fixed when varying \(x\); the resolvent Lipschitz estimate bounds its change by \((1+\theta)\alpha qL\|\Delta x\|\). Hence
\[
\|\Delta x^+\|\le\beta s c_\theta\|\Delta y\|+s[1+\alpha\beta(1+\theta)qL]\|\Delta x\|.
\]
In vector form the pair of componentwise differences is bounded by the nonnegative matrix
\[
G_\theta=
\begin{pmatrix}
q&\alpha qL\\
\beta s c_\theta&s[1+\alpha\beta(1+\theta)qL]
\end{pmatrix}.
\]
For \(q,s\in(0,1)\), the nonsingular \(M\)-matrix test gives \(\rho(G_\theta)<1\) if and only if \(\det(I-G_\theta)>0\). Direct expansion and \(1-q=\alpha\mu_A q\), \(1-s=\beta\mu_B s\) give the identity
\[
\boxed{\det(I-G_\theta)=\alpha\beta q s\left[\mu_A\mu_B-L\Psi_\theta(q)\right]},
\qquad
\Psi_\theta(q)=(1-q)(1+\theta)+c_\theta.
\]
Both summands defining \(\Psi_\theta\) are nondecreasing in \(\theta\in[0,1]\), so
\[\Psi_\theta(q)\le\Psi_1(q)=3-2q.\]
In contrast, the cited source's triangle-inequality matrix has the scalar condition \(\mu_A\mu_B>L(1+2\theta)\) for positive \(\theta\). The new bound is strictly weaker for \(L>0\), \(q>0\), and \(\theta>0\) whenever both apply; it need not be optimal among all possible global certificates.

**3. Common contraction and arbitrary switching.** If \(\mu_A\mu_B>L\), choose \(\alpha>0\) so small that
\[L\bigl(3-2/(1+\alpha\mu_A)\bigr)<\mu_A\mu_B.\]
This is possible because its left side tends to \(L\) as \(\alpha\downarrow0\). All \(\beta>0\) are allowed. In fact, if \(L>0\) and \(r=\mu_A\mu_B/L\in(1,3)\), it suffices that
\[0<\alpha<(r-1)/[\mu_A(3-r)];\]
if \(r\ge3\) or \(L=0\), every \(\alpha>0\) works. By Step 2, \(G_1\) is Schur and \(G_\theta\le G_1\) entrywise for all \(\theta\in[0,1]\). Choose any \(\gamma\in(\rho(G_1),1)\) and the positive weight vector
\[w=(\gamma I-G_1)^{-1}(1,1)^\mathsf T.\]
Since \(G_1w=\gamma w-(1,1)^\mathsf T<\gamma w\), every \(G_\theta w\le G_1w<\gamma w\). Therefore all the nonlinear maps are \(\gamma\)-contractions in the **same** complete weighted block-maximum norm
\[\|(y,x)\|_w=\max\{\|y\|/w_1,\|x\|/w_2\}.\]
Banach's fixed-point theorem gives a unique fixed point for \(\theta=1\). At any fixed point \(y^+=y\), so \((1+\theta)y^+-\theta y=y\), and the fixed-point equations are independent of \(\theta\). Thus this fixed point belongs to every map, and arbitrary switching yields the error estimate \(\|z^k-z_*\|_w\le\gamma^k\|z^0-z_*\|_w\).

**4. Sharp necessity for uniform tunability.** In one real dimension set \(A=\mu_A I\), \(B=\mu_B I\), \(H=-LI\), and \(b=0\). The exact iteration matrix in the coordinate order \((y,x)\) is
\[
T_\theta=
\begin{pmatrix}
q&\alpha qL\\
\beta s[(1+\theta)q-\theta]&s[1+\alpha\beta(1+\theta)qL]
\end{pmatrix}.
\]
For **every** \(\alpha,\beta>0\) and \(\theta\in[0,1]\), direct cancellation gives
\[\boxed{\det(I-T_\theta)=\alpha\beta qs(\mu_A\mu_B-L)}.\]
If \(\mu_A\mu_B<L\), this determinant is negative, and the real quadratic characteristic polynomial changes sign between \(1\) and \(+\infty\); hence the matrix has a real eigenvalue strictly larger than one. When \(\mu_A\mu_B=L\), it has eigenvalue one and cannot be a strict contraction in any norm. Consequently, no choice of steps can give a universal strict-contraction guarantee at or below the threshold. This completes the necessary and sufficient class-level assertion.

**5. Explicit strict separation.** With \(\mu_A=3\), \(\mu_B=1/4\), \(\alpha=\beta=1\), \(L=29/100\), \(\theta=1\), one has \(q=1/4\), \(s=4/5\), and
\[\det(I-G_1)=1/200>0.\]
For the original gain matrix in the cited source the corresponding determinant is \(-3/125<0\). Thus the new guarantee certifies every admissible nonlinear problem with these bounds at the prescribed steps while the published comparison certificate does not. All numbers are exact rational values.

## Verification

The standalone `verify.py` checks the rational strict-separation example exactly, checks the scalar negative-feedback determinant identity over a grid of rational parameters, tests sharpness of the isolated firm-resolvent transfer on planar skew resolvents, and checks two-block inequalities on randomly sampled positive-plus-skew planar operators. It reports 8,737 passed diagnostic groups. No finite test is used to infer the universal theorem; Steps 1–4 above establish it analytically. Reproduce from this package with `python3 verify.py` (Python standard library only).

## Relationship to prior work

Qu, Wu and Chaffey (arXiv:2610.39480v1) introduced precisely this two-resolvent triangular splitting and proved the triangle-inequality small-gain matrix (Theorem 15), scalar criterion (Proposition 16), and strong-monotonicity condition \(\mu_A\mu_B>L(1+2\theta)\) for positive extrapolation (Corollary 17). Their Remark 21 addresses positive-extrapolation conservatism for particular linear families and leaves general sharpness unresolved. The present result does **not** replace their algorithm: it proves a different, stronger, class-uniform sufficient test by exploiting the firmly nonexpansive structure of the first resolvent, and closes the class-level **existence of stable steps** question for all positive extrapolation weights, even under switching. It does **not** claim a necessary and sufficient fixed-step criterion.

Firm nonexpansiveness and nonexpansiveness of reflected resolvents are classical, and Liu, Moursi and Vanderwerff (arXiv:2205.09040v1, Fact 2.5) discuss that correspondence and related reflected-resolvent theory. This finding does not claim those facts or their standard interpolation inequalities as new in isolation. Earlier preconditioned proximal/DR splitting theory, including Evens, Pas, Latafat and Patrinos (arXiv:2305.03605), treats other operator-splitting formulations and is not known here to furnish this exact variable-extrapolation composition-family threshold directly. A specific equivalent reduction in older literature remains possible.

## Limitations

The equivalence is at the level of **uniform tunability for a class**, not fixed-step necessity for every nonlinear instance. The explicit sufficient condition may be conservative at fixed parameters, especially for strongly monotone skew resolvents where the abstract sharp firm-transfer example uses a merely monotone skew factor. Small \(\alpha\) may make the certified factor close to one. The theorem assumes positive strong-monotonicity bounds for **both** factors, exact resolvents, fixed operators and a globally Lipschitz \(H\); it does not cover stochastic noise, operator changes, approximate resolvents, or relaxation weights outside \([0,1]\). It does not assert optimal iteration complexity or solve the full fixed-step sharpness question.

## References

1. H. Qu, Y. Wu and T. Chaffey, *Splitting Compositions of Monotone Operators*, arXiv:2610.39480v1, October 29, 2026. https://arxiv.org/html/2610.39480v1.
2. L. Liu, W. M. Moursi and J. Vanderwerff, *Strongly nonexpansive mappings revisited: uniform monotonicity and operator splitting*, arXiv:2205.09040v1, May 18, 2022. https://arxiv.org/pdf/2205.09040.
3. B. Evens, P. Pas, P. Latafat and P. Patrinos, *Convergence of the Preconditioned Proximal Point Method and Douglas-Rachford Splitting in the Absence of Monotonicity*, arXiv:2305.03605, May 5, 2023. https://arxiv.org/abs/2305.03605.
