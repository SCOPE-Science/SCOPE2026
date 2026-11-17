# Three closure intervals and exact frequencies for reciprocal-square divisor sums on cube-free integers

## Finding
Let \(\mathcal C\) be the set of positive integers not divisible by a cube greater than one, and set \(f(n)=\sigma_{-2}(n)=\sum_{d\mid n}d^{-2}\). Then
\[
\overline{f(\mathcal C)}=
\left[1,\frac{9720}{91\pi^4}\right]
\cup\left[\frac{10}{9},\frac{120}{\pi^4}\right]
\cup\left[\frac54,\frac{315}{2\pi^4}\right].
\]
These are exactly three disjoint closed intervals. Among all positive integers, the cube-free integers whose \(f\)-values lie in the three respective intervals have natural densities
\[
\frac{36}{91\zeta(3)},\qquad \frac{16}{91\zeta(3)},\qquad \frac{39}{91\zeta(3)}.
\]
In particular, conditional on being cube-free, the three respective proportions are \(36/91\), \(16/91\), and \(39/91\).

## Assumptions and scope
The closure is in the real line. The ordinary reciprocal-square divisor sum is used, **not** the unitary or alternating divisor sum. Cube-free means that every prime exponent belongs to \(\{0,1,2\}\). For a prime \(p\) define
\[
F_p(0)=1,\quad F_p(1)=1+p^{-2},\quad
F_p(2)=1+p^{-2}+p^{-4}.
\]
Consequently \(f(n)=\prod_p F_p(\nu_p(n))\). The natural densities refer to all positive integers unless explicitly conditioned on cube-freeness.

## Proof
**1. The unrestricted tail of primes at least five is a full interval.** Write
\[
U=\prod_{p\ge5}F_p(2),\qquad
\mathcal T=\overline{\left\{\prod_{p\ge5}F_p(e_p):e_p\in\{0,1,2\},\text{ finitely many }e_p\ne0\right\}}.
\]
We first prove \(\mathcal T=[1,U]\). For every prime \(p\ge5\), show
\[
\prod_{q>p}F_q(2)\ \ge\ F_p(1)=1+p^{-2}. \tag{1}
\]
Let \(p_i\) be the \(i\)-th prime. Defant's Lemma 2.1 [1] proves \(p_{i+1}/p_i<\sqrt2\) whenever \(i\notin\{1,2,4\}\). Thus for \(p=p_i\ge11\), each \(p_{i+h}<2^{h/2}p_i\). It follows that
\[
\prod_{q>p}F_q(2)\ge\prod_{h\ge1}(1+p_{i+h}^{-2})
>1+\sum_{h\ge1}p_{i+h}^{-2}
>1+p_i^{-2}\sum_{h\ge1}2^{-h}=1+p_i^{-2}.
\]
For \(p=5\), the finite primes \(7,11,13,17,19\) suffice; for \(p=7\), the finite primes \(11,13,17,19,23\) suffice. Exact rational arithmetic gives the respective positive differences
\[
\prod_{q\in\{7,11,13,17,19\}}(1+q^{-2})-(1+5^{-2})
=\frac{213216438}{153732003425}>0,
\]
\[
\prod_{q\in\{11,13,17,19,23\}}(1+q^{-2})-(1+7^{-2})
=\frac{6767013150}{3252969192473}>0.
\]
Since each \(F_q(2)>1+q^{-2}\), (1) follows for all \(p\ge5\).

Here is a direct proof that (1) gives a full interval, including all endpoints. Work with logarithms and index the tail primes increasingly. For index \(i\), put \(a_i=\log F_{p_i}(1)\), \(b_i=\log F_{p_i}(2)\), and \(T_i=\sum_{j>i}b_j\). Condition (1) is \(T_i\ge a_i\), and the local digit increments obey \(b_i-a_i<a_i\), since \(F_p(2)<F_p(1)^2\).

Fix any \(x\in[0,\sum_i b_i]\). Choose at each prime the largest one of the three digits \(0,a_i,b_i\) not exceeding the remaining residual \(r\). Initially \(r\le b_i+T_i\) at the first prime. After selecting \(b_i\), the new residual is at most \(T_i\); after selecting \(a_i\), it is smaller than \(b_i-a_i<a_i\le T_i\); after selecting zero, it is smaller than \(a_i\le T_i\). Therefore the residual after the \(i\)-th prime is at most \(T_i\), which tends to zero. The finite partial choices yield cube-free integers with \(f\)-values tending to \(e^x\). All allowed products are bounded by \(U\), and thus \(\mathcal T=[1,U]\).

