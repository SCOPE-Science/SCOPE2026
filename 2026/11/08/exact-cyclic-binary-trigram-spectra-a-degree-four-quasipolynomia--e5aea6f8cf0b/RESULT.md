# Exact cyclic binary trigram spectra: a degree-four quasipolynomial of period twelve

## Finding

For each integer \(n\ge1\), put \(\Sigma=\{0,1\}\). The **circular trigram count vector** of a word \(w=w_0\cdots w_{n-1}\in\Sigma^n\) is \(H(w)=(h_{abc})_{abc\in\Sigma^3}\), where \(h_{abc}\) counts indices \(i\in\{0,\ldots,n-1\}\) such that \((w_i,w_{i+1},w_{i+2})=(a,b,c)\), with subscripts taken modulo \(n\). Let \(C_n=|\{H(w):w\in\Sigma^n\}|\). Different cyclic rotations of a word need not be counted separately because they have the same vector, but different vectors are counted even if they are related by bit complementation.

**Theorem.** The exact ordinary generating function for feasible spectra is

\[
\begin{aligned}
\sum_{n\ge1}C_nz^n={}&\frac{2z}{1-z}+\frac{z^2}{1-z^2}
+\frac{2z^3}{(1-z)(1-z^2)(1-z^3)}\\
&+\frac{z^4}{(1-z)^3(1-z^2)(1-z^3)}
-\frac{z^5}{(1-z)^3(1-z^3)(1-z^4)}.
\end{aligned}
\]

Equivalently, for **every** integer \(n\ge1\),

\[
C_n=\frac{6n^4+276n^2+3943}{1728}
+\frac{19}{64}(-1)^n
+\frac4{27}\bigl(3\mathbf 1_{3\mid n}-1\bigr)
+\frac18\cos\left(\frac{\pi n}{2}\right).
\]

Thus \(C_n\) is a quasipolynomial of degree \(4\) and **minimal period \(12\)**, with \(C_n=n^4/288+O(n^2)\). The first values, for \(n=1,\ldots,18\), are \(2,3,4,6,8,13,18,27,38,53,72,98,128,167,214,271,338,419\). In the error-free observation model that records the multiset of circular trigrams of a length-\(n\) binary word, the largest set of pairwise distinguishable words has exactly \(C_n\) elements (one representative from each feasible vector).

## Assumptions and scope

The alphabet is ordered and fixed as \(\{0,1\}\). Words are **indexed binary strings**, not necessarily primitive necklaces. The observation counts the \(n\) cyclic windows with multiplicity, including periodic wraparound when \(n=1\) or \(n=2\); it does not include a starting position. The theorem concerns distinct attainable observation **vectors**, rather than the number of words realizing each vector. The length \(n\) ranges over all positive integers without a cutoff.

## Proof

Use the directed binary order-two de Bruijn graph, whose vertices are \(00,01,10,11\) and whose edge indexed by a triple \(abc\) goes from \(ab\) to \(bc\). A vector of nonnegative integer edge multiplicities is a circular trigram spectrum precisely when (i) incoming and outgoing multiplicities balance at each vertex and (ii) its positive-edge support is connected after zero-degree vertices are omitted. Indeed, any circular word gives a closed walk traversing all of its edges, and conversely the directed Euler-tour criterion produces a circular word with that histogram. This criterion includes all periodic and short words.

Write

\[
p=h_{000},\quad q=h_{111},\quad a=h_{001},\quad b=h_{011},\quad d=h_{101}.
\]

The balance constraints at vertices \(00,11,01,10\) force

\[
h_{100}=a,\qquad h_{110}=b,\qquad h_{010}=a+d-b=:c.
\]

Thus every balanced nonnegative profile is described uniquely by integers \(p,q,a,b,d\ge0\) with \(b\le a+d\). Its total length is

\[
n=p+q+3a+b+2d.
\]

The following cases are **disjoint and exhaustive** for profiles whose nonzero support is connected.

1. **Both bridges present**: \(a,b\ge1\), \(d,p,q\ge0\), \(b\le a+d\). The edges \(001,011,110,100\) give a connected directed cycle through all four vertices. The contribution to the generating function, summing \(z^n\) once per integer tuple, is

\[
\begin{aligned}
T(z)&=\frac1{(1-z)^2}\sum_{a\ge1,d\ge0}z^{3a+2d}\sum_{b=1}^{a+d}z^b\\
&=\frac{z^4}{(1-z)^3(1-z^2)(1-z^3)}
-\frac{z^5}{(1-z)^3(1-z^3)(1-z^4)}.
\end{aligned}
\]

2. **Only the \(00\)-bridge present**: \(a\ge1,b=0\). Then \(c=a+d\), and connectedness holds exactly when \(q=0\); \(p,d\ge0\) are free. The contribution is \(\frac{z^3}{(1-z)(1-z^2)(1-z^3)}\).

