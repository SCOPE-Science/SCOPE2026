# Exact binary and ternary divisibility of Padovan square-window GCDs

## Finding
Let \(P_0=P_1=P_2=1\) and \(P_{n+3}=P_{n+1}+P_n\) for every \(n\geq0\). For every integer \(k\geq1\), set
\[
G(k)=\gcd\left\{\sum_{j=0}^{k-1}P_{n+j}^{2}:n\geq0\right\}.
\]
Then the exact local factors of this integer at the first two primes are
\[
\boxed{\nu_2(G(k))=\begin{cases}2+\nu_2(k),&7\mid k,\\0,&7\nmid k,\end{cases}}
\qquad
\boxed{\nu_3(G(k))=\begin{cases}1+\nu_3(k),&13\mid k,\\0,&13\nmid k.\end{cases}}
\]
Here \(\nu_p\) is the exponent of the prime \(p\) in a nonzero integer. Equivalently, the least periods of \((P_n^2)_{n\ge0}\) modulo prime powers are, for every integer \(r\geq1\),
\[
\pi_{P^2}(2^r)=\begin{cases}7,&r=1,2,\\7\cdot2^{r-2},&r\ge3,\end{cases}
\qquad
\pi_{P^2}(3^r)=13\cdot3^{r-1}.
\]
In particular, squaring the Padovan terms removes one binary period-doubling level from every modulus \(2^r\) with \(r\geq2\), but causes no analogous loss at powers of three.

## Assumptions and scope
The recurrence is the standard Padovan indexing beginning with three ones. The window length \(k\) and the precision exponent \(r\) are arbitrary positive integers. The gcd of infinitely many positive integers is their greatest positive common divisor, which exists because the first member is nonzero. The theorem computes **only** the \(2\)-primary and \(3\)-primary factors of \(G(k)\), not the entire prime factorization or periods at other primes. No asymptotic or probabilistic assumption is involved.

## Proof
**1. An integral recurrence for squared Padovan terms.** Write \(u_n=P_n^2\) and let \(E\) denote the left shift in \(n\). The characteristic polynomial of the Padovan recurrence is \(f(X)=X^3-X-1\). Passing to the symmetric square, the six characteristic multipliers are the three squared roots and the three pairwise products. Their integral annihilator is
\[
Q(X)=(X^3+X^2-1)(X^3-2X^2+X-1)
=X^6-X^5-X^4-X^3+X^2-X+1.
\]
Indeed the pairwise products of roots of \(f\), whose product is one, are the reciprocals of its roots and satisfy the first cubic; the squared roots satisfy the second cubic (or verify by eliminating \(\alpha^3=\alpha+1\)). The symmetric-square construction remains valid without diagonalizing over a finite field because the identity holds over the integers. Thus \(Q(E)u_n=0\) for all \(n\geq0\). Crucially, \(Q(1)=-1\).

Let \(W_n(k)=\sum_{j=0}^{k-1}u_{n+j}\). It satisfies \(Q(E)W_n(k)=0\) and
\[
W_{n+1}(k)-W_n(k)=u_{n+k}-u_n.
\]
For any modulus \(m\geq2\), if every \(W_n(k)\) is zero modulo \(m\), then \(u_{n+k}=u_n\) for every \(n\). Conversely if \(u_{n+k}=u_n\) for all \(n\), the window sums are constant modulo \(m\); applying \(Q(E)\) gives \(0=Q(1)W_n(k)=-W_n(k)\), so they are all zero. Therefore
\[
m\mid G(k)\quad\Longleftrightarrow\quad k\text{ is a period of }(u_n\bmod m).
\]
An ordinary least period exists for each modulus because the Padovan state transition is invertible, with determinant one. It divides any other period. Also the gcd across all windows equals the gcd of the first six windows, since \(Q(E)W=0\) is a monic sixth-order integer recurrence.

**2. Exact binary periods.** The state vector \(v_n=(P_n,P_{n+1},P_{n+2})^{\mathsf T}\) evolves by
\[
v_{n+1}=Av_n,\qquad
A=\begin{pmatrix}0&1&0\\0&0&1\\1&1&0\end{pmatrix},\qquad v_0=(1,1,1)^{\mathsf T}.
\]
Direct exact matrix multiplication gives \(A^7\equiv I\pmod2\) and \(A^{14}=I+4B\), where
\[
B\equiv\begin{pmatrix}0&0&1\\1&1&0\\0&1&1\end{pmatrix}\pmod2.
\]
The squared sequence is nonconstant modulo two, so its least period there is seven. Since \(A^7\equiv I\pmod2\), every \(P_{n+7}-P_n\) is even, making \(u_{n+7}-u_n\) divisible by four. Therefore its period modulo four is seven as well. The shift by fourteen is a period modulo eight since \(A^{14}\equiv I\pmod4\); the shift by seven is not, as
\[
u_{10}-u_3=12^2-2^2=140\equiv4\pmod8.
\]
Thus the least period modulo eight is fourteen.

