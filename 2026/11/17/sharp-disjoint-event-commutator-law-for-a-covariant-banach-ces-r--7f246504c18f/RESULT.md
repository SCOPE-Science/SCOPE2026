# Sharp disjoint-event commutator law for a covariant Banach–Cesàro operator measure

## Finding

Let \(\mu\) be the normalized covariant finitely additive positive operator-valued measure obtained from the two-frequency-block construction specified below. For any two **disjoint measurable events** \(E,F\subset\mathbb R\), let \(a,b\) be their scalar Banach–Cesàro densities, and put \(c=1-a-b\). Set \(r(s)=\sin(\pi s)/\pi\), and let \(u\le v\le w\) be the increasing rearrangement of \(a,b,c\). The exact, attained fixed-density commutator optimum is

\[
\boxed{\sup_{E\cap F=\varnothing\atop \mathrm{dens}(E)=a,\ \mathrm{dens}(F)=b}
\|[\mu(E),\mu(F)]\|=2\varepsilon^2\,\mathcal D(a,b,c),}
\]
where
\[
\mathcal D(a,b,c)=
\begin{cases}
\displaystyle\frac{\sin(\pi u)\sin(\pi v)}{\pi^2},&w\ge\frac12,\\[5pt]
\displaystyle\frac{\sin(\pi a)\sin(\pi b)\sin(\pi c)}{\pi^2},&w\le\frac12.
\end{cases}
\]
The two expressions agree at \(w=1/2\); a vanishing density gives zero. In the strict regime \(w<1/2\), every maximizing **periodic** three-color partition consists, up to null sets and rotation or reversal, of three successive arcs. In the strict regime \(w>1/2\), the two smaller-density colors must be circular arcs with first Fourier moments perpendicular, and the third color is their complement. In both regimes these constructions attain the maximum, not merely its limit.

The unrestricted sharp value over all disjoint event pairs is
\[
\boxed{\sup_{E\cap F=\varnothing}\|[\mu(E),\mu(F)]\|=
\frac{3\sqrt3}{4\pi^2}\,\varepsilon^2,}
\]
attained when \(E,F\) and their complement are three consecutive equal-length circular arcs, lifted periodically to \(\mathbb R\). The maximizing density triple is uniquely \((1/3,1/3,1/3)\).

## Assumptions and scope

Work on the complex Hilbert space \(H=L^2(\mathbb R)\). Let \(S_t f(y)=f(y+t)\). In the Fourier representation, let \(P_0,P_1\) be the spectral projections onto \([0,1]\) and \([1,2]\), and let \(V=M_{e^{iy}}P_0\). Then \(V^*V=P_0\), \(VV^*=P_1\), \(V^2=(V^*)^2=0\), and \(S_t^*VS_t=e^{-it}V\). Fix \(0<\varepsilon<1/2\), and define the positive bounded operator \(T=I+\varepsilon(V+V^*)\). For Lebesgue measurable \(E\subset\mathbb R\), put
\[
m_T(E)=\int_E S_x^*TS_x\,dx,\qquad
\mu(E)=\mathrm{WOT}\!\!-\!\lim_{R\to\mathcal U}\frac{m_T(E\cap[-R,R])}{2R},
\]
where \(\mathcal U\) is any free ultrafilter tending to positive infinity and the limit is weak-operator. The underlying positive operator-valued measure is normalized: \(\mu(\mathbb R)=I\). Its scalar density, the coefficient of the identity, is
\[
\mathrm{dens}(E)=\lim_{R\to\mathcal U}\frac{|E\cap[-R,R]|}{2R}\in[0,1].
\]
Every supremum fixes \(\varepsilon\) and \(\mathcal U\) and ranges over **Lebesgue measurable disjoint events** of the stated scalar densities. The bound is the same for every admissible \(\mathcal U\); all witnesses are ordinary periodic measurable sets, independent of \(\mathcal U\).

## Proof

**Fourier reduction.** Write
\[
z(E)=\lim_{R\to\mathcal U}\frac{1}{2R}\int_{E\cap[-R,R]}e^{-ix}\,dx.
\]
The explicit operator density gives \(\mu(E)=aI+\varepsilon(z(E)V+\overline{z(E)}V^*)\). For disjoint \(E,F\), setting \(C=\mathbb R\setminus(E\cup F)\), finite additivity and the vanishing mean of \(e^{-ix}\) imply
\[
a+b+c=1,\qquad z(E)+z(F)+z(C)=0.
\]
Using the relations for \(V\), one obtains the exact normalization
\[
[\mu(E),\mu(F)]
=2i\varepsilon^2\operatorname{Im}(z(E)\overline{z(F)})(P_1-P_0),
\]
so its norm is \(2\varepsilon^2|\operatorname{Im}(z(E)\overline{z(F)})|\).

**Individual moment cap.** Every measurable event of density \(s\) obeys \(|z(E)|\le r(s)\). Indeed, on \([-R,R]\) separate complete \(2\pi\)-periods from at most two partial periods. Folding the event to the circle gives a function taking values between zero and one. Among such functions with given integral, the first complex Fourier coefficient has maximal modulus for the indicator of a single centered arc (the elementary bathtub inequality for cosine), and that modulus is \(\sin(\pi s)/\pi\). The partial-period contribution is \(O(R^{-1})\) after normalization. Pass to the ultralimit, using continuity of \(r\). For a periodic event of density \(s\in(0,1)\), equality holds precisely for a single arc modulo a null set.

