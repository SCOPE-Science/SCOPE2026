# A sharp stabilization threshold for minimal absent words of periodic prefixes

## Finding
Let \(\Sigma\) be a finite alphabet containing at least two symbols, let \(r=r_0\cdots r_{d-1}\in\Sigma^d\) be a nonempty **primitive** word, and let \(P=r^\omega\) be its one-sided infinite periodic repetition. Write \(P[ i:j )\) for the factor in zero-based positions \(i,\ldots,j-1\), and let \(\mathcal M_\Sigma(X)\) be the set of *minimal absent contiguous factors* of a word or factorial language \(X\), with missing one-letter words included.

**Theorem (one moving boundary obstruction).** For every integer
\[
 n\ge N(d):=\max\{1,2d-2\},\qquad S_n=P[0:n),
\]
there is the exact disjoint decomposition
\[
\boxed{\mathcal M_\Sigma(S_n)=\mathcal M_\Sigma(P)\;\dot\cup\;\{P[d-1:n+1)\}.}
\]
All the stable factors have length at most \(d\). The sole changing factor has length \(n-d+2\), and therefore
\[
 |\mathcal M_\Sigma(S_n)|=|\mathcal M_\Sigma(P)|+1
\]
for every permitted \(n\). In particular, advancing from \(S_n\) to \(S_{n+1}\) replaces exactly one minimal absent factor by its one-letter right extension, while every other minimal absence stays unchanged.

The threshold is sharp as a **uniform** guarantee: for the primitive binary period `01101` of length \(d=5\), the length-\(7\) prefix `0110101` lacks the periodic minimal absent factor `11011` (although the latter belongs to \(\mathcal M_\Sigma(P)\)). Hence the claimed decomposition need not hold at \(n=2d-3\).

**Power corollary.** If \(w=r^s\) with primitive root \(r\) and \(s\ge1\), then for all \(t\ge2\)
\[
\mathcal M_\Sigma(w^t)=\mathcal M_\Sigma(P)\;\dot\cup\;\{r_{d-1}r^{st-1}r_0\}.
\]
This covers arbitrary primitive or nonprimitive repeated blocks, every finite alphabet, and every exponent, not just single-run or distinct-letter periods.

## Assumptions and scope
A word \(r\) is primitive when it is not a nontrivial integer power of a shorter word. All occurrences and absences refer to **contiguous** factors, not scattered subsequences. Alphabet symbols unused by \(r\) remain in \(\Sigma\), so each unused symbol is itself a minimal absent word. For a length-\(\ell\) word \(x\), minimal absence means \(x\notin\operatorname{Fact}(X)\) while its length-\(\ell-1\) prefix and suffix occur; for \(\ell=1\), the empty word is treated as occurring. The conclusion concerns prefixes of \(r^\omega\), with the period aligned at index zero. No probability, genetic interpretation, or arbitrary eventually-periodic preperiod is assumed.

## Proof
**Lemma 1 (short rotations distinguish phase).** For \(d\ge2\), the \(d\) circular factors of length \(d-1\) of the primitive period \(r\) are pairwise distinct. Indeed, if two cyclic rotations share their first \(d-1\) symbols, they have the same multiset of symbols because both are rotations of \(r\); their final symbols consequently also agree. The two rotations coincide, contradicting primitivity. For \(d=1\), there is only one possible phase.

**Lemma 2 (no long periodic minimal absence).** If \(x\) has length at least \(d+1\) and both its length-one-shorter prefix and suffix occur in \(P\), then \(x\) occurs in \(P\). Their common overlap has length at least \(d-1\). By Lemma 1 (or the unique phase when \(d=1\)), that overlap identifies the same periodic phase in both occurrences, forcing a compatible extension. It follows that every element of \(\mathcal M_\Sigma(P)\) has length at most \(d\).

**Lemma 3 (the stable component is present).** For \(d\ge2\), the prefix \(S_n\) has all \(d\) circular factors of every length \(\ell\le d-1\), since \(n-\ell+1\ge d\). Therefore every periodic minimal absent word, whose proper factors have length at most \(d-1\), is also minimal absent from \(S_n\). This is equally immediate for \(d=1\), when periodic minimal absences are precisely the unused alphabet letters.

**The unique possible new absence.** Let \(x\in\mathcal M_\Sigma(S_n)\setminus\mathcal M_\Sigma(P)\), of length \(\ell\). It must be a periodic factor; otherwise, its proper factors belong to \(P\), making \(x\) a periodic minimal absent word. For \(\ell\le d-1\), every periodic factor appears in \(S_n\); thus \(\ell\ge d\). For \(\ell=d\), all length-\(d\) rotations are present when \(n\ge2d-1\); at the sole remaining boundary \(n=2d-2\), the only missing one is the rotation beginning at phase \(d-1\), namely \(P[d-1:n+1)\).

