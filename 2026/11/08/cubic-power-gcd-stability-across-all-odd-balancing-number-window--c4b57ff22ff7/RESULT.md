# Cubic-power GCD stability across all odd balancing-number windows

## Finding
Let \(B_0=0\), \(B_1=1\), and \(B_{t+2}=6B_{t+1}-B_t\) for every integer \(t\ge0\). For every integer \(m\ge1\), define \(k=2m-1\) and \(g=B_m+B_{m-1}\). Then
\[
\gcd_{n\ge0}\left(\sum_{j=1}^{k}B_{n+j}^{3}\right)=g.
\]
Equivalently this gcd is the associated Pell number \(Q_k\), with \(Q_0=Q_1=1\) and \(Q_{t+2}=2Q_{t+1}+Q_t\). Thus the GCD of every odd-length window of *cubes* equals the known GCD of the corresponding windows of first powers. This is a statement for every odd positive window length, not merely an asymptotic or experimentally sampled pattern.

## Assumptions and scope
All sequences and gcds are over ordinary integers. The gcd of an infinite sequence of positive integers means their positive common greatest divisor. Initial windows begin at \(B_1\), and all starting indices \(n\ge0\) are included. No assertion is made for even window length, exponent five, or a generic Lucas sequence. The contrast with exponent seven is explicit: at \(k=3\), the gcd of the seventh-power windows is \(49\), rather than \(7\).

## Proof
Set \(\alpha=3+\sqrt8\), \(\beta=3-\sqrt8=\alpha^{-1}\), and \(s=n+m\). The Binet formula \(B_t=(\alpha^t-\beta^t)/(\alpha-\beta)\) implies
\[
B_{3t}=32B_t^3+3B_t.
\]
For \(r\in\{1,3\}\), let \(D_r=\sum_{j=1-m}^{m-1}\alpha^{rj}\). Symmetry under \(\alpha\leftrightarrow\beta\) gives the same sum with \(\beta\) substituted. A geometric sum or the odd-indexed associated-Pell identity gives \(D_1=g\) and
\[
\frac{D_3}{D_1}=\frac{\alpha^k+\beta^k+1}{\alpha+\beta+1}
 =\frac{4g^2+3}{7}.
\]
For completeness, \(g=(\alpha^{k/2}-\beta^{k/2})/(\alpha^{1/2}-\beta^{1/2})\), and thus \(\alpha^k+\beta^k=4g^2+2\). In the expressions involving square roots, take the positive real square roots of the positive \(\alpha\) and \(\beta\).

Summing the cubes by the Binet formula and using \(B_{3s}=32B_s^3+3B_s\) yields the exact identity
\[
7\sum_{j=1}^{2m-1}B_{n+j}^3 = g\,f_g(B_s),\qquad
f_g(z)=(4g^2+3)z^3+\frac{3(g^2-1)}8z.
\tag{1}
\]
We show that the greatest common divisor of \(f_g(B_s)\) for \(s\ge m\) is exactly \(7\).

First, \(g\equiv(-1)^{m-1}\pmod8\), proved from the recurrence with \(g_1=1\), \(g_2=7\); hence \(g^2\equiv1\pmod{16}\), so \(H=3(g^2-1)/8\) is an integer, and \(f_g(z)=Az^3+Hz\) lies in \(\mathbb Z[z]\), where \(A=4g^2+3\). Modulo \(7\), the balancing sequence cycles through \(0,1,-1\), and the \(g\)-sequence cycles through \(1,0,-1\). If \(g^2\equiv1\pmod7\), then \(A\equiv H\equiv0\pmod7\). Otherwise \(g^2\equiv0\pmod7\) and \(f_g(z)\equiv3z(z^2-1)\pmod7\). In either case
\[
7\mid f_g(B_s)\quad\text{for every integer }s\ge0.
\tag{2}
\]

