# Exact seven-adic Pell residue fibers and a nested quadratic critical branch

## Finding

Define \(P_0=0\), \(P_1=1\), and \(P_{n+2}=2P_{n+1}+P_n\). For each \(k\ge1\), set \(T_k=6\cdot7^{k-1}\) and
\[
N_k(y)=\#\{0\le n<T_k:P_n\equiv y\pmod{7^k}\}.
\]
Put \(b(y)=2\) when \(y\equiv1\pmod7\), \(b(y)=1\) when \(y\equiv0,2,5\pmod7\), and \(b(y)=0\) otherwise. At depth one,
\[
N_1(y)=b(y)+\mathbf{1}_{y=5}.
\]
For \(k\ge2\), define the uniquely lifted root \(c_k\pmod{7^k}\) by \(2c_k^2\equiv1\pmod{7^k}\), \(c_k\equiv5\pmod7\), and \(d_k=c_k2^{-1}\pmod{7^k}\). For \(m\ge0\) write
\[
R_m(z)=\#\{u\pmod{7^m}:u^2\equiv z\pmod{7^m}\},\quad R_0(z)=1.
\]
Then the complete exact fiber law is
\[
N_k(y)=b(y)+\begin{cases}
7R_{k-2}\!\left(\dfrac{y-c_k}{49}d_k^{-1}\right),&y\equiv c_k\pmod{49},\\
0,&\text{otherwise}.
\end{cases}
\]
The quotient and inverse in the first branch are interpreted modulo \(7^{k-2}\). The least index period is \(T_k\), and the exact image is precisely all classes congruent to \(0,1,2,5\pmod7\). Its limit in \(\mathbb Z_7\) is the union of these four residue balls, of Haar measure \(4/7\). In particular, the full value frequency is not uniform: the exceptional square-root contribution is unbounded across prime-power depths.

## Assumptions and scope

All indices are nonnegative integers; all congruences and root counts are for the prime seven. The formula is exact for every integer \(k\ge1\) and every integer target \(y\) taken modulo \(7^k\), with the special depth-one convention above. A root count for \(m\ge1\) is \(7^{\lfloor m/2\rfloor}\) when \(z\equiv0\pmod{7^m}\), is \(2\cdot7^h\) when \(\nu_7(z)=2h<m\) and its unit part is a square modulo seven, and zero otherwise. There is no claim about ordinary integer-square values.

## Proof

**Period.** Let \(M=\begin{pmatrix}0&1\\1&2\end{pmatrix}\). Direct multiplication yields \(M^6=\begin{pmatrix}29&70\\70&169\end{pmatrix}=I+7A\), with \(A\not\equiv0\pmod7\). The first-coordinate recurrence state \((P_n,P_{n+1})\) has period six modulo seven and runs through six distinct nonzero states. The binomial expansion gives \((I+7A)^{7^j}\equiv I+7^{j+1}A\pmod{7^{j+2}}\) for \(j\ge0\), and its off-diagonal component is nonzero at exact valuation \(j+1\). Consequently, the state and the Pell sequence itself have least period \(6\cdot7^{k-1}\). For the scalar Pell sequence, two successive values recover the state, so their least periods coincide.

**Five regular index branches.** For each \(r=0,\ldots,5\), interpolate \(P_{r+6t}\) continuously on \(t\in\mathbb Z_7\) by \(M^{6t}=(I+7A)^t\), using the convergent binomial series. The residue values \(P_r\pmod7\) are respectively \((0,1,2,5,5,1)\). The normalized initial slopes \((P_{r+6}-P_r)/7\pmod7\) are \((3,3,2,0,2,4)\). On each of the five branches \(r\ne3\), the higher divided-difference terms are multiples of seven after normalizing by seven. Thus \(t\mapsto(P_{r+6t}-P_r)/7\) is a \(7\)-adic isometry and bijection of \(\mathbb Z_7\). For targets \(y\equiv P_r\pmod7\), this gives exactly one \(t\pmod{7^{k-1}}\) per target. Counting the five regular branches gives exactly \(b(y)\).

