# Smooth coloring components and Potts counts of commuting idempotents in incidence algebras
## Finding
Let \(P\) be any nonempty finite poset, \(K\) any field, and \(r\geq1\). Write \(A=I(P,K)\) for its incidence algebra, and let \(\mathcal E_{P,r}\) be the affine scheme of ordered \(r\)-tuples of elements of \(A\) that are idempotent and commute pairwise. Let \(G(P)\) be the **comparability graph**: its edges are *all* strict comparable pairs \(x<y\), not just covers. Set \(Q=2^r\). A coloring is any map \(c:P\to\{0,1\}^r\), and
\[
 m(c)=\#\{(x,y):x<y\text{ in }P,\ c(x)\ne c(y)\}.
\]

**Theorem.** The scheme \(\mathcal E_{P,r}\) is smooth over \(K\). It has exactly \(Q^{|P|}\) geometrically irreducible connected components, indexed by the diagonal colorings \(c\). The component with coloring \(c\) has dimension \(m(c)\), and every point in it over every extension field of \(K\) is conjugate to the same diagonal tuple by an element of \(1+J\), where \(J\) is the strictly upper incidence ideal. If \(K=\mathbb F_q\), the component has precisely \(q^{m(c)}\) rational points. Consequently the exact total is
\[
 \boxed{N_{P,r}(q)=\sum_{c:P\to\{0,1\}^r}q^{m(c)}.}
\]
If \(E\) is the edge set of \(G(P)\), and \(\kappa(S)\) is the number of connected components of the spanning subgraph \((P,S)\), this is the equivalent random-cluster expansion
\[
 \boxed{N_{P,r}(q)=\sum_{S\subseteq E}q^{|E|-|S|}(1-q)^{|S|}Q^{\kappa(S)},\qquad Q=2^r.}
\]
Thus the numbers of commuting-idempotent tuples, as \(q\) runs through prime powers and \(r\) through positive integers, determine the ordinary Tutte polynomial of the comparability graph (not generally the graph itself).

## Assumptions and scope
The incidence algebra has basis \(e_{xy}\) for \(x\leq y\) and multiplication \(e_{xy}e_{uv}=\delta_{y,u}e_{xv}\). The ideal \(J\) consists of elements with zero diagonal. It is nilpotent, and the diagonal quotient is \(A/J\cong K^P\). No characteristic restriction, connectedness assumption on \(P\), or algebraic closure hypothesis is imposed. A tuple is **ordered**; its members need not be distinct and can equal zero or one. The claim concerns exact equations \(E_i^2=E_i\) and \(E_iE_j=E_jE_i\) for all indices, not arbitrary simultaneously triangularizable operators or idempotent sums. Geometric components refer to the scheme after extension to an algebraic closure.

## Proof
**Step 1: diagonal labels and simultaneous spectral idempotents.** If \((E_1,\ldots,E_r)\) is a commuting-idempotent tuple, its diagonal entries are zeros or ones, defining \(c(x)=(E_1(x,x),\ldots,E_r(x,x))\). For each binary word \(s\in\{0,1\}^r\) put
\[
 f_s=\prod_{i=1}^r\begin{cases}E_i,&s_i=1,\\1-E_i,&s_i=0.\end{cases}
\]
These are pairwise orthogonal idempotents with \(\sum_s f_s=1\). Their diagonal reductions equal those of the canonical mutually orthogonal diagonal idempotents
\[
 d_s=\sum_{x:c(x)=s}e_{xx}.
\]
The products are unambiguous because the given \(E_i\) commute.

**Step 2: conjugacy, including the nonempty and empty spectral blocks.** Define \(u=\sum_s f_s d_s\). Its image modulo \(J\) is \(\sum_s d_s=1\), so \(u\in1+J\) and is invertible because \(J\) is nilpotent. Orthogonality gives \(ud_s=f_sd_s=f_su\) for each \(s\). Hence \(f_s=ud_su^{-1}\), and therefore
\[
 E_i=uD_i(c)u^{-1},\qquad D_i(c)=\sum_{x:c(x)_i=1}e_{xx}.
\]
This also proves transitivity for every field extension, with no assumption that each word \(s\) is used. The diagonal coloring is invariant under conjugation by \(1+J\), so distinct colorings cannot coalesce.

**Step 3: point counts and orbit dimensions.** The algebraic group \(U=1+J\) has \(\dim U=|E|\) and, over \(\mathbb F_q\), cardinality \(q^{|E|}\). An element \(1+v\in U\) fixes all the \(D_i(c)\) precisely when \(v(x,y)=0\) for each \(x<y\) with \(c(x)\ne c(y)\). Thus its stabilizer is the smooth group \(1+J_c\), where \(J_c\) is the linear span of those \(e_{xy}\) whose endpoints have equal colors. It has dimension \(|E|-m(c)\) and \(q^{|E|-m(c)}\) points. Orbit-stabilizer gives exactly \(q^{m(c)}\) rational points, and the orbit has dimension \(m(c)\).

**Step 4: scheme smoothness and geometric irreducibility.** For each diagonal position \((x,x)\), linearizing \(E_i^2-E_i=0\) forces every diagonal tangent coefficient to vanish because \(2c(x)_i-1\) is \(\pm1\) in any characteristic. At an off-diagonal position \((x,y)\) with \(x<y\), writing \(z_i\) for the infinitesimal perturbation of \(E_i(x,y)\), the linearized relations are
\[
 (c(x)_i+c(y)_i-1)z_i=0,
 \qquad (c(x)_i-c(y)_i)z_j-(c(x)_j-c(y)_j)z_i=0.
\]
If \(c(x)=c(y)\) the only solution is the zero vector; if \(c(x)\ne c(y)\), the solution space is the one-dimensional span of \(c(x)-c(y)\). Therefore the tangent-space dimension at the diagonal tuple is exactly \(m(c)\). Conjugation transports this statement to every geometric point. Since the whole fixed-color fiber is the orbit of \(U\), a smooth irreducible homogeneous orbit of dimension \(m(c)\), its scheme tangent dimension equals its local dimension everywhere; the defining scheme is smooth and reduced there. Diagonal entries take values in the finite étale set \(\{0,1\}\), so fixed-color fibers are both open and closed. They are consequently exactly the geometrically irreducible connected components.

