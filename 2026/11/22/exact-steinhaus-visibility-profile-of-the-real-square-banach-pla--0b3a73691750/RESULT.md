# Exact Steinhaus visibility profile of the real square Banach plane

## Finding

For the real two-dimensional Banach space \(X=(\mathbb R^2,\|\cdot\|_\infty)\), consider the norm-difference Steinhaus modulus
\[
U_X(d;a)=\inf_{\substack{x,y\in S_X\\\|x-y\|_\infty\ge d}}
\sup_{\|z\|_\infty\le a}
\big|\|x+z\|_\infty-\|y+z\|_\infty\big|.
\]
For all \(0<d\le2\) and \(a\ge0\),
\[
\boxed{U_X(d;a)=\min\left\{d,\max\left\{0,2a+\frac d2-1\right\}\right\}.}
\]
Equivalently, there is an **exact three-regime profile**:
\[
U_X(d;a)=\begin{cases}
0,&0\le a\le(2-d)/4,\\
2a+d/2-1,&(2-d)/4\le a\le(2+d)/4,\\
d,&a\ge(2+d)/4.
\end{cases}
\]
The formula is attained for every pair of parameters by
\[
x_d=(1,d/2),\qquad y_d=(1,-d/2).
\]
It also holds, without changing \(d\) or \(a\), for the **real** two-atom \(\ell_1^2\) plane, via the real linear isometry \((u,v)\mapsto((u+v)/2,(u-v)/2)\).

## Assumptions and scope

All scalars and perturbations are real. The unit sphere is the boundary of the square \([-1,1]^2\). The parameters satisfy \(0<d\le2\), \(a\ge0\). In the original uniform Steinhaus definition the customary parameter range is \(0<d<2\), \(a>0\); the boundary cases here follow from the same proof. The supremum uses the **closed** perturbation ball. The absolute difference is essential. The complex two-atom \(\ell_1\) space has additional imaginary perturbation directions and is **not** claimed to satisfy this law.

Write \(B(x,y;a)\) for the inner supremum. Since the norm is 1-Lipschitz,
\[
0\le B(x,y;a)\le\|x-y\|_\infty.
\]
We use \(\Phi_a(s)=\min\{s,\max\{0,2a+s/2-1\}\}\), a nondecreasing function of \(s\in[0,2]\).

## Proof

**1. The large-radius case.** If \(a\ge1\), then \(z=-x\) is allowed for any \(x\in S_X\), and
\[
B(x,y;a)\ge\big|\|0\|-\|y-x\|\big|=\|x-y\|.
\]
The opposite inequality above yields equality. Since there are unit pairs at every separation \(d\in(0,2]\), \(U_X(d;a)=d=\Phi_a(d)\). Henceforth assume \(0\le a\le1\). At \(a=0\) the formula is immediate; the argument below also covers it.

**2. A scalar convexity lemma.** Put \(c=1-a\ge0\) and \(h(s)=\max\{c,|s|\}\). For any \(\delta\in[0,2]\),
\[
h(a+\delta/2)-h(a-\delta/2)=\Phi_a(\delta).\tag{1}
\]
Indeed, set \(A=a+\delta/2\), \(B=|a-\delta/2|\). If \(A\le c\), both maxima equal \(c\). Otherwise, if \(B\le c\), the difference equals \(A-c=2a+\delta/2-1\); if \(B>c\), necessarily \(a\ge\delta/2\) and \(2a>1+\delta/2\), and the difference is \(A-B=\delta\). These are precisely the three regimes of \(\Phi_a\). Furthermore, for every convex even \(h\), the increment
\[
D_\delta(s)=h(s+\delta/2)-h(s-\delta/2)
\]
is odd and nondecreasing in \(s\). Convexity proves monotonicity by increasing secant slopes (or one-sided derivatives).

We shall also use the elementary identity, for \(0\le b\le2\),
\[
1+a-\max\{1-a,|1+a-b|\}=\min\{2a,b\}.\tag{2}
\]
It follows by comparing \(b\le2a\) with \(b\ge2a\); in the latter case \(|1+a-b|\le1-a\) because \(b\le2\).

**3. Uniform lower bound for an arbitrary unit pair.** Signed coordinate permutations allow us to put \(x=(1,t)\), \(-1\le t\le1\). The second unit point lies on one of the four facets of the square. Write \(\delta=\|x-y\|_\infty\).

* If \(y=(1,s)\), then \(\delta=|t-s|\). Exchange \(x,y\) if needed to assume \(t\ge s\), and set \(m=(t+s)/2\). Restrict to \(z=(-a,z_2)\), which gives the difference \(|D_\delta(m+z_2)|\) with \(h\) from Step 2. If \(m\ge0\), choose \(z_2=a\); if \(m<0\), choose \(z_2=-a\). Oddness and monotonicity yield \(B(x,y;a)\ge D_\delta(a)=\Phi_a(\delta)\).

* If \(y=(u,1)\), let \(\alpha=1-u\), \(\beta=1-t\), so \(\delta=\max\{\alpha,\beta\}\). The perturbations \((-a,a)\) and \((a,-a)\), respectively, yield norm differences \(\min\{2a,\beta\}\) and \(\min\{2a,\alpha\}\) by (2). Thus \(B(x,y;a)\ge\min\{2a,\delta\}\ge\Phi_a(\delta)\), as \(\delta\le2\).

* If \(y=(u,-1)\), put \(\alpha=1-u\), \(\beta=1+t\), and \(\delta=\max\{\alpha,\beta\}\). The perturbations \((a,a)\) and \((-a,-a)\) give the same respective differences \(\min\{2a,\alpha\}\) and \(\min\{2a,\beta\}\). Hence the same lower bound holds.

