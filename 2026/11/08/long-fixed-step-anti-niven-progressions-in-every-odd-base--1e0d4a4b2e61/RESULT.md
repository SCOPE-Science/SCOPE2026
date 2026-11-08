# Long fixed-step anti-Niven progressions in every odd base

## Finding

For an integer base \(b\ge 2\), let \(s_b(n)\) be the base-\(b\) digit sum of the positive integer \(n\). Call \(n\) *\(b\)-anti-Niven* when \(\gcd(n,s_b(n))=1\).

**Theorem.** For every odd integer \(b\ge3\), there exist infinitely many positive integers \(N\) such that
\[
\gcd\bigl(N+j(b-1),s_b(N+j(b-1))\bigr)=1
\quad\text{for every }j\in\{0,1,\ldots,2b\}.
\]
Thus the maximum length of a base-\(b\) anti-Niven arithmetic progression with the **fixed** common difference \(b-1\) is at least \(2b+1\), including for every odd composite base.

The published result for even bases gives an exact maximum \(2b+1\) for this difference, while its odd-base lower bound was proved there only for prime bases. The present theorem fills the composite odd-base case at the same natural length. It does not assert that the lower bound is sharp in odd bases.

## Assumptions and scope

Throughout the proof, \(b\ge3\) is an odd integer. The residue system contains only positive integers, and \(\gcd\) denotes the positive greatest common divisor. We use elementary Chinese remaindering and the finite multiplicative order of a unit modulo a positive integer. The construction is non-effective in size but explicit once a finite CRT residue is selected; no conjecture about primes is required.

## Proof

**Step 1: two digit-sum levels.** Put \(d=b-1\), \(U=1+2bd\), and \(L_j=1+jd\) for \(0\le j\le2b\). A direct base-\(b\) expansion gives
\[
s_b(L_j)=\begin{cases}1,&j\in\{0,1,b+1\},\\ b,&j\in\{2,\ldots,b\}\cup\{b+2,\ldots,2b\}.\end{cases}
\]
Indeed, \(L_0=1\), \(L_1=b\), and \(L_{b+1}=b^2\). For \(2\le j\le b\), write \(L_j=(j-1)b+(b+1-j)\), where both coefficients are digits. For \(b+2\le j\le2b\), put \(v=j-b-1\); then \(1\le v\le b-1\) and \(L_j=b^2+(v-1)b+(b-v)\). These expansions yield the displayed digit sums and give \(1\le L_j\le U\). For the three exceptional indices, also
\[
1\le L_j+2d\le 1+(b+3)d\le U,
\]
where the last inequality uses \(b\ge3\).

**Step 2: simultaneous roughness via CRT.** We claim that arbitrarily large integers \(P\) exist such that, with \(Q=P-d\),
\[
P\equiv1\pmod b,\qquad P\equiv-1\pmod d,
\]
and neither \(P\) nor \(Q\) is divisible by any prime \(q\le U\). At a prime \(q\mid d\), prescribe \(P\equiv-1\pmod q\); then \(Q\equiv-1\pmod q\). At a prime \(q\mid b\), prescribe \(P\equiv1\pmod q\); then \(Q\equiv2\pmod q\), which is nonzero because \(b\) is odd. At any other prime \(q\le U\), choose one of the residues avoiding both \(0\) and \(d\) modulo \(q\). Such a choice exists: \(q\) is odd (since \(2\mid d\)), so at most two of at least three residues are forbidden. The full congruences modulo \(b\) and \(d\), together with these conditions at the remaining primes, are compatible because \(\gcd(b,d)=1\). The Chinese remainder theorem gives an infinite arithmetic progression of eligible \(P\). Take one sufficiently large that \(P,Q>U\) and the integers defined below are nonnegative. In particular,
\[
\gcd(b,PQ)=1,\quad \gcd(P,L_j)=1\ (0\le j\le2b),\quad
\gcd(Q,L_j+2d)=1\ (j\in\{0,1,b+1\}).
\]
The last two facts follow because all relevant positive integers are at most \(U\), while \(P,Q\) have no prime factors at most \(U\).