**Step 5: polynomial identity and Tutte recovery.** For any edge \(xy\) and coloring \(c\),
\[
 q^{\mathbf1_{c(x)\ne c(y)}}=q+(1-q)\mathbf1_{c(x)=c(y)}.
\]
Multiply over all comparable pairs, expand over edge subsets \(S\), and sum over colorings. An edge subset \(S\) imposes equal colors along each of its connected components, leaving \(Q^{\kappa(S)}\) possibilities. This proves the second displayed formula. The right side is the random-cluster polynomial after the invertible change of variables from \((Q,q)\) to the usual random-cluster variables \((Q,v)\), where \(v=(1-q)/q\). It therefore determines the Tutte polynomial. Values at infinitely many \(Q=2^r\) determine the polynomial in \(Q\) for each \(q\); values at infinitely many prime powers \(q\) then determine the remaining polynomial coefficients. There is no claim that a fixed finite selection of \((q,r)\) distinguishes posets or graphs.

## Verification
The standalone `verify.py` enumerates all incidence-algebra elements and directly checks the complete commuting-idempotent equations for finite instances, independently of conjugation or orbit-stabilizer. It also constructs the complete linearized equation matrix at every binary diagonal coloring and checks its rank. It exercises \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) (the last using a polynomial-field implementation), including the four-element diamond poset. The expected and observed tuple counts are \(120\) for a two-element chain with \((q,r)=(2,3)\); \(340,976,2116\) for a three-element chain with \((q,r)=(2,2),(3,2),(4,2)\); \(400\) for a three-element fork with \((3,2)\); and \(4132\) for the diamond with \((2,2)\). The script also checks two other two-element-chain cases and prints `VERIFY_OK` on success. These finite enumerations are consistency tests, not a substitute for Steps 1–5.

For illustration, if \(P\) is a three-element chain, every strict pair is an edge and
\[
 N_{P,r}(q)=Q+3Q(Q-1)q^2+Q(Q-1)(Q-2)q^3.
\]
If \(P\) is a fork consisting of two incomparable minimal elements below a maximum, then
\[
 N_{P,r}(q)=Q\bigl(1+(Q-1)q\bigr)^2.
\]

## Relationship to prior work
The recent incidence-algebra grading framework of Hindi and Schutzer (arXiv:2609.21184v1, publicly posted September 18, 2026) foregrounds complete families of orthogonal idempotents. Dos Santos and Yasumura (arXiv:2406.19329, available full manuscript) classify group gradings on incidence algebras and describe their Peirce-block structure, but their results address grading equivalence rather than the ordinary commuting-idempotent scheme and its point-count and component dimensions. Gargate and Gargate (arXiv:2009.04243) give counts of **single** potent matrices in incidence algebras. Their earlier arXiv:1907.06805 gives involution counts over finite fields of odd characteristic; via the equivalence between an idempotent and an involution, this covers the one-tuple specialization in odd characteristic. Neither single-element enumerator gives the unrestricted **simultaneously commuting** tuples, their fixed-color fibers, and their scheme geometry. Garcés and Khrypchenko (2022) study maps preserving idempotents, which is a different functional question. Standard conjugacy of complete orthogonal idempotent lifts is used explicitly as a proof ingredient; novelty is not claimed for that lifting principle itself. The additional geometric and Potts-polynomial information is not asserted to supersede grading or potent-element classifications.

## Limitations
A covering formulation may occur under terminology such as split-separable algebra homomorphisms, pattern-algebra projection varieties, or orthogonal idempotent lift systems; the historical originality comparison is not exhaustive. Full text of the September 2026 motivating preprint and the 2020 potent-matrix preprint was not obtained. A general conjugacy lemma plus a short stabilizer computation also makes the proof relatively elementary; this limits claims about technical depth, although the complete smooth-component classification and multivariate enumerator are substantive structural information. The result concerns finite posets; no theorem for infinite locally finite posets, arbitrary finite base rings, or noncommuting idempotents is asserted. The polynomial counts do not recover the full poset up to isomorphism.

## References
1. F. de Mattos Chafik Hindi and W. Schutzer, *A classification of group gradings on incidence algebras over commutative rings*, arXiv:2609.21184v1 (September 18, 2026).
2. H. S. Dos Santos and F. Y. Yasumura, *Group gradings on finite-dimensional incidence algebras. II*, arXiv:2406.19329 (June 27, 2024); full manuscript: https://www.ime.usp.br/~fyyasumura/manuscripts/Group_gradings_on_Incidence_Algebras__II.pdf.
3. I. Gargate and M. Gargate, *(k+1)-potent Matrices in triangular matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243 (2020).
4. I. Gargate and M. Gargate, *Involutions on Incidence Algebras of Finite Posets*, arXiv:1907.06805 (July 16, 2019).
5. J. J. Garcés and M. Khrypchenko, *Potent preservers of incidence algebras*, Linear Algebra and its Applications 635 (2022), 171–200, DOI:10.1016/j.laa.2021.11.020.
6. E. Spiegel and C. J. O'Donnell, *Incidence Algebras*, Marcel Dekker (1997), for the standard nilpotent radical and convolution conventions.
