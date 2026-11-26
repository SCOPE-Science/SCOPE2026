# The isotropic-conic locus of rank-one Nijenhuis operators on forms of \(\mathfrak{sl}_2\)

## Finding
Let \(k\) be a field with \(\operatorname{char} k\ne2\), and let \(\mathfrak g\) be any three-dimensional \(k\)-form of \(\mathfrak{sl}_2\). Put \(b=\kappa/4\), where \(\kappa\) is the Killing form. For nonzero \(u,v\in\mathfrak g\), define the rank-one endomorphism
\[
N_{u,v}(x)=b(v,x)u.
\]
Then, for all \(x,y\in\mathfrak g\), its Nijenhuis torsion is exactly
\[
\boxed{\mathcal T_{N_{u,v}}(x,y)=b(v,v)b(u,[x,y])u.}
\]
Consequently \(N_{u,v}\) is Nijenhuis if and only if \(b(v,v)=0\). The projectivized rank-one Nijenhuis locus, with its reduced variety structure, is the Segre variety
\[
\boxed{\mathbb P(\mathfrak g)\times C_b,\qquad C_b=\{[v]\in\mathbb P(\mathfrak g):b(v,v)=0\},}
\]
where \(C_b\) is a smooth conic. In particular, a nonzero rank-one Nijenhuis operator exists over \(k\) precisely when the Killing form is isotropic over \(k\).

For \(\mathfrak g=\mathfrak{sl}_2(\mathbb F_q)\) with every odd prime power \(q\), the exact number of rank-one Nijenhuis endomorphisms is
\[
\boxed{(q^2+q+1)(q^2-1).}
\]
Of these, exactly \((q-1)(q+1)^2\) square to zero. For **each fixed** nonzero \(t\in\mathbb F_q\), precisely \(q^2(q+1)\) have endomorphism trace \(t\). Every nonzero rank-one Nijenhuis operator satisfies \(N^2=(\operatorname{tr}N)N\).

## Assumptions and scope
A \(k\)-form of \(\mathfrak{sl}_2\) means a Lie algebra whose scalar extension to a separable closure is isomorphic to \(\mathfrak{sl}_2\). This assumption ensures that \(b\) is nondegenerate when \(2\ne0\). The Nijenhuis torsion convention is
\[
\mathcal T_N(x,y)=[Nx,Ny]-N\bigl([Nx,y]+[x,Ny]-N[x,y]\bigr).
\]
No assumption that \(k\) be algebraically closed or infinite is made. The geometric statement concerns the reduced projective locus of **nonzero rank-one** operators; it does not classify operators of higher rank or assert a scheme-theoretic description of the unreduced torsion equations. The finite-field statement concerns the split Lie algebra \(\mathfrak{sl}_2(\mathbb F_q)\) and all odd prime powers, including characteristic three.

## Proof
**1. Rank-one torsion identity.** Let \(\mathfrak g=\mathfrak{sl}_2(k)\). The Killing form is \(\kappa(x,y)=4\operatorname{tr}(xy)\), hence \(b(x,y)=\operatorname{tr}(xy)\). For a linear functional \(f\) and nonzero \(u\), put \(N(x)=f(x)u\). Direct expansion for arbitrary \(x,y\) gives:
\[
\mathcal T_N(x,y)=-u\{f(x)f([u,y])-f(y)f([u,x])-f(u)f([x,y])\}.
\]
Take the usual basis \(E,H,F\), with \([H,E]=2E\), \([H,F]=-2F\), \([E,F]=H\). Write \(u=aE+b_0H+cF\), and \(f(E)=A\), \(f(H)=B\), \(f(F)=C\). The scalar in braces on the three pairs \((E,H),(E,F),(H,F)\) is, respectively,
\[
 c(B^2+4AC),\qquad -b_0(B^2+4AC),\qquad a(B^2+4AC).
\]
If \(f(x)=b(v,x)\), then \(v=CE+(B/2)H+AF\), and \(B^2+4AC=2b(v,v)\). Moreover
\[
 b(u,[E,H])=-2c,\quad b(u,[E,F])=2b_0,\quad b(u,[H,F])=-2a.
\]
These three evaluations establish the boxed torsion identity for every pair by bilinearity and alternation, including characteristic three.

