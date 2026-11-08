# Exact mixed-length palindromic-duplication spheres over distinct-letter words

## Finding

Fix integers \(q\ge n\ge1\), \(1\le k\le n\), and \(2\le\ell\le n+k\) with \(k\ne\ell\). On words over a \(q\)-symbol alphabet, let \(D_{r,i}\) denote palindromic duplication of the consecutive length-\(r\) block beginning at zero-based position \(i\). Let
\[
\mathcal B_{k,\ell}(x)=\{D_{\ell,j}(D_{k,i}(x)):0\le i\le n-k,\ 0\le j\le n+k-\ell\}.
\]
Then
\[
\max_{x\in\Sigma_q^n}|\mathcal B_{k,\ell}(x)|=(n-k+1)(n+k-\ell+1).
\]
Moreover, **every source word with \(n\) pairwise distinct symbols has a distinct descendant for each ordered pair of allowed duplication sites**. In particular, a descendant together with that source word and the two prescribed lengths uniquely determines both sites.

The excluded regimes matter: when the second length equals one or both lengths are equal, different histories can yield identical descendants even when all original symbols are distinct.

## Assumptions and scope

For \(x=UVW\) with \(|V|=r\), define the palindromic duplication \(D_r(x)=UVV^RW\), with the reversed copy inserted immediately after the selected block. Both operations act on the currently existing word, so the second block may include copied symbols from the first operation. The first length is \(k\); the **second**, ordered length is \(\ell\). We assume the first source has all distinct letters only to attain the maximum; the upper bound holds for any source word. All parameter inequalities in the finding are required. In particular, this is not an unordered choice of two duplication lengths.

## Proof

**1. Universal history bound.** The first operation has exactly \(n-k+1\) sites. The intermediate word has length \(n+k\), with exactly \(n+k-\ell+1\) sites for the second operation. Hence the number of distinct descendants is at most the stated product for every source word.

**2. Recoverable first occurrences.** Fix an all-distinct source \(x=x_0x_1\cdots x_{n-1}\). In every descendant, the *first* occurrence of each \(x_a\) is its original occurrence: each newly inserted copy is placed after a source block that already contains an earlier occurrence of that symbol. These \(n\) first occurrences remain ordered. The intervening substrings after each original \(x_a\) and before the next original symbol (or the word end) form uniquely determined **gaps**, indexed by \(a\in\{0,\ldots,n-1\}\). Every inserted copy is wholly contained in one such gap.

For the first duplication starting at \(i\), put \(g=i+k-1\). Its inserted block is
\[
X=x_gx_{g-1}\cdots x_{g-k+1},
\]
of length \(k\), entirely in gap \(g\). A second duplication inserts \(\ell\) consecutive symbols into exactly one gap, because insertion occurs immediately after the last symbol of its selected block. Thus the final descendant has either two nonempty gaps, of respective sizes \(k\) and \(\ell\), or a single nonempty gap of size \(k+\ell\).

**3. Two nonempty gaps.** Their unequal lengths identify which gap contains the first inserted block of length \(k\). Its index \(g\) uniquely gives the first site \(i=g-k+1\). We can therefore reconstruct the entire intermediate word. The second inserted block occupies a different gap, so it was inserted immediately after the corresponding **original** occurrence \(x_b\), since there were no previous copies in that gap. Its endpoint in the reconstructed intermediate word is now fixed, uniquely determining its start site \(j\) from its prescribed length \(\ell\). Hence no two histories give the same two-gap descendant.

**4. One nonempty gap.** Its index \(g\) gives \(i=g-k+1\), so \(X\) and the intermediate word are again uniquely known. The second insertion occurs immediately after \(h\) letters of \(X\), for a unique \(h\in\{0,1,\ldots,k\}\), with \(h=0\) meaning immediately after the original \(x_g\). Not every \(h\) need be feasible; compare only those for which a length-\(\ell\) source block exists.

Call the resulting gap word \(S_h\). For \(1\le h<h'\le k\), compare the zero-based character of \(S_h\) and \(S_{h'}\) at gap index \(h\). The first is the first symbol of the second copied block, namely \(X_{h-1}\), while the second remains the uncopied original \(X_h\). These letters are different because all \(x_a\) are distinct.

