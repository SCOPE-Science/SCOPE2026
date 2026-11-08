# Universal maximal Tjurina length for Artin--Schreier plane embeddings

## Finding
Let \(k\) be an algebraically closed field of characteristic \(p>0\), let \(q=p^e\) with \(e\ge1\), and let \(g(T)=\sum_{j=0}^{m}a_jT^j\in\mathbb F_p[T]\) have degree \(m\), with \(d=pm>q\). Put \(r=d-q\) and
\[
G(X,Z)=\sum_{j=0}^{m}a_jX^{pj}Z^{p(m-j)}.
\]
Consider the reduced projective plane curve
\[
C_{q,g}:\quad Y^qZ^r-G(X,Z)-XZ^{d-1}=0\quad\text{in }\mathbb P^2_k.
\]
Its singular subscheme is supported at the unique point \(P=[0:1:0]\). The local Tjurina algebra at \(P\) has **length exactly \((d-1)^2\)**, regardless of \(q\) and of the coefficients of \(g\) apart from its nonzero leading coefficient. More precisely, writing \(x=X/Y,z=Z/Y\) in the affine chart \(Y\ne0\), and letting \(\mathfrak m=(x,z)\), there is an explicit presentation
\[
\mathcal T_P\cong
\frac{k[[x,z]]}{\bigl(h,\ z^{d-2}\mathfrak m\bigr)},\qquad
h=z^r-\sum_{j=0}^{m}a_jx^{pj}z^{p(m-j)}.
\]
Consequently the whole projective singular scheme has length \((d-1)^2\). This is the full local Jacobian/Tjurina length, not the delta invariant or a Milnor number.

## Assumptions and scope
The characteristic is any prime \(p\). The coefficients of \(g\) lie in \(\mathbb F_p\), its highest coefficient \(a_m\) is nonzero, and \(r=pm-q>0\). Thus \(r\ge p\ge2\) and \(d\ge4\). The scheme is the hypersurface singular scheme defined locally by the equation and its first partial derivatives. The statement is over \(k\) (and the same length already holds over \(\mathbb F_p\)).

## Proof
On \(Z\ne0\), the equation is \(y^q=g(x^p)+x\); its derivative with respect to \(x\) is \(-1\), hence this affine part is smooth. On the line \(Z=0\), the equation reads \(a_mX^d=0\), so there is exactly one point at infinity, \(P=[0:1:0]\). Since \(r\ge2\), all partials vanish there. Kollár's construction also identifies the affine part with \(\mathbb A^1\), but only smoothness is needed here.

In the local chart \(Y=1\), the defining equation is \(f=h-xz^{d-1}\). Every exponent in \(h\) is divisible by \(p\), while \(d-1\) is a unit modulo \(p\). Therefore
\[
f_x=-z^{d-1},\qquad f_z=-(d-1)xz^{d-2}.
\]
Modulo these derivatives the last term in \(f\) vanishes. Thus the completed local Tjurina algebra is exactly \(R/z^{d-2}\mathfrak m R\), with \(R=k[[x,z]]/(h)\) and \(\mathfrak m=(x,z)\). Importantly, \(h(x,0)=-a_mx^d\ne0\), so \(z\) is a nonzerodivisor on \(R\): in the regular local UFD \(k[[x,z]]\), the prime element \(z\) does not divide \(h\).

Set \(t=z^{d-2}\). There is a short exact sequence of finite-length \(R\)-modules
\[
0\longrightarrow tR/t\mathfrak m R
\longrightarrow R/t\mathfrak m R
\longrightarrow R/tR\longrightarrow0.
\]
As \(t\) is a nonzerodivisor, multiplication by \(t\) identifies \(tR/t\mathfrak m R\) with \(R/\mathfrak m R\cong k\), of length one. Repeated use of the nonzerodivisor \(z\) gives
\[
\ell(R/z^{d-2}R)=(d-2)\ell(R/zR).
\]
Finally \(R/zR\cong k[[x]]/(a_mx^d)\), of length \(d\). Hence
\[
\boxed{\ell(\mathcal T_P)=1+d(d-2)=(d-1)^2.}
\]
No step depends on \(q\) or on the coefficients \(a_0,\ldots,a_{m-1}\). The singular scheme has no other support by the first paragraph. This proves the theorem for every admissible prime, power and polynomial.

## Verification
The standalone exact checker `wild_tjurina_family_verifier.py` recomputes Jacobian ideals and their zero-dimensional Groebner bases over finite prime fields, counts standard monomials independently, and confirms the formula in six mixed-characteristic, nonmonomial cases. It is corroboration, not a proof of the unrestricted statement; the proof is the regular-element length sequence above. Execute with Python 3 and SymPy: `python wild_tjurina_family_verifier.py`.

## Relationship to prior work
János Kollár, *Planar, rational curves over \(\mathbb F_2\), whose only singularity is a double point*, arXiv:2603.04211 (first submitted March 4, 2026), Example 1 and Lemma 2, constructs this Artin--Schreier family and proves the embedded affine line and the unique point at infinity. His Example 3 studies particular characteristic-two members and their cusp type. The present theorem concerns the complete nonreduced Jacobian/Tjurina singular scheme uniformly across **all** prime characteristics and all polynomials satisfying the degree condition. The cited construction and local equations are prior work; no new embedding or irreducibility is claimed. The distinction between singularity types and local Tjurina length is relevant in positive characteristic.

## Limitations
The statement is about the singular subscheme length, not the resolution graph, delta invariant, contact equivalence classification, Jacobian module, or positivity of a Milnor number. It is restricted to the characteristic-\(p\) Artin--Schreier construction and the strict inequality \(pm>q\). Published classification of these plane curves and general positive-characteristic invariants may contain equivalent deductions under different terminology; historical priority has not been independently established.

## References
- J. Kollár, *Planar, rational curves over \(\mathbb F_2\), whose only singularity is a double point*, arXiv:2603.04211v1, March 4, 2026, Example 1, Lemma 2, Example 3; later version v3 also inspected. https://arxiv.org/html/2603.04211v3
- H. Ma, A. Ying, H. Zuo, *Tjurina Number Jumps and Unimodal Hypersurface Singularities in Positive Characteristic*, arXiv:2510.02619, 2025; related positive-characteristic singularity context, with the abstract specifically focusing its classification on characteristic greater than three.
