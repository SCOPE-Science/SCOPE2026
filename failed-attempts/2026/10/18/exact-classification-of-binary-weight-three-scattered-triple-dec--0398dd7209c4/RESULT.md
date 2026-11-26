# Exact classification of binary weight-three scattered triple decks

## Finding
For every integer \(n\ge 0\), let \(D_{3,3}(n)\) denote the number of distinct *scattered length-three decks* attained by binary words of length \(n\) containing exactly three symbols \(1\); set this number to zero for \(n<3\). A scattered triple deck records, for each of the eight binary words of length three, its total number of occurrences as a not-necessarily-contiguous subsequence.

For all \(n\), the exact generating function is
\[
\boxed{\sum_{n\ge0}D_{3,3}(n)z^n=\frac{z^3}{(1-z)^4}-\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.}
\]
This establishes Conjecture 1 of Chrisnata, Kiah, Karingula, Vardy, Yaakobi and Yao [1]. Furthermore, **every scattered triple-deck equivalence class within the weight-three language has either one or two words**, with an explicit classification of all two-word classes.

For \(n\ge3\), the number of two-word classes is
\[
P_n=\sum_{h=1}^{\lfloor(n-3)/4\rfloor}\sum_{b=0}^{\lfloor(n-3-4h)/2\rfloor}(n-2-4h-2b).
\]
The initial values for \(n=3,\ldots,16\) are \(D_{3,3}(n)=1,4,10,20,34,54,80,114,155,206,266,338,420,516\).

## Assumptions and scope
The alphabet is \(\{0,1\}\); all words are linear (not cyclic) and have Hamming weight exactly three. Two such words have the same deck only if their multiplicities of **all eight** subsequences of length three agree. A weight-three word admits precisely one gap representation
\[
w(a,b,c,d)=0^a1\,0^b1\,0^c1\,0^d,
\qquad (a,b,c,d)\in\mathbb{Z}_{\ge0}^4,
\quad a+b+c+d=N=n-3.
\]
Here \(\binom{x}{j}=0\) when \(0\le x<j\).

