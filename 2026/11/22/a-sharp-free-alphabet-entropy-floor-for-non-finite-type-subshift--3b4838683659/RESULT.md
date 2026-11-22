# A sharp free-alphabet entropy floor for non-finite-type subshifts

## Finding

For every nonempty, two-sided subshift \(X\subseteq A^{\mathbb Z}\) over a finite alphabet, and every finite alphabet \(B\) of size \(q\ge2\), write \(Y=X\times B^{\mathbb Z}\), represented as a subshift over \(A\times B\). Define \(h_{\mathcal G}\) to be the infimum, over all sets of forbidden words generating a subshift, of their upper exponential word-count rates, with \(\log0=-\infty\).

**Theorem.** If \(X\) is not of finite type, then
\[
h_{\mathcal G}(X\times B^{\mathbb Z})\ \ge\ \log q.
\]
For every such \(X\), one also has the upper estimate
\[
h_{\mathcal G}(X\times B^{\mathbb Z})\ \le\ h_{\mathcal G}(X)+\log q.
\]
In particular, if \(h_{\mathcal G}(X)=0\), then equality holds at \(\log q\). If \(X\) is of finite type, so is the product, and its generating-forbidden-word entropy is \(-\infty\). Thus no non-finite-type base can have a free-\(q\)-alphabet product of generating-forbidden-word entropy below \(\log q\).

For the four-letter subshift \(X_*\) in Wu and Zhang's Example 1(2), the following **complete exact entropy triple** holds for every \(q\ge2\):
\[
\bigl(h_{\mathcal G},h_{\mathcal M},h_{\mathrm{top}}\bigr)(X_*\times B^{\mathbb Z})
=\bigl(\log q,\log(2q),\log(2q)\bigr).
\]
This triple is a corollary of the new universal product lower bound and the source's independently established entropy values for \(X_*\); the base system and those base values are not asserted to be new.

## Assumptions and scope

A subshift is a nonempty, closed, shift-invariant subset of \(A^{\mathbb Z}\), where \(A\) is finite. Its length-\(n\) language is \(\mathcal L_n(X)\). A word is *minimal forbidden* when it is not in the language while both its length-\((n-1)\) prefix and suffix are in the language (for \(n\ge2\)). This is equivalent to all proper contiguous subwords occurring. A subshift is not of finite type exactly when lengths of its minimal forbidden words are unbounded.

For a generating forbidden list \(\mathcal F\), put \(\mathcal F_n=\mathcal F\cap A^n\), and define
\[
\gamma(\mathcal F)=\limsup_{n\to\infty}n^{-1}\log|\mathcal F_n|,\qquad
h_{\mathcal G}(X)=\inf_{\Sigma_{\mathcal F}=X}\gamma(\mathcal F).
\]
Here the same convention \(\log0=-\infty\) is used throughout; \(\Sigma_{\mathcal F}\) is the set of all sequences avoiding every member of \(\mathcal F\). Also define \(h_{\mathcal M}\) by the upper exponential rate of the minimal-forbidden-word counts, and \(h_{\mathrm{top}}\) by the exponential growth of \(\mathcal L_n\). There is no mixing, irreducibility, positive-entropy, or ergodicity assumption.

## Proof

**1. Long single-obstruction splices.** Let \(X\) be non-finite-type. For arbitrarily large integers \(n\ge2\), take a minimal forbidden word \(u=u_0\cdots u_{n-1}\). The prefix \(u_0\cdots u_{n-2}\) occurs in a point \(x^-\in X\) at positions \(0,\ldots,n-2\). The suffix \(u_1\cdots u_{n-1}\) occurs in a point \(x^+\in X\) at positions \(1,\ldots,n-1\). Let \(z_i=x^-_i\) when \(i\le n-2\), and \(z_i=x^+_i\) when \(i\ge n-1\). Then \(z_{[0,n)}=u\), so \(z\notin X\), but \(z\) agrees with \(x^-\) at every index \(i\le n-2\) and with \(x^+\) at every index \(i\ge1\) (using the common overlap \(1,\ldots,n-2\)). Therefore *any* forbidden \(\ell\)-block occurring in \(z\) must start at \(i\le0\) and end at \(i+\ell-1\ge n-1\). Necessarily \(\ell\ge n\), and at most \(\ell-n+1\) start positions are possible.

