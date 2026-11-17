# Exact GCDs of consecutive squared cobalancing numbers

## Finding

Let the Pell and associated Pell numbers satisfy
\[
P_0=0,\quad P_1=1,\quad P_{n+2}=2P_{n+1}+P_n,
\qquad
Q_0=Q_1=1,\quad Q_{n+2}=2Q_{n+1}+Q_n.
\]
The cobalancing numbers use the indexing
\[
b_0=b_1=0,\qquad b_{n+2}=6b_{n+1}-b_n+2.
\]
For each positive integer \(k\), define the infinite-shift GCD
\[
\mathcal B_2(k)=\gcd_{n\ge0}\left(\sum_{j=1}^{k}b_{n+j}^{\,2}\right).
\]
Define the integer
\[
D_k=\begin{cases}
 Q_k\gcd\!\left(7,\dfrac{3P_k-1}{2}\right),&k\text{ odd},\\[5pt]
 \dfrac{P_k}{2}\gcd\!\left(14,\dfrac{Q_k-1}{2}\right),&k\text{ even}.
\end{cases}
\]
**Theorem.** For every integer \(k\ge1\),
\[
\boxed{\mathcal B_2(k)=4\gcd\!\left(D_k,\frac{5k}{2^{\mathbf 1_{2\mid k}}}\right).}
\]
Equivalently, the auxiliary factor has the explicit residue-class description
\[
D_k=\begin{cases}
7^{\mathbf{1}_{3\mid k}}Q_k,&k\text{ odd},\\[3pt]
2^{\mathbf{1}_{4\mid k}}7^{\mathbf{1}_{3\mid k}}\,P_k/2,&k\text{ even}.
\end{cases}
\]
Here \(\mathbf{1}_E\) equals one if \(E\) holds and zero otherwise. Sample values are
\[
\mathcal B_2(4)=8,\quad \mathcal B_2(6)=20,\quad
\mathcal B_2(12)=120,\quad \mathcal B_2(21)=28,\quad
\mathcal B_2(30)=100.
\]
This determines the previously open exact squared-cobalancing GCD at every window length, including all exceptional powers of \(2\) and \(7\).

## Assumptions and scope

All variables \(n\) and \(k\) in the GCD definition are integers with \(n\ge0\) and \(k\ge1\). GCDs are positive GCDs in \(\mathbb Z\). The indexing of \(b_n\) is the one in Definition 7 and Convention 1 of Mbirika--Schrader--Spilker (2023). In particular, \(b_1=0\), whereas \(b_2=2\). No assumptions on primality or parity of \(k\) are hidden. All identities use ordinary exact integers.

## Proof

### 1. Normalization and the difference GCD

Write \(u_n=b_n/2\) and \(a_n=u_n^2\). Recurrence and initial values give
\[
u_0=u_1=0,\qquad u_{n+2}=6u_{n+1}-u_n+1,
\qquad u_n=\frac{P_{2n-1}-1}{4}\quad(n\ge1),
\]
where the identity follows by checking the initial values and the common recurrence; extend \(P_{-1}=1\) when needed. Thus \(b_n^2=4a_n\). Put
\[
S_k(n)=\sum_{j=1}^k a_{n+j},\qquad
E_k=\gcd_{n\ge0}(a_{n+k}-a_n).
\]
(The symbol \(E_k\) is used only inside this proof; it will equal \(D_k\).)
The elementary sliding-window identity and the GCD-of-differences rule give
\[
\gcd_{n\ge0}S_k(n)
=\gcd\left(S_k(0),\gcd_{n\ge1}(a_{n+k}-a_n)\right).
\tag{1}
\]

For Pell numbers use
\[
P_{2j}=2P_jQ_j,\qquad
Q_{2j}=2Q_j^2-(-1)^j,\qquad
Q_j^2-2P_j^2=(-1)^j.
\tag{2}
\]
We will show that the last inner GCD in (1) equals \(D_k\), with the same result if its starting index is zero.

Suppose first that \(k\) is odd and put \(s=P_k\). The Pell addition identities, with \(t=n+(k-1)/2\), give
\[
a_{n+k}-a_n
=Q_k f_t(s),\qquad
f_t(s)=\frac{P_{2t}(sQ_{2t}-1)}4
=\frac{sP_{4t}-2P_{2t}}8.
\tag{3}
\]
The sequence \(t\mapsto f_t(s)\) is integral. It obeys the integer recurrence with characteristic polynomial
\[
(X^2-6X+1)(X^2-34X+1)
=X^4-40X^3+206X^2-40X+1.
\tag{4}
\]
Because the polynomial is monic with unit constant term, the GCD of any four successive values equals the GCD of the entire forward and backward sequence; in particular, it does not change on shifting the starting index. The first four values are
\[
f_0=0,\quad f_1=\frac{3s-1}{2},\quad
f_2=3(17s-1),\quad f_3=\frac{35(99s-1)}{2}.
\]
Since \(f_2-34f_1=14\), their GCD divides \(14\). For odd \(k\), \(P_k\equiv1\pmod4\), making \(f_1\) odd. Thus the GCD divides \(7\). If \(7\mid f_1\), all four displayed terms are divisible by \(7\). Therefore
\[
\gcd_t f_t(s)=\gcd\!\left(7,\frac{3P_k-1}{2}\right).
\tag{5}
\]

