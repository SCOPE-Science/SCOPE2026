# First four-bit one-deletion code under guarded \((2,\infty)\) run-length limitation

## Finding

Let \(S_n\) be the length-\(n\) binary words in which every maximal zero run has length at least two, including the first and last runs, and every one run has length exactly one. A word consisting entirely of zeros is included. Let \(M_n\) be the maximum number of words in a code \(C\subseteq S_n\) for which the sets \(D_1(w)\) of distinct outputs of exactly one symbol deletion are pairwise disjoint. Then

\[
M_{16}=14,
\]

and there exists a code \(C\subseteq S_{17}\) with \(|C|=16\). Moreover, for every integer \(n\ge1\), a code \(C\subseteq S_n\) correcting one deletion can have at least sixteen words only if \(n\ge17\). Consequently, the minimum blocklength for transmitting four information bits in this model is exactly seventeen.

## Assumptions and scope

The channel deletes exactly one symbol, either zero or one, at an unknown position. Different deletion positions producing the same output are counted once. Input words are fixed length, with no adjacent ones and with at least two zeros before the first one, between successive ones, and after the final one. The all-zero word is allowed; no cyclic end-to-start condition is imposed. The code is a set of distinct words, and decoding is required for every single-deletion output.

## Proof

**Zero padding lemma.** If \(C\subseteq S_n\) is one-deletion correcting, then \(C0=\{w0:w\in C\}\subseteq S_{n+1}\) is one-deletion correcting. To prove this, assume two different appended codewords \(x0,y0\) have the same length-\(n\) deletion output. If both deletions remove the appended zero, then \(x=y\), impossible. If neither deletes the appended zero, removing the final zero from the common output would give a common single-deletion output of \(x\) and \(y\). If exactly one deletion removes the appended zero, say the deletion of \(x0\) produces \(x\) and the deletion of an original position of \(y0\) produces \(u0\), then \(x=u0\). Therefore the word \(u\) lies in both \(D_1(x)\) (delete its final zero) and \(D_1(y)\), a contradiction. Repeated appending proves \(M_n\le M_{16}\) whenever \(n\le16\).

**Exact finite upper bound.** There are precisely 129 allowed words in \(S_{16}\). Construct their compatibility graph by joining two distinct words when their single-deletion output sets are disjoint. Every correcting code is a clique, and conversely. The attached `verify.py` constructs the graph directly from all 129 words, then exhaustively searches its cliques using exact arbitrary-precision integer bitmasks and a proper greedy coloring to bound the attainable clique size in each branch. The coloring bound is valid because any clique contains at most one vertex per color. The algorithm starts with an explicit verified fourteen-word clique, explores all branches that might exceed it, and terminates with maximum fourteen; it visits 33,491 search nodes. The source code includes the full enumeration and pruning rule rather than a precomputed solver transcript. The fourteen listed words in `witnesses.json` have pairwise disjoint deletion shadows, so the exact maximum is \(M_{16}=14\).

**Achievability at length seventeen.** The sixteen length-seventeen words in `witnesses.json` satisfy every run constraint. Direct generation of their distinct single-deletion outputs confirms that the sixteen shadow sets are disjoint. Thus \(M_{17}\ge16\), and the zero-padding lemma and the preceding exact upper bound exclude any shorter admissible blocklength.

## Verification

From the directory containing `verify.py` and `witnesses.json`, run `python3 verify.py` with standard Python 3 (no third-party packages). It regenerates the candidate sets, both witnesses, all deletion shadows and the exhaustive upper-bound search. The observed successful output was `EXACT_PROOF_OK n16_max=14 n17_code=16`, with 129 candidate words and 33,491 search nodes. An independent integer-programming formulation using one constraint per possible deletion output also returned optimum fourteen at length sixteen. That second numerical cross-check is not used as the finite proof.

## Relationship to prior work

Kulkarni and Kiyavash (first public preprint November 13, 2012) study nonasymptotic bounds for constrained single-deletion-correcting codes, including guarded run-length-limited sources. Their Theorems V.1–V.2 bound sizes but do not provide the exact sixteen-symbol optimum or the first blocklength supporting sixteen messages. Their direct fractional matching relaxation for this instance is above seventeen, and therefore does not establish the sharp upper bound fourteen. Earlier work of Bours and of Palunčić and collaborators develops constrained insertion/deletion-correcting constructions under related channel models, not an inspected full-text finite optimum matching this claim. The novelty conclusion is limited to the inspected materials and comparisons; an inaccessible complete predecessor could alter historical priority.

## Limitations

The exact capacity proved here is for blocklength sixteen under these specific guarded \((2,\infty)\) conditions. The result for length seventeen is a lower bound, not a full capacity value. There is no claim of an all-length capacity formula or physical-device performance. The finite search is exhaustive for the stated labeled source alphabet but is not an independent scientific audit.

## References

- Ankur A. Kulkarni and Negar Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128v1 (public November 13, 2012), https://arxiv.org/abs/1211.3128; full text https://ar5iv.labs.arxiv.org/html/1211.3128.
- P. A. H. Bours, *Construction of fixed-length insertion/deletion correcting runlength-limited codes*, IEEE Transactions on Information Theory 40 (1994), 1841–1856, https://doi.org/10.1109/18.340459.
- F. Palunčić, K. A. S. Abdel-Ghaffar, H. C. Ferreira and W. A. Clarke, *A multiple insertion/deletion correcting code for run-length limited sequences*, IEEE Transactions on Information Theory 58 (2012), 1809–1824, https://doi.org/10.1109/TIT.2011.2172725.
