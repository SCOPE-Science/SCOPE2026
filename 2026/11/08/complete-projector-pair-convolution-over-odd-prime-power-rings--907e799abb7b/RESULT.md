# Complete projector-pair convolution over odd prime-power rings

## Finding

Let \(p\) be any odd prime, \(k\ge2\), \(q=p^k\), and \(R=\mathbb Z/q\mathbb Z\). Let \(\mathcal P_{p,k}\) be the set of rank-one idempotent matrices in \(M_2(R)\). Its **entire ordered pair-sum representation function**
\[
r_{p,k}(S)=\#\{(P_1,P_2)\in\mathcal P_{p,k}^2:P_1+P_2=S\}
\]
is determined explicitly below. Every matrix with trace \(2\pmod q\) is represented, and no other matrix is. In particular, the number of representations is everywhere positive on the trace-two affine hyperplane, with sharp minimum
\[
\min_{\operatorname{tr}S=2}r_{p,k}(S)=p^{k-1}\begin{cases}4,&p=3,\\p-1,&p\ge5.\end{cases}
\]
The number of targets attaining this minimum is
\[
\begin{cases}
42\cdot3^{3k-4},&p=3,\\[2pt]
\dfrac{p-3}{2}(p^2+p)p^{3k-3},&p\ge5.
\end{cases}
\]
The exact additive energy, equivalently the unweighted fourth Fourier moment, is
\[
\boxed{\ E(\mathcal P_{p,k})=p^{5k-3}(p^3+7p^2+5p-1)-3p^{4k-2}(p+1).\ }
\]
Unlike mere existence of a two-projector decomposition, these formulas quantify every fiber and yield a depth-independent, sharp probability-minorization constant.

## Assumptions and scope

The ring \(R\) is a cyclic local ring with **odd prime** residue characteristic; no conclusion is asserted for \(p=2\), for non-prime residue size, or for matrices of size other than two. Since \(2\) is invertible in \(R\), every rank-one idempotent is uniquely \(P=\frac12 I+Y\), where
\[
Y=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\quad Q(Y)=a^2+bc=\frac14.
\]
The traceless matrices form an additive group of size \(q^3\), on which \(Q\) is nondegenerate. Write any trace-two target as \(S=I+T\) with traceless
\[
T=\begin{pmatrix}a&b\\c&-a\end{pmatrix}.
\]
For a residue \(u\in R\), \(v_p(u)\) is its valuation in \(\{0,\ldots,k\}\), with \(v_p(0)=k\). For nonzero \(T\), put \(j=\min(v_p(a),v_p(b),v_p(c))<k\), \(m=k-j\), and \(T=p^j T_0\) where \(T_0\) is primitive modulo \(p^m\) (at least one coordinate is a unit). Let \(D_0=Q(T_0)\pmod {p^m}\); it is independent of the choice of lift of \(T_0\). For a unit modulo \(p\), \(\chi_p\) is the quadratic sign \(+1\) for a square and \(-1\) for a nonsquare.

The complete pointwise formula is as follows. If \(\operatorname{tr}S\ne2\), then \(r_{p,k}(S)=0\). If \(T=0\), then
\[
r_{p,k}(I)=p^{2k-1}(p+1).
\]
If \(1\le j<k\), then
\[
r_{p,k}(I+T)=\begin{cases}
2p^{k+j},&p\mid D_0,\\
p^{k+j-1}(p-\chi_p(D_0)),&p\nmid D_0.
\end{cases}
\]
If \(j=0\), put \(D=Q(T)\pmod q\). Then
\[
r_{p,k}(I+T)=\begin{cases}
2p^k,&p\mid D,\\
p^{k-1}(p+1),&\chi_p(D)=-1,\\
(t+1)(p-1)p^{k-1},&\chi_p(D)=1,\quad t=v_p(1-D)<k,\\
\bigl(p+k(p-1)\bigr)p^{k-1},&D=1\pmod q.
\end{cases}
\]
The first three lines and last line cover all possibilities, including \(p=3\) and singular discriminant strata. All counts are **ordered** pair counts.

Let \(\mu\) be the uniform probability on \(\mathcal P_{p,k}\), and \(u\) the uniform probability on the trace-two hyperplane. The pointwise minorization is sharp:
\[
\mu*\mu\ge c_p u,\qquad c_p=\begin{cases}\frac34,&p=3,\\\frac{p(p-1)}{(p+1)^2},&p\ge5.\end{cases}
\]
Here the comparison is of nonnegative functions on the ambient additive matrix group, with \(u\) extended by zero outside the trace-two hyperplane.

## Proof