## Proof
**Step 1: a complete set of deck parameters.** Define
\[
T=\#(01)=3a+2b+c,\quad
U=\#(011)=3a+b,\quad
Q=\#(001)=\binom a2+\binom{a+b}{2}+\binom{a+b+c}{2}.
\]
The symbols \(\#(u)\) mean scattered subsequence counts of \(u\) in \(w\). The eight triple counts, in order \(000,001,010,011,100,101,110,111\), are
\[
\left(\binom N3,\ Q,\ T(N-1)-2Q,\ U,\ 3\binom N2-T(N-1)+Q,\ 2(T-U),\ 3N-2T+U,\ 1\right).
\]
Indeed, among all triples containing two zeroes, there are \(3\binom N2\) choices. Every \(01\) pair extends using one of the other \(N-1\) zeroes, yielding \(2\#(001)+\#(010)=T(N-1)\). Among all triples with two ones there are \(3N\) choices; extending an \(01\) pair using the other one yields \(2\#(011)+\#(101)=2T\). These identities prove the displayed deck vector.

Consequently the entire triple deck is determined by \((N,T,U,Q)\), and conversely these data are recoverable from that deck: \(N=n-3\) is fixed; \(Q=\#(001)\), \(U=\#(011)\) and \(T=U+\#(101)/2\).

**Step 2: classify collisions.** Fix \(N,T,U\). Subtracting the three linear equations for two gap vectors yields uniquely
\[
(a',b',c',d')=(a+t,b-3t,c+3t,d-t),\qquad t\in\mathbb Z.
\]
Direct expansion of the binomial expressions in Step 1 yields
\[
Q'-Q=t(c-b+3t).
\]
Thus two *different* gap vectors have identical triple decks if and only if \(b-c\) is a nonzero multiple of three and
\[
(a',b',c',d')=\left(a+\frac{b-c}{3},\ c,\ b,\ d-\frac{b-c}{3}\right)
\]
has nonnegative coordinates. The transformation is an involution (apply it twice to recover the original). Therefore every equivalence class contains at most two distinct words.

**Step 3: count the two-word classes.** Each nontrivial class has precisely one member with \(c>b\). Write \(c=b+3h\), \(h\ge1\). For the other member to have nonnegative coordinates it is necessary and sufficient that \(a\ge h\). With \(a=A+h\), the constraints reduce to
\[
(A,b,d,h)\in\mathbb Z_{\ge0}^3\times\mathbb Z_{\ge1},
\qquad N=A+2b+d+4h.
\]
Every solution gives one and only one two-word class. Therefore its generating function, indexed by full word length \(n=N+3\), is
\[
\sum_{n\ge0}P_nz^n
=z^3\left(\sum_{h\ge1}z^{4h}\right)
\left(\sum_{A\ge0}z^A\right)
\left(\sum_{b\ge0}z^{2b}\right)
\left(\sum_{d\ge0}z^d\right)
=\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.
\]
As the number of weight-three words is \(\binom n3\) for \(n\ge3\), and each two-word class reduces the number of classes by exactly one, \(D_{3,3}(n)=\binom n3-P_n\). Since \(\sum_{n\ge3}\binom n3z^n=z^3/(1-z)^4\), the formula follows for every \(n\ge0\). The double-sum expression for \(P_n\) counts \((A,d)\) with prescribed sum after \(h,b\) are fixed. \(\square\)

## Verification
Run `python3 CHECK.py` in the directory containing this result. The checker directly enumerates all ordered index triples (not a hash surrogate), groups the resulting decks, independently tests the four-gap matching involution, and compares the exact two-word class count with its coefficient formula. The included output records every case for \(3\le n\le19\), covering all \(4{,}845\) weight-three words in that interval. The finite check is a consistency test; the proof of the assertion for arbitrary \(n\) is Steps 1–3, not the enumeration.

## Relationship to prior work
Chrisnata et al. [1], PDF page 17, give the same rational function as **Conjecture 1**, with its first twenty coefficients checked numerically; their Theorem 27 and Corollary 28 prove lower bounds and cubic-order asymptotics rather than the all-length equality or a complete two-word-class classification. The gap-coordinate perspective is natural in that work, but the quadratic cancellation and exact pairing argument above close the stated gap.

Nilforoushan and Parvaresh [2], first made public on 2026-09-19, explain general linear relations among the coordinates of scattered decks and prove improved asymptotic bounds; they do not state this exact weight-three enumeration or the collision involution. Lejeune, Rigo and Rosenfeld [3] study general binomial equivalence, with explicit algorithms for two-binomial classes, not this three-binomial constant-weight classification.

## Limitations
The result concerns binary weight-three words and length-three scattered decks only. It does not count unrestricted-weight binary triple decks or decks of longer subsequence length. The independent finite check reaches length nineteen; it does not replace the proof. Absence of an equivalent statement from the examined sources does not establish exhaustive historical priority. No independent scholarly validation has been performed.

## References
[1] J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi and H. Yao, *On the Number of Distinct k-Decks: Enumeration and Bounds*, Advances in Mathematics of Communications 17 (2023), 960–978, doi:10.3934/amc.2021032. Lawful author PDF: https://yaakobi.net.technion.ac.il/files/2022/08/60_k_Decks_Disc_Math21.pdf (Conjecture 1, printed p. 17).

[2] A. Nilforoushan and F. Parvaresh, *Improved upper bound on the number of distinct k-decks for any k and alphabet size by counting the independent parameters*, arXiv:2609.23106 (first submitted 2026-09-19), https://arxiv.org/abs/2609.23106.

[3] M. Lejeune, M. Rigo and M. Rosenfeld, *On the Binomial Equivalence Classes of Finite Words*, International Journal of Algebra and Computation (2020), arXiv:2001.11732. Lawful manuscript: https://orbi.uliege.be/bitstream/2268/249124/1/LejeuneRigoRosenfeld-ijacVersion2.pdf.
