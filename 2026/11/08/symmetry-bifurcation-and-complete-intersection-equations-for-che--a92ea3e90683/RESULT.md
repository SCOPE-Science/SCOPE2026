# Symmetry bifurcation and complete-intersection equations for Chebyshev–Lucas triples

## Finding
For integers \(u\ge3\) and even \(n\ge4\), define the norm-one Lucas sequence by
\[
U_0=0,\quad U_1=1,\quad U_{j+2}=uU_{j+1}-U_j\qquad(j\ge0),
\]
and put \(a=U_n\), \(b=U_{n+2}\), \(c=U_{n+3}\). The numerical semigroup \(S=\langle a,b,c\rangle\) is symmetric **if and only if**
\[
n=4\quad\text{or}\quad 6\mid n.
\]
The three generators are minimal for every parameter in this domain. Every symmetric member is a complete intersection, with the following explicit pair of binomial defining equations, Hilbert series and Frobenius number.

**Exceptional branch \(n=4\).** Put \(A=a/u\) and \(B=b/u\). In the graded polynomial ring \(K[X,Y,Z]\), with degrees \(a,b,c\), the kernel of \(X\mapsto t^a\), \(Y\mapsto t^b\), \(Z\mapsto t^c\) is
\[
I_S=(X^B-Y^A,\ Z^u-X^{B-1}Y).
\]
For \(H_S(t)=\sum_{s\in S}t^s\),
\[
H_S(t)=\frac{(1-t^{Ba})(1-t^{uc})}{(1-t^a)(1-t^b)(1-t^c)},\qquad
F(S)=(B-1)a+(u-1)c-b.
\]

**Periodic branch \(6\mid n\).** Put \(d=u^2-1=U_3\), \(A=a/d\), \(C=c/d\). Then
\[
I_S=(Y^d-XZ^u,\ X^C-Z^A),
\]
\[
H_S(t)=\frac{(1-t^{db})(1-t^{Ca})}{(1-t^a)(1-t^b)(1-t^c)},\qquad
F(S)=(C-1)a+(d-1)b-c.
\]
For all other even \(n\ge4\), \(S\) is nonsymmetric and therefore is not a complete intersection.

## Assumptions and scope
Here \(u\) and \(n\) are integers in the stated ranges, and \(K\) is any field. An additive numerical semigroup is a cofinite submonoid of nonnegative integers. Its Frobenius number \(F(S)\) is its greatest nonmember. Symmetry means \(g\notin S\) if and only if \(F(S)-g\in S\), for each integer \(g\). Its semigroup algebra is the subring \(K[t^a,t^b,t^c]\subseteq K[t]\). A three-generated numerical semigroup is a complete intersection when its defining ideal has two generators. Powers and coefficient normalizations in the equations above are literal integer exponents.

## Proof
**1. Divisibility and the key identity.** The recurrence implies the addition formula
\[
U_{m+r}=U_{m+1}U_r-U_mU_{r-1}\quad(m,r\ge1),
\]
and the Cassini relation \(U_{m+1}U_{m-1}-U_m^2=-1\). Consequently consecutive terms are coprime, and the Euclidean algorithm on indices gives the strong-divisibility identity
\[
\gcd(U_j,U_k)=U_{\gcd(j,k)}\quad(j,k\ge1).
\]
(The addition formula follows by induction on \(r\); Cassini follows by induction on \(m\).) Because \(u\ge3\), the positive terms strictly increase after index one. As \(n\) is even,
\[
\gcd(a,b)=u,\quad \gcd(b,c)=1,\quad
\gcd(a,c)=\begin{cases}d,&3\mid n,\\1,&3\nmid n.\end{cases}
\]
The recurrence also gives the *exact* identity
\[
db=a+uc,\qquad d=u^2-1.
\]
Every even-indexed term is divisible by \(u\), whereas every odd-indexed term is congruent to \(1\) or \(-1\) modulo \(u\). Thus \(a<b<c\), \(a\nmid b\), and \(u\nmid c\); the three generators are minimal and their common gcd is one.

**2. Symmetry at index four.** At \(n=4\), \(A=U_4/u=u^2-2=d-1\), \(B=U_6/u\), \(\gcd(A,B)=1\), and \(\gcd(u,c)=1\). The identity above yields
\[
c=dB-A=(B-1)A+B,
\]
so \(S=\langle uA,uB,(B-1)A+B\rangle\) is a gluing of the coprime two-generator semigroup \(\langle A,B\rangle\) by \(u\). Here is also a self-contained presentation argument. Use the relations \(X^B=Y^A\) and \(Z^u=X^{B-1}Y\) to reduce every monomial to \(X^iY^jZ^k\), where \(0\le i<B\), \(0\le k<u\), \(j\ge0\). These normal forms have distinct weighted degrees: reduce equal degrees modulo \(u\) to obtain equal \(k\) (since \(\gcd(c,u)=1\)); then reduce the remaining equality \((i-i')A=(j'-j)B\), using \(\gcd(A,B)=1\), to force \(i=i'\), then \(j=j'\). Thus the two relations generate the complete kernel.

The canonical forms also imply
\[
\operatorname{Ap}(S,b)=\{ia+kc:0\le i<B,\ 0\le k<u\},
\]
where \(\operatorname{Ap}(S,b)=\{s\in S:s-b\notin S\}\). Its largest element is \(\Omega=(B-1)a+(u-1)c\). This gives \(F(S)=\Omega-b\). Moreover \(\Omega-w\in\operatorname{Ap}(S,b)\) for every \(w\) of this rectangular Apéry set, which proves that \(S\) is symmetric (by translating each gap from its least residue representative). The displayed normal forms give the stated Hilbert series.

