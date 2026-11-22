# Square-one automorphisms of cyclic radical-square-zero Nakayama algebras: necklace classes and a parity split

## Finding
Let \(k=\mathbb F_q\) have odd cardinality, let \(n\ge3\), and let \(A_n=kQ_n/J^2\), where \(Q_n\) is the consistently oriented cycle with \(n\) vertices and \(J\) is its arrow ideal. Write \(\mathcal T_n(q)=\{\sigma\in\operatorname{Aut}_k(A_n):\sigma^2=1\}\), **including the identity**. Then
\[
 |\mathcal T_n(q)|=(q+1)^n+\mathbf1_{2\mid n}\,[q(q-1)]^{n/2}.
\]
The complete fixed-dimension enumerator is
\[
 \sum_{\sigma\in\mathcal T_n(q)}z^{\dim_k A_n^\sigma}
 =z^n(z+q)^n+\mathbf1_{2\mid n}\,[q(q-1)]^{n/2}z^n.
\]
There are precisely
\[
 \frac1n\sum_{d\mid n}\varphi(d)\,2^{n/d}+\mathbf1_{2\mid n}
\]
conjugacy classes within \(\mathcal T_n(q)\). The classes with trivial vertex permutation are indexed by **binary necklaces** on \(n\) arrow positions: a necklace with \(r\) negative signs and rotational period \(p\) gives one class of size \(p q^r\), with fixed algebra the radical-square-zero path algebra obtained from the directed cycle by retaining precisely its positive-sign arrows. When \(n=2m\), there is one further class of size \([q(q-1)]^m\); its elements permute vertices by the half-turn and have fixed algebra isomorphic to \(A_m\). The all-negative-sign class has fixed algebra \(k^n\) and size \(q^n\).

For a uniformly sampled element of \(\mathcal T_n(q)\) and fixed \(n\), the following **fixed-algebra dichotomy** holds as odd prime powers \(q\) grow. When \(n\) is odd, the fixed algebra is \(k^n\) with probability tending to one. When \(n\) is even, the probability of the semisimple fixed algebra \(k^n\) tends to \(1/2\), the probability of the nonsemisimple cyclic fixed algebra \(A_{n/2}\) tends to \(1/2\), and all other types have vanishing total probability. This is a statement about algebra isomorphism types, not only fixed-space dimension. For exact order-two elements rather than square-one elements, subtract the identity from the count and the top fixed-dimension coefficient.

## Assumptions and scope
The field is \(k=\mathbb F_q\) with \(q\) odd. The cycle length is any integer \(n\ge3\); this restriction avoids the parallel-arrow convention that arises for a two-vertex cycle in some treatments. Indices are in \(\mathbb Z/n\mathbb Z\). The algebra has basis \(e_i,a_i\), and its only nonzero basis products are \(e_i^2=e_i\), \(e_ia_i=a_i\), and \(a_ie_{i+1}=a_i\). Thus \(A_n/J\cong k^n\), \(J=\bigoplus_i k a_i\), \(J^2=0\), and \(\dim A_n=2n\). Here \(A_n^\sigma=\{a:\sigma(a)=a\}\), and all automorphisms are unital \(k\)-algebra automorphisms. The symbol \(\mathbf1_{2\mid n}\) is one if \(n\) is even and zero otherwise. A sign necklace means a binary string up to cyclic rotation, with negative entries recorded at the arrows that an automorphism negates.

