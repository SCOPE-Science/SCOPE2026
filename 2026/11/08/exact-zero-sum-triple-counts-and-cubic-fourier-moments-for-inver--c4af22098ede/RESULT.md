# Exact zero-sum triple counts and cubic Fourier moments for inverse-square modular graphs

## Finding

For any integer \(m\ge2\), write \(U_m=(\mathbb Z/m\mathbb Z)^\times\) and consider the modular inverse-square graph
\[H_m=\{(x,x^{-2}):x\in U_m\}\subseteq(\mathbb Z/m\mathbb Z)^2.\]
Let \(Z(m)\) be the number of **ordered triples** \((P_1,P_2,P_3)\in H_m^3\) whose sum is zero, counting repeated points if they occur. The exact answer is
\[Z(m)=\varphi(m)\prod_{p^a\parallel m}c(p,a),\]
where the product is over the prime powers dividing \(m\), and
\[c(p,a)=\begin{cases}
2p^{\lfloor a/2\rfloor},&p\equiv1\pmod3,\\
3^{a-1},&p=3\text{ and }a\in\{1,2\},\\
0,&\text{otherwise}.
\end{cases}\]
Thus the count is nonzero if and only if every prime divisor other than \(3\) is congruent to \(1\) modulo \(3\), and \(3^3\) does not divide \(m\). In particular, the count is positive for \(m=9\) but vanishes for \(m=27\); for primes congruent to \(1\) modulo \(3\), the multiplicity grows by a square-root-scale factor along higher prime-power levels.

Define the generalized complete exponential sum
\[S_m(r,s)=\sum_{x\in U_m}\exp\!\left(\frac{2\pi i}{m}(rx+sx^{-2})\right).\]
Then the same exact statement is the **non-absolute cubic moment** identity
\[\sum_{r,s\bmod m}S_m(r,s)^3=m^2 Z(m).\]
No absolute values are inserted in the cubic moment.

## Assumptions and scope

All arithmetic is in the residue ring modulo the specified integer. Negative exponents occur only on units. The integers \(r,s\) in the cubic moment independently range over all residue classes modulo \(m\). There is no squarefree assumption. The theorem treats all integers \(m\ge2\); it does not assert an extension estimate or a fourth-moment formula.

## Proof

