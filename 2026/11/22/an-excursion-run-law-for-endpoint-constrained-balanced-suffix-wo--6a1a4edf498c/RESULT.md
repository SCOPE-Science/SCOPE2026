# An excursion-run law for endpoint-constrained balanced-suffix word games

## Finding

Consider the normal-play impartial game on every finite word over the ordered alphabet \(\{a,b\}\). A legal move removes a nonempty **contiguous suffix** with equally many \(a\)'s and \(b\)'s and with both its first and its last letter equal to \(a\). Denote the Sprague–Grundy number by \(G(w)\), with \(G(\varepsilon)=0\). This endpoint-constrained move language is neither the Dyck language nor the complete zero-sum language.

Read the reverse \(w^{\mathrm{rev}}\) as a walk from zero, giving \(a\) increment \(+1\) and \(b\) increment \(-1\). Decompose uniquely into successive nonempty *primitive returns* to level zero (walks with no interior zero), followed by a possibly empty terminal walk with no nonempty zero-return prefix. Write \(s=s_1\cdots s_\ell\in\{P,N\}^{*}\) for the signs of the successive primitive returns (\(P\): first step \(+1\); \(N\): first step \(-1\)). Then

\[
G(w)=\begin{cases}
0,&s=\varepsilon\text{ or }s_1=N,\\
\#\{\text{maximal nonempty runs of }N\text{ in }s\},&s_1=P.
\end{cases}
\]

