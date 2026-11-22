# Parity-unified exact deletion-fiber multiplicities of alternating binary prefixes

## Finding
Let \(H_n\) denote the length-\(n\) prefix of the infinite word `010101...`, with \(H_0\) empty. For integers \(n\ge d\ge0\), choose \(d\) deletion positions in \(H_n\) whose selected letters, in order, spell precisely \(H_d\). Let \(M_{n,d}(v)\) be the number of these **positional deletion choices** leaving a specified residual word \(v\), so distinct choices with the same residual retain their multiplicity.

Put \(r=n-d\), \(\ell=\lfloor r/2\rfloor\), and \(p=d\bmod2\). Every residual with nonzero multiplicity has the unique representation
\[
v=B_1\cdots B_\ell\,p^{\,r\bmod2},\qquad
B_i\in\{01,10\}.
\]
Here the final notation means append the single symbol \(p\) if \(r\) is odd, and append nothing otherwise. Encode \(B_i=01\) by \(x_i=0\), and \(B_i=10\) by \(x_i=1\). Set \(x_0=0\), \(x_{\ell+1}=p\), and
\[
T(v)=\sum_{i=0}^{\ell}{\bf1}\{x_i\ne x_{i+1}\}.
\]
**Exact fiber theorem:**
\[
\boxed{M_{n,d}(v)=
 \begin{cases}
 \displaystyle\binom{\ell+(d-T(v))/2}{\ell},&T(v)\le d,\\
 0,&T(v)>d.
 \end{cases}}
\]
A word not of the indicated paired form has multiplicity zero. The binomial is evaluated only in the displayed nonnegative case; \(T(v)\equiv d\pmod2\) automatically. In particular, for each \(t\le d\) with \(t\equiv p\pmod2\), **exactly** \(\binom{\ell+1}{t}\) different residuals have transition index \(t\), all with the same positive multiplicity \(\binom{\ell+(d-t)/2}{\ell}\). This is the complete positive deletion-fiber multiplicity histogram, not merely the set of possible residuals.

Consequently
\[
|C(H_n,H_d)|=
\sum_{\substack{0\le t\le\min(d,\ell+1)\\t\equiv d\ (\mathrm{mod}\,2)}}\binom{\ell+1}{t}
=\sum_{j=0}^{\min(d,\ell)}\binom{\ell}{j}.
\]
All \(2^\ell\) paired residuals are possible exactly when \(\ell\le d\); when \(\ell=d+1\) precisely one paired word is excluded, namely the alternating block-type sequence \(x_i=i\bmod2\). These statements include \(d=0\), \(r=0\), both endpoint parities and the empty source.

## Assumptions and scope
The source and deleted pattern are **linear** alternating prefixes beginning with \(0\), not cyclic words. An embedding is an increasing sequence of selected source positions. Different embeddings, even when leaving the same \(v\), count separately. The alphabet contains two distinct symbols labeled \(0,1\); any relabeling yields the same formulas. The claim is for every pair of nonnegative integers \(n\ge d\) and every residual \(v\in\{0,1\}^{n-d}\), without a finite-length cutoff. The first-public-date scope is supplied by the cited complement-scattered-factor research, not a date assigned to this theorem.

## Proof
**1. Even residual prefixes are balanced.** For any prefix of \(H_n\) or \(H_d\), its number of zeros minus ones is either \(0\) or \(1\). Consider an arbitrary even-length prefix of a residual arising from a valid deletion embedding. It consists of a source prefix with a prefix of \(H_d\) removed, hence its zero-minus-one discrepancy lies in \(\{-1,0,1\}\). Because that residual prefix has even length, its discrepancy is even, and therefore it is exactly zero. It follows that the first \(2\ell\) residual symbols split into balanced pairs, necessarily \(01\) or \(10\).

