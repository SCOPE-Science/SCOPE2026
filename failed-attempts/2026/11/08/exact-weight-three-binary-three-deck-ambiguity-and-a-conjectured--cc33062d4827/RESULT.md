# Exact weight-three binary three-deck ambiguity and a conjectured generating function

## Finding

For each integer \(n\geq 3\), let \(\mathcal W_{n,3}\) consist of the binary words of length \(n\) with exactly three occurrences of \(1\). The **three-deck** \(\mathcal D_3(w)\) records, with multiplicity, all scattered subsequences of length three. Let \(D_{3,3}(n)\) be the number of three-decks realized by \(\mathcal W_{n,3}\).

**Theorem.** Every three-deck equivalence class within \(\mathcal W_{n,3}\) has size one or two. Write a word uniquely as
\[
 w_g=0^{g_0}1\,0^{g_1}1\,0^{g_2}1\,0^{g_3},\qquad
 g_i\in\mathbb Z_{\geq0},\quad\sum_{i=0}^3g_i=n-3.
\]
Its class has size two precisely if
\[
 t=\frac{g_1-g_2}{3}\in\mathbb Z\setminus\{0\},\qquad
 g_0+t\geq0,\quad g_3-t\geq0.
\]
The other member is exactly the word with gap vector
\[
 I(g)=(g_0+t,g_2,g_1,g_3-t).
\]
This is an involution on the ambiguous words, and every other word has a singleton class. If \(c_n\) is the number of doubleton classes, then
\[
 c_n=\sum_{t=1}^{\lfloor(n-3)/4\rfloor}
 \sum_{h=0}^{\lfloor(n-3-4t)/2\rfloor}
 (n-2-4t-2h),
\]
where empty sums are zero, and
\[
 \boxed{\sum_{n\geq3}D_{3,3}(n)z^n
  =\frac{z^3}{(1-z)^4}
  -\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.}
\]
In particular, this establishes the exact formula proposed as **Conjecture 1** in Chrisnata, Kiah, Karingula, Vardy, Yaakobi and Yao, *On the Number of Distinct \(k\)-Decks: Enumeration and Bounds* (Advances in Mathematics of Communications, DOI:10.3934/amc.2021032, Section 5.3).

Equivalently, the doubleton count is the following degree-three quasipolynomial of period dividing four:
\[
 c_n=\begin{cases}
 \dfrac{n(n-4)(n-5)}{48},&n\equiv0\pmod4,\\[4pt]
 \dfrac{(n-1)(n-3)(n-5)}{48},&n\equiv1,3\pmod4,\\[4pt]
 \dfrac{(n-1)(n-2)(n-6)}{48},&n\equiv2\pmod4.
 \end{cases}
\]
The maximum number of length-\(n\), weight-three binary codewords distinguishable by their three-decks is exactly
\[
 D_{3,3}(n)=\binom n3-c_n
  =\frac{7}{48}n^3+O(n^2).
\]
Thus the proportion of the \(\binom n3\) possible weight-three source words retainable in a zero-error three-deck code tends to \(7/8\).

## Assumptions and scope

All positions are linearly ordered, not circular. A scattered subsequence is specified by three strictly increasing indices; multiplicities, not just existence, constitute the deck. The alphabet is \(\{0,1\}\); all source words have exactly three ones and \(n\geq3\). The empty-word case and decks of other lengths or weights are outside this statement. The zero-error code is restricted to this fixed-weight source family.

For distinct \(n\)-letter words with \(n\geq3\), three-deck equality also forces equality of their length and number of ones: the sum of deck entries equals \(\binom n3\), and the total number of ones over all three-letter subsequence occurrences is \(\binom{n-1}{2}\) times the source number of ones. Therefore the in-class classification cannot be bypassed by changing the length or content of a candidate word.

## Proof

