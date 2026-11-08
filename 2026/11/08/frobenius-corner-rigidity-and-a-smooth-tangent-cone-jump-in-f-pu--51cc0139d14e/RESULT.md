# Frobenius-corner rigidity and a smooth-tangent-cone jump in F-pure thresholds

## Finding

Let \(k\) be a field of characteristic \(p>0\), \(r\ge1\), \(q=p^r\ge4\), and \(n\ge2\). In \(R=k[[x_1,\ldots,x_n]]\), write \(\mathfrak m=(x_1,\ldots,x_n)\). For \(f\in\mathfrak m\), define \(I_e=(x_1^{p^e},\ldots,x_n^{p^e})\) and
\[
\nu_e(f)=\max\{N\ge0:f^N\notin I_e\},\qquad
\operatorname{fpt}_{\mathfrak m}(f)=\lim_{e\to\infty}\frac{\nu_e(f)}{p^e}.
\]

**Frobenius-corner rigidity.** For any \(n\ge1\), any \(c\in k^\times\), and any \(h\in(x_1^q,\ldots,x_n^q)\), put \(f=c\prod_{i=1}^n x_i^{q-1}+h\). Then for every \(e\ge1\),
\[
\boxed{\nu_e(f)=\left\lfloor\frac{p^e-1}{q-1}\right\rfloor,\qquad
\operatorname{fpt}_{\mathfrak m}(f)=\frac1{q-1}.}
\]
This is a statement about the full Frobenius quotient, not an approximation from a leading homogeneous form.

**Geometric jump.** For \(n\ge2\), define
\[
f_\lambda=\sum_{i=1}^n x_i^{q+1}+\lambda\prod_{i=1}^n x_i^{q-1},\qquad \lambda\in k.
\]
Each germ \((f_\lambda=0,0)\) is an isolated ordinary multiple-point hypersurface with the **same smooth projective tangent cone** \(\sum x_i^{q+1}=0\), the **same multiplicity** \(q+1\), and the **same Milnor number** \(q^n\), but
\[
\boxed{\operatorname{fpt}_{\mathfrak m}(f_\lambda)=
\begin{cases}
1/q,&\lambda=0,\\
1/(q-1),&\lambda\ne0.
\end{cases}}
\]
Thus even the simultaneous data of a smooth tangent cone and its isolated singularity's Milnor number do not determine the F-pure threshold. The exact positive jump is \(1/[q(q-1)]\).

## Assumptions and scope

The field can be arbitrary for the exponent and threshold identities; the geometric interpretation uses an algebraically closed field. In every case \(p\) is prime, \(r\ge1\), \(q=p^r\ge4\), \(n\ge2\) for the geometric family, and \(\lambda\) is any field element. The corner lemma permits any \(n\ge1\). All threshold statements are local at the origin and use the maximal-ideal Frobenius powers, not global thresholds or characteristic-zero log canonical thresholds.

For \(n=2\), a smooth projective tangent cone means a reduced collection of \(q+1\) distinct directions in \(\mathbb P^1\); the local curve may have multiple analytic branches. For \(n>2\), the tangent cone is a smooth projective hypersurface of positive dimension.

## Proof

**1. The exact corner congruence.** Put \(m=q-1\), \(P=\prod x_i\), \(Q_s=q^s=p^{rs}\), and \(a_s=(Q_s-1)/m\) for \(s\ge1\). We prove
\[
f^{a_s}\equiv c^{a_s}P^{Q_s-1}\pmod{I_{rs}}. \tag{1}
\]
For \(s=1\), \(a_1=1\), and this is exactly the hypothesis \(f\equiv cP^m\pmod{I_r}\). If (1) holds, raise it to the \(q\)-th power: in characteristic \(p\), Frobenius sends \(I_{rs}\) into \(I_{r(s+1)}\). Multiply by \(f\). Every term from \(h\in I_r\) then has at least one variable exponent at least \((Q_{s+1}-q)+q=Q_{s+1}\), so vanishes modulo \(I_{r(s+1)}\). The surviving term is \(c^{q a_s+1}P^{q(Q_s-1)+m}\); because \(a_{s+1}=qa_s+1\), it is exactly (1) at \(s+1\).

For an arbitrary \(e\ge1\), uniquely write \(e=rs+t\) with \(s\ge0\) and \(0\le t<r\). When \(s=0\), \(f\in I_e\) and \(\nu_e(f)=0\). Otherwise set \(N=p^ta_s=\lfloor(p^e-1)/m\rfloor\). Raising (1) to the \(p^t\)-th power gives
\[
f^N\equiv c^N P^{p^e-p^t}\pmod {I_e}, \tag{2}
\]
which is nonzero. Multiplication by every monomial of \(f\) kills the right-hand side modulo \(I_e\): the corner term adds \(m=q-1\ge p^t\) to every exponent, and every monomial in \(h\) adds at least \(q\) in one exponent. Thus \(f^{N+1}\in I_e\); together with (2) this proves \(\nu_e(f)=N\) and the limit \(1/m\).