**Step 3: prescribe both a digit sum and a residue.** Define
\[
K=P-b,\qquad a=\frac{P+b}{b-1},\qquad R=K-a.
\]
The integer \(a\) is integral because \(P\equiv-1\pmod{b-1}\). We may enlarge \(P\) so that \(R\ge0\): equivalently, \((b-2)P\ge b^2\). Let \(H\) be the multiplicative order of \(b\) modulo \(PQ\), which exists by Step 2. Set
\[
C=\sum_{i=1}^{R} b^{2Hi}+\sum_{i=1}^{a}b^{2Hi+1}.
\]
The exponents are pairwise distinct, so all displayed summands occupy distinct unit digits in base \(b\). Consequently \(s_b(C)=R+a=K\). As \(b^H\equiv1\pmod{PQ}\),
\[
C\equiv R+ab=K+a(b-1)=2P\pmod{PQ}.
\]

**Step 4: infinitely many progressions.** Choose any positive multiple \(m\) of \(H\) with \(m\ge3\), and put \(N=C b^m+1\). The low part \(L_j<b^3\le b^m\) never carries into the high block. Therefore
\[
s_b(N+jd)=s_b(C)+s_b(L_j)=\begin{cases}Q,&j\in\{0,1,b+1\},\\P,&\text{otherwise}.
\end{cases}
\]
Since \(b^m\equiv1\pmod{PQ}\), we have \(N+jd\equiv2P+L_j\pmod{PQ}\). If \(j\) is not exceptional, reduce this congruence modulo \(P\) and use \(\gcd(P,L_j)=1\). If \(j\) is exceptional, reduce modulo \(Q\) and use \(P\equiv d\pmod Q\) to obtain \(\gcd(Q,2d+L_j)=1\). Thus every one of the \(2b+1\) terms is \(b\)-anti-Niven. Different arbitrarily large multiples \(m\) produce distinct starts \(N\), completing the proof. \(\square\)

## Verification

The accompanying standalone Python file `verification/check_anti_niven.py` checks the exact digit-sum splitting, local CRT admissibility, the auxiliary-parameter identities, and all required coprimality residues for ten bases, including odd composite examples. It also constructs the literal large integers for bases \(3\) and \(5\), checking their entire \(2b+1\)-term progressions directly. It prints `VERIFY_OK bases=10 complete_literal_bases=2 modular_checks=10` on success. These are finite consistency checks; the four-step argument above covers every odd base and infinitely many starts.

A compact composite-base certificate is \(b=9\), \(P=199\), \(Q=191\), \(a=26\), \(R=164\), and \(H=9405\). The resulting integer \(C\) is extremely large, but only its digit sum and residue are needed to check the entire progression symbolically.

## Relationship to prior work

Blau, Harrington, Lohrey, Sosis, and Wong, *Arithmetic Progressions of Integers that are Relatively Prime to their Digital Sums* (first public arXiv version, 9 August 2023), investigate anti-Niven arithmetic progressions. Their Theorem 3.5 proves the **exact** maximum \(2b+1\) for difference \(b-1\) when \(b\) is even. Their Theorem 4.2 establishes the **lower** bound \(2b+1\) for odd **prime** \(b\), using the low-digit progression directly. The proof above establishes infinitely many progressions of that length in **every odd composite base**, where the prime-base direct argument does not suffice. Their Theorem 2.4 permits the common difference to vary with the length and therefore does not yield this fixed-difference assertion. Theorem 2.5 is inapplicable at the chosen difference because every prime dividing \(b-1\) also divides it.

## Limitations

The result does not determine the maximum length for odd bases, does not cover other fixed differences, and does not resolve the paper's general odd-base conjecture for even differences with a prime divisor of \(b-1\) excluded from the difference. The CRT construction yields enormous witnesses; it is a proof of infinitude, not a practical search bound for the first start. Bibliographic searches cannot rule out an unindexed equivalent result, and the journal version's full text was not separately inspected (the arXiv full text was inspected).

## References

1. R. Blau, J. Harrington, S. Lohrey, E. Sosis, and T. W. H. Wong, *Arithmetic Progressions of Integers that are Relatively Prime to their Digital Sums*, arXiv:2308.05228 (first version 9 August 2023); later published in *Rocky Mountain Journal of Mathematics* 56 (2026), 13–21. https://arxiv.org/html/2308.05228 and https://doi.org/10.1216/rmj.2026.56.13.
2. J. Harrington, M. Litman, and T. W. H. Wong, *Every arithmetic progression contains infinitely many b-Niven numbers*, arXiv:2303.06534 (2023). https://arxiv.org/abs/2303.06534. This concerns Niven rather than anti-Niven numbers and does not imply the claim above.
