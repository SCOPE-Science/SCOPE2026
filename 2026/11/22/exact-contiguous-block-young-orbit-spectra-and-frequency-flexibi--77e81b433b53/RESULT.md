# Exact contiguous-block Young-orbit spectra and frequency flexibility of mechanical words

## Finding
For a real slope \(0<\alpha<1\), an arbitrary real intercept \(\rho\), and the lower mechanical binary word
\[
w_t=\lfloor(t+1)\alpha+\rho\rfloor-\lfloor t\alpha+\rho\rfloor\qquad(t\ge0),
\]
fix any integer \(r\ge1\) and positive block lengths \(\ell_1,\ldots,\ell_r\). Put \(n=\sum_i\ell_i\), \(S_0=0\), and \(S_i=\sum_{j=1}^i\ell_j\). Let \(G=\prod_{i=1}^r S_{\ell_i}\le S_n\) act by independently permuting the \(r\) successive position blocks. Let \(P_G(n)\) be the number of \(G\)-orbits intersecting the length-\(n\) factor language of \(w\).

**All-slope exact law.** Put
\[
T=\{0\}\cup\bigl\{1-\{S_i\alpha\}:1\le i\le r,\ \{S_i\alpha\}\ne0\bigr\}.
\]
If \(0=t_0<t_1<\cdots<t_{h-1}<t_h=1\) are the distinct elements of \(T\) followed by \(1\), then \(P_G(n)=h\). Each class occurs with natural starting-position frequency exactly \(t_j-t_{j-1}\), for \(1\le j\le h\). In particular, if \(\alpha\) is irrational, then \(P_G(n)=r+1\) **for every composition**, while for \(\alpha=p/q\) in lowest terms,
\[
P_G(n)=\bigl|\{S_0,S_1,\ldots,S_r\}\bmod q\bigr|.
\]

**Sharp frequency flexibility.** For a fixed irrational \(\alpha\) and fixed \(r\ge1\), as the positive block lengths vary, the vectors of \(r+1\) class frequencies, listed by increasing rotation-phase interval, are dense in the open probability simplex on \(r+1\) coordinates. Consequently their Shannon entropies (natural logarithms) have exact unattained infimum \(0\) and unattained supremum \(\log(r+1)\). The entropy claim concerns the distribution of these quotient classes, **not** the measure-theoretic entropy of the underlying Sturmian shift.

## Assumptions and scope
The full word is the one-sided lower mechanical word at all \(t\ge0\). The group action is taken on the ambient binary length-\(n\) words; a class is counted if its orbit intersects the factor set, whether or not every member is itself a factor. Frequencies refer to the natural density of factor starting positions \(t\), not frequencies of finite-word embeddings. A rational slope has reduced denominator \(q\ge2\). Empty blocks are excluded. The prefix boundaries \(S_i\) are strictly increasing, and no assertion is made for arbitrary nonconsecutive coordinate partitions.

## Proof
**Step 1 (orbit invariant).** Two binary length-\(n\) words lie in the same \(G\)-orbit precisely when every block has the same number of ones. Write this block-one-count vector as \((B_1,\ldots,B_r)\). Its cumulative sums \(N_i=\sum_{j\le i}B_j\) determine and are determined by the block vector.

**Step 2 (rotation thresholds).** Fix a factor starting at \(t\) and set \(x_t=\{t\alpha+\rho\}\). Telescoping the mechanical word gives
\[
N_i(t)=\lfloor(t+S_i)\alpha+\rho\rfloor-\lfloor t\alpha+\rho\rfloor
=\lfloor S_i\alpha\rfloor+\epsilon_i(x_t),
\]
where \(\epsilon_i(x)=\mathbf1_{\{x\ge1-\{S_i\alpha\}\}}\) when \(\{S_i\alpha\}>0\), and \(\epsilon_i(x)=0\) when \(\{S_i\alpha\}=0\). Thus every class is determined by its threshold-indicator vector. Each distinct nonzero threshold induces a genuine change, possibly simultaneously in several coordinates. Because each indicator is nondecreasing in \(x\), two different complementary intervals cannot have the same vector. Hence the classes correspond bijectively to the intervals \([t_{j-1},t_j)\), and their number is \(|T|\).

