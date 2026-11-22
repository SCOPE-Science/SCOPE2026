# Sharp Fourier-bias balancing on incomplete finite-field line pencils

## Finding

Fix a prime power \(q\ge2\) and \(2\le k\le q\). Let \(L_1,\ldots,L_k\) be any \(k\) distinct one-dimensional \(\mathbb F_q\)-linear subspaces of \(\mathbb F_q^2\), and set \(S=\bigcup_{j=1}^k L_j\). Given any nontrivial additive character \(\psi\) of \(\mathbb F_q\), define the unnormalized Fourier transform of a probability mass \(\mu\) by
\[
\widehat\mu(\xi)=\sum_{x\in\mathbb F_q^2}\mu(x)\,\psi(-\xi\cdot x).
\]
The *optimal nontrivial Fourier bias* of the support is
\[
\mathfrak b(S)=\inf_{\substack{\mu\ge0,\ \operatorname{supp}(\mu)\subseteq S\\\sum_x\mu(x)=1}}\ \max_{\xi\ne0}|\widehat\mu(\xi)|.
\]
Then the exact sharp result, independent of the selected directions and of \(\psi\), is
\[
\boxed{\mathfrak b(S)=\begin{cases}
\dfrac{1}{2k-1},&q\le2k,\\[3pt]
\dfrac{q-k}{k(q-1)},&q\ge2k.
\end{cases}}
\]
The branches agree at \(q=2k\). An attaining mass has constant weight \(a\) at the origin and constant weight \(b\) at each of the other \(k(q-1)\) points, with
\[
(a,b)=\begin{cases}
\left(\dfrac{2k-q}{q(2k-1)},\dfrac{2}{q(2k-1)}\right),&q\le2k,\\[4pt]
\left(0,\dfrac{1}{k(q-1)}\right),&q\ge2k.
\end{cases}
\]
**Central-atom rigidity:** every attaining probability measure, even one without radial or line-permutation symmetry, assigns exactly the displayed mass \(a\) to the origin. Thus every optimizer charges the origin if \(q<2k\), and no optimizer charges it if \(q\ge2k\). The displayed canonical optimizer has *constant absolute Fourier coefficient at every nonzero frequency* exactly when \(q\le2k\); for \(q>2k\), its nontrivial Fourier magnitudes have two distinct levels. The uniform probability mass on all of \(S\) is optimal exactly when \(q=2k-2\).

## Assumptions and scope

All fields have finite order \(q=p^m\) and all lines are through the origin. Nonnegative real probability weights may vanish, so the support need only be contained in \(S\). The maximum excludes the zero frequency, at which \(\widehat\mu(0)=1\). The Fourier normalization is **unnormalized**; this is essential for the numerical constants. The result holds for every choice of distinct line directions and every nontrivial additive character, including characteristic two. It concerns positive-measure Fourier flatness, not unconstrained complex Fourier synthesis or restriction norms.

## Proof

**1. Radial symmetrization.** For every \(c\in\mathbb F_q^*\), replace \(\mu\) by the pushforward of \(\mu\) under \(x\mapsto cx\). This preserves \(S\), the mass at the origin, positivity, and total mass; it permutes nonzero Fourier frequencies. Since the maximum absolute Fourier coefficient is a convex function of the measure, averaging these \(q-1\) pushforwards cannot increase the objective. The averaged measure takes one value \(a\ge0\) at \(0\) and a common value \(b_j\ge0\) on \(L_j\setminus\{0\}\). Write \(B=\sum_j b_j\), so \(a+(q-1)B=1\).

**2. Exact Fourier levels.** For nontrivial \(\psi\), the sum over nonzero elements of a line is \(q-1\) when \(\xi\) annihilates that line and \(-1\) otherwise. Each nonzero frequency annihilates exactly one projective line, and the annihilator lines of the selected \(L_j\) are disjoint except at zero. Consequently, with \(t=a-B\), the averaged Fourier transform equals \(1\) at \(\xi=0\); it equals \(t+qb_j\) at each of the \(q-1\) nonzero frequencies of \(L_j^\perp\); and it equals \(t\) at the \((q+1-k)(q-1)\) remaining nonzero frequencies. As \(k\le q\), that last class is nonempty. Thus the exact bias of the averaged mass is
\[
\max\left\{|t|,\max_{1\le j\le k}|t+qb_j|\right\}.
\]
For fixed \(a,B\), replacing every \(b_j\) by the mean \(B/k\) preserves feasibility and cannot increase this maximum: \(\big|t+qB/k\big|\le\max_j|t+qb_j|\) by the triangle inequality. In particular, an optimum exists among the *fully symmetrized* masses \(a\) at zero, \(b\) at every other site. Both symmetrizations leave the origin mass unchanged.

