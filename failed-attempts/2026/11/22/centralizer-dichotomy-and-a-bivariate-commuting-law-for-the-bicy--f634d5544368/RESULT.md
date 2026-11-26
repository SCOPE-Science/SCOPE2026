# Centralizer dichotomy and a bivariate commuting law for the bicyclic monoid

## Finding
Consider the bicyclic monoid \(B=\langle p,q\mid pq=1\rangle\), without an adjoined zero. Every element has the unique normal form \(q^a p^b\), \(a,b\in\mathbb N_0\). Write \(C_B(w)=\{z\in B:zw=wz\}\). The following statements hold.

**Complete centralizer structure.** For \(w=q^a p^b\), every commuting element \(z=q^c p^d\) satisfies exactly one of these cases:

- If \(a>b\), then \((c,d)=(k,k)\) with \(0\le k<b\), or \(d=b\) and \(c\ge b\).
- If \(a<b\), then \((c,d)=(k,k)\) with \(0\le k<a\), or \(c=a\) and \(d\ge a\).
- If \(a=b\), then \((c,d)=(k,k)\) with \(0\le k<a\), or both \(c,d\ge a\).

Consequently, \(C_B(w)\) is commutative if and only if \(a\ne b\). In particular, the elements whose centralizers are noncommutative are exactly the idempotents.

**Complete joint-length law.** Let \(\ell(q^a p^b)=a+b\), the minimum length of a generator word representing the element. The formal bivariate generating series of ordered commuting pairs is
\[
F(x,y)=\sum_{uv=vu}x^{\ell(u)}y^{\ell(v)}
=\frac{1-xy}{(1-x)^2(1-y)^2(1+xy)}.
\]

Let \(B_N=\{w\in B:\ell(w)\le N\}\), \(N\in\mathbb N_0\). Then \(|B_N|=(N+1)(N+2)/2\), and the exact number of ordered commuting pairs in \(B_N\times B_N\) is
\[
K_N=\begin{cases}
\frac{(N+2)^2(2N+1)}4,&N\text{ even},\\
\frac{(N+1)^2(2N+5)}4,&N\text{ odd}.
\end{cases}
\]
Thus for two independent uniform elements of \(B_N\),
\[
\Pr(uv=vu)=\frac{2}{N}+O(N^{-2})\quad(N\to\infty).
\]

## Assumptions and scope
The generators satisfy only \(pq=1\); in particular \(qp\ne1\). All variables \(a,b,c,d,N\) are nonnegative integers. The generator word length is with respect to \(\{p,q\}\), and normal forms are reduced words; there is no zero element, and the displayed formulas do not apply unchanged after adjoining a zero. The series is a formal series in two commuting indeterminates, and all counts are of ordered pairs including the diagonal.

## Proof
The defining relation cancels the maximal overlap of adjacent \(p\)- and \(q\)-powers. In normal-form pair notation one has
\[
(a,b)(c,d)=(a+c-t,b+d-t),\qquad t=\min(b,c).
\]
The reversed product has the same expression except that \(t'=\min(d,a)\). Since the differences of both coordinates are \(t'-t\), commutation is equivalent to
\[
\min(b,c)=\min(d,a).\tag{1}
\]

If \(a>b\), the common minimum in (1) cannot exceed \(b\). If \(c<b\), the first minimum equals \(c\), which is strictly less than \(a\); the second is then \(d=c\). If \(c\ge b\), the first minimum is \(b<a\), so \(d=b\). The \(a<b\) case follows by exchanging the two coordinates. If \(a=b\), either both \(c,d\) are at least \(a\), or their common minimum is strictly smaller than \(a\), forcing \(c=d<a\). These partitions are disjoint and exhaustive.

