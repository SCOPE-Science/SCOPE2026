# Two-phase residue statistics for partial sums of central binomial coefficients modulo five

## Finding
For every integer \(n\ge0\), define
\[
S(n)=\sum_{k=0}^{n-1}\binom{2k}{k},\qquad S(0)=0.
\]
For \(r\ge1\) and \(y\in\mathbb Z/5\mathbb Z\), define
\[
N_r(y)=\#\{0\le n<5^r:S(n)\equiv y\pmod5\}.
\]
With vector coordinates ordered by \(y=0,1,2,3,4\), the exact alternating limiting laws are
\[
\lim_{j\to\infty}5^{-2j}(N_{2j}(0),\ldots,N_{2j}(4))
=\frac1{14}(1,8,2,1,2),
\]
\[
\lim_{j\to\infty}5^{-(2j+1)}(N_{2j+1}(0),\ldots,N_{2j+1}(4))
=\frac1{14}(1,2,1,2,8).
\]
Here the first limit is taken over positive depths. More quantitatively, with \(q=(1,8,2,1,2)/14\) and subscripts interpreted modulo five, for every \(r\ge1\) and every residue \(y\),
\[
\left|N_r(y)-5^r q_{(-1)^r y}\right|\le3^r.
\]
Thus **none of the four nonzero residue classes of \(S(n)\bmod5\) has a natural density** among nonnegative indices. No assertion is made about the existence of a natural density for residue zero. The result concerns unweighted partial sums, rather than the individual central-binomial residues.

## Assumptions and scope
All binomial coefficients are ordinary integers; only their residues modulo the fixed prime five are used. The index \(n\) is nonnegative. A natural density of a residue class means the limit of \(N^{-1}\#\{0\le n<N:S(n)\equiv y\pmod5\}\) as \(N\to\infty\), along all integers \(N\). The displayed limits concern the two subsequences \(N=5^r\); the failure of agreement between those subsequences proves the claimed nonexistence. The quantitative inequality is uniform in the residue and depth, and does not assert that the exponent \(\log_5 3\) is optimal.

## Proof
**Digitwise congruences and summatory recurrence.** Put \(a(n)=\binom{2n}{n}\bmod5\). Lucas's congruence (or Kummer's carry criterion followed by Lucas's congruence) shows
\[
a(5m+d)=w_d a(m),\qquad (w_0,w_1,w_2,w_3,w_4)=(1,2,1,0,0).
\]
Indeed, in a base-five expansion of \(m\), a digit three or four produces a carry when doubling; otherwise the local factors are \(\binom00,\binom21,\binom42\). Since \(\sum_{d=0}^4w_d=4\equiv-1\pmod5\), complete five-term blocks give, with \(c=(0,1,3,4,4)\),
\[
S(5m+d)\equiv-S(m)+c_d a(m),\qquad
 a(5m+d)\equiv w_d a(m)\pmod5.
\]
Consequently each base-five digit acts on \((u,a)=(S(m),a(m))\in\mathbb F_5^2\) by
\[
T_d(u,a)=(-u+c_da,w_da),\qquad d\in\{0,1,2,3,4\},
\]
starting from \((S(0),a(0))=(0,1)\). Leading zero digits preserve this initial state, so every word of length \(r\) encodes exactly one \(0\le n<5^r\).

**Absorption and convergence.** Sample successive base-five digits independently and uniformly and iterate the \(T_d\). If the current second coordinate is nonzero, the next coordinate is zero precisely for digits three and four; once zero, it remains zero. Thus, with \(U_r\) the first coordinate after \(r\) digits,
\[
\mathbb P\{\text{not absorbed after }r\text{ digits}\}=(3/5)^r.
\]
Once absorbed, the update of the first coordinate is just \(u\mapsto-u\), regardless of subsequent digits. Hence \(Y_r=(-1)^rU_r\) stabilizes almost surely to a random variable \(Y_\infty\in\mathbb F_5\), and for each residue \(y\),
\[
|\mathbb P(Y_r=y)-\mathbb P(Y_\infty=y)|\le(3/5)^r.
\]
It remains to evaluate the distribution of \(Y_\infty\) exactly.

**Exact finite rational certificate.** Index the twenty active states by \((u,a)\) with \(u=0,1,2,3,4\) and \(a=1,2,3,4\). Let \(B\) be the \(20\times20\) nonnegative integer matrix whose column for \((u,a)\) has one contribution at \(T_d(u,a)\) for each \(d=0,1,2\). Let \(C\) be the \(5\times20\) integer matrix whose column has one contribution in row \(u'\) for each \(d=3,4\) such that \(T_d(u,a)=(u',0)\). Let \(F\) be the \(5\times5\) permutation matrix defined by \(F e_u=e_{-u}\), and \(e\) the basis vector of active state \((0,1)\). Each column of \(B\) sums to three, so \(\rho(B)\le3\). The convergent geometric sum over first-absorption depths gives
\[
q:=\bigl(\mathbb P(Y_\infty=y)\bigr)_{y=0}^4
=\frac15\left(FC+\frac15CB\right)
\left(I-\frac{B^2}{25}\right)^{-1}e.
\]
For a hand-checkable exact rational certificate, the following table is the vector \(100800\,t\) for \(t=(I-B^2/25)^{-1}e\). Rows are \(u=0,1,2,3,4\), and columns are \(a=1,2,3,4\):