* If \(y=(-1,s)\), then \(\delta=2\). Choose \(z_1=a\) and \(z_2\in[-a,a]\) minimizing \(|s+z_2|\). Since \(|s|\le1\), the latter minimum is at most \(1-a\). Thus \(\|x+z\|_\infty=1+a\), while \(\|y+z\|_\infty=1-a\), and \(B(x,y;a)\ge2a=\Phi_a(2)\) for \(0\le a\le1\).

Therefore every unit pair with \(\delta\ge d\) satisfies \(B(x,y;a)\ge\Phi_a(\delta)\ge\Phi_a(d)\).

**4. Exact matching pair.** Let \(x=x_d\), \(y=y_d\) as in the theorem; both are unit vectors and their distance is \(d\). For a perturbation \(z=(z_1,z_2)\), set \(C=|1+z_1|\), \(u=|z_2+d/2|\) and \(v=|z_2-d/2|\). Then
\[
|\|x+z\|-\|y+z\||=|\max\{C,u\}-\max\{C,v\}|.
\]
For fixed \(z_2\), this difference cannot increase as \(C\) increases. On \([-a,a]\), the minimum \(C=1-a\) occurs at \(z_1=-a\). With this choice, the remaining expression is \(|D_d(z_2)|\); oddness and monotonicity of \(D_d\) show its maximum on \([-a,a]\) is \(D_d(a)\). By (1), this is exactly \(\Phi_a(d)\). Together with Step 3, this completes the proof for all \(0\le a\le1\), and Step 1 handles larger radii.

**5. Real two-atom identification.** For real \(u,v\),
\[
\frac{|u+v|+|u-v|}{2}=\max\{|u|,|v|\}.
\]
Thus the linear map displayed in the theorem is a surjective isometry from the square plane onto real \(\ell_1^2\); it preserves sphere separation and all admissible perturbations, hence the entire modulus.

## Verification

The proof is analytic for arbitrary real parameters and does not rely on numerical optimization. The finite exact-rational checker `check.py` evaluates the maximum over every vertex of the affine subdivision determined by the two norm functions and the perturbation square; it checks arbitrary boundary pairs against the analytic lower bound and the explicit extremizer against equality. On execution it reported `STEINHAUS_SQUARE_EXACT_RATIONAL_DIAGNOSTIC_OK 18145`. Every arithmetic step in this diagnostic uses exact rational numbers. Finite tests are supporting evidence, not an exhaustive proof for continuum parameters.

For reproducibility, run `python3 check.py` using Python 3's standard library. The key proof identities (1) and (2), the four facet cases, and the real linear isometry can also be checked directly without code.

## Relationship to prior work

Johnson and Kania [1] introduced this **exact norm-difference** modulus and determined it for nonatomic real \(L_1\), where its value is \(d\min\{4a/(2+d),1\}\), positive at every positive radius. Their original source's definitions and central results do not contain the real square-plane formula. The present result exposes a different atomic phenomenon: complete invisibility until a sharp, positive radius, followed by a linear transition and exact saturation.

Kania and Kochanek [2] established the qualitative characterization of property \((S)\) and, in real dimension at most two, its equivalence to strict convexity. Their theorem implies that the square lacks property \((S)\), but gives neither of the exact detection and saturation thresholds nor the full two-parameter modulus. The relevant published note [3] concerns the **complex** two-atom \(\ell_1\) plane (real dimension four): it establishes a positive quadratic small-radius modulus, not this finite-radius real two-dimensional profile. Neither the real finite-\(p\) estimates [4] nor the scalar-Hilbert one-sum [5] have a hypothesis or bound implying the formula for the square. The real isometry to \(\ell_1^2\) is explicitly accounted for rather than treated as a second result.

## Limitations

This is a full quantitative result for the **real two-dimensional** supremum-norm plane, not for higher-dimensional cubes, complex scalars, other polyhedral norms, or powered versions of the modulus. It does not claim uniqueness of extremizing pairs, a generalized classification of spaces with property \((S)\), or a universal formula for all finite atomic measure spaces. Earlier work proves the qualitative failure of property \((S)\) in this plane; the claim here is the exact two-parameter profile. Searches cannot rule out unindexed equivalent formulas, and no independent mathematical audit has been conducted.

## References

[1] W. B. Johnson and T. Kania, *Uniform Property (S)*, arXiv:2602.09106v1, publicly posted 9 February 2026; Definitions 1.1–1.2, Proposition 1.4, Theorems B and C, and their proofs. https://arxiv.org/abs/2602.09106 . An author-accessible full-text copy is at https://www.researchgate.net/publication/400661716_Uniform_Property_S .

[2] T. Kania and T. Kochanek, *Steinhaus' lattice-point problem for Banach spaces*, arXiv:1302.6443, J. Math. Anal. Appl. 446 (2017), 1219–1229; Theorems A–B. https://arxiv.org/abs/1302.6443 . An author-uploaded full text appears at https://www.researchgate.net/publication/286447168_Steinhaus%27_lattice-point_problem_for_Banach_spaces .

[3] *Sharp quadratic Steinhaus modulus of the complex two-atom \(\ell_1\) plane*, public mathematical research record, 17 November 2026, full RESULT.md inspected at https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-quadratic-steinhaus-modulus-of-the-complex-two-atom-ell-1--c83f634f9c2d .

[4] *Sharp small-radius Steinhaus modulus of real \(\ell_p\) for \(p\ge2\)*, public mathematical research record, 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-small-radius-steinhaus-modulus-of-real-ell-p-for-p-ge2--072a2f172b7d .

[5] *Sharp quadratic Steinhaus modulus of a scalar–Hilbert one-sum*, public mathematical research record, 18 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-quadratic-steinhaus-modulus-of-a-scalar-hilbert-one-sum--102221e3c81d .
