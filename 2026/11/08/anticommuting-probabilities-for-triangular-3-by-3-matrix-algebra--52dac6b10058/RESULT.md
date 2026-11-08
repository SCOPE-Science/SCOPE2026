# Anticommuting probabilities for triangular \(3\times3\) matrix algebras over finite fields

## Finding

Let \(k=\mathbb F_q\) be any finite field and \(T_3(k)\) the unital algebra of upper-triangular \(3\times3\) matrices. Define the anticommuting-pair count and probability by
\[
N_q=\#\{(A,B)\in T_3(k)^2:AB+BA=0\},\qquad p_{\mathrm{ac}}(T_3(k))=N_q/q^{12}.
\]
Then the **exact count over every finite field** is
\[
\boxed{N_q=\begin{cases}
q^3(2q-1)(11q^2-15q+5),&\operatorname{char}k\ne2,\\
q^5(q^4+3q^3-2q^2-2q+1),&\operatorname{char}k=2.
\end{cases}}
\]
Equivalently, \(p_{\mathrm{ac}}=(2q-1)(11q^2-15q+5)/q^9\) in odd characteristic and \(p_{\mathrm{ac}}=(q^4+3q^3-2q^2-2q+1)/q^7\) in characteristic two. Consequently, along fields of growing size in odd characteristic the probability is asymptotic to \(22q^{-6}\), while along characteristic-two fields it is asymptotic to \(q^{-3}\).

The count concerns *all* triangular matrices, including singular ones, and ordered pairs; it is not a count of conjugacy classes or of unit-group elements.

## Assumptions and scope

The algebra is the full six-dimensional associative upper-triangular algebra, not the group of invertible triangular matrices, nor its radical-square-zero quotient. The radical of \(T_3(k)\) satisfies \(J^3=0\) but \(J^2\ne0\), as witnessed by \(E_{12}E_{23}=E_{13}\). It is the smallest standard upper-triangular algebra in which products of two radical elements can be nonzero. All the finite-field formulas include arbitrary prime-power orders; the proof uses only field arithmetic.

## Proof

Write
\[
A=\begin{pmatrix}a&x&z\\0&b&y\\0&0&c\end{pmatrix},\qquad
B=\begin{pmatrix}d&u&w\\0&e&v\\0&0&f\end{pmatrix}.
\]
Literal multiplication shows that \(AB+BA=0\) is equivalent to the following six scalar equations:
\[
2ad=2be=2cf=0,\quad
(a+b)u+(d+e)x=0,\quad
(b+c)v+(e+f)y=0,\quad
(a+c)w+(d+f)z+xv+uy=0.\tag{1}
\]
The last summand \(xv+uy\) records the nonzero radical product and is essential to the calculation.

**Odd characteristic.** Put \(\Omega=\{(s,t)\in k^2:st=0\}\), whose cardinality is \(h=2q-1\). The diagonal equations in (1) force the three ordered states \(U=(a,d),V=(b,e),W=(c,f)\) to lie in \(\Omega\). Define \(\delta_{12}=[U+V=0]\) and \(\delta_{23}=[V+W=0]\).

If \(U+W\ne0\), the first two off-diagonal equations admit respectively \(q^{1+\delta_{12}}\) and \(q^{1+\delta_{23}}\) solutions. The final equation is a nonzero linear equation in \((z,w)\), and hence has exactly \(q\) solutions for every choice of \((x,u,y,v)\). Such a diagonal triple contributes exactly \(q^{3+\delta_{12}+\delta_{23}}\). Summing its weight over *all* diagonal triples gives \(h(h+q-1)^2\). For triples with \(U+W=0\), the sum of the same weights is
\[
R_0=q^2+h-1+(h-1)(2q+h-2).
\]
Indeed, for \(U=0\) the choice \(V=0\) has both indicators equal to one and the remaining \(h-1\) choices have neither; for each nonzero \(U\), the distinct values \(V=U\) and \(V=-U\) each activate one indicator and all other choices activate neither. Thus the contribution with \(U+W\ne0\) is \(q^3[h(h+q-1)^2-R_0]\).

For the remaining triples \(W=-U\), there are \(h^2\) choices of \((U,V)\). The final equation reduces to \(xv+uy=0\), and \((z,w)\) are free. Except for the cases described below, the first two off-diagonal equations are nonzero independent scalar equations in disjoint pairs of variables, and the bilinear condition follows automatically. In fact, if both coefficients are nonzero, one may write
\[
(x,u)=\lambda(a+b,-d-e),\qquad(y,v)=\mu(b-a,d-e),
\]
which makes \(xv+uy=2\lambda\mu(ad-be)=0\). Hence each ordinary case contributes \(q^4\).

There are precisely three deviations from this baseline. When \(U=V=0\), the equation \(xv+uy=0\) has \(q^3+q^2-q\) solutions in \((x,u,y,v)\), giving \(q^5+q^4-q^3\) after choosing \((z,w)\). When \(U\ne0\) and \(V=U\) or \(V=-U\), exactly one of the two preceding linear conditions vanishes; the other constrains its pair to a line. If that constrained pair is zero, the other pair is free; otherwise the bilinear equation is one nonzero linear condition. This gives \(q^2+(q-1)q=2q^2-q\) choices in the first four variables, and \(2q^4-q^3\) after \((z,w)\). There are \(2(h-1)\) such exceptional diagonal triples, since \(2\ne0\). Their total contribution is therefore
\[
h^2q^4+(q^5-q^3)+2(h-1)(q^4-q^3).
\]
Adding this to the \(U+W\ne0\) contribution and substituting \(h=2q-1\) simplifies exactly to
\[
N_q=q^3(2q-1)(11q^2-15q+5).
\]

