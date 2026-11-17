# Sharp reentrant transverse stability of synchronous two-cycles in a three-species Lotka–Volterra map

## Finding

For the cyclic three-species discrete Lotka–Volterra map of Muni (2024), the positive synchronous primitive two-cycle has an **exact three-dimensional Floquet spectrum** for every interaction pair with \(1+\alpha+\beta>0\). On the biologically competitive line \(\alpha=\beta=c>0\), the orbit exhibits a sharp **sink–saddle–sink reentrance** as \(c\) increases at fixed birth-rate parameter \(R\), precisely when \(R_*<R<\sqrt6\), where \(R_*\) is the unique real root greater than two of \(R^3-3R-6=0\) (numerically \(R_*=2.3553013976\ldots\)). This stability reversal occurs without changing the orbit's longitudinal two-step multiplier.

Let \(\mathcal P_R(w)=1-(R+2)(R-1)w+(R+2)w^2\). For all \(R>2\), the unique strictly positive synchronous primitive two-cycle has Floquet multipliers

\[
\boxed{5-R^2,\quad \mathcal P_R(w_+),\quad\mathcal P_R(w_-)}
\]

with \(w_\pm=[1-(\alpha+\beta)/2\pm i\sqrt3(\alpha-\beta)/2]/(1+\alpha+\beta)\). For \(\alpha=\beta=c\), the transverse multipliers coincide and equal \(\mathcal P_R((1-c)/(1+2c))\).

For each \(R\in(R_*,\sqrt6)\), set

\[
\begin{aligned}
 v_\pm(R)&=\frac{R-1\pm\sqrt{(R-1)^2-8/(R+2)}}2,\\
 c_1(R)&=\frac{1-v_+(R)}{1+2v_+(R)},\qquad
 c_2(R)=\frac{1-v_-(R)}{1+2v_-(R)}.
\end{aligned}
\]

Then \(0<c_1(R)<c_2(R)<1\). Among \(0<c<1\), the two-cycle is a hyperbolic **attracting** orbit exactly for \(0<c<c_1(R)\) or \(c_2(R)<c<1\); it is a hyperbolic saddle with two transverse expanding directions exactly for \(c_1(R)<c<c_2(R)\). At either threshold a double transverse multiplier is exactly \(-1\), so no nonlinear bifurcation type is asserted there.

For \(2<R<R_*\), every \(0<c<1\) yields a hyperbolic sink. At \(R=R_*\), the unique neutral coupling is \(c=(3-R_*)/(2R_*)\) and all other \(0<c<1\) give hyperbolic sinks. At \(R\ge\sqrt6\), no synchronous primitive two-cycle is a hyperbolic sink; at \(c=1\) the transverse multipliers equal \(1\), and at \(c>1\) both are greater than \(1\). These statements concern **local** stability in the full three-dimensional smooth map.

## Assumptions and scope

For \(R>0\) and real \(\alpha,\beta\), define \(F:\mathbb R^3\to\mathbb R^3\) by

\[
\begin{aligned}
 F_1(x,y,z)&=x+Rx(1-x-\alpha y-\beta z),\\
 F_2(x,y,z)&=y+Ry(1-\beta x-y-\alpha z),\\
 F_3(x,y,z)&=z+Rz(1-\alpha x-\beta y-z).
\end{aligned}
\]

For the general spectrum, suppose \(S=1+\alpha+\beta>0\). A **synchronous** point has equal coordinates, and a **primitive two-cycle** is a pair of distinct states interchanged by \(F\). The multipliers are eigenvalues of \(DF(p_-)DF(p_+)\); their modulus determines local hyperbolic attraction/instability. For the reentrance classification, restrict to \(R>2\), \(\alpha=\beta=c>0\), so all cross-interactions are competitive. No claim is made that the entire positive octant is forward invariant for arbitrary states, nor that there are no nonsynchronous cycles.

## Proof

**1. Existence and uniqueness on the diagonal.** On \((s,s,s)\), the map reduces to \(f(s)=(1+R)s-RSs^2\). With \(q=RSs\), the scalar equation becomes \(q\mapsto(1+R)q-q^2\). Its nonfixed primitive two-cycle satisfies

\[
q^2-(R+2)q+(R+2)=0.
\]

Thus it exists precisely for \(R>2\), and its two positive states are

\[
 p_\pm=(s_\pm,s_\pm,s_\pm),\qquad
 s_\pm=\frac{R+2\pm\sqrt{R^2-4}}{2RS}.
\]

Both are positive, distinct and exchanged by the map; this is the unique positive primitive two-cycle **contained in the diagonal**, not a count of all two-cycles in \(\mathbb R^3\).

**2. Exact monodromy polynomial.** Introduce the real circulant interaction matrix

\[
 C=\begin{pmatrix}1&\alpha&\beta\\\beta&1&\alpha\\\alpha&\beta&1\end{pmatrix}.
\]

At a diagonal state, direct differentiation gives \(DF(s,s,s)=(1+R-RSs)I-RsC\). Writing \(\delta=\sqrt{R^2-4}\), the scalar coefficients at \(s_\pm\) are \((R\mp\delta)/2\), and \(Rs_\pm=(R+2\pm\delta)/(2S)\). Multiplication, using that both Jacobians are polynomials in the **same** matrix \(C\), yields the exact identity

\[
 DF(p_-)DF(p_+)
 =I-(R+2)(R-1)\frac{C}{S}+(R+2)\left(\frac{C}{S}\right)^2.
\]

