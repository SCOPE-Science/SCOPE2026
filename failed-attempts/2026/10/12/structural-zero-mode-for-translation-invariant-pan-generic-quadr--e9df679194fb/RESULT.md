# Structural zero mode for translation-invariant pan-generic quadratic forms
## Finding
Let \(u=(1,1,1,1)^T\). Consider
\[Q(x,y)=x^Tax+x^Tby+y^Tcy\]
with \(a,c\in\operatorname{Mat}_4(\mathbb Z)\) symmetric, \(\det(ab)\ne0\), and
\[\Delta=4b^{-1}ab^{-T}c-I_4.\]
Then translation invariance of \(Q\), namely
\[\begin{pmatrix}a&b/2\\b^T/2&c\end{pmatrix}(u,u)^T=0,\]
is equivalent to the pair of four-dimensional conditions
\[au+\frac12bu=0,\qquad \Delta u=0.\]
In particular, translation invariance forces \(0\) to be an eigenvalue of \(\Delta\). Consequently, Green's generic hypothesis for eight-prime quadratic forms, which requires the four eigenvalues of \(\Delta\) to avoid \(0\), is incompatible with translation invariance whenever \(\det(ab)\ne0\).

If, moreover, \(Q\) is pan-generic in the sense of Pei--Tan--Zhang--Zhao, so that the four eigenvalues of \(\Delta\) are distinct, then \(0\) is a simple eigenvalue and
\[\operatorname{rank}(Q)=7,\qquad \ker(Q)=\operatorname{span}\{(u,u)\}.\]
Thus the 2026 relaxation that allows a zero eigenvalue is structurally necessary for the translation-invariant dense-prime application, rather than merely a cosmetic weakening of the older generic condition.

The class is nonempty among indefinite integral forms. One example is
\[a=I_4,\qquad b=-2I_4,\qquad c=\begin{pmatrix}3&0&-4&2\\0&3&2&-4\\-4&2&3&0\\2&-4&0&3\end{pmatrix}.\]
Here \(\Delta=c-I_4\) has spectrum \(\{-4,0,4,8\}\), the block matrix has rank \(7\), and \(Q\) is indefinite.

## Assumptions and scope
The result concerns the same \(4+4\) block presentation used in the cited papers. The assumptions \(\det(ab)\ne0\) ensure that \(a\) and \(b\) are invertible. No analytic number theory is used in the new deduction, and indefiniteness is needed only for the displayed example and for the application context, not for the structural zero-mode statement itself.

## Proof
Write
\[M=\begin{pmatrix}a&b/2\\b^T/2&c\end{pmatrix}.\]
If \(M(u,u)^T=0\), its two block equations are
\[au+\frac12bu=0,\qquad \frac12b^Tu+cu=0.\]
Using the second equation first and then the first gives
\[\Delta u=4b^{-1}ab^{-T}cu-u=-2b^{-1}au-u=0.\]
This proves the forward implication.

Conversely, assume \(au+\tfrac12bu=0\) and \(\Delta u=0\). The latter identity gives
\[4b^{-1}ab^{-T}cu=u.\]
Multiplying by \(b\), then by \(a^{-1}\), yields
\[b^{-T}cu=\frac14a^{-1}bu=-\frac12u,\]
where the last equality uses \(au=-bu/2\). Hence \(cu=-b^Tu/2\), so both block equations hold and \(M(u,u)^T=0\).

Pei--Tan--Zhang--Zhao record the factorization
\[M=\begin{pmatrix}I&0\\b^Ta^{-T}/2&I\end{pmatrix}
\begin{pmatrix}a&0\\0&b^Ta^{-1}b\Delta/4\end{pmatrix}
\begin{pmatrix}I&a^{-1}b/2\\0&I\end{pmatrix}.\]
The outer factors are invertible, as are \(a\) and \(b^Ta^{-1}b\). Therefore
\[\operatorname{rank}(M)=4+\operatorname{rank}(\Delta).\]
For a pan-generic translation-invariant form, \(0\) is one of four distinct eigenvalues of \(\Delta\), hence it is simple and \(\operatorname{rank}(\Delta)=3\). Thus \(\operatorname{rank}(M)=7\). Since \((u,u)\) already lies in the kernel and the kernel is one-dimensional, it is exactly \(\operatorname{span}\{(u,u)\}\).

For the displayed example, \(c\) has row sum \(1\), so \(M(u,u)^T=0\). The four Hadamard vectors are eigenvectors of \(c\) with eigenvalues \(1,-3,5,9\), respectively, hence \(\Delta=c-I_4\) has eigenvalues \(0,-4,4,8\). The factorization then gives rank \(7\). Also \(Q(e_1,0)=1>0\). If \(v=(1,-1,1,-1)^T\), then \(cv=-3v\); taking \(x=y=v\) gives \(Q(v,v)=-16<0\), so the form is indefinite.

## Verification
The bundled `verify.py` uses exact integer and rational arithmetic only. It checks the displayed matrices, translation invariance, the four stated eigenpairs of \(\Delta\), rank \(7\) by rational row reduction, and explicit positive and negative values of \(Q\). These finite checks verify the concrete witness; the general theorem is established by the algebraic proof above and does not rely on enumeration.

## Relationship to prior work
Pei--Tan--Zhang--Zhao define pan-genericity by \(\det(ab)\ne0\) and four distinct eigenvalues of \(\Delta\), explicitly dropping Green's older prohibition on eigenvalues \(0\) and \(-1\). They also place this definition immediately before the translation-invariant application and record the block factorization used above. Their text states that pan-genericity implies rank at least \(7\), but it does not state the exact zero-mode identity \(\Delta u=0\), the incompatibility with Green's generic hypothesis, or the resulting exact kernel classification.

Green's 2025 theorem requires the spectrum of \(\Delta\) to avoid \(0\), and explains that this is essentially the regular, nonsingular case. The new observation identifies why that regular regime cannot contain the translation-invariant forms targeted by the 2026 dense-set theorem: the translation direction forces the missing eigenvalue exactly at \(0\).

## Limitations
The equivalence is tied to the chosen \(4+4\) block decomposition and assumes \(\det(ab)\ne0\). It does not weaken the distinct-eigenvalue part of pan-genericity, prove any new prime-counting estimate, or address forms for which \(a\) or \(b\) is singular. The exact-rank conclusion uses distinctness of the four eigenvalues; without it, translation invariance still forces \(\Delta u=0\) but the nullity can be larger.

## References
1. Zhaochen Pei, Maoru Tan, Weiwen Zhang, Lilu Zhao, *Translation invariant quadratic forms in \(8\) variables and dense sets of primes*, arXiv:2610.01091v1, submitted 2026-10-01. Primary MSC2020 includes 11P55.
2. Ben Green, *Quadratic Forms in \(8\) Prime Variables*, Geometric and Functional Analysis 35 (2025), 1587--1637, DOI 10.1007/s00039-025-00727-9; arXiv:2108.10401.
