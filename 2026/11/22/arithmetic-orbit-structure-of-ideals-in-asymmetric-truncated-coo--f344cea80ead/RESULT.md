# Arithmetic orbit structure of ideals in asymmetric truncated coordinate nodes

## Finding
Let \(k=\mathbb F_q\) be any finite field, and let \(3\le m<n\). Set
\[
 A_{m,n}=k[x,y]/(xy,x^m,y^n),\qquad \mathfrak m=(x,y).
\]
Under the full group \(\operatorname{Aut}_k(A_{m,n})\), every ideal orbit belongs to exactly one of the following families.

* Exactly \(mn-1\) singleton orbits consist of the whole ring and the monomial ideals \(I_{a,b}=(x^a,y^b)\), \(1\le a\le m\), \(1\le b\le n\), excluding \(I_{1,n}=(x)\) and \(I_{m,1}=(y)\).
* Exactly two exceptional orbits, each of size \(q\), are \(\{(x)\}\cup\{J_{1,n-1,c}:c\in k^\times\}\) and \(\{(y)\}\cup\{J_{m-1,1,c}:c\in k^\times\}\), where
  \[
   J_{u,v,c}=(x^{u+1},y^{v+1},x^u+c y^v),\quad 1\le u<m,\quad 1\le v<n,\quad c\in k^\times.
  \]
* For each of the remaining exponent pairs \((u,v)\), the \(q-1\) distinct ideals \(J_{u,v,c}\) form exactly \(g_{u,v}=\gcd(u,v,q-1)\) orbits, all of size \((q-1)/g_{u,v}\).

Consequently, writing \(\mathcal E=\{(1,n-1),(m-1,1)\}\), the orbit-size polynomial (coefficient = number of orbits) is
\[
 \mathcal O_{m,n,q}(Z)=(mn-1)Z+2Z^q+
 \sum_{\substack{1\le u<m,\ 1\le v<n\\(u,v)\notin\mathcal E}}
   g_{u,v}Z^{(q-1)/g_{u,v}}.
\]
The exact number of ideals fixed by every automorphism (characteristic ideals in the sense of \(k\)-algebra automorphism invariance) is
\[
 H_{m,n}(q)=mn-1+(q-1)
  \left\lfloor\frac{m-1}{q-1}\right\rfloor
  \left\lfloor\frac{n-1}{q-1}\right\rfloor-2\mathbf 1_{q=2}.
\]
**Binary four-exception rigidity:** over \(\mathbb F_2\), precisely four ideals fail to be characteristic, independent of \(m,n\): the two principal branch ideals \((x),(y)\) and \(J_{1,n-1,1},J_{m-1,1,1}\). The other \(2mn-m-n-2\) ideals are characteristic. For any fixed \(q\), as both \(m,n\to\infty\), the characteristic-ideal proportion tends to \(1/(q-1)\), including the limit one over \(\mathbb F_2\).

The exact characteristic-ideal dimension polynomial, counting the whole ring, is
\[
\begin{aligned}
 Z^{\mathrm{char}}_{m,n,q}(T)={}&T^{m+n-1}
 +\left(\sum_{i=0}^{m-1}T^i\right)\left(\sum_{j=0}^{n-1}T^j\right)
 -(T^{m-1}+T^{n-1})\\
 &+(q-1)\sum_{a=1}^{\lfloor(m-1)/(q-1)\rfloor}
 \sum_{b=1}^{\lfloor(n-1)/(q-1)\rfloor}
 T^{m+n-1-(q-1)(a+b)}
 -\mathbf 1_{q=2}(T^{m-1}+T^{n-1}).
\end{aligned}
\]

## Assumptions and scope
All automorphisms are unital and \(k\)-linear (fix the finite coefficient field pointwise), and ideals mean all two-sided ideals (equivalently, ideals, since the ring is commutative). The asymmetry \(m<n\) and both lengths at least three rule out branch swaps and linear mixing from square-zero branches. The polynomial \(\mathcal O\) records orbit *sizes*, not algebraic-geometric dimensions. For any subscript exceeding the branch length, powers vanish in the quotient, e.g. \(x^m=0\).

## Proof
**1. Exhaustion of ideals.** Every proper ideal is inside \(\mathfrak m\). Its intersections with \(xk[x]/(x^m)\) and \(yk[y]/(y^n)\) are uniquely the two tails \((x^a)\) and \((y^b)\). Multiplication by \(x\) and \(y\) forces any element modulo these tails to lie in the at-most-two-dimensional span of the preceding boundary monomials \(x^{a-1}\) (when \(a\ge2\)) and \(y^{b-1}\) (when \(b\ge2\)). A nonzero boundary subspace cannot contain a coordinate axis, by the definition of the intersections; it is therefore exactly one diagonal line if both coordinates exist. Accordingly all proper ideals are the \(mn\) distinct monomial ideals \(I_{a,b}\) and the \((q-1)(m-1)(n-1)\) distinct mixed ideals \(J_{u,v,c}\). This establishes their uniqueness independently of any parameter count.

**2. Exhaustion of automorphism actions.** Each automorphism necessarily has the form
\[
 \phi(x)=f(x)+\alpha y^{n-1},\qquad
 \phi(y)=g(y)+\beta x^{m-1},
\]
with \(f(x)=a x+\sum_{j=2}^{m-1}a_jx^j\), \(g(y)=b y+\sum_{j=2}^{n-1}b_jy^j\), and \(a,b\in k^\times\); conversely every such assignment is invertible. For completeness, relations \(xy=0\) in the quotient force the degree-one action to be monomial because squares are nonzero and linearly independent. A transposition of branches would violate the unequal nilpotency lengths. All off-branch terms must be in the opposite branch socle, since they must annihilate the opposite generator's nonzero linear part. The unipotent within-branch jets are arbitrary by direct substitution; invertibility follows from the invertible cotangent linear part.

