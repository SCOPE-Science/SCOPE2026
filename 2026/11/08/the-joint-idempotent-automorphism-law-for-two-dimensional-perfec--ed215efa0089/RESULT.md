# The joint idempotent–automorphism law for two-dimensional perfect evolution algebras over finite fields

## Finding

Let \(q=p^m\) be any prime power. Choose uniformly a matrix \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) in \(\operatorname{GL}_2(\mathbb F_q)\), and form the evolution algebra \(E_A\) with \(e_1^2=ae_1+be_2\), \(e_2^2=ce_1+de_2\), and \(e_1e_2=0\). Let \(K(A)\) be its number of **nonzero** \(\mathbb F_q\)-rational idempotents; let \(G(A)=|\operatorname{Aut}_{\mathbb F_q}(E_A)|\), counting ordinary field-rational linear automorphisms (not group-scheme length).

Define \(T=q(q-1)^2(q+1)\), \(s=(q-1)^2\), \(g=\gcd(3,q-1)\), \(r=1\) if \(p=2\), otherwise \(r=2\), and \(H=0\) if \(p=2\), otherwise \(H=(q-1)^3\). Set

\[
R=\begin{cases}
q/2-\mathbf 1_{2\mid m},&p=2,\\
(q-1)/2-\mathbf 1_{q\equiv1\pmod4}-\mathbf 1_{g=3},&p\ne2.
\end{cases}
\]

Here indicator symbols are \(0\) or \(1\). For \(j\in\{0,1,2,3\}\), put \(M_0=T/3\), \(M_1=(T-H)/2\), \(M_2=H\), \(M_3=(T-3H)/6\). Then the **complete joint distribution**, as counts of labeled invertible structure matrices, is

| \(G(A)\) | \(K=0\) | \(K=1\) | \(K=2\) | \(K=3\) |
|---|---:|---:|---:|---:|
| \(1\) | \(M_0-2s\mathbf 1_{g=3}/3\) | \(M_1-s(q-r-R+\mathbf 1_{g=1})\) | \(M_2\) | \(M_3-sR-s\mathbf 1_{g=3}/3\) |
| \(2\) | \(0\) | \(s(q-r-R+\mathbf 1_{g=1})\) | \(0\) | \(sR\) |
| \(3\) | \(2s\mathbf 1_{g=3}/3\) | \(0\) | \(0\) | \(0\) |
| \(6\) | \(0\) | \(0\) | \(0\) | \(s\mathbf 1_{g=3}/3\) |

The only possible abstract automorphism groups are the trivial group, \(C_2\), \(C_3\), and \(S_3\). In particular, a nontrivial order-three automorphism group forces **zero** nonzero rational idempotents, whereas \(S_3\) forces **three**. Nontrivial order-two automorphism groups force either one or three, never zero or two. The order-two split has an additional quadratic-character dependence when \(p\ne2\) and an absolute-trace dependence when \(p=2\).

## Assumptions and scope

All assertions hold for every finite field \(\mathbb F_{p^m}\), including characteristics two and three. The sample space is the set of \(T\) invertible \(2\times2\) matrices in a fixed natural basis, with uniform measure; isomorphic algebras may appear more than once. Every automorphism is \(\mathbb F_q\)-linear. The group orders \(1,2,3,6\) specify respectively \(1,C_2,C_3,S_3\). Zero is excluded from \(K\). The formulas do not assert a law for all (possibly singular) structure matrices, nor for higher dimensions.

## Proof

**Step 1: the idempotent marginal distribution, independently derived.** The quadratic map on \(\mathbb F_q^2\) governing idempotents is \(f_A(x,y)=(ax^2+cy^2,bx^2+dy^2)\). Each rational fixed point of the induced projective map \([x:y]\mapsto[f_A(x,y)]\) lifts to exactly one nonzero idempotent by scaling, and conversely: if \(f_A(v)=\lambda v\) with \(\lambda\ne0\), then \(\lambda^{-1}v\) is the unique nonzero idempotent on that line. The fixed-point equation is a nonzero homogeneous cubic (nonzero because \(A\) is invertible), so \(K\le3\).

