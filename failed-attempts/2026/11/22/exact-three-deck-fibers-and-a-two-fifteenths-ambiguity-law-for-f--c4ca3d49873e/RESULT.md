# Exact three-deck fibers and a two-fifteenths ambiguity law for four-one binary palindromes

## Finding

Let \(\mathcal P_n\) be the binary palindromes of length \(n\ge4\) containing exactly four \(1\)'s. The *three-deck* \(\mathcal D_3(w)\) is the vector of multiplicities of all eight scattered (not necessarily contiguous) binary subsequences of length three. Set \(N=n-4\). Every word in \(\mathcal P_n\) is uniquely represented as
\[
P(a,b,c)=0^a1\,0^b1\,0^c1\,0^b1\,0^a,
\qquad a,b,c\in\mathbb Z_{\ge0},\quad 2a+2b+c=N.
\]

**Complete inverse-fiber theorem.** Two distinct words in \(\mathcal P_n\) have the same three-deck if and only if, after exchanging the two words, they are
\[
\boxed{P(a,c+5d,c)\quad\text{and}\quad P(a+d,c+d,c+6d)}
\]
for some integers \(a,c\ge0\) and \(d\ge1\). Every three-deck fiber inside \(\mathcal P_n\) has size one or two, and each two-word fiber has this unique parameterization.

The exact number of two-word fibers at length \(n=N+4\) is
\[
\boxed{C_N=[z^N]\frac{z^{10}}{(1-z^2)(1-z^3)(1-z^{10})}.}
\]
The number of distinct three-decks attained on \(\mathcal P_n\) is
\[
\boxed{\binom{\lfloor N/2\rfloor+2}{2}-C_N.}
\]
The first collision occurs at \(n=14\), an example already exhibited in earlier work; there is none at \(n=15\), and there is at least one at every \(n\ge16\). Under uniform sampling from \(\mathcal P_n\), the probability of belonging to a nontrivial fiber tends to \(\boxed{2/15}\) as \(n\to\infty\).

## Assumptions and scope

All words are finite, linear, binary, and indexed in their given orientation; no quotient by complement or reversal is taken. Subsequence multiplicities count different strictly increasing triples of positions even if they yield the same three-letter pattern. The theorem classifies equivalence *within the palindromic four-one family*; it does not assert that such a word cannot have a nonpalindromic three-deck twin. Empty zero runs, including \(c=0\), are permitted. All statements are exact for integers \(n\ge4\), with the probability limit as \(n\to\infty\).

## Proof

**1. The full deck has two independent coordinates.** Let \(z_i\) be the number of zeroes preceding the \(i\)-th one. For the indicated palindrome these are \(a,a+b,N-a-b,N-a\), and their sum is \(2N\). Write \(D_{uvw}\) for the count of scattered occurrences of \(uvw\). Define
\[
t=4a+b,\qquad H=\sum_{i=1}^{4}\binom{z_i}{2}
=N^2+2Na-Nt-N+10a^2-6at+t^2.
\]
Clearly \(D_{001}=H\), and reversal symmetry gives \(D_{100}=H\). Counting the number of later pairs of ones available after each zero run gives
\[
D_{011}=6a+3b+c=N+t,\qquad D_{110}=N+t.
\]
Each zero between two ones contributes to \(101\) in the number of ways to choose the bounding ones, yielding
\[
D_{101}=3b+4c+3b=6b+4c=4N-2t.
\]
Further, \(D_{010}=\sum_i z_i(N-z_i)=2N(N-1)-2H\). Finally, \(D_{000}=\binom N3\) and \(D_{111}=\binom43=4\). Thus, in lexicographic pattern order, the *entire* three-deck is
\[
\boxed{\left(\binom N3,\ H,\ 2N(N-1)-2H,\ N+t,\ H,\ 4N-2t,\ N+t,\ 4\right).}
\]
In particular two same-length words in this family have equal decks if and only if their pairs \((t,H)\) agree.

