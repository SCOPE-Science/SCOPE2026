# Strict habitat-occupancy gain from mirror-specialized competing colonizers

## Finding

For every \(a,b>0\) and \(0<d<D\), consider two competitors with equal colonization matrix \(C=\begin{pmatrix}a&b\\b&a\end{pmatrix}\) but opposite habitat preferences. Define \(R=\rho(\operatorname{diag}(d,D)^{-1}C)\). If \(R>1\), then there is a strictly positive mirror-symmetric coexistence equilibrium, locally exponentially attracting among all four habitat/species coordinates. Its **total occupied habitat capacity** exceeds that of either monospecific positive equilibrium *strictly*:
\[
Q=2(1-R^{-1})>P=h+\ell.
\]
An exact witness is \((a,b,d,D)=(2,2,1,3)\), for which the mirror coexistence equilibrium is \((u_1,u_2,v_1,v_2)=(15/32,5/32,5/32,15/32)\), giving \(Q=5/4\). The monospecific equilibrium has \(P=\sqrt5/2\), so the occupancy advantage equals \((5-2\sqrt5)/4>0\). The strict all-parameter comparison quantifies complementarity of opposite habitat specialists even though they preempt each other's vacant sites.

## Assumptions and scope

There are two habitat types, each with unit available capacity, and exactly two competing colonizers. Let \(u_i,v_i\) be the occupancy fractions of species \(u,v\) on habitat \(i\). Invariance holds on \(\{u_i,v_i\ge0,\ u_i+v_i\le1:\ i=1,2\}\). Colonization does not displace occupied patches. Colonization coupling is identical for both species, positive, and symmetric, with self-habitat rate \(a>0\) and cross-habitat rate \(b>0\). Extinction is \((d,D)\) for \(u\) and \((D,d)\) for \(v\), where \(0<d<D\). Explicitly,
\[
\begin{aligned}
\dot u_1&=-d u_1+(1-u_1-v_1)(a u_1+b u_2),\\
\dot u_2&=-D u_2+(1-u_2-v_2)(b u_1+a u_2),\\
\dot v_1&=-D v_1+(1-u_1-v_1)(a v_1+b v_2),\\
\dot v_2&=-d v_2+(1-u_2-v_2)(b v_1+a v_2).
\end{aligned}
\]
The assumption \(R>1\) is the standard monomorphic growth viability condition. 'Total occupancy' is the sum of occupied fractions across two unit-capacity habitats, hence ranges from zero to two. Local exponential attraction means within the full four-dimensional physical state space, not global attraction. When \(d=D\), the strict claim does not apply.

## Proof

**Existence and explicit mirror equilibrium.** Put \(B=\operatorname{diag}(d,D)^{-1}C\). It is strictly positive, with Perron root \(R>1\) and a unique positive eigenvector direction \((x,y)\). Normalize this direction so that \(x+y=1-R^{-1}\), and let \(w=R^{-1}\). Then \(wC(x,y)^\mathsf T=\operatorname{diag}(d,D)(x,y)^\mathsf T\). The state \((u_1,u_2,v_1,v_2)=(x,y,y,x)\) has free fractions \(w\) in both habitats and hence solves all four equations; it is strictly interior. From the two component eigenvector equations, \(d=w(a+b y/x)\) and \(D=w(a+b x/y)\). As \(d<D\) this forces \(x>y>0\). Its total occupied capacity is \(Q=2(x+y)=2(1-R^{-1})\).

**Monospecific comparison.** Set \(v_1=v_2=0\). Standard irreducible cooperative, strongly sublinear patch-colonization dynamics have a unique positive equilibrium \((h,\ell)\in(0,1)^2\) if and only if \(R>1\); this is also the monomorphic theorem of Lajmanovich–Yorke, quoted as Theorem 3.1 in [1]. Its equations are
\[
dh=(1-h)(ah+b\ell),\qquad D\ell=(1-\ell)(bh+a\ell).
\]
They force \(h>\ell>0\): if \(h\le\ell\) then \(d=(1-h)(a+b\ell/h)\ge(1-\ell)(a+bh/\ell)=D\), contrary to \(d<D\). Let \(w_0=1-(h+\ell)/2>0\). Taking the dot product of the monoculture equations with \((h/(1-h),\ell/(1-\ell))\) in their elementary rearranged form yields
\[
(h,\ell)C(h,\ell)^\mathsf T=\frac{dh^2}{1-h}+\frac{D\ell^2}{1-\ell}.
\]
The difference from the constant-free-fraction comparison is exactly
\[
\begin{aligned}
&(h,\ell)C(h,\ell)^\mathsf T-\frac{dh^2+D\ell^2}{w_0}\\
&=\frac{h-\ell}{2w_0}\left[\frac{dh^2}{1-h}-\frac{D\ell^2}{1-\ell}\right]
=\frac{a(h-\ell)^2(h+\ell)}{2w_0}>0.
\end{aligned}
\]
Since \(C\) is symmetric and \(\operatorname{diag}(d,D)\) is positive definite,
\[
R=\max_{z\ne0}\frac{z^\mathsf T C z}{dz_1^2+Dz_2^2}.
\]
Testing \(z=(h,\ell)\) and using the strict gap gives \(R>1/w_0\). Therefore \(1-1/R>1-w_0=(h+\ell)/2\), proving \(Q>P\). The mirrored monoculture has identical total occupancy by exchange of habitat labels.

