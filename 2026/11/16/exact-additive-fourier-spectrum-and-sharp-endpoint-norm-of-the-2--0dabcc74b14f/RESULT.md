# Exact additive Fourier spectrum and sharp endpoint norm of the \(2\times2\times2\) Segre cone

## Finding
Let \(q\ge2\) be any prime power, \(G=\mathbb F_q^2\otimes\mathbb F_q^2\otimes\mathbb F_q^2\), and \(C\subset G\) the affine cone of decomposable tensors (including zero). For any nontrivial additive character \(\psi\) of \(\mathbb F_q\), put
\[
 F(T)=\sum_{X\in C}\psi(\langle T,X\rangle),\qquad T\in G.
\]
Write \(g_q=(q^2-1)(q^2-q)\). The complete Fourier spectrum, including multiplicities, has exactly the following six levels for every \(q\ge2\):

| Incidence number \(B\) | Fourier value \(F=q(qB-q-2)\) | Multiplicity |
|:--|:--|:--|
| \(0\) | \(-q(q+2)\) | \(q^2(q-1)^2g_q/2\) |
| \(1\) | \(-2q\) | \((q+1)^2(q-1)g_q\) |
| \(2\) | \(q(q-2)\) | \(q^2(q+1)^2g_q/2\) |
| \(q+1\) | \(q(q^2-2)\) | \(2(q+1)g_q+q(q^2-1)^2\) |
| \(2q+1\) | \(q(2q^2-2)\) | \((q+1)^2(q^2-1)\) |
| \((q+1)^2\) | \(q^4+2q^3-2q\) | \(1\) |

For the Fourier projection \(P_C\) retaining precisely the frequency set \(C\), the sharp counting-measure endpoint norms are
\[
 \boxed{\|P_C\|_{\ell^1\to\ell^1}=\|P_C\|_{\ell^\infty\to\ell^\infty}
 =1+\frac{(q-1)^3(q+1)(q^4+q^3+2q^2+8q+4)}{q^6}.}
\]
Equivalently the norm is \(q^2-q+1+6q^{-1}-11q^{-2}-5q^{-3}+14q^{-4}-4q^{-6}\). For every \(q\ge3\), \(F(T)\ne0\) at every tensor, whereas for \(q=2\) there are exactly \(108\) zeros and the norm is \(55/16\). Thus the associated convolution matrix is invertible exactly when \(q\ge3\).

## Assumptions and scope
Throughout, \(q\) ranges over all prime powers, \(\mathbb F_q\) is a field of order \(q\), \(G\) has cardinality \(q^8\), and \(\langle\cdot,\cdot\rangle\) is the nondegenerate coordinatewise bilinear pairing in a fixed product basis. Identifying the dual group with \(G\) through \(\psi\), \(P_C f\) means the translation-invariant operator with Fourier multiplier \(\mathbf1_C\). All norms are for counting measure; their value is identical under uniform-probability normalization. The cone includes zero and has \(|C|=q^4+2q^3-2q\). No assertion is made about tensors of other formats, higher-order cones, or nonlinear operator norms.

## Proof
**1. Projective character reduction.** Every nonzero decomposable tensor belongs to one of \((q+1)^3\) projective Segre points, each with \(q-1\) nonzero scalar representatives. Orthogonality of additive characters gives
\[
 \sum_{a\in\mathbb F_q^\times}\psi(a t)=\begin{cases}q-1,&t=0,\\-1,&t\ne0.\end{cases}
\]
Let \(Z(T)\) count projective triples \(([u],[v],[w])\in(\mathbb P^1(\mathbb F_q))^3\) with \(T(u,v,w)=0\). Therefore
\[
 F(T)=1+qZ(T)-(q+1)^3.
\]
Represent \(T\) by a two-by-four matrix of slices, acting on \(u\otimes v\in\mathbb F_q^2\otimes\mathbb F_q^2\). Let \(B(T)\) be the number of points of the rank-one quadric
\[
 Q=\{[u\otimes v]:[u],[v]\in\mathbb P^1(\mathbb F_q)\}\subset\mathbb P^3(\mathbb F_q)
\]
that lie in the common kernel of both slices. For each \(([u],[v])\), the remaining equation in \([w]\) has one solution when its coefficient vector is nonzero, and \(q+1\) solutions when zero. It follows exactly that \(Z(T)=(q+1)^2+qB(T)\), hence
\[
 F(T)=q(qB(T)-q-2).
\]
This pointwise incidence reduction is a specialization of the general tensor-Cayley spectral framework in Byrne--François; it is **not** asserted as a new general Fourier identity.

**2. Rank-two slice census.** When the two-by-four slice matrix has rank two, the common kernel defines a projective line in \(\mathbb P^3\). Each such line arises from exactly \(g_q=|\mathrm{GL}_2(\mathbb F_q)|\) ordered independent slice pairs. A nondegenerate hyperbolic quadric has \((q+1)^2\) points and two generator rulings consisting of \(q+1\) lines each. Its projective line intersections have sizes \(q+1,2,1,0\), respectively.

