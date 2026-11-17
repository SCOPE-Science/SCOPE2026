# Sharp total-variation amplification of the first coupled natural cubic spline

## Finding

The natural \(C^2\) cubic spline through four uniformly spaced real observations has **sharp discrete-to-continuous total-variation amplification**
\[
\boxed{\sup_{V_d(y)>0}\frac{\operatorname{Var}_{[0,3]}(S_y)}{V_d(y)}=1+\frac{8}{9\sqrt{3}}=1.51320023927966\ldots.}
\]
Here \(V_d(y)=|y_1-y_0|+|y_2-y_1|+|y_3-y_2|\). The binary central step \((0,0,1,1)\) attains equality; the same coefficient is sharp for differences of two inputs.

## Assumptions and scope

There are exactly four abscissae \(x_i=i\), indexed \(i=0,1,2,3\). Data \(y\) are arbitrary in \(\mathbb R^4\). The interpolant \(S_y\in C^2([0,3])\) is cubic on each unit interval, satisfies \(S_y(i)=y_i\), and obeys natural endpoint conditions \(S_y''(0)=S_y''(3)=0\). Continuous variation means \(\operatorname{Var}(S_y)=\int_0^3|S_y'(t)|\,dt\). Constants have zero input and output variation. The uniform interval length is normalized to one; common scaling of all abscissae leaves this gain invariant.

## Proof

**1. Interior-curvature system.** Write \(M_i=S_y''(i)\), with \(M_0=M_3=0\). The standard spline continuity equations are
\[
4M_1+M_2=6(y_2-2y_1+y_0),\qquad M_1+4M_2=6(y_3-2y_2+y_1).
\]
For each cell \([i,i+1]\), set \(u=t-i\). Its derivative is
\[
S_y'(i+u)=(y_{i+1}-y_i)-\frac{M_{i+1}-M_i}{6}-\frac{M_i}{2}(1-u)^2+\frac{M_{i+1}}{2}u^2,\qquad0\le u\le1.
\]
This follows by differentiating the cubic representation with endpoint values and second derivatives.

**2. Reduction to the three cuts.** For \(j=1,2,3\), put \(h^{(j)}_i=\mathbf1_{i\ge j}\). Every data vector is \(y=y_0\mathbf1+\sum_{j=1}^3(y_j-y_{j-1})h^{(j)}\). The spline map is linear and sends constants to constants, so the variation triangle inequality yields
\[
\operatorname{Var}(S_y)\le\big(\max_j\operatorname{Var}(S_{h^{(j)}})\big)V_d(y).
\]
Every step has \(V_d(h^{(j)})=1\), so equality is attained for a maximizing step. In particular this is an *exact* operator-norm reduction, not a numerical optimization.

**3. Central cut.** For \(h^{(2)}=(0,0,1,1)\), solve the curvature equations to obtain \(M_1=2\), \(M_2=-2\). The three derivative polynomials, with local coordinate \(u\in[0,1]\), are
\[
\begin{aligned}
p_0(u)&=u^2-\tfrac13,\\
p_1(u)&=\tfrac23+2u-2u^2,\\
p_2(u)&=(1-u)^2-\tfrac13.
\end{aligned}
\]
The first derivative changes sign once at \(u=1/\sqrt3\), the middle is strictly positive, and the last changes sign once at \(u=1-1/\sqrt3\). The negative excursion below the first two observed zeros and the positive excursion above the final two observed ones both have height
\[
\left|\int_0^{1/\sqrt3}\left(u^2-\tfrac13\right)du\right|=\frac{2}{9\sqrt3}.
\]
Therefore the first cell contributes \(4/(9\sqrt3)\), the central cell contributes \(1\), and the last contributes \(4/(9\sqrt3)\), giving \(1+8/(9\sqrt3)\).

**4. Outer cuts and strict comparison.** By reflection the first and third steps have the same gain. For \(h^{(1)}=(0,1,1,1)\), the curvature variables are \(M_1=-8/5\), \(M_2=2/5\). The derivatives, cell by cell, are
\[
\begin{aligned}
q_0(u)&=\tfrac{19}{15}-\tfrac45u^2,\\
q_1(u)&=u^2-\tfrac85u+\tfrac7{15},\\
q_2(u)&=\tfrac1{15}-\tfrac15(1-u)^2.
\end{aligned}
\]
The first derivative is positive. The middle polynomial has its unique zero in \((0,1)\) at \(r=(12-\sqrt{39})/15\), and \(q_2\) changes from negative to positive at \(1-1/\sqrt3\). Their two excursions give
\[
\operatorname{Var}(S_{h^{(1)}})=1+2\int_0^r q_1(u)du+\frac{4}{45\sqrt3}=\frac{133}{125}+\frac{4\sqrt3}{135}+\frac{52\sqrt{39}}{3375}.
\]
This value is strictly less than \(5/4\), using \(\sqrt3<7/4\) and \(\sqrt{39}<7\); the central gain exceeds \(3/2\) since \(\sqrt3<16/9\). Thus the central cut is strictly worst among the three, completing the sharp proof.

**5. Two inputs.** Since \(S_y-S_z=S_{y-z}\), the identical coefficient is the sharp Lipschitz constant under these variation seminorms. Single-cut differences attain it.

## Verification

The accompanying standalone Python checker constructs the exact natural-spline system using rational arithmetic, checks all three derivative coefficient triples, locates each derivative root in the correct cell, evaluates polynomial antiderivatives and compares both symbolic sharp values numerically at high precision. It also tests random four-point datasets against the analytically sharp inequality and checks the central-cut witness. The full proof above establishes all real datasets; finite tests alone are not used as evidence for its universal quantifier.

## Relationship to prior work

Natural cubic splines and their curvature equations are classical. Dermoune and Preda (first arXiv posting 2014-03-06) develop a basis and smoothing analysis of natural cubic splines, including the natural endpoint conditions and curvature construction, but not the four-knot discrete-to-continuous variation norm. The shape-preserving weighted-spline investigation by Kvasov and collaborators (2012) treats alternative weighted splines and interpolation monotonicity, not this unweighted natural-spline sharp norm. An existing three-knot positivity-defect theorem establishes overshoot behavior for the *one-interior-curvature* case; it does not evaluate or imply the first *two-interior-curvature* four-knot variation constant. Numerical and exact identity searches found no corresponding historical table or covering result, though unindexed equivalent formulae remain possible.

## Limitations

The computation is an exact natural invariant of the first genuinely coupled (four-knot) case, not a classification for arbitrary numbers of knots or nonuniform grids. It is not an independent audit, and it does not claim an interpolation approximation-error bound or a nonlinear shape-preservation guarantee. Priority against inaccessible or unindexed historical treatments of four-node natural splines is not conclusively settled.

## References

1. A. Dermoune and C. Preda, *Estimation of noisy cubic spline using a natural basis*, arXiv:1403.1388, posted 2014-03-06, https://arxiv.org/abs/1403.1388.
2. *A shape-preserving approximation by weighted cubic splines*, *Journal of Computational and Applied Mathematics* **236** (2012), 4383–4397, https://doi.org/10.1016/j.cam.2012.04.001.
3. *A sharp three-knot positivity defect for natural cubic interpolation*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-sharp-three-knot-positivity-defect-for-natural-cubic-interpola--0b51d8330304.