## Proof
**1. Full automorphism group.** An automorphism preserves \(J\) and permutes the primitive central idempotents of \(A_n/J\cong k^n\). The one-dimensional bimodule pieces \(e_iJe_j\) are nonzero precisely when \(j=i+1\). Hence its vertex permutation preserves the oriented cycle and is necessarily a rotation \(\rho^t\), \(0\le t<n\). The images of the primitive idempotents are an ordered family of pairwise orthogonal lifts of the standard idempotents. Since \(J^2=0\) and there are no loops, every such family is uniquely \((1+x)e_{i+t}(1-x)\) for one \(x\in J\). After choosing this lift, every arrow is mapped to a nonzero scalar multiple of its rotated arrow. Consequently every automorphism is uniquely \(\operatorname{Ad}(1+x)h\) with
\[
 x\in J,\qquad h(e_i)=e_{i+t},\qquad h(a_i)=\lambda_i a_{i+t},\quad\lambda_i\in k^\times.
\]
Conjugation by \(1+x\) acts trivially on \(J\). Multiplying two such conjugations adds their \(J\)-parameters. It follows that
\[
 \operatorname{Aut}_k(A_n)\cong (J,+)\rtimes\bigl((k^\times)^n\rtimes C_n\bigr),\qquad
 |\operatorname{Aut}_k(A_n)|=n q^n(q-1)^n.
\]
This factorization is also obtained directly by checking idempotents and arrows against the defining relations; it requires no choice of algebraic closure.

**2. Square-one condition.** Denote by \(h\) an element of the diagonal-scaling-by-rotation subgroup. Since \(\operatorname{Ad}(1+x)\) is the additive normal subgroup,
\[
 (\operatorname{Ad}(1+x)h)^2=1\quad\Longleftrightarrow\quad h^2=1\text{ and }(1+h)x=0.
\]
The rotation in \(h\) must be either the identity or, when \(n=2m\), the unique half-turn. For identity rotation, each \(\lambda_i\) is \(+1\) or \(-1\). If \(r\) signs are negative, the \((-1)\)-eigenspace on \(J\) has dimension \(r\), so precisely \(q^r\) values of \(x\) work. Summing over the \(\binom nr\) sign configurations gives \((q+1)^n\). For half-turn rotation, \(\lambda_i\lambda_{i+m}=1\) for every \(i\), giving \((q-1)^m\) diagonal choices; on each paired arrow space the square-one operator has one negative eigenline, giving \(q^m\) choices of \(x\). There are no other square-one cases. This proves the cardinality formula.

**3. Class and centralizer classification.** Since \(q\) is odd, the image of \(1-h\) on \(J\) equals the \((-1)\)-eigenspace of any square-one \(h\): if \(hx=-x\), then \(x=(1-h)(x/2)\). Therefore conjugation by the normal additive group removes every allowable \(x\). In the identity-rotation case, diagonal conjugations preserve the sign pattern and rotations act by cyclic shifts. Its classes are exactly binary necklaces. A particular sign pattern having \(r\) negative entries contributes \(q^r\) conjugates, and its orbit under rotations has length \(p\), hence class size \(p q^r\). Burnside's count of binary necklaces is \(n^{-1}\sum_{d\mid n}\varphi(d)2^{n/d}\). For a half-turn, conjugation by a diagonal scaling normalizes all \(\lambda_i\) to one (the equations \(\lambda_i\lambda_{i+m}=1\) are exactly the consistency equations). Thus every half-turn square-one automorphism is conjugate to \(\rho^m\), giving one class, of the entire half-turn size \([q(q-1)]^m\). This establishes every claimed class and class size.

**4. Fixed spaces and fixed subalgebras.** Conjugation preserves fixed-space dimensions and fixed-algebra isomorphism types, so use the normalized representatives. An identity-rotation representative fixes all \(e_i\) and exactly the \(n-r\) positive-sign arrows, yielding dimension \(2n-r\). Its fixed algebra is exactly the span of those idempotents and arrows with the inherited radical-square-zero multiplication. A normalized half-turn \(\rho^m\) has invariant basis
\[
 E_i=e_i+e_{i+m},\qquad B_i=a_i+a_{i+m},\qquad 0\le i<m.
\]
These elements satisfy \(E_i^2=E_i\), \(E_iB_i=B_i\), \(B_iE_{i+1}=B_i\) (indices modulo \(m\)), and all other basis products vanish. Hence the fixed algebra is \(A_m\), of dimension \(2m=n\). Combining these dimensions with the counts in step 2 proves the fixed-space polynomial. When all signs are negative, the fixed algebra is precisely the semisimple quotient copy \(k^n\).

