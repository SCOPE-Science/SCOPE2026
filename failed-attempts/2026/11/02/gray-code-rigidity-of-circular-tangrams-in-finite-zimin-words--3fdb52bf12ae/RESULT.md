# Gray-code rigidity of circular tangrams in finite Zimin words

## Finding
For every integer \(n\ge1\), define \(Z_0=\varepsilon\) and \(Z_n=Z_{n-1}a_n Z_{n-1}\), with distinct literal symbols \(a_1,\ldots,a_n\). Set \(N=2^n-1\). A *circular factor* of length \(\ell\le N\) begins at a position \(s\in\{0,\ldots,N-1\}\) and follows the word modulo \(N\) for exactly \(\ell\) symbols. An *even-Parikh factor* (a *tangram*) has even multiplicity of every symbol; an *abelian square* is a concatenation \(UV\) of nonempty blocks with equal Parikh vectors.

**Theorem.** The complete set of pairs \((s,d)\) giving circular even-Parikh factors of length \(2d\), equivalently circular abelian squares of that length, is
\[
\left\{(N-d,d):1\le d\le 2^{n-1}-1\right\}.
\]
For such \(d\), the unique factor equals \(\operatorname{suf}_d(Z_n)\operatorname{pre}_d(Z_n)\). Thus there are precisely \(2^{n-1}-1\) *positioned* circular tangrams, exactly one at each admissible even length, and there is no circular abelian cube of total length at most \(N\).

## Assumptions and scope
The alphabet consists of \(n\) pairwise distinct literal symbols; no identification or morphic coding of symbols is allowed. Positions are zero-based, circular factors wrap at most once, and their lengths never exceed \(N\). Distinct starts of the same circular factor are counted separately when counting positioned occurrences. For \(n=1\), the asserted set is empty. All other assertions quantify over every integer \(n\ge1\) and every permissible half-length or start.

## Proof
Write \(w_t\) for the symbol at one-based position \(t\in\{1,\ldots,N\}\). The recursion shows by induction on \(n\) that
\[
w_t=a_{1+\nu_2(t)}.
\]
Indeed, each smaller-rank copy occupies a translated interval of length \(2^{n-1}-1\); the new central position is \(2^{n-1}\), while \(\nu_2(t)\) is unchanged by adding \(2^{n-1}\) at positions below that power. The base case is immediate.

Encode the Parikh vector modulo two of the linear prefix of length \(t\) as \(P(t)\in\mathbb F_2^n\), with the coordinate for \(a_{j+1}\) being bit \(j\). For \(0\le t\le N\), the count of positions \(i\le t\) with \(\nu_2(i)=j\) is
\[
\left\lfloor\frac{t}{2^j}\right\rfloor-\left\lfloor\frac{t}{2^{j+1}}\right\rfloor.
\]
Modulo two, that is binary bit \(j\) of \(t\) exclusive-OR binary bit \(j+1\) of \(t\). Consequently,
\[
P(t)=G(t):=t\oplus(t\mathbin{\gg}1),
\]
where \(\oplus\) denotes bitwise exclusive-OR and \(\gg\) a right shift. This is the binary reflected Gray code on all \(n\)-bit integers, which is a bijection on \(\{0,\ldots,2^n-1\}\): the original binary bits are uniquely recovered by recursively taking suffix exclusive-ORs of its bits. In particular,
\[
P(N)=G(N)=2^{n-1}.
\]
Moreover, for indices \(0\le e,s\le N\),
\[
G(e)=G(s)\oplus2^{n-1}\quad\Longleftrightarrow\quad e=N-s.
\]
To see this, toggling only the most significant Gray bit toggles every binary digit of its inverse, exactly complementing the \(n\)-bit binary representation.

Fix \(1\le d\le\lfloor N/2\rfloor\) and a circular start \(0\le s<N\). If the length-\(2d\) circular factor does not cross the boundary, its parity vector is \(P(s+2d)\oplus P(s)\), which is nonzero by injectivity of \(G\) because \(2d>0\). If it crosses the boundary, put \(e=s+2d-N\), where \(0<e<s<N\). Its parity vector is
\[
P(N)\oplus P(s)\oplus P(e)=2^{n-1}\oplus G(s)\oplus G(e).
\]
This vanishes exactly when \(e=N-s\), and substituting \(e=s+2d-N\) gives \(s=N-d\). Conversely this start wraps with \(e=d\), and its parity is zero by the displayed identity. Hence there is exactly one circular even-Parikh factor at each even length, with the stated starting point.

Finally, \(Z_n\) is a palindrome by induction from its defining recursion. Hence \(\operatorname{suf}_d(Z_n)\) is the reversal of \(\operatorname{pre}_d(Z_n)\), so the two halves of the uniquely positioned even-Parikh factor have identical Parikh vectors. Thus every such factor is actually an abelian square, proving both set equalities and the total count. If an abelian cube \(ABC\) with blocks of common positive length \(d\) existed as a circular factor of total length \(3d\le N\), then \(AB\) and \(BC\) would be circular abelian squares of the same length \(2d\), beginning at distinct starts \(s\) and \(s+d\pmod N\). This contradicts uniqueness. The theorem follows.

## Verification
A standalone Python 3 checker independently constructs each \(Z_n\), enumerates *all* cyclic starts and all even lengths through \(N\), compares both the even-Parikh and abelian-square occurrence sets against the formula, and checks the Gray-prefix parity identity. It ran successfully for \(1\le n\le8\), with respective occurrence counts \(0,1,3,7,15,31,63,127\). To replay, run `python checker.py` from the delivered package. The universal assertion follows from the preceding proof rather than extrapolation from these tests.

## Relationship to prior work
Glen, Halldórsson and Kitaev (2010) establish linear abelian-square avoidance for finite Zimin words and study crucial abelian-power-free words. The circular square-free word literature of Aberkane and Currie (2004) motivates analyzing boundary-crossing repetitions but treats different binary words and ordinary powers. Rytter and Shur (2014) study Zimin pattern matching. Fici, Gagie, Kärkkäinen and Kempa (2014) use related palindrome structure in factorization. The present theorem answers a different, *circular* Parikh-question: a complete position-by-position classification of every tangram and every abelian square. The cited sources do not, in the inspected material, assert that classification or imply it by their stated conclusions. Literature coverage is not asserted to be exhaustive.

## Limitations
The result does not apply automatically to word morphic images, arbitrary Zimin factors, or cyclic traversals longer than one word. Counts are positioned circular occurrences, not counts of distinct lexical values across lengths. Only two-block equal-Parikh repetitions are classified exactly; circular abelian cubes are excluded as a consequence. Historical priority outside the inspected material remains uncertain, and independent mathematical audit has not been performed.

## References
- Aberkane, A., and Currie, J. D., *There exist binary circular 5/2+ power free words of every length*, Electronic Journal of Combinatorics 11 (2004), R10, DOI: 10.37236/1763. Public paper dated January 23, 2004.
- Glen, A., Halldórsson, S., and Kitaev, S., *Crucial abelian k-power-free words*, Discrete Mathematics & Theoretical Computer Science 12(5) (2010), DOI: 10.46298/dmtcs.513.
- Rytter, W., and Shur, A. M., *On Searching Zimin Patterns*, arXiv:1409.8235 (2014).
- Fici, G., Gagie, T., Kärkkäinen, J., and Kempa, D., *A Subquadratic Algorithm for Minimum Palindromic Factorization*, arXiv:1403.2431 (2014).