Suppose next that \(k\) is even and put \(r=Q_k\), \(z=(r-1)/2\). Pell addition identities now give, for \(t=n+(k-2)/2\),
\[
a_{n+k}-a_n=\frac{P_k}{2}h_t(r),\qquad
h_t(r)=\frac{Q_{2t+1}(rP_{2t+1}-1)}2
=\frac{rP_{4t+2}-2Q_{2t+1}}4.
\tag{6}
\]
This integral sequence obeys the same recurrence (4). Its first four terms are
\[
h_0=z,\quad h_1=35z+14,\quad
h_2=1189z+574,\quad h_3=40391z+20076.
\]
The identity \(h_1-35h_0=14\) shows that their GCD divides \(\gcd(z,14)\); conversely all four terms are divisible by \(\gcd(z,14)\), since \(574=14\cdot41\) and \(20076=14\cdot1434\). Hence
\[
\gcd_t h_t(r)=\gcd\!\left(14,\frac{Q_k-1}{2}\right).
\tag{7}
\]
Equations (3)--(7), together with shift invariance, prove
\[
E_k=\gcd_{n\ge1}(a_{n+k}-a_n)=D_k.
\tag{8}
\]
The equivalent residue-class description of \(D_k\) follows from the Pell recurrences modulo \(4\), \(7\), and \(14\): for odd \(k\), \(P_k\equiv5\pmod7\) precisely when \(3\mid k\); for even \(k\), \(Q_k\equiv1\pmod4\) precisely when \(4\mid k\), and \(Q_k\equiv1\pmod7\) precisely when \(3\mid k\). The sequences modulo \(7\) repeat after six indices, a fact also checked directly from the initial recurrence states.

### 2. Exact initial sum and odd-prime valuations

The Pell identities imply, for odd integers \(j\), \(P_j^2=(Q_{2j}+1)/4\). Telescoping via
\[
P_{2j}-P_{2j-2}=2P_{2j-1},\qquad
P_{4j}-P_{4j-4}=4Q_{4j-2},
\]
gives
\[
S_k(n)=\frac{P_{4(n+k)}-P_{4n}-16(P_{2(n+k)}-P_{2n})+20k}{256}.
\tag{9}
\]
At \(n=0\), double-angle identities simplify this to
\[
64S_k(0)=P_kQ_k(Q_{2k}-8)+5k.
\tag{10}
\]
We claim \(D_k\mid P_kQ_k(Q_{2k}-8)\). For odd \(k\), the only factor in \(D_k/Q_k\) is possibly \(7\). If it occurs, \(P_k\equiv5\pmod7\); by \(Q_k^2-2P_k^2=-1\), \(7\mid Q_k\), and \(Q_{2k}-8=2Q_k^2-7\) is divisible by \(7\). For even \(k\), the possible extra factors in \(D_k/(P_k/2)\) divide \(14\). The factor \(2\) is already present in \(P_k\). An extra factor \(7\) forces \(Q_k\equiv1\pmod7\), and hence \(Q_{2k}-8=2Q_k^2-9\equiv0\pmod7\). This proves the claim and yields
\[
64S_k(0)\equiv5k\pmod{D_k}.
\tag{11}
\]
Consequently, for every **odd** prime \(p\), the powers of \(p\) in
\(\gcd(D_k,S_k(0))\) agree exactly with those in \(\gcd(D_k,5k)\).

### 3. The exact power of two

If \(k\) is odd, \(D_k\) is odd. If \(k\equiv2\pmod4\), \(D_k\) is also odd, since \(\nu_2(P_k)=\nu_2(k)\) and the small factor in (7) is odd. Thus it remains to treat \(4\mid k\).

We establish the following dyadic lemma for the affine recurrence \(u_n\): for every \(r\ge2\) and \(n\ge0\),
\[
u_{n+2^r}-u_n\equiv2^{r-1}\pmod{2^r}.
\tag{12}
\]
For \(r=2\), both \(u_4-u_0=42\) and \(u_5-u_1=246\) are congruent to \(2\pmod4\). Their difference sequence satisfies the homogeneous recurrence with matrix
\[
A=\begin{pmatrix}6&-1\\1&0\end{pmatrix},\qquad A^4\equiv I\pmod4,
\]
so (12) holds for all \(n\). For induction, set \(h=2^r\) and \(d_n=u_{n+h}-u_n\). The induction hypothesis says all \(d_n\) are \(2^{r-1}\) modulo \(2^r\). The homogeneous recurrence and \(A^h\equiv I\pmod4\) therefore imply \(d_{n+h}\equiv d_n\pmod{2^{r+1}}\). Thus
\(u_{n+2h}-u_n=d_{n+h}+d_n\equiv2^r\pmod{2^{r+1}}\), completing the induction.