In the \(a>b\) case the ray \(\{(c,b):c\ge b\}\) multiplies within itself by \((c,b)(c',b)=(c+c'-b,b)\). The lower diagonal idempotents \((k,k)\), \(k<b\), commute pairwise and act identically on that ray. Therefore the centralizer is commutative. The \(a<b\) case is symmetric. For \(a=b\), the two centralizer elements \((a+1,a)\) and \((a,a+1)\) have products \((a+1,a+1)\) and \((a,a)\) in opposite orders, proving noncommutativity. The diagonal elements, and only those elements, are idempotent by the product formula.

For fixed \(m\ge0\), define
\[
H_m(x,y)=\sum_{\min(b,c)=m}x^b y^c.
\]
The condition either has \(b=m,c\ge m\), or \(c=m,b>m\), so
\[
H_m(x,y)=\frac{(xy)^m(1-xy)}{(1-x)(1-y)}.
\]
The independent equality \(\min(d,a)=m\) contributes a second factor \(H_m(x,y)\) (with variables interchanged, which does not change this symmetric expression). Summing over the uniquely determined common minimum yields
\[
F(x,y)=\sum_{m\ge0}H_m(x,y)^2
=\frac{(1-xy)^2}{(1-x)^2(1-y)^2(1-x^2y^2)}
=\frac{1-xy}{(1-x)^2(1-y)^2(1+xy)}.
\]

Coefficientwise summation of \(F\) over lengths at most \(N\) in both variables gives
\[
K_N=[x^Ny^N]\frac{F(x,y)}{(1-x)(1-y)}
=\binom{N+2}{2}^{\!2}+2\sum_{j=1}^N(-1)^j\binom{N-j+2}{2}^{\!2}.
\]
Set \(A_N=\binom{N+2}{2}\), and \(K_{-1}=0\). The displayed alternating sum implies \(K_N+K_{N-1}=A_N^2-A_{N-1}^2\) for \(N\ge1\), with \(K_0=1\). Substituting the stated even and odd cubic polynomials verifies this recurrence and base value, proving the exact piecewise formula. Finally \(K_N=\frac12N^3+O(N^2)\) and \(|B_N|^2=\frac14N^4+O(N^3)\), giving the probability limit.

## Verification
A standalone checker `bicyclic_commutation_check.py` verifies the normal-form multiplication against the complete centralizer classification on all ordered pairs from length balls \(B_N\), \(0\le N\le7\), and checks the resulting commuting-pair count against the closed formula for each \(N\). It independently checks each of the \(49\) coefficients with both lengths from \(0\) to \(6\) against the expanded rational generating function. See `bicyclic_commutation_check_output.txt` for reproducible output. These are finite checks; the displayed algebraic proof covers all \(N\).

## Relationship to prior work
Mesyan and Mitchell (arXiv:1409.4380, first posted 2014-09-15), Section 2.3, identify the zero-adjoined bicyclic monoid as the one-loop graph inverse semigroup, and study its general graph inverse semigroup structure; the article does not present this joint commuting-length enumerator. The standard bicyclic normal-form multiplication is also recorded in the PlanetMath bicyclic semigroup entry. The normal form and existence of the bicyclic monoid are classical and are not new. This finding concerns the complete individual centralizer dichotomy together with the joint-length and finite-ball commuting distributions, rather than the defining multiplication rule.

## Limitations
The proof concerns the bicyclic monoid without zero, and these natural word-length balls are not submonoids. A literature search is not a proof of absolute novelty; equivalent bicyclic centralizer calculations in older texts may exist. The exact joint-length enumeration and its density law are assessed together with the centralizer dichotomy, not as a claim that the minimum criterion itself is new. There is no independent mathematical audit.

## References
- Z. Mesyan and J. D. Mitchell, *The Structure of a Graph Inverse Semigroup*, arXiv:1409.4380 (v1 publicly posted 2014-09-15), https://arxiv.org/abs/1409.4380 ; full text https://ar5iv.labs.arxiv.org/html/1409.4380 .
- *Bicyclic semigroup*, PlanetMath, https://planetmath.org/bicyclicsemigroup (normal-form and multiplication reference).