Uniform \(A\) induces a uniform element of \(\operatorname{PGL}_2(\mathbb F_q)\) applied after projective squaring \(s:[x:y]\mapsto[x^2:y^2]\). Since \(\operatorname{PGL}_2\) acts sharply three-transitively on \(\mathbb P^1(\mathbb F_q)\), the first three factorial moments of the fixed-point count are determined by the numbers of ordered distinct inputs with distinct squared images. The first factorial moment is \(\mathbb E K=1\). In characteristic two, squaring is bijective, so \(\mathbb E(K)_2=\mathbb E(K)_3=1\). In odd characteristic, among the \((q+1)q\) ordered distinct pairs, exactly \(q-1\) have equal squared images, namely distinct \(t,-t\) in \(\mathbb F_q^\times\). Among ordered distinct triples, exactly \(3(q-1)^2\) contain an opposite pair, and no triple contains two such pairs. Hence, with \(\alpha=(q-1)/(q(q+1))\) in odd characteristic and \(\alpha=0\) in even characteristic,

\[\mathbb E(K)_1=1,\qquad\mathbb E(K)_2=1-\alpha,\qquad\mathbb E(K)_3=1-3\alpha.\]

Solving for the four masses on \(\{0,1,2,3\}\) gives counts \(M_0,M_1,M_2,M_3\) above because \(T\alpha=H\). This derivation does not assume an earlier counting theorem.

**Step 2: all automorphisms are monomial.** Since \(A\) is invertible, \(e_1^2,e_2^2\) are linearly independent. If an automorphism sends \(e_i\) to \(\sum_j u_{ji}e_j\), preservation of \(e_1e_2=0\) implies \(u_{11}u_{12}=u_{21}u_{22}=0\). Invertibility leaves precisely a diagonal or a swapping monomial matrix.

For a diagonal automorphism \(e_1\mapsto xe_1\), \(e_2\mapsto ye_2\), \(x,y\ne0\), multiplication preservation is

\[a(x^2-x)=0,\quad b(x^2-y)=0,\quad c(y^2-x)=0,\quad d(y^2-y)=0.\]

The only case with a nonidentity solution is \(a=d=0\), \(bc\ne0\), where \(y=x^2\) and \(x^3=1\), giving exactly \(g\) diagonal automorphisms.

For a swapping automorphism \(e_1\mapsto ue_2\), \(e_2\mapsto ve_1\), the equations are

\[cu^2=bv,\quad du^2=au,\quad av^2=dv,\quad bv^2=cu.\]

If exactly one of \(a,d\) vanishes, there is no solution. If \(ad\ne0\), there is precisely one solution \(u=a/d\), \(v=d/a\) if and only if \(ca^3=bd^3\). It has order two, and there are no other nonidentity automorphisms. If \(a=d=0\), there are \(g\) swapping automorphisms precisely when \(b/c\) is a cube; then the full group has order \(2g\), equal to \(C_2\) for \(g=1\) and \(S_3\) for \(g=3\). Otherwise, if \(g=3\), the full group is \(C_3\).

**Step 3: zero-diagonal block.** For \(a=d=0\), \(bc\ne0\), the idempotent equations give \(x^3=(cb^2)^{-1}\) for every nonzero idempotent, and its other coordinate is uniquely determined. Since \(cb^2=c^3(b/c)^2\), when \(g=3\) the cube-solvability condition is exactly that \(b/c\) be a cube. Thus precisely \(s/3\) matrices have \((G,K)=(6,3)\) and \(2s/3\) have \((G,K)=(3,0)\). When \(g=1\), every one of the \(s\) matrices has \((G,K)=(2,1)\).

**Step 4: swapping block and the arithmetic correction.** In the \(ad\ne0\) swapping case, write \(z=bd/a^2=ca/d^2\). Invertibility is equivalent to \(z^2\ne1\). For each permissible \(z\) there are \(s\) choices of \(a,d\), all isomorphic by diagonal basis rescaling to

\[e_1^2=e_1+ze_2,\qquad e_2^2=ze_1+e_2.\]

There is always one diagonal-coordinate idempotent, with \(x=y=(1+z)^{-1}\). Any other nonzero idempotents occur in a swapped pair. For \(p\ne2\), subtracting the two idempotent equations and assuming \(x\ne y\) yields

\[x+y=(1-z)^{-1},\qquad(x-y)^2=\frac{1-3z}{(1-z)^2(1+z)}.\]