**Step 3 (existence and frequencies).** If \(\alpha\) is irrational, the fractional phases \(x_t\) are uniformly distributed modulo one; every nonempty interval occurs with frequency equal to its length. All \(r\) nonzero thresholds are distinct: otherwise \((S_i-S_j)\alpha\) or \(S_i\alpha\) would be an integer. Hence there are \(r+1\) classes. If \(\alpha=p/q\) in lowest terms, the \(q\) consecutive phases form a translated, equally spaced \(q\)-grid. Every threshold is a multiple of \(1/q\), so each positive-length interval contains exactly \(q\) times its length many grid points, independent of the intercept (including boundary intercepts under the half-open convention). This gives every class frequency and shows \(|T|=|\{S_0,\ldots,S_r\}\bmod q|\) because multiplication by \(p\) is invertible modulo \(q\).

**Step 4 (simplex density and sharpness).** Fix any positive probability vector \((a_0,\ldots,a_r)\) summing to one and let \(v_i=\sum_{j=0}^{i-1}a_j\) for \(1\le i\le r\); these satisfy \(0<v_1<\cdots<v_r<1\). The tail of an irrational rotation is dense in the circle. Hence one can inductively select arbitrarily large strictly increasing integers \(S_1<\cdots<S_r\) so that \(1-\{S_i\alpha\}\) is as close as desired to \(v_i\). Setting \(\ell_i=S_i-S_{i-1}>0\) makes the ordered class frequencies converge to \((a_0,\ldots,a_r)\). Continuity of Shannon entropy gives values arbitrarily close to both simplex extremes. Every class frequency is positive, so entropy is strictly positive. Entropy \(\log(r+1)\) requires all gaps equal to \(1/(r+1)\), which would make one of the nonzero thresholds rational, impossible for irrational \(\alpha\). This completes the proof.

## Verification
The standalone `check_random_profiles.py` compares actual factor block-count dictionaries with the predicted class counts for 90,312 rational cases and 3,240 irrational cases, with several intercepts and sampled compositions. The independently implemented `check_exact_frequencies.py` uses exact rational arithmetic to verify 8,370 rational cases, checking class injectivity, absence of missing classes, and the complete predicted frequency distribution. Their execution outputs are supplied separately. These finite tests are corroboration, not a proof of the universal statement; the proof is Steps 1–4.

## Relationship to prior work
Launer, Puzynina and Voloshinova (2026) introduced the universal-group-complexity question and proved that Sturmian words attain each complexity between their Abelian and ordinary factor complexities, using subgroups that permute a suffix. The present result instead gives the quotient and the entire orbit-frequency measure **for every partition into contiguous blocks**, includes rational mechanical words, and proves a simplex-density law for their frequencies. The earlier existence theorem does not itself determine the values for these Young subgroups or their class frequencies. Classical rotation codings and the heavy/light interval criterion for Sturmian factors supply important starting ingredients; these are credited rather than claimed as new. No claim is made that the ordinary rotation-interval representation is original.

## Limitations
The result does not classify groups with noncontiguous position orbits, or generic words not coded by a single mechanical rotation. The extremal entropies are not attained at any finite positive block composition for irrational slope. The mathematical argument is a self-contained derivation from established rotation and factor-group definitions, and a related unindexed formulation or equivalent prior corollary remains a priority risk. Independent expert validation has not been performed.

## References
1. M. Launer, S. Puzynina, and E. Voloshinova, *On possible values of the group complexity function of infinite words*, arXiv:2607.07620v1 (first public version 2026-07-08), https://arxiv.org/abs/2607.07620.
2. *Abelian-square-rich words*, Theoretical Computer Science (2017), DOI:10.1016/j.tcs.2017.02.012, https://doi.org/10.1016/j.tcs.2017.02.012, especially Section 5 on Sturmian rotation intervals and the heavy/light criterion.
3. K. O'Bryant, *Sturmian Words and the Permutation that Orders Fractional Parts*, Journal of Algebraic Combinatorics 19 (2004), 91–115, especially the ordering of rotation fractional parts.
