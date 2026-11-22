# A complete five-adic valuation law for quartic Lucas-balancing window gcds

## Finding

For the Lucas-balancing numbers \(C_0=1\), \(C_1=3\), \(C_{n+2}=6C_{n+1}-C_n\), define the greatest common divisor of all translated quartic windows by
\[
G_4(k)=\gcd_{n\ge0}\left(\sum_{j=1}^{k}C_{n+j}^4\right),\qquad k\ge1.
\]
Then for every positive integer \(k\),
\[
\nu_5(G_4(k))=\begin{cases}
0,&5\nmid k,\\
1,&5\mid k\text{ and }3\nmid k,\\
\nu_5(k),&15\mid k.
\end{cases}
\]
The structural ingredient is an exact, all-moduli period/mean theorem. For each integer \(a\ge1\), the least period of \(C_n^4\pmod{5^a}\) is
\[
P_a=\begin{cases}1,&a=1,\\3\cdot5^{a-1},&a\ge2.\end{cases}
\]
For all \(s\ge0\) and all \(n\ge0\),
\[
\sum_{j=1}^{3\cdot5^s}C_{n+j}^4\equiv3\cdot5^s\pmod{5^{s+1}},
\]
so every such block has exact five-adic valuation \(s\).

## Assumptions and scope

All indices and window lengths are nonnegative and positive integers respectively. The valuation \(\nu_5(m)\) of a positive integer is its exponent of five. The GCD is taken over **all** translates, not a truncated numerical list. The theorem computes the five-primary part only, not the entire integer GCD.

## Proof

Put \(\alpha=3+2\sqrt2\), so \(\alpha^{-1}=3-2\sqrt2\) and
\[
C_n=\frac{\alpha^n+\alpha^{-n}}2.
\]
Work in the unramified quadratic five-adic integer ring \(\mathcal O=\mathbb Z_5[\sqrt2]\). This is unramified because \(2\) is a nonsquare modulo five. Set
\[
\gamma=-\alpha^3=-99-70\sqrt2=1+5u,
\qquad u=-20-14\sqrt2\equiv\sqrt2\pmod5.
\]
In particular, \(u\) is a unit. For \(r\in\{0,1,2\}\) and \(t\ge0\) write
\[
f_r(t)=C_{3t+r}^4=g_r(\gamma^t),\quad
 g_r(x)=\left(\frac{\alpha^r x+\alpha^{-r}x^{-1}}2\right)^4.
\]
The sign \((-1)^t\) relating \(\alpha^{3t}\) to \(\gamma^t\) disappears on taking fourth powers. Each \(g_r\) is an integral Laurent polynomial over \(\mathcal O\), since two is invertible.

First, every \(C_n\) is a unit modulo five and \(C_n^4\equiv1\pmod5\). Indeed \(\alpha^3\equiv-1\pmod5\), hence \(C_{3t+r}\equiv(-1)^t C_r\pmod5\) and \((C_0,C_1,C_2)\equiv(1,3,2)\). This proves that the least period modulo five is one.

Next, the first-order Taylor congruence \(\gamma^t\equiv1+5ut\pmod{25}\) yields
\[
f_r(t)\equiv C_r^4+5c_rt\pmod{25},\qquad
(c_0,c_1,c_2)=(0,2,3)\pmod5.
\]
To compute the slopes, set the balancing numbers \(B_r=(\alpha^r-\alpha^{-r})/(4\sqrt2)\), for which \(B_0=0,B_1=1,B_2=6\). At \(x=1\),
\[
 u xg_r'(x)\equiv16 C_r^3B_r\pmod5,
\]
which gives the three displayed pairwise distinct slopes. Thus a shift \(h\) that is a period of \(C_n^4\pmod{25}\) must preserve each residue class of \(n\) modulo three: otherwise, as \(t\) varies, it would identify two affine functions with different slopes modulo five. Consequently \(3\mid h\).

For a shift \(h=3q\), the \(r=1\) class is decisive. For every \(t,q\ge0\), the Laurent polynomial identity
\[
f_1(t+q)-f_1(t)=g_1(\gamma^t\gamma^q)-g_1(\gamma^t)
\]
and Taylor expansion in the increment \(\gamma^q-1\) give a first derivative which is a unit in \(\mathcal O\) modulo five; the higher terms have an extra factor of \(\gamma^q-1\). Hence
\[
\nu_5(f_1(t+q)-f_1(t))=\nu_5(\gamma^q-1)=1+\nu_5(q)
\]
for \(q\ge1\). The second equality is ordinary five-adic lifting for the principal unit \(\gamma=1+5u\) with \(u\) a unit. Conversely, \(\gamma^q\equiv1\pmod{5^a}\) implies that all three functions \(f_r(t)\) are fixed modulo \(5^a\). Therefore a shift is a period modulo \(5^a\), \(a\ge2\), if and only if \(3\cdot5^{a-1}\) divides it, proving the claimed least period.