**2. Descent and nonvanishing.** The displayed tensor identity is polynomial in the bracket, \(b,u,v,x,y\) and is invariant under isomorphism; it therefore holds for any form after extension to a separable closure and hence over the original field. For nonzero \(u\), there exist \(x,y\) with \(b(u,[x,y])\ne0\), since \([\mathfrak g,\mathfrak g]=\mathfrak g\) and \(b\) is nondegenerate. Thus the tensor vanishes identically exactly when \(b(v,v)=0\).

**3. Geometry.** Each nonzero rank-one endomorphism has a factorization \(b(v,\cdot)u\), unique up to \((u,v)\mapsto(\lambda u,\lambda^{-1}v)\) for \(\lambda\in k^\times\). Hence the reduced projectivized rank-one locus is the Segre image of \(\mathbb P(\mathfrak g)\times C_b\). Nondegeneracy of \(b\) in odd characteristic makes \(C_b\) a smooth plane conic; its rational points are exactly isotropic lines.

**4. Counting.** Over \(\mathbb F_q\), set \(v=rE+sH+tF\). Since \(b(v,v)=2(s^2+rt)\), the nilpotent cone contains exactly \(q^2\) vectors: if \(r\ne0\), the \(q-1\) choices of \(r\) and \(q\) choices of \(s\) determine \(t\); if \(r=0\), necessarily \(s=0\) and \(t\) is arbitrary. Thus \(q^2-1\) nonzero \(v\)'s are admissible. There are \(q^3-1\) nonzero \(u\)'s, and each rank-one map is represented by exactly \(q-1\) pairs, proving the total count.

For fixed nonzero \(v\), the nonzero functional \(b(v,\cdot)\) has a kernel of size \(q^2\). There are \(q^2-1\) nonzero \(u\)'s with \(b(v,u)=0\), and for each prescribed \(t\ne0\) exactly \(q^2\) vectors with \(b(v,u)=t\). Divide the corresponding pair counts by \(q-1\) to obtain \((q-1)(q+1)^2\) for trace zero and \(q^2(q+1)\) for every fixed nonzero trace. Finally \(N^2(x)=b(v,u)N(x)\), so square-zero is equivalent to trace zero.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. It independently checks the rank-one torsion expansion against the direct Lie-bracket definition on all nonzero tensor presentations \((u,f)\) for \(q=3,5,7\), tests the exact uniform number of admissible covectors for each nonzero image vector, and checks both trace strata and the final formula. For these fields the checked counts are respectively \(104\), \(744\), and \(2736\). This finite verification supplements, but does not replace, the argument valid for all odd prime powers and all forms.

## Relationship to prior work
Liu, Sheng, Zhou and Bai (arXiv:1601.02356v1, first posted 2016-01-11) place algebraic Nijenhuis operators in the deformation framework and give the defining identity in their Definition 3.4. The present result classifies the entire nonzero rank-one stratum specifically for forms of \(\mathfrak{sl}_2\), not merely examples or polynomial closure. Zhikhareva (arXiv:2410.10536v1, posted 2024-10-14), especially Theorems 1–3 and Section 6, classifies existence and eigenbases of **regular semisimple** operators on real and complex three-dimensional Lie algebras; these are disjoint from the rank-one stratum in dimension three. Neither inspected work presents the isotropic-conic description or the exact odd-finite-field trace-refined count. This is a bounded literature comparison, not a proof of worldwide publication priority.

## Limitations
Characteristic two is excluded because the trace/Killing normalization and the simple Lie algebra structure change. The theorem does not enumerate higher-rank Nijenhuis operators, describe the unreduced scheme of torsion equations, or classify automorphism orbits inside the rank-one locus. The originality assessment is limited to the explicitly inspected literature and searched research records; an unknown stronger source could subsume the result.

## References
1. J. Liu, Y. Sheng, Y. Zhou, C. Bai, *Nijenhuis operators on \(n\)-Lie algebras*, arXiv:1601.02356v1 (2016-01-11), especially Definition 3.4 and Section 4. https://arxiv.org/abs/1601.02356
2. E. S. Zhikhareva, *Three-dimensional Lie algebras admitting regular semisimple algebraic Nijenhuis operators*, arXiv:2410.10536v1 (2024-10-14), Theorems 1–3 and Section 6. https://arxiv.org/abs/2410.10536
