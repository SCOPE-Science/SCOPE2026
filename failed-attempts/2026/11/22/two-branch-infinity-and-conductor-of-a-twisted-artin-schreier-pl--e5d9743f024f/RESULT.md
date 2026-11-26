# Two-branch infinity and conductor of a twisted Artin--Schreier plane model

## Finding

**Theorem (ordinary plane compactification).** Let \(k\) be algebraically closed of odd prime characteristic \(p\), and let \(f(u)\in k[u]\) have degree \(d>p+2\) and nonzero leading coefficient. Assume \(p\nmid d-1\). Let \(\overline C_f\subset\mathbb P^2_k\) be the ordinary degree-\(d\) projective closure of the affine equation
\[
 u v^p+v=f(u).
\]
Put \(A=d-p-1\) and \(B=d-1\). Then \(\overline C_f\) is geometrically integral, is smooth off the single point \(Q=[0:1:0]\), and has exactly **two** geometric branches at \(Q\):

* A smooth branch \(P_0\), lying over \(u=0\) on the normalization, tangent to the line \(U=0\).
* A cuspidal branch \(P_\infty\), lying over \(u=\infty\), tangent to the line at infinity \(W=0\), whose local value semigroup is \(\langle A,B\rangle\) and whose tame Puiseux characteristic is the single pair \((A,B)\).

The branches have intersection multiplicity \(I_Q(P_0,P_\infty)=A\). In particular, with \(\delta_\infty\) the cusp-branch normalization defect,
\[
 \delta_\infty=\frac{(A-1)(B-1)}2,
 \qquad \delta_Q=\frac{(A-1)(B-1)}2+A
          =\frac{d(d-p-2)+2}{2}.
\]
The normalization conductor, viewed as an ideal in \(k[[t_0]]\oplus k[[t_\infty]]\), has exact branch orders
\[
 (c_0,c_\infty)=\bigl(A,(A-1)(B-1)+A\bigr).
\]
The normalization has genus \(\frac{(p-1)d}{2}\). If \(f\) is defined over \(\mathbb F_p\), both normalization preimages of \(Q\) are \(\mathbb F_p\)-rational.

**Application to the recent maximal curves.** For the explicit Bartoli--Borges--Timpanella--Zini prime-field maximal curve \(X_{p,n}\), \(p\) odd and \(n\ge2\), take
\[
 f(u)=-1-2\sum_{i=1}^{n}u^{(p^{2i}-1)/(2(p-1))},
 \qquad d=\frac{p^{2n}-1}{2(p-1)}.
\]
Then all the conclusions above hold, the two singular branches are rational over \(\mathbb F_p\), and their gluing accounts for the entire plane arithmetic-genus defect. For \(p=3,n=2\), the degree-20 model has cusp semigroup \(\langle16,19\rangle\), transverse branch contact \(16\), total \(\delta_Q=151\), and normalized genus \(20\).

## Assumptions and scope

Here \([U:V:W]\) are the homogeneous plane coordinates, \(u=U/W\), \(v=V/W\); the displayed **ordinary projective plane closure** is distinguished from the smooth projective curve itself. The hypotheses are \(p\ge3\) prime, \(k\) algebraically closed of characteristic \(p\), \(d>p+2\), and \(p\nmid d-1\), with arbitrary lower coefficients of \(f\). Local branches and their value semigroups are taken geometrically over \(k\). The normalization conductor is the largest ideal of the local plane-curve ring which is also an ideal of its two-branch normalization. No assertion is made for the excluded degree or congruence regimes.

## Proof

**1. Integral affine curve, its closure and its only possible singularity.** The polynomial \(u v^p+v-f(u)\) has derivative \(1\) with respect to \(v\) in characteristic \(p\), so every affine point is nonsingular. Its polynomial in \(v\), over \(k(u)\), has degree \(p\). At \(u=\infty\), putting \(s=1/u\) and multiplying by \(s\) gives
\[
 v^p+s v=s f(1/s).
\]
The right-hand side has leading valuation \(1-d=-B\). The unique lower Newton segment has slope \(B/p\) in the coefficient convention, hence every root has valuation \(-B/p\) over \(k((s))\). Because \(\gcd(p,B)=1\), a root generates a local field extension of ramification degree \(p\), so the degree-\(p\) polynomial is irreducible over \(k(u)\). It has a single geometric point over \(u=\infty\), with
\[
 \operatorname{ord}_{P_\infty}(u)=-p,
 \qquad \operatorname{ord}_{P_\infty}(v)=-B.
\]
Homogenization gives the degree-\(d\) plane equation
\[
 G(U,V,W)=U V^p W^{d-p-1}+V W^{d-1}-W^d f(U/W)=0,
\]
where \(W^df(U/W)\) means the homogeneous polynomial \(\sum_j f_j U^jW^{d-j}\). Setting \(W=0\) leaves the nonzero leading coefficient times \(U^d\), so \(Q=[0:1:0]\) is the unique point on the line at infinity. Thus the only possible singular point is \(Q\).

