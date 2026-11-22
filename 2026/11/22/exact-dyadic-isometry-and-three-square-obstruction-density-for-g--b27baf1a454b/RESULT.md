# Exact dyadic isometry and three-square obstruction density for generalized derangements with parameter two

## Finding
Let \(G_n=D_n^{(2)}\) be the generalized derangement numbers of parameter two in the normalization of Ulas, with \(G_0=1\), \(G_1=2\), and
\[
G_n=(n+1)G_{n-1}+(n-1)G_{n-2}\quad(n\ge2).
\]
For any distinct nonnegative integers \(m,n\), the exact metric identity is
\[
\boxed{\nu_2(G_m-G_n)=\nu_2(m-n).}
\]
Hence \(n\mapsto G_n\bmod2^k\) is a bijection of \(\mathbb Z/2^k\mathbb Z\) for every integer \(k\ge1\), with least period \(2^k\).

For \(j\ge0\), let \(a_j\) be the unique residue modulo \(2^{2j+3}\) for which \(G_{a_j}\equiv7\cdot2^{2j}\pmod{2^{2j+3}}\). Then
\[
\boxed{\{n\ge0:G_n\text{ is not a sum of three integer squares}\}=\bigsqcup_{j\ge0}\{n\ge0:n\equiv a_j\pmod{2^{2j+3}}\}.}
\]
The first classes are \(a_0\equiv2\pmod8\), \(a_1\equiv23\pmod{32}\), \(a_2\equiv115\pmod{128}\), \(a_3\equiv227\pmod{512}\), and \(a_4\equiv675\pmod{2048}\). In particular, if \(S(X)=\#\{0\le n<X:G_n\text{ is not a sum of three integer squares}\}\), then
\[
\boxed{S(X)=X/6+O(\log(2+X)).}
\]
Thus the natural density exists and equals \(1/6\).

## Assumptions and scope
All indices are nonnegative integers, all sums of three squares allow arbitrary integer coordinates, and \(\nu_2\) is the ordinary two-adic valuation with \(\nu_2(0)=+\infty\). There are no asymptotic hypotheses on indices or exponents. The normalization \(G_0=1\), not twice that value, is essential. The result concerns the parameter \(v=2\), not every even parameter.

## Proof
**Step 1: Reduction to ordinary derangements.** Let \(d_0=1\), \(d_n=nd_{n-1}+(-1)^n\) for \(n\ge1\). Since \(\sum_{n\ge0}d_n z^n/n!=e^{-z}/(1-z)\), taking two applications of \(1+\frac{d}{dz}\) yields
\[
G_n=\frac{d_n+2d_{n+1}+d_{n+2}}2
=\frac{(n^2+5n+5)d_n-(n+3)(-1)^n}{2}.
\]
This also follows directly from the defining finite sum \(G_n=\sum_{j=0}^n(-1)^j\binom{n+2-j}{n-j}n!/j!\). Set \(P(x)=x^2+5x+5\).

**Step 2: A convergent two-adic interpolation.** For \(x\in\mathbb Z_2\), put
\[
F(x)=\sum_{j\ge0}(-1)^j\,x(x-1)\cdots(x-j+1),
\]
with the empty product one. The \(j\)-th falling factorial is divisible by \(2^{\lfloor j/2\rfloor}\) on each of the two discs \(x\in2\mathbb Z_2\) or \(x\in1+2\mathbb Z_2\), and, after replacing \(x\) by \(2t\) or \(1+2t\), this divisibility holds coefficient by coefficient in \(\mathbb Z_2[t]\). Consequently both \(F(2t)\) and \(F(1+2t)\) belong to the restricted power-series ring \(\mathbb Z_2\langle t\rangle\), with coefficients converging to zero two-adically. At nonnegative integer \(n\), the falling factorials vanish for \(j>n\), giving \(d_n=(-1)^nF(n)\).

Truncating the restricted series at \(j=4\) for the even disc and at \(j=5\) for the odd disc gives the coefficientwise congruences
\[
F(2t)\equiv1+4t+4t^2\pmod8,\qquad
F(1+2t)\equiv2t+4t^2\pmod8.
\]
All omitted terms have at least three factors divisible by two, coefficientwise.

**Step 3: Two isometric branches.** Define integral restricted power series
\[
K_0(t)=\frac{P(2t)F(2t)-(2t+5)}4,\qquad
K_1(t)=\frac{2t+4-P(2t+1)F(2t+1)}4.
\]
The preceding mod-eight congruences show that both numerators have coefficients divisible by four and, after division, satisfy
\[
K_0(t)\equiv t\pmod2,\qquad K_1(t)\equiv t+1\pmod2.
\]
In other words, \(K_0(t)=t+2Q_0(t)\) and \(K_1(t)=t+1+2Q_1(t)\) for \(Q_0,Q_1\in\mathbb Z_2\langle t\rangle\). Any integral restricted power series is one-Lipschitz, because \(Q(t)-Q(s)\in(t-s)\mathbb Z_2\). Thus, for any distinct \(s,t\in\mathbb Z_2\),
\[
\nu_2(K_i(t)-K_i(s))=\nu_2(t-s)\qquad(i=0,1).
\]
By Step 1, \(G_{2t}=1+2K_0(t)\) and \(G_{2t+1}=2K_1(t)\). Both same-parity branches therefore preserve all two-adic distances, while across parities the values have opposite parity. This proves \(\nu_2(G_m-G_n)=\nu_2(m-n)\) for all distinct nonnegative indices. The bijection and minimal period follow at once: the induced map modulo \(2^k\) is injective, hence bijective, and equality of values modulo \(2^k\) is equivalent to equality of indices modulo \(2^k\).

**Step 4: Three-square classes.** Legendre's theorem says that a nonnegative integer fails to be a sum of three integer squares exactly when it is \(4^j(8b+7)\), for some \(j,b\ge0\). Since every residue modulo \(2^{2j+3}\) has exactly one index antecedent under \(G\), this produces precisely the progression \(n\equiv a_j\pmod{2^{2j+3}}\). The progressions are pairwise disjoint because their value-residue classes have different two-adic valuations.

**Step 5: Density and quantitative error.** Fix \(X\ge2\) and choose \(L\) with \(2^{L-1}<X\le2^L\). For every \(j\) with \(2j+3\le L\), the progression contributes \(X/2^{2j+3}+O(1)\) indices below \(X\), and there are \(O(L)\) such progressions. Every omitted progression has \(2j\ge L-2\); hence its indices necessarily satisfy \(G_n\equiv0\pmod{2^{L-2}}\). By the bijection, these indices lie in a single class modulo \(2^{L-2}\), giving at most a bounded number below \(X\). The omitted geometric tail of the target main term contributes only \(O(1)\). Therefore
\[
S(X)=X\sum_{j\ge0}2^{-(2j+3)}+O(L)=X/6+O(\log(2+X)).
\]

## Verification
The included standalone `verify.py` uses only Python's standard library. It verifies the two polynomial coefficient congruences, the first 50 defining-recurrence terms against the independent ordinary-derangement formula, the first 15 finite-sum formulas, complete bijections and full periods modulo \(2^k\) for \(1\le k\le13\), thousands of distinct-pair valuation identities, and the first five unique forbidden-index progressions. Running `python3 verify.py` terminates with `PASS`. The infinite proof is the analytic argument above; finite tests are corroboration, not its substitute.

## Relationship to prior work
Maciej Ulas, *Representing Generalized Derangements as Sums of Three Squares*, The Fibonacci Quarterly 61 (2023), 231–239, defines this normalization and explicitly poses Problem 4.1 (even parameters) and Question 4.3 (existence of density), establishing only restricted congruence progressions when \(v\) is even. The present result gives a complete solution of those questions for \(v=2\), not for all even \(v\). Earlier classical-derangement modular results concern \(v=0\) and do not imply the global isometry for \(v=2\). The combinatorial identities of Ferrari, Munarini and Zagaglia Salvi cover related generalized-derangement enumerations but do not provide the stated dyadic metric or three-square density.

## Limitations
The theorem does not determine any higher even parameter \(v\ge4\), nor finer statistics of the three-square representations themselves. The uniqueness claim is a proved arithmetic property of parameter two, not a general uniqueness assertion across all generalized derangements. Existing literature not indexed or not inspected in full may contain an equivalent earlier result; no claim of independent external validation is made. The exact first-public-source date uses the publisher's verified online date; the journal issue carries an earlier 2023 month label.

## References
- M. Ulas, *Representing Generalized Derangements as Sums of Three Squares*, Fibonacci Quarterly 61 (2023), no. 3, 231–239. Full text: https://www.fq.math.ca/Papers/61-3/ulas11202022.pdf; publisher record: https://doi.org/10.1080/00150517.2023.12427401 (online 2024-09-10).
- L. Ferrari, E. Munarini, L. Zagaglia Salvi, *Some combinatorial properties of generalized derangement numbers*, Rivista di Matematica della Università di Parma (2020). https://www.rivmat.unipr.it/wwwprotetto/2020-11-2/Riv_Parma_11-2-2020_03.pdf
- P. Miska, *Arithmetic properties of the sequence of derangements and its generalizations*, arXiv:1508.01987 (2015/2016), https://arxiv.org/abs/1508.01987.