**Characteristic two.** The three diagonal equations in (1) vanish identically. Now \(U,V,W\) range through all \(k^2\); write \(h=q^2\). For \(U\ne W\), the final equation has \(q\) choices of \((z,w)\), and the two preceding equations each have \(q\) choices unless \(U=V\) or \(V=W\), respectively, in which case they have \(q^2\). The two exceptional equalities are disjoint when \(U\ne W\). There are \(h(h-1)(h-2)\) triples satisfying neither and \(h(h-1)\) of each exceptional kind. Hence the contribution is
\[
q^3h(h-1)(h-2+2q).
\]
For \(U=W\), if \(V=U\), the first two off-diagonal conditions vanish and the last reduces to \(xv+uy=0\): this contributes \(q^5+q^4-q^3\) for each of the \(h\) choices of \(U\). If \(V\ne U\), both preceding equations impose the *same nonzero linear relation* on \((x,u)\) and \((y,v)\). Thus both pairs lie on the same one-dimensional line. The alternating expression \(xv+uy\) vanishes on proportional vectors in characteristic two; this gives \(q^4\) for each of \(h(h-1)\) triples. So the remaining contribution is \(hq^5+h^2q^4-hq^3\). Substituting \(h=q^2\) and adding the two pieces gives
\[
N_q=q^5(q^4+3q^3-2q^2-2q+1).
\]
These two cases exhaust every field characteristic and every ordered pair of triangular matrices. Dividing by \(|T_3(k)|^2=q^{12}\) proves the probability formulas. The displayed asymptotics follow by comparing highest powers of \(q\).

## Verification

`checks/verify.py` supplies two independent enumerations. The first loops over all \(q^6\) possible first factors and computes the rank of the linear map \(B\mapsto AB+BA\) by exact finite-field Gaussian elimination; its count is the sum of \(q^{6-\operatorname{rank}}\) over first factors. It checks all possibilities over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8\). The second loops over *both* factors and literally multiplies full \(3\times3\) matrices over \(\mathbb F_2\) and \(\mathbb F_3\). No interpolation, random sampling, or symbolic formula fitting is involved. Outputs are recorded in `checks/verify_output.txt` and may be reproduced with `python checks/verify.py`. Verification of finitely many fields supplements, but does not replace, the preceding all-field proof.

The resulting counts for field orders \(2,3,4,5,7,8\) are respectively \(928,7965,418816,230625,1957501,179863552\). Both full literal-multiplication tests agree with the same count.

## Relationship to prior work

Buckley, MacHale, and Zelenyuk define finite-ring anticommuting probability and establish general kernel-averaging identities and a classification of *large* values, above the threshold \(15/32\). Their paper's full text has been inspected, including the introduction, formula (2.1), and the spectral classification. That identity does not evaluate the specific anticommutant rank distribution in \(T_3(k)\), and the exact values proved here fall strictly below the paper's large-probability threshold.

Ghahramani studies zero-Jordan-product-determined triangular algebras: a universal factorization property of bilinear maps, not a finite-field cardinality formula. The accessible abstract does not imply the present numerical result; its full text was unavailable, leaving a bounded historical-priority risk. Kaur, Sharma, and Singh study commuting-tuples and branching rules in the *invertible triangular group* in odd characteristic, with different objects and equations; relevant full-text sections were read.

Related formulas for commutators in radical-square-zero quiver algebras do not cover \(T_3(k)\), whose radical has nonzero square. Nor does ordinary commutation in a triangular group imply the odd-characteristic anticommuting count. In characteristic two, the equation coincides with commutation of the full ring, not the unit group.

No prior source inspected gives the two closed formulas above. An unidentified broader finite-ring enumeration may nevertheless subsume them; this is a self-review, not independent validation or a proof of historical priority.

## Limitations

The result is a complete count for the natural six-dimensional algebra \(T_3(k)\), not a formula for arbitrary triangular dimension, prescribed nonzero Jordan products, factor rank distributions, or conjugacy orbits. The generalization to \(T_n(k)\) for \(n>3\) is not claimed. The originality assessment is necessarily provisional; all algebraic assertions in the finding are proved directly, while comprehensive independent historical verification has not been performed.

## References

1. S. M. Buckley, D. MacHale, Y. Zelenyuk, *Finite Rings with Large Anticommuting Probability*, Applied Mathematics & Information Sciences **8** (2014), 13–25. DOI: https://doi.org/10.12785/amis/080102. Lawful full text: https://mural.maynoothuniversity.ie/id/eprint/4832/1/SB_Finite%20rings.pdf (publication header dates online release 2014-01-01).
2. H. Ghahramani, *Zero product determined triangular algebras*, Linear and Multilinear Algebra **61** (2013), 741–757. DOI: https://doi.org/10.1080/03081087.2012.703193. Publisher online-release date 2012-07-18; only abstract accessible for comparison.
3. D. Kaur, U. B. Sharma, A. Singh, *Branching rules and commuting probabilities for Triangular and Unitriangular matrices*, arXiv:2006.01493 (initial public preprint 2020-06-02), https://arxiv.org/pdf/2006.01493.