**Three-side area bound.** Denote the three Fourier coefficients by \(z_1,z_2,z_3\). Their sum is zero. Writing \(x=|z_1|^2\), \(y=|z_2|^2\), \(z=|z_3|^2\), the real Gram matrix
\[
G(x,y,z)=\begin{pmatrix}x&(z-x-y)/2\\(z-x-y)/2&y\end{pmatrix}
\]
is positive semidefinite and
\[
D:=|\operatorname{Im}(z_1\overline{z_2})|=\sqrt{\det G(x,y,z)}.
\]
If \(w\ge1/2\), take the two colors with smaller masses \(u,v\). Cyclic area invariance under \(z_1+z_2+z_3=0\) and the moment caps give \(D\le r(u)r(v)\). Since \(u+v\le1/2\), two arcs of lengths \(2\pi u\), \(2\pi v\) with centers separated by \(\pi/2\) are disjoint. Their Fourier moments are perpendicular, and the third color is the complement, so the bound is attained.

Suppose now \(\max\{a,b,c\}<1/2\). Put \(X_i=r(a_i)^2\) for \((a_1,a_2,a_3)=(a,b,c)\), and \(D_0=\sin(\pi a)\sin(\pi b)\sin(\pi c)/\pi^2\). The three lengths \(\sqrt{X_i}\) form an **acute triangle**: by the sine rule its angles are \(\pi a_i\), all below \(\pi/2\). Thus \(G(X_1,X_2,X_3)\) is positive definite and \(D_0=\sqrt{\det G(X_1,X_2,X_3)}\). The function \(G\mapsto\sqrt{\det G}\) is concave and homogeneous of degree one on positive semidefinite real \(2\)-by-\(2\) matrices. One direct proof is to conjugate two positive definite matrices until one is the identity and use \((1+\lambda_1)(1+\lambda_2)\ge(1+\sqrt{\lambda_1\lambda_2})^2\), followed by homogeneity and continuity. The supporting-plane inequality therefore yields
\[
D\le\sum_{i=1}^3\frac{X_j+X_k-X_i}{4D_0}\,|z_i|^2
\le\sum_{i=1}^3\frac{X_j+X_k-X_i}{4D_0}\,X_i=D_0,
\]
where \(\{i,j,k\}=\{1,2,3\}\). Each coefficient is strictly positive because the cap triangle is acute. Three consecutive arcs with respective proportions \(a,b,c\) give Fourier magnitudes \(r(a),r(b),r(c)\), and the first two phases differ by \(\pi(a+b)\), hence their determinant is \(r(a)r(b)\sin(\pi c)=D_0\). Sharpness and periodic rigidity follow from the positive supporting-plane coefficients and the equality cases of the individual Fourier cap. Continuity handles the boundary \(w=1/2\) and zero masses.

**Global optimization.** For \(w\ge1/2\), concavity of \(\log\sin\) gives \(\sin(\pi u)\sin(\pi v)\le\sin^2(\pi(u+v)/2)\le1/2\), so \(D\le1/(2\pi^2)\). For \(w<1/2\), the same strict concavity with \(a+b+c=1\) gives \(D\le\sin^3(\pi/3)/\pi^2=3\sqrt3/(8\pi^2)\), attained only at equal thirds. Since \(3\sqrt3/8>1/2\), the stated unrestricted maximum and density rigidity follow.

## Verification

The independent-of-ultrafilter Fourier reduction and normalization are symbolic consequences of the two-block density. The attached standalone `verify.py` reconstructs exact circular-cell Fourier integrals and tests the piecewise bound on \(5{,}000\) randomized three-color circle partitions, separately checks arc attainment, tests the Gram supporting plane, and checks the commutator coefficient directly with \(2\)-by-\(2\) matrices. Its recorded successful output is: `PASS: 12316 finite checks; global sharp determinant=0.065810039231830`. The proof above establishes the infinite family; finite tests do not certify arbitrary measurable sets or ultrafilters.

## Relationship to prior work

Dzhenzher, *Banach–Cesàro positive operator-valued measure*, arXiv:2610.33821v1 (24 October 2026), constructs precisely this noncommutative two-band covariant measure (Example 2.5) and computes a nonzero commutator for the **overlapping** half-circle events defined by positive cosine and sine. That paper does not state the fixed-density **disjoint-event** optimization, the three-density threshold at \(1/2\), or the globally sharp equal-third value. Pellonpää's earlier work describes Fourier-matrix representations of countably additive covariant phase observables; its inspected formulas and structural results do not directly imply the sharp three-color area inequality. Both the classical Fourier arc inequality and concavity of \(\sqrt{\det}\) are acknowledged as ingredients, not claimed new.

## Limitations

The theorem concerns the stated two-band covariant operator-valued measure, not arbitrary positive operator-valued measures or arbitrary higher-frequency matrix kernels. The uniqueness statement is for the maximizing density triple; geometric characterizations of maximizing event sets are asserted only for periodic event partitions. A fully independent literature and mathematical audit has not been carried out. Related older circular Fourier partition inequalities or equivalent qubit-phase formulations could reduce the originality of the sharp area law.

## References

1. S. V. Dzhenzher, *Banach–Cesàro positive operator-valued measure*, arXiv:2610.33821v1, 24 October 2026, https://arxiv.org/html/2610.33821 . Relevant material: Example 2.5, Section 2.
2. J.-P. Pellonpää, *On the structure of covariant phase observables*, arXiv:quant-ph/0108105v2, https://arxiv.org/pdf/quant-ph/0108105 . Relevant material: Section 2, Equation (1), and Sections 4–5.
3. J.-P. Pellonpää, *Covariant phase observables*, Fortschritte der Physik 51 (2003), 207–210, https://doi.org/10.1002/prop.200310028 . Context for phase-observable covariance; full text not used to exclude overlap.
