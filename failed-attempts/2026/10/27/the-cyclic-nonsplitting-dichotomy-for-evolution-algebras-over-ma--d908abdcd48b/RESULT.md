# The cyclic nonsplitting dichotomy for evolution algebras over \(\mathbb F_4\)

## Finding
For every positive integer \(n\), all evolution algebras over \(\mathbb F_4\) whose natural-basis structure matrix is a nonzero weighted directed \(n\)-cycle are classified by parity. In odd dimension they form one isomorphism class with automorphism group \(C_n\) and exactly one nonzero idempotent. In even dimension there are exactly two classes: an unweighted cycle with \(\operatorname{Aut}\cong C_3\rtimes C_n\) and three nonzero idempotents, and a twisted cycle with \(\operatorname{Aut}\cong C_{3n/2}\) and no nonzero idempotents. The twisted class has a canonical nonsplit permutation-automorphism extension precisely when \(6\mid n\). In particular, an infinite sequence of simple evolution algebras has such nonsplit extensions.

## Assumptions and scope
Let \(K=\mathbb F_4\), and fix \(\omega\in K\) with \(\omega^2+\omega+1=0\). Thus \(K^\times=\langle\omega\rangle\cong C_3\). For each \(n\ge1\) and \(a=(a_0,\ldots,a_{n-1})\in(K^\times)^n\), define the commutative, generally nonassociative evolution algebra \(E(a)\) with natural basis \(e_0,\ldots,e_{n-1}\), distinct basis products zero, and \(e_i^2=a_i e_{i+1\bmod n}\). The special normal forms \(E_c\) have \(a_i=1\) for \(0\le i<n-1\) and \(a_{n-1}=c\). The automorphism groups below are groups of \(K\)-linear algebra automorphisms, not automorphism group schemes. The canonical permutation representation records the image of each natural basis line.

## Proof
**(1) Simplicity and monomial rigidity.** The structure matrix is a weighted permutation matrix, hence invertible: \(E(a)^2=E(a)\). If an ideal contains a nonzero vector \(v=\sum v_i e_i\), choose \(i\) with \(v_i\ne0\). Then \(v e_i=v_i a_i e_{i+1}\) belongs to the ideal. Taking successive squares produces every basis vector because the graph is one directed cycle. Therefore every nonzero ideal is the whole algebra. Moreover, if \(f_i=\sum_j u_{ji}e_j\) is the image of a natural basis under any automorphism, then \(f_i f_k=0\) for \(i\ne k\). Since the squares of the target natural basis are linearly independent, \(u_{ji}u_{jk}=0\) for every \(j\) and \(i\ne k\). Invertibility makes the automorphism matrix monomial. Preservation of the sole outgoing edge at each vertex forces its permutation to be a rotation \(i\mapsto i+j\pmod n\).

**(2) Normal forms and isomorphism invariants.** A diagonal change \(f_i=t_i e_i\) changes the outgoing coefficient to \(t_i^2a_i/t_{i+1}\). Choose \(t_{i+1}=t_i^2a_i\) for \(0\le i<n-1\). This makes all but the final coefficient equal to one. The final coefficient then has the form \(c(t_0)=\bigl(\prod_{i=0}^{n-1}a_i^{2^{n-1-i}}\bigr)t_0^{2^n-1}\). Since \(K^\times\) has order three, when \(n\) is odd the map \(t_0\mapsto t_0^{2^n-1}\) is bijective and \(c\) can be normalized to one. When \(n\) is even, \(t_0^{2^n-1}=1\) and the residual coefficient \(c\in\{1,\omega,\omega^2\}\) is independent of this diagonal choice.

For an isomorphism \(E_c\to E_d\), monomial rigidity gives \(F(e_i)=t_i e_{i+j}\). Put \(c=\omega^u\), \(d=\omega^v\), and \(t_i=\omega^{x_i}\). Comparing the images of the squares gives the exact recurrence \(x_{i+1}=2x_i+\beta_{i+j}-\alpha_i\pmod3\), where \(\alpha_i=0\) except \(\alpha_{n-1}=u\), and \(\beta_i=0\) except \(\beta_{n-1}=v\). Closing this recurrence gives
\[
(2^n-1)x_0+2^jv-u=0\pmod3.
\]
For even \(n\), this is equivalent to \(u=2^jv\pmod3\). Thus \(1\) cannot be isomorphic to \(\omega\) or \(\omega^2\), while a one-step rotation exchanges the two nontrivial normal forms. There are exactly two classes. For odd \(n\), the first part already gives exactly one.

**(3) Automorphism groups.** Apply the closing equation with \(d=c\), so \(u=v\). When \(n\) is odd, \(2^n-1\equiv1\pmod3\), hence every rotation has exactly one lift, giving \(\operatorname{Aut}(E_1)\cong C_n\) with trivial diagonal kernel. For even \(n\) and \(c=1\), every rotation has three lifts. The pure rotations split the extension and generate a subgroup \(C_n\). The diagonal kernel consists of \(\delta_z(e_i)=z^{2^i}e_i\), \(z^3=1\), and a one-step rotation acts on it by inversion. Therefore \(\operatorname{Aut}(E_1)\cong C_3\rtimes C_n\), with inversion action (well-defined since \(n\) is even).

