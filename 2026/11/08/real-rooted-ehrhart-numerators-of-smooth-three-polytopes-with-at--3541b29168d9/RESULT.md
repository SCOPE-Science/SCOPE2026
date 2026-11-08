# Real-rooted Ehrhart numerators of smooth three-polytopes with at most five facets

## Finding

**Theorem.** Let \(P\subset\mathbb R^3\) be any full-dimensional smooth lattice polytope with at most five facets. Smooth means that the primitive directions of the three edges at each vertex form a basis of \(\mathbb Z^3\). Write its Ehrhart series as
\[
\sum_{k\ge 0}|kP\cap\mathbb Z^3|z^k=\frac{h_P^*(z)}{(1-z)^4}.
\]
Then **every zero of \(h_P^*\) is strictly negative, real, and simple**. The constant polynomial is understood to have no zeros. There is no lower bound on lattice width, lattice edge length, or number of lattice points.

## Assumptions and scope

This theorem concerns three-dimensional *smooth* lattice polytopes with four or five facets; fewer facets are impossible for a three-polytope. The claim includes all integral lengths and all nonnegative twisting parameters in Kleinschmidt's classification of smooth lattice polytopes with \(d+2\) facets, as presented in Liu–Tang–Tao–Zhang (2026, Theorem 2.1). It makes no claim for six-facet polytopes or for nonsmooth polytopes. The publication motivating the problem appeared publicly on 2026-10-20 (arXiv:2610.27819, version 1).

## Proof

**Step 1: reduction to two normal forms.** The cited classification gives a four-facet polytope \(a\Delta_3\), with integer \(a\ge1\), or a five-facet polytope lattice-equivalent to
\[
P_{p,q}=\{(x,y)\in\mathbb R^p\times\mathbb R^q:\ y_j\ge0,\ \textstyle\sum_jy_j\le b,\ x_i\ge0,\ \textstyle\sum_ix_i\le a+\sum_jc_jy_j\},
\]
where \(p+q=3\), \(p,q\ge1\), \(a,b\) are positive integers, and all \(c_j\) are nonnegative integers. Integer-point enumeration of the simplex fibers is exact:
\[
L_{P_{p,q}}(k)=\sum_{y\in k b\Delta_q\cap\mathbb Z^q}\binom{ka+\sum_jc_jy_j+p}{p}.
\]
This uses the actual ambient lattice; there is no asymptotic approximation.

**Step 2: elementary polynomial forms.** In the \((p,q)=(1,2)\) case write \(C=c_1+c_2\), and use the symmetry of weak compositions of \(bk\) into three parts. Since there are \(\binom{bk+2}{2}\) compositions and the mean of each part is \(bk/3\),
\[
L_{12}(k)=\frac{(bk+1)(bk+2)}2\left(1+\left(a+\frac{bC}{3}\right)k\right).
\]
In the \((p,q)=(2,1)\) case write \(C=c_1\). Summing squares of an arithmetic progression gives
\[
L_{21}(k)=\frac{bk+1}{2}\left[(ak+1)(ak+2)+\frac{Cbk(2ak+3)}2+\frac{C^2bk(2bk+1)}6\right].
\]
For a four-facet polytope, \(L_{a\Delta_3}(k)=\binom{ak+3}{3}\).

**Step 3: numerator and discriminant.** For any of these degree-three Ehrhart polynomials \(L\), set \(v_j=L(j)\) for \(j=0,1,2,3\), and define
\[
h_j=\sum_{i=0}^j(-1)^i\binom4i v_{j-i},\qquad H(z)=h_0+h_1z+h_2z^2+h_3z^3.
\]
The Ehrhart-series identity gives \(H=h_P^*\), and \(h_0=1\). Stanley's nonnegativity theorem for lattice-polytope Ehrhart numerators guarantees \(h_1,h_2,h_3\ge0\). For a five-facet smooth polytope, \(h_1>0\), since it has at least six lattice vertices and \(h_1=|P\cap\mathbb Z^3|-4\). For a four-facet simplex, \(h_1>0\) when \(a\ge2\); the unimodular case \(a=1\) is treated separately.

For the cubic coefficient convention in this proof, the discriminant is
\[
\mathcal D=h_1^2h_2^2-4h_2^3-4h_3h_1^3-27h_3^2+18h_3h_2h_1.
\]
The exact algebraic coefficient certificate `certificate.json`, reproduced from the formulas above by `verify.py`, establishes the following **polynomial identities over \(\mathbb Q\)**: after the substitution \(A=a-1\ge0\), \(B=b-1\ge0\), \(C\ge0\), the full expanded discriminant \(\mathcal D\) has **139 strictly positive monomial coefficients** in the \((1,2)\) form and **338 strictly positive monomial coefficients** in the \((2,1)\) form; every other coefficient is zero. These counts include all monomials of the respective discriminant, not a sample. To make strictness transparent, the same exact identities give
\[
\begin{aligned}
\mathcal D_{12}(0,B,0)&=B^2(B+1)^2(2B+1)^2(B^2+8B+4),\\
\mathcal D_{21}(A,0,0)&=A^2(A+1)^2(2A+1)^2(A^2+8A+4),\\
\mathcal D_{21}(0,0,C)&=\frac{C^2(C+1)^3(C^3+9C^2+16C+16)}{16}.
\end{aligned}
\]
All monomial coefficients being nonnegative, these specializations imply \(\mathcal D_{12}>0\) whenever \(B>0\), and \(\mathcal D_{21}>0\) whenever \(A>0\) or \(C>0\), uniformly in the remaining nonnegative variables. In the excluded degenerate cases, the numerator is linear: \(B=0\) in the first form, or \(A=C=0\) in the second. Its linear coefficient is strictly positive. Thus every five-facet numerator of degree at least two has positive cubic-form discriminant. If its cubic coefficient vanishes, the same formula becomes \(h_2^2(h_1^2-4h_2)>0\), proving the reduced quadratic has two distinct real roots.

