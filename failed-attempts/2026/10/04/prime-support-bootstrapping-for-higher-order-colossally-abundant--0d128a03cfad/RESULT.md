# Prime-support bootstrapping for higher-order colossally abundant contacts
## Finding
Let \(k\ge 1\), and let \(n\) be a contact covered by the hypotheses of Musin's prime-exponent inequalities: \(n\in C_D(F(u),-\rho^k)\), with \(f(x)=F(\log x)\) increasing and concave on the required range. For a prime \(r\) and integer \(b\ge 0\), write
\[
L_k(r,b)=\frac{(1+1/S_{b+1}(r))^k-1}{k\log r},\qquad
U_k(r,b)=\frac{1-(1+1/S_b(r))^{-k}}{k\log r},
\]
where \(S_j(r)=r+r^2+\cdots+r^j\) and \(U_k(r,b)\) is used only for \(b\ge1\).

A prime divisor can be bootstrapped to another prime: if \(q\mid n\) and
\[
L_k(p,0)>U_k(q,1),
\]
then \(p\mid n\). Consequently, at order \(k=8\), every such contact is divisible by
\[
89\#=2\cdot3\cdot5\cdots89=23768741896345550770650537601358310.
\]
The adjacent-prime bootstrap is exact through \(89\): the required inequality holds for every consecutive-prime pair from \(2\to3\) through \(83\to89\), while it reverses for \(89\to97\). The reversal only marks the end of this certificate; it does not assert that \(97\nmid n\).

## Assumptions and scope
The statement applies to contacts satisfying the hypotheses of Theorem 3.9 of arXiv:2609.33794v1. In particular, the abscissa must obey the stated increasing-concave condition after the paper's reference point. No Riemann-hypothesis assumption is used. The conclusion concerns divisibility of every contact at level \(8\), not only a least contact and not only the specific numerical family \(A_k(1,1)\).

## Proof
Theorem 3.9 supplies an associated parameter \(\varepsilon>0\) such that, with \(b_r=v_r(n)\),
\[
L_k(r,b_r)\le \varepsilon
\]
for every prime \(r\), and
\[
\varepsilon\le U_k(r,b_r)
\]
whenever \(r\mid n\).

Suppose \(q\mid n\). Since \(b_q\ge1\), and \(S_b(q)\) increases with \(b\), the quantity \(U_k(q,b)\) decreases with \(b\). Hence
\[
\varepsilon\le U_k(q,b_q)\le U_k(q,1).
\]
If \(p\nmid n\), then \(b_p=0\), so Theorem 3.9 also gives
\[
L_k(p,0)\le\varepsilon.
\]
Therefore \(L_k(p,0)>U_k(q,1)\) is incompatible with \(p\nmid n\), proving the bootstrap implication.

Every contact in the theorem's setting is even. Starting with \(q=2\), apply the implication successively along the consecutive primes
\[
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89.
\]
For \(k=8\), each of the twenty-three required inequalities is strict. Multiplying the positive denominators shows that the comparison for an adjacent pair \(q<p\) is equivalent to
\[
\left(\left(1+\frac1p\right)^8-1\right)\log q
>
\left(1-\left(1+\frac1q\right)^{-8}\right)\log p.
\]
The supplied verifier proves all twenty-three signs by rational interval bounds for the logarithms. It also proves the opposite sign for \(q=89,p=97\). Induction gives \(89\#\mid n\).

## Verification
The standalone verifier uses only exact rational arithmetic. It bounds every logarithm by the positive \(\operatorname{atanh}\)-series after exact dyadic range reduction; the omitted tail is bounded by a geometric series. It verifies all twenty-three positive adjacent-prime comparisons, the negative \(89\to97\) comparison, and the exact value of \(89\#\).

It also evaluates the paper's one-shot Corollary 3.10 threshold for \(89\#\). The relevant exponent-one ratio for the largest prime \(89\) lies strictly between \(180\) and \(181\), so that criterion gives order \(181\). At order \(8\), the same one-shot criterion certifies exponent-one divisibility only through the prime \(5\), whereas the bootstrap certifies every prime through \(89\).

## Relationship to prior work
Musin's Theorem 3.9 is the source of the two-sided order-dependent prime-exponent inequalities. Its Corollary 3.10 uses evenness and then replaces the tight upper bound by the coarse estimate \(\varepsilon<1/(k\log2)\), yielding a direct sufficient order for any prescribed divisor. The bootstrap above instead feeds each newly forced prime back into the sharper upper inequality and iterates; this is what lowers the universal certificate for \(89\#\) from order \(181\) to order \(8\).

Alaoglu and Erdős give the classical prime-increment description of colossally abundant maximizers, and classical colossally abundant numbers have an initial segment of the primes as support. Those facts do not by themselves produce an order-\(8\) universal lower bound on the support for every higher-order contact. The numerical first-contact data in arXiv:2609.33794v1 are family-specific; the present conclusion is uniform over every abscissa satisfying Theorem 3.9.

## Limitations
The endpoint \(89\) is sharp only for the stated adjacent-prime bootstrap at order \(8\): failure of the \(89\to97\) comparison does not prove that a level-\(8\) contact can omit \(97\). The argument does not optimize certificates using higher prime exponents or non-adjacent forcing paths, and it gives no asymptotic analysis of the bootstrap endpoint as \(k\to\infty\).

## References
1. O. R. Musin, *Higher-order colossally abundant numbers*, arXiv:2609.33794v1, 27 Sep 2026; especially Theorem 3.9, Corollary 3.10, and the prime-increment discussion.
2. L. Alaoglu and P. Erdős, *On highly composite and similar numbers*, Transactions of the American Mathematical Society 56 (1944), 448–469; especially Theorem 10.
3. OEIS A073751, classical colossally abundant prime-transition data; used only as a comparison table, not as evidence for the higher-order claim.
