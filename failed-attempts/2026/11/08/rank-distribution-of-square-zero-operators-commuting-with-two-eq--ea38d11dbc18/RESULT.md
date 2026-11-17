# Rank distribution of square-zero operators commuting with two equal nilpotent Jordan blocks

## Finding

Let \(k=\mathbb F_q\) be any finite field, let \(m\ge3\), and put \(B=J_m(0)\oplus J_m(0)\) on \(k^{2m}\). Write
\[
H_{m,q}(r)=\#\{X\in M_{2m}(k):XB=BX,\ X^2=0,\ \operatorname{rank}_k X=r\},\quad
\mathcal H_{m,q}(z)=\sum_{r=0}^{m}H_{m,q}(r)z^r.
\]
This note determines **every** \(H_{m,q}(r)\) through the following finite formulas.

Set \(s=\lfloor m/2\rfloor\), \(h=\lceil m/2\rceil\), and
\[
D_q=\frac{(q^2-1)^2}{q-1},\qquad
U_{\ell,q}=q^{4\ell-4}(q^2-1)(q^2-q)
\]
for \(\ell\ge1\). Define
\[
P_{\ell,q}(z)=U_{\ell,q}z^{2\ell}
+D_q q^{3\ell-3}z^\ell
+D_q(q-1)\sum_{d=1}^{\ell-1}q^{4\ell-4-d}z^{2\ell-d}.
\]
Then the complete rank-generating polynomial is
\[
\boxed{\begin{aligned}
\mathcal H_{m,q}(z)
={}&1+\sum_{\ell=1}^{s}P_{\ell,q}(z)
+(q^2-1)q^{2m-2}z^m\\
&+\sum_{a=1}^{h-1}\left[
(q^2-1)q^{2m-a-2}z^{m-a}
+(q^2-1)(q-1)\sum_{c=0}^{a-1}q^{2m-c-3}z^{m-c}
\right].
\end{aligned}}
\]
Empty sums are zero. All exponents and coefficients are nonnegative integers in the stated domain; the displayed \(D_q\) is integral.

Two compact consequences are
\[
\boxed{\sum_{r=0}^{m}H_{m,q}(r)
=h(q^2-1)q^{2m-2}+q^{4s}}
\]
and
\[
\boxed{H_{m,q}(m)
=(q^2-1)q^{2m-3}\left(q+s(q-1)\right).}
\]
The first counts all commuting square-zero matrices, and the second counts those of **maximal possible square-zero rank**, namely \(m\). Both hold in every characteristic, including characteristic two. The intermediate coefficients describe the complete intersections with the square-zero Jordan classes of types \((2^r,1^{2m-2r})\), including \(r=0\).

For example, in characteristic two the polynomials are
\[
\mathcal H_{3,2}(z)=1+9z+30z^2+72z^3,
\]
\[
\mathcal H_{4,2}(z)=1+9z+78z^2+168z^3+384z^4.
\]

## Assumptions and scope

All matrices are labeled elements of \(M_{2m}(k)\), not simultaneous-conjugation orbits. We count \(X\) satisfying \(X^2=0\) and commuting with the **fixed** matrix \(B\) of Jordan type \((m,m)\). The field size is an arbitrary prime power. A square-zero \(2m\)-by-\(2m\) matrix has \(k\)-rank at most \(m\), and its Jordan type is entirely determined by that rank.

The lower cases \(m=1,2\) can also be evaluated by the same formulas and are used only as consistency checks. The finding asserts the unrestricted new length range \(m\ge3\).

## Proof

**1. Reduction to matrices over a chain ring.** Identify \(k^{2m}\) with \(R_m^2\), where \(R_m=k[t]/(t^m)\). Under this identification \(B\) acts by multiplication by \(t\). Consequently its full centralizer is \(\operatorname{End}_{R_m}(R_m^2)=M_2(R_m)\), and the ranks of its elements over \(k\) are the dimensions of their images as \(k\)-vector spaces. This correspondence preserves the equation \(X^2=0\).

