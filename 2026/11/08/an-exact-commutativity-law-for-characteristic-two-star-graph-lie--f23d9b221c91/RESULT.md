# An exact commutativity law for characteristic-two star graph Lie algebras

## Finding
Let \(q=2^s\), with \(s\ge1\), and let \(m\ge3\). For the class-three graph Lie algebra \(L=\mathfrak n_{K_{1,m}}(\mathbb F_q)\) defined below, the probability that two independently and uniformly chosen elements commute is
\[
\operatorname{cp}(L)=2(q+1)q^{-2m}-(q+1)^2q^{-3m}+q^{2-4m}.
\]
For its canonical two-step quotient \(\overline L=L/\gamma_3(L)\), the analogous probability is
\[
\operatorname{cp}(\overline L)=q^{-2}+(1-q^{-2})q^{-m}.
\]
Consequently, for any fixed \(q=2^s\), \(\operatorname{cp}(L)\sim2(q+1)q^{-2m}\) and \(\operatorname{cp}(L)\to0\) as \(m\to\infty\), while \(\operatorname{cp}(\overline L)\to q^{-2}>0\). The formula resolves an exact invariant over an infinite family rather than just a small graph.

## Assumptions and scope
The base field is the finite field \(\mathbb F_q\) with \(q\) an even prime power. Fix an integer \(m\ge3\). Let \(U\cong\mathbb F_q^m\), and take the underlying vector space
\[
L=\mathbb F_q c\oplus U\oplus U_A\oplus \Lambda^2U,
\]
where \(U_A\) is a second copy of \(U\). Write \(x_i\) and \(a_i\) for the natural bases of \(U\) and \(U_A\), and \(z_{ij}\) for the exterior-square basis with \(i<j\). Impose
\[
[c,x_i]=a_i,\qquad [x_i,a_j]=[x_j,a_i]=z_{ij}\quad(i<j),
\]
with the remaining basis brackets zero and bilinearity and alternation. This is the Lie algebra attached to the star \(K_{1,m}\) in Gallo--Videla's construction, including the characteristic-two signs. Its central third layer \(W=\Lambda^2U\) has dimension \(\binom m2\), and \(L\) has dimension \(1+2m+\binom m2\). The element commutativity probability is \(\operatorname{cp}(L)=|\{(X,Y)\in L^2:[X,Y]=0\}|/|L|^2\). This definition is not the subalgebra commutativity degree.

## Proof
Put \(x=q^m\). Write two general elements as \(X=t c+u+a+z\) and \(Y=s c+v+b+w\), with \(t,s\in\mathbb F_q\), \(u,v,a,b\in U\) (identifying \(U_A\) with \(U\)), and \(z,w\in W\). The defining brackets give
\[
[X,Y]=(tv-su)_A+u\wedge b-v\wedge a.
\]
In characteristic two the symmetric pair of structure constants \([x_i,a_j]=[x_j,a_i]\) coincides with the coefficient of the alternating exterior product. The two displayed components lie in independent direct summands. The central variables \(z,w\) are free and cancel from the probability, so we count commuting pairs among the \(q^{1+2m}\) choices of \((t,u,a)\) and the same number of \((s,v,b)\).

**Zero hub coordinates.** Let \(F\) denote the size of the zero fiber of the map \((u,b)\mapsto u\wedge b\). When \(u=0\), any \(b\) is possible; for \(u\ne0\), the vectors \(b\) with zero exterior product form the one-dimensional span of \(u\). Thus
\[
F=x+(x-1)q=(q+1)x-q.
\]
Every nonzero decomposable bivector determines a unique two-dimensional support plane; it has exactly \(|\operatorname{SL}_2(\mathbb F_q)|=q(q^2-1)\) ordered independent preimages. This follows by fixing one ordered basis of its support: a second ordered pair has the same bivector exactly when its \(2\times2\) change-of-basis matrix has determinant one. The number of distinct nonzero decomposable bivectors is
\[
D=\frac{(x-1)(x-q)}{q(q^2-1)}=(q-1)\genfrac{[}{]}{0pt}{}{m}{2}_q.
\]
The number of quadruples \((u,v,a,b)\) satisfying \(u\wedge b=v\wedge a\), for \(t=s=0\), is therefore the sum of squared fiber sizes,
\[
N_0=F^2+D[q(q^2-1)]^2=F^2+q(q^2-1)(x-1)(x-q).
\]
This formula includes all zero and nonzero bivector fibers; no assumption is made that a general bivector is decomposable.

