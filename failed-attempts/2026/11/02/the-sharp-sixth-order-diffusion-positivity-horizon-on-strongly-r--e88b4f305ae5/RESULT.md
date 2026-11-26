# The sharp sixth-order diffusion positivity horizon on strongly regular graphs

## Finding

Let \(G\) be a connected, noncomplete, simple strongly regular graph with parameters \((v,k,\lambda,\mu)\), where \(\mu>0\), and let every graph edge have the same conductance \(c>0\). For the weighted combinatorial Laplacian \(L=c(kI-A)\), consider the three-stage Gauss–Legendre (diagonal \([3/3]\) Padé) diffusion end-step
\[
P(h)=r(hL),\qquad
r(z)=\frac{120-60z+12z^2-z^3}{120+60z+12z^2+z^3},\qquad h\ge0.
\]
Write the two distinct positive eigenvalues of \(kI-A\) as \(0<a<b\), with multiplicities \(f\) and \(g\). Then **every off-diagonal entry of \(P(h)\) is strictly positive for every finite \(h>0\)**, and every diagonal entry is equal to a strictly decreasing function of \(h\). There is a unique finite number \(H>0\) such that
\[
P(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le h\le H.
\]
Precisely, \(H=z_*/c\), where \(z_*>0\) is the unique positive solution of
\[
1+f\,r(az_*)+g\,r(bz_*)=0.
\]
At \(h=H\), **all diagonal entries vanish and all off-diagonal entries remain strictly positive**. For \(h>H\), all diagonal entries are negative; there are no re-entrant positivity windows.

Equivalently, \(z_*\) is the unique positive zero of the explicit degree-six polynomial
\[
F(z)=D(az)D(bz)+fN(az)D(bz)+gN(bz)D(az),
\]
where \(D(t)=120+60t+12t^2+t^3\), \(N(t)=120-60t+12t^2-t^3\). All denominators are strictly positive for nonnegative arguments.

## Assumptions and scope

Here strongly regular means that \(G\) has \(v\) vertices, degree \(k\) at every vertex, and exactly \(\lambda\) or \(\mu\) common neighbors for respectively adjacent or distinct nonadjacent vertex pairs. Assume connected, noncomplete, simple, and \(\mu>0\); in particular \(v\ge4\). The graph is fixed; its edge conductances are uniform, not optimization variables. Matrix entrywise nonnegativity is tested for all nonnegative initial vectors, with \(h=0\) included.

The spectral parameters can be computed directly from the graph parameters:
\[
\begin{aligned}
S&=2k-\lambda+\mu,\\
T&=\sqrt{(\lambda-\mu)^2+4(k-\mu)},\\
a&=(S-T)/2,\qquad b=(S+T)/2,\\
f&=\frac{b(v-1)-vk}{b-a},\qquad
 g=\frac{vk-a(v-1)}{b-a}.
\end{aligned}
\]
For these graphs \(a,b,f,g\) are positive and \(f+g=v-1\). The positive roots \(a,b\) may be irrational. The dimensionless timestep is \(z=ch\).

## Proof

**1. Resolvent-free spectral interpolation.** Let \(\bar L=kI-A\), \(J\) be the all-ones matrix, and \(E_0=J/v\). Strong regularity gives exactly the three Laplacian eigenspaces with projectors
\[
E_a=\frac{b(I-E_0)-\bar L}{b-a},\qquad
E_b=\frac{\bar L-a(I-E_0)}{b-a}.
\]
Therefore
\[
P(h)=E_0+r(az)E_a+r(bz)E_b,
\quad z=ch.
\]
The projectors have constant diagonals \((E_a)_{ii}=f/v\), \((E_b)_{ii}=g/v\). For distinct nonadjacent vertices \(i,j\), since \(\bar L_{ij}=0\),
\[
P_{ij}(h)=\frac{(b-a)-b\,r(az)+a\,r(bz)}{v(b-a)}.
\]
For adjacent vertices, \(\bar L_{ij}=-1\), so
\[
P_{ij}(h)=\frac{(b-a)-b\,r(az)+a\,r(bz)}{v(b-a)}
+\frac{r(az)-r(bz)}{b-a}.
\]

**2. Strict positivity of both off-diagonal classes.** Define the positive scalar function \(q(t)=(1-r(t))/t\) for \(t>0\). Direct differentiation (with \(D\) as above) gives
\[
r'(t)=-\frac{24(t^4-30t^2+600)}{D(t)^2}<0,
\qquad q(t)=\frac{2(t^2+60)}{D(t)},
\]
\[
q'(t)=-\frac{2(t^4+120t^2+1200t+3600)}{D(t)^2}<0
\quad(t\ge0),
\]
where \(t^4-30t^2+600=(t^2-15)^2+375>0\). Since \(0<a<b\), both \(r(az)-r(bz)\) and \(q(az)-q(bz)\) are strictly positive for every \(z>0\). The nonedge entry rearranges exactly to
\[
P_{ij}(h)=\frac{abz}{v(b-a)}\bigl(q(az)-q(bz)\bigr)>0.
\]
Every edge entry is strictly larger by \((r(az)-r(bz))/(b-a)>0\). The argument requires no sign approximation, graph enumeration, or uniformity of eigenvalue multiplicities.

**3. Exact single diagonal crossing.** Every diagonal entry is
\[
d(z)=\frac{1+f\,r(az)+g\,r(bz)}v.
\]
Because \(f,g,a,b>0\) and \(r'<0\), \(d'(z)<0\) for all \(z\ge0\). At \(z=0\), \(d(0)=1\). As \(z\to\infty\), \(r(az),r(bz)\to-1\), hence \(d(z)\to(2-v)/v<0\). Continuity and strict monotonicity provide exactly one positive crossing \(z_*\); clearing strictly positive denominators yields \(F(z_*)=0\). Symmetry and \(r(0)=1\) give \(P(h)\mathbf 1=\mathbf 1\) for every \(h\), so entrywise nonnegativity is exactly the stochastic-positivity condition. Parts 2 and 3 prove the stated interval and strict post-threshold sign pattern.

**4. Useful spectral bounds.** For each fixed integer \(v\ge4\), let \(\rho_v>0\) be the unique root of \(r(\rho_v)=-1/(v-1)\). The diagonal expression is a positive weighted average of \(r(az)\) and \(r(bz)\). Thus
\[
\frac{\rho_v}{bc}\le H\le\frac{\rho_v}{ac}.
\]
These bounds, unlike the defining scalar root, require only the extremes of the nonzero spectrum.

## Verification

The included standard-library Python program `verify.py` computes the matrix rational function directly with exact rational Gaussian elimination, independently compares each entry to the projector formula, checks row sums and strict off-diagonal signs, and brackets the unique diagonal root with exact rational arithmetic. Six connected noncomplete integral-spectrum examples are covered: the four-cycle, \(K_{3,3}\), Petersen graph, \(3\times3\) and \(4\times4\) rook graphs, and triangular graph \(T(5)\). It also checks the three rational-derivative identities and one fourth-order comparison identity exactly.

Successful replay reports 4 symbolic identities, 2,945 full-matrix entries, 2,670 strict off-diagonal comparisons, 275 stochastic rows, and 6 exact root brackets. These finite tests are **not** used to infer the theorem for untested or infinite graph families: that follows from the analytic proof above.

For unit conductance, the Petersen graph has \(v=10\), \((a,b)=(2,5)\), \((f,g)=(5,4)\), and \(H\approx3.12731503346\). The four-cycle has \((a,b)=(2,4)\), \((f,g)=(2,1)\), and \(H\approx8.60919950864\). Both values are numerical displays of uniquely defined exact algebraic roots.

## Relationship to prior work

The sixth-order method is a classical three-stage Gauss–Legendre collocation method, and general positivity/absolute-monotonicity methods for Runge–Kutta discretizations predate this result. Wade, Khaliq, Siddique and Yousuf (first public online 2004) studied Padé-based positivity-preserving smoothing, while Horváth, Song and Terlaky (2014 preprint/2015 publication) developed general rational-discretization invariance thresholds. The latter supplies sufficient general-purpose criteria, not the sharp graph-family formula or permanent strict off-diagonal sign result proved here.

A direct fourth-order \([2/2]\) comparison reveals a different positivity mechanism: on the Petersen graph an **edge** entry at dimensionless step \(z=4\) is \(-36/4123\), while on the four-cycle all entries stay nonnegative for every fourth-order step. The sixth-order scheme has the opposite, universal structure over strongly regular graphs: off-diagonal entries are always positive and the diagonal always crosses at a finite step. In particular, the four-cycle is unconditionally positivity-preserving for \([2/2]\) but not for \([3/3]\). A previously derived general \([3/3]\) complete-bipartite classification supplies overlapping special cases, such as \(K_{m,m}\), but does not include primitive strongly regular families (e.g. Petersen, triangular and rook graphs). Those overlapping cases are not asserted as new.

For completeness, fourth-order positivity on the four-cycle follows directly from its \(0,2,2,4\) spectrum and the rational function \(r_{22}(t)=(12-6t+t^2)/(12+6t+t^2)\). Its diagonal is strictly positive since \(r_{22}(t)>0\); its edge entry is \((1-r_{22}(4z))/4>0\); and its opposite-vertex entry is \((1-2r_{22}(2z)+r_{22}(4z))/4=z^2(z+1)/(D_{22}(2z)D_{22}(4z))>0\), where \(D_{22}(t)=1+t/2+t^2/12\).

## Limitations

The theorem concerns **only** the end-step update, not positivity of intermediate Gauss–Legendre stages or stability under repeated floating-point implementation. Uniform edge conductance and a connected, noncomplete, simple strongly regular graph are essential assumptions of the stated proof. It does not classify general irregular graphs, directed Markov generators, weighted arbitrary graphs, or all higher diagonal Padé orders. The scalar root is an exact specification, not generally a simple radical expression. Special-case prior coverage (notably complete bipartite graphs) is explicitly excluded from the novelty claim; a possibility of specialized earlier strongly regular graph treatment remains a historical originality risk. The 2004 Padé smoothing paper's complete text was not accessible in the consulted sources.

## References

1. B. A. Wade, A. Q. M. Khaliq, M. Siddique, M. Yousuf, *Smoothing with positivity-preserving Padé schemes for parabolic problems with nonsmooth data*, Numerical Methods for Partial Differential Equations **21** (2005), 553–573; first online September 29, 2004. https://doi.org/10.1002/num.20039
2. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics **53** (2005), 341–356. https://doi.org/10.1016/j.apnum.2004.08.026
3. Z. Horváth, Y. Song, T. Terlaky, *Steplength thresholds for invariance preserving of discretization methods of dynamical systems on a polyhedron*, Discrete and Continuous Dynamical Systems **35** (2015), 2997–3013; authorized preprint: https://engineering.lehigh.edu/sites/engineering.lehigh.edu/files/_DEPARTMENTS/ise/pdf/tech-papers/14/14T_007.pdf ; DOI: https://doi.org/10.3934/dcds.2015.35.2997
4. M. N. Spijker, *Stepsize conditions for general monotonicity in numerical initial value problems*, SIAM Journal on Numerical Analysis **45** (2007), 1222–1245. https://doi.org/10.1137/060661739