When \(n=2m\) and \(c=\omega\), the closing equation permits precisely the even rotations and gives exactly three lifts for each. Thus \(|\operatorname{Aut}(E_\omega)|=3m\), the natural permutation image is \(C_m\), and the diagonal kernel is \(C_3\). Construct the explicit automorphism \(\phi\) by
\[
\phi(e_i)=e_{i+2}\ (0\le i\le n-3),\qquad
\phi(e_{n-2})=\omega e_0,\quad
\phi(e_{n-1})=\omega^2e_1.
\]
The multiplication identities verify directly that \(\phi\) is an automorphism. It rotates indices by two; after \(m\) applications, each even basis vector has acquired precisely one factor \(\omega\) and each odd vector one factor \(\omega^2\). Therefore \(\phi^m=\delta_\omega\), a diagonal automorphism of order three. Since the permutation image of \(\phi\) has order \(m\), \(\phi\) has order \(3m\). This equals the full automorphism-group order, giving \(\operatorname{Aut}(E_\omega)\cong C_{3m}\). The canonical exact sequence is \(1\to C_3\to C_{3m}\to C_m\to1\). A cyclic group of order \(3m\) has a complement to its subgroup of order three exactly when \(\gcd(3,m)=1\). Hence the extension is nonsplit exactly when \(3\mid m\), equivalently \(6\mid n\).

**(4) Nonzero idempotents.** If \(x=\sum x_i e_i\) satisfies \(x^2=x\), the relations are \(x_{i+1}=a_ix_i^2\) cyclically. Either all coordinates vanish or all are nonzero. For normal form \(E_c\), the first coordinate must satisfy \(x_0^{2^n-1}=c^{-1}\); each solution determines all coordinates. In odd dimension the power exponent equals one modulo three, so exactly one nonzero idempotent occurs. In even dimension the exponent is divisible by three: there are three nonzero idempotents when \(c=1\), and none when \(c\ne1\). This completes the classification.

## Verification
Run the included standalone \(`verify.py`\) with Python 3. It independently enumerates all \(3^n\) weighted-cycle coefficient vectors for \(1\le n\le7\), enumerates their allowed monomial maps and compares isomorphism classes and automorphism-group orders. It directly enumerates idempotent vectors for \(1\le n\le5\) and checks the existence of a generator of order \(3n/2\) for twisted even-cycle dimensions \(2,4,6,8,10,12,18,24\). The actual packaged checker terminates with \(`VERIFY_OK`\). The unrestricted theorem rests on the proof, not on this finite test.

## Relationship to prior work
Kaygorodov, Martín González and Viruel (arXiv:2610.22248v1, Proposition 21, pp. 18–19) already exhibited a **different six-dimensional perfect evolution algebra** with nonsplit automorphism extension \(C_3\hookrightarrow C_9\twoheadrightarrow C_3\). The source's support graph is three directed two-cycles with additional edges, not one weighted directed cycle; it also formulates Question 33 about characterizing splitting. Thus the existence of a nonsplit extension, or of one order-nine automorphism group, is not claimed as new. The contribution here is the **uniform complete classification over \(\mathbb F_4\)** for simple weighted cycle algebras in every dimension, including the exact split/nonsplit cutoff.

Costoya, Mayorga and Viruel (2025), building on Elduque–Labra, provide the general monomial automorphism sequence; it does not provide the above group orders or splitting dichotomy for the weighted-cycle family. Narkuziyev (2018, 2020) studied permutation-associated evolution algebras and idempotents; the scalar idempotent recurrence here is explicitly not asserted to be novel on its own. Wei and Zou (2023) offer general isomorphism-orbit methods, but no located statement was found implying this infinite-field-four nonsplitting classification.

## Limitations
The theorem concerns \(K\)-rational linear automorphism groups over \(\mathbb F_4\) for weighted **single** directed cycles only. It is not a classification of general evolution algebras or of their automorphism group schemes. The small-field enumeration is confirmatory, not an infinite proof. Earlier or unindexed results on permutation evolution algebras may imply parts of the normal-form or idempotent calculations; the group-extension classification is the focal assertion. No independent mathematical audit has been performed.

## References
1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems* (2026), arXiv:2610.22248v1, especially Proposition 21 and Question 33. https://arxiv.org/abs/2610.22248
2. C. Costoya, P. Mayorga, A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, Mediterranean J. Math. 22 (2025), article 149. https://doi.org/10.1007/s00009-025-02924-0
3. B. Narkuziyev, *On absolute nilpotent and idempotent elements of an evolution algebra corresponding to permutations* (2018), arXiv:1803.11415. https://arxiv.org/abs/1803.11415
4. B. Narkuziyev, *Some remarks on evolution algebras corresponding to permutations* (2020), arXiv:2005.05793. https://arxiv.org/abs/2005.05793
5. W. Wei, Y. Zou, *Isomorphism Classes of Idempotent Evolution Algebras* (2023), arXiv:2310.12368. https://arxiv.org/abs/2310.12368