It remains to compare \(h=0\) with \(h\ge1\). If \(S_0\) is feasible, then \(\ell\le g+1\), and its first \(\ell\) gap symbols are the reversed original segment \(x_gx_{g-1}\cdots x_{g-\ell+1}\), followed by \(X\). At zero-based gap index \(h\), \(S_h\) has symbol \(X_{h-1}=x_{g-h+1}\), whereas \(S_0\) has
\[
(S_0)_h=\begin{cases}x_{g-h},&h<\ell,\\ x_{g-h+\ell},&h\ge\ell.\end{cases}
\]
Both alternatives differ from \(x_{g-h+1}\); the second comparison uses \(\ell\ge2\). Thus all feasible \(S_h\) are pairwise different, and the second site is recoverable from the final gap.

**5. Conclusion and sharpness.** The one-gap and two-gap cases cannot coincide. In each case the final word determines the two ordered sites. Thus every one of the \((n-k+1)(n+k-\ell+1)\) histories is distinct for an all-distinct source, which exists whenever \(q\ge n\). The history bound from Step 1 is therefore attained.

For a boundary illustration, with source \((0,1,2)\) and successive lengths \((2,1)\), first site \(0\) followed by second site \(1\) or \(2\) gives the same descendant \((0,1,1,1,0,2)\). With source \((0,1,2,3)\) and lengths \((2,2)\), histories \((0,4)\) and \((2,0)\) both yield \((0,1,1,0,2,3,3,2)\). Thus neither excluded hypothesis can simply be removed from the injective-history statement.

## Verification

Run `python checker.py` (Python 3, standard library only). It constructs all permitted palindromic duplication histories directly from the channel definition and verifies injectivity for **all 671 admissible parameter triples with \(n\le11\)** and pairwise distinct canonical sources. It independently checks the trivial upper bound for **4,338 instances of binary source words with \(n\le6\)** and reproduces collisions at both excluded boundaries. The infinite theorem rests on Steps 1–5, not on finite enumeration; the checker is a reproducibility and small-case regression test.

## Relationship to prior work

Zabokritskiy (2026) studies repeated palindromic/reverse-complement duplications **of one fixed length** \(k\) and investigates exact-two descendant maxima, where collision phenomena are central. The present theorem instead treats **two prescribed, unequal lengths in a prescribed order**. Its collision-free behavior on pairwise distinct sources is not implied by a fixed-equal-length sphere computation. The full text of Zabokritskiy's paper could not be retrieved during this comparison; the paper's dated abstract unambiguously describes its fixed-length setting, so a possible unindexed extension remains a priority risk.

Sun and Ge (2026) define the same duplication operation and develop correction constructions for arbitrary-length *single* duplications and for multiple **disjoint** long duplications. Those bounds do not enumerate the exact descendants of two unequal-length sequential operations that may reuse copied letters. An accessible full-text PDF was inspected for its definitions, results roadmap and relevant sections. Prior indexed research on two fixed-length duplications and their correcting codes likewise does not imply the mixed-length history-injectivity formula. This is a mathematical nonimplication based on different allowed channel histories, not a claim that a failed search proves absolute novelty.

## Limitations

The exact sphere value is proved for \(q\ge n\). Over smaller alphabets, repeated source symbols can create additional collisions, so the same product need not be achievable. The theorem treats exactly two prescribed operations in the order \((k,\ell)\), with \(\ell\ge2\) and \(\ell\ne k\), not arbitrary length sequences or three or more errors. It does not produce optimal error-correcting codes. Historical priority beyond the inspected accessible sources remains open, and independent validation has not been performed.

## References

1. A. L. Zabokritskiy, *Coding for Multiple Reverse-Complement and Palindromic Duplications*, arXiv:2609.00779, first posted 2026-09-01. https://arxiv.org/abs/2609.00779
2. Y. Sun and G. Ge, *On the Palindromic/Reverse-Complement Duplication Correcting Codes*, arXiv:2602.01151, first posted 2026-02-01. https://arxiv.org/abs/2602.01151
