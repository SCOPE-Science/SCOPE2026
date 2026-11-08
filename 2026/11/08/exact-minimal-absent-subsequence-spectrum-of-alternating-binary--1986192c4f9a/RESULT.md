# Exact minimal-absent-subsequence spectrum of alternating binary words

## Finding

For every integer \(k\ge1\), let \(W_k=(01)^k\), let \(\mathcal M_k\) be the words absent as scattered subsequences of \(W_k\) whose every proper scattered subsequence occurs in \(W_k\), and let \(a_{k,\ell}=\#\{v\in\mathcal M_k:|v|=\ell\}\). Define the weak-descent statistic
\[
D(v)=\#\{i:2\le i\le |v|,\ v_{i-1}\ge v_i\},\qquad v\in\{0,1\}^{|v|}.
\]
The complete membership classification is
\[
\boxed{\mathcal M_k=\{v\in\{0,1\}^{\ge2}:D(v)=k,\ v_1\ge v_2,\ v_{|v|-1}\ge v_{|v|},\ \text{neither }010\text{ nor }101\text{ occurs contiguously in }v\}.}
\]
In particular, \(k+1\le |v|\le2k\) for each \(v\in\mathcal M_k\). The exact length-resolved generating function is
\[
\boxed{\sum_{k\ge1}\sum_{\ell\ge2}a_{k,\ell}z^k y^\ell=\frac{y^2z(3-2yz+y^2z+2y^3z^2)}{1-2yz+y^2z^2-y^4z^3}.}
\]
Writing \(a_k=\#\mathcal M_k\), this specializes to
\[
\sum_{k\ge1}a_kz^k=\frac{z(3-z+2z^2)}{1-2z+z^2-z^3},\qquad
(a_1,a_2,a_3,a_4,a_5,a_6,a_7)=(3,5,9,16,28,49,86),
\]
with recurrence \(a_k=2a_{k-1}-a_{k-2}+a_{k-3}\) for every \(k\ge4\). Consequently \(a_k\sim C\lambda^k\), where \(\lambda\approx1.754877666246693\) is the unique real root of \(\lambda^3-2\lambda^2+\lambda-1=0\) greater than one, and \(C\approx1.6787356025941633\). This is exponential minimal-absence growth already on the binary alphabet, while the number of *shortest* absent subsequences is exactly \(k+2\).

## Assumptions and scope

The ambient alphabet is exactly \(\{0,1\}\). A scattered subsequence preserves the order of selected symbols but need not be contiguous; a *proper* scattered subsequence is obtained by one or more deletions. A word is minimal absent precisely when it is absent and each one-letter deletion is present, since subsequence containment is transitive. Positions in \(W_k\) are indexed \(0,1,\ldots,2k-1\), and the infinite alternating word begins with \(0\). The indeterminates \(z,y\) are formal, marking the number of complete alternating blocks and candidate length. There are no restrictions on \(k\) other than \(k\ge1\).

## Proof

**1. An exact subsequence test.** Greedily embed a nonempty binary candidate \(v=v_1\cdots v_\ell\) in \(010101\cdots\). Its first matched position is \(v_1\). If a next symbol is different, the position advances by one; if it is equal, the position advances by two. Equivalently, for every neighboring pair \((a,b)\), the advance equals \(b-a+2\mathbf1_{\{a\ge b\}}\), as one checks for the four binary pairs. Summation telescopes, so the last matched zero-based position is exactly \(v_\ell+2D(v)\). Greedy matching is optimal for subsequence containment. Thus
\[
v\preceq W_k\quad\Longleftrightarrow\quad v_\ell+2D(v)\le2k-1\quad\Longleftrightarrow\quad D(v)\le k-1.
\]
The empty word is always a subsequence, and no one-letter word is absent.

**2. Minimality under deletion.** Removing an interior letter from a binary triple \(abc\) changes the weak-descent number by
\[
\Delta(a,b,c)=\mathbf1_{\{a\ge b\}}+\mathbf1_{\{b\ge c\}}-\mathbf1_{\{a\ge c\}}\in\{0,1\}.
\]
Direct evaluation of the eight triples shows \(\Delta=0\) exactly for \(010\) and \(101\), and \(\Delta=1\) otherwise. Deleting the first (respectively last) letter decreases \(D\) by one exactly when the first (respectively last) neighboring pair is weakly descending. Therefore each deletion decreases \(D\) by at most one, and all one-letter deletions of an absent \(v\) are present if and only if \(D(v)=k\), both boundary pairs descend and no interior triple is alternating. Necessity of \(D(v)=k\) follows since if \(D(v)\ge k+1\), every deletion still has at least \(k\) descents and is absent. This proves the classification, including the length-two boundary case.

The minimum length is \(k+1\), because \(D(v)=k\le\ell-1\). If the first pair is descending and the word avoids alternating triples, each strict ascent \(01\) is followed by a weak descent (the next pair is necessarily \(11\), unless at the end, which is forbidden by the final descending-pair condition). Such pairs can be chosen distinct from all strict ascents, and the first pair is an additional descent; hence the number of ascents is at most \(k-1\). Thus \(\ell-1=k+\#\{\text{ascents}\}\le2k-1\), giving \(\ell\le2k\).

**3. Rational generating function.** Use pair states in the order \(00,01,10,11\). To append a symbol, attach weight \(z\) when the new pair is weakly descending and weight one otherwise; forbid any transition whose three-letter window is \(010\) or \(101\). The exact transition matrix and boundary row are
\[
T(z)=\begin{pmatrix}z&1&0&0\\0&0&0&z\\z&0&0&0\\0&0&z&z\end{pmatrix},\qquad e=(1,0,1,1).
\]
The initial two letters contribute weight \(y^2z\), and the two boundary pairs must belong to the support of \(e\). Therefore the generating function of all characterized words, with descent number recorded by \(z\), is the formal matrix series
\[
G(z,y)=y^2z\,e\,(I-yT(z))^{-1}e^{\mathsf T}.
\]
Expanding the four-by-four inverse (or multiplying by its adjugate) yields
\[
G(z,y)=\frac{y^2z(3-2yz+y^2z+2y^3z^2)}{1-2yz+y^2z^2-y^4z^3}.
\]
Since the coefficient of \(z^k y^\ell\) counts exactly the characterized minimal absent words, the bivariate theorem follows. Substituting \(y=1\) gives the univariate formula; multiplying by its denominator gives the stated recurrence. The shortest absent candidates satisfy \(D(v)=k\) at length \(k+1\) if and only if every adjacent pair weakly descends, so they are exactly the \(k+2\) words \(1^a0^{k+1-a}\) for \(0\le a\le k+1\).

**4. Asymptotic.** Let \(Q(z)=1-2z+z^2-z^3\) and \(N(z)=z(3-z+2z^2)\). The cubic \(\lambda^3-2\lambda^2+\lambda-1\) has derivative \((\lambda-1)(3\lambda-1)\) and is strictly increasing on \((1,\infty)\), with opposite signs at one and two. Its other two roots form a conjugate pair of modulus \(\sqrt{1/\lambda}\) (product of all roots is one), strictly smaller than \(\lambda\). Consequently \(r=1/\lambda\) is the unique singularity of \(N/Q\) of smallest modulus; its zero is simple, and \(N(r)\ne0\). The simple-pole coefficient rule gives
\[
a_k=C\lambda^k+O(\gamma^k),\qquad C=-\frac{N(r)}{rQ'(r)}>0,
\]
for some \(\gamma<\lambda\), and gives the displayed numerical values. This is a proof of exponential growth for all large \(k\), not an extrapolation from finite enumeration.

## Verification

The accompanying standalone `verify.py` recomputes minimal-absence membership by direct greedy subsequence matching and one-letter deletions, without using the theorem's descent characterization. It compares every binary word of lengths at most \(2k+2\) for \(1\le k\le7\) against the proposed criterion, checks each exact length distribution against a separate weighted-state dynamic program, and verifies the univariate recurrence. Run `python3 verify.py` in the same extracted directory. These finite tests corroborate, but do not replace, the all-\(k\) proof above.

## Relationship to prior work

Kosche, Koß, Manea and Siemer introduced and characterized minimal absent scattered subsequences and, in their Proposition 3.6, proved that for the canonical periodic family \(B_k=(1\cdots\sigma)^k\), the number of minimal absent subsequences is exponential for sufficiently large *fixed even* alphabet size \(\sigma\ge4\), whereas shortest absent subsequences are polynomially many. The present theorem settles the missing binary case of that same family with an exact length spectrum, a finite forbidden-pattern description, and a growth constant; it does not claim novelty for the general definition, the higher-alphabet exponential lower bound, or general enumeration algorithms. Adamson et al. (2024) count absent words of specified length under universality constraints, a distinct question from minimal absent words across all lengths for one prescribed periodic family. Manea et al. (2025) give general enumeration algorithms, not this specialized closed form. No equivalent exact binary-family formula was identified in the sources or literature-index comparisons consulted, but this does not prove global bibliographic uniqueness.

## Limitations

The exact formula applies to \(W_k=(01)^k\) and its symbol-renamed counterparts, not arbitrary binary input words or larger alphabets. It describes minimal *scattered-subsequence* absence, not minimal absent contiguous factors. The work does not assert an algorithmic improvement over general enumeration methods. No independent scientific validation or complete global literature certification has been performed; an equivalent formula in unindexed or differently named prior work may exist.

## References

- M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, first public 2021-08-31, especially Section 3 and Proposition 3.6. https://arxiv.org/abs/2108.13968
- D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599, first public 2024-07-26. https://arxiv.org/abs/2407.18599
- F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471, first public 2025-04-30. https://arxiv.org/abs/2504.21471
