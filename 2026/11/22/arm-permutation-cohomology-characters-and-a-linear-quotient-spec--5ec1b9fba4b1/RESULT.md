# Arm-permutation cohomology characters and a linear quotient spectrum for star nilmanifolds

## Finding

Let \(n\ge1\) and let \(N_n\) be the standard compact Dani–Mainkar nilmanifold of the star \(K_{1,n}\), defined explicitly below, with the symmetric group \(S_n\) permuting its \(n\) arms. For a permutation \(\sigma\in S_n\), write \(c_\ell(\sigma)\) for the number of its cycles of length \(\ell\). Define the *graded rational cohomology character*
\[
\mathcal P_\sigma(t)=\sum_{k=0}^{2n+1}\operatorname{tr}\!\left(\sigma\mid H^k(N_n;\mathbb Q)\right)t^k.
\]
Then every graded trace is determined by the finite coefficient formula
\[
\boxed{\mathcal P_\sigma(t)=(1+t)\bigl([q^0]+[q^1]\bigr)\prod_{\ell\ge1}\bigl(1-(-tq)^\ell\bigr)^{c_\ell(\sigma)}\bigl(1-(-tq^{-1})^\ell\bigr)^{c_\ell(\sigma)}.}
\]
Here \([q^j]\) denotes extraction of the coefficient of \(q^j\) from the Laurent polynomial immediately to its right; only finitely many factors are nontrivial. In particular, for the natural compact quotient \(N_n/S_n\),
\[
\boxed{\sum_{n\ge0}u^n\sum_{k\ge0}\dim_{\mathbb Q} H^k(N_n/S_n;\mathbb Q)t^k
=\frac{(1+t)(1+ut+u^2t^2)}{(1-u)(1-ut^2)},}
\]
where \(N_0\) is the circle for the sole purpose of the generating function. For \(n\ge2\), the quotient Betti vector in degrees \(0,\ldots,2n+1\) is
\[
\boxed{(1,2,\underbrace{3,\ldots,3}_{2n-2\text{ terms}},2,1),}
\]
and for \(n=1\) it is \((1,2,2,1)\). Thus \(\sum_k\dim H^k(N_n/S_n;\mathbb Q)=6n\) for every \(n\ge1\). By comparison the previously known nonequivariant total is \(2\binom{2n+1}{n}\). The full character formula is stronger than these quotient dimensions: it determines the rational cohomology representation of every permutation in every degree.

## Assumptions and scope

