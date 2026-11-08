# Exact quasiperiod spectra of three-marker binary words

## Finding

A *quasiperiod* (or *proper cover*) of a finite word is a nonempty proper factor all of whose occurrences, taken together, cover every position of the word. Let \(q(w)\) be the number of distinct quasiperiods of \(w\), and let \(F_j(z)=\sum_{n\ge3} f_j(n)z^n\), where \(f_j(n)\) counts **indexed** length-\(n\) binary words with exactly three ones and \(q(w)=j\).

Every such word has \(q(w)\in\{0,1,2\}\), and all three generating functions are determined explicitly. Define

\[
A(z)=\frac{z^3(1+z^3)}{(1-z^3)(1-z)^2}\left(\frac1{1-z^4}-\frac{2z}{1-z^5}+\frac{z^2}{1-z^6}\right),
\]
\[
B(z)=\frac{z}{(1-z)^2}\left(\frac{z^2}{1-z^2}-\frac{2z^3}{1-z^3}+\frac{z^4}{1-z^4}\right),\qquad
C(z)=\frac{z^3}{(1-z^3)^2(1-z^4)}.
\]
Then

\[
\boxed{F_2(z)=C(z),\qquad F_1(z)=A(z)+B(z)-2C(z),\qquad
F_0(z)=\frac{z^3}{(1-z)^4}-A(z)-B(z)+C(z).}
\]

Consequently, if \(W_n\) is uniformly distributed over all length-\(n\) words with three ones, then

\[
\boxed{\lim_{n\to\infty}\Pr(q(W_n)>0)=\frac1{90},\qquad
\Pr(q(W_n)=2)\sim\frac1{12n}.}
\]

More precisely, the complete criterion for each possible quasiperiod follows from the four positive/zero gap parameters below. This is a classification of all quasiperiods, not merely a count of words possessing one.

## Assumptions and scope

The alphabet is \(\{0,1\}\); words are linear and indexed rather than identified under reversal or rotation. The symbol \(1\) occurs **exactly three times**. Write uniquely

\[
w=0^p\,1\,0^{d-1}\,1\,0^{e-1}\,1\,0^c,
\qquad p,c\in\mathbb Z_{\ge0},\quad d,e\in\mathbb Z_{\ge1},
\qquad n=p+d+e+c+1.
\]

A quasiperiod is **proper** (shorter than \(n\)), and overlapping occurrences are allowed. It must be a prefix and a suffix because the first and last positions need coverage. Define predicates

\[
\mathsf A:\quad p<\min(d,e),\quad c<\min(d,e),\quad\max(d,e)\le p+c+1;
\]
\[
\mathsf B:\quad d=e,\quad p<d,\quad c<d.
\]

Exactly one quasiperiod with one \(1\) exists if and only if \(\mathsf A\), namely the prefix \(0^p1 0^c\) of length \(p+c+1\). Exactly one quasiperiod with two \(1\)'s exists if and only if \(\mathsf B\), namely the prefix of length \(n-d\). There are no other quasiperiods. Therefore \(q(w)=\mathbf1_{\mathsf A}+\mathbf1_{\mathsf B}\).

## Proof

**1. No other quasiperiod type is possible.** Every occurrence of a zero-only factor avoids every position marked \(1\), so such a factor cannot cover \(w\). A factor containing all three ones cannot be both a proper prefix and a suffix: its first one would occupy the same relative position in both, implying a zero shift between the two required occurrences. Therefore a proper cover contains exactly one or exactly two ones. If a cover contains \(r\) ones, its prefix occurrence must contain the first \(r\) ones of \(w\), and its suffix occurrence the last \(r\); their relative positions force their start shift. Thus for each \(r=1,2\) the cover length is uniquely determined.

**2. One-one quasiperiod.** Its prefix occurrence must contain the first one at relative position \(p\) and its suffix occurrence the last one at that same relative position. The start shift is \(d+e\), so its length is necessarily \(n-d-e=p+c+1\), and the factor must be \(0^p1 0^c\). Each of the three ones must be covered by a distinct occurrence of this factor, whose only possible starts are \(0,d,d+e\). Such occurrences exist exactly when both adjacent one-to-one distances exceed \(p\) and \(c\): \(p,c<\min(d,e)\). Their intervals cover the whole word exactly when both gaps between successive starts are at most the factor length, i.e. \(\max(d,e)\le p+c+1\). This proves \(\mathsf A\), including sufficiency.

**3. Two-one quasiperiod.** The two ones in its prefix occurrence are at positions \(p,p+d\), whereas the two ones in its suffix occurrence are the last two of \(w\), at positions \(p+d,p+d+e\). Equality of their relative separations forces \(d=e\). The suffix begins at position \(d\), so its length is \(n-d\). The two-one requirement in both occurrences holds precisely when the initial and final zero runs have length less than \(d\): \(p<d\), \(c<d\). Conversely these conditions give the two identical prefix and suffix factors, with overlapping occurrence intervals because \(n-d\ge d\). They cover \(w\), proving \(\mathsf B\).