**1. Projector parametrization and lifts.** Cayley–Hamilton for traceless \(Y\) gives \(Y^2=Q(Y)I\), proving the stated parametrization. At any point \(Q(Y)=1/4\), the gradient \((2a,c,b)\) is not zero modulo \(p\). Thus each solution modulo \(p^m\) lifts to exactly \(p^2\) solutions modulo \(p^{m+1}\). Modulo \(p\), the number of solutions is \(p(p+1)\): for each \(a\), there are \(p-1\) solutions to \(bc=1/4-a^2\) if the latter is nonzero, and \(2p-1\) if it vanishes, yielding \(p^2+p\). It follows that \(|\mathcal P_{p,k}|=p^{2k-1}(p+1)\). For any unit \(D\), the primitive norm fiber \(Q(T)=D\pmod{p^m}\) has \((p^2+p\chi_p(D))p^{2m-2}\) elements. For any nonunit \(D\), the primitive fiber has \((p^2-1)p^{2m-2}\) elements, since the zero-norm quadric over \(\mathbb F_p\) has \(p^2\) points, one of which is nonprimitive.

**2. Normal form for primitive targets.** A primitive traceless \(2\times2\) matrix \(T_0\) modulo \(p^m\) reduces to a nonscalar matrix over \(\mathbb F_p\). (A scalar traceless matrix in odd characteristic is zero.) Such a matrix has a cyclic vector; lifting that vector and its image gives a basis over \(R_m\). Cayley–Hamilton then makes \(T_0\) conjugate to
\[
\begin{pmatrix}0&1\\D_0&0\end{pmatrix}.
\]
Conjugation preserves the idempotent set and pair counts, so all counting can be done in this normal form. The polarization \(B(Y,T)=Q(Y+T)-Q(Y)-Q(T)\) satisfies
\[
Q(T-Y)=Q(T)+Q(Y)-B(Y,T).
\]
Therefore, with \(Q(Y)=1/4\), the condition \(Q(T-Y)=1/4\) is \(B(Y,T)=Q(T)\).

**3. Primitive target fibers.** For \(j=0\), set \(D=D_0\). Writing \(Y=\begin{psmallmatrix}x&b\\c&-x\end{psmallmatrix}\), the polarization equation forces \(c=D(1-b)\). The norm condition, after the invertible change \(w=b-1/2\), is
\[
x^2-Dw^2=(1-D)/4.
\]
If \(p\mid D\), the right-hand side is a unit. For each \(w\pmod {p^k}\), Hensel lifting gives exactly two \(x\) solutions (the roots \(\pm1/2\pmod p\) have unit derivatives), giving \(2p^k\). If \(D\) is a nonsquare unit, the binary form is an unramified quadratic norm form and the right side is a unit, so every unit norm fiber has \((p+1)p^{k-1}\) points. If \(D\) is a square unit, it has a square root in \(R\), and the linear substitution \((x,w)\mapsto(x-\sqrt D w,x+\sqrt D w)\) is invertible. The equation becomes \(uv=(1-D)/4\). For a nonzero right side of valuation \(t<k\), summing the possible valuations of \(u\) gives \((t+1)(p-1)p^{k-1}\) solutions. For a zero right side, the count is \(p^k+k(p-1)p^{k-1}\) (including \(u=0\)). This proves every primitive line in the formula.

**4. Nonprimitive target fibers.** For \(T=p^jT_0\ne0\), \(1\le j<k\), put \(m=k-j\). The linear condition reduces modulo \(p^m\) to \(B(Y,T_0)=p^jD_0\). Each solution \(Y\) modulo \(p^m\) of this condition and \(Q(Y)=1/4\) lifts to exactly \(p^{2j}\) points on the smooth norm conic modulo \(p^k\). In the primitive normal form, the trace equation gives \(c=D_0(p^j-b)\), so
\[
x^2-D_0(b-p^j/2)^2=(1-p^{2j}D_0)/4.
\]
The right-hand side is always a unit modulo \(p\). When \(D_0\) is nonunit, there are \(2p^m\) solutions, as above. When it is a unit, the split or anisotropic binary form has \((p-\chi_p(D_0))p^{m-1}\) solutions. Multiplication by \(p^{2j}\) establishes the stated factors. The case \(T=0\) has \(|\mathcal P_{p,k}|\) solutions.

**5. Sharp lower bound and equality count.** The minimum over primitive targets is \((p-1)p^{k-1}\) when \(p\ge5\), attained exactly when \(D\) is a quadratic residue modulo \(p\) distinct from \(1\). The number of such targets is \((p-3)(p^2+p)p^{3k-3}/2\), by the norm-fiber counts in step 1. When \(p=3\), the only square unit residue is \(1\); the minimum becomes \(4\cdot3^{k-1}\), attained by all primitive nonsquare-norm targets and, for \(k\ge2\), by targets with \(v_3(1-D)=1\). The two counts add to \(6\cdot3^{3k-3}+24\cdot3^{3k-4}=42\cdot3^{3k-4}\). All nonprimitive and zero targets have strictly larger counts. Hence every trace-two target is represented and the bounds are sharp. Dividing the smallest count by \(|\mathcal P_{p,k}|^2/p^{3k}\) gives exactly \(c_p\).