**2. Uniform-noise obstruction.** Fix an arbitrary generating forbidden list \(\mathcal H\) for \(Y=X\times B^{\mathbb Z}\). Each member \(h\in\mathcal H_\ell\) has an \(A\)-projection absent from \(\mathcal L_\ell(X)\): if the projected word occurred in \(X\), every pairing with a \(B\)-word would occur in \(Y\), contradicting that \(h\) is forbidden. Give \(B^{\mathbb Z}\) its uniform iid measure. Every \((z,y)\) is outside \(Y\), so it contains some forbidden word from \(\mathcal H\) for every \(y\). For a fixed forbidden word of length \(\ell\), its \(B\)-projection matches uniform \(y\) at any prescribed site with probability exactly \(q^{-\ell}\). The count of possible sites from Step 1 and the countable union bound imply, for every length \(n\) of a minimal forbidden word,
\[
1\ \le\ \sum_{\ell\ge n}(\ell-n+1)|\mathcal H_\ell|q^{-\ell}
\ \le\ \sum_{\ell\ge n}\ell|\mathcal H_\ell|q^{-\ell}.
\]
Suppose \(\gamma(\mathcal H)<\log q\). Choose \(c<\log q\) strictly larger than \(\gamma(\mathcal H)\). For all sufficiently large \(\ell\), \(|\mathcal H_\ell|\le e^{c\ell}\). Hence the series in the rightmost expression converges, and its tails tend to zero as \(n\to\infty\). This contradicts the preceding inequality along the unbounded sequence of minimal-forbidden lengths. Thus \(\gamma(\mathcal H)\ge\log q\) for *every* \(\mathcal H\) generating \(Y\), proving the lower bound after infimizing.

**3. Upper bound and finite-type boundary.** For any forbidden generator \(\mathcal F\) of \(X\), lift each forbidden word of length \(n\) to its product with *every* \(B\)-word of length \(n\). The resulting \(\widehat{\mathcal F}\) generates \(Y\) and satisfies \(|\widehat{\mathcal F}_n|=q^n|\mathcal F_n|\). Consequently \(\gamma(\widehat{\mathcal F})=\gamma(\mathcal F)+\log q\), including the case \(\gamma=-\infty\). Infimizing gives the upper bound. A finite forbidden generator for \(X\) lifts to a finite one for \(Y\), making both entropies \(-\infty\); conversely, the lower bound rules out such a value for a non-finite-type \(X\).

**4. Exact motivating example.** On \(A=\{0,1,2,3\}\), take the generating forbidden list with short words \(02,12,23,30,31,32\) and, for every integer \(m\ge1\), all words \(2u3^{m^2+1}\) with \(u\in\{0,1\}^m\). Wu and Zhang prove that the resulting \(X_*\) has \(|\mathcal L_n(X_*)|=3\cdot2^n-2\), \(h_{\mathrm{top}}(X_*)=h_{\mathcal M}(X_*)=\log2\), and \(h_{\mathcal G}(X_*)=0\). The preceding lower and upper bounds give exactly \(h_{\mathcal G}(X_*\times B^{\mathbb Z})=\log q\). For the remaining two entropies, every minimal forbidden word of the product is exactly a minimal forbidden \(A\)-word paired with an arbitrary \(B\)-word of the same length, whence \(|\mathcal M_n(Y)|=q^n|\mathcal M_n(X_*)|\). Also \(|\mathcal L_n(Y)|=q^n|\mathcal L_n(X_*)|\). Taking exponential rates proves the displayed entropy triple.

## Verification

Run `python3 check.py` with Python 3 standard library only. It exhaustively checks \(4^n\) candidate words for the source example for each \(1\le n\le8\), compares its exact language counts, enumerates its minimal forbidden words, verifies free-alphabet scaling for \(q=2,3\) and \(1\le n\le4\), and checks the permitted splice-start count for a range of integer lengths. It is a *finite sanity check*, not an exhaustive verification of the infinite theorem; the infinite proof is Steps 1–4 above. The source paper's proof establishes the motivating base-example entropies.

## Relationship to prior work

Wu and Zhang [1] introduce \(h_{\mathcal G}\), prove the base-example entropies in Example 1(2), and prove an **upper** bound for the self-product \(X\times X\) (their Proposition 1). The present result gives a **universal lower bound** in the different setting \(X\times B^{\mathbb Z}\), for every non-finite-type \(X\), and an exact sharp value for zero-generating-entropy bases. The base-example definition, numerical language formula, and previously known base entropy values are credited to [1]. The older symmetric-constraint-entropy framework [2] concerns a different invariant, not an asserted equivalent of \(h_{\mathcal G}\). The novelty comparison concerns the new product lower bound and its consequence, not the general existence of minimal forbidden words or the trivial product-language identity.

## Limitations

The lower bound is specific to an **unrestricted independent full-shift coordinate**, and does not assert the same bound for a general positive-entropy second factor. For \(h_{\mathcal G}(X)>0\) it yields lower and upper bounds but does not determine the exact product value. Uniform-noise sampling is a proof device, not a probabilistic assumption on \(X\). Numerical finite-length checks are not the proof. Historical priority against undiscovered statements using equivalent generating-list notions remains provisional. No independent external mathematical audit has been performed.

## References

[1] X. Wu and X. Zhang, *Generating Forbidden Words and Measures of Maximal Entropy for Subshifts*, arXiv:2611.03758v1, first public 2026-11-02. https://arxiv.org/html/2611.03758v1 (Definitions (6), Example 1(2), Proposition 1).

[2] J. Buzzi, *Subshifts of quasi-finite type*, arXiv:math/0305164, https://arxiv.org/abs/math/0305164. Cited for background on symmetric constraint entropy, not claimed to establish the new product statement.