**4. Counting \(\mathsf A\).** Put \(a=\min(p,c)\) and \(h=|p-c|\). There is one orientation when \(h=0\) and two otherwise. The admissible distances are \(d,e=\max(p,c)+1+u\) and \(\max(p,c)+1+v\), with \(0\le u,v\le a\). The word length is \(n=4a+3h+3+u+v\). Summing the weights gives

\[
A(z)=z^3\left(1+2\sum_{h\ge1}z^{3h}\right)\sum_{a\ge0}z^{4a}(1+z+\cdots+z^a)^2,
\]
which simplifies to the displayed rational function.

**5. Counting \(\mathsf B\).** Fix \(d=e\ge1\). Then \(0\le p,c\le d-1\) and \(n=2d+1+p+c\), whence

\[
B(z)=\sum_{d\ge1}z^{2d+1}(1+z+\cdots+z^{d-1})^2.
\]
Expanding the two geometric sums gives the stated \(B(z)\).

**6. Counting the intersection.** Under \(\mathsf B\), condition \(\mathsf A\) reduces to \(p+c\ge d-1\). Setting \(p+c=d-1+h\), where \(0\le h\le d-1\), gives exactly \(d-h\) ordered pairs \((p,c)\), and word length \(3d+h\). Substitute \(k=d-h\ge1\):

\[
C(z)=\sum_{k\ge1}\sum_{h\ge0} k z^{3k+4h}
=\frac{z^3}{(1-z^3)^2(1-z^4)}.
\]

A word satisfies exactly two conditions precisely when it has two distinct quasiperiods; exactly one condition when it has one. Inclusion-exclusion therefore yields the displayed \(F_0,F_1,F_2\). The total generating function for three-one words is \(z^3/(1-z)^4\).

**7. Asymptotics.** As \(z\to1\),

\[
(1-z)^4 A(z)\longrightarrow\frac1{90},\quad
(1-z)^3 B(z)\longrightarrow\frac1{12},\quad
(1-z)^3 C(z)\longrightarrow\frac1{36}.
\]
All rational-function poles lie at roots of unity; at other roots their orders are strictly smaller than the displayed principal pole orders. By partial fractions, \([z^n]A(z)=n^3/540+O(n^2)\), \([z^n]B(z)=n^2/24+O(n)\), and \([z^n]C(z)=n^2/72+O(n)\). Dividing \([z^n](A+B-C)\) and \([z^n]C\) by \(\binom n3=n^3/6+O(n^2)\) proves the two probability claims.

## Verification

The accompanying dependency-free script `verify.py` computes every proper cover directly from occurrences and position coverage. It independently compares the resulting classification and all three count arrays for every binary word with three ones and lengths \(3\) through \(25\) (\(14,950\) words). Two distinct implementations of the rational coefficients and integer-parameter counts agree through degree \(65\). Running `python3 verify.py` printed `VERIFY_OK words 14950 lengths 3..25 GF coefficients 0..65`. These are finite checks of the formulas; the unrestricted conclusion follows from the seven proof steps above.

For example, the number of words with two quasiperiods at lengths \(n=3,4,5,6,7,8,9\) is respectively \(1,0,0,2,1,0,3\).

## Relationship to prior work

Quasiperiods as full covers of strings are classical. Levé and Richomme (2013) study how morphisms create finite and infinite quasiperiodic words, and Gamard and Richomme (2016) study the structure of quasiperiod sets of **right-infinite** words. The 2012 survey by Smyth treats algorithms for finding covers and related repetitions, and OEIS A320434 tabulates the **unrestricted** number of quasiperiodic binary words. None of those inspected results supplies the simultaneous classification by marker gaps, the three exact **fixed-weight** quasiperiod-count generating functions, or the fixed-weight limiting probability here. Algorithms to compute covers from a given string are not themselves an enumeration of the fixed-content families.

## Limitations

Only linear binary words with exactly three ones are classified. The formula does not count covers of different lengths as separate occurrences, count words up to reversal, cover words with four or more ones, or apply to infinite words. The scientific priority conclusion is qualified: an unindexed or implicit equivalent enumeration could exist. Independent mathematical review has not been performed.

## References

- F. Levé and G. Richomme, *On Quasiperiodic Morphisms* (first public arXiv version, 2013-04-23), https://arxiv.org/abs/1304.6280.
- G. Gamard and G. Richomme, *Determining Sets of Quasiperiods of Infinite Words*, MFCS 2016, https://doi.org/10.4230/LIPIcs.MFCS.2016.40.
- W. F. Smyth, *Computing regularities in strings: A survey*, European Journal of Combinatorics, https://doi.org/10.1016/j.ejc.2012.07.010.
- OEIS A320434, *Number of length-n quasiperiodic binary strings*, https://oeis.org/A320434.
