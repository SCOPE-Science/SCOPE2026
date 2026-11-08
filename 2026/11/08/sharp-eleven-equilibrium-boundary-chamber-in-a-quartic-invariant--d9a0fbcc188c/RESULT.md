# Sharp eleven-equilibrium boundary chamber in a quartic invariant-square flow

## Finding

Consider the six-parameter quartic planar family introduced by Grau and Szántó [1]:
\[
\begin{aligned}
\dot x&=(1-x^2)(\lambda x-y+a x^2+bxy-a y^2),\\
\dot y&=(1-y^2)(x+\lambda y+c x^2+dxy+e y^2),
\end{aligned}
\qquad (\lambda,a,b,c,d,e)\in\mathbb R^6.
\]
Let \(N_{\partial S}\) be the cardinality of the set of **distinct real equilibrium points on the boundary** of \(S=[-1,1]^2\); a continuum has cardinality \(\infty\) here. Then
\[
\boxed{N_{\partial S}\in\{4,5,6,7,8,9,10,11,\infty\},}
\]
and **every displayed value occurs**. In particular, the sharp finite bound is eleven, not twelve, despite four invariant edges each carrying a quadratic stationary equation. Infinite boundary equilibrium sets occur **if and only if** one of the vertical edges consists entirely of equilibria; this happens precisely if
\[
\boxed{e=0,\quad c=-s,\quad\lambda+ds=0\quad\text{for some }s\in\{-1,1\}.}
\]

Moreover, the entire parameter locus attaining eleven is characterized by explicit strict polynomial inequalities. Define \(\mathsf T(A,B,C)\) by the conjunction
\[
 A\ne0,\quad B^2-4AC>0,\quad B^2<4A^2,\quad
 A(A+B+C)>0,\quad A(A-B+C)>0.
\]
(These conditions say precisely that \(Au^2+Bu+C\) has two distinct roots in \((-1,1)\).) Then \(N_{\partial S}=11\) if and only if **all** of the following hold:
\[
\begin{gathered}
\mathsf T(e,\lambda+d,c+1),\qquad \mathsf T(e,\lambda-d,c-1),\\
\bigl[\mathsf T(a,\lambda+b,-1-a)\ \wedge\ |\lambda-b|>1\bigr]\\
\hspace{1em}\vee\bigl[\mathsf T(a,\lambda-b,1-a)\ \wedge\ |\lambda+b|>1\bigr].
\end{gathered}
\]
The final disjunction is taken together with the two preceding conditions. In particular this chamber is open and nonempty, and the eleven boundary equilibria can all be **hyperbolic**.

## Assumptions and scope

The parameters are arbitrary real numbers and the phase space is the real plane. Only equilibrium points on \(\partial S\) are counted, with all four corners counted **once each**. Non-corner roots must lie in the open edge intervals, so corner repetitions and endpoint roots are not double-counted. A repeated root within an edge counts as one equilibrium, not two. This is an exact boundary classification, not a census of interior or exterior equilibria or a claim about global separatrices.

For \(t=\pm1\) on the horizontal edge \(y=t\), write
\[
 H_t(u)=a u^2+(\lambda+bt)u-a-t.
\]
For \(s=\pm1\) on the vertical edge \(x=s\), write
\[
 V_s(u)=e u^2+(\lambda+ds)u+c+s.
\]
When no vertical-edge polynomial vanishes identically, the exact cardinality is
\[
 N_{\partial S}=4+\sum_{t=\pm1}\#\{u\in(-1,1):H_t(u)=0\}
 +\sum_{s=\pm1}\#\{u\in(-1,1):V_s(u)=0\}.
\]

## Proof

**Boundary reduction and degeneracies.** On \(y=t\), the second component vanishes identically and the first is \((1-u^2)H_t(u)\). On \(x=s\), the first component vanishes identically and the second is \((1-u^2)V_s(u)\). The four corners are always equilibria. Neither horizontal polynomial can vanish identically: if \(a=0\), then its constant coefficient is \(-t\ne0\). The vertical polynomial \(V_s\) vanishes identically exactly under \(e=0\), \(c=-s\), \(\lambda+ds=0\). At most one vertical edge can be identically stationary because \(c\) cannot equal both \(-1\) and \(1\). This proves the infinite-set characterization and the finite counting formula.

**Why eleven rather than twelve.** Each vertical polynomial has at most two interior roots, giving at most four non-corner vertical equilibria. Each horizontal polynomial also has at most two interior roots, but they cannot *both* have two. Indeed,
\[
 H_+(1)=\lambda+b-1,\quad H_+(-1)=-\lambda-b-1,
\]
whereas
\[
 H_-(1)=\lambda-b+1,\quad H_-(-1)=-\lambda+b+1.
\]
Two distinct interior roots of \(H_+\) force both endpoint values to be negative and \(a<0\): the quadratic is concave and positive between its zeros. Two distinct interior roots of \(H_-\) force both endpoint values to be positive and \(a>0\): the quadratic is convex and negative between its zeros. The two requirements are incompatible. Hence at most three non-corner horizontal equilibria and \(N_{\partial S}\le4+3+4=11\).

**The exact maximal chamber.** A quadratic \(Au^2+Bu+C\) has two distinct roots in \((-1,1)\) exactly when its discriminant is positive, its vertex lies strictly between \(-1\) and \(1\), and its values at both endpoints have the sign of \(A\). Those conditions are precisely \(\mathsf T(A,B,C)\). Eleven requires two interior roots on each vertical side and three horizontally. If \(H_+\) has two roots, then \(a<0\). In that case \(H_-\) has one interior root exactly when its endpoint values have opposite signs, namely \(|\lambda-b|>1\). At equality, one endpoint is a root while the interior remains of constant nonzero sign, so there is no hidden third interior root. The symmetric argument for \(H_-\) having two roots gives \(|\lambda+b|>1\). This proves the iff conditions, including their strict inequalities and all endpoints.