| \(u\) | \(a=1\) | \(a=2\) | \(a=3\) | \(a=4\) |
|---|---:|---:|---:|---:|
| 0 | 110373 | 5561 | 689 | 877 |
| 1 | 373 | 5561 | 689 | 5877 |
| 2 | 4973 | 961 | 689 | 877 |
| 3 | 4973 | 5561 | 689 | 1277 |
| 4 | 373 | 5561 | 289 | 1277 |

Direct substitution verifies \((25I-B^2)(100800\,t)=25\cdot100800\,e\). Applying \(C\) and \(CB\) to this vector gives, in row order \(0,1,2,3,4\),
\[
C t=\frac1{504}(125,75,125,75,1175),
\qquad
CBt=\frac1{504}(275,1325,1425,275,1425).
\]
Substitution into the displayed formula yields \(q=(1,8,2,1,2)/14\). Since \(U_r=(-1)^rY_r\), it gives the two limiting laws and the uniform error bound.

**Nonexistence of nonzero residue densities.** The even and odd limiting vectors differ in coordinates one, two, three and four. Any natural density would have to agree on every subsequence of cutoffs. Consequently none of those four residue classes has a natural density. This completes the proof.

## Verification
The self-contained standard-library Python file `verify.py` separately constructs the twenty active transitions and five absorbing transitions, checks all twenty integer equations for the displayed rational vector, evaluates both limiting vectors exactly using `fractions.Fraction`, and checks the asserted finite-block error bounds. It additionally compares the Lucas digit product with the actual integer binomial coefficient for indices \(0\le n\le200\), verifies the state recurrence directly for every index below \(5^4\), and enumerates all residue counts through depth seven (indices below \(5^7=78125\)). The checker prints `PASS` after completing all tests. Infinite conclusions follow from the digit recurrence, first-absorption argument and exact rational certificate, not from finite enumeration.

## Relationship to prior work
Sun and Tauraso (2008, arXiv:0805.0563, Theorem 1.1) establish congruences for sums of central binomial coefficients at prime-power endpoints and related weights. Mattarei (2009, arXiv:0906.4290, Theorem 3 and Section 3) evaluates the complete prime-power initial-sum polynomial modulo a prime. Chen, Hou and Zeilberger (2015, arXiv:1509.09070, Theorem 2.1 and Corollary 2.3) develop methods for endpoint summatory congruences of constant-term sequences. Their endpoint identities are consistent with \(S(5^r)\equiv(-1)^r\pmod5\). They do not themselves evaluate, or assert the existence/nonexistence of, the limiting frequencies of all values of the running sum as its upper endpoint varies through a full base-five interval. The extra result here is the exact alternating frequency law and failure of natural densities, not Lucas's congruence or a new endpoint congruence. The known 2026 central-binomial quadratic-character classification concerns individual coefficients and shifts, not prefix sums; its digit-product step is compatible but does not imply the computed distribution.

## Limitations
The theorem treats only modulus five, not higher powers or general odd primes. The error bound is an explicit uniform bound, not a claimed optimal rate. The residue zero has the same limiting frequency along the two displayed cutoffs, but its density along *all* integer cutoffs is not determined. The finite certificate is reproduced by the supplied checker, but there has been no independent external mathematical audit. Broad general results about automata and digital functions may provide methods for recovering the theorem; priority of this precise evaluated result remains subject to further specialist literature review, particularly the full 2001 work of Barat and Grabner, which was not accessible for full-text comparison.

## References
1. Z.-W. Sun and R. Tauraso, *New congruences for central binomial coefficients*, arXiv:0805.0563 (first posted 2008-05-05), Theorem 1.1; https://arxiv.org/abs/0805.0563.
2. S. Mattarei, *Asymptotics of partial sums of central binomial coefficients and Catalan numbers*, arXiv:0906.4290 (first posted 2009-06-23), Section 3, Theorem 3; https://arxiv.org/abs/0906.4290.
3. W. Y. C. Chen, Q.-H. Hou and D. Zeilberger, *Automated Discovery and Proof of Congruence Theorems for Partial Sums of Combinatorial Sequences*, arXiv:1509.09070 (2015-09-30), Sections 2–3; https://arxiv.org/abs/1509.09070.
4. G. Barat and P. J. Grabner, *Distribution of Binomial Coefficients and Digital Functions*, Journal of the London Mathematical Society **64** (2001), 523–547, DOI:10.1112/S0024610701002630 (abstract accessible; full text not inspected).
5. *Parity rigidity and exact first-defect laws for central-binomial quadratic characters*, published number-theory manuscript, 2026-11-02; https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-parity-rigidity-and-exact-first-defect-laws-for-central-binomial--85923533227d.
