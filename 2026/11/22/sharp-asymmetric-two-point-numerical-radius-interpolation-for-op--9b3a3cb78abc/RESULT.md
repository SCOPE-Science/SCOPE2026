# Sharp asymmetric two-point numerical-radius interpolation for opposite matrix units

## Finding
Let \(E_{12}\) and \(E_{21}\) denote the standard opposite matrix units. For distinct \(z_0,z_1\in\mathbb D\) set
\[
\rho=\left|\frac{z_0-z_1}{1-\overline{z_0}z_1}\right|\in(0,1).
\]
For every \(a,b>0\) with \(a\ne b\), the exact least uniform numerical radius of a bounded analytic matrix-valued interpolant satisfying \(F(z_0)=aE_{12}\), \(F(z_1)=bE_{21}\) is
\[
\mathcal M(a,b,\rho)=\frac{a+b+\sqrt{(a+b)^2-4\rho^2ab}}{4\rho}.
\]
In particular a numerical-radius-unit-ball solution exists exactly when \(\mathcal M(a,b,\rho)\le1\). The minimum is attained by a rational matrix-valued function.

## Assumptions and scope
All matrix spaces are over \(\mathbb C\). The numerical radius is \(w(T)=\sup_{\|v\|_2=1}|\langle Tv,v\rangle|\). The values \(a,b\) are strictly positive and unequal; both nodes are interior to the unit disk and distinct. The analytic maps considered have finite uniform numerical radius, equivalently are bounded as matrix-valued functions. Only these two prescribed off-diagonal values are imposed; the result does not classify general numerical-radius Nevanlinna–Pick interpolation or arbitrary matrix data.

## Proof
An automorphism of the disk carries the ordered nodes to \(0\) and a real \(t=\rho>0\), with precomposition preserving all suprema. Write \(m=\sup w(F(z))\) for any competitor. The scalar function \(h(z)=(F_{12}(z)-F_{21}(z))/2\) satisfies \(|h(z)|\le w(F(z))\): indeed the anti-diagonal off-diagonal skew combination is bounded by the numerical radius, as can be seen by averaging \(\langle Fv,v\rangle\) over the appropriate phase angles. In particular, \(h(0)=a/2\), \(h(t)=-b/2\). The Schwarz–Pick inequality for \(h/m\) yields
\[
t\ge\frac{2m(a+b)}{4m^2+ab}.
\]
Since \(m\ge\max\{a,b\}/2\), the relevant branch of this quadratic inequality gives \(m\ge\mathcal M(a,b,t)\). This includes all \(t\in(0,1)\) and all strictly positive \(a,b\).

To attain equality let \(m=\mathcal M(a,b,t)\), \(u=a/(2m)\in(0,1)\), \(v=-b/(2m)\in(-1,0)\). They satisfy \(t=(u-v)/(1-uv)\). Put
\[
B(z)=\frac{u-z}{1-uz},\quad A=u+u^{-1}>2,\quad C=v+v^{-1}<-2,\quad k=(A-C)^{-1},\quad c=-C(A-C)^{-1}.
\]
Define
\[
p(z)=2m\{cB(z)+k[B(z)^2+1]\},\qquad
q(z)=2m\{(c-1)B(z)+k[B(z)^2+1]\},
\]
and \(F(z)=\begin{pmatrix}0&p(z)\\q(z)&0\end{pmatrix}\). Direct substitution in the two interpolation nodes gives \(p(0)=a,q(0)=0,p(t)=0,q(t)=b\), because \(c+kA=1\) and \(c+kC=0\). For \(|z|=1\), \(|B(z)|=1\) and
\[
H(z)=c+k[B(z)+B(z)^{-1}]\in[c-2k,c+2k]\subset(0,1),
\]
where strict containment follows from \(A>2\) and \(C<-2\). Consequently \(p=2mBH\) and \(q=2mB(H-1)\) on the boundary; hence \(|p|+|q|=2m\). The exact identity \(w(\begin{psmallmatrix}0&p\\q&0\end{psmallmatrix})=(|p|+|q|)/2\) and the maximum principle give \(w(F(z))\le m\) throughout the disk, with uniform supremum \(m\). Precomposition by the inverse normalization automorphism furnishes the asserted rational extremizer for the original nodes.

## Verification
The derivation above is exact and holds uniformly in all admissible parameters. The accompanying standalone script `verify_asymmetric.py` independently evaluates five parameter triples (including the equal-strength boundary check), checks endpoint identities, the Möbius relation and strict envelope inequalities, and samples 90 boundary angles for each triple. It reports 480 successful high-precision assertions. The finite diagnostic does not prove the theorem; the Schwarz–Pick and maximum-principle steps do.

## Relationship to prior work
Ahmed, Bhowmik, Das and Sau formulate general numerical-radius-unit-ball interpolation via factorization and include equal-strength opposite-matrix-unit examples (Examples 2.5 and 4.6). Their general criterion does not state this explicit closed-form asymmetric norm and extremizer. The earlier equal-amplitude threshold is recovered when \(a=b\); it is not a novel special case. Kosiński and Zwonek discuss general complex geodesics and Nevanlinna–Pick questions in convex domains; that framework is broader in principle, but the inspected material does not exhibit this concrete two-parameter formula. A common scalar rescaling and unitary conjugation preserve the unordered ratio of the two nonzero prescribed singular values, so they cannot reduce unequal amplitudes to the equal case.

## Limitations
No uniqueness of extremizers is asserted. General operator-valued numerical-radius interpolation and more than two nodes are outside the theorem. Literature overlap was checked against identified papers, available earlier claims and published-finding corpus searches, but the possibility of an implicit derivation via classical convex-domain geodesic theory remains a bibliographic risk. The computation is a finite sanity check, not an independent proof or independent mathematical audit.

## References
1. H. Ahmed, M. Bhowmik, B. K. Das and H. Sau, *Interpolation, Factorization, and Approximation in the Numerical Radius Unit Ball*, arXiv:2611.19189v1 (first posted 14 November 2026), https://arxiv.org/abs/2611.19189; especially Sections 2 and 4 and Examples 2.5 and 4.6.
2. Ł. Kosiński and W. Zwonek, *Nevanlinna–Pick Problem and Uniqueness of Left Inverses in Convex Domains, Symmetrized Bidisc and Tetrablock*, arXiv:1303.0482v1, https://arxiv.org/abs/1303.0482.
3. Classical Schwarz–Pick lemma for holomorphic self-maps of the unit disk.