3. **Only the \(11\)-bridge present**: \(a=0,b\ge1\). Then \(d\ge b\), \(c=d-b\), and connectedness holds exactly when \(p=0\); \(q\ge0\) is free. Complementing bits identifies this case with case 2 and gives the same contribution.

4. **Neither bridge present**: \(a=b=0\), hence \(c=d\). The positive-edge support is one component only when the vector is (a) \(p>0,q=d=0\), (b) \(q>0,p=d=0\), or (c) \(d>0,p=q=0\). These are, respectively, an \(000\) loop, an \(111\) loop, or the two-edge \(010\leftrightarrow101\) cycle. Their total contribution is \(\frac{2z}{1-z}+\frac{z^2}{1-z^2}\).

Adding the four contributions proves the rational generating function. Each tuple specifies one and only one histogram; the Euler criterion guarantees at least one realizing word. In particular, balanced but disconnected disjoint unions of positive loops are **not** counted as attainable histograms.

To extract coefficients, partial fractions give, for \(n\ge1\), a polynomial contribution \(\frac{6n^4+276n^2+3943}{1728}\), and contributions from the poles at \(-1\), the primitive third roots, and the primitive fourth roots, respectively \(\frac{19}{64}(-1)^n\), \(\frac4{27}(3\mathbf1_{3\mid n}-1)\), and \(\frac18\cos(\pi n/2)\). This is the displayed exact coefficient formula. The primitive third- and fourth-root poles are nonremovable, so any quasipolynomial period must be divisible by both \(3\) and \(4\). The formula itself has period \(12\); therefore \(12\) is minimal. The leading term is \(n^4/288\) and the remaining polynomial term has degree \(2\). Finally, an observation code can use at most one word per histogram, and choosing one word from every attained histogram meets that bound.

## Verification

The included standalone `checker.py` implements three comparisons independent of the symbolic proof: direct enumeration of all \(2^n\) cyclic binary words for each \(1\le n\le17\), enumeration of the balanced-support parameter tuples, and coefficient extraction from the finite arithmetic sum. It also evaluates the independent partial-fraction formula through \(n=84\). Running `python3 checker.py` from the folder containing the file prints three `PASS` lines. These checks corroborate the algebra but do not replace the proof for arbitrary \(n\).

## Relationship to prior work

The full-text 2025 work by He, Kari and Millan Arias connects \(k\)-mer counts to de Bruijn Eulerian reconstruction and proves approximation of prescribed frequency vectors. The present argument uses the established Euler criterion but **counts exactly** the feasible length-\(n\) **circular binary trigram profiles** for every \(n\); their Theorem 4.2 does not give this enumeration.

Varshney and Goyal's 2007 discussion counts **linear** Markov-type classes; the associated OEIS A132298 has initial values \(8,15,28,52\) at input lengths \(3,4,5,6\), unlike the circular counts \(4,6,8,13\) at those lengths. Jacquet, Knessl and Szpankowski count balanced matrices for **order-one** Markov sources and give asymptotics for that matrix family; that analysis neither supplies the exact order-two binary de Bruijn enumerator nor handles the support-connectivity corrections here. The publicly indexed prior two-read result on binary adjacent-pair multispectra concerns linear read length two, a strictly different observation. No claim of historical uniqueness or independent certification is made.

## Limitations

No enumeration is asserted for nonbinary alphabets, read lengths above three, or **linear** nonwraparound reads. The formula counts observable types, not the number of realizations per type, and does not by itself give optimal decoding under noise. Historical-priority checks are necessarily nonexhaustive; related Markov-type literature might contain an implicit equivalent specialization. Finite checker runs are not a proof of the infinite theorem. Independent review has not been performed.

## References

1. H. He, L. Kari, P. Millan Arias, *Bridging Chaos Game Representations and \(k\)-mer Frequencies of DNA Sequences*, arXiv:2506.22172, first posted 27 June 2025, https://arxiv.org/abs/2506.22172 (especially §§3–4).
2. L. R. Varshney, V. K. Goyal, *Benefiting from Disorder: Source Coding for Unordered Data*, arXiv:0708.2310, 2007, https://arxiv.org/html/0708.2310v1 (especially §VII-A).
3. P. Jacquet, C. Knessl, W. Szpankowski, *Counting Markov Types*, DMTCS (2010), https://doi.org/10.46298/dmtcs.2768 (especially pp. 388–390).
4. OEIS A132298, *Number of distinct Markov type classes of order 3 possible in binary strings of length \(n\)*, https://oeis.org/A132298 (linear, not circular, histograms).
5. *Exact binary two-multispectrum code size and singleton classification*, publicly indexed record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-binary-two-multispectrum-code-size-and-singleton-classific--13779c08da71 (linear length-two read multispectra; complete text was unavailable for this comparison).