**Step 4: simplices.** When \(a=1\), \(h^*_{\Delta_3}=1\). For integer \(a\ge2\), put \(u=a-2\ge0\). The exact discriminant calculation for \(\binom{ak+3}{3}\) yields
\[
\mathcal D_{a\Delta_3}=\frac{(u+1)^2(u+2)^6}{108}\bigl(u^4+22u^3+183u^2+540u+54\bigr)>0.
\]
The same degree-drop reasoning applies if \(h_3=0\). All roots are therefore real and distinct in every nonconstant case.

**Step 5: negativity.** Any nonconstant polynomial with nonnegative coefficients and positive constant term has no nonnegative real zeros. Combining this with the discriminant conclusions, every zero is strictly negative, real, and simple. This proves the theorem.

## Verification

The finite coefficient certificate is mathematical evidence for a universal polynomial inequality, not an experiment over finitely many parameter choices. Run `python verify.py certificate.json` with SymPy available. The code symbolically reconstructs each Ehrhart polynomial, forms all four numerator coefficients, computes both discriminants independently by two formulas, recomputes their complete rational monomial expansions, compares every coefficient with the supplied immutable coefficient lists, checks positivity of **all 477 nonzero monomial coefficients**, and verifies the simplex identity. It also checks small cases directly by integer slice enumeration as a *separate supplementary consistency test*. No floating-point calculation is used in the main proof or certificate. The certificate plus explicit bounded algebraic identities make the parameter-uniform conclusion auditable.

For example, the second normal form with \((a,b,C)=(2,2,1)\) has \(h^*(z)=(1+z)(1+26z+z^2)\), exhibiting the three distinct negative real roots.

## Relationship to prior work

Liu–Tang–Tao–Zhang (2026) show Ehrhart **coefficient positivity** for smooth three-dimensional polytopes with at most five facets, and give the Kleinschmidt coordinates used here. Coefficient positivity of \(L_P\) is different from, and does not imply, real-rootedness of \(h_P^*\). Their analysis does not assert the present root classification. Nill (2026) proves root-realness only once *lattice width is sufficiently large*; the present theorem imposes no width threshold and includes width-one examples. Ohsugi–Tsuchiya (2026) prove real-rootedness for certain duals of pseudo-symmetric reflexive polytopes using magic positivity; this is a distinct restricted class, not all the above smooth, generally non-reflexive, five-facet polytopes. Liu (2026) supplies a general Cayley counting formula and shows real-rootedness is not generally preserved by Cayley summation; it does not classify this smooth five-facet case. Existing Cartesian-product real-rootedness results do not cover twisted cases with \(C>0\). The unit triangular prism already shows that this claim is not merely an instance of general magic positivity: its Ehrhart polynomial \(L(k)=(k+1)^2(k+2)/2\) has coefficient \(-1/2\) on \(k(k+1)^2\) in the magic basis \(k^i(k+1)^{3-i}\), although its numerator is \(1+2z\).

## Limitations

No statement is made for nonsmooth polytopes, six or more facets, higher dimensions, or Ehrhart polynomial zeros (as opposed to numerator zeros). The use of the published classification and of Stanley's nonnegativity theorem is explicit. The discriminant-positivity lemma is supported by a complete reproducible rational coefficient certificate; readers may verify its finite algebra rather than rely on any numerical sampling. Historical-priority research is not a proof of uniqueness, and older special-case literature may contain equivalent formulations. No independent external mathematical audit has been performed.

## References

1. F. Liu, J. Tang, S. Tao, Z. Zhang, *Ehrhart positivity of smooth polytopes with few facets*, arXiv:2610.27819, first public 2026-10-20; especially Theorem 2.1, Proposition 3.1, and equation (3.1).
2. B. Nill, *Lattice polytopes of large width have real-rooted Ehrhart \(h^*\)-polynomials*, arXiv:2608.03635, 2026-08-04, Theorem 1.1.
3. H. Ohsugi, A. Tsuchiya, *Magic positivity for polar duals of pseudo-symmetric smooth Fano polytopes*, arXiv:2610.06419, 2026-10-05, Theorem 1.2.
4. F. Liu, *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338, 2026-10-05, §7, especially Proposition 7.1 and Theorem 7.4.
5. R. P. Stanley, *Decompositions of rational convex polytopes*, Ann. Discrete Math. 6 (1980), 333–342 (nonnegativity of lattice-polytope Ehrhart numerators).
6. P. Kleinschmidt, *A classification of toric varieties with few generators*, Aequationes Math. 35 (1988), 254–266 (smooth Picard-rank-two classification).