**Step 1: linear constraints.** Put \(G=n-3\). The three deck entries containing exactly two ones satisfy
\[
 N(011,w_g)=3g_0+g_1,\qquad
 N(101,w_g)=2(g_1+g_2),\qquad
 N(110,w_g)=g_2+3g_3.
\]
Here \(N(v,w)\) counts the scattered occurrences of \(v\) in \(w\). If \(g'\) is another four-gap vector with the same three-deck, subtracting these equalities and the constraint \(\sum_i g_i'=\sum_i g_i\) yields
\[
 g'=g+t(1,-3,3,-1),\qquad t\in\mathbb Z.
\]
Conversely, this displacement preserves the three two-one counts and the total zero count. The parameter \(t=g'_0-g_0\) is integral because the gap entries are integers.

**Step 2: the decisive quadratic constraint.** Define \(H_0=g_0\), \(H_1=g_0+g_1\), and \(H_2=g_0+g_1+g_2\). These are the numbers of zeros before each of the three successive ones. Then
\[
 N(001,w_g)=\sum_{j=0}^2\binom{H_j}{2},\quad
 N(010,w_g)=\sum_{j=0}^2H_j(G-H_j),\quad
 N(100,w_g)=\sum_{j=0}^2\binom{G-H_j}{2}.
\]
Under the displacement in Step 1, the triple of \(H\)-values changes by \((t,-2t,t)\). Its sum is unchanged, while
\[
 \sum_{j=0}^2 (H_j'^2-H_j^2)
 =2t(H_0-2H_1+H_2)+6t^2
 =2t(g_2-g_1+3t).
\]
Equality of the \(001\) entry therefore forces
\[
 t=0\quad\text{or}\quad t=\frac{g_1-g_2}{3}.
\]
For the nonzero choice, the resulting vector has the form \((g_0+t,g_2,g_1,g_3-t)\). It is valid exactly when the two displayed outer-gap inequalities hold; the two middle gaps are automatically nonnegative. Every one-zero entry is then preserved because the sum and sum of squares of \(H_0,H_1,H_2\) are preserved. The remaining \(000\) and \(111\) counts are \(\binom G3\) and \(1\), respectively, and are unchanged. Thus the stated conditions are both necessary and sufficient for equality of all eight deck entries.

If \(t\ne0\), the new middle-gap difference is \(g'_1-g'_2=g_2-g_1=-3t\), so applying the same construction again uses \(-t\) and returns \(g\). This proves involutivity, the exact partnership and the upper bound of two on class size.

**Step 3: count each doubleton once.** Orient each two-element class by choosing the member for which the nonzero displacement parameter is \(t>0\). Every such member is written uniquely as
\[
 g=(u,h+3t,h,v+t),\qquad
 u,v,h\in\mathbb Z_{\geq0},\quad t\in\mathbb Z_{\geq1}.
\]
Its partner is \((u+t,h,h+3t,v)\). The total number of zeros is
\[
 G=u+v+2h+4t.
\]
For each feasible pair \((t,h)\), there are exactly \(G-4t-2h+1=n-2-4t-2h\) nonnegative choices of \((u,v)\). These are precisely the terms in the displayed finite double sum. Summing with a formal variable gives the generating function of doubleton classes:
\[
 \sum_{n\geq3}c_nz^n
 =\sum_{u,v,h\geq0}\sum_{t\geq1} z^{3+u+v+2h+4t}
 =\frac{z^7}{(1-z)^2(1-z^2)(1-z^4)}.
\]
Since there are exactly \(\binom n3\) source words and each doubleton decreases the number of classes by one, \(D_{3,3}(n)=\binom n3-c_n\). Summing the binomial coefficients gives \(\sum_{n\geq3}\binom n3z^n=z^3/(1-z)^4\), proving the conjectured generating function.

For a direct closed-form extraction, write \(m=G-4t\). The inner sum over \(h\) is \((q+1)^2\) when \(m=2q\), and \((q+1)(q+2)\) when \(m=2q+1\). On increasing \(t\) by one, \(q\) decreases by two. Summing the resulting squares or consecutive products in each congruence class modulo four yields the displayed quasipolynomial, including the zero cases \(n=3,4,5,6\). Finally \(c_n=n^3/48+O(n^2)\), while \(\binom n3=n^3/6+O(n^2)\), giving the \(7/8\) asymptotic fraction.

## Verification

The accompanying `verify_deck3.py` constructs every weight-three binary word of length \(3\leq n\leq19\), computes full three-decks, forms all exact equivalence classes and checks each proposed partner. For \(n\leq16\), it also independently counts all index triples directly and compares with dynamic subsequence counting. There are 4,845 words and 370 doubletons across the seventeen tested lengths. Further seeded longer-word samples test the involution, and integer double-sum and quasipolynomial formulas are compared through length 400.

The complete infinite theorem follows from Steps 1–3, not from finite enumeration. The checker serves as an independently implemented finite cross-check. Reproduce using Python 3 with `python verify_deck3.py`; no external packages or data are required.

## Relationship to prior work

Chrisnata et al. give the null-vector \((1,-3,3,-1)\), study a partial ordering of the \(001\) counts, exhibit the length-seven pair `1000110` and `0110001`, prove the cubic-order bound, and state the **exact generating function as Conjecture 1** (Section 5.3, pp. 15–17). The expression is therefore *conjectured prior work*, not presented here as a newly guessed sequence. The new contribution is a complete necessary-and-sufficient two-member involution, its proof, a bijective enumeration of every collision, and hence a proof of their all-length conjecture.

Nilforoushan and Parvaresh (public preprint dated September 19, 2026) develop independent coordinates and the global \(\Theta(n^9)\) binary-three-deck enumeration. Those global bounds, and their discussion of fixed-content fibers, do not imply the exact weight-three count. Angal et al. (public preprint October 30, 2026) study reconstruction thresholds for restricted classes including fixed numbers of ones; their general fixed-one theorem assumes at least five ones and does not settle this exact three-one equivalence spectrum. Lejeune, Rigo and Rosenfeld (2020) establish general binomial-equivalence theory and an algorithm for two-binomial classes, not this three-deck classification.

## Limitations

This is a theorem for the exact three-deck on binary words with exactly three ones. It does not classify the weight-four slice, the full unrestricted binary three-deck, noisy observations, or deck lengths other than three. An independent mathematical audit has not been performed. Research-index and accessible-primary-text comparisons do not exclude undiscovered equivalent proofs or later independent work; definitive bibliographic priority remains an open verification matter.

## References

- J. Chrisnata, H. M. Kiah, S. R. Karingula, A. Vardy, E. Yaakobi, H. Yao, *On the Number of Distinct \(k\)-Decks: Enumeration and Bounds*, Advances in Mathematics of Communications 17(4) (2023), 960–978; DOI:10.3934/amc.2021032. Full manuscript: https://yaakobi.net.technion.ac.il/files/2022/08/60_k_Decks_Disc_Math21.pdf; particularly Section 5.3, Conjecture 1.
- A. Nilforoushan, F. Parvaresh, *Improved upper bound on the number of distinct \(k\)-decks for any \(k\) and alphabet size by counting the independent parameters*, arXiv:2609.23106 (first public September 19, 2026), https://arxiv.org/abs/2609.23106.
- K. Angal, R. Ascoli, S. X. He, X. He, L. Post, A. O. Soe, O. Zhukova, *Deck Reconstruction for Restricted Word Classes*, arXiv:2610.41110v1 (first public October 30, 2026), https://arxiv.org/html/2610.41110v1.
- M. Lejeune, M. Rigo, M. Rosenfeld, *On the Binomial Equivalence Classes of Finite Words*, International Journal of Algebra and Computation 30 (2020), https://orbi.uliege.be/bitstream/2268/249124/1/LejeuneRigoRosenfeld-ijacVersion2.pdf.