Now suppose \(\ell\ge d+1\). As \(x\) is a factor of \(P\), its occurrence phase \(i\in\{0,\ldots,d-1\}\) is unique, by Lemma 1. Its prefix of length \(\ell-1\) occurs in \(S_n\) but \(x\) itself does not, so
\[
 i+\ell-1\le n<i+\ell,\qquad\text{hence }i+\ell=n+1.
\]
Its suffix has the unique phase \(j=(i+1)\bmod d\) and length \(\ell-1\), so \(j+\ell-1\le n\). If \(i<d-1\), then \(j=i+1\) and this inequality contradicts \(i+\ell=n+1\). Consequently \(i=d-1\) and \(\ell=n-d+2\), forcing \(x=P[d-1:n+1)\).

Finally, this forced candidate is indeed minimal absent. Its length-\((\ell-1)\) prefix occurs in \(S_n\) starting at position \(d-1\), and its length-\((\ell-1)\) suffix occurs at position zero. Its full occurrence would need to start in phase \(d-1\), at or after position \(d-1\), and would end beyond position \(n-1\); therefore it is absent. For the special case \(n=2d-2\), use the same phase-uniqueness argument with the length-\(d\) candidate. The long word is a factor of \(P\), so it is disjoint from \(\mathcal M_\Sigma(P)\). This completes the proof.

For the power corollary, set \(n=std\), where \(w=r^s\). The boundary factor from phase \(d-1\) is exactly \(r_{d-1}r^{st-1}r_0\).

## Verification
Two separate executable standard-library programs accompany the result. `check_factors.py` builds sets of contiguous factors of each finite prefix and tests the complete antidictionary equality in **11,747** finite cases for alphabet sizes two through four. `check_contexts.py` independently reconstructs absent words by two-sided extension contexts and compares against a circular-factor construction in **4,567** exhaustive or reproducibly sampled cases. Both tests passed; they include primitive roots, incomplete last periods, absent alphabet letters, and unary periods embedded in larger alphabets. The proof above, not these finite tests, establishes the unlimited-parameter theorem.

As an effective corollary, the stable antidictionary may be obtained from a two-period text: 
\[
\mathcal M_\Sigma(P)=\{x\in\mathcal M_\Sigma(r^2):|x|\le d\}.
\]
A compact description of the antidictionary for arbitrarily large \(n\) therefore requires the stable set and one boundary factor described by its start phase and length. Explicitly writing that long factor still takes time proportional to its length.

## Relationship to prior work
Pinho et al. (2009) introduced an operative minimal-absent-word characterization through left/right contexts, and Barton et al. (2014) gave a linear-time suffix-array algorithm for general texts; neither inspected treatment gives this periodic-prefix stabilization law. Fici, Restivo, and Rizzo (2017 preprint, revised 2018) established the circular identity \(\mathcal M_\Sigma(P)=\mathcal M_\Sigma(r^2)\cap\Sigma^{\le d}\), an important stable-component predecessor, but did not state the unique finite-endpoint obstruction or the sharp cutoff for every prefix. A publicly indexed 2026 result proves a one-moving-boundary classification for the special subclass of cycles consisting of runs on pairwise distinct letters. Its conclusion applies directly to that subclass; it does not classify arbitrary primitive periods, noncomplete final periods, or the sharp universal prefix threshold proved here. The comparison is about implication and domain, not merely differences in titles.

## Limitations
This result is about factor sets, not about the speed or performance of any particular compressed index. The cutoff is uniform and sharp in general but may be smaller for individual periods. The special distinct-run periodic-power case already has an indexed exact result; historical originality of the unrestricted statement remains subject to discovery of unindexed work or a general earlier implication. The cited indexed special-case full package was not accessible for full-text inspection; its available result statement was compared directly. No independent audit has been performed.

## References
- A. J. Pinho, P. J. S. G. Ferreira, S. P. Garcia, and J. M. O. S. Rodrigues, *On finding minimal absent words*, BMC Bioinformatics 10 (2009), article 137; first verified public date 2009-05-08. https://doi.org/10.1186/1471-2105-10-137
- C. Barton, A. Héliou, L. Mouchard, and S. P. Pissis, *Linear-time computation of minimal absent words using suffix array*, BMC Bioinformatics 15 (2014), article 388. https://doi.org/10.1186/s12859-014-0388-9
- G. Fici, A. Restivo, and L. Rizzo, *Minimal Forbidden Factors of Circular Words*, preprint arXiv:1707.04450, updated 2018; especially Section 3, Lemma 2. https://arxiv.org/abs/1707.04450
- *The complete minimal-absent-factor spectrum of cyclic distinct-run powers*, public indexed result (2026), identifier `2026/11/2/SCOPE-the-complete-minimal-absent-factor-spectrum-of-cyclic-distinct-r--3a571b3bae66`. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-complete-minimal-absent-factor-spectrum-of-cyclic-distinct-r--3a571b3bae66