**2. The nine small-prime intervals merge into exactly three components.** Using the Euler product,
\[
\prod_pF_p(2)=\frac{\zeta(2)}{\zeta(6)}=\frac{315}{2\pi^4},\quad
F_2(2)=\frac{21}{16},\quad F_3(2)=\frac{91}{81},
\]
so
\[
U=\frac{315}{2\pi^4}\frac{16}{21}\frac{81}{91}
=\frac{9720}{91\pi^4}.
\]
The classical bound \(223/71<\pi<22/7\) implies
\[
\frac{109}{100}<U<\frac{11}{10}. \tag{2}
\]
For exponents \(a,b\in\{0,1,2\}\) at primes \(2,3\), the corresponding exact interval of possible closure-values is
\[
F_2(a)F_3(b)[1,U]. \tag{3}
\]
For \(a=b=0\), this gives \([1,U]\). For \(a=0\) and \(b\in\{1,2\}\), the two intervals meet because \((10/9)U>91/81\) (using \(U>91/90\)), and their union is
\[
\left[\frac{10}{9},\frac{91}{81}U\right]
=\left[\frac{10}{9},\frac{120}{\pi^4}\right].
\]
For \(a\in\{1,2\}\), the six starting points of (3), in increasing order, are
\[
\frac54,\quad\frac{21}{16},\quad\frac{25}{18},\quad
\frac{455}{324},\quad\frac{35}{24},\quad\frac{637}{432}.
\]
The lower bound in (2) shows that every interval overlaps the preceding one (even without enlarging to the running union). Their collective union is
\[
\left[\frac54,\frac{21}{16}\frac{91}{81}U\right]
=\left[\frac54,\frac{315}{2\pi^4}\right].
\]
The three blocks are genuinely separated: \(U<11/10<10/9\) and
\[
\frac{91}{81}U<\frac{91}{81}\frac{11}{10}<\frac54.
\]
This proves the exact closure identity and the component count.

**3. The component densities are exact.** For a prime \(p\) and nonnegative integer \(e\), the natural density of \(\nu_p(n)=e\) is \(p^{-e}-p^{-(e+1)}\). Standard finite-prime inclusion-exclusion, followed by the absolutely convergent bound \(\sum_{p>Y}p^{-3}\to0\), shows that the density of integers cube-free at all primes \(p\ge5\) is
\[
\prod_{p\ge5}(1-p^{-3})
=\frac{108}{91\zeta(3)}.
\]
By the disjoint interval decomposition just proved, the first, second, and third components correspond respectively to exponent pairs
\[
(\nu_2,\nu_3)=(0,0),\qquad
(\nu_2,\nu_3)\in\{(0,1),(0,2)\},\qquad
\nu_2\in\{1,2\},\ \nu_3\in\{0,1,2\}.
\]
Their local densities at \(2,3\) are, respectively, \(1/3\), \(4/27\), and \(13/36\). Multiplication by the preceding tail factor gives exactly
\[
\frac{36}{91\zeta(3)},\qquad
\frac{16}{91\zeta(3)},\qquad
\frac{39}{91\zeta(3)}.
\]
The sum is \(1/\zeta(3)\), the full cube-free density. Dividing through by this density gives the stated conditional proportions.

## Verification
Run `python3 verify.py` in the same directory. The program uses only exact integer and rational arithmetic. It checks the two exceptional-prime product inequalities, proves the coarse rational enclosure of \(U\) from the stated bounds for \(\pi\), checks all nine interval placements and the three component divisions, and confirms all three density identities. A successful run prints `VERIFY_OK`. The infinite prime-ratio input is explicitly taken from the published Lemma 2.1 of [1]; the finite checks do **not** certify that analytic lemma. The infinite greedy construction and density argument above are mathematical proofs, not extrapolations from a finite sample.

## Relationship to prior work
Defant [1] introduced generalized divisor sums on bounded-prime-exponent domains and proved exactly when the image is dense in its *entire* ambient Euler-product interval. His Section 3 expressly asks for the number of connected components when density fails; his Theorem 2.1 also supplies a related logarithmic greedy method. At the cube-free parameter \(r=2\), the new statement supplies the exact connected components, all endpoints and their natural densities, which do not follow from his yes/no full-interval-density theorem alone.

Sanna [2] determined for the **unrestricted** reciprocal-square divisor sum the three intervals \([1,\pi^2/9]\), \([10/9,\pi^2/8]\), \([5/4,\pi^2/6]\) and corresponding ordinary-integer frequencies \(1/3,1/6,1/2\). Here the input integers are required to be cube-free, changing all upper endpoints and all unconditional densities. The unrestricted result alone does not imply the tail-filling property for the restricted domain. Work on *unitary* or *alternating* divisor sums concerns a different local prime-power factor and does not entail this exact classification.

## Limitations
The classification is only for reciprocal-square sums on cube-free integers. No general formula for other exponents or other powers allowed in the domain is claimed; it also does not give the distribution of individual values inside each interval. Historical-priority uncertainty remains for unindexed or differently titled restricted-domain calculations. The argument relies on the published prime-ratio lemma, plus two exact finite rational checks, and does not claim independent reproof of that external analytic lemma.

## References
1. C. Defant, *On the Density of Ranges of Generalized Divisor Functions with Restricted Domains*, arXiv:1507.02663, first public version 2015-07-09, especially Theorem 2.1, Lemma 2.1, and Section 3. https://arxiv.org/abs/1507.02663
2. C. Sanna, *On the Closure of the Image of the Generalized Divisor Function*, arXiv:1507.08091, first public version 2015-07-29; later *Uniform Distribution Theory* 12 (2017), no. 2, 77–90. https://arxiv.org/abs/1507.08091
3. J. Nagura, *On the interval containing at least one prime number*, *Proceedings of the Japan Academy* 28 (1952), 177–181. Background prime-gap context; the explicit ratio input is credited to [1].