If \(r\) is odd, the total discrepancy of the residual equals \((n\bmod2)-(d\bmod2)\), which is \(+1\) when \(d\) is even and \(-1\) when \(d\) is odd. The remaining symbol is thus \(0\) for even \(d\), and \(1\) for odd \(d\), namely \(p\). This proves the required output form.

**2. No deletion lies inside a retained pair.** At each boundary after an even-length retained prefix, the discrepancy of that retained prefix is zero, so the source prefix and deleted \(H_d\) prefix have the same discrepancy. Both are alternating prefixes, so their lengths have the same parity. Their next letters, if present, consequently agree. At the first symbol of a retained pair \(B_i\), its initial symbol equals this common phase and is \(x_i\). After retaining it, the next source letter is \(1-x_i\), whereas the next not-yet-deleted pattern letter is still \(x_i\). Hence no deletion is possible before the second symbol \(1-x_i\) is retained. Both symbols of each retained pair therefore occupy consecutive source positions.

If the residual has a final unpaired letter \(p\), all remaining deletions must occur **before** that letter: just after retaining it the next source letter would be \(1-p\), whereas the next deleted-pattern letter would still be \(p\). The same phase reasoning excludes any subsequent deletion. Thus every embedding is uniquely described by \(\ell+1\) nonnegative gap counts \(g_0,\ldots,g_\ell\): one before the first pair, one between each consecutive pair, and one after the last pair (for even \(r\)) or before the final unpaired symbol (for odd \(r\)). There are no other deletion positions.

**3. The phase-gap bijection.** At every such gap the source and next required deleted-pattern letters have the same phase. Consequently deleting \(g_i\) consecutive source letters is always legal as long as the total deleted count is \(d\). Such a gap flips the phase of the next retained pair if and only if \(g_i\) is odd. It follows that
\[
 g_i\equiv x_i\oplus x_{i+1}\pmod2\quad(0\le i\le\ell),
\]
where \(x_0=0\), \(x_{\ell+1}=p\) and the final phase is the phase of the end (for even \(r\)) or the unpaired last letter (for odd \(r\)). All selected deletions spell \(H_d\), since each deleted gap begins in exactly the next required alternating phase and the intervening retained pair has even length.

Write the prescribed parity of gap \(i\) as \(e_i\in\{0,1\}\). Then \(\sum e_i=T(v)\), and every permissible gap vector is uniquely
\[
 g_i=e_i+2h_i,\qquad h_i\ge0,\qquad
 \sum_{i=0}^{\ell}h_i=(d-T(v))/2.
\]
If \(T(v)>d\), no such vector exists. Otherwise the right side is a nonnegative integer because the number of phase switches from \(x_0=0\) to \(x_{\ell+1}=p\) has parity \(p=d\bmod2\). By stars and bars, the number of weak compositions into \(\ell+1\) parts is \(\binom{\ell+(d-T(v))/2}{\ell}\). Conversely, every such gap vector spells the prescribed source \(H_n\) and realizes the prescribed deleted \(H_d\) and retained \(v\), so there are no extraneous or missing embeddings. This proves the exact fiber formula.

**4. Histogram, count and sharp boundary.** A block-type sequence is uniquely determined by its transition subset on the \(\ell+1\) edges from \(x_0=0\) to \(x_{\ell+1}=p\). Exactly \(t\) switches are possible with endpoint \(p\) iff \(t\equiv p\pmod2\), and then there are \(\binom{\ell+1}{t}\) such sequences. This gives the histogram. Applying Pascal's identity to \(\binom{\ell+1}{t}=\binom{\ell}{t}+\binom{\ell}{t-1}\) and pairing the two adjacent parities yields the stated partial binomial sum. The maximum admissible transition count across all \(2^\ell\) block strings is \(\ell\) when \(\ell\equiv p\pmod2\), and \(\ell+1\) otherwise. Since \(d\equiv p\pmod2\), every paired word is attainable exactly for \(\ell\le d\). When \(\ell=d+1\), the unique word of transition count \(\ell+1=d+2\) is the all-switching block sequence; every other paired word has transition count at most \(d\). This proves the first missing-word assertion.