**Step 1 (scaling and an exact polynomial identity).** Write a zero-sum triple in the form \((x,x^{-2})\), \((y,y^{-2})\), \((z,z^{-2})\). Its first-coordinate equation gives \(z=-x-y\). Because \(x\in U_m\), put \(t=yx^{-1}\). Then \(y=xt\) and \(z=-x(1+t)\), so the three first coordinates are units exactly when \(x,t,1+t\) are units. The second-coordinate equation is
\[x^{-2}\bigl(1+t^{-2}+(1+t)^{-2}\bigr)=0.\]
Multiplying by the unit \(x^2t^2(1+t)^2\), it is equivalent to
\[t^2(1+t)^2+(1+t)^2+t^2=(t^2+t+1)^2=0\pmod m.\]
Consequently the number of choices for \(x\) is \(\varphi(m)\), independently of \(t\), and
\[Z(m)=\varphi(m)\#\{t\bmod m:\gcd(t(t+1),m)=1,\ (t^2+t+1)^2\equiv0\pmod m\}.\]
No solutions are lost by clearing denominators, since the cleared factors are explicitly units.

**Step 2 (Chinese-remainder reduction).** For \(m=\prod_{p^a\parallel m}p^a\), the set of admissible ratios \(t\) decomposes under the Chinese remainder theorem into independent local ratio sets. Therefore their cardinalities multiply. It remains to count \(t\) modulo each \(p^a\).

**Step 3 (primes away from three).** Let \(F(t)=t^2+t+1\). If \(p\neq3\), the congruence \(F(t)\equiv0\pmod p\) has exactly two roots when \(p\equiv1\pmod3\) and no roots otherwise. Indeed, a root is a nontrivial cubic root of unity in the multiplicative group of \(\mathbb F_p\), since \((t-1)F(t)=t^3-1\). When \(p=2\) there is no admissible ratio because \(t\) and \(t+1\) cannot both be units. At the two roots for \(p\equiv1\pmod3\), the derivative \(F'(t)=2t+1\) is nonzero modulo \(p\): otherwise \(4F(t)=3\pmod p\), which would force \(p=3\). Each simple root lifts uniquely through every power of \(p\) by Hensel's lemma. The square condition \(p^a\mid F(t)^2\) is exactly \(F(t)\equiv0\pmod{p^{\lceil a/2\rceil}}\). Hence there are two roots modulo \(p^{\lceil a/2\rceil}\), each with \(p^{\lfloor a/2\rfloor}\) unrestricted lifts modulo \(p^a\); all retain the unit conditions. This gives \(c(p,a)=2p^{\lfloor a/2\rfloor}\).

**Step 4 (the ramified prime three).** Modulo \(3\), the polynomial has the unique root \(t=1\), which satisfies the required unit conditions. Every possible root modulo a power of \(3\) therefore has \(t=1+3u\) and
\[F(1+3u)=3(1+3u+3u^2).\]
The parenthetical factor is a unit modulo \(3\), so \(\nu_3(F(t))=1\) for every candidate. Accordingly \(3^a\mid F(t)^2\) holds exactly for \(a\le2\). There are \(3^{a-1}\) residues \(t\equiv1\pmod3\) modulo \(3^a\), yielding \(c(3,1)=1\), \(c(3,2)=3\), and \(c(3,a)=0\) for every \(a\ge3\). Combining Steps 1–4 proves the formula and the complete nonvanishing criterion.

**Step 5 (cubic Fourier identity).** Expand \(S_m(r,s)^3\) as a sum over ordered triples \((x,y,z)\in U_m^3\). For each triple, summing independently over \(r\) and \(s\) uses character orthogonality:
\[\sum_{r\bmod m}\exp\!\left(\frac{2\pi ir}{m}(x+y+z)\right)=m\,\mathbf1_{x+y+z=0},\]
with an analogous formula for inverse-square second coordinates. The product is \(m^2\) precisely for the counted triples and zero otherwise. This proves the moment identity.

## Verification

The self-contained `verify.py` enumerates the complete unit-pair search for every modulus \(2\le m\le300\). It independently counts direct triples, counts admissible ratios using the polynomial identity, and computes the prime-factor formula. These agree in all \(299\) cases. It also checks values \(Z(3)=2\), \(Z(9)=18\), \(Z(27)=0\), \(Z(49)=588\), \(Z(81)=0\), and \(Z(169)=4056\). Run with `python verify.py` from the directory containing that file. These are finite corroborations only; the unrestricted conclusion is the proof above.

## Relationship to prior work

Shparlinski's survey *Modular Hyperbolas* [1] treats modular inverse graphs, arithmetic and geometric distribution questions, rational-function exponential sums and generalized polynomial congruences; Sections 1.2, 2.1, 6.1 and 6.2 provide context and tools, but the inspected statements do not give the present inverse-square zero-triple formula or its ramified \(3\)-adic count. Bourgain and Garaev [2] analyze additive properties of reciprocal sets over prime fields, principally intervals, without the present full-ring inverse-square classification. A separate finite-field result on additive **four**-energy of inverse-square graphs is related by the object but has a different number of summands, coefficient conditions, and domain; that fourth-order statement alone cannot imply this cubic moment or any prime-power lifting counts. The polynomial factorization, CRT, Hensel lifting and Fourier orthogonality used here are standard; priority is claimed only for their specific complete triple-count application, not for these general tools.

## Limitations

The proof does not address nonzero target vectors, mixed powers, or graphs completed by nonunits. Historical novelty has not been independently adjudicated; an unlocated theorem on ternary zero sums or generalized cubic moments might imply this result. The verified numeric range is finite, not a substitute for the global argument. The equality of non-absolute cubic moments does not imply a sharp extension inequality.

## References

1. I. E. Shparlinski, *Modular Hyperbolas*, arXiv:1103.2879 (first publicly submitted 2011-03-15), especially §§1.2, 2.1, 6.1–6.2. https://arxiv.org/abs/1103.2879
2. J. Bourgain and M. Z. Garaev, *Sumsets of reciprocals in prime fields and multilinear Kloosterman sums*, arXiv:1211.4184 (2012-11-18), especially §§1–2. https://arxiv.org/abs/1211.4184
