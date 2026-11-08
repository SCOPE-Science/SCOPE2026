# Uniform finite-field census and twenty automorphism orbits of idempotent Rota–Baxter splittings on triangular matrices

## Finding
Let \(k\) be any field, and let \(A=T_2(k)\) be the three-dimensional associative algebra of upper-triangular \(2\times2\) matrices. An idempotent weight-minus-one Rota–Baxter map is a \(k\)-linear map \(P:A\to A\) with
\[
P^2=P,\qquad P(x)P(y)=P\bigl(P(x)y+xP(y)-xy\bigr)\quad\text{for all }x,y\in A.
\]
All automorphisms in the classification are \(k\)-linear **algebra** automorphisms of \(A\), acting by \(P\mapsto\phi P\phi^{-1}\); no identification under anti-automorphisms or interchange of image and kernel is imposed.

**Theorem.** For each prime power \(q\), the rank-generating polynomial of all these maps over \(\mathbb F_q\), where rank means the linear rank on \(A\), is exactly
\[
\boxed{1+(2q^2+3q+2)T+(2q^2+3q+2)T^2+T^3.}
\]
In particular, the total is \(\boxed{4q^2+6q+6}\). Over **every field** \(k\), the automorphism group of \(A\) has exactly \(\boxed{20}\) orbits on this set: one at each rank zero and three, and nine at each rank one and two. For finite \(k=\mathbb F_q\), the nine rank-one orbits have sizes
\[
\boxed{1,1,q,q,q,q,q,q(q-1),q(q-1)},
\]
and rank two has the identical orbit-size multiset. The rank-specific orbit representatives and all exceptional characteristic-two cases are covered by the proof below.

The classical equivalence between an idempotent weight-minus-one Rota–Baxter map and a decomposition into complementary subalgebras is not claimed as new. Neither is the characteristic-zero classification of all (not necessarily idempotent) weight-one maps on three-dimensional associative algebras. The assessed contribution is the exact all-characteristic finite-field rank census and the uniform automorphism-orbit refinement.

## Assumptions and scope
Write \(e=E_{11}\), \(f=E_{22}\), \(z=E_{12}\), \(1=e+f\); the nonzero basis products are \(e^2=e\), \(f^2=f\), \(ez=z\), \(zf=z\). A subalgebra is a \(k\)-linear subspace closed under multiplication; it need not contain the identity of \(A\). For \(s,t\in k\), put
\[
L_e(s)=k(e+sz),\quad L_f(s)=k(f+sz),\quad L_1=k1,\quad J=kz,
\]
\[
Q_e=ke+kz,\quad Q_f=kf+kz,\quad Q_\Delta=k1+kz,\quad U_t=k(e+tz)+k(f-tz).
\]
The use of minus signs is valid in characteristic two, where \(-t=t\).

## Proof
**1. Projection correspondence.** For \(P^2=P\), set \(B=\operatorname{im}P\) and \(C=\ker P\). Then \(A=B\oplus C\) as vector spaces. If the Rota–Baxter identity holds, for \(x,y\in B\) it reduces to \(xy=P(xy)\), so \(B\) is a subalgebra; for \(x,y\in C\), it says \(P(xy)=0\), so \(C\) is a subalgebra. Conversely, writing \(x=b+c\), \(y=b'+c'\) with \(b,b'\in B\), \(c,c'\in C\), one obtains
\[
P(x)y+xP(y)-xy=bb'-cc',
\]
so projection onto \(B\) satisfies the identity precisely when both summands are subalgebras. Therefore idempotent operators are in bijection with **ordered** complementary subalgebra pairs \((B,C)\).

**2. Complete low-dimensional subalgebras.** A nonzero line \(kv\) is a subalgebra exactly when \(v^2\in kv\). The diagonal coefficients of \(v=ae+df+bz\) give \(a^2=\lambda a\), \(d^2=\lambda d\). If \(a=d=0\), this gives \(J\); if just one of \(a,d\) is nonzero, rescaling gives \(L_e(s)\) or \(L_f(s)\); if both are nonzero, they equal \(\lambda\), and the off-diagonal equation \((a+d)b=\lambda b\) forces \(b=0\), yielding \(L_1\). Thus the line subalgebras are exactly \(J,L_1,L_e(s),L_f(s)\).