## Verification
The standalone `verify_literal.py` enumerates all \(2^n\) position subsets for every source length \(0\le n\le18\), independently filters those whose deleted subsequence is \(H_d\), and compares every resulting multiplicity to the theorem for all 190 parameter pairs. It also checks all distinct-output counts.

The separate `verify_shuffle.py` computes interleaving counts from a two-dimensional dynamic recurrence on consumed deleted/retained prefixes, rather than using the gap decomposition. It tests all paired strings for every \(0\le n\le22\), then 500 deterministic pseudorandom longer cases through \(n=100\). It independently checks all transition histogram bins. Both scripts use only the Python standard library; run with `python3 verify_literal.py` and `python3 verify_shuffle.py` from this directory. Their exact console outputs are in `verify_literal.stdout.txt` and `verify_shuffle.stdout.txt`.

As a further consistency identity, summing all individual multiplicities gives \(\binom{\lfloor(n+d)/2\rfloor}{d}\), the independently calculable number of positional embeddings of \(H_d\) into \(H_n\). It was checked for all \(0\le d\le n\le34\); this normalization is not needed for the proof of the fiber theorem.

## Relationship to prior work
Adamson, Fleischmann and Huch (2026) introduce complement scattered-factor sets and give general algorithms, reconstruction results and perfect-shuffle conditions. Their March 2026 open-access paper does not state the position-by-position multiplicities for this alternating-prefix family. A published binomial-tail result for \(C((01)^{m+k},(01)^k)\) already proves its residual **support** and run-count law; the even-even distinct-output specialization is therefore known and is *not* claimed new here. The new contribution is the exact **per-residual embedding multiplicity histogram** together with its phase-unified proof, covering all four combinations of host/deleted-length parity. The prior support theorem alone cannot recover positional multiplicities from a count of distinct residuals.

The published generalized embedding spectrum for repeated cyclic permutation words counts every embedding of a given target into a host, without conditioning the **complementary deleted positions** to spell a second prescribed target; its all-subsequence multiplicities do not imply the constrained fibers here. Likewise the fixed-composition spectrum for unrestricted deletion outputs from alternating hosts is a distinct-output census, not a fixed-deleted-subsequence multiplicity law. Standard stars-and-bars and binomial identities are mathematical tools, not standalone novelty claims.

## Limitations
This is an exact two-symbol alternating-prefix family, not a theorem about arbitrary sources or arbitrary deleted patterns. The conditional distribution assumes uniform positional selection only if subsequently interpreted probabilistically; no nonuniform channel model is analyzed. The result makes no claim of publication or independent validation. An unindexed earlier shuffle or word-binomial specialization with the same conditional-fiber law remains a priority risk; external independent review has not yet been performed.

## References
1. D. Adamson, P. Fleischmann, A. Huch, *\(\text{(Sets of) Complement Scattered Factors}\)*, arXiv:2603.20790, first publicly posted 2026-03-21. https://arxiv.org/pdf/2603.20790
2. *Binomial-tail law for complements of alternating words*, published research record, `2026/11/2/SCOPE-binomial-tail-law-for-complements-of-alternating-words--d7ef6cdd9c92`. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-binomial-tail-law-for-complements-of-alternating-words--d7ef6cdd9c92
3. *Exact embedding-multiplicity spectrum of cyclic permutation powers*, published research record, `2026/11/2/SCOPE-exact-embedding-multiplicity-spectrum-of-cyclic-permutation-powe--bcaf0c227997`. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-embedding-multiplicity-spectrum-of-cyclic-permutation-powe--bcaf0c227997
4. *Fixed-composition deletion spectra and parity bias for alternating binary words*, published research record, `2026/11/8/SCOPE-fixed-composition-deletion-spectra-and-parity-bias-for-alternati--4b7dc91ebfc9`. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-fixed-composition-deletion-spectra-and-parity-bias-for-alternati--4b7dc91ebfc9
