# Conductor multidegrees and parity of the Pfister–Schönemann curve germs

## Finding

For each integer \(m\ge4\), put
\[
 A_m=\mathbb C\{x,y,z\}/(f,g_m),\qquad
 f=xy+z^3,\qquad g_m=xz+yz^2+y^m.
\]
Let \(\widetilde A_m\) be its normalization, \(\mathfrak c_m=\{a\in A_m:a\widetilde A_m\subset A_m\}\) its conductor, and \(\delta_m=\dim_{\mathbb C}(\widetilde A_m/A_m)\). With a local normalization parameter on each branch, \(\mathfrak c_m\) is the product of the indicated principal branch ideals, where the tuples list their exponents:
\[
 (c_i)=\begin{cases}
 (2,3,3,m+2),&m\text{ even},\\
 (2,3,3,(m+3)/2,(m+3)/2),&m\text{ odd}.
 \end{cases}
\]
Thus the number \(r_m\) of branches is \(4\) or \(5\), respectively, and
\[
 \delta_m=\begin{cases}(m+10)/2,&m\text{ even},\\(m+11)/2,&m\text{ odd}.\end{cases}
\]
The change in branch count and conductor partition is controlled by the parity of \(m-3\).

## Assumptions and scope

All analytic germs and power series are over \(\mathbb C\). The hypotheses are \(m\in\mathbb Z\) and \(m\ge4\). The quoted defining equations give a reduced one-dimensional isolated complete intersection (the established Pfister–Schönemann family). All branch orders refer to a uniformizing parameter in the completed or convergent normalization; their values agree. The conductor exponents are the valuations of the extended conductor ideal on its separate branches, not the orders of a single generator in \(A_m\).

## Proof

**1. All branches.** On a branch not contained in \(y=0\), eliminate \(x=-z^3/y\). The second equation becomes
\[
 z^4-y^2z^2-y^{m+1}=0.
\]
The integral element \(u=z/y\) satisfies
\[
 u^4-u^2=y^{m-3}.
\]
Writing \(e=m-3\), the two solutions for \(w=u^2\) are \(w_+=(1+\sqrt{1+4y^e})/2\) and \(w_-=(1-\sqrt{1+4y^e})/2\). The first is a unit with constant term one and gives two smooth branches \(u=\pm\sqrt{w_+}\), parametrized by \(y=t\). On them \((\operatorname{ord}x,\operatorname{ord}y,\operatorname{ord}z)=(2,1,1)\).

For \(w_-=-y^e+O(y^{2e})\), if \(e\) is even (equivalently \(m\) odd), there are two further smooth branches, \(y=t\), \(u=\pm i t^{e/2}(1+O(t^e))\). Their valuation triples are \(((3m-5)/2,1,(m-1)/2)\). If \(e\) is odd (\(m\) even), the two square-root signs are interchanged by \(t\mapsto-t\) after setting \(y=t^2\): they are one analytically irreducible branch, with \(u=i t^e(1+O(t^{2e}))\) and valuations \((3m-5,2,m-1)\). Since \(\gcd(2,m-1)=1\), this \(t\) is a primitive normalization parameter. The locus \(y=0\) contributes exactly the smooth \(x\)-axis branch \((x,y,z)=(t,0,0)\), by the two defining equations. This exhausts the branches.

**2. Differential orders and conductor.** As \(A_m\) is a one-dimensional complete intersection, its dualizing module is free on the Poincaré residue \(\omega\). For \(J_{xz}=f_x(g_m)_z-f_z(g_m)_x\), the equations give
\[
 \omega=\frac{dy}{J_{xz}},\qquad
 J_{xz}=2z(y^2-2z^2)
\]
on the non-axis branches. On each of the two outer branches \(y=t\), \(z=\pm t+O(t^2)\), so \(\operatorname{ord}_t\omega=-3\). On the inner branch or branches, \(z/y\to0\), so \(\operatorname{ord}_t J_{xz}=\operatorname{ord}_t z+2\operatorname{ord}_t y\). Thus \(\operatorname{ord}_t\omega=-(m+2)\) in the even case and \(-(m+3)/2\) on each of the two inner branches in the odd case.

On the axis take the equivalent residue \(\omega=dx/J_{yz}\), where \(J_{yz}=f_y(g_m)_z-f_z(g_m)_y\). Restriction to \((x,y,z)=(t,0,0)\) gives \(J_{yz}=t^2\), hence \(\operatorname{ord}_t\omega=-2\).

For any reduced Gorenstein curve germ, finite-normalization duality identifies \(\nu_*\omega_{\widetilde A_m}=\operatorname{Hom}_{A_m}(\widetilde A_m,\omega_{A_m})=\mathfrak c_m\omega_{A_m}\). On a normalized disk the canonical module is \(\mathbb C\{t\}dt\); if \(\omega\) has order \(-c\), the extended conductor is exactly \(t^c\mathbb C\{t\}\). Applying this to the orders above yields the asserted complete conductor tuples.

**3. Delta-invariant.** The Gorenstein conductor-length identity gives \(\operatorname{length}(\widetilde A_m/\mathfrak c_m)=2\delta_m\). Summing the calculated branch exponents yields \(m+10\) for even \(m\) and \(m+11\) for odd \(m\), proving the delta formulas. As a separate consistency check, the known Milnor number \(\mu_m=m+7\) satisfies \(\mu_m=2\delta_m-r_m+1\) in both parity classes.

## Verification

The included standalone Python program `verify.py` checks the valuation balances and conductor identities across \(4\le m\le 100\), both parity cases, and the Milnor–delta relation. These finite calculations corroborate, but cannot establish, the unrestricted analytic proof. The proof of the result rests on Hensel factorization and normalization duality, as detailed above.

## Relationship to prior work

Pfister and Schönemann introduced the nonquasihomogeneous complete-intersection curve family and studied its differential complexes and Milnor–Tjurina invariants (1989). He and Wang study the same analytic family in their revised work on derived Hodge-to-de Rham degeneration (arXiv:2604.05825, revision of November 4, 2026), including a projective pinching construction whose proof introduces branchwise conductor exponents but uses their aggregate length. Their Proposition C.7 states \(\mu_m=m+7\) and \(\tau_m=m+6\), and the relation \(\sum_i(c_i-1)=m+6\); these do not by themselves determine the individual conductor exponents or branch count. The present result supplies the branchwise conductor divisor and explicit parity dependence, which specify the jet orders needed for local normalization and pinching calculations. The general duality and conductor-length identities used in the proof are standard and are not claimed as new.

## Limitations

The statement concerns only the stated complex-analytic complete-intersection family. It does not compute global moduli, classify all Wall singularity types, or assert new spectral-sequence degeneration results. Priority for the explicit conductor partitions remains subject to further investigation of historical singularity tables and hard-to-search older sources. Independent mathematical validation has not been performed.

## References

- G. Pfister and H. Schönemann, *Singularities with exact Poincaré complex but not quasihomogeneous*, Revista Matemática Complutense 2 (1989), 161–173. DOI: 10.5209/rev_REMA.1989.v2.n2.18111.
- Y. He and J. Wang, *Derived Hodge-to-de Rham Degeneration and Quasihomogeneous Curve Singularities*, arXiv:2604.05825, revised November 4, 2026, especially Proposition C.7 and its proof. The original preprint under a different title first appeared April 7, 2026.
- R.-O. Buchweitz and G.-M. Greuel, *The Milnor number and deformations of complex curve singularities*, Inventiones Mathematicae 58 (1980), 241–281.
- Standard dualizing-module description for one-dimensional complete intersections and the Gorenstein conductor-length formula.
