# Three prescribed-commutator fibers in characteristic-two split octonion algebras

## Finding

For every \(q=2^e\), \(e\ge1\), let \(\mathcal O_q\) be the split Cayley (octonion) algebra over \(\mathbb F_q\) with the Zorn product defined below. The number \(N_q(z)\) of **ordered**, labeled solutions to \(xy-yx=z\) depends on only three trace-zero target types:

\[
N_q(z)=\begin{cases}
0,&\operatorname{tr}(z)\ne0,\\
q^{13}+q^{10}-q^7,&z=0,\\
q^{13}-q^7,&z\in\mathbb F_q^\times 1,\\
(q^2-1)q^7,&\operatorname{tr}(z)=0\text{ and }z\notin\mathbb F_q1.
\end{cases}
\]

Every trace-zero value is a commutator. The \(q^7\) trace-zero targets split into one zero, \(q-1\) nonzero scalar targets, and \(q^7-q\) nonscalar targets. In particular **all nonscalar trace-zero commutators have identical fiber size**, irrespective of their octonion norm. The commuting probability is \(q^{-3}+q^{-6}-q^{-9}\). The zero-fiber expression follows independently from earlier centralizer structure; the assessed new result is the *full nonzero-fiber* law, including the contrast between scalar and nonscalar targets.

## Assumptions and scope

Let \(k=\mathbb F_q\) have characteristic \(2\). An octonion is a formal Zorn matrix \([a,u;v,b]\), where \(a,b\in k\) and \(u,v\in k^3\). For \(B=[c,x;y,d]\), the multiplication is

\[
[a,u;v,b][c,x;y,d]
=[ac+u\cdot y,\ ax+du-v\times y;\ cv+by+u\times x,\ bd+v\cdot x].
\]

The symbols \(\cdot\) and \(\times\) are the standard coordinate dot and cross products over \(k\). This is the eight-dimensional split unital alternative algebra; its identity is \([1,0;0,1]\), and \(\operatorname{tr}[a,u;v,b]=a+b\). Note that \(-1=1\) in \(k\). All counts refer to ordered pairs in the *entire algebra*, without quotienting by automorphisms. The result applies only to finite fields of characteristic two, not to arbitrary non-split octonion algebras over other fields.

## Proof

**1. Cancellation of cross terms and symplectic reduction.** For \(A=[a,u;v,b]\) and \(B=[c,x;y,d]\), put \(\alpha=a+b\), \(\beta=c+d\), \(w=(u,v)\in k^6\), and \(t=(x,y)\in k^6\). Define

\[
\omega(w,t)=u\cdot y+v\cdot x.
\]

This is a nondegenerate alternating bilinear form on \(k^6\): for each nonzero \(w\), the functional \(t\mapsto\omega(w,t)\) is nonzero and therefore has \(q^5\) solutions at every prescribed value. Directly subtracting the two Zorn products, using \(v\times y+y\times v=0\) and \(u\times x+x\times u=0\) in characteristic two, gives the exact formula

\[
[A,B]=[s,U;V,s],\qquad s=\omega(w,t),\quad (U,V)=\alpha t+\beta w.
\]

In particular every output is trace zero. For fixed \(\alpha,\beta,w,t\), the diagonal entries \(a,c\) are freely chosen and \(b=a+\alpha\), \(d=c+\beta\); hence each choice of these variables represents exactly \(q^2\) ordered octonion pairs.

**2. The case \(\alpha=\beta=0\).** Now \((U,V)=0\). If \(s=0\), count \(w=0\) with all \(q^6\) choices of \(t\), plus \(q^6-1\) nonzero \(w\), each with \(q^5\) compatible \(t\). Multiplying by \(q^2\) gives \(q^{13}+q^8-q^7\). If \(s\ne0\), one must have \(w\ne0\), and each such \(w\) has \(q^5\) compatible \(t\); the count is \(q^{13}-q^7\). There are no solutions in this case for nonzero \((U,V)\).

**3. The case \(\alpha\ne0\).** Fix a desired six-vector \(W=(U,V)\). The vector \(t\) is forced by \(t=\alpha^{-1}(W+\beta w)\), so \(s=\alpha^{-1}\omega(w,W)\). If \(W\ne0\), this is one nonzero linear equation in \(w\) and admits exactly \(q^5\) solutions for every \(s\). There are \(q-1\) values of \(\alpha\), \(q\) values of \(\beta\), and the factor \(q^2\) from the diagonal choices, giving \((q-1)q^8\) ordered pairs for each \((s,W)\). If \(W=0\), necessarily \(s=0\), and there are \(q^6\) choices of \(w\), producing \((q-1)q^9\) pairs. No other scalar outputs arise here.