**5. Parity split.** For odd \(n\), the total is \((q+1)^n\), and the all-negative class weighs \(q^n\), so its probability tends to one. For even \(n=2m\), the total is \((q+1)^n+[q(q-1)]^m=2q^n+O_n(q^{n-1})\). The all-negative class contributes \(q^n\), while the half-turn class contributes \([q(q-1)]^m=q^n+O_n(q^{n-1})\). All remaining classes together contribute \(O_n(q^{n-1})\). Since \(k^n\) is semisimple and \(A_m\) has nonzero radical, these two limiting fixed-algebra types are not isomorphic. This proves the dichotomy.

## Verification
The included `checker.py` constructs every algebra automorphism as an actual \(2n\times2n\) matrix over the prime fields \(\mathbb F_3\) and \(\mathbb F_5\), computes its square and fixed-space dimension independently of the counting formula, and compares the resulting polynomials. The configurations \((n,q)=(3,3),(4,3),(3,5)\) yield respectively \(64,292,216\) square-one automorphisms. At \((4,3)\), it independently generates conjugacy orbits using radical translations, diagonal scalings and rotation and obtains sorted class sizes \(1,12,18,36,36,81,108\), totaling \(292\). It verifies the semidirect-product multiplication against matrix composition on sampled representative pairs. The expected output is preserved in `checker_output.txt`. All numerical tests are finite checks; the all-\(n\), all-odd-field assertion follows from the proof above, not from enumeration.

## Relationship to prior work
Xu, Han, and Jiang, *Hochschild cohomology of truncated quiver algebras* (2005), supplies the broader truncated-basic-cycle setting but concerns cohomological invariants rather than algebra automorphism conjugacy or fixed rings. Chen, *The singularity category of an algebra with radical square zero* (2011), treats general radical-square-zero algebras and the special role of oriented-cycle quivers in homological structure, not the automorphism involution or fixed-subalgebra census. Zhang, *\(\tau\)-rigid modules for algebras with radical square zero* (2012), describes module-theoretic properties of radical-square-zero Nakayama algebras, again not this automorphism question. The published study *The endomorphism rank spectrum of radical-square-zero cyclic Nakayama algebras* gives a full parameterization and total number of algebra endomorphisms, in particular \(nq^n(q-1)^n\) automorphisms. The automorphism group structure in step 1 is therefore not claimed independently; the contribution here is the complete square-one conjugacy and fixed-algebra census, especially the half-turn fixed algebra and its even-cycle asymptotic weight. The published result *Complete power-map fibers in radical-square-zero quiver unit groups* concerns the unit group, not the algebra automorphism group, and hence does not imply these conjugacy and fixed-algebra assertions. General elementary facts about signed necklaces and split semidirect products are likewise used, not claimed as new. A stronger earlier classification of fixed subalgebras for all finite-order quiver-algebra automorphisms, if found, could subsume this statement.

## Limitations
The characteristic-two case is not covered: square-one operators need not split into \(\pm1\)-eigenspaces and the normal-radical conjugacy argument fails. Only one-arrow-per-edge directed cycles of length at least three and radical square zero are considered; no assertion is made for longer Loewy length or arbitrary quivers. The formula counts square-one automorphisms including the identity; exact order-two counts are smaller by one. Originality is assessed against the named searched literature, not claimed as an exhaustive historical uniqueness certificate. Numerical verification is restricted to the stated prime-field instances.

## References
- Xu, Han, and Jiang, *Hochschild cohomology of truncated quiver algebras*, arXiv:math/0509202v1, first public 2005-09-09, https://arxiv.org/abs/math/0509202.
- X.-W. Chen, *The singularity category of an algebra with radical square zero*, arXiv:1104.4006v1, first public 2011-04-20, https://arxiv.org/abs/1104.4006.
- X. Zhang, *\(\tau\)-rigid modules for algebras with radical square zero*, arXiv:1211.5622v1, first public 2012-11-23, https://arxiv.org/abs/1211.5622.
- *The endomorphism rank spectrum of radical-square-zero cyclic Nakayama algebras*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-the-endomorphism-rank-spectrum-of-radical-square-zero-cyclic-nak--dfd7ae4c0025.
- *Complete power-map fibers in radical-square-zero quiver unit groups*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-complete-power-map-fibers-in-radical-square-zero-quiver-unit-gro--1c150d6b326e.