For arbitrary \(s\geq1\) and odd \(m\geq1\), the standard binomial lifting of the integer matrix \(I+4B\) yields
\[
A^{7\cdot2^s m}=I+2^{s+1}mB+2^{s+2}C_{s,m}
\]
for an integral matrix \(C_{s,m}\). At index \(n\), subtracting first coordinates and squaring gives
\[
u_{n+7\cdot2^sm}-u_n\equiv
2^{s+2}m P_n(Bv_n)_1\pmod{2^{s+3}}.
\]
At \(n=0\), both \(P_0\) and \((Bv_0)_1\) are odd. Hence this period shift is valid modulo \(2^{s+2}\) for every index but fails modulo \(2^{s+3}\) at index zero. For odd multiples of seven, the modulo-eight witness above remains nonzero because fourteen is already a period modulo eight. Combining these observations with the period-seven base case establishes all claimed binary periods and the exact binary GCD valuation.

**3. Exact ternary periods.** Direct multiplication gives \(A^{13}=I+3C\) with
\[
C\equiv\begin{pmatrix}2&1&0\\0&2&1\\1&1&2\end{pmatrix}\pmod3.
\]
The squared sequence is nonconstant modulo three (\(u_0=1\), while \(u_5=9\)), so the least ternary period at precision one is thirteen. For every \(s\geq0\) and positive \(m\) with \(3\nmid m\), binomial lifting gives
\[
A^{13\cdot3^sm}=I+3^{s+1}mC+3^{s+2}D_{s,m}
\]
with \(D_{s,m}\) integral, hence
\[
u_{n+13\cdot3^sm}-u_n\equiv
2\cdot3^{s+1}mP_n(Cv_n)_1\pmod{3^{s+2}}.
\]
At \(n=2\), \(v_2=(1,2,2)^{\mathsf T}\), so \(P_2=1\) and \((Cv_2)_1\equiv2+2\equiv1\pmod3\). Therefore the shift has exact uniform divisibility precision \(3^{s+1}\): it is a period at that precision and not at the next. Together with the prime base period thirteen this proves the exact ternary period and the corresponding valuation formula. \(\square\)

## Verification
The accompanying standalone `check.py` uses direct integer Padovan generation and exact arithmetic, independently of the symbolic argument, to test the annihilating recurrence at 400 indices, the lifting matrices and witnesses, all six initial square-window sums for each length \(1\leq k\leq360\), and every index of the predicted minimal cycles at binary precisions \(1\leq r\leq8\) and ternary precisions \(1\leq r\leq6\). These are finite corroborations of the all-index proof, not substitutes for it. `CHECKS.txt` records the actual completed run.

## Relationship to prior work
Guyer and Mbirika, first publicly posted April 25, 2021, provide a motivating GCD/period framework for sums of *unsquared* second-order generalized Fibonacci sequences. Their proofs and the inspected journal text do not cover this squared third-order Padovan recurrence. The ordinary Padovan sequence and its modular periods have been studied by Taş and Karaduman (2014). Published work on ordinary Padovan orbits modulo powers of two and on sliding square-window gcds of other recurrence families concerns different objects; neither implies the exact two-prime Padovan-square result without additional structural calculations. The present proof explicitly exhibits those calculations and the exceptional binary cancellation caused by squaring.

## Limitations
No statement is made about primes other than two and three, about other initial seeds, or about higher powers of Padovan terms. A complete bibliography of implicit symmetric-square recurrence consequences is not available, so a logically equivalent result may exist elsewhere; the originality assessment is limited to identified accessible sources and relevant indexed records. Independent mathematical validation has not been performed.

## References
1. D. Guyer and aBa Mbirika, *GCD of sums of \(k\) consecutive Fibonacci, Lucas, and generalized Fibonacci numbers*, arXiv:2104.12262, version 1 publicly submitted April 25, 2021; *Journal of Integer Sequences* **24** (2021), Article 21.9.8. https://arxiv.org/abs/2104.12262 ; https://cs.uwaterloo.ca/journals/JIS/VOL24/Mbirika/mb5.pdf .
2. S. Taş and E. Karaduman, *The Padovan sequences in finite groups* (2014), https://www.thaiscience.info/journals/Article/CMJS/10932734.pdf .
3. *Exact zero-hit variance for primitive Padovan orbits modulo powers of two*, published mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-zero-hit-variance-for-primitive-padovan-orbits-modulo-powe--3b25687bed0c . (Indexed summary consulted; complete GitHub content was not accessible.)
4. *Exact sliding-square GCDs for the Jacobsthal companion pair*, published mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-sliding-square-gcds-for-the-jacobsthal-companion-pair--91949360d442 . (Indexed summary consulted; complete GitHub content was not accessible.)