Write \(V(h)=\sum_{j=1}^h u_j^2\). We next prove, for every \(r\ge2\),
\[
V(2^r)\equiv2^{r-1}\pmod{2^r}.
\tag{13}
\]
The initial value is \(V(4)=1814\equiv2\pmod4\). Put \(h=2^r\), \(d_j=u_{j+h}-u_j\), and use (12) to expand the difference of the two halves:
\[
V(2h)-2V(h)=\sum_{j=1}^h(2u_jd_j+d_j^2)
\equiv2^r\sum_{j=1}^h u_j+h\,2^{2r-2}\pmod{2^{r+1}}.
\]
The parity pattern of \(u_j\) is \(0,1,1,0\), repeated every four indices; hence \(\sum_{j=1}^{2^r}u_j\) is even. The second displayed term is also divisible by \(2^{r+1}\). Therefore \(V(2h)\equiv2V(h)\pmod{2^{r+1}}\), proving (13) inductively.

Now write \(k=2^r m\), with \(r\ge2\) and \(m\) odd. Equation (12) implies \(u_{j+2^r}^2\equiv u_j^2\pmod{2^r}\). Partitioning the sum into \(m\) blocks of length \(2^r\) gives
\[
S_k(0)\equiv mV(2^r)\equiv2^{r-1}\pmod{2^r}.
\tag{14}
\]
Hence \(\nu_2(S_k(0))=r-1\). Meanwhile \(\nu_2(P_k)=\nu_2(k)=r\), by repeated application of \(P_{2j}=2P_jQ_j\) and the oddness of every \(Q_j\); the extra factor in \(D_k\) is \(2\) when \(4\mid k\), so \(\nu_2(D_k)=r\). Thus
\[
\nu_2(\gcd(D_k,S_k(0)))=r-1
=\nu_2\!\left(\gcd(D_k,5k/2)\right).
\tag{15}
\]
The odd-prime comparison (11), together with the trivial odd cases and (15), proves
\(\gcd(D_k,S_k(0))=\gcd(D_k,5k/2^{\mathbf{1}_{2\mid k}})\). Substitute into (1) and (8), then multiply by \(4\), completing the theorem.

## Verification

A standalone Python 3 checker `verify_cobalancing.py`, requiring only the standard library, independently generates the cobalancing recurrence, Pell recurrences, shifted sums, and finite-shift difference GCDs. Executing `python3 verify_cobalancing.py` produced:

```text
VERIFY_OK k=1..500 gcd_windows=6000 gcd_differences=6000
PELL_SUM_IDENTITY_OK samples=2500
DYADIC_SHIFT_OK r=2..8 n=0..79
EXAMPLES {1: 4, 3: 4, 4: 8, 6: 20, 8: 16, 12: 120, 21: 28, 24: 240, 30: 100, 42: 140, 60: 600}
```

The finite checks are supplementary: the recurrence, GCD, and dyadic arguments above establish the result for every positive integer \(k\).

## Relationship to prior work

Mbirika, Schrader, and Spilker, *Pell and associated Pell braid sequences as GCDs of sums of k consecutive Pell, balancing, and related numbers*, arXiv:2301.05758, Section 6.1 and Question 30, introduce the squared-GCD question for the cobalancing sequence. They observe the divisibility \(4\mid\mathcal B_2(k)\), but do not give its exact value. Their primary theorems concern first powers. The present theorem answers their squared-cobalancing question for every \(k\), rather than merely deriving this divisibility or reusing a finite recurrence truncation. The 2022 Mbirika--Spilker squared-GCD formulas concern generalized Fibonacci sequences with a different homogeneous recurrence; their formulas do not directly determine the affine cobalancing square GCD here.

## Limitations

The theorem determines only the squared-cobalancing branch of Question 30. It does not simultaneously classify the other squared Pell/balancing-related sequences, nor higher powers or arbitrary affine recurrences. The numerical checks cover finitely many windows, while the infinite result is mathematical. Although inspected published sources and focused research-record searches did not reveal a stronger encompassing theorem, a matching result in unindexed literature cannot be excluded. Independent mathematical validation has not been conducted.

## References

1. aBa Mbirika, Janee Schrader, Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, Journal of Integer Sequences **26** (2023), Article 23.6.4, Section 6.1, Question 30. First posted 2023-01-13 as arXiv:2301.05758. https://cs.uwaterloo.ca/journals/JIS/VOL26/Mbirika/mbir5.pdf
2. aBa Mbirika, Jürgen Spilker, *GCD of sums of k consecutive squares of generalized Fibonacci numbers*, Fibonacci Quarterly **60** (2022), 255--269, arXiv:2204.12626. https://www.fq.math.ca/Papers1/60-5/mbirika.pdf
