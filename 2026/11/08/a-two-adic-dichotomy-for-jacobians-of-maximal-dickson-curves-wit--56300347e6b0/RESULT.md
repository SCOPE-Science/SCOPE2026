# A two-adic dichotomy for Jacobians of maximal Dickson curves with minimal automorphisms

## Finding
Let \(p>3\) be prime, \(q=p^s\) with \(s\geq1\), and let \(n>5\) be odd with \(n\mid(q+1)/2\). Suppose neither \(2n-1\) nor \(4n-1\) is a power of \(p\). Define the first-kind Dickson polynomial \(D_n\) by \(D_n(z+z^{-1})=z^n+z^{-n}\), and let \(C_n/\mathbb F_q\) be the smooth projective curve with affine model \(y^2=(x+2)D_n(x)\). Set \(g=(n-1)/2\) and \(J_n=\operatorname{Jac}(C_n)\).

**Claim (exact rational Jacobian group).** As finite abstract abelian groups,
\[
J_n(\mathbb F_q)\cong
\begin{cases}
(\mathbb Z/(q+1)\mathbb Z)^{g}, &q\equiv1\pmod4,\\[3pt]
(\mathbb Z/2\mathbb Z)^g\oplus(\mathbb Z/((q+1)/2)\mathbb Z)^g,&q\equiv3\pmod4.
\end{cases}
\]
In either case \(\#J_n(\mathbb F_q)=(q+1)^g\). These groups occur on the infinite, unbounded-genus family whose geometric automorphism group consists only of the hyperelliptic involution, as established by Borges and Reis. The statement concerns the exact group structure over \(\mathbb F_q\); maximality and the automorphism classification are previously known.

## Assumptions and scope
The finite-field base, oddness and divisibility hypotheses are those above. The smooth projective model is used throughout. Since \(p\nmid n\), the polynomial \(D_n\) is separable, and \(D_n(-2)=-2\ne0\); the polynomial \((x+2)D_n(x)\) has \(n+1=2g+2\) distinct geometric roots, so \(C_n\) is a smooth hyperelliptic curve of genus \(g\). The exact hypotheses excluding exceptional powers of \(p\) ensure the small geometric automorphism group in the cited source; the algebraic group calculation itself uses maximality and the branch orbit structure, and does not assume any additional unproved property.

For any prime \(\ell\ne p\), let \(T_\ell J_n\) denote the free \(\mathbb Z_\ell\)-Tate module of rank \(2g\), and let \(\pi\) denote the arithmetic \(q\)-Frobenius endomorphism on \(J_n\). The notation \(v_2\) denotes the ordinary \(2\)-adic valuation.

## Proof
**1. Frobenius equation and total order.** Borges--Reis, Theorem 1.2, shows that \(C_n\) is maximal over \(\mathbb F_{q^2}\); this maximality was already known from Tafazolian--Top, Theorem 1.4. Hence every reciprocal root of its zeta numerator over \(\mathbb F_{q^2}\) is \(-q\). Frobenius is semisimple on \(T_\ell J_n\otimes\mathbb Q_\ell\) and the Tate representation of the endomorphism algebra is faithful. It follows that the \(q^2\)-Frobenius is \([-q]\), so \(\pi^2=[-q]\). Since \(X^2+q\) has distinct characteristic-zero roots and is irreducible over \(\mathbb Q\), the characteristic polynomial of \(\pi\) is \((X^2+q)^g\). Thus
\[\#J_n(\mathbb F_q)=\det(1-\pi\mid T_\ell J_n)=(q+1)^g.\]
For each \(\ell\ne p\), the \(\ell\)-primary rational subgroup identifies with the finite cokernel of \(\pi-1\) on \(T_\ell J_n\). This follows from the exact sequence \(0\to T_\ell J_n\to T_\ell J_n\otimes\mathbb Q_\ell\to J_n[\ell^\infty]\to0\), because \(\pi-1\) is invertible on the middle term.

**2. All odd-prime elementary divisors.** Let \(\ell\mid(q+1)\) be odd and write \(a=v_\ell(q+1)\). Modulo \(\ell\), \(X^2+q\equiv(X-1)(X+1)\). Since \(2\) is an \(\ell\)-adic unit, Hensel's lemma gives distinct roots \(r_+,r_-\in\mathbb Z_\ell\) with \(r_+\equiv1\), \(r_-\equiv-1\pmod\ell\), and \(r_+-r_-\) a unit. The integral spectral idempotents split \(T_\ell J_n\) into rank-\(g\) \(r_+\)- and rank-\(g\) \(r_-\)-eigensummands. From \((r_+-1)(r_++1)=-(q+1)\), the first summand has \(v_\ell(r_+-1)=a\); on the second, \(r_--1\) is a unit. Therefore
\[J_n(\mathbb F_q)[\ell^\infty]\cong(\mathbb Z/\ell^a\mathbb Z)^g.\]
This handles every odd prime factor of \(q+1\), while no prime outside \(q+1\) can divide the group order.

**3. Rational Weierstrass points and Frobenius on \(2\)-torsion.** The branch points of the hyperelliptic double cover \(C_n\to\mathbb P^1\) are \(-2\) and the \(n\) roots of \(D_n\); the two points at infinity are unramified. Write any root of \(D_n\) as \(x=z+z^{-1}\) with \(z^{2n}=-1\). Thus \(z^{4n}=1\) and \(z\) has odd exponent in a fixed primitive \(4n\)-th root. Since \(n\mid(q+1)/2\), we have \(q\equiv-1\pmod{2n}\).

If \(q\equiv3\pmod4\), the oddness of \(n\) forces \(4n\mid(q+1)\); therefore \(z^q=z^{-1}\) and every \(D_n\)-root lies in \(\mathbb F_q\). All \(2g+2\) Weierstrass points are rational and all \(J_n[2]\) is rational.

If \(q\equiv1\pmod4\), one instead has \(q\equiv2n-1\pmod{4n}\). Consequently \(z^q=-z^{-1}\) and \(x^q=-x\). The odd polynomial \(D_n\) has exactly one fixed root \(0\), and its other \(n-1=2g\) roots form \(g\) opposite pairs; \(-2\) is a second fixed branch point. The standard even-subset description
\[J_n[2](\overline{\mathbb F}_q)\cong\{(\epsilon_b)_{b\in B}\in\mathbb F_2^B:\sum_{b\in B}\epsilon_b=0\}/\langle(1)_{b\in B}\rangle\]
for the \(2g+2\)-element branch set \(B\) then gives \(\dim_{\mathbb F_2}J_n[2](\mathbb F_q)=g\): among the \(g+2\) Frobenius orbits, the even-sum condition and quotient by the all-ones vector remove two dimensions. One must check invariants commute with passage to the quotient: any representative \(v\) of a fixed quotient class satisfies \(\sigma v-v\in\{0,\mathbf1\}\); the two individually fixed branch coordinates force \(\sigma v-v\ne\mathbf1\), so the quotient fixed vectors do have fixed representatives.

**4. The \(2\)-primary group.** If \(q\equiv1\pmod4\), then \(v_2(q+1)=1\). The total \(2\)-primary order is \(2^g\), whereas the preceding calculation gives exactly \(2^g\) rational points of order dividing \(2\). It follows that \(J_n(\mathbb F_q)[2^\infty]\cong(\mathbb Z/2\mathbb Z)^g\).

Now suppose \(q\equiv3\pmod4\), and put \(a=v_2(q+1)\ge2\). Full rational \(2\)-torsion means that \(\pi-1\) is divisible by \(2\) as an endomorphism of the free \(\mathbb Z_2\)-module \(T_2J_n\). Put \(A=(\pi-1)/2\in\operatorname{End}_{\mathbb Z_2}(T_2J_n)\). The relation \(\pi^2=-q\) gives
\[A^2+A+c=0,\qquad c=(q+1)/4.\]
If \(a=2\), then \(c\) is odd; the identity \(A(A+1)=-cI\) makes \(A\) invertible over \(\mathbb Z_2\). Hence the cokernel of \(\pi-1=2A\) is \((\mathbb Z/2\mathbb Z)^{2g}\), in agreement with the claimed formula.

If \(a\ge3\), then \(c\) is even. Hensel's lemma splits \(t^2+t+c\) over \(\mathbb Z_2\) into roots \(u_0\equiv0\) and \(u_1\equiv1\pmod2\), differing by a unit. Integral idempotents decompose \(T_2J_n\) into their two rank-\(g\) eigensublattices (multiplicities follow from \((X^2+q)^g\)). Here \(u_1\) is a unit and \(u_0u_1=c\), so \(v_2(u_0)=a-2\). Consequently the elementary divisors of \(\pi-1=2A\) are \(2^{a-1}\) repeated \(g\) times and \(2\) repeated \(g\) times. Thus for all \(a\ge2\),
\[J_n(\mathbb F_q)[2^\infty]\cong(\mathbb Z/2\mathbb Z)^g\oplus(\mathbb Z/2^{a-1}\mathbb Z)^g.\]

**5. Assembly.** The odd-primary computation in Step 2 and the \(2\)-primary computation in Step 4 combine by the Chinese remainder theorem to yield the two displayed abstract group structures, for every permitted \(q,n\). This proves the claim.

## Verification
The standalone executable `verify.py` uses only Python's standard library and exact arithmetic. Its checks for ten admissible cases with \(n=7,9,11,13\), including \((q,n)=(41,7),(83,7),(167,7),(223,7)\), reconstruct \(D_7\), enumerate every affine \(\mathbb F_q\)-point plus both rational points at infinity, enumerate rational branch roots, calculate Frobenius-fixed even-subset classes representing rational \(2\)-torsion, and cross-check the proposed invariant factors against \((q+1)^g\). It returns `VERIFY_OK` on success. The chosen cases test \(v_2(q+1)=1,2,3,5\). These computations corroborate examples only; Steps 1--5 are the uniform proof, including all extension-field cases and arbitrarily large \(n\).

## Relationship to prior work
Tafazolian--Top (2019), Theorem 1.4, already determines maximality for the odd-degree Chebyshev hyperelliptic family. Borges--Reis (2026), Theorem 1.2, identifies the subfamily with exactly the hyperelliptic involution as geometric automorphism and reiterates its maximality. Neither maximality nor the automorphism order is asserted as a new theorem here. Prior Jacobian isogeny and zeta-polynomial discussions determine the order \((q+1)^g\) but do not alone specify the finite group's elementary divisors. The new argument uses the Dickson branch permutation together with \(2\)-adic integral Frobenius structure to distinguish two group presentations. Broad generic rational-point group algorithms and module-structure criteria are not exact group classifications for this specific family.

## Limitations
This proves the abstract \(\mathbb F_q\)-rational group, not a canonical list of divisor generators, the polarization, the \(\mathbb F_q\)-isomorphism type of \(J_n\), or group structures over every extension \(\mathbb F_{q^r}\). The argument assumes the cited maximality theorem, not an independent reproof of that published result. Existing broad module-structure results could subsume some steps, and not every potentially relevant full-text publication could be inspected; historical priority remains provisional. No independent specialist audit has been performed.

## References
1. H. Borges and L. Reis, *Maximal Curves with Few Automorphisms*, arXiv:2610.37777v1 (first publicly submitted 2026-10-27), especially Theorem 1.2, Lemma 2.1 and Section 5.2. https://arxiv.org/html/2610.37777v1
2. S. Tafazolian and J. Top, *On certain maximal hyperelliptic curves related to Chebyshev polynomials*, arXiv:1902.06262 (2019), especially Theorem 1.4 and Sections 2--5. https://arxiv.org/abs/1902.06262
3. G. Dias, S. Tafazolian and J. Top, *On certain maximal curves related to Chebyshev polynomials*, Finite Fields and Their Applications 101 (2025), Article 102521, DOI:10.1016/j.ffa.2024.102521. Relevant Chebyshev maximality context, but no complete full-text originality comparison was possible.
4. C. Springer, *The structure of the group of rational points of an abelian variety over a finite field*, European Journal of Mathematics 7 (2021), 1124--1136, DOI:10.1007/s40879-021-00460-1. General group-structure context; the present proof uses an explicit integral Frobenius decomposition rather than invoking its hypotheses.
