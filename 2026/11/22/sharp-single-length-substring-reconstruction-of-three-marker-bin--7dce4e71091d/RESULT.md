# Sharp single-length substring reconstruction of three-marker binary words

## Finding

For integers \(n\ge8\) and \(1\le k\le n\), let \(\mathcal B_{n,3}\) consist of length-\(n\) binary words having exactly three occurrences of \(1\). For \(w\in\mathcal B_{n,3}\), denote by \(\mathcal D_k(w)\) the **multiset of all contiguous length-\(k\) substrings**, including overlapping occurrences and multiplicities. This is not the scattered-subsequence deck.

Define
\[
 r_* =\left\lceil\frac{n+2}{4}\right\rceil,\qquad
 k_* =n-r_*+1.
\]
Then \(\mathcal D_k\) is injective on \(\mathcal B_{n,3}\) for every \(k>k_*\); at \(k=k_*\), there exist distinct members with equal decks. More strongly, in the injective regime, the \(k\) numbers of ones observed at each *offset within the unordered reads* suffice to reconstruct the source. Consequently \(k_*\) is the exact **largest ambiguous read length**, and the least length above which *every* length is identifying is
\[
 K(n)=n-\left\lceil\frac{n+2}{4}\right\rceil+2.
\]
This is a statement about the last ambiguity: there can be smaller identifying lengths followed by another ambiguous length.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). The source word is *linear*, not circular; it has known length \(n\) and known exact Hamming weight three. Each of its \(r=n-k+1\) overlapping windows contributes to the read multiset. No ordering or positions of reads are supplied, but letters *within* a read remain in their original order. Coordinates in proofs are zero-based. The claim applies to every integer \(n\ge8\), and every asserted large-read length \(k>k_*\) up to \(n\).

## Proof

**1. Observable column marginals.** Given the unordered deck, for \(0\le t\le k-1\) let
\[
 c_t=\sum_{u\in\mathcal D_k(w)}u_t
     =\sum_{j=0}^{r-1}w_{t+j},
\]
where the first sum counts each read with its multiplicity. Subtract consecutive marginals:
\[
 d_t=c_{t+1}-c_t=w_{t+r}-w_t,
 \qquad 0\le t\le k-2=n-r-1.
\]
Thus for each residue class modulo \(r\), the differences between **successive entries** of its position chain are known. A binary chain with any nonzero difference is uniquely reconstructible: the sign of the first nonzero difference determines its preceding bit (\(+1\) means \(0\), \(-1\) means \(1\)), after which all entries are forced by differences. A chain whose differences all vanish is constant, and its value is the only potential unknown.

**2. Rigidity at weight three.** If \(k>k_*\), then \(r\le r_*-1\). By the ceiling definition, \(n\ge4r-1\). There are \(r\) residue chains, with lengths differing by at most one. Under \(n\ge4r-1\), all have at least four entries except possibly exactly one chain, which may have exactly three; when \(r=1\), the single chain has length \(n\ge8\). Since the entire word contains only three ones, any constant chain of length at least four must be all zeros. All nonconstant chains are already reconstructed by their signed differences. The only possible remaining constant chain has three entries and is determined by the total source weight: it is all ones precisely when none of the already determined chains contains a one, and is all zeros otherwise. Thus the column marginals recover \(w\) uniquely, and so does the full deck, for every \(k>k_*\).

**3. Exact witnesses at \(k_*\).** Let \(r=r_*\) and \(k=k_*=n-r+1\). For \(n\ge8\), elementary ceiling inequalities give \(r\ge3\) and \(2r\le n\le4r-2\), hence write \(n=hr+b\) with \(h\in\{2,3\}\) and \(0\le b<r\). For each phase \(a\in\{0,\ldots,r-1\}\), form
\[
 w^{(a)}_j=\mathbf 1_{\{j\equiv a\pmod r\}},
 \qquad 0\le j<n.
\]
If \(h=2\), exactly \(h+1=3\) ones occur in the source when \(0\le a<b\); in this case \(b\ge2\). If \(h=3\), exactly \(h=3\) occur when \(b\le a<r\), and \(r-b\ge2\) because \(n\le4r-2\). So in either case at least two distinct phases lie in \(\mathcal B_{n,3}\). Now \(\mathcal D_k(w^{(a)})\) consists of the length-\(k\) substrings beginning at positions \(0,\ldots,r-1\), namely *one from each residue modulo the period \(r\)*. Changing the phase merely permutes these starts. Therefore all eligible phases have the **identical multiset** of reads. Distinct phases give distinct words since \(r\le n\) and the single-one period is primitive. This proves ambiguity at \(k_*\).

**4. Threshold conclusion.** Step 2 proves every strictly larger length is identifying, and Step 3 supplies collision at \(k_*\). Together these establish both claimed sharp formulas. The construction has at least two witnesses for each stated \(n\). \(\square\)

## Verification

The standalone program `verify_sparse3.py` independently generates complete unordered decks for all \(\binom n3\) words at every \(n=8,\ldots,26\); it compares all length choices strictly above the predicted boundary and separately checks the strictly weaker offset-marginal fingerprint. It also checks that every \(n=8,\ldots,500\) admits at least two distinct explicit equal-deck periodic witnesses at the predicted boundary. Reproduce with `python verify_sparse3.py`; its captured output is `verification_output.txt`. The program contains assertions and raises an exception on failure. Its finite checks corroborate, but do not replace, the general proof.

## Relationship to prior work

Angal et al. (arXiv:2610.41110v1, first publicly posted October 30, 2026) investigate reconstruction of binary words of restricted types from the multiplicity deck of **scattered length-\(k\) subsequences**. Their fixed-weight restriction motivates this different *contiguous-window* observation channel; no implication between the respective formulas is asserted. Piña and Uzcátegui (2008) study equality of **all** contiguous factor multisets \(\mathcal D_i\) up to a cutoff, whose simultaneous information is different and stronger than only one \(\mathcal D_k\). Other existing results treat cyclic necklaces, short fixed three-mer decks or two-marker linear sources. None of the inspected claims supplies this exact linear three-marker last-ambiguity boundary or the offset-marginal rigidity assertion. The absence of an unindexed equivalent theorem has not been established.

## Limitations

The theorem assumes exact weight three, linear words and noiseless complete decks. It does not classify all exceptional fibers below the boundary, nor establish monotonicity of injectivity over smaller values of \(k\) (such monotonicity should not be presumed). The offset-marginal reconstruction argument relies critically on the at-most-three-one condition. Finite tests alone cannot verify unbounded \(n\). Historical priority remains subject to potentially unindexed equivalent work.

## References

1. K. Angal, R. Ascoli, S. X. He, X. He, L. Post, A. O. Soe, O. Zhukova, *Deck Reconstruction for Restricted Word Classes*, arXiv:2610.41110v1 (initial public submission 2026-10-30). https://arxiv.org/abs/2610.41110
2. C. Piña and C. Uzcátegui, *Reconstruction of a word from a multiset of its factors*, Theoretical Computer Science **400** (2008), 70–83. https://doi.org/10.1016/j.tcs.2008.01.052