It remains to rule out every additional common prime factor. At \(B_1=1\) and \(B_2=6\),
\[
f_g(1)=A+H=\frac{7(5g^2+3)}8,\qquad f_g(6)=6(36A+H),
\]
and \(3A-32H=21\). The first value is odd since \(g^2\equiv1\pmod{16}\), not divisible by \(3\) since the \(g\)-sequence modulo \(3\) is \(1,1,-1,-1\), and not divisible by \(5\) since it is \(2\pmod5\). Its \(7\)-adic valuation is exactly one: \(g^2\equiv0\) or \(1\pmod7\) makes \(5g^2+3\not\equiv0\pmod7\). If a prime \(p\ge11\) divided both displayed values, then \(p\nmid6\) and subtracting the two linear expressions would yield \(35A\equiv0\pmod p\), hence \(A\equiv H\equiv0\pmod p\). This contradicts \(3A-32H=21\). Consequently,
\[
\gcd(f_g(B_1),f_g(B_2))=7.
\tag{3}
\]

For every modulus \(d\ge1\), the state transition \((B_{t+1},B_t)\mapsto(6B_{t+1}-B_t,B_{t+1})\) is invertible modulo \(d\) (determinant \(1\)). Its finite orbit therefore is purely periodic. In particular, both residues \(B_1\) and \(B_2\) recur at arbitrarily large indices modulo \(d\). Take \(d=\gcd_{s\ge m}f_g(B_s)\). Periodicity forces \(d\) to divide both values in (3), and (2) forces \(7\mid d\). Thus \(d=7\). Taking the gcd of (1) over every \(n\ge0\) gives the result after cancelling \(7\).

Finally, the identity \(g=Q_{2m-1}\) follows since both sequences, indexed by \(m\), start \(1,7\) and satisfy \(g_{m+2}=6g_{m+1}-g_m\), as do the odd-indexed associated Pell numbers.

## Verification
Run \(\texttt{python3 check_cubic_balancing.py}\) using the supplied standalone checker. The output in \(\texttt{checks.json}\) records 70 independent window-length parameters, 910 exact cube-window identity checks, and 70 checks that \(\gcd(f_g(1),f_g(6))=7\). It also checks the analytic \(D_3\) coefficient recurrence and confirms the exponent-seven contrasting example \(49\) at length three. This finite evidence checks algebra and implementation but does **not** certify the infinite theorem; equations (1)–(3) and the modular periodicity argument supply that proof.

## Relationship to prior work
Mbirika, Schrader, and Spilker [1] prove an odd-window gcd formula for *first* powers of balancing numbers, with value \(Q_k\); their study of higher powers reports partial results for squares, not the exact cubic formula here. Rayaguru and Panda [2] give formulas for sums of powers, including cubes, but do not determine the infinite gcd over all starting indices or the prime-seven primitive content in (1). Kang [3] obtains related polynomial power-sum divisibility properties, not this odd-window gcd formula. The new statement is not a claim that the Binet identity, recurrence, or linear gcd formula is novel; the contribution is the exact cubic all-window GCD and its prime-content proof.

## Limitations
The theorem concerns only cubic powers and odd-length consecutive windows in the specified balancing sequence. Some other odd exponents behave differently; seventh powers at length three give gcd \(49\), not \(7\). An exhaustive review of every unpublished source cannot be guaranteed, and no independent scientific audit is asserted.

## References
1. aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, Journal of Integer Sequences 26 (2023), Article 23.6.4; preprint arXiv:2301.05758, first publicly posted 2023-01-13. https://arxiv.org/abs/2301.05758 ; https://cs.uwaterloo.ca/journals/JIS/VOL26/Mbirika/mbir5.pdf
2. D. Rayaguru and G. K. Panda, *Sum formulas involving powers of balancing and Lucas-balancing numbers – II*, Notes on Number Theory and Discrete Mathematics 25 (2019), 102–110. https://nntdm.net/papers/nntdm-25/NNTDM-25-3-102-110.pdf
3. W. Kang, *The power sum of balancing polynomials and their divisible properties*, AIMS Mathematics 9 (2024), 2684–2694. https://www.aimspress.com/aimspress-data/math/2024/2/PDF/math-09-02-133.pdf
