# A universal one-third law for idempotent-free two-dimensional perfect evolution algebras

## Finding
Let \(q\ge2\) be a prime power, let \(K=\mathbb F_q\), and choose \(M\) uniformly from \(\mathrm{GL}_2(K)\). Form the two-dimensional evolution algebra with an ordered natural basis \(e_1,e_2\), cross product \(e_1e_2=0\), and structure matrix \(M\) with column convention \(e_i^2=\sum_j M_{ji}e_j\). Write \(N=N(M)\) for the number of **nonzero** idempotents. Then \(N\le3\), and its entire distribution is
\[
\begin{array}{c|cccc}
 &\Pr(N=0)&\Pr(N=1)&\Pr(N=2)&\Pr(N=3)\\\hline
q\text{ even}&\frac13&\frac12&0&\frac16\\[2pt]
q\text{ odd}&\frac13&\frac{q^2+1}{2q(q+1)}&\frac{q-1}{q(q+1)}&\frac{q^2-2q+3}{6q(q+1)}
\end{array}
\]
In particular, precisely one third of all invertible \(2\times2\) structure matrices yield algebras with no nonzero idempotents, **independent of the finite field**. In odd characteristic the probability of exactly two nonzero idempotents is \((q-1)/(q(q+1))\); in characteristic two it is zero.

## Assumptions and scope
The sample space is the set of invertible matrices \(M\in\mathrm{GL}_2(K)\), each equally likely, with a specified ordered natural basis. The statement is **not** a count of isomorphism classes with equal class weights. An idempotent is a solution of \(x=M(x_1^2,x_2^2)^T\); the zero solution is deliberately excluded. Every prime power, including characteristic two and small fields, is covered.

## Proof
**Step 1 (projective correspondence).** Define \(s:\mathbb P^1(K)\to\mathbb P^1(K)\) by \(s([u:v])=[u^2:v^2]\), and let \(f_M=[M]\circ s\). For a nonzero vector \(v\in K^2\), \([v]\) is fixed by \(f_M\) exactly when \(Mv^{[2]}=\lambda v\) for some \(\lambda\in K^\times\). The scalar is nonzero because \(M\) is invertible. For this line, \(x=\lambda^{-1}v\) is the unique nonzero idempotent, since \(M(tv)^{[2]}=t^2\lambda v=tv\) requires \(t=\lambda^{-1}\). This correspondence does not depend on the chosen representative \(v\). Hence \(N\) equals the number of fixed points of \(f_M\) on \(\mathbb P^1(K)\).

Writing \(M=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), a projective fixed point \([X:Y]\) satisfies the nonzero binary cubic
\[
-cX^3+aX^2Y-dXY^2+bY^3=0.
\]
The four coefficients cannot all vanish for invertible \(M\). Thus \(0\le N\le3\) for every field, including the smallest fields.

**Step 2 (factorial moments).** Set \(P=\mathbb P^1(K)\), so \(|P|=q+1\). Scalar multiples of \(M\) induce the same projective map, and a uniform matrix induces a uniform element of \(\mathrm{PGL}_2(K)\). This group acts transitively on ordered distinct one- and two-tuples and *sharply* transitively on ordered distinct triples: an ordered triple of distinct projective points determines a unique projective linear map to any other such triple. It has order \((q+1)q(q-1)\).

For \(r\in\{1,2,3\}\), an ordered distinct \(r\)-tuple \((x_1,\dots,x_r)\in P^r\) can be simultaneously fixed by \(f_M\) only when \(s(x_1),\dots,s(x_r)\) are distinct. For such a tuple the probability that \([M]s(x_i)=x_i\) for every \(i\) equals
\[
\frac{1}{(q+1)q\cdots(q+2-r)}.
\]
Consequently the falling factorial moment \(\mathbb E[(N)_r]\) equals the number of ordered distinct \(r\)-tuples having pairwise distinct square images divided by this denominator.