**3. Monomial ideals and two exceptional orbits.** Every \(I_{a,b}\) is preserved by the jets and scalings. The off-branch term in \(\phi(x)\) can escape \(I_{a,b}\) exactly when \((a,b)=(1,n)\); similarly the off-branch term in \(\phi(y)\) escapes exactly when \((a,b)=(m,1)\). On the corresponding boundary lines, the same socle shears act by arbitrary translations of the coefficient \(c\) through all \(k\), including \(0\), which represents the monomial endpoint. Thus each exceptional orbit contains \(q\) ideals.

**4. Remaining mixed-ideal orbits.** When \((u,v)\notin\mathcal E\), every higher-order jet contribution to \(x^u+c y^v\) belongs to \((x^{u+1},y^{v+1})\). Neither socle shear survives in the quotient, except in the excluded pairs. Therefore the only action on its slope is
\[
 c\longmapsto (b^v/a^u)c,\qquad a,b\in k^\times.
\]
The coefficient group is cyclic of order \(q-1\). The subgroup generated by its \(u\)-th and \(v\)-th powers has order \((q-1)/\gcd(u,v,q-1)\), establishing exactly \(g_{u,v}\) orbits of the asserted common size. Distinct exponent pairs cannot mix because the pure-branch intersection exponents are preserved by the automorphism normal form. Summing these exhaustive cases proves \(\mathcal O\).

**5. Fixed ideals, ranks, and limits.** Each nonexceptional mixed slope is fixed by every torus scaling iff \(q-1\) divides both \(u\) and \(v\). For \(q>2\), such a pair is never exceptional; for \(q=2\), precisely the two exceptional pairs must be subtracted. This gives \(H_{m,n}(q)\). Dimensions of monomial ideals are \(m+n-a-b\); dimensions of mixed ideals are \(m+n-u-v-1\), since the mixed boundary contributes one extra dimension beyond the two strict tails. Summing these dimensions gives the stated polynomial. The total number of all ideals is \(1+mn+(q-1)(m-1)(n-1)\), so the ratio has limit \(1/(q-1)\) when both lengths diverge. For \(q=2\), this total exceeds the fixed count by exactly four for every permitted \(m,n\).

## Verification
The accompanying independent Python 3 standard-library checkers exhaustively enumerate all reduced-row-echelon subspaces of the radical over six prime-field examples, test ideal invariance under multiplication by both generators, and compute the orbits under explicit scaling, within-branch and socle-shear automorphisms. They agree with the orbit-size polynomial, fixed-ideal total, and full characteristic-ideal dimension polynomial. At \((m,n,q)=(3,4,5)\), for example, there are \(37\) ideals partitioned into \(11\) singleton orbits, two of size two, three of size four, and two of size five. Over \(\mathbb F_2\), all three checked pairs have exactly two size-two orbits and every other ideal fixed. The full check transcript is in `verification.log`. Finite enumerations supplement but do not substitute for the arbitrary-field and all-length proof above.

## Relationship to prior work
The full ideal normal form for finite truncated coordinate fibre products, including the two-branch case, was already published in *Ideal-dimension distributions and radical duality in multi-branch Artinian fibre products* (2026); the present result does **not** claim that underlying ideal classification. Likewise *Automorphisms of heterogeneous truncated coordinate-cross algebras over finite fields* (2026) already proves the full automorphism normal form and size; that input is credited, not reasserted as a novelty contribution. The specific new conclusion is their combined *action* on all ideals: the complete finite-field orbit partition, arithmetic slope-orbit gcd formula, four-exception rigidity, and fixed-ideal dimension distribution. Neither inspected prior theorem states these orbit counts. The earlier 2024 paper by Díaz, Liendo, Manzano-Flores and Regeta studies automorphisms of zero-dimensional monomial algebras in characteristic zero; the current calculation uses finite-field rational automorphism actions and characterizes finite-field fixed ideals. The 2024 Díaz–Lucchini Arteche reconstruction result concerns recovering a monomial ring from an automorphism group, not its ideal orbits. These earlier classifications make the new proof short and pose a genuine residual risk that this action computation could be regarded as an implicit corollary rather than an independently prioritized result.

## Limitations
No claim extends to equal branch lengths, nilpotency-two branches, arbitrary monomial ideals, semilinear field automorphisms, nonreduced ideal schemes, or classification of automorphism-orbit *stabilizer groups*. The computational verification covers small prime fields, while the proof covers every finite field. The priority comparison is not exhaustive; a full automorphism action on the ideal lattice in unpublished or inaccessible literature could subsume the orbit formula.

## References
1. R. Díaz, Á. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197, first posted 2024-08-05. https://arxiv.org/abs/2408.02197.
2. R. Díaz, G. Lucchini Arteche, *Finite monomial algebras are determined by their automorphism group*, arXiv:2409.15081, first posted 2024-09-23. https://arxiv.org/abs/2409.15081.
3. *Automorphisms of heterogeneous truncated coordinate-cross algebras over finite fields*, published result (2026): https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-automorphisms-of-heterogeneous-truncated-coordinate-cross-algebr--f45a4cb0bac6.
4. *Ideal-dimension distributions and radical duality in multi-branch Artinian fibre products*, published result (2026): https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-ideal-dimension-distributions-and-radical-duality-in-multi-branc--3c121a92d2ba.
5. *Endomorphism varieties of truncated two-branch Artinian nodes*, published result (2026): https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-endomorphism-varieties-of-truncated-two-branch-artinian-nodes--e79ee988b8ee.