There are \(2(q+1)\) lines contained in \(Q\). A tangent non-generator line through each point of \(Q\) is one of the other \(q-1\) lines through that point in its tangent plane; such a line meets \(Q\) exactly once. Thus there are \((q+1)^2(q-1)\) one-point lines. Every pair of distinct points of \(Q\) not sharing a generator line determines a secant; since each point lies on two generators and there are \(2(q+1)\) generators, the secant count is
\[
 \binom{(q+1)^2}{2}-2(q+1)\binom{q+1}{2}=\frac{q^2(q+1)^2}{2}.
\]
Since \(\mathbb P^3(\mathbb F_q)\) has \((q^2+1)(q^2+q+1)\) lines, the remaining \(q^2(q-1)^2/2\) lines miss \(Q\). Multiplying by \(g_q\) gives the four rank-two multiplicities.

**3. Rank-one and zero slice census.** Rank-one two-by-four matrices have a projective hyperplane as common kernel; each such hyperplane arises from exactly \(q^2-1\) nonzero two-component scalar multiples of a fixed functional. The \((q+1)^2\) tangent planes to \(Q\) cut it in two generators and have \(2q+1\) points. Of the \(q^3+q^2+q+1\) planes in total, the remaining \(q(q^2-1)\) cut \(Q\) in a nonsingular conic of \(q+1\) points. Thus rank one contributes \((q+1)^2(q^2-1)\) to \(B=2q+1\) and \(q(q^2-1)^2\) to \(B=q+1\). Finally \(T=0\) contributes one copy of \(B=(q+1)^2\). These are exactly all six rows of the table; their multiplicities sum to \(q^8\).

**4. Sharp endpoint norm.** By Fourier inversion the projection is convolution with \(K(T)=q^{-8}F(T)\) up to sign or transpose of the argument, irrelevant for the absolute norm. The \(\ell^1\) and \(\ell^\infty\) convolution norms are exactly \(\sum_T|K(T)|\): the point mass attains the former and the pointwise conjugate-phase selector attains the latter.

The only negative levels are \(B=0\) and \(B=1\); at \(B=2\), the value vanishes only when \(q=2\) and is positive for \(q>2\). Since \(\sum_TF(T)=q^8\), writing \(m_0,m_1\) for the first two row multiplicities,
\[
 \begin{aligned}
 \|P_C\|&=q^{-8}\sum_T|F(T)|\\
 &=1+2q^{-8}\big(q(q+2)m_0+2qm_1\big)\\
 &=1+\frac{(q-1)^3(q+1)(q^4+q^3+2q^2+8q+4)}{q^6}.
 \end{aligned}
\]
The zero classification follows because no other level can vanish for integer \(q\ge2\). In characteristic two with \(q\ge4\), the Fourier transform is still nowhere zero; the distinction is precisely the field of order two.

## Verification
The accompanying `check_spectrum.py` directly enumerates the entire tensor cone and its complete finite-field Fourier transform for field orders \(2,3,4,5\), using integer Walsh--Hadamard arithmetic for \(q=4\). An independent projective finite-geometry census enumerates all lines and hyperplanes for \(q=2,3,5,7\), confirming each of the four line-section and two hyperplane-section multiplicities. At all four field sizes the program checks the full coefficient-frequency table, the exact endpoint norm, Parseval identity and sum of coefficients. Reproduction: install the single dependency stated in `requirements.txt` and execute `python check_spectrum.py`. The expected final line is `SEGRE_FULL_SPECTRUM_AND_ENDPOINT_CHECKS_PASS`. These finite checks support, but do not replace, the general counting proof.

## Relationship to prior work
Lavrauw--Sheekey (arXiv:1207.3972, first public 2012-07-17) describe the projective Segre tensor geometry and group orbits. Byrne--François (arXiv:2607.03479) give a general Cayley-graph eigenvalue expression based on Segre intersections (Theorem 42 and Corollary 44) and calculate a larger \(2\times3\times3\) tensor-graph spectrum; consequently the character-incidence mechanism is **covered** by their work. The contribution here is the complete, directly verified six-level multiplicity census for the \(2\times2\times2\) geometry, its exactly evaluated sharp harmonic endpoint norm, and its field-order-two-only zero transition. A prior binary tensor-rank Fourier-shell table overlaps the \(q=2\) specialization; the new all-prime-power formula is not represented as an independently novel binary result. The inspected sources do not explicitly state the six-level all-field table and norm. No assertion of exhaustive historical priority is made.

## Limitations
The evaluated spectrum is confined to the full affine decomposable-tensor frequency cone in the \(2\times2\times2\) tensor format. The pointwise character reduction is an established special case of a general theorem; the new contribution is a complete explicit spectral *evaluation*, not a new general eigenvalue identity. The exceptional \(q=2\) specialization overlaps earlier finite binary data. Additional historical literature or tables may contain a formerly unnoticed exact equivalent. General validity rests on the combinatorial proof, while machine enumeration covers only the stated finite fields. Independent mathematical validation has not been performed.

## References
- M. Lavrauw and J. Sheekey, *Orbits of the stabiliser group of the Segre variety product of three projective lines*, arXiv:1207.3972 (first submitted 2012-07-17). https://arxiv.org/abs/1207.3972
- E. Byrne and L. François, *The multilinear forms Cayley graph and the eigenvalue method for tensor codes*, arXiv:2607.03479 (first submitted 2026-07-03; v2 2026-07-30), especially Theorem 42 and Corollary 44. https://arxiv.org/html/2607.03479v2