**3. Symmetry when \(6\mid n\).** Strong divisibility gives \(d=\gcd(a,c)\), so \(A=a/d\) and \(C=c/d\) are coprime, and \(\gcd(d,b)=1\). From the key identity, \(b=A+uC\). Reducing by \(Y^d=XZ^u\) and \(X^C=Z^A\), each monomial has a normal form \(X^iY^jZ^k\) with \(0\le i<C\), \(0\le j<d\), \(k\ge0\). Equality of weighted degrees modulo \(d\) forces equal \(j\) because \(\gcd(b,d)=1\); coprimality of \(A,C\) then forces equal \(i\) and \(k\). The relations therefore generate the full kernel. Consequently
\[
\operatorname{Ap}(S,c)=\{ia+jb:0\le i<C,\ 0\le j<d\}.
\]
It is a rectangular Apéry set, symmetric around \(\Omega=(C-1)a+(d-1)b\). Hence \(S\) is symmetric, \(F(S)=\Omega-c\), and its normal forms yield the stated Hilbert series.

**4. Nonsymmetry for all remaining even indices.** The remaining even \(n\ge4\) satisfy \(n\ge8\) and \(3\nmid n\). The only generator pair with nontrivial gcd is \((a,b)\), of gcd \(u\). The three-generator symmetry criterion (Herzog–Watanabe; see Fel's Theorem 1 and Corollary 1 below) requires \(c\in\langle a/u,b/u\rangle\) in any symmetric semigroup with these minimal generators. Put \(A=a/u\), \(B=b/u\), so \(\gcd(A,B)=1\) and \(c=dB-A\). If \(c=xA+yB\) with \(x,y\ge0\), then
\[
(x+1)A=(d-y)B.
\]
Since \(c<dB\), one has \(0\le y<d\). Coprimality forces \(A\mid d-y\), with \(1\le d-y\le d\). But \(U_6/u=(u^2-1)(u^2-3)\ge d\) and \(U_n>U_6\) for \(n\ge8\), so \(A>d\), a contradiction. Hence \(S\) is nonsymmetric. This exhausts all even indices.

## Verification
An independent arithmetic checker `check.py` implements the recurrence, checks the gcd and linear-relation identities, and computes actual Apéry sets using shortest paths on residue graphs. It tests 24 triples for \(2\le u\le7\) and even indices from \(4\) through \(20\), subject to \(a\le100000\), comparing the complete symmetry classification, both Frobenius formulas and selected complete rectangular Apéry sets. It reports `VERIFY_OK cases=24 symmetric_cases=15`. The \(u=2\) tests cover an additional degenerate boundary; the theorem is stated only for \(u\ge3\). Computations are finite checks; all infinite assertions follow from the proof above.

## Relationship to prior work
The paper by Komatsu and Mu, *p-Numerical semigroups of Pell triples* (arXiv:2307.08998, first public 18 July 2023), studies the **positive-sign** recurrence \(P_{j+2}=uP_{j+1}+P_j\), and its even-index section explicitly declines \(i>k\). The later preprint by Mu and Komatsu, *p-Numerical Semigroups of Triples from the Three-Term Recurrence Relations* (posted 24 July 2024; subsequently Axioms 13 (2024), 608), gives Apéry sets and Frobenius formulas for \(W_{j+2}=uW_{j+1}+vW_j\) with **positive integers** \(u,v\), including the positive-sign Pell case omitted earlier. Those results are not claimed as new. The present norm-one **negative-sign** sequence \(U_{j+2}=uU_{j+1}-U_j\) is outside their hypotheses. In particular, the isolated symmetric index \(n=4\) arises from the sharp equality \(U_4/u=U_3-1\); it is not obtained by simply importing the positive-sign formulas. Fel, *Symmetric Numerical Semigroups Generated by Fibonacci and Lucas Triples* (arXiv:0803.1606, Section 2), supplies the general three-generator gluing criterion and complete-intersection context; it does not state this Chebyshev–Lucas parameter classification.

## Limitations
The result concerns the fixed index gaps two and three, integer \(u\ge3\), even starting indices, and the ordinary \(p=0\) numerical semigroup. It does not address odd starting indices, other gaps, or positive-representation thresholds \(p>0\). The non-symmetric cases are classified by symmetry status but their full toric ideals are not presented. Earlier results under different nomenclature for Chebyshev or Lucas sequences remain a literature-completeness risk. No independent external scientific audit was performed.

## References
1. T. Komatsu and J. Mu, *p-Numerical Semigroups of Pell Triples*, first posted 18 July 2023, arXiv:2307.08998, https://arxiv.org/abs/2307.08998.
2. J. Mu and T. Komatsu, *p-Numerical Semigroups of Triples from the Three-Term Recurrence Relations*, posted 24 July 2024, https://www.preprints.org/manuscript/202407.1982; published in *Axioms* **13** (2024), 608, DOI:10.3390/axioms13090608.
3. L. G. Fel, *Symmetric Numerical Semigroups Generated by Fibonacci and Lucas Triples*, first posted 11 March 2008, arXiv:0803.1606, https://arxiv.org/abs/0803.1606 (especially Theorem 1 and Corollary 1).
