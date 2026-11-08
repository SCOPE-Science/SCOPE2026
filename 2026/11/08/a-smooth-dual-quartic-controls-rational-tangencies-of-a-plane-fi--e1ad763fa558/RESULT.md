# A smooth dual quartic controls rational tangencies of a plane-filling pencil

## Finding
Let \(q\) be an odd prime power and let \(k\in\mathbb F_q\) be such that \(f_k(T)=T^7+kT^3-1\) has no root in \(\mathbb F_q\). Consider the plane-filling curve
\[
C_k:\quad X^2(X^qY-XY^q)+Y^2(Y^qZ-YZ^q)+(Z^2+kX^2)(Z^qX-ZX^q)=0.
\]
For \(j\in\{0,1,2\}\), let \(N_j\) be the number of \(\mathbb F_q\)-lines tangent to \(C_k\) at exactly \(j\) **distinct smooth \(\mathbb F_q\)-points**. Define the dual-coordinate plane quartic
\[
D_k:\quad H_k(A,B,C)=A^3B+B^3C+AC^3+k(B^4+ABC^2)=0.
\]
Then \(D_k\) is geometrically smooth (so has genus \(3\)), no \(\mathbb F_q\)-line is tangent to \(C_k\) at more than two rational points, and
\[
\boxed{N_1=\#D_k(\mathbb F_q),\qquad N_0=N_2=\frac{q^2+q+1-\#D_k(\mathbb F_q)}{2}.}
\]
In particular, writing \(\epsilon_k=\#D_k(\mathbb F_q)-(q+1)\), the exact number of rational lines not tangent at any rational point is \((q^2-\epsilon_k)/2\), where \(|\epsilon_k|\le6\sqrt q\).

## Assumptions and scope
The field \(\mathbb F_q\) has odd cardinality; \(k\) is a field element satisfying the displayed root-free condition. The high-degree curve \(C_k\) contains every rational point of the plane and is smooth *at those rational points*. No geometric smoothness assertion about \(C_k\) at points over larger extensions is needed or made. The quartic \(D_k\) is a separate, geometrically smooth curve in the **dual projective plane**. The integer \(N_j\) counts rational lines according to their *rational* points of tangency only: nonrational tangencies are not counted. All conclusions hold for prime powers, not just prime fields.

## Proof
**(1) Rational smoothness.** Every \(\mathbb F_q\)-point is on \(C_k\), since each Frobenius bracket vanishes there. At a rational point \([x:y:z]\), the partial derivatives of the defining polynomial are
\[
(G_0,G_1,G_2)=(z^3+kx^2z-x^2y,\ x^3-y^2z,\ y^3-xz^2-kx^3).
\]
If these three vanish, then \(x\ne0\): when \(x=0\), the first gives \(z=0\) and the third gives \(y=0\). Normalize \(x=1\). The middle equation gives \(z=y^{-2}\); the third gives \(k=y^3-y^{-4}\), and the first then vanishes automatically. Setting \(t=y^{-1}\), this is equivalent to \(t^7+kt^3-1=0\). Thus the root-free hypothesis is precisely the condition for all rational points to be smooth.

**(2) A residual quadratic on each line.** Write an arbitrary rational line \(\ell\) as \(aX+bY+cZ=0\), and parametrize it by \(P(u,v)=uV+vW\) with \(V,W\in\mathbb F_q^3\) independent and \(V\times W=(a,b,c)\). On \(\ell\), every Frobenius bracket is a constant minor of \(V,W\) times \(u^qv-uv^q\). Hence
\[
F_k(P(u,v))=(u^qv-uv^q)Q_\ell(P(u,v)),\qquad
Q_\ell=(c+kb)X^2+aY^2+bZ^2.
\]
The binary quadratic \(Q_\ell|_\ell\) never vanishes identically for odd characteristic. For \(c\ne0\), substituting \(Z=-(aX+bY)/c\), its mixed coefficient is \(2ab^2/c^2\). If all coefficients vanished, this forces \(a=0\) or \(b=0\), and the remaining pure coefficients then force \(a=b=0\), leaving coefficient \(c\ne0\), a contradiction. For \(c=0,b\ne0\), the \(Z^2\)-coefficient equals \(b\ne0\); for \(b=c=0\), the restriction is \(aY^2\ne0\). In particular \(\ell\) is never a component of \(C_k\).

The polynomial \(u^qv-uv^q\) has simple zeros at exactly the \(q+1\) rational points of \(\ell\). Since \(C_k\) is smooth there, \(\ell\) is the tangent line at a rational point \(P\in\ell\) if and only if \(Q_\ell(P)=0\). A nonzero binary quadratic over \(\mathbb F_q\) has \(0,1\), or \(2\) rational projective roots.

**(3) The quartic discriminant.** Restricting \(Q_\ell\) to \(\ell\), the determinant of its binary quadratic form vanishes precisely when
\[
(a,b,c)\,\operatorname{adj}\bigl(\operatorname{diag}(c+kb,a,b)\bigr)(a,b,c)^\top
=a^3b+b^3c+ac^3+k(b^4+abc^2)=0.
\]
This identity follows from the usual two-dimensional determinant/adjugate formula (and remains valid when the diagonal ternary form is degenerate). In odd characteristic, a nonzero binary quadratic has exactly one rational projective zero if and only if its determinant is zero. Therefore \(N_1=\#D_k(\mathbb F_q)\).

**(4) Geometric smoothness of the quartic.** We show that a singular point of \(D_k\) would force a rational root of \(f_k\). Let \(p\) be the characteristic. At \(C=0\), the derivative \(H_C=B^3\), so a singular point would have \(B=0\), but then \(H_B=A^3\) forces \(A=0\), impossible. Thus normalize \(C=1\), writing \(a=A,b=B\). The three partial derivatives become
\[
H_A=3a^2b+kb+1,\quad H_B=a^3+3b^2+4kb^3+ka,\quad
H_C=b^3+3a+2kab.
\]
If \(p=3\), the first derivative implies \(k\ne0\), \(b=-1/k\). The third gives \(a=1/k^3\), and then the second equals \(a^3\ne0\), contradiction.

Suppose \(p\ne3\) (and \(p\) is odd). At a common zero of the derivatives, \(ab\ne0\). Put \(u=kb\). Using the integral polynomial identity \(3bH_B=aH_A+3(3+4kb)H_C-4a(kb+1)(6kb+7)\), the simultaneous vanishing of the three derivatives gives
\[
\frac{-4a}{3}(u+1)(6u+7)=0.
\]
The factor \(u+1\) cannot vanish, since then \(a^2b=0\). Hence \(6u+7=0\). If \(p=7\), this forces \(k=0\), contradicting the root-free hypothesis because \(f_0(1)=0\). If \(p\ne7\), then \(k\ne0\) and \(b=-7/(6k)\). The first and third derivatives now give \(a^2b=1/18\) and \(a=-3b^3/2\), so \(b^7=2/81\), equivalently
\[
2^8 3^3 k^7+7^7=0.
\]
The rational element \(t=-12k^2/49\) consequently satisfies \(t^4=-3k/7\) and \(t^3=7/(4k)\). Therefore \(t^7+kt^3-1=0\), again a contradiction. Thus \(D_k\) has no geometric singularities. A smooth plane quartic is geometrically integral of genus three.

**(5) Exact line spectrum and bound.** There are \(M=q^2+q+1\) rational points and the same number of rational lines. Every rational point of \(C_k\) has a unique rational tangent, so counting point--tangent-line incidences yields \(N_1+2N_2=M\). As \(N_0+N_1+N_2=M\), it follows that \(N_0=N_2=(M-N_1)/2\). The Hasse--Weil inequality on the smooth genus-three curve \(D_k\) gives \(|\#D_k(\mathbb F_q)-(q+1)|\le6\sqrt q\), finishing the proof.

## Verification
The supplied dependency-free Python verifier enumerates projective points and lines over the prime fields \(\mathbb F_p\) for \(p=3,5,7,11,13,17,19,23,29\), checks all \(41\) parameters with no rational root of \(f_k\), recomputes the explicit tangent map, the quartic zeros, and their asserted equality. For \(p\le17\) it separately tests every point/line incidence rather than relying only on tangent-map fibers. Representative \((p,k;N_1,N_2,N_0)\) outputs are \((3,2;5,4,4)\), \((5,4;5,13,13)\), \((7,1;11,23,23)\), \((7,3;7,25,25)\), \((11,4;17,58,58)\), and \((29,4;25,423,423)\). The proof above, not these finite tests, establishes the statement for every odd prime power.

## Relationship to prior work
Asgarli and Ghioca introduced this explicit degree-\(q+3\) plane-filling pencil and proved the rational-smoothness criterion and absence of rational line components; those are prior results and are reproved here only to make the incidence argument self-contained. The new assertion is the **exact full rational-tangent-line spectrum**, its expression via the explicitly identified **geometrically smooth genus-three dual quartic**, and the resulting uniform \(O(\sqrt q)\) error term. Their paper addresses smoothness and parameter existence, not this dual quartic or line spectrum. Their separate tangent-filling paper concerns a different covering property; Homma's earlier plane-filling work concerns degree \(q+2\) and its fragments. An older equivalent incidence calculation under other terminology has not been excluded categorically.

## Limitations
The theorem concerns only tangencies at rational smooth points, not the complete geometric dual or all nonrational tangencies. It neither resolves the global smoothness conjecture for \(C_k\) nor determines the zeta function of \(D_k\) for general \(k\). The Hasse--Weil inequality bounds the quartic's point count but does not determine it from \(q\) alone. No independent external audit of the result has been performed.

## References
- S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072, first version 2023-07-06, https://arxiv.org/abs/2307.03072 ; lawful author full text: https://personal.math.ubc.ca/~dghioca/papers/0706_plane_filling_curves.pdf .
- S. Asgarli and D. Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, 2023, https://arxiv.org/abs/2302.13420 .
- M. Homma, *Fragments of plane filling curves of degree q+2 over the finite field of q elements, and of affine-plane filling curves of degree q+1*, Linear Algebra Appl. 589 (2020), 9–27, DOI:10.1016/j.laa.2019.12.012.
- M. Homma and S. J. Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups*, Linear Algebra Appl. 438 (2013), 969–985, DOI:10.1016/j.laa.2012.08.032.