**6. Complete energy count.** The additive energy equals \(\sum_{\operatorname{tr}S=2}r_{p,k}(S)^2\). Using the counts in step 1, separate the \(D\)-values into nonunits (\(p^{k-1}\) choices), nonsquare units (\(\frac{p-1}{2}p^{k-1}\) choices), square units with \(D\not\equiv1\pmod p\) (\(\frac{p-3}{2}p^{k-1}\) choices), and the \(D\equiv1\pmod p\) stratum. In the latter stratum, for each \(1\le t<k\), precisely \((p-1)p^{k-t-1}\) values satisfy \(v_p(1-D)=t\), in addition to \(D=1\). Multiply these numbers by the corresponding fixed-norm primitive fibers \((p^2+p\chi_p(D))p^{2k-2}\) or \((p^2-1)p^{2k-2}\), and by the square of the pair-sum multiplicity in step 3. The resulting elementary geometric sums give the primitive contribution
\[
U_k=(p+1)p^{4k-3}\bigl[p^k(p^2+5p-4)-p\bigr].
\]
For transparency, at each positive valuation \(j\), with \(m=k-j\), the respective counts of targets of norm-sign \(+1\), norm-sign \(-1\), and nonunit norm are
\[
\frac{p-1}{2}(p^2+p)p^{3m-3},\quad
\frac{p-1}{2}(p^2-p)p^{3m-3},\quad
(p^2-1)p^{3m-3}.
\]
Squaring the three fiber sizes in step 4 and summing gives exactly
\[
V_{k,j}=(p^2-1)(p+3)p^{5k-j-3}.
\]
The zero target contributes \(W_k=p^{4k-2}(p+1)^2\). Thus
\[
E(\mathcal P_{p,k})=U_k+\sum_{j=1}^{k-1}V_{k,j}+W_k,
\]
and finite geometric-series simplification yields the closed expression in the Finding section. Every target stratum has been included; no asymptotic or heuristic argument is used.

**7. Fourier identity.** Let \(\psi(z)=\exp(2\pi iz/q)\) and
\[
F_{p,k}(A)=\sum_{P\in\mathcal P_{p,k}}\psi(\operatorname{tr}(AP)),\qquad A\in M_2(R).
\]
The trace pairing of the additive matrix group is nondegenerate. Character orthogonality therefore yields
\[
q^{-4}\sum_{A\in M_2(R)}|F_{p,k}(A)|^4
=\#\{(P_1,P_2,P_3,P_4)\in\mathcal P_{p,k}^4:P_1+P_2=P_3+P_4\}
=E(\mathcal P_{p,k}).
\]
This is an exact **unweighted** fourth moment, not a sharp extension inequality for arbitrary input weights.

## Verification

The standalone standard-library `check.py` independently constructs the idempotent conic, forms the ordered pair convolution by integer arithmetic, and compares **every trace-two target** with the pointwise formula at prime powers \(3,9,27,5,25,7,11,13\). It checks the minimum and its equality multiplicity, support, and the energy formula. Invoke `python3 check.py` in the extracted directory. It prints `PROJECTOR_PAIR_CONVOLUTION_PASS` only if all assertions succeed. These finite tests corroborate, but do not replace, the proof for every odd prime and \(k\ge2\).

## Relationship to prior work

De Seguins Pazzis [1] proves existence criteria for decompositions as sums of two idempotents over **fields**, including the corresponding characteristic-not-two cases (Theorem 3). It does not state prime-power representation numbers, a sharp local-ring pointwise lower bound, or an all-depth fourth Fourier moment. Evdokimov and Ponomarenko [2] establish structural results on cyclotomic schemes and ring translation schemes, not the exact convolution of the rank-one idempotent conjugacy class. Tang, Zhou, and Su [3] study when **three** idempotents suffice over commutative rings and do not enumerate two-summand local-ring fibers. Prior finite-field Fourier work on the same rank-one idempotents fully covers the field-depth analog through Fourier inversion; the new claim is **restricted to \(k\ge2\)** and does not reassert depth-one novelty. The present formulas exploit nontrivial valuation strata and local lifting that are absent over fields.

## Limitations

The result is confined to \(M_2(\mathbb Z/p^k\mathbb Z)\) with odd prime \(p\) and \(k\ge2\). It does not establish sharp weighted extension constants or a full additive convolution on the ambient trace-unrestricted space (there the convolution is zero outside trace two). General local-ring association schemes or unlocated quadratic representation-density tables might imply the formula; historical priority cannot be certified from bounded searches. The computations are finite checks, not substitutes for the all-depth argument. Independent external mathematical validation has not been performed.

## References

1. C. de Seguins Pazzis, *On linear combinations of two idempotent matrices over an arbitrary field*, arXiv:0907.4436v1, first publicly submitted 25 July 2009, https://arxiv.org/abs/0907.4436v1. Theorem 3 and proof, pp. 3–17.
2. S. Evdokimov and I. Ponomarenko, *Normal cyclotomic schemes over a finite commutative ring*, arXiv:math/0608469v1, first publicly submitted 18 August 2006, https://arxiv.org/abs/math/0608469. Introduction, structural theorems, and Appendix 7.2.
3. G. Tang, Y. Zhou, and H. Su, *Matrices over a commutative ring as sums of three idempotents or three involutions*, arXiv:1712.04607v1, first publicly submitted 13 December 2017, https://arxiv.org/abs/1712.04607. Abstract, Theorems 1.1–1.3 and Section 2.