**Sharp attainable finite spectrum.** The following rational parameter witnesses realize every integer \(N_{\partial S}\in\{4,\ldots,11\}\). The ordered root-count tuple records interior roots on \(y=+1\), \(y=-1\), \(x=+1\), and \(x=-1\), respectively.

| \(N_{\partial S}\) | \((\lambda,a,b,c,d,e)\) | Root-count tuple |
| ---: | --- | --- |
| 4 | \((0,0,0,0,0,0)\) | \((0,0,0,0)\) |
| 5 | \((2,0,2,5,0,0)\) | \((1,0,0,0)\) |
| 6 | \((0,2,0,0,0,0)\) | \((0,2,0,0)\) |
| 7 | \((3/2,2,3/2,-2,0,-1)\) | \((1,2,0,0)\) |
| 8 | \((3/2,2,3/2,-2,0,0)\) | \((1,2,1,0)\) |
| 9 | \((3/2,2,3/2,-2,0,2)\) | \((1,2,1,1)\) |
| 10 | \((3/2,2,3/2,-2,0,3)\) | \((1,2,2,1)\) |
| 11 | \((3/2,2,3/2,-2,0,5)\) | \((1,2,2,2)\) |

An infinite example is \((\lambda,a,b,c,d,e)=(0,0,0,-1,0,0)\), for which \(x=1\) is entirely stationary.

**Hyperbolic sharp witness.** At the last rational tuple, the four edge quadratics are
\[
\begin{array}{ll}
 H_+(u)=2u^2+3u-3,&H_-(u)=2u^2-1,\\
 V_+(u)=5u^2+\tfrac32u-1,&V_-(u)=5u^2+\tfrac32u-3.
\end{array}
\]
Each counted interior root is simple. At a horizontal root \((u,t)\), the two Jacobian eigenvalues are \((1-u^2)H_t'(u)\) and \(-2tQ_0(u,t)\), where \(Q_0(x,y)=x+\lambda y+cx^2+dxy+ey^2\). At a vertical root \((s,u)\), they are \((1-u^2)V_s'(u)\) and \(-2sP_0(s,u)\), with \(P_0(x,y)=\lambda x-y+ax^2+bxy-ay^2\). Exact polynomial resultants of the edge quadratic with the transverse factor are, in the order \(H_+,H_-,V_+,V_-\),
\[
 -131,\quad23,\quad\frac{1669}{8},\quad-\frac{415}{8},
\]
all nonzero. The corner eigenvalue pairs at \((1,1),(1,-1),(-1,1),(-1,-1)\) are, respectively, \((-4,-11),(-2,5),(-8,-7),(2,1)\). Thus **all eleven** equilibria are hyperbolic. The inequalities defining the maximal chamber are strict, and hyperbolicity persists under sufficiently small parameter perturbations, proving nonempty open realization.

## Verification

`CHECK.py` is a standalone Python standard-library exact-rational checker. It computes each open-edge root count with inward endpoint signs (so endpoint roots are excluded), certifies the eight rational witnesses, checks \(17{,}998\) additional rational parameter tuples, compares the two-root inequalities against \(1{,}330\) rational quadratic triples, and exactly evaluates the four transverse resultants and four corner eigenvalue pairs at the eleven-equilibrium witness. These are finite cross-checks of the preceding all-real-parameter proof, not a substitute for it. Run `python3 CHECK.py` from the package directory.

## Relationship to prior work

Grau and Szántó [1, Eq. (3), Theorems 1--4] introduced this exact six-parameter invariant-square family and derived center/focus conditions and an open parameter set with at least five small-amplitude cycles **inside** the square. Those statements neither bound nor classify equilibrium points **on the four edges**. The present theorem addresses the different, natural boundary-equilibrium invariant and supplies its exact cardinality spectrum and maximal semialgebraic chamber. Llibre and Rodrígues [2] consider periodic-orbit existence for polynomial fields with invariant lines, not this exact boundary stationary-point census. The assertion of scientific novelty is limited to the checked material; an unindexed equivalent parametrization could give prior coverage. In particular, the eleven-equilibrium witness is **not** asserted to lie in the parameter region producing five interior cycles.

## Limitations

The result is exact for the printed six-parameter family but is not an upper bound for arbitrary quartic plane vector fields with an invariant square. It classifies the set of equilibria *on* the square boundary, not equilibria elsewhere, limit-cycle counts, separatrix connections, or global topological phase portraits. Repeated interior roots are counted as one distinct equilibrium. The sharp hyperbolicity assertion is existence on a nonempty open chamber, not that every eleven-equilibrium parameter tuple must be hyperbolic. No independent mathematical audit has been performed.

## References

[1] M. Grau and I. Szántó, “A Polynomial System of Degree Four with an Invariant Square Containing At Least Five Limit Cycles,” *Qualitative Theory of Dynamical Systems* **23**, article 247 (first publicly online 2024-07-26), DOI: `10.1007/s12346-024-01106-9`, https://link.springer.com/article/10.1007/s12346-024-01106-9 . Full open-access article, especially Eq. (3) and Theorems 1–4, inspected.

[2] J. Llibre and A. Rodrígues, “Periodic orbits for real planar polynomial vector fields of degree n having n invariant straight lines taking into account their multiplicities,” *Electronic Journal of Qualitative Theory of Differential Equations* **2015**(55), 1–15. DOI: `10.14232/ejqtde.2015.1.55`. Its periodic-orbit focus does not provide the stated edge-root classification.
