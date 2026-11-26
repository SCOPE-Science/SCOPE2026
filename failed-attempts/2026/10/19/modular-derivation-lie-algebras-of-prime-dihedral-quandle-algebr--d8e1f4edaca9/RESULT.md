# Modular derivation Lie algebras of prime dihedral quandle algebras

## Finding

Let \(p\) be any odd prime, let \(K\) be any field of characteristic \(p\), and let \(A=K[R_p]\) be the quandle algebra of the dihedral quandle \(R_p=\mathbb Z/p\mathbb Z\) with \(i\triangleright j=2j-i\). Put
\[
d=\operatorname{ord}_p(2),\qquad L=\operatorname{lcm}(2,d),\qquad m=(p-1)/L.
\]
The Lie algebra \(\operatorname{Der}_K(A)\) of ordinary Leibniz derivations has dimension exactly \(2m\), over **every** such field \(K\). More precisely, identify \(A\) linearly with \(K[x]/(x^p)\) so that its nonassociative multiplication is
\[
f\star g=f(-x)g(2x)\pmod{x^p}.
\]
Then the following \(2m\) endomorphisms are a basis of all derivations:
\[
H_j=x^{1+jL}\frac{d}{dx},\qquad E_j(f)=x^{1+jL}f,
\qquad 0\le j<m.
\]
Their complete Lie bracket table, with any symbol indexed \(\ge m\) interpreted as zero, is
\[
[H_i,H_j]=(j-i)LH_{i+j},\quad
[H_i,E_j]=(1+jL)E_{i+j},\quad
[E_i,E_j]=0.
\]
In particular \(\langle E_0,\ldots,E_{m-1}\rangle\) is an abelian ideal and the derived Lie algebra has codimension one, spanned by all \(E_j\) and \(H_1,\ldots,H_{m-1}\). The derivation dimension is \(2\) for \(p=3,5,7,11,13\), jumps to \(4\) at \(p=17\), and is \(6\) at \(p=31\) and \(p=43\).

## Assumptions and scope

The prime \(p\) is odd, \(K\) need not be finite, perfect, or algebraically closed, and derivations are \(K\)-linear maps satisfying \(D(a\star b)=D(a)\star b+a\star D(b)\). The claim is solely about the dihedral quandle of size exactly \(p\) over a field of the same characteristic \(p\), not arbitrary composite moduli, other field characteristics, or derivations defined by alternative twisted Leibniz rules. Derivation brackets are ordinary commutators of linear operators.

## Proof

**1. Polynomial coordinates.** Give the vector space of the quandle algebra the basis \(t^i\), \(0\le i<p\), in the ordinary group algebra \(B=K[t]/(t^p-1)\). Its quandle product is \(f\star g=f(t^{-1})g(t^2)\), where the multiplication on the right is the *ordinary associative* multiplication of \(B\). This is immediate on \(t^i\star t^j=t^{2j-i}\). Since \(t-1\) is nilpotent of order \(p\), the truncated series
\[
x=\log t=\sum_{k=1}^{p-1}\frac{(-1)^{k+1}(t-1)^k}{k}
\]
is defined in characteristic \(p\). The truncated logarithm and exponential invert each other through degree \(p-1\), because all denominators involved below \(p\) are invertible. Thus \(B=K[x]/(x^p)\), \(t=\exp x\), \(t^{-1}=\exp(-x)\), and \(t^2=\exp(2x)\). In the polynomial coordinates the displayed product follows, and on monomials it reads
\[
x^a\star x^b=\begin{cases}(-1)^a2^b x^{a+b},&a+b<p,\\0,&a+b\ge p.\end{cases}
\]
The elements \(1,x\) generate this nonassociative algebra: \(x^{a+1}=(-1)^a(x^a\star x)/2\) for \(1\le a<p-1\).

**2. Homogeneous decomposition.** For each integer shift \(s\), a linear map of homogeneous degree \(s\) has \(D_s(x^a)=c_a x^{a+s}\) if \(0\le a+s<p\), and zero otherwise. Since the displayed multiplication respects polynomial degree, the degree components of any derivation are themselves derivations. If \(s<0\), then \(D_s(1)=0\), and \(D_s(x)=0\) unless \(s=-1\). For \(s=-1\), the equation \(1\star x=2x\) forces \(2D_s(x)=1\star D_s(x)=D_s(x)\), whence \(D_s(x)=0\). As \(1,x\) generate, all negative-degree derivations vanish.

