# Fixed damping cannot uniformly safeguard the Twin-Step objective: a sharp angular boundary

## Finding

Let \(F_\kappa(u,v)=(u^2+\kappa v^2)/2\), where \(\kappa>1\). For each \(0<\varepsilon<1\) initialize the two normalized-gradient Twin-Step paths at \(x=(2,2)\) and \(z=(1,1+\varepsilon)\). Both unconstrained ray-intersection lengths are strictly positive, hence coincide with the nonnegative least-distance Twin-Step minimizer, and their undamped endpoints coincide at
\[
w_{\kappa,\varepsilon}=\left(\frac{(\kappa-1)(\varepsilon-1)}{\kappa\varepsilon},-\frac{(\kappa-1)(1+\varepsilon)}{\varepsilon}\right).\]
For every fixed damping \(0<\eta\le1\), let \(x_\eta=(1-\eta)x+\eta w_{\kappa,\varepsilon}\) and \(z_\eta=(1-\eta)z+\eta w_{\kappa,\varepsilon}\). Then the mutual distance contracts exactly by \(1-\eta\), yet
\[
F_\kappa(x_\eta)\sim F_\kappa(z_\eta)\sim
\frac{\eta^2(\kappa-1)^2}{2\varepsilon^2}\left(\kappa+\kappa^{-2}\right).
\]
Both initial objective values remain bounded. Thus **for every fixed nonisotropic condition number \(\kappa>1\) and every positive fixed damping, the first Twin-Step can amplify the better available objective by an arbitrarily large factor**, even while strictly reducing the mutual distance.

The necessary damping scale is quantified sharply on the fixed-condition-number case \(\kappa=2\). If \(\eta=c\varepsilon\) for fixed \(c>0\), the best of the two post-step objective values has the limit
\[
L(c)=\min\left\{6-5c+\frac{9c^2}{8},\ \frac32-\frac{5c}{2}+\frac{9c^2}{8}\right\}.
\]
The better initial value tends to \(3/2\), and
\[
L(c)<\frac32\ \Longleftrightarrow\ 0<c<c_*,\qquad
L(c)>\frac32\ \Longleftrightarrow\ c>c_*,\qquad
c_*:=\frac{20+2\sqrt{19}}9.
\]
At \(c=c_*\) the limiting values tie; the claim makes no assertion about the finite-\(\varepsilon\) comparison at that boundary. The initial gradient-direction cosine satisfies \(1-\gamma\sim2\varepsilon^2/25\) when \(\kappa=2\); consequently the critical damping scale on this family is \(\Theta(\sqrt{1-\gamma})\).

## Assumptions and scope

The underlying algorithm is the two-parameter **basic** Twin-Step of De Magistris, Hochstenbach and Toraldo: for current points \(x,z\) having nonzero gradients, put \(p=-\nabla F_\kappa(x)/\|\nabla F_\kappa(x)\|\) and \(q=-\nabla F_\kappa(z)/\|\nabla F_\kappa(z)\|\), minimize \(\|x+\alpha p-z-\beta q\|^2\) over \(\alpha,\beta\ge0\), then apply the **same** damping \(\eta\in(0,1]\) to both lengths. The statement concerns only that single raw Twin phase; it does not claim failure of a hybrid restart or angle/linesearch safeguard. Arithmetic is exact and \(\kappa\) may be fixed as close to \(1\) as desired but must exceed \(1\). The first-public source date of the motivating method is 2026-07-13 (arXiv:2607.11575v1); the inspected full text includes its subsequent version.

## Proof

Write \(H=\operatorname{diag}(1,\kappa)\). The two normalized descent rays have the same points as \(x-tHx\) and \(z-sHz\) for \(t,s\ge0\). Their direction determinant is \(\det(Hx,Hz)=2\kappa\varepsilon\ne0\), so the two supporting lines have exactly one intersection. Solving \(x-tHx=z-sHz\) gives
\[
t=\frac{\varepsilon\kappa+\varepsilon+\kappa-1}{2\varepsilon\kappa}>0,
\qquad
s=\frac{\varepsilon+\kappa-1}{\varepsilon\kappa}>0.
\]
The normalized-ray lengths are \(\alpha=t\|Hx\|>0\) and \(\beta=s\|Hz\|>0\). Substitution yields exactly the displayed \(w_{\kappa,\varepsilon}\). At that unique feasible pair the distance objective is zero, proving it is the global nonnegative Twin-Step optimum (unique, since the rays are nonparallel). With common damping, subtracting the two updates yields
\[
x_\eta-z_\eta=(1-\eta)(x-z).
\]
The intersection satisfies the coordinatewise limit
\[
\varepsilon w_{\kappa,\varepsilon}\longrightarrow
\left(-\frac{\kappa-1}{\kappa},-(\kappa-1)\right)
\quad(\varepsilon\downarrow0).
\]
For fixed \(\eta>0\), multiplication by \(\varepsilon\) kills each bounded initial point in the damped affine combinations. Applying the positive quadratic form \(F_\kappa\) therefore proves both divergent objective asymptotics and their positive common leading constant. Meanwhile \(F_\kappa(x)=2(1+\kappa)\) and \(F_\kappa(z)=[1+\kappa(1+\varepsilon)^2]/2\) are bounded above and away from zero as \(\varepsilon\downarrow0\). Thus the ratio of the better post-step value to the better pre-step value diverges to infinity; this remains true if one compares against the worse initial value.