**One quadratic branch.** Put \(Q_n=(\alpha^n+\beta^n)/2\), \(\alpha=1+\sqrt2\), \(\beta=1-\sqrt2\). Then \(Q_n^2-2P_n^2=(-1)^n\). For \(n=3+6t\) (always odd), the identity becomes \(2P_n^2=1+Q_n^2\). Moreover \(Q_3=7\), so \(Q_{3+6t}\in7\mathbb Z_7\) for every \(t\in\mathbb Z_7\). As \(\sqrt2\in\mathbb Z_7\) (Hensel's lemma), the same interpolation defines \(Q_{3+6t}\). Its normalized derivative at every \(t\), divided by seven, is a unit modulo seven; equivalently, \(t\mapsto Q_{3+6t}/7\) is a \(7\)-adic isometry and bijection. This follows directly from the matrix step \(M^6=I+7A\), the value \(Q_3=7\), and the nonzero reduced difference \((Q_9-Q_3)/7\pmod7\).

Let \(c\in\mathbb Z_7\) be the unique root \(2c^2=1\) with \(c\equiv5\pmod7\). On the critical branch \(P_{3+6t}\equiv5\pmod7\), hence the uniquely chosen square root gives
\[
P_{3+6t}=c\sqrt{1+Q_{3+6t}^2}.
\]
Define \(U(q)=\sqrt{2/(1+\sqrt{1+q^2})}\) for \(q\in7\mathbb Z_7\), with roots congruent to one modulo seven. The identity \(\sqrt{1+q^2}-1=q^2/(1+\sqrt{1+q^2})\) yields
\[
P_{3+6t}=c+49(c/2)\,u(t)^2,\qquad
u(t)=\frac{Q_{3+6t}}{7}\,U(Q_{3+6t}).
\]
Since \(U(q)\equiv1\pmod7\) and its higher derivatives carry extra factors of seven on \(q\in7\mathbb Z_7\), \(u(t)\) remains an isometry/bijection of \(\mathbb Z_7\). The congruence \(c\equiv5\pmod49\) follows from the uniquely lifted equation \(2c^2=1\). Thus for \(k\ge2\) the singular branch produces solutions only when \(y\equiv c_k\pmod49\), and each solution \(u\pmod{7^{k-2}}\) lifts to exactly seven inputs \(t\pmod{7^{k-1}}\), giving the asserted \(7R_{k-2}\) term. For \(k=1\) it supplies one extra index at residue five.

**Image and density.** Each of the four residue classes \(0,1,2,5\pmod7\) already has a regular isometric branch and hence is filled at every prime-power depth. The singular branch maps only into the fifth residue class and cannot create additional residue classes. Therefore the image and its four-ball closure, and the measure \(4/7\), follow. The square-root count at the central value \(y=c_k\) grows with depth, proving the claimed unbounded multiplicity.

## Verification

Run the standalone script `VERIFY.py` with Python 3. It checks the lifted root, the exact period, and every fiber at depths one through five by direct modular recurrence and a separate modular square-root counter. The total checked indices across these five periods is \(16806\). These finite calculations are regression checks; the proof of the all-depth theorem is the preceding isometry and quadratic normal-form argument.

## Relationship to prior work

Lang and Lang (arXiv:1307.7463, first publicly posted 2013-07-29), sections 4.4 and 5, establish non-residue-completeness of Pell numbers modulo seven and classify complete-residue moduli, but do not determine all prime-power fiber multiplicities, the precise four-ball image, or the singular square-root correction. Related studied sequences include Pell numbers modulo thirteen, Pell–Lucas numbers modulo two, and classical Fibonacci/Lucas numbers modulo seven; these are not the same Pell value distribution at seven. The analytic isometry and square-normal-form method is not asserted to be new in general.

## Limitations

Only the prime seven and classical Pell normalization are covered. The proof does not imply new global perfect-power results or claims of a general formula at other primes. Historical priority remains subject to discovery of stronger general results on Lucas-recursion local fibers; no independent mathematical audit is represented.

## References

- C. L. Lang and M. L. Lang, *Three term recurrence and residue completeness*, arXiv:1307.7463v1 (2013-07-29), https://arxiv.org/abs/1307.7463.
- Classical Hensel lifting and Pell identities, used as standard elementary tools.