**3. Classification in every nonnegative degree.** Fix \(0\le s\le p-1\), set \(\varepsilon=(-1)^s\) and \(\beta=2^s\in K^\times\), and restrict \(a\) to \(0\le a\le p-1-s\). Applying the derivation equation to \(x^a\star1=(-1)^a x^a\) and \(1\star x^a=2^a x^a\) gives respectively
\[
(1-\varepsilon)c_a=\beta c_0,\qquad
(1-\beta)c_a=\varepsilon c_0.
\]
If \(s\) is even, the first identity forces \(c_0=0\). The second forces all \(c_a=0\) unless \(\beta=1\). When \(\beta=1\), applying Leibniz to \(x^a\star x^b\) for \(a+b+s<p\) gives \(c_{a+b}=c_a+c_b\), hence \(c_a=ac_1\), provided \(s\le p-2\). This is precisely the one-dimensional space spanned by \(x^{s+1}d/dx\); for \(s=p-1\) only \(c_0\) exists and it has already vanished.

If \(s\) is odd, the first identity becomes \(2c_a=\beta c_0\). Taking \(a=0\) shows that a nonzero solution requires \(\beta=2\), in which case every \(c_a=c_0\). This is precisely the one-dimensional space spanned by multiplication by \(x^s\). In both surviving cases substitution into the monomial Leibniz equation proves sufficiency, including monomial products of degree at least \(p\) (all terms then vanish). No further equations occur.

**4. Arithmetic and Lie brackets.** The order \(d\) of \(2\) divides \(p-1\), and \(L=\operatorname{lcm}(2,d)\) also divides \(p-1\). The even surviving shifts are exactly \(s=jL\), and the odd shifts exactly \(s=1+jL\), both with \(0\le j<(p-1)/L=m\). This proves the basis and the dimension. Using the product rule for ordinary differentiation and the identity \([a(x)d/dx,b(x)d/dx]=(ab'-ba')d/dx\), together with \([a(x)d/dx,M_b]=M_{ab'}\), gives all three bracket formulas. Since \(0<1+jL<p\) and \(0<jL<p\) for \(j\ge1\), the brackets with \(H_0\) generate all \(E_j\) and \(H_j\) for \(j\ge1\), but no bracket has an \(H_0\) component. The derived-algebra and ideal statements follow. \(\square\)

## Verification

Run \(\texttt{python3 check_derivations.py}\) with Python 3 and no third-party packages. The checker constructs the **original quandle-basis** Leibniz linear equations, without using the proof's coordinate transformation or its basis in solving them, and computes their ranks modulo \(p\) for \(p\in\{3,5,7,11,13,17,19,23,31,37,41,43\}\). The resulting derivation dimensions are respectively \(2,2,2,2,2,4,2,2,6,2,4,6\), agreeing with the theorem. It separately checks the candidate operators against the monomial Leibniz equations for thirteen primes (including \(29\)) and verifies every stated Lie bracket by full matrix multiplication. All checks completed successfully. These finite checks corroborate, but do not replace, the preceding proof for all odd primes and all characteristic-\(p\) fields.

## Relationship to prior work

Elhamdadi, Makhlouf, Silvestrov, and Zappala's 2021 *The derivation problem for quandle algebras*, arXiv:2106.08289, gives the general structure-constant equation for derivations, characterizes dihedral-quandle derivations over **characteristic zero**, and tabulates positive-characteristic examples only for small quandle sizes (Section 4.2, sizes \(3\) through \(6\)). The present result solves the uniform equal-prime-characteristic problem, identifies the first nonconstant dimension at \(17\), and determines the entire Lie algebra and its brackets, not merely a nullspace equation. Aader's 2023 thesis surveys that characteristic-zero result and studies **group-conjugation** quandles; that is a different quandle product. Kaur and Singh's 2023 decomposition of Takasaki quandle rings concerns real and complex coefficient fields and their module decompositions, not the modular derivation Lie algebra. General structural equations and small tables are not asserted to be new here.

## Limitations

The work does not classify derivations in field characteristic unequal to quandle order or for composite-order quandles. The source comparison is not a guarantee of exhaustive worldwide novelty; an equivalent modular computation in unindexed work remains possible. The Lie structure is proved internally but has not undergone independent specialist validation. The separate algebraic equation for **idempotent elements** may exhibit the same logarithmic coordinates and arithmetic modulus \(L\), but does not determine the derivation Lie algebra; its generators and brackets require a separate Leibniz analysis.

## References

1. M. Elhamdadi, A. Makhlouf, S. Silvestrov, and E. Zappala, *The derivation problem for quandle algebras*, arXiv:2106.08289, first posted 2021-06-15. https://arxiv.org/abs/2106.08289
2. A. M. Aader, *Derivations on quandle algebras*, Master's thesis, University of Tartu, 2023. https://hdl.handle.net/10062/91201
3. D. Kaur and P. Singh, *Decomposition of quandle rings of Takasaki quandles*, arXiv:2303.06948, first posted 2023-03-13. https://arxiv.org/abs/2303.06948
4. V. G. Bardakov, I. B. S. Passi, and M. Singh, *Quandle rings*, arXiv:1709.03069, foundational construction.