For the sharp fixed-condition-number refinement let \(\kappa=2\), so \(w=((\varepsilon-1)/(2\varepsilon),-(1+\varepsilon)/\varepsilon)\). Taking \(\eta=c\varepsilon\) and sending \(\varepsilon\downarrow0\) gives
\[
x_\eta\longrightarrow(2-c/2,2-c),\qquad
z_\eta\longrightarrow(1-c/2,1-c).
\]
Evaluating the quadratic gives the two arguments of \(L(c)\). Their difference is \(9/2-5c/2\): the second branch is the lower branch for \(c\le9/5\), and the first is lower for \(c\ge9/5\). The second branch is strictly below \(3/2\) for \(0<c<20/9\); the first is below \(3/2\) precisely between the roots \((20-2\sqrt{19})/9\) and \((20+2\sqrt{19})/9\). Their union, accounting for which is lower, is exactly \(0<c<c_*\). Beyond \(c_*\), both values exceed \(3/2\). At equality the first branch is exactly \(3/2\). Finally, the identity
\[
1-\gamma^2=\frac{\det(Hx,Hz)^2}{\|Hx\|^2\|Hz\|^2}
=\frac{16\varepsilon^2}{20(5+8\varepsilon+4\varepsilon^2)}
\]
implies \(1-\gamma\sim2\varepsilon^2/25\) because \(\gamma\to1\). This completes the proof.

## Verification

The standalone `checker.py` reconstructs the two ray lengths and intersection using exact rational arithmetic, verifies positivity and all geometric identities across five fixed Hessian ratios and multiple positive offsets/dampings, checks the limiting quadratic formulas at rational offsets, and tests the limiting sharp boundary against both sides. It also checks explicit finite cases with both objectives exceeding both initial values. Its finite checks are **not** substitutes for the exact formulas and limiting proof above. Run `python3 checker.py` from the directory containing this file.

## Relationship to prior work

The motivating work, *A Twin gradient method for unconstrained optimization* (De Magistris, Hochstenbach, Toraldo, arXiv:2607.11575), develops the minimum-mutual-distance Twin-Step and notes that in two dimensions the undamped process terminates after one step; its Sections 3.3 and 5 discuss near-collinearity, potentially large steps and damping/restart safeguards. Thus first-step coalescence, possible nonmonotonicity and the desirability of safeguards **are not claimed as new**. The narrower contribution here is a universal **fixed-curvature, bounded-input unbounded-objective** family valid for *every fixed positive damping*, and a sharp limiting objective-safe damping coefficient connected to the angle gap. The source does not state these quantified conclusions in the examined main theorems, damping analysis, or hybrid algorithm.

Related work on acceleration by objective-minimizing steps (De Magistris et al., *A speed up strategy for gradient methods*, 2026) uses a different selection functional and objective linesearch. Van Lith, Hansen and Hochstenbach (2021) use twin sequences as an error gauge for tomography, not this simultaneous normalized-gradient ray-intersection rule. General one-step steepest-descent objective bounds do not constrain this Twin-Step length, because it is selected by intertrajectory distance rather than by the objective or curvature. Historical equivalences may exist and were not ruled out by a finite literature search.

## Limitations

This is a one-step exact-arithmetic result on a two-dimensional strictly convex quadratic, not a statement of global divergence of safeguarded methods. The source's hybrid restart and adaptive clipping may prevent the exhibited step. The asymptotic threshold at \(c=c_*\) concerns limiting objective values and says nothing about finite-offset equality or monotonicity there. The formula does not extend without analysis to nonsymmetric or nonquadratic systems. The literature comparison cannot certify uniqueness in unindexed manuscripts.

## References

1. A. De Magistris, M. E. Hochstenbach and G. Toraldo, *A Twin gradient method for unconstrained optimization*, arXiv:2607.11575v1 (first public 2026-07-13); subsequent full-text revision arXiv:2607.11575v2, https://arxiv.org/abs/2607.11575.
2. A. De Magistris, S. Crisci, V. De Simone and G. Toraldo, *A speed up strategy for gradient methods*, *Computational Optimization and Applications* **94** (2026), 509–541, https://doi.org/10.1007/s10589-026-00778-0.
3. B. S. van Lith, P. C. Hansen and M. E. Hochstenbach, *A twin error gauge for Kaczmarz's iterations*, *SIAM Journal on Scientific Computing* **43** (2021), S173–S199, https://doi.org/10.1137/20M1349011.