**Nonzero hub pair.** For any fixed \((t,s)\ne(0,0)\), the equation \(tv=su\) makes \(u,v\) proportional. If \(t\ne0\), put \(v=(s/t)u\). For every \(u\) and \(a\), the remaining condition becomes \(u\wedge(b-(s/t)a)=0\). There are exactly \(F x\) choices for \((u,a,b)\). If \(t=0\) and \(s\ne0\), then \(u=0\), and the same count \(F x\) follows by exchanging the roles of the two elements. As there are \(q^2-1\) nonzero choices of \((t,s)\),
\[
N_1=(q^2-1)xF.
\]
Summing the disjoint cases and expanding exactly gives
\[
N=N_0+N_1=2q^2(q+1)x^2-q^2(q+1)^2x+q^4.
\]
The noncentral coordinate-pair sample space has size \(q^{2+4m}=q^2x^4\). Dividing \(N\) by this size, then substituting \(x=q^m\), yields
\[
\operatorname{cp}(L)=2(q+1)q^{-2m}-(q+1)^2q^{-3m}+q^{2-4m}.
\]
For the quotient \(\overline L=L/W\), only the constraint \(tv=su\) survives. When \(t=s=0\) there are \(x^2\) choices of \((u,v)\); for any of the other \(q^2-1\) pairs there are \(x\). Hence
\[
\operatorname{cp}(\overline L)=\frac{x^2+(q^2-1)x}{q^2x^2}=q^{-2}+(1-q^{-2})q^{-m}.
\]
Finally the leading term in \(\operatorname{cp}(L)\) at fixed \(q\) is \(2(q+1)q^{-2m}\), while the other terms are of strictly smaller order. This proves the contrasting limits.

## Verification
The included standalone Python 3 file `verify.py` (standard library only) implements the Lie bracket directly over \(\mathbb F_2\) and \(\mathbb F_4\), exhaustively counts commuting noncentral pairs for \((q,m)=(2,2),(2,3),(2,4),(4,2)\), and checks all calculations against the symbolic expression. An independent exterior-product fiber routine checks the zero and nonzero fiber sizes over \(\mathbb F_2,\mathbb F_4,\mathbb F_8\) in nine field/rank combinations; additional exact-arithmetic checks cover six field sizes and ranks \(2\) through \(12\). In total the direct pair loop examines \(1,328,128\) ordered pairs, and the fiber enumeration examines \(337,488\) ordered vector pairs. It prints `VERIFY_OK` only if all assertions hold. Reproduce with `python3 verify.py` in the directory containing that file. The proof, not the finite tests, establishes the universal claim. As a specific instance \(\operatorname{cp}(L_{3,2})=79/1024\).

## Relationship to prior work
Gallo and Videla, arXiv:2610.33963v1, introduced the graph Lie algebras and wrote the complete star-graph brackets and lower-central-series dimensions; their inspected Sections 2--6 do not compute the element commutativity probability. The present result uses their construction but analyzes the full commuting-pair fibers in characteristic two. Shamsaki, Erfanian and Parvizi, *Characterizing Lie Algebra Structure via the Commutativity Degree*, Journal of Mathematics (2026), study general bounds, values, and asymptotics for different finite-dimensional Lie algebra families. Their class-three examples with derived dimension two do not cover these stars, whose derived dimensions are \(m+\binom m2\ge6\). The exact star law and its sharp contrast with the class-two quotient were not found in the inspected literature and mathematical-record searches. The authorship and formulas of cited work are attributed to the original authors, and historical priority is not independently established.

## Limitations
The calculation uses \(\operatorname{char}(\mathbb F_q)=2\) essentially: in other characteristics, the star mixed bracket has a symmetric bilinear coefficient that is not the exterior product. No odd-characteristic extension, distribution of other commutator values, group-theoretic integration, or arbitrary-graph classification is claimed. Values for \(m=2\) appear in computational checks but lie outside the new theorem's stated range. The proof gives a complete exact finite-field counting statement but has not been independently mathematically audited. General commutativity bounds in older sources could still contain an implicit specialization not surfaced by the comparisons.

## References
1. A. L. Gallo and D. E. Videla, *Nilpotent Lie algebras of nilpotence class at most three via graphs*, arXiv:2610.33963v1, first publicly posted 2026-10-25, especially Sections 2, 3 (Stars), and 4. https://arxiv.org/html/2610.33963v1
2. A. Shamsaki, A. Erfanian and M. Parvizi, *Characterizing Lie Algebra Structure via the Commutativity Degree*, Journal of Mathematics (2026), article 9921706, first published 2026-02-25, DOI 10.1155/jom/9921706. https://onlinelibrary.wiley.com/doi/full/10.1155/jom/9921706
3. A. Shamsaki, A. Erfanian and M. Parvizi, *On the commutativity degree of a finite-dimensional Lie algebra*, arXiv:2406.10064 (2024). Its earlier abstract-level general bounds were considered as possible background; complete full-text coverage of this source was not established.