The pair exists precisely when \(t=(1-3z)/(1+z)\) is a **nonzero square**. As \(z\) ranges over \(\mathbb F_q\setminus\{1,-1\}\), this Möbius map ranges bijectively over \(\mathbb F_q\setminus\{-1,-3\}\). Thus the number of \(z\)'s producing three idempotents is \((q-1)/2-\mathbf1_{-1\text{ square}}-\mathbf1_{-3\text{ nonzero square}}\). The first indicator is \(\mathbf1_{q\equiv1\pmod4}\); the second is \(\mathbf1_{g=3}\), since in odd characteristic a nonzero square root of \(-3\) exists exactly when there is a primitive cube root of unity. This is \(R\) as stated, including characteristic three where \(-3=0\).

If \(p=2\), there is again one diagonal-coordinate idempotent. Writing \(S=(1+z)^{-1}\) for the sum of coordinates of a possible off-diagonal pair and \(t=(1+z)x\), the other idempotent equation reduces to

\[t^2+t=\frac{z}{1+z}.\]

It has two roots exactly when \(\operatorname{Tr}_{\mathbb F_q/\mathbb F_2}(z/(1+z))=0\). The rational transformation \(z\mapsto z/(1+z)\) bijects \(\mathbb F_q\setminus\{1\}\) with itself. Among the \(q/2\) trace-zero elements, the excluded element \(1\) has trace zero exactly when \(m\) is even. Thus the number of \(z\)'s producing three idempotents is \(R=q/2-\mathbf1_{2\mid m}\). The other \(q-r-R\) values produce one idempotent. Multiplication by \(s\) gives the complete \(G=2\) swapping row.

**Step 5: completion.** All nontrivial automorphisms arise in Steps 3–4. Subtract their joint counts from the independently proved marginal counts \(M_j\) in Step 1; this yields the \(G=1\) row. The four rows sum to \(T\), proving the table for every prime power.

## Verification

The standalone `CHECK.py` implements \(\mathbb F_q\) arithmetic for both prime fields and extension fields. For \(q=2,3,4,5,7,8,9,11,13\), it enumerates every invertible structure matrix, every nonzero idempotent by direct evaluation, and all field-rational diagonal and swapping monomial automorphisms; it then compares the complete two-variable histogram with the displayed formula. Additional arithmetic integrality and total-count checks cover selected larger prime powers. The independent finite checks finish with `VERIFY_OK`; see `CHECK_OUTPUT.txt`. These examples are consistency tests, not an infinite proof.

## Relationship to prior work

Kaygorodov–Martín González–Viruel (2026) explicitly ask for random-evolution-algebra automorphism rigidity and idempotent statistics; their finite-field idempotent statement concerns a first moment. Wei–Zou (2023) count *total isomorphism orbits* of perfect evolution algebras over finite fields, and Cabrera Casado and collaborators (2024) determine automorphism group schemes of individual two-dimensional types. Those results do not explicitly give the above joint distribution of rational idempotent counts and ordinary automorphism-group orders. Earlier exact **marginal** distributions for each invariant separately do not mathematically determine their joint law. The distinctive content here is the correlation and its arithmetic stratification, notably the cubic obstruction, quadratic-character exclusions, and absolute-trace correction. No claim of priority for monomial rigidity, the individual group types, or the marginal distributions is made.

## Limitations

The theorem counts labeled invertible natural-basis matrices rather than giving a uniform measure on isomorphism classes. Group orders refer to \(\mathbb F_q\)-points and not group-scheme lengths; characteristic two and three may have nonreduced group schemes. The theorem concerns dimension two only. While relevant available sources were compared, complete historical priority cannot be certified, particularly if a broader algebra-classification result implicitly contains the joint law.

## References

- I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first public 2026-10-15), especially Question 22 and the finite-field idempotent discussion; https://arxiv.org/abs/2610.22248.
- Y. Wei, Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368v1 (2023), especially Section 4; https://arxiv.org/abs/2310.12368.
- Y. Cabrera Casado et al., *Hopf algebras and associative representations of two-dimensional evolution algebras*, arXiv:2407.15769v2 (2024), especially Section 2; https://arxiv.org/abs/2407.15769.