**2. The unperturbed Fermat sum.** Set \(F=\sum x_i^{q+1}\). If \(e<r\), then \(F\in I_e\) and \(\nu_e(F)=0\). If \(e=r+s\) with \(s\ge0\), let \(M=p^s\). Frobenius gives \(F^M=\sum x_i^{(q+1)M}\in I_e\), so \(\nu_e(F)\le M-1\). For \(s\ge1\), choose \(a=\lfloor(M-1)/2\rfloor\), \(b=M-1-a\). The monomial \(x_1^{(q+1)a}x_2^{(q+1)b}\) in \(F^{M-1}\) has coefficient \(\binom{M-1}{a}\not\equiv0\pmod p\) by Lucas's theorem (all base-\(p\) digits of \(M-1\) equal \(p-1\)). Both variable exponents are smaller than \(qM=p^e\), because \((q+1)\lceil(M-1)/2\rceil<qM\) for \(q\ge4\). Distinct multinomial choices yield distinct monomials, so no cancellation is possible. This survives modulo \(I_e\), and \(\nu_e(F)=M-1\). The case \(s=0\) has \(M-1=0\) and the same formula. Consequently the limit of \(\nu_e(F)/p^e\) is \(1/q\).

**3. Tangent cone and Milnor number.** Since \(n(q-1)>q+1\) for \(n\ge2,q\ge4\), the order-\((q+1)\) homogeneous initial form of every \(f_\lambda\) is \(H=\sum x_i^{q+1}\), and the multiplicity is \(q+1\). Because \(q\equiv0\pmod p\), its partial derivatives are \(\partial_iH=x_i^q\); these have no common zero in projective space. Thus \(V(H)\subset\mathbb P^{n-1}\) is smooth.

For the same strict inequality, the terms \(\partial_i(\lambda P^{q-1})\) have total order \(n(q-1)-1>q\). Hence the \(\mathfrak m\)-initial forms of the partial derivatives of \(f_\lambda\) are exactly \(x_1^q,\ldots,x_n^q\), a homogeneous regular sequence. The filtered regular-sequence/Koszul criterion shows that the associated graded Jacobian quotient is \(k[x_1,\ldots,x_n]/(x_1^q,\ldots,x_n^q)\). Its length is \(q^n\), so the singularity is isolated and its Milnor number, the Jacobian quotient length, equals \(q^n\) for every \(\lambda\). With \(\lambda\ne0\), the corner rigidity of Step 1 applies since \(\sum x_i^{q+1}\in I_r\); with \(\lambda=0\), Step 2 applies. This proves every assertion.

## Verification

The accompanying `VERIFY_FPT.py` performs *finite* exact sparse-polynomial computations modulo \(I_e\), checking both the surviving critical power and the vanishing of the next power. Tested tuples \((p,r,n,e_{\max})\) were \((2,2,2,6)\), \((2,2,3,4)\), \((3,2,2,4)\), \((5,1,2,3)\), and \((2,3,2,5)\), for \(\lambda=0,1\). The verifier returns `CERTIFICATE_OK` when all assertions pass. These finitely many tests are consistency checks; the symbolic Frobenius induction and the Jacobian initial-form argument supply the all-degree proof.

## Relationship to prior work

Y. Svoray's *Bounds on the F-Pure Threshold of Isolated Hypersurface Singularities* (arXiv:2606.04014, first posted 2026-05-31) develops inequalities from Milnor and Tjurina numbers and includes an explicit characteristic-two plane-branch example \(x^5+y^7+x^3y^3\) whose threshold jumps relative to \(x^5+y^7\) (Example 3.8 in the HTML presentation). That motivating example has a singular/nonhomogeneous weighted-initial curve and concerns one characteristic/two exponents; its Frobenius-monomial technique is acknowledged here. The present theorem does not claim the technique or the existence of *some* threshold jump as new. Its distinct statement is a universal exact corner congruence and an arbitrary-prime, arbitrary-dimension jump with *the same smooth projective tangent cone and identical Milnor number*.

K. E. Smith's *Values of the F-pure threshold for homogeneous polynomials* (2023) concerns homogeneous forms and their threshold strata, including Fermat-type examples; it does not itself classify the nonhomogeneous family above. Hernández–Núñez-Betancourt–Witt (2018) prove local \(\mathfrak m\)-adic constancy for a fixed isolated singularity, which does not force constancy on the perturbation of degree \(n(q-1)\) considered here. Historical priority requires additional independent comparison against general deformation and finite-determinacy literature; the absence of a found equivalent is not a uniqueness certificate.

## Limitations

This is an exact local theorem in characteristic \(p\); it is not a statement about all ordinary multiple points, their moduli, their Tjurina numbers, or their log canonical thresholds. The corner lemma's arbitrary perturbation class is specified by the *Frobenius ideal* \((x_i^q)\), not by an unrestricted total-degree jet. The displayed geometric family is a particular natural deformation of Fermat singularities, not a classification of all possible threshold jumps. Computations do not substitute for the infinite proof. No independent mathematical audit or exhaustive historical-priority check has been performed.

## References

1. Y. Svoray, *Bounds on the F-Pure Threshold of Isolated Hypersurface Singularities*, arXiv:2606.04014 (first public version, 2026-05-31), https://arxiv.org/abs/2606.04014.
2. K. E. Smith, *Values of the F-pure threshold for homogeneous polynomials*, J. London Math. Soc. 108 (2023), 1004–1035, https://doi.org/10.1112/jlms.12774.
3. D. J. Hernández, L. Núñez-Betancourt, and E. E. Witt, *Local m-adic constancy of F-pure thresholds and test ideals*, Math. Proc. Cambridge Philos. Soc. 164 (2018), 285–295, https://arxiv.org/abs/1801.05506.