Let \(A_{n,k}=\#\{w\in\{a,b\}^{n}:G(w)=k\}\). Define \(E(z)=\bigl(1-\sqrt{1-4z^2}\bigr)/2\) and \(M(z)=\sqrt{1-4z^2}/(1-2z)\), as formal power series. The complete exact distribution is given by

\[
\boxed{\displaystyle
\sum_{n,k\ge0}A_{n,k}z^nt^k
=M(z)\left(1+\frac{E(z)}{1-2E(z)}+
\frac{E(z)\bigl(1-E(z)+tE(z)\bigr)}{\bigl(1-E(z)\bigr)^2-tE(z)^2}\right).}
\]

Consequently, for all \(n\ge0\) and \(k\ge0\),

\[
A_{2n+1,k}=2A_{2n,k},\qquad
\max_{|w|=n}G(w)=\left\lfloor\frac n4\right\rfloor.
\]

Every integer between zero and that maximum is attained. For a uniformly random binary word \(W_n\), with \(Z\) a standard normal random variable,

\[
\boxed{\displaystyle
\frac{G(W_n)}{\sqrt n}\ \xrightarrow{\ d\ }\
\frac12\delta_0+\frac12\operatorname{Law}(|Z|/4).}
\]

In particular, the asymptotic law has a genuine atom of mass one half at zero even though the positive nimbers have order \(\sqrt n\).

## Assumptions and scope

All words are finite; alphabet letters are literal symbols. A suffix is contiguous, not scattered; it must have positive even length, equal counts of both letters, and both endpoints \(a\). A move removes the entire chosen suffix, leaving the preceding prefix. No other moves are allowed. The normal-play convention assigns Grundy value \(\operatorname{mex}\) of the option values, with the empty option set having Grundy value zero. All generating-function identities are in formal series about zero, and \(\sqrt{1-4z^2}\) is its branch with constant coefficient one. The asymptotic statement takes integers \(n\to\infty\) through both parities.

## Proof

**1. Unique excursion coordinates.** Reverse the word, and enumerate its successive first strictly positive times of return to height zero; each segment between returns is a primitive balanced walk and hence is wholly positive between its endpoints or wholly negative between its endpoints. Once the final return has occurred, the remaining segment is a zero-free meander (possibly empty). This decomposition is unique, including when there are no returns.

A move removing suffix \(v\) of the original word becomes removal of prefix \(v^{\mathrm{rev}}\) of the reversed word. The prefix is balanced exactly when it ends at one of the successive return times, so it consists of the first \(j\ge1\) complete excursions. It begins with \(a\) exactly when \(s_1=P\). It ends with \(a\) exactly when its final excursion is negative, i.e. \(s_j=N\): a positive primitive return ends in the \(-1\) letter \(b\), and a negative primitive return ends in \(+1\) letter \(a\). Thus, after discarding the invariant final meander, the game is the sign-word game whose legal options delete a nonempty prefix beginning \(P\) and ending \(N\).

**2. Exact nimber.** Proceed by induction on \(|s|\). An empty sign word or one beginning \(N\) has no legal move and value zero. Suppose \(s\) begins \(P\) and has \(r\) nonempty maximal \(N\)-runs. If \(r=0\), no move is legal. If \(r\ge1\), deleting through any letter of the \(j\)-th \(N\)-run leaves a suffix with at most \(r-j\) complete \(N\)-runs, so, by induction, any option has value at most \(r-1\). In particular, deleting precisely through the **last** letter of that run leaves a suffix beginning \(P\) with exactly \(r-j\) remaining \(N\)-runs when \(j<r\), and leaves either a \(P\)-only suffix or the empty sign string when \(j=r\). These \(r\) choices give option values \(r-1,r-2,\ldots,0\), respectively. The mex is therefore exactly \(r\). Note that this depends on **runs**, not the number of legal moves: for \(w=\mathtt{ababba}\), the sign string is \(PNN\), giving two moves and Grundy number one.

**3. Enumeration.** A primitive positive return has the form \(aDb\), where \(D\) is a Dyck word, and there are \(C_{m-1}\) such words of length \(2m\) (\(C_j\) is Catalan). A negative return has the same series by reflection. Thus the generating series for each signed primitive excursion is \(E(z)=\sum_{m\ge1}C_{m-1}z^{2m}\). The total binary-word series is \(1/(1-2z)\). Because an arbitrary word is a sequence of signed primitive returns followed by one terminal zero-free meander, its meander series is

\[
M(z)=\frac{1-2E(z)}{1-2z}=\frac{\sqrt{1-4z^2}}{1-2z}.
\]

The sign strings with no initial \(P\) have series \(1+E/(1-2E)\) and all have nimber zero. For sign strings beginning \(P\), write \(R=E/(1-E)\) for the generating series of a nonempty homogeneous sign run. They have the unique decomposition \(P^+(N^+P^+)^rN^{\ast}\) for \(r\ge0\), where the final optional nonempty \(N\)-run is separately marked. The corresponding run-weighted generating series is

\[
\frac{R}{1-tR^2}(1+tR)
=\frac{E(1-E+tE)}{(1-E)^2-tE^2}.
\]

Multiplication by \(M(z)\) accounts for the terminal incomplete meander and proves the boxed series. Setting \(t=1\) simplifies to \(1/(1-2z)\), as independently required.

Because \(E(z)\) contains only even powers, the bivariate series has the form \((1+2z)\Phi(z^2,t)\), proving \(A_{2n+1,k}=2A_{2n,k}\). Every \(N\)-run in a sign word beginning \(P\) requires at least one preceding positive primitive return and one negative primitive return, each of length at least two, so \(4G(w)\le|w|\). Equality is achieved with sign word \((PN)^k\) realized by the reverse of \((\mathtt{abba})^k\); extending with a zero-free terminal meander of length \(n-4k\) realizes the same value for any larger \(n\), and hence proves the maximum and complete support.

**4. Limit law.** Let \(L_n\) denote the number of complete excursions in a uniform length-\(n\) reversed word. Its bivariate generating series is \(M(z)/(1-2uE(z))\). The \(r\)-th factorial moment has generating series

\[
\frac{r!\,(2E(z))^r}{(1-2z)(1-2E(z))^r}
=\frac{r!\,(1-\sqrt{1-4z^2})^r}{(1-2z)(1-4z^2)^{r/2}}.
\]

Coefficient asymptotics as \(z\to1/2\) give

\[
\mathbb E[(L_n)_r]\sim\frac{r!}{2^{r/2}\Gamma(1+r/2)}\,n^{r/2}
=\mathbb E[|Z|^r]n^{r/2}.
\]

The same estimates at \(z=-1/2\) are lower order because the factor \(1-2z\) is then nonzero; thus parity causes no change to the leading constant. These moments are those of the moment-determinate half-normal distribution, and imply \(L_n/\sqrt n\Rightarrow|Z|\). In particular \(L_n\to\infty\) in probability.

Conditional on \(L_n=\ell\), the signs of the \(\ell\) excursions are independent unbiased \(P/N\) coins: exchanging \(a\) and \(b\) within each primitive excursion is a length-preserving bijection and leaves the terminal meander independent of those signs. The first sign is \(N\) with probability one half when \(\ell\ge1\), causing Grundy number zero. Conditional on its being \(P\), the number of \(N\)-runs is asymptotic to \(\ell/4\) by the law of large numbers for successive \(PN\) transitions (the difference from the \(N\)-run count is at most one), and concentration holds as \(\ell\to\infty\). Combining this conditional convergence, \(L_n/\sqrt n\Rightarrow|Z|\), and the unbiased first sign yields the stated mixture law.

## Verification

Standalone standard-library Python programs `verification/exhaustive.py` and `verification/series.py` are included with their exact output `verification/checks.txt`. The first recursively computes actual legal suffix moves and mex independently of the sign-word characterization, on every binary word of length at most 14 (32,767 nonempty words). The second computes exact coefficients of the displayed formal series through length 78, compares them with a separate first-return renewal dynamic program through length 50, and checks normalization, parity doubling, and sharp support. Both programs ran successfully. These computations are finite cross-checks, not substitutes for the infinite mathematical proof above.

## Relationship to prior work

Inoue and Inazu, *Word Subtraction Games*, arXiv:2611.09157 (first posted November 6, 2026), introduce the word-subtraction framework and study game positions and winning languages; the complete Grundy functions of particular nonregular subtraction languages motivate this question. The present endpoint-constrained balanced language is different from the Dyck-suffix language, for which nimbers are determined by completed Dyck factors, and from the full zero-sum suffix language, for which positions are counted by returns without endpoint constraints. Here two eligible deletion endpoints inside the same negative run can yield the same mex outcome, so neither simpler invariant determines these Grundy values.

The Catalan excursion series and the half-normal return-count limit use standard lattice-path methods. Hetyei's *Enumeration by kernel positions for strongly Bernoulli type truncation games on words* (arXiv:0912.0573) is a relevant earlier game-enumeration title; only its accessible abstract was available for comparison, so an equivalent special case cannot be ruled out from that source alone.

## Limitations

The theorem concerns precisely two letters and the simultaneous *equal-count* and *first/last letter \(a\)* suffix restrictions. It asserts no analogue for arbitrary endpoint patterns, three or more symbols, misère play, or other move languages. Priority against unindexed literature remains provisional, and the earlier kernel-position paper was not fully accessible. The verification programs confirm finite prefixes of the theorem only; the infinite assertions rest on the proofs above. The probabilistic limit is distributional, not a total-variation statement.

## References

- Y. Inoue and H. Inazu, *Word Subtraction Games*, arXiv:2611.09157, version 1 posted November 6, 2026, https://arxiv.org/abs/2611.09157.
- G. Hetyei, *Enumeration by kernel positions for strongly Bernoulli type truncation games on words*, arXiv:0912.0573, https://arxiv.org/abs/0912.0573.
- Standard Catalan first-return decomposition and the method of moments for the simple symmetric random walk (used as background, not as a claim of novelty).