**2. Solve the equality of deck coordinates.** At fixed \(N,t\), the other gaps are \(b=t-4a\) and \(c=N+6a-2t\), and \(H\) is a quadratic in \(a\) with leading coefficient \(10\). If \(a,a'\) are two possible values, their \(H\) values agree exactly when
\[
(a-a')\bigl(10(a+a')+2N-6t\bigr)=0.
\]
Consequently a fiber has at most two words. In the distinct case, substitution of \(t=4a+b\) and \(N=2a+2b+c\) gives the only possible partner parameters
\[
(a',b',c')=\left(a+\frac{b-c}{5},\;\frac{b+4c}{5},\;\frac{6b-c}{5}\right).
\]
The difference of the partner's middle gaps is \(b'-c'=c-b\). Thus, of any two different partners exactly one satisfies \(b>c\). For that member, integrality forces \(b-c=5d\) with \(d\ge1\). Its partner is automatically nonnegative and is precisely \((a+d,c+d,c+6d)\) for \(b=c+5d\). Conversely these two triples have equal \((N,t,H)\) by the displayed equations. The orientation \(b>c\) makes the parameters unique.

**3. Exact census.** A two-element fiber has a unique representative \(P(a,c+5d,c)\), where \(a,c\ge0,d\ge1\); its zero count is \(N=2a+3c+10d\). Consequently the ordinary generating series for collision pairs is
\[
\sum_{N\ge0}C_Nz^N=\sum_{a,c\ge0,d\ge1}z^{2a+3c+10d}
=\frac{z^{10}}{(1-z^2)(1-z^3)(1-z^{10})}.
\]
The number of family words at zero count \(N\) is the number of \((a,b)\ge0\) with \(a+b\le\lfloor N/2\rfloor\), namely \(T_N=\binom{\lfloor N/2\rfloor+2}{2}\). Every collision merges exactly two words into one deck class, hence the number of distinct decks is \(T_N-C_N\). The least attainable \(N\) is ten. Since every integer at least two is a nonnegative combination of two and three, every \(N\ge12\) is attained, whereas eleven is not.

**4. Limit law.** Counting the nonnegative lattice solutions of \(2a+3c+10d=N\), \(d\ge1\), gives \(C_N=N^2/120+O(N)\), for instance by summing the two-variable coin-change counts over \(d\). As \(T_N=N^2/8+O(N)\), the probability that a uniformly chosen family word belongs to a two-word fiber is \(2C_N/T_N=2/15+O(N^{-1})\).

## Verification

The included `verify.py` constructs every allowed gap triple for each zero count \(0\le N\le100\). It computes three-decks by an incremental subsequence-count dynamic program, compares with the theorem's eight-component formula, enumerates every actual deck fiber, checks that all nontrivial fibers equal the proposed involution orbits, and verifies the generating-function coefficients. A second literal triple-of-positions counter is used for every triple through \(N=18\). Coefficient calculations extend through \(N=500\). Run `python3 verify.py`; the expected output is included as `verify_output.txt`. These finite tests corroborate, but do not replace, the all-parameter algebraic proof above.

## Relationship to prior work

Angal, Ascoli, He, He, Post, Soe and Zhukova (arXiv:2610.41110v1, Section 3.1 and Remark 3.2) study restricted scattered-deck reconstruction and explicitly exhibit the length-14 ambiguous pair \(P(0,5,0)\), \(P(1,1,6)\) under the three-deck. Their stated threshold results and that example do **not** give the entire palindrome-restricted collision involution, the exact fiber generating function, or the limiting ambiguous fraction established here. Chrisnata and collaborators (Advances in Mathematics of Communications 17 (2023), 960–978) study unrestricted finite \(k\)-deck counts and enumerate tables, not this all-length palindromic four-one fiber structure. Nilforoushan and Parvaresh (arXiv:2609.23106v1) study general dimension and asymptotic upper bounds for distinct decks, which do not directly determine the fixed-palindrome content restriction. Related indexed results for weight-three three-decks and four-run binary words apply to different source families. The original length-14 witness is credited to prior literature; the claimed contribution is its all-length and all-fiber classification.

## Limitations

Novelty is assessed against the cited inspected primary text and indexed related records, not proved against all possible unpublished or unindexed work. The 2026 dimension-bound preprint was available by abstract for this comparison, not full-text inspection. The theorem addresses *in-class* fibers only. It makes no claim about four-deck reconstruction or about unrestricted binary weight-four fibers, which can be larger. The leading asymptotic gives no uniform error bound for small lengths, for which the exact generating series should be used. No external independent validation is claimed.

## References

1. K. Angal, R. Ascoli, S. X. He, X. He, L. Post, A. O. Soe and O. Zhukova, *Deck Reconstruction for Restricted Word Classes*, arXiv:2610.41110v1 (first posted 2026-10-30), https://arxiv.org/html/2610.41110v1, especially Section 3.1 and Remark 3.2.
2. A. Nilforoushan and F. Parvaresh, *Improved upper bound on the number of distinct k-decks for any k and alphabet size by counting the independent parameters*, arXiv:2609.23106v1 (first posted 2026-09-19), https://arxiv.org/abs/2609.23106.
3. J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi and H. Yao, *On the Number of Distinct k-Decks: Enumeration and Bounds*, Advances in Mathematics of Communications 17 (2023), 960–978, https://doi.org/10.3934/amc.2021032 (public full text includes the 2020 Mathematics Subject Classification 68R15).
