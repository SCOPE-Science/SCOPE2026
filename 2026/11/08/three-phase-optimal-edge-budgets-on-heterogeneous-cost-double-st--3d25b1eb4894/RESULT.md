# Three-phase optimal edge budgets on heterogeneous-cost double-star networks

## Finding
Let \(D_{a,b}\) be the double star formed by joining two hub vertices, the first with \(a\ge2\) pendant leaves and the second with \(b\ge2\) pendant leaves. Its individual edge conductances are independent nonnegative variables; all \(a\) left edges have price \(\ell^2\), all \(b\) right edges have price \(r^2\), and the bridge has price \(z^2\), where \(\ell,r,z>0\). For any budget \(B>0\), consider maximizing the second eigenvalue \(\lambda_2\) of the corresponding weighted graph Laplacian subject to
\[
\ell^2\sum_{i=1}^{a}w_{Li}+r^2\sum_{j=1}^{b}w_{Rj}+z^2w_0\le B.
\]
Define \(N=a+b+2\), \(S=(b+1)z-a\ell+br\), and
\[
F_L=a\ell^2+br^2+(b+1)z^2+2bzr,\qquad
F_R=a\ell^2+br^2+(a+1)z^2+2az\ell,
\]
\[
F_C=a\ell^2+br^2+(b+1)z^2+2bzr-\frac{S^2}{N}.
\]
The **exact** optimal spectral gap is \(\Lambda=B/F\), with the three phases
\[
 F=\begin{cases}
 F_L,&S<0,\\
 F_C,&0\le S\le Nz,\\
 F_R,&S>Nz.
 \end{cases}
\]
The maximizing edge allocation is **unique**, and in particular is constant within each leaf class. Write \(u\) for the conductance of each left pendant edge, \(v\) for each right pendant edge and \(c\) for the bridge. Their exact values are
\[
(u,v,c)=\begin{cases}
\left(\Lambda,\ \Lambda(1+z/r),\ \Lambda((b+1)z+br)/z\right),&S<0,\\[2pt]
\left(\Lambda(1+\mu/\ell),\ \Lambda(1+(z-\mu)/r),\ \Lambda(a(\ell+\mu)+\mu)/z\right),&0\le S\le Nz,\\[2pt]
\left(\Lambda(1+z/\ell),\ \Lambda,\ \Lambda((a+1)z+a\ell)/z\right),&S>Nz,
\end{cases}
\qquad \mu=S/N.
\]
At the phase boundaries the adjacent formulas agree. The multiplicity of \(\lambda_2\) is \(a\) when \(S\le0\), is \(1\) when \(0<S<Nz\), and is \(b\) when \(S\ge Nz\). The interior one-dimensional Fiedler embedding thus bifurcates into a high-multiplicity leaf mode when the optimal centered geometry reaches either hub.

## Assumptions and scope
All graphs are finite, undirected, with the stated positive price coefficients; the conductances themselves are optimized separately, without an a priori class-symmetry restriction. The source graph has precisely \(a+b+2\) vertices and \(a+b+1\) edges. The graph Laplacian is \(L_{ii}=\sum_{j\sim i}w_{ij}\) and \(L_{ij}=-w_{ij}\) on edges. The statement covers all integers \(a,b\ge2\), all real \(\ell,r,z,B>0\) and both regime boundaries. Edge price, not geometric length, equals the corresponding square \(\ell^2,r^2,z^2\). The positive optimum uses every edge, so its graph remains connected.

## Proof
**(1) A universal upper certificate.** For any centered vectors \(Y_i\) in any Euclidean space with squared distance across each edge at most that edge's price, define \(Q(Y)=\sum_i\|Y_i\|^2\). By the Rayleigh characterization of the second Laplacian eigenvalue, applied independently to each coordinate of \(Y\), every feasible conductance vector satisfies
\[
\lambda_2(L)Q(Y)\le\sum_{ij\in E}w_{ij}\|Y_i-Y_j\|^2\le\sum_{ij\in E}\mathrm{price}_{ij}w_{ij}\le B.
\]
We construct centered witnesses achieving \(Q(Y)=F\) in each phase; hence \(\lambda_2\le B/F\).