**2. Two and only two normalization preimages of \(Q\).** A normalization point tending to \(Q\) has \(v\) tending to infinity, or \(u\) tending to infinity. In the first case, set \(z=1/v\). The defining equation becomes
\[
 u+z^{p-1}=f(u)z^p.
\]
At \(z=0\), it forces \(u=0\), and its partial derivative with respect to \(u\) at \((u,z)=(0,0)\) equals \(1\). By the formal implicit-function theorem it defines a unique smooth branch \(P_0\), with uniformizer \(z\) and expansion
\[
 u=-z^{p-1}+f(0)z^p+O(z^{p+1}).
\]
The second possibility is exactly the unique place \(P_\infty\) of Step 1. Conversely, all other finite \((u,v)\) remain in the affine chart, so these are the only two preimages. Both map to \(Q\). When \(f\) is \(\mathbb F_p\)-rational, the unique smooth formal branch and the unique geometric place at infinity are stable under Frobenius; hence both are rational.

**3. Embedded local valuations and branch contact.** Use plane local coordinates \(a=U/V=u/v\), \(b=W/V=1/v\) at \(Q\). From Step 2, on the smooth branch \(b=z\) and
\[
 a=u z=-z^p+O(z^{p+1}),
\]
so it is smooth with tangent \(a=0\). On the other branch, Step 1 gives
\[
 \operatorname{ord}_{P_\infty}(a)=B-p=A,
 \qquad \operatorname{ord}_{P_\infty}(b)=B.
\]
Since \(1<A<B\), it is singular with tangent \(b=0\), distinct from the smooth-branch tangent; indeed \(\gcd(A,B)=\gcd(p,B)=1\), and \(p\nmid A\). Let the smooth-branch equation be \(a=\phi(b)\), \(\phi(b)=-b^p+O(b^{p+1})\). On the cusp branch, \(\operatorname{ord}(a)=A<pB=\operatorname{ord}(b^p)\). Thus the intersection multiplicity is
\[
 I_Q(P_0,P_\infty)=\operatorname{ord}_{P_\infty}(a-\phi(b))=A.
\]
For direct confirmation, the local equation has initial homogeneous term \(a b^{A}\), hence tangent cone \(a b^{A}\), with exactly the displayed branch multiplicities and directions.

**4. Complete cusp semigroup, defect and conductor.** Because \(p\nmid A\), a local-parameter change and extraction of an \(A\)-th root of a formal unit give \(a=t^A\), \(b=t^B(c+O(t))\), \(c\ne0\). As \(\gcd(A,B)=1\), the \(A\) powers \(1,b,\dots,b^{A-1}\) have distinct valuation residues modulo \(A\). Since the local extension \(k((t))/k((a))\) has degree \(A\), and the valuation of \(b\) is coprime to \(A\), the powers \(1,b,\dots,b^{A-1}\) form a basis over \(k((a))\); Weierstrass division makes them a free basis of the branch ring over \(k[[a]]\). In a combination \(\sum_{j=0}^{A-1}g_j(a)b^j\), the nonzero summands have pairwise distinct valuation residues modulo \(A\), and hence cannot cancel at their smallest value. Consequently the local value semigroup is exactly \(\langle A,B\rangle\). Equivalently, the tame Puiseux characteristic has the single pair \((A,B)\), with no later characteristic exponents after the gcd becomes one. Its gap count is the two-generator numerical-semigroup genus \(\delta_\infty=(A-1)(B-1)/2\). For two reduced branches, \(\delta_Q=\delta(P_0)+\delta(P_\infty)+I_Q(P_0,P_\infty)\); the smooth branch has defect zero, giving the asserted \(\delta_Q\).

For completeness, write the completed plane equation as a product \(g_0 g_\infty\) of the two distinct reduced branch equations. An element supported on just one normalization component lifts through the plane ring only when divisible by the equation of the other branch; after this factor is removed, it must lie in the conductor of that component's own branch ring. The restriction of the other branch equation has valuation \(I=A\). The smooth branch has intrinsic conductor order zero, while the one-branch cusp semigroup \(\langle A,B\rangle\) has intrinsic conductor order \((A-1)(B-1)\). Thus the conductor on the two normalization branches has orders \(c_0=A\) and \(c_\infty=(A-1)(B-1)+A\). Their sum equals \(2\delta_Q\), consistently with the Gorenstein conductor-length identity.