**Step 3 (square-image collisions).** For even \(q\), squaring is a bijection of \(K\), hence of \(P\). Every ordered distinct tuple has distinct square images, so
\[
\mathbb E[N]=\mathbb E[(N)_2]=\mathbb E[(N)_3]=1.
\]
For odd \(q\), the only square-image collisions on \(P\) are \(t\leftrightarrow-t\) for \(t\in K^\times\); both \(0\) and \(\infty\) have singleton fibers. There are exactly \(q-1\) forbidden ordered distinct pairs. Therefore
\[
\mathbb E[N]=1,\qquad
\mathbb E[(N)_2]=\frac{(q+1)q-(q-1)}{(q+1)q}=
\frac{q^2+1}{q(q+1)}.
\]
For ordered distinct triples, choose which two positions form the colliding pair (three choices), choose its first nonzero value (\(q-1\) choices), and choose the third projective point outside this pair (\(q-1\) choices). No forbidden triple is counted twice, because a square fiber contains at most two points. Hence there are \(3(q-1)^2\) forbidden triples and
\[
\mathbb E[(N)_3]
=1-\frac{3(q-1)^2}{(q+1)q(q-1)}
=\frac{q^2-2q+3}{q(q+1)}.
\]

**Step 4 (recover the distribution).** Write \(p_j=\Pr(N=j)\) for \(0\le j\le3\), and let \(m_r=\mathbb E[(N)_r]\). Since \(N\le3\),
\[
p_3=\frac{m_3}{6},\qquad
p_2=\frac{m_2-m_3}{2},\qquad
p_1=m_1-m_2+\frac{m_3}{2},\qquad
p_0=1-m_1+\frac{m_2}{2}-\frac{m_3}{6}.
\]
Substitution gives the displayed laws. In particular, in both characteristics the final expression for \(p_0\) simplifies identically to \(1/3\), not just asymptotically. The proof covers all prime powers without a genericity or separability assumption.

## Verification
The standalone `verify.py` enumerates every invertible structure matrix over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8,\mathbb F_9,\mathbb F_{11}\), compares exact integer histogram counts to the formula, and checks finite-field arithmetic. For \(q\le5\), it additionally enumerates all nonzero coordinate vectors and confirms that the original algebraic idempotent equations yield the same counts as the projective fixed-point criterion. The checker prints `VERIFY_OK` on success. This finite cross-check is not used to infer the unrestricted theorem.

## Relationship to prior work
Kaygorodov, Martín González and Viruel [1] study the existence and average number of idempotents over finite fields, and their survey collects further open questions. The expected value \(\mathbb E[N]=1\) is background, not claimed as new here. The distinct result established here is the **entire** dimension-two distribution, especially the exact field-independent \(1/3\) probability of idempotent-freeness and the odd-characteristic two-idempotent stratum. Cabrera Casado, Martín Barquero and Martín González [2] classify two-dimensional perfect evolution algebras over domains; their classification has a different purpose from the uniform labeled-matrix distribution. Wei and Zou [3] count isomorphism classes of perfect evolution algebras, using a different weighting on objects. The proof's projective viewpoint is related to standard three-transitivity of \(\mathrm{PGL}_2\), used here as an elementary group-theoretic ingredient.

## Limitations
The result concerns dimension two and uniform sampling of invertible matrices only. It does not give the distribution for higher dimensions or for uniform sampling of isomorphism classes. It is a self-review, not an independent audit. The finite-field probability count does not identify all possible moduli representatives or automorphism groups. Equivalent formulas in older literature on finite-field rational maps or cubic root statistics remain possible.

## References
[1] I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first submitted 2026-10-15), https://arxiv.org/abs/2610.22248.

[2] Y. Cabrera Casado, D. Martín Barquero, C. Martín González, *Two-dimensional perfect evolution algebras over domains*, Journal of Algebraic Combinatorics **58** (2023), 569–587, https://doi.org/10.1007/s10801-022-01196-1.

[3] Y. Wei, Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, Linear Algebra and its Applications **675** (2023), 142–178, arXiv:2310.12368, https://arxiv.org/abs/2310.12368.