For a two-dimensional subalgebra \(D\), let \(\pi:A\to A/J\simeq k\times k\). If \(J\subseteq D\), then \(\pi(D)\) is a subalgebra line of \(k\times k\), hence one of the two coordinate axes or the diagonal; their preimages give exactly \(Q_e,Q_f,Q_\Delta\). If \(J\cap D=0\), projection \(\pi|_D\) is an isomorphism of vector spaces onto \(k^2\), and \(D\) is a graph \(\{ae+df+(sa+td)z:a,d\in k\}\). Multiplicative closure of the lifts of \(e,f\) forces \(s+t=0\); the graph is exactly \(U_s\). All listed spaces are indeed subalgebras. No other lines or planes exist. In particular, \(U_t\) is the graph of a complementary semisimple subalgebra, not a plane containing \(J\).

**3. Complement census.** A line and plane in the three-dimensional space are complementary precisely when the line is not contained in the plane. There are \(q\) choices of complementary plane for \(B=J\), namely all \(U_t\). For \(B=L_1\), the only complementary planes are \(Q_e,Q_f\). For \(B=L_e(s)\), precisely \(Q_e,U_s\) among the \(q+3\) planes contain it; the \(q+1\) complements are \(Q_f,Q_\Delta,U_t\) for \(t\ne s\). For \(B=L_f(s)\), precisely \(Q_f,U_{-s}\) contain it; complements are \(Q_e,Q_\Delta,U_t\) for \(t\ne-s\). Consequently the number of ordered pairs with line image is
\[
q+2+q(q+1)+q(q+1)=2q^2+3q+2.
\]
Reversing every ordered pair gives the same count for plane image. Rank zero and rank three give only the zero map and identity respectively, proving the polynomial and total.

**4. Automorphism group and orbits.** The radical \(J=kz\) is characteristic. An algebra automorphism induces the identity (not the swap) on the two primitive quotient idempotents: the property \(eJ=J\), \(Je=0\) distinguishes their order. Every automorphism has the unique form
\[
\phi_{\tau,\lambda}(e)=e+\tau z,\quad \phi_{\tau,\lambda}(f)=f-\tau z,\quad \phi_{\tau,\lambda}(z)=\lambda z,
\qquad \tau\in k,\quad \lambda\in k^\times.
\]
It fixes \(J,L_1,Q_e,Q_f,Q_\Delta\) and acts by
\[
L_e(s)\mapsto L_e(\tau+\lambda s),\quad L_f(s)\mapsto L_f(-\tau+\lambda s),\quad U_t\mapsto U_{\tau+\lambda t}.
\]
Representatives for the **nine rank-one orbits** are exactly the following ordered image/kernel pairs (the displayed \(1\in k\) is the multiplicative identity):

| Image \(B\) | Kernel \(C\) | Orbit size over \(\mathbb F_q\) |
|---|---|---:|
| \(J\) | \(U_0\) | \(q\) |
| \(L_1\) | \(Q_e\) | \(1\) |
| \(L_1\) | \(Q_f\) | \(1\) |
| \(L_e(0)\) | \(Q_f\) | \(q\) |
| \(L_e(0)\) | \(Q_\Delta\) | \(q\) |
| \(L_e(0)\) | \(U_1\) | \(q(q-1)\) |
| \(L_f(0)\) | \(Q_e\) | \(q\) |
| \(L_f(0)\) | \(Q_\Delta\) | \(q\) |
| \(L_f(0)\) | \(U_1\) | \(q(q-1)\) |