The eigenvalues of \(C\) are \(S\) and \(1-(\alpha+\beta)/2\pm i\sqrt3(\alpha-\beta)/2\). Evaluating the displayed matrix polynomial at these eigenvalues proves the full spectrum. In particular, \(\mathcal P_R(1)=5-R^2\).

**3. Sharp symmetric stability diagram.** When \(\alpha=\beta=c>0\), the two transverse normalized eigenvalues are \(w=(1-c)/(1+2c)\). A hyperbolic sink must have \(|5-R^2|<1\), equivalent (given \(R>2\)) to \(2<R<\sqrt6\). For \(0<c<1\), \(w\in(0,1)\), and

\[
 \mathcal P_R(w)-1=(R+2)w\bigl(w-(R-1)\bigr)<0.
\]

The remaining stability condition is \(\mathcal P_R(w)>-1\). On \(0<w<1\), this quadratic has its unique minimum at \(w_0=(R-1)/2\), of value \(1-(R+2)(R-1)^2/4\). The minimum crosses \(-1\) at \((R+2)(R-1)^2=8\), namely at \(R=R_*\). The left-hand side increases strictly with \(R>2\), equals \(4\) at \(R=2\), and exceeds \(8\) at \(R=\sqrt6\). For \(R_*<R<\sqrt6\), the two roots of \(\mathcal P_R(w)=-1\) are \(v_-<v_+\), both in \((0,1)\). Because \(c=(1-w)/(1+2w)\) decreases strictly with \(w\), the stated ordered thresholds and the sink–saddle–sink intervals follow. At the middle interval \(\mathcal P_R(w)<-1\), the two transverse modes expand, while the longitudinal mode still contracts. At \(c\ge1\), \(w\le0\) and \(\mathcal P_R(w)\ge1\); equality holds only at \(c=1\). This also proves the endpoint claims.

**4. An exact rational witness.** At \(R=12/5\), the longitudinal multiplier is \(-19/25\). At positive cross-competitions \(c=1/100,1/10,1/2\), the repeated transverse multiplier equals, respectively,

\[
 \boxed{-12049/14450,\qquad-229/200,\qquad-53/200.}
\]

Thus these three fully positive parameter choices give, respectively, a hyperbolic sink, a two-direction hyperbolic saddle, and another hyperbolic sink. Their positivity and the two-cycle relation follow from the exact formula in step 1.

## Verification

The accompanying standalone script `verify_two_cycle.py` reconstructs the scalar two-cycle equations, the monodromy coefficient identities, the circulant spectrum and all three exact rational witnesses using symbolic arithmetic. Run `python verify_two_cycle.py` with Python 3 and SymPy installed. In addition to these executable identities, step 3 of the proof analytically establishes every quantified stability interval; no finite sampling is used as a substitute for that argument.

## Relationship to prior work

Muni, *Torus and hyperchaos in 3D Lotka–Volterra map* (arXiv:2408.15054v1), introduces exactly this cyclic three-species map in equation (2.1) and numerically studies period-two to period-six, torus and hyperchaos transitions. Its period-two study uses \(R\) around \(1\), where the **synchronous** primitive two-cycle here does not exist; its interacting parameters include negative values. The inspected complete preprint does not provide the diagonal-cycle monodromy polynomial or this positive-competition reentrant stability diagram. The scalar logistic two-cycle itself and the Fourier diagonalization of circulant matrices are classical ingredients, not claimed as independent discoveries.

A published result on **synchronous Ricker competition** provides a spectral Floquet reduction for an exponential update law, not the Euler-polynomial map here; its formulas do not imply the displayed quadratic multiplier or threshold \(R_*\) without a new calculation. A separate published **antisymmetrically coupled two-site logistic** study exhibits reentrant transverse stability in a different, clipped and lower-dimensional map; the qualitative phenomenon alone does not imply this three-species classification. Balibrea–García Guirao–Lampart–Llibre (2006) study an explicitly different planar Lotka–Volterra map.

Gardini–Lupini–Mammana–Messia (1987) study a cyclically invariant three-dimensional Lotka–Volterra map and are a relevant possible precedent. The available abstract emphasizes equilibrium bifurcation and weak resonance, but the full article was unavailable through checked lawful access routes. Priority relative to its uninspected interior remains a specific limitation; absence of indexed matches alone is not proof of universal novelty.

## Limitations

The stability assertions are strictly local to the synchronous orbit. The polynomial update may leave the positive octant away from its periodic states. At the nonhyperbolic thresholds the proof does not determine flip criticality, existence of adjacent nonsynchronous cycles or nonlinear attraction. The full parameter-plane stability inequalities for \(\alpha\ne\beta\) are encoded by the complex polynomial but not separately classified. The uninspected 1987 article and possible unindexed equivalents leave a publication-priority risk. Independent mathematical audit has not been performed.

## References

1. S. S. Muni, *Torus and hyperchaos in 3D Lotka–Volterra map*, arXiv:2408.15054v1 (first publicly submitted 2024-08-27), https://arxiv.org/abs/2408.15054.
2. L. Gardini, R. Lupini, C. Mammana, M. G. Messia, *Bifurcations and Transitions to Chaos in the Three-Dimensional Lotka–Volterra Map*, SIAM J. Appl. Math. 47 (1987), 455–482, https://doi.org/10.1137/0147031.
3. F. Balibrea, J. L. García Guirao, M. Lampart, J. Llibre, *Dynamics of a Lotka–Volterra map*, Fundamenta Mathematicae 191 (2006), 265–279, https://doi.org/10.4064/fm191-3-5.