To compute block sums, observe from the binomial theorem (or the five-adic lifting lemma) that, for every \(s\ge0\), \(j\in\{\pm2,\pm4\}\), and \(t_0\ge0\),
\[
\sum_{t=t_0}^{t_0+5^s-1}\gamma^{jt}\equiv5^s\pmod{5^{s+1}}.
\]
Indeed \(\gamma^j\in1+5\mathcal O\), and the geometric-series quotient is \(5^s\) times a principal unit congruent to one modulo five. The quartic expansion
\[
g_r(x)=\frac{\alpha^{4r}x^4+4\alpha^{2r}x^2+6+4\alpha^{-2r}x^{-2}+\alpha^{-4r}x^{-4}}{16}
\]
therefore implies
\[
\sum_{t=t_0}^{t_0+5^s-1}f_r(t)
\equiv5^s C_r^4\pmod{5^{s+1}}.
\]
Every window of length \(3\cdot5^s\) consists of exactly \(5^s\) consecutive terms from each of the three residue classes modulo three. Hence its sum is congruent to
\(5^s(C_0^4+C_1^4+C_2^4)\equiv3\cdot5^s\pmod{5^{s+1}}\).

Finally let \(S_n(k)=\sum_{j=1}^k C_{n+j}^4\). For each \(a\ge1\), the condition \(5^a\mid S_n(k)\) for every \(n\) implies, by subtracting adjacent windows,
\[
C_{n+k+1}^4\equiv C_{n+1}^4\pmod{5^a}\quad\text{for all }n\ge0,
\]
so \(k\) is a period of the quartic sequence modulo \(5^a\). For \(a=1\), all terms equal one and this condition is precisely \(5\mid k\). For \(a\ge2\), the period lemma forces \(k=m\cdot3\cdot5^{a-1}\). Break the window into \(m\) blocks of that length. Their sum is \(3m5^{a-1}\pmod{5^a}\). Thus
\[
5^a\mid G_4(k)\quad\Longleftrightarrow\quad3\cdot5^a\mid k\qquad(a\ge2).
\]
Combining this with the case \(a=1\) proves the three-branch valuation formula for all \(k\ge1\).

## Verification

The included `checker.py` independently verifies the fifth-order integral recurrence of the quartic sequence, exactly computes the GCD of the first five window sums for lengths one through 179 (five suffice because the window sums obey the same monic integer recurrence), tests prime-power periods through modulus \(5^5\), and confirms block congruences through length \(3\cdot5^3\). These finite calculations corroborate but do not replace the all-index five-adic proof above. Run with `python checker.py`; it requires Python 3 and SymPy.

## Relationship to prior work

Mbirika, Schrader and Spilker (2023) posed questions on GCDs of translated **squared** balancing and associated-sequence windows, motivating higher-power analogues. Rayaguru and Panda (2019) established quartic summation identities for balancing and Lucas-balancing numbers. The present statement is instead an exact five-adic classification of translated **quartic** Lucas-balancing windows, including sharp all-power periods and fixed block means; neither cited statement evaluates this invariant. Previously reported results for higher powers of the different balancing sequence concern the prime seventeen, and fourth-power Pell companion studies address primes two and three. These related objects and primes do not themselves imply the present five-primary formula; an earlier implicit derivation from general summation methods remains possible.

## Limitations

No other prime-primary part of \(G_4(k)\) is determined, and no claim of a complete integer factorization or independent validation is made. The originality comparison is limited by access to and indexing of the existing mathematical literature. A proof of this local theorem does not establish publication priority against all sources.

## References

1. A. Mbirika, J. Schrader and J. Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, 2023; arXiv:2301.05758, https://arxiv.org/abs/2301.05758. Full text: https://cs.uwaterloo.ca/journals/JIS/VOL26/Mbirika/mbir5.pdf.
2. S. G. Rayaguru and G. K. Panda, *Sum formulas involving powers of balancing and Lucas-balancing numbers – II*, Notes on Number Theory and Discrete Mathematics **25** (2019), 102–110, DOI:10.7546/nntdm.2019.25.3.102-110. Full text: https://nntdm.net/papers/nntdm-25/NNTDM-25-3-102-110.pdf.