**4. The case \(\alpha=0\), \(\beta\ne0\).** Now \(W=\beta w\), hence \(w=\beta^{-1}W\). For \(W\ne0\), the functional \(t\mapsto\omega(w,t)\) again has \(q^5\) solutions at every \(s\). Accounting for the \(q-1\) values of \(\beta\) and the diagonal factor \(q^2\), the count is \((q-1)q^7\). If \(W=0\), then \(w=0\) and \(s=0\), yielding \((q-1)q^8\) pairs. No nonzero scalar outputs arise.

**5. Summation and boundary cases.** For every \(W\ne0\), summing the last two cases gives \((q-1)q^8+(q-1)q^7=(q^2-1)q^7\), independently of the scalar coordinate \(s\). For \(W=0,s=0\), the three contributions sum to

\[
q^{13}+q^8-q^7+(q-1)q^9+(q-1)q^8=q^{13}+q^{10}-q^7.
\]

For \(W=0,s\ne0\), only Step 2 contributes, yielding \(q^{13}-q^7\). These are all target types. Every listed trace-zero fiber is positive, proving surjectivity. The sum across all target types is

\[
(q^{13}+q^{10}-q^7)+(q-1)(q^{13}-q^7)+(q^7-q)(q^2-1)q^7=q^{16},
\]

which accounts for every ordered pair. Dividing the zero-fiber count by \(|\mathcal O_q|^2=q^{16}\) gives the commuting probability.

## Verification

The standalone Python 3 program `verify_char2_octonion.py` builds the Zorn multiplication from its eight coordinates and checks all \(2^{16}=65,536\) ordered input pairs over \(\mathbb F_2\), covering all 128 trace-zero targets and every predicted fiber multiplicity. An independent formula check for 15,000 deterministically seeded pairs over \(\mathbb F_4\) uses explicit arithmetic modulo \(X^2+X+1\) and compares direct multiplication with the symplectic reduction. `verification_output.txt` contains actual executable output. The finite checks test the proof but are not substitutes for the argument over arbitrary \(q=2^e\).

## Relationship to prior work

Castillo-Ramírez and Elduque [1], originally posted in 2015, supply the split Cayley setting and special features of its characteristic-two derivation algebra (their primary MSC is 17A75). Knarr and Stroppel [2] classify subalgebras and centralizers, including characteristic two, so a zero-commutator count from centralizer dimensions is **not** asserted as new. Lopatin and Zubkov [3] classify pairs of octonions up to automorphism over algebraically closed fields; this does not directly count labeled fibers over finite fields. The closely related finite-field fiber theorem [4] concerns only **odd characteristic** and exhibits a quadratic-character-dependent split of nonzero targets; its proof explicitly uses division by two and its stated scope excludes characteristic two. Our off-zero result instead has a uniform nonscalar fiber and a separate enlarged nonzero-scalar fiber. The exact characteristic-two laws do not follow by plugging even \(q\) into the odd-characteristic formulas.

## Limitations

The theorem concerns the split Cayley algebra over \(\mathbb F_{2^e}\), ordered pairs, and ordinary additive commutators. It does not classify automorphism orbits of each fiber, nor does it claim uniqueness of a historical proof. Older results on centralizers account for the zero fiber; a possible unstated implication of finite-field pair-orbit enumeration or bilinear-map representation theory remains a historical-priority risk. Independent validation has not been performed.

## References

1. A. Castillo-Ramírez and A. Elduque, *Some special features of Cayley algebras, and \(G_2\), in low characteristics*, arXiv:1503.05529, first posted 2015-03-18. See introduction, split good-basis table and Section 4.
2. N. Knarr and M. J. Stroppel, *Subalgebras of Octonion Algebras*, arXiv:2303.00335, 2023, Sections 3 and 7.
3. A. Lopatin and A. N. Zubkov, *Classification of \(G_2\)-orbits for pairs of octonions*, arXiv:2208.08122, 2022, Sections 1.2 and 4.
4. *Exact commutator fibers of split octonion algebras over odd finite fields*, public record dated 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-commutator-fibers-of-split-octonion-algebras-over-odd-fini--a9de9b1b9f96. Its scope excludes characteristic two.