Work with the simply connected real nilpotent Lie group whose global coordinates are \((a,b,c)\in\mathbb R\times\mathbb R^n\times\mathbb R^n\), with multiplication
\[
(a,b,c)\cdot(a',b',c')=(a+a',b+b',c+c'+ab').
\]
Here \(ab'\) is the coordinatewise product of the scalar \(a\) and vector \(b'\). The integer-coordinate subgroup \(\Gamma_n=\mathbb Z\times\mathbb Z^n\times\mathbb Z^n\) is a uniform lattice, and \(N_n=\Gamma_n\backslash G_n\). Permuting the coordinates of \(b\) and \(c\) simultaneously gives an honest action of \(S_n\) on \(G_n\), preserving \(\Gamma_n\) and inducing the claimed action on \(N_n\). Its Lie brackets are \([A,B_i]=C_i\), so this is the Dani–Mainkar construction for \(K_{1,n}\). Results concern rational singular cohomology (equivalently characteristic-zero real de Rham cohomology characters) and the topological orbit-space quotient. No integral torsion or equivariant cohomology of Borel constructions is asserted.

## Proof

**1. Equivariant differential model.** The Nomizu comparison identifies the de Rham cohomology with the Chevalley–Eilenberg cohomology of the Lie algebra, naturally under the finite group of arm-permutation automorphisms. With degree-one variables \(a,x_i,z_i\), choosing a sign for the duals of the central generators gives
\[
 da=dx_i=0,\qquad dz_i=a\wedge x_i.
\]
Put \(A_n=\bigwedge_{\mathbb Q}\langle x_1,z_1,\ldots,x_n,z_n\rangle\). Let \(E\) be the degree-zero derivation of \(A_n\) with \(E(z_i)=x_i\), \(E(x_i)=0\). Since \(d\alpha=a\wedge E\alpha\) on \(A_n\), while \(d(a\wedge\beta)=0\), the cohomology in each degree splits, equivariantly, as
\[
H^k\cong\ker(E\mid A_n^k)\oplus a\wedge\operatorname{coker}(E\mid A_n^{k-1}). \tag{1}
\]
For any endomorphism of a finite-dimensional module commuting with a finite-group action, kernel and cokernel have the same virtual character, by the two short exact sequences involving its image. Therefore the total graded character of (1) is \((1+t)\) times the graded character of \(\ker E\).

**2. A weight extraction identity.** On \(\langle x_i,z_i\rangle\) let \(E\) act as above, let \(F(x_i)=z_i\), \(F(z_i)=0\), and let \(H(x_i)=x_i\), \(H(z_i)=-z_i\). These operators extend to \(A_n\) as degree-zero derivations and form an \(\mathfrak{sl}_2\)-triple. Arm permutations commute with all three. In each finite-dimensional irreducible \(\mathfrak{sl}_2\)-representation, precisely one of weights zero and one occurs, and each occurs once if present; its highest-weight line is \(\ker E\). Consequently, for every commuting arm permutation, the trace on \(\ker E\) is the sum of its traces on the weight-zero and weight-one spaces. This statement holds degree by degree because the \(\mathfrak{sl}_2\)-operators preserve exterior degree.

For a permutation \(\sigma\), the two \(H\)-weights of the one-arm representation are \(q\) and \(q^{-1}\). The graded character of \(A_n\) is the determinant \(\det(1+t\,\sigma\mid\mathbb Q^n\otimes(q\oplus q^{-1}))\). Each length-\(\ell\) cycle contributes \((1-(-tq)^\ell)(1-(-tq^{-1})^\ell)\). Extracting weights zero and one, then multiplying by \((1+t)\) from (1), proves the boxed graded-character formula.

**3. Invariants and the quotient.** Because the finite group has characteristic-zero coefficients, taking invariants is exact. Moreover the exterior algebra \(A_n\) is the graded tensor product of \(n\) copies of \(\bigwedge\langle x,z\rangle\), and arm permutations act by graded-factor permutations. Hence the \(S_n\)-invariant part is the \(n\)-th graded-symmetric power of the four-dimensional local exterior algebra. This local algebra contains two *even* one-dimensional weight-zero pieces in exterior degrees zero and two, and two *odd* one-dimensional pieces in exterior degree one of \(H\)-weights \(+1\) and \(-1\). Thus
\[
\sum_{n\ge0}u^n\sum_k t^k\operatorname{ch}_H((A_n^k)^{S_n})
=\frac{(1+utq)(1+utq^{-1})}{(1-u)(1-ut^2)}. \tag{2}
\]
Taking the \(q^0\) and \(q^1\) coefficients of (2), and multiplying by \((1+t)\), gives precisely \((1+t)(1+ut+u^2t^2)/((1-u)(1-ut^2))\). Expanding the coefficient of \(u^n\) gives the stated Betti vectors and the dimension \(6n\) for \(n\ge1\).

The finite smooth action admits an equivariant triangulation. Over \(\mathbb Q\), averaging cellular cochains identifies the cohomology of the orbit space with the \(S_n\)-invariant part of \(H^*(N_n;\mathbb Q)\). Therefore the invariant calculation indeed computes the ordinary rational cohomology of \(N_n/S_n\).

## Verification

The accompanying standalone `checker.py` constructs the degree-preserving exterior derivation \(E\) using signed wedge monomials, finds its image via row reduction over \(\mathbb F_{1009}\), computes each permutation's trace on its kernel, and compares against the cycle-type coefficient expression. It checks all \(1,2,6,24\) permutations for \(n=1,2,3,4\), respectively, in every cohomological degree; it also averages those finite-field traces and checks the stated invariant Betti vectors. The number of graded-trace comparisons is \(4+12+48+240=304\). These are exact finite-field sanity checks rather than a characteristic-zero proof. The characteristic-zero all-rank conclusion rests on the three algebraic steps above. To replay, run `python3 checker.py` using a standard Python installation, without external dependencies.

## Relationship to prior work

The nonequivariant cohomology of all star-graph Dani–Mainkar Lie algebras is already known. Armstrong–Cairns–Jessup (1997) introduce the same derivation and obtain complete ordinary Betti numbers, and Aldi–Butler–Gardiner–Grandini–Lichtenwalner–Pan (first public 2024) revisit the star calculation using induced subgraphs. The paper by Aldi et al. (first public November 12, 2026) treats explicit Poincaré polynomials of *path* graph nilmanifolds and mentions stars as prior results. The new statement here is **not** the nonequivariant Betti calculation or the standard kernel/cokernel decomposition: it is the full graded \(S_n\)-character evaluated on arbitrary cycle types and the closed \(6n\)-dimensional cohomology spectrum of the natural arm-permutation orbit space. These require the commuting \(\mathfrak{sl}_2\)-weight and graded-symmetric-invariant computations.

## Limitations

The stated rational characters do not determine the integral cohomology or torsion of \(N_n\) or of the quotient. Orbit spaces may have singular points and are not claimed to be nilmanifolds. No ring presentation for the quotient is asserted. The result applies to the specified symmetric integer lattice and full arm-permutation group, not to arbitrary lattice choices or arbitrary graph automorphism subgroups without specializing the character. The published literature comparison cannot exclude an unindexed earlier equivalent representation calculation; the explicit Betti numbers themselves have clear older priority. No independent mathematical audit has been performed.

## References

1. M. Aldi, S. Bevins, E. Chatzitheodoridis, S. Da Silva, Q. Frias, T. Mejía Gómez, *Poincaré polynomials of nilmanifolds associated with path graphs*, arXiv:2611.17014v1, publicly submitted November 12, 2026. https://arxiv.org/html/2611.17014v1
2. M. Aldi, A. Butler, J. Gardiner, D. Grandini, M. Lichtenwalner, K. Pan, *On the cohomology of Lie algebras associated with graphs*, arXiv:2402.14188v2 (initial preprint February 22, 2024), §4. https://arxiv.org/html/2402.14188v2
3. G. F. Armstrong, G. Cairns, B. Jessup, *Explicit Betti numbers for a family of nilpotent Lie algebras*, Proc. Amer. Math. Soc. 125 (1997), 381–385. https://doi.org/10.1090/S0002-9939-97-03607-1
4. K. Nomizu, *On the cohomology of compact homogeneous spaces of nilpotent Lie groups*, Ann. of Math. 59 (1954), 531–538.
