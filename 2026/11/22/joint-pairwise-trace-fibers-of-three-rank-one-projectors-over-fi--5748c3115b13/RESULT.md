# Joint pairwise-trace fibers of three rank-one projectors over finite fields

## Finding

Let \(K=\mathbb F_q\) be any finite field, including even characteristic, and let \(\mathcal P\) be the set of rank-one idempotents in \(M_2(K)\). For each ordered triple \((a,b,c)\in K^3\), define
\[
\Phi_q(a,b,c)=\#\{(E,F,G)\in\mathcal P^3:\operatorname{tr}(EF)=a,\ \operatorname{tr}(FG)=b,\ \operatorname{tr}(GE)=c\}.
\]
Put \(A=a(1-a)\), \(C=c(1-c)\), and \(d=b-(1-a-c+2ac)\). Let \(r_q(d,z)\) be the number of roots in \(K^\times\) of \(s^2-ds+z=0\). Then **every joint fiber**, including the empty fibers, is exactly
\[
\boxed{\Phi_q(a,b,c)=q(q+1)\begin{cases}
(q-1)r_q(d,AC),&AC\ne0,\\
q-1,&\text{exactly one of }A,C\text{ is zero and }d=0,\\
2(q-1),&\text{exactly one of }A,C\text{ is zero and }d\ne0,\\
2q^2-1,&A=C=0,\ d=0,\\
2(q-1),&A=C=0,\ d\ne0.
\end{cases}}
\]
The **exact number of attainable triples of trace values** is
\[
\boxed{\#\{(a,b,c):\Phi_q(a,b,c)>0\}=\frac{q^3+4q^2-4q+\epsilon_q}{2},\qquad\epsilon_q=\begin{cases}1,&q\text{ odd},\\0,&q\text{ even}.\end{cases}}
\]
Thus, as \(q\) increases, asymptotically half of all prescribed joint trace triples are unattainable. The maximum fiber has size \(q(q+1)(2q^2-1)\) and occurs at exactly four targets, namely \((a,b,c)=(0,1,0),(0,0,1),(1,0,0),(1,1,1)\).

## Assumptions and scope

The field \(K\) is arbitrary finite of cardinality \(q\ge2\); all traces are ordinary matrix traces, no self-adjointness or positivity is assumed, and every factor is a **nonzero rank-one** idempotent. The triple order matters. A trace fiber is evaluated for *each field element* \(a,b,c\), not just for equality or square classes. When \(AC\ne0\), the polynomial has no zero root, so the root count is either zero, one or two. In odd characteristic, it equals \(1+\chi(d^2-4AC)\), with \(\chi(0)=0\). In characteristic two, it is one when \(d=0\); when \(d\ne0\), it is two precisely when \(\operatorname{Tr}_{K/\mathbb F_2}(AC/d^2)=0\), and otherwise zero. These are equivalent formulations of the same formula. The support expression counts distinct triples \((a,b,c)\), not the number of ordered projector triples.

## Proof

**1. Projector normalization.** A rank-one idempotent \(P\) is determined by a one-dimensional image and complementary kernel. There are \(q+1\) images and \(q\) permitted kernels per image, so \(|\mathcal P|=q(q+1)\). Conjugation by \(\operatorname{GL}_2(K)\) acts transitively on \(\mathcal P\), and simultaneously conjugating \((E,F,G)\) does not alter their three pairwise traces. Thus it suffices to fix \(E=\operatorname{diag}(1,0)\), calculate \(N_q(a,b,c)\), and multiply by \(q(q+1)\).

**2. Reduction to one quadratic.** Every rank-one idempotent has trace one and determinant zero, and conversely trace one and determinant zero imply idempotence by Cayley--Hamilton even in characteristic two. Consequently write uniquely
\[
F=\begin{pmatrix}a&x\\y&1-a\end{pmatrix},\quad xy=A=a(1-a),\qquad
G=\begin{pmatrix}c&u\\v&1-c\end{pmatrix},\quad uv=C=c(1-c).
\]
The two traces involving \(E\) are already \(a,c\), while direct multiplication gives
\[
\operatorname{tr}(FG)=1-a-c+2ac+xv+yu.
\]
The desired fixed-\(E\) count is therefore the cardinality of
\[
xy=A,\qquad uv=C,\qquad xv+yu=d.\tag{1}
\]
If \(AC\ne0\), all four variables are nonzero. Set \(s=xv\), \(t=yu\). Then \(s+t=d\), \(st=AC\), so \(s\) must solve \(s^2-ds+AC=0\). Conversely, for each nonzero root \(s\) and each \(x\in K^\times\), define uniquely \(y=A/x\), \(v=s/x\), and \(u=Cx/s\). This is a bijection, proving \(N_q=(q-1)r_q(d,AC)\).

**3. Degenerate strata.** If \(A\ne0\) and \(C=0\), then \(x,y\) are nonzero, with exactly \(q-1\) choices for the pair. For each, \(uv=0\) forces \(u=0\) or \(v=0\). The linear equation \(xv+yu=d\) has two distinct such solutions for \(d\ne0\) and the single common solution \((u,v)=(0,0)\) for \(d=0\). Hence the counts are \(2(q-1)\) and \(q-1\). The case \(A=0,C\ne0\) is symmetric under exchanging \((x,y)\) with \((u,v)\). Finally, if \(A=C=0\), split into \((x,y)=(0,0)\), \((x\ne0,y=0)\), and \((x=0,y\ne0)\). For \(d\ne0\), the latter two categories each contribute \(q-1\); the zero pair contributes none. For \(d=0\), they contribute \(q(q-1)\) apiece and the zero pair contributes \(2q-1\), totaling \(2q^2-1\). These cases partition all inputs to (1), proving the complete fiber formula.

**4. Attainable trace triples.** The degenerate parameter pairs \((a,c)\), where \(A=0\) or \(C=0\), number \(q^2-(q-2)^2=4(q-1)\) (since \(a(1-a)=0\) exactly for \(a\in\{0,1\}\)). Each supports all \(q\) values of \(b\). For the remaining \((q-2)^2\) pairs, put \(z=AC\ne0\). A value \(d\) is attainable exactly when \(d=s+z/s\) for some \(s\ne0\), the image of the involution \(s\mapsto z/s\) on \(K^\times\).

If \(q\) is even, the involution has exactly one fixed point because \(s^2=z\) has exactly one solution, so its image has \(q/2\) elements for every \(z\). If \(q\) is odd, it has \(1+\chi(z)\) fixed points, hence the image size is \((q+\chi(z))/2\). To sum this over all nondegenerate \((a,c)\), use multiplicativity to obtain
\[
\sum_{a,c\notin\{0,1\}}\chi\bigl(a(1-a)c(1-c)\bigr)
=\left(\sum_{a\in K}\chi\bigl(a(1-a)\bigr)\right)^2=1.
\]
The last identity follows from \(a(1-a)=-(a-1/2)^2+1/4\) and the elementary character sum \(\sum_t\chi(t^2-1)=-1\). The latter is proved directly by counting \((t,z)\in K^2\) with \(z^2=t^2-1\), equivalently \((t-z)(t+z)=1\), which has exactly \(q-1\) solutions because two is invertible. Thus the generic support size is \((q(q-2)^2+1)/2\) in odd characteristic, and \(q(q-2)^2/2\) in even characteristic. Adding the \(4q(q-1)\) degenerate-support triples produces the claimed closed expression.

**5. Maximum.** In any nondegenerate or one-degenerate stratum the fixed-\(E\) fiber is at most \(2(q-1)\), strictly below \(2q^2-1\). Therefore the latter is the unique maximal fixed-\(E\) value, attained exactly when \(A=C=d=0\). The choices \(a,c\in\{0,1\}\) give exactly four targets; their corresponding \(b=1-a-c+2ac\) equals one when \(a=c\) and zero otherwise. Multiplication by \(q(q+1)\) gives the maximum total fiber. This covers the smallest field \(q=2\).

## Verification

Extract `verify_projector_triple_traces.py` and run `python3 verify_projector_triple_traces.py` using Python 3 standard library. The checker independently constructs every rank-one idempotent as a matrix, multiplies all ordered pairs \((F,G)\) with \(E=\operatorname{diag}(1,0)\) fixed, and verifies the exact value of every fiber against the formula. It covers fields of orders \(2,3,4,5,7,8,9,11\), including extension fields \(\mathbb F_4,\mathbb F_8,\mathbb F_9\), and checks the total number \(q^2(q+1)^2\) of ordered pairs. The executable output is included as `verify_projector_triple_traces.out` and ends in `PROJECTOR_TRIPLE_TRACE_PASS`. Separately, support cardinalities and the maxima were checked independently for the same field orders. Finite experiments validate test cases; the proof above establishes all finite fields.

## Relationship to prior work

De Seguins Pazzis [1] treats **linear combinations of two idempotents**, giving existence and matrix-similarity conditions rather than joint prescribed trace fibers of three projectors. Rowen--Segev [2] establish the algebra structure **generated by two idempotents**; their central two-generator element and normal forms are consistent with the pairwise trace parameter but do not count the three pairwise correlations.

The published field-of-definition and conjugacy census for pairs [3] determines the nondegenerate orbit for one scalar \(\operatorname{tr}(EF)\), but its statement contains no prescribed joint constraints on an added third projector. The all-length product-fiber theorem [4] fixes **one total product matrix**, not all three two-factor trace values simultaneously; the latter joint law is not obtained from that marginal product distribution. The rank-one-idempotent generation criterion [5] concerns generation by \(n\) rank-one projectors in \(M_n\) and counts generating triples in dimension three, rather than pairwise trace fibers in dimension two.

The originality claim is restricted to the complete three-coordinate prescribed fiber spectrum and its sharp support and maximum. It does not claim novelty for Cayley--Hamilton normalization, quadratic character sums, simultaneous conjugacy of individual projectors, or any existing two-idempotent structure theorem.

## Limitations

The result concerns exactly three ordered rank-one idempotents in a two-dimensional full matrix algebra. It does not classify simultaneous conjugacy orbits of triples, since pairwise traces alone may not separate orbits; it does not count three-projector triples in higher dimension. Previously unindexed invariant-theoretic or conic-incidence formulas could imply the present expression; literature searching and semantic matching cannot certify absolute priority. No independent external mathematical audit has occurred.

## References

1. C. de Seguins Pazzis, *On linear combinations of two idempotent matrices over an arbitrary field*, arXiv:0907.4436v1 (first posted 2009-07-25), https://arxiv.org/abs/0907.4436; especially introduction and Sections 3--7.
2. L. Rowen and Y. Segev, *Associative and Jordan algebras generated by two idempotents*, arXiv:1609.04899v1 (first posted 2016-09-16), https://arxiv.org/abs/1609.04899; especially Theorem 1.1 and Section 2.
3. *Frobenius-degree and orbit laws for pairs of idempotents in finite matrix rings*, published 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-frobenius-degree-and-orbit-laws-for-pairs-of-idempotents-in-fini--158f1d5d0025.
4. *Exact all-arity product fibers of rank-one idempotents over finite fields*, published 2026-10-12, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-all-arity-product-fibers-of-rank-one-idempotents-over-fini--dfb5f1d17166.
5. *Rank-one idempotent generation: directed reachability and an exact three-dimensional count*, published 2026-10-12, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-rank-one-idempotent-generation-directed-reachability-and-an-exac--1f309735163a.
