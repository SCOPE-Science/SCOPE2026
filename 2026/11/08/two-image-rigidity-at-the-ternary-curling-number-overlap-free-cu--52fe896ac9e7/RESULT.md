# Two-image rigidity at the ternary curling-number overlap-free cutoff

## Finding

For a finite word \(w\), its *curling-number transform* \(C(w)\) records at each position the largest integer number of identical consecutive nonempty blocks forming a suffix of the prefix ending there. A word is *overlap-free* if it has no factor of the form \(axaxa\), where \(a\) is one letter and \(x\) is possibly empty.

Let \(\mathcal E_{84}\) be the set of words \(w\in\{0,1,2\}^{84}\) for which both \(w\) and \(C(w)\) are overlap-free. Define the following length-83 binary word:

```
P = 11211221211212211221211221121221122121121221211221121221122121122112122121121221121
```

**Exact terminal image-fiber theorem.** Write \(P1\) and \(P2\) for concatenation of \(P\) with the indicated final symbol. The set of curling-number transforms of all \(w\in\mathcal E_{84}\) consists of exactly \(P1\) and \(P2\). Their preimage multiplicities are respectively

\[
\#\{w\in\mathcal E_{84}:C(w)=P1\}=4032,\qquad
\#\{w\in\mathcal E_{84}:C(w)=P2\}=2016.
\]

Consequently the \(6048\) valid source words have a common first \(83\) transform symbols and split in a \(2:1\) ratio according to the final square-suffix indicator. All \(6048\) source words use all three alphabet symbols. Under global renaming of \(\{0,1,2\}\), there are exactly \(1008\) source-word classes, with image multiplicities \(672\) and \(336\).

## Assumptions and scope

The alphabet is exactly \(\{0,1,2\}\), with all words of length \(84\) considered (no primitivity, balance, or prescribed first letter is imposed). Positions are indexed from the first position for the transform. The published sharp finite boundary \(84\) motivates the terminal census; the new assertion is the complete image set and its fibers, not merely the previously known total or maximum length.

## Proof

**1. The overlap and curling tests are exact.** A newly appended letter creates an overlap if and only if the resulting word has a suffix with period \(p\ge1\) and length \(2p+1\). Such a suffix is precisely \(axaxa\), with \(p=|ax|\). Thus testing all \(p\) with \(2p+1\le |w|\) is exhaustive. An overlap-free word is cubefree: any cube begins with an overlap. Therefore every prefix of an overlap-free source has curling number either \(1\) or \(2\), and the value is \(2\) exactly when the prefix has some square suffix of length \(2p\), with \(1\le p\le\lfloor |w|/2\rfloor\).

**2. Recursive generation is exhaustive.** The condition that both a source and its transform be overlap-free is inherited by prefixes, because the transform of a prefix is the corresponding prefix of the transform. Start from the empty source and empty transform. Extend each valid source by each of the three letters; reject the extension if its new suffix contains an overlap, compute its new curling symbol from the square-suffix test, and reject it if the new transform suffix contains an overlap. By induction on the source length, this constructs *all and only* valid sources at each level. There is no sampling, search timeout, or unverified exclusion.

**3. Alphabet symmetry gives a second exhaustive formulation.** Global renaming of source letters leaves both overlap-freeness and the curling transform unchanged. Each renaming orbit has a unique restricted-growth representative: its first distinct letter is encoded \(0\), its next new letter \(1\), and its third new letter \(2\). Equivalently, a representative starts with \(0\) and each subsequent digit is at most one larger than the greatest preceding digit. Enumerating only these extensions is therefore exhaustive up to renaming. A representative using \(k\) symbols has exactly \(3!/(3-k)!\) distinct labeled sources.

**4. Exact finite certificate.** The complete restricted-growth enumeration through length \(85\), independently reproduced by the fully labeled enumeration, gives the following terminal counts:

| Level | Restricted-growth sources | Distinct transforms | Labeled sources |
| --- | ---: | ---: | ---: |
| \(84\) | \(1008\) | \(2\) | \(6048\) |
| \(85\) | \(0\) | \(0\) | \(0\) |

The complete \(1008\)-row restricted-growth census is `canonical84.tsv`. Its last column, checked by `verify_rgs.py` against an independently regenerated level, contains exactly \(672\) occurrences of \(P1\) and \(336\) of \(P2\), and no other strings. Every representative contains three distinct symbols; each therefore has exactly six labeled images under alphabet renaming. This yields the asserted \(4032\) and \(2016\) labeled preimages. Independently, `verify_labeled.cpp` enumerates all \(6048\) labeled valid sources directly and computes the same two transform-fiber counts without the restricted-growth reduction. Both routines check that level \(85\) is empty. The claim is a finite exhaustive theorem, with its entire search space specified by exact recurrences and independently executable code.

## Verification

From the directory containing the accompanying files, run:

```
python3 verify_rgs.py
c++ -std=c++17 -O3 verify_labeled.cpp -o verify_labeled
./verify_labeled
```

The respective successful outputs are `TERMINAL_CURL_RGS_VERIFY_OK 1008 672 336` and `TERMINAL_CURL_LABELED_VERIFY_OK 6048 4032 2016`. The first program regenerates and byte-compares every row of `canonical84.tsv`; the second enumerates all labeled words directly. The SHA-256 checksum of `canonical84.tsv` is `f9cbf37faf2e799e541f6d147866ae1046d68da2cfdfbad1d4e4db2e275af2bd`. The displayed full-transform example in the motivating paper is also the \(P2\) image, furnishing an independent consistency witness.

## Relationship to prior work

Caveney, Dong, and Shallit (2026), Theorem 7, establish the maximum admissible ternary length \(84\) and the total \(6048\) terminal source words, giving one explicit example and its transform. Their Appendix B describes verification of terminal source counts. Those results do not state the number of *distinct transform images* or the distribution of source words over those images; the total count by itself does not determine these quantities. The present terminal-fiber theorem refines the boundary by identifying its full transform image and exact nonuniform fibers. The original studies of curling numbers by van de Bult et al. (2007) and Chaffin et al. (2013) concern the defining recurrence and related sequence statistics, rather than this simultaneous overlap-free terminal image.

## Limitations

The two-image result is only about the sharp ternary finite boundary at length \(84\). It does not classify shorter-level image fibers, alphabets of size at least four, or infinite transform images. The proof of the new exact terminal counts is exhaustive finite computation whose soundness depends on the supplied small enumerators and their justified recurrence; independent mathematical validation and definitive priority assessment remain outstanding.

## References

1. G. Caveney, H. Dong, and J. Shallit, *Repetition Avoidance in Curling-Number Transforms*, arXiv:2608.15670v1, first posted 2026-08-16. https://arxiv.org/html/2608.15670v1
2. F. J. van de Bult, D. C. Gijswijt, J. P. Linderman, N. J. A. Sloane, and A. R. Wilks, *A Slow-Growing Sequence Defined by an Unusual Recurrence*, Journal of Integer Sequences 10 (2007), Article 07.1.2. https://cs.uwaterloo.ca/journals/JIS/VOL10/Sloane/sloane55.html
3. B. Chaffin, J. P. Linderman, N. J. A. Sloane, and A. R. Wilks, *On Curling Numbers of Integer Sequences*, Journal of Integer Sequences 16 (2013), Article 13.4.3. https://cs.uwaterloo.ca/journals/JIS/VOL16/Sloane/sloane3.html