**5. Genus, rationality and the maximal-curve specialization.** The plane arithmetic genus is \((d-1)(d-2)/2\), and the only singularity is \(Q\). The normalization genus is therefore
\[
 \frac{(d-1)(d-2)}2-\frac{(A-1)(B-1)}2-A
 =\frac{(p-1)d}{2}.
\]
For the odd-characteristic maximal family, the exponents \(e_i=(p^{2i}-1)/(2(p-1))\) are strictly increasing integers, the leading coefficient \(-2\) is nonzero, and \(d\equiv2^{-1}\pmod p\), hence \(p\nmid(d-1)\) and \(d>p+2\) for \(n\ge2\). Substitution gives \((p-1)d/2=(p^{2n}-1)/4\), agreeing with the genus established independently for its smooth projective normalization. This equality is a consistency check, not a new genus theorem.

## Verification

The standalone `verify_plane_model.py` uses exact integer arithmetic. It checks the degrees and initial tangent monomial of the actual sparse homogeneous equation, the coprimality and tame characteristic hypotheses, both projected branch valuations, contact, cusp semigroup gap count, conductor sum, normalized genus and specialization for \(p\in\{3,5,7,11,13\}\) and \(n\in\{2,3\}\). For modest degrees it independently enumerates all gaps of \(\langle A,B\rangle\). It reports `ALL_EXACT_CHECKS_OK`. The universal branch and semigroup assertions follow from the proof, not from these finite tests. The two examples \((p,n)=(3,2),(5,2)\) yield respectively \((A,B,\delta_Q,g)=(16,19,151,20)\) and \((72,77,2770,156)\).

## Relationship to prior work

Bartoli, Borges, Timpanella and Zini, *Maximal curves with trivial automorphism group* (arXiv:2610.35788v1, first public October 26, 2026), Theorem 1.3(ii), Proposition 2.1 and Section 6.1, introduce precisely the specialized equation and prove its normalized genus, maximality, automorphism triviality and ramification in the \(u\)-projection. Those results are assumed, not represented as new. Their discussion does not classify the singularity of its **ordinary projective plane closure**.

An earlier published analysis titled *The Weierstrass semigroup of a non-Galois twisted Artin--Schreier cover* treats the same more general affine equation up to a harmless sign, and determines the pole semigroup at the sole normalization point over \(u=\infty\), together with genus and certain ramification data. Its pole semigroup \(\langle p,p+j(d-1):1\le j<p\rangle\) is **not** the new local **plane branch** semigroup \(\langle d-p-1,d-1\rangle\), nor does it give the two-branch local normalization conductor or embedded contact at \(Q\).

The prior *First two point counts of prime-field maximal curves with trivial automorphism group* explicitly identifies two rational points off the affine chart, one over \(u=0\) and one over \(u=\infty\), and so already establishes that part of the boundary-point count. The present theorem's new content is the full embedded singularity type of their **common image** at \(Q\), branch semigroup, intersection multiplicity and conductor multidegree. These are not the rational-point or one-point-pole-semigroup formulas. Earlier or unindexed local computations under other presentations remain possible.

## Limitations

The theorem requires \(d>p+2\), \(p\nmid(d-1)\), a polynomial right-hand side, and algebraically closed odd-characteristic ground field for the geometric branch classification. It does not identify the minimal resolution graph, prove an analytic isomorphism to the monomial cusp, compute all Hilbert schemes or classify all plane embeddings of the underlying smooth curve. The two-generator value semigroup and Puiseux **characteristic** do not imply that all higher formal coefficients can be removed by coordinates. No independent mathematical audit has been performed, and priority against inaccessible or unindexed literature is not certified.

## References

1. D. Bartoli, H. Borges, M. Timpanella, G. Zini, *Maximal curves with trivial automorphism group*, arXiv:2610.35788v1 (first posted October 26, 2026), especially Theorem 1.3(ii), Proposition 2.1 and Section 6.1. https://arxiv.org/abs/2610.35788
2. *The Weierstrass semigroup of a non-Galois twisted Artin--Schreier cover*, publicly available mathematical record, especially its Finding, Proof, and Relationship to prior work. https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-the-weierstrass-semigroup-of-a-non-galois-twisted-artin-schreier--60088f5a2835/RESULT.md
3. *First two point counts of prime-field maximal curves with trivial automorphism group*, publicly available mathematical record, especially its analysis of boundary places. https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-first-two-point-counts-of-prime-field-maximal-curves-with-trivia--ce30fe86f123/RESULT.md
4. Standard local algebra of plane branches: tame Puiseux parametrization, the numerical-semigroup delta formula, and the Gorenstein plane-curve normalization conductor formula (as used and explained in the proof).