In the middle phase, place the left hub at \(0\), the right hub at \(z\), all left leaves at \(-\ell\), and all right leaves at \(z+r\) on a line. Their mean is \(\mu=S/N\). Subtracting that mean gives a centered embedding with every edge distance equal to its prescribed length and squared norm sum \(F_C\).

If \(S<0\), put \(K=(b+1)z+br<a\ell\). Place the left hub at the origin, the right hub at \(ze_1\), and every right leaf at \((z+r)e_1\). Place the \(a\) left leaves at \(-K e_1/a+t_i\), where the perpendicular vectors \(t_i\) are the vertices of a centered regular \(a\)-gon (for \(a=2\), the opposite endpoints of a segment) of radius \(\sqrt{\ell^2-(K/a)^2}\). Their sum is zero, each left spoke has length \(\ell\), and the whole embedding is centered. Its squared norm sum is exactly \(F_L\).

If \(S>Nz\), put \(K'=(a+1)z+a\ell<br\). Place all left leaves at \(-\ell e_1\), the left hub at the origin, the right hub at \(ze_1\), and the \(b\) right leaves at \((z+K'/b)e_1+t_j\), with the perpendicular \(t_j\) forming a centered regular \(b\)-gon of radius \(\sqrt{r^2-(K'/b)^2}\). The mean is \(ze_1\); after subtracting it, the squared norm sum is \(F_R\). These constructions remain valid at the boundaries by taking the corresponding zero-radius polygons.

**(2) Matching feasible conductances.** Assign the displayed \((u,v,c)\), with \(\Lambda=B/F\). Direct expansion gives \(a\ell^2u+br^2v+z^2c=B\) in every phase; all three conductances are positive. The leaf-class-difference eigenspaces of the Laplacian have eigenvalues \(u\) (multiplicity \(a-1\)) and \(v\) (multiplicity \(b-1\)). In all phases \(u,v\ge\Lambda\).

The remaining invariant four-dimensional space consists of vectors constant on each leaf class. It is the generalized weighted path on four ordered blocks (left leaves, left hub, right hub, right leaves), with vertex masses \((a,1,1,b)\) and edge conductances \((au,c,bv)\). In the middle phase, the four block coordinates \((-\ell,0,z,z+r)\), after weighted centering by \(\mu\), solve the generalized eigenvalue equation with eigenvalue \(\Lambda\). In the left phase, use \((-K/a,0,z,z+r)\); in the right phase, use \((-\ell,0,z,z+K'/b)\). These two vectors are already centered after subtracting \(0\) or \(z\), respectively. Substitution into the four block equations verifies \(L f=\Lambda f\) exactly. Each four-block vector is strictly increasing from left to right and, being orthogonal to constants, changes sign once (counting a zero at a hub as the separating position). By the elementary Sturm oscillation theorem for an irreducible symmetric tridiagonal weighted-path eigenproblem, it is the **first positive** mode of that quotient. Equivalently, the weighted path's nonconstant eigenvectors are ordered by the number of their sign changes. Therefore the quotient has no positive eigenvalue below \(\Lambda\); together with \(u,v\ge\Lambda\), this gives \(\lambda_2=\Lambda\). The upper certificate in (1) proves global optimality, not just stationarity.

**(3) Multiplicity and uniqueness.** The four-block path eigenvalues are simple. In the middle open phase \(u,v>\Lambda\), so the eigenspace of \(\Lambda\) is one-dimensional. In the left phase \(u=\Lambda\), and the additional \(a-1\) left leaf-difference vectors give multiplicity \(a\); at \(S=0\) the same statement holds. The right phase is symmetric, with multiplicity \(b\), including \(S=Nz\).

For uniqueness, take any other optimal conductance vector. Equality throughout the inequality in (1) forces full budget use and forces *every coordinate* of the corresponding centered witness to be a \(\Lambda\)-eigenvector. For the middle witness, the pendant-vertex eigenvalue equations, followed by a hub equation, uniquely recover each of the displayed conductances. In the left phase the regular polygon supplies perpendicular eigenvector coordinates, all nonzero at every left leaf in at least one such coordinate, forcing each of its individual pendant conductances to equal \(\Lambda\). The longitudinal eigenvector equations then uniquely fix all right pendant conductances and the bridge conductance. The right phase is symmetric. At either boundary the middle one-dimensional witness still pins all edge weights. Hence the optimizer is unique without imposing symmetry on the individual variables.

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic and SymPy to test the formulas on **368** sets of parameters, including the phase boundaries, heavily unbalanced leaf counts, and every phase. For each case it independently checks budget saturation, the four-block generalized eigenvector equations, all principal minors of the exact four-by-four matrix representing \(L-\Lambda\) on the centered quotient, both pendant-mode inequalities, and equality of the supporting variance certificate. These are reproducibility checks, not a substitute for the all-parameter proof above. Run `python3 verify.py` with Python 3 and SymPy installed.

For example, when \(a=b=2\) and \(\ell=r=z=B=1\), the optimal gap is \(2/19\) with \((u,v,c)=(3/19,3/19,7/19)\). If \(\ell=3\) but \(r=z=B=1\), the optimum enters the left phase, the gap is \(1/27\), and \((u,v,c)=(1/27,2/27,5/27)\).

## Relationship to prior work
Sun, Boyd, Xiao and Diaconis (2006) formulated fastest mixing continuous-time Markov processes under general squared-edge-cost budgets, deriving semidefinite and Euclidean-embedding dual descriptions; their general framework and the Rayleigh certificate are used here, not claimed as new. Their worked exact case includes paths, whereas the double stars here have at least two pendant leaves on each hub and admit genuinely multi-dimensional supporting configurations in two price regimes.

Fiedler (1990) established the absolute algebraic connectivity of trees with *uniform* edge-cost normalization. Richter and Rocha's publicly circulated 2014 preprint (subsequently published as *Absolute algebraic connectivity of double brooms and trees*) gives explicit values and eigenvector transitions for the uniform-price double-broom family, which includes the equal-price specialization of the present double-star result. Those equal-price cases are **prior results**. The contribution here is the exact arbitrary-three-price phase diagram, the unique allocation of all individually variable edge conductances, and the cost-induced multiplicity transitions.

## Limitations
The costs are constant within each of the two pendant classes and arbitrary on the bridge; costs that differ between individual spokes are not classified. The tree has exactly two adjacent hubs and at least two leaves on each; longer double brooms, directed consensus, unequal node masses, and discrete-time stochastic-matrix constraints are not addressed. The result is independent of a total network size limit, but assumes positive edge prices and budget. The existence of a more general prior treatment that implicitly specializes to this formula remains a publication-priority risk, especially for work on cost-weighted tree embeddings.

## References
1. J. Sun, S. Boyd, L. Xiao and P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48 (2006), 681–699. DOI: https://doi.org/10.1137/S0036144504443821 (published online November 2, 2006).
2. M. Fiedler, *Absolute algebraic connectivity of trees*, Linear and Multilinear Algebra 26 (1990), 85–106. DOI: https://doi.org/10.1080/03081089008817967.
3. S. Richter and I. Rocha, *Absolute algebraic connectivity of double brooms*, TU Chemnitz Preprint 2014/10 (2014), https://www.tu-chemnitz.de/mathematik/preprint/2014/PREPRINT_10.pdf ; later *Absolute algebraic connectivity of double brooms and trees*, Discrete Applied Mathematics 201 (2016), 213–221, DOI: https://doi.org/10.1016/j.dam.2015.08.009.