**3. One-variable minimax.** The constraints \(a+k(q-1)b=1\) and \(t=a-kb\) give
\[
 b=\frac{1-t}{kq},\qquad a=\frac{1+(q-1)t}{q},\qquad
 -\frac1{q-1}\le t\le1.
\]
For nonzero dual-line frequencies the coefficient is
\[
y=t+qb=\frac{1+(k-1)t}{k},\]
which is nonnegative throughout this interval because \(k\le q\). Hence one must minimize \(\max\{|t|,y\}\). On \(t\ge0\), the objective is \(y\), which increases with \(t\) because \(k\ge2\). On \(t\le0\), the two competitors \(-t\) and \(y\) cross exactly at \(t_*=-1/(2k-1)\). The crosspoint is feasible precisely when \(q\le2k\). If feasible it is the unique minimizer. Otherwise the unique minimizer is the left endpoint \(t=-1/(q-1)\), which makes \(a=0\). Substitution gives the boxed constant and displayed weights, including agreement at the boundary. For \(q>2k\), the two levels are \(1/(q-1)\) off selected dual lines and \((q-k)/(k(q-1))\) on them; the latter is strictly larger. For \(q\le2k\), their magnitudes both equal \(1/(2k-1)\).

**4. Rigidity of the origin atom.** Apply the two averaging steps to an *arbitrary* global minimizer. Neither step changes its origin atom and neither can increase its bias; since the starting bias was minimal, the resulting fully symmetric mass also minimizes. The one-variable minimizer above is unique, so this symmetric mass has the displayed atom \(a\). Therefore the original, possibly asymmetric minimizer must have precisely that same \(a\). The only fully symmetric optimum is the displayed one. Finally, uniform mass means \(a=b\). In the interior branch \(a/b=(2k-q)/2\), yielding \(q=2k-2\); in the boundary/exterior branch \(a=0<b\). This proves the uniform-mass assertion.

## Verification

The standalone standard-library script `check_bias.py` constructs the field operations, distinct projective lines, selected pencils, and their unnormalized complex Fourier transforms. It tests prime orders \(2,3,5,7,11\), and nonprime prime powers \(4,8,9\), several values of \(k\), and multiple direction selections. Its run compared 4,376 nonzero Fourier coefficients with the two-level formulas and checked the maximum against the exact minimax constant; all comparisons passed. These finite numerical checks are supplementary only. The proof above establishes the result for every prime power and every permitted pencil.

Two illustrative exact cases: when \(q=5,k=2\), the optimum is \(3/8\), attained with no atom at the origin and weight \(1/8\) at each of eight other support points; when \(q=5,k=3\), the optimum is \(1/5\), attained with weight \(1/25\) at the origin and \(2/25\) at each of twelve other support points. In the latter case all \(24\) nonzero Fourier coefficients have magnitude \(1/5\).

## Relationship to prior work

Fraser, *Fourier analytic properties of Kakeya sets in finite fields*, first available as arXiv:2505.09464 on 2025-05-14, proves an existence bound for probability measures on unions of lines in prescribed orientations (Theorem 2.1 and the accompanying incidence construction). For \(k\) concurrent directions in the plane, that construction gives the bound \(1/k\), but the inspected theorem and proof do not solve the exact nontrivial-frequency minimax problem or the change in the optimal intersection mass. The present result gives an exact value strictly below that incidence bound for \(2\le k\le q\), a spectral-flatness threshold, and atom rigidity. This is a specialization of the *geometric setup*, not a corollary of the previously stated inequality.

Iosevich–Li–Yu, *Spectral synthesis, Fourier extension, and arithmetic in \(\mathbb Z_N^d\)*, arXiv:2609.25404v2, studies a different ratio involving the largest Fourier coefficient divided by its full \(\ell^r\) norm. Its affine-transitive exact-constant theorem does not apply to this intersection-versus-lines support, and its ratio does not imply the positive-measure off-zero minimax value here. Independently catalogued sharp Fourier synthesis constants for line pencils at the fourth power, and all-exponent synthesis for two axes, concern that different objective and do not settle this theorem.

## Limitations

The theorem does not classify the *entire* set of nonsymmetric optimizing measures, though it proves their origin mass is fixed. It does not concern affine translates of different lines with separate intersection patterns, complex signed measures, or quantitative perturbation stability. For the excluded complete pencil \(k=q+1\), \(S=\mathbb F_q^2\) and the uniform measure has bias zero. No claim of independent mathematical review or unrestricted bibliographic novelty is made; an older equivalent exact minimax statement for positive measures could remain undiscovered.

## References

1. J. M. Fraser, *Fourier analytic properties of Kakeya sets in finite fields*, arXiv:2505.09464v1 (2025-05-14), https://arxiv.org/abs/2505.09464 ; *Bulletin of the London Mathematical Society* (2026), https://doi.org/10.1112/blms.70367. Specifically §2, Theorem 2.1, and §3.1.
2. A. Iosevich, Z. Li, and K. Yu, *Spectral synthesis, Fourier extension, and arithmetic in \(\mathbb Z_N^d\)*, arXiv:2609.25404v2 (2026-11-16), https://arxiv.org/html/2609.25404v2. Specifically §1 and §4.