**Full local exponential attraction.** Write \(F=ax+by\), \(G=bx+ay\), and \(w=1-x-y\). At the mirror coexistence point, linearize the four-dimensional system and split it under simultaneous exchange of habitat and species labels. The two real two-by-two Jacobian blocks are
\[
J_+=\begin{pmatrix}aw-d-F&bw-F\\bw-G&aw-D-G\end{pmatrix},\quad
J_-=\begin{pmatrix}aw-d-F&bw+F\\bw+G&aw-D-G\end{pmatrix}.
\]
The equilibrium equations yield \(aw-d=-bw\,y/x<0\) and \(aw-D=-bw\,x/y<0\). Thus both blocks have negative trace. Direct substitution into their determinants yields
\[
\det J_-=\frac{ab w(x-y)^2(x+y)}{xy}>0,
\quad
\det J_+=\frac{bw(x+y)(a x^2+a y^2+2bxy)}{xy}>0.
\]
Both real two-by-two blocks are Hurwitz (negative trace and positive determinant), proving local exponential attraction for every parameter in the stated regime. The strictness of \(\det J_-\) reflects genuine opposing habitat preferences.

**Exact witness.** Take \(a=b=2,d=1,D=3\). Then \(R=8/3\), \(w=3/8\), \(x=15/32\), \(y=5/32\). For a single competitor, \(h=\sqrt5/(1+\sqrt5)\) and \(\ell=\sqrt5/(3+\sqrt5)\), whose sum is \(\sqrt5/2\). All fractions lie in the physical domain, and \(5/4-\sqrt5/2=(5-2\sqrt5)/4>0\).

## Verification

The accompanying script `checker.py` checks the exact symbolic determinant formulas and Rayleigh gap, the rational coexistence equilibrium, the algebraic monoculture benchmark, and local-stability and occupancy inequalities over 158 independently generated viable parameter sets. It reports `PASS symbolic determinant identities, Rayleigh gap, exact example; numerical admissible cases: 158`. The finite checks support, but do not substitute for, the analytic universal proof. Reproduce with Python 3 and the `sympy`, `numpy`, and `scipy` packages using `python checker.py`.

## Relationship to prior work

Costa, Kubasch and Loeuille [1] introduce a continuum two-species patch occupancy model and a two-habitat reduced system. Their Theorems 3.3–3.4 establish persistence under mutual invasibility and existence of a positive coexistence equilibrium; they do not assert this all-parameter strict *total occupancy comparison* with the same-species monocultures, its spectral Rayleigh-gap certificate, or local exponential attraction of this mirrored family. The monomorphic equilibrium theorem is already known from Lajmanovich–Yorke [2] and is used here, not claimed. Leibold and Loeuille [3] analyze species sorting and patch dynamics, and Mouquet and Loreau [4] analyze source-sink occupancy more broadly; their available abstracts do not settle claim-level coverage, so full-text historical priority remains a stated risk. The recent public mathematical record [5] studies a mirror-specialized two-strain **SIS model with host migration between patches** and a conservation constraint; its coexistence and slow-relaxation theorem neither contains the present preemptive colonization occupancy comparison nor directly implies the strict Rayleigh gap. Earlier generic monotone-epidemic theorems also imply the monospecific existence result but not the comparison to a two-species mirror equilibrium.

## Limitations

The theorem concerns equilibria and their local linear/nonlinear stability, not global convergence or uniqueness among all (not necessarily mirror-symmetric) coexistence equilibria. It assumes exactly two equal-capacity habitat classes, mirror-specialized mortality, symmetric strictly positive shared colonization, and preemptive competition. A more general total-occupancy theorem might subsume this special case; two older relevant full texts were not accessible for exhaustive exclusion. No stochastic finite-network survival probability is computed, and the theorem does not prescribe habitat management without ecological calibration. Numerical tests are finite and cannot establish the all-parameter inequalities.

## References

[1] M. Costa, M. Kubasch and N. Loeuille, *Metacommunity persistence on spatially heterogeneous landscapes*, arXiv:2607.11291 (first public 2026-07-13), https://arxiv.org/abs/2607.11291 .

[2] A. Lajmanovich and J. A. Yorke, *A deterministic model for gonorrhea in a nonhomogeneous population*, *Mathematical Biosciences* **28** (1976), 221–236; monomorphic global equilibrium theorem summarized and used in [1, Theorem 3.1].

[3] M. A. Leibold and N. Loeuille, *Species sorting and patch dynamics in harlequin metacommunities affect the relative importance of environment and space*, *Ecology* **96** (2015), https://doi.org/10.1890/14-2354.1 .

[4] N. Mouquet and M. Loreau, *Community Patterns in Source-Sink Metacommunities*, *The American Naturalist* **162** (2003), https://doi.org/10.1086/378857 .

[5] *Mirror-specialized SIS strains: exact coexistence and slow exchange under strong migration*, published-finding corpus mathematical research record, 2026-11-08, https://github.com/published-finding corpus/2026 .