Indeed, the additive translations normalize any \(L_e(s)\) or \(L_f(s)\) to parameter zero, leaving the nonzero difference between a line parameter and the associated forbidden \(U\)-parameter rescaled by \(k^\times\). That difference is a single nonzero orbit. Every pair in the complement census lies in exactly one displayed class; orbit representatives are distinct because the ambient radical, unit, and the two oriented idempotent-line families are invariant, and the indicated kernel types cannot be interchanged by an automorphism. For rank-two projections, swap each representative's ordered image and kernel; swapping is merely an enumeration bijection and is **not** part of the conjugacy action. Each rank-two orbit has the same size as its swapped rank-one orbit. The ranks zero and three contribute one orbit each. This proves exactly \(1+9+9+1=20\) orbits for every field, including \(\mathbb F_2\).

## Verification
Two independent computational approaches accompany the proof. `verify_rb.py` exhausts all \(q^9\) linear maps on the three-dimensional vector space for \(q=2,3\), checks idempotence and every Rota–Baxter identity on basis pairs by direct multiplication, obtains rank vectors \((1,16,16,1)\) and \((1,29,29,1)\), then enumerates actual automorphism-conjugation orbits. `verify_splittings.py` independently enumerates all lines and planes, checks closure and complementarity, and tests \(q=2,3,4,5\), implementing \(\mathbb F_4\) as \(\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\); predicted totals are \(34,60,94,136\). The accompanying `.out` files are actual program outputs; neither a finite test nor the output alone proves an all-field classification.

## Relationship to prior work
An and Bai, *From Rota-Baxter Algebras to Pre-Lie Algebras* (2007), Proposition 4.2 (their case T9), already classify **all weight-one operators** on complex three-dimensional associative algebras, including an algebra equivalent to \(T_2(\mathbb C)\). Since multiplying a weight-minus-one operator by minus one yields weight plus one, their classification **already covers the characteristic-zero operator-classification problem on this algebra**. The present theorem **does not claim a new characteristic-zero parameterization of all such operators**: its additional assertions are the exact rational-point count and rank histogram for every finite field and the explicitly stratified 20 algebra-automorphism orbits uniformly for arbitrary fields. These statements are not given in their tables, although they could be further derived by a substantial specialty-by-specialty analysis. Their normal forms are a strong priority warning, not an irrelevant neighboring paper.

Jian's 2013 article (arXiv:1307.6966) supplies a general idempotent weight-minus-one projection construction. It neither classifies all complementary subalgebra decompositions of this specific algebra nor gives the rational-point or automorphism-orbit formulas. Li and Liu's 2015 analysis concerns weight-one operators on the **full four-dimensional** algebra \(M_2\) over algebraically closed fields. Restricting or extending operators is not an automatic bijection of the two operator spaces, nor does their \(\operatorname{PGL}_2\)-action determine \(\operatorname{Aut}(T_2)\)-orbits. Earlier weight-zero triangular-algebra enumerations also concern a different operator identity. Exact historical priority for the count/orbit refinement remains unverified beyond the literature inspected.

## Limitations
The theorem treats **idempotent** maps only, not all non-idempotent Rota–Baxter operators; the results for arbitrary fields concern orbits, while point counts require finite fields. The result is an explicit small-algebra baseline, not a statement about arbitrary triangular matrix size. It makes no claim about the nonreduced scheme of all operator equations, classification of operators on \(M_2\), or independence from the cited characteristic-zero normal forms. No independent mathematical audit has been carried out.

## References
1. H. An and C. Bai, *From Rota-Baxter Algebras to Pre-Lie Algebras*, arXiv:0711.1389v1 (November 9, 2007), Proposition 4.2, pp. 13–17. https://arxiv.org/abs/0711.1389
2. R.-Q. Jian, *Construction of Rota-Baxter algebras via Hopf module algebras*, arXiv:1307.6966v1 (July 26, 2013), especially the projection construction. https://arxiv.org/abs/1307.6966
3. J. Li and W. Liu, *Rota-Baxter Operators of Weight 1 on 2×2-Matrix Algebras*, Communications in Mathematical Research **31** (2015), 71–80, https://doi.org/10.13447/j.1674-5647.2015.01.08.
4. S. Zheng, L. Guo and M. Rosenkranz, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, arXiv:1402.3702 (February 15, 2014), weight-zero comparison. https://arxiv.org/abs/1402.3702