**2. Primitive square-zero matrices.** An element \(Y\in M_2(R_\ell)\) is *primitive* if at least one entry is a unit. If \(Y^2=0\) and \(Y\) is primitive, then its reduction modulo \(t\) is a nonzero square-zero \(2\)-by-\(2\) matrix over \(k\). Choose \(v\) whose image under \(Y\) is primitive. Modulo \(t\), \(Yv\) and \(v\) are independent because a nonzero square-zero endomorphism of \(k^2\) has image equal to kernel. Nakayama's lemma therefore makes \((Yv,v)\) an \(R_\ell\)-basis. In this basis \(Y\) equals the elementary matrix \(E_{12}\). Thus all primitive square-zero matrices constitute one \(\operatorname{GL}_2(R_\ell)\)-conjugacy class. The invertible centralizer of \(E_{12}\) consists of \(\begin{psmallmatrix}u&w\\0&u\end{psmallmatrix}\) with \(u\in R_\ell^\times\), \(w\in R_\ell\), so orbit–stabilizer yields
\[
\#\{Y\text{ primitive}:Y^2=0\}
=\frac{q^{4(\ell-1)}|\operatorname{GL}_2(k)|}{(q-1)q^{2\ell-1}}
=(q^2-1)q^{2\ell-2}.
\tag{1}
\]

**3. Valuation layers of the square-zero equation.** Define the valuation of a nonzero matrix \(X\in M_2(R_m)\) as the least \(t\)-adic valuation of its four entries. If this is \(a<h\), then \(X=t^aY\) for a unique primitive \(Y\in M_2(R_{m-a})\); the equation \(X^2=0\) is equivalent to
\[
Y^2=0\pmod{t^{m-2a}}.
\]
Put \(\ell=m-2a>0\). Reduction to \(R_\ell\) gives a primitive square-zero matrix and exactly \(q^{4a}\) lifts. Hence by (1) **every** such valuation layer has
\[
(q^2-1)q^{2\ell-2}q^{4a}=(q^2-1)q^{2m-2}
\tag{2}
\]
matrices.

For \(a=0\), the matrix is conjugate to \(E_{12}\) over \(R_m\) and has underlying \(k\)-rank \(m\). For \(1\le a<h\), use conjugation over \(R_\ell\) and lift the conjugating matrix to \(R_{m-a}\); it is enough to study
\[
Y=E_{12}+t^\ell T,\qquad T\in M_2(R_a).
\]
The quantity \(\det(Y)/t^\ell\) modulo \(t^a\) is uniformly distributed over \(R_a\): after fixing three entries of \(T\), its dependence on the remaining \((2,1)\)-entry is affine with unit coefficient \(-(1+t^\ell T_{12})\). Thus the valuation of \(\det(Y)/t^\ell\) is \(c<a\) for exactly \((q-1)q^{a-c-1}\) values, or is at least \(a\) for one value. The other three entries of \(T\) are arbitrary, and equation (1) gives the respective counts
\[
(q^2-1)(q-1)q^{2m-c-3}\quad(0\le c<a),\qquad
(q^2-1)q^{2m-a-2}\quad(c=a).
\tag{3}
\]
Since \(Y\) has a unit entry, its Smith exponents are \((0,\nu_t(\det Y))\) (with the second exponent capped at \(m-a\)). The Smith exponents of \(X=t^aY\) therefore give \(k\)-rank \(m-c\), including the capped case \(c=a\). Equations (2)–(3) prove the explicit non-tail summands in \(\mathcal H_{m,q}\).

**4. The high-valuation tail.** All remaining matrices have entries divisible by \(t^h\), and are automatically square-zero. Multiplication by \(t^h\) identifies their \(k\)-rank distribution with that of **all** matrices in \(M_2(R_s)\), where \(s=m-h\). This family contains \(q^{4s}\) matrices.

For any nonzero \(Z\in M_2(R_s)\), write uniquely \(Z=t^{s-\ell}W\) with \(1\le\ell\le s\) and \(W\in M_2(R_\ell)\) primitive. Its \(k\)-rank agrees with that of \(W\) on \(R_\ell^2\). There are exactly \(|\operatorname{GL}_2(R_\ell)|=U_{\ell,q}\) invertible \(W\), each of rank \(2\ell\). Of the remaining primitive matrices, precisely
\[
D_q=\frac{(q^2-1)^2}{q-1}
\]
are rank one modulo \(t\), and each has \(q^{4(\ell-1)}\) lifts. For a fixed rank-one reduction, the determinant divided by \(t\) is uniform modulo \(t^{\ell-1}\): after elementary invertible row and column changes modulo \(t\), the Schur complement has a free coefficient with unit multiplier. Thus determinant valuation \(d\), \(1\le d<\ell\), occurs with fraction \((q-1)q^{-d}\), and determinant zero in \(R_\ell\) occurs with fraction \(q^{-(\ell-1)}\). Their Smith exponents are \((0,d)\) or \((0,\ell)\), and their respective \(k\)-ranks are \(2\ell-d\) or \(\ell\). This produces exactly \(P_{\ell,q}(z)\). Including the zero matrix proves that the tail polynomial is \(1+\sum_{\ell=1}^sP_{\ell,q}(z)\).

**5. Total and maximal rank.** There are \(h\) equal-size non-tail valuation layers in (2), and a tail of cardinality \(q^{4s}\). Hence the total count follows. For maximal \(k\)-rank \(m\), the \(a=0\) layer contributes \((q^2-1)q^{2m-2}\), every nonzero \(a<h\) layer contributes a fraction \(1-q^{-1}\) of that amount, and, only for even \(m=2s\), the tail contributes \(|\operatorname{GL}_2(R_s)|=(q^2-1)(q-1)q^{2m-3}\). The odd and even cases simplify to the same displayed formula involving \(s=\lfloor m/2\rfloor\). Every step is valid for arbitrary characteristic and all prime-power \(q\). This completes the proof.

## Verification

The companion standalone program `verify_centralizer.py` constructs every \(2\)-by-\(2\) polynomial matrix over \(k[t]/(t^m)\) in its selected finite cases, tests the four defining coefficients of its literal square, and independently computes the rank of its induced \(2m\)-by-\(2m\) \(k\)-linear map. It compares the full rank histogram with the formula, not merely total counts. Finite-field cases include \(q=2\), \(1\le m\le4\); \(q=3,4\), \(1\le m\le2\); and \(q=5,m=1\). The output in `VERIFY_OUTPUT.txt` is obtained by executing that program; `ALL_EXACT_SQUARE_ZERO_CENTRALIZER_RANK_CHECKS_PASS` is the success marker.

These are finite consistency checks. The proof above, not the finite search, establishes the theorem for all \(m\ge3\) and prime powers \(q\).

## Relationship to prior work

Britnell–Wildon (arXiv:1001.0811, initially public 2010-01-06) studies when nilpotent similarity classes contain commuting representatives and characterizes several possible Jordan-class pairings, including two-part partitions. Its result is existential and class-level; it does not specify labeled intersection cardinalities for fixed \(B\) and each square-zero rank.

Harima–Watanabe (arXiv:1206.6574, public on arXiv 2012-06-28; published in Journal of Algebra earlier) establishes structural results about centralizer algebras of nilpotent matrices, including their semisimple quotient. The chain-ring centralizer identification is standard context, not claimed new here. The inspected text does not formulate finite-field square-zero rank multiplicities.

Bogdanić–Đurić–Koljančić–Oblak–Šivic (arXiv:2212.08425, public 2022-12-16) gives a comprehensive description of which Jordan partitions can occur in the nilpotent centralizer of a matrix of type \((m,m)\). Its Theorem 3 and orbit tables address **nonempty intersections**, not exact finite-field numbers in the square-zero strata. Thus it motivates but does not explicitly provide the present enumeration.

The familiar \(m=1\) field case and \(m=2\) dual-number case are consistency checks, not claimed separately original. The general \(m\ge3\) rank polynomial and valuation-shell equidistribution are the assessed result.

## Limitations

No assertion is made for a fixed nilpotent matrix of arbitrary Jordan type, for nilpotent partners of index greater than two, or for simultaneous-conjugacy-orbit counts. Literature comparisons do not exclude an unidentified general Hall-polynomial or local-ring matrix-enumeration formula that would imply this specialization. No independent audit or priority certification has been performed.

## References

1. J. R. Britnell and M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first arXiv version 2010-01-06), https://arxiv.org/abs/1001.0811 .
2. T. Harima and J. Watanabe, *The commutator algebra of a nilpotent matrix and an application to the theory of commutative Artinian algebras*, arXiv:1206.6574 (arXiv version 2012-06-28), https://arxiv.org/abs/1206.6574 .
3. A. Carnevale, S. Shechter and C. Voll, *Enumerating traceless matrices over compact discrete valuation rings*, arXiv:1709.02717 (2017-09-08), https://arxiv.org/abs/1709.02717 .
4. D. Bogdanić, A. Đurić, S. Koljančić, P. Oblak and K. Šivic, *Jordan structures of nilpotent matrices in the centralizer of a nilpotent matrix with two Jordan blocks of the same size*, arXiv:2212.08425 (first version 2022-12-16), https://arxiv.org/abs/2212.08425 .
