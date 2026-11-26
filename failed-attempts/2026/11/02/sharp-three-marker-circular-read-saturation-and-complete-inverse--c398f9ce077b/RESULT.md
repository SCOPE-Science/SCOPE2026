# Sharp three-marker circular read saturation and complete inverse fibers

## Finding

For each integer \(k\ge 2\), let \(C_{n,k}\) be the number of different multisets of all cyclic length-\(k\) binary factors of a length-\(n\) word containing exactly three ones. Factors retain their internal symbol order and their multiplicities; the starting positions of the factors are not reported. For every \(n\ge 3k-1\),

\[
C_{n,k}=k+(k-1)^2-\left\lfloor\frac{(k-1)^2}{4}\right\rfloor
-\mathbf 1_{\{n=3k-1\}}.
\]

Thus the exact **permanent** stabilization threshold is \(n=3k\): one profile is absent at \(n=3k-1\), whereas the same number occurs at every \(n\ge3k\). The stabilized value is \(3m^2-m+1\) for \(k=2m\), and \(3m^2+2m+1\) for \(k=2m+1\). Equivalently it is the largest zero-error code size for this complete circular read-multiset channel, when the codewords are indexed words of weight three.

The theorem also specifies **every inverse fiber** in this range. Write the positive clockwise spacings between successive ones as \((d_0,d_1,d_2)\), so their sum is \(n\). A spacing is *short* when it is less than \(k\). At least one spacing is not short. The following table classifies spectra; the fiber sizes count indexed binary words, not necklaces.

| Type | Recoverable label of a read multiset | Number of profiles | Indexed-word fiber size |
|---|---|---:|---:|
| A | No short spacing | \(\mathbf1_{\{n\ge3k\}}\) | \(\frac n3\binom{n-3k+2}{2}\) |
| B | Exactly one short spacing \(a\), \(1\le a<k\) | \(k-1\) | \(n(n-a-2k+1)\) |
| C | Two short spacings with \(a+b\ge k\), unordered label \(\{a,b\}\) | \(\binom{k}{2}-\lfloor(k-1)^2/4\rfloor\) | \(n\) if \(a=b\), otherwise \(2n\) |
| D | Two short spacings in clockwise order \((a,b)\), with \(a+b<k\) | \(\binom{k-1}{2}\) | \(n\) |

The type-A fiber formula is used only when \(n\ge3k\). Every row and label listed is attainable at the specified lengths. In particular the total of the fiber sizes is \(\binom n3\), the number of source words.

## Assumptions and scope

The alphabet is \(\{0,1\}\), and exactly three of the \(n\) labeled positions contain a one. Read length satisfies \(2\le k\le n\) and the theorem concerns \(n\ge3k-1\). For each word \(w\), the observation \(\mathsf H_{n,k}(w)\) is the vector of counts of each ordered \(v\in\{0,1\}^k\) among the \(n\) cyclic factors \((w_i,\ldots,w_{i+k-1})\), with indices interpreted modulo \(n\). Cyclic rotations give the same observation but are still distinct input words. A reversal of a factor is not identified with the factor itself.

The labels in the table are read-multiset invariants, not merely convenient ways to describe inputs. The classification asserts that two source words have equal observations if and only if they carry the same listed label.

## Proof

**1. Recovering correlations from exact factor counts.** Number the \(k\) positions within a factor as \(0,1,\ldots,k-1\). For \(T\subseteq\{0,\ldots,k-1\}\), let

\[
F_w(T)=\#\{i\pmod n:w_{i+t}=1\text{ for every }t\in T\}.
\]

If \(H_w(U)\) counts factors whose set of one-positions is exactly \(U\), then

\[
F_w(T)=\sum_{U\supseteq T}H_w(U),\qquad
H_w(U)=\sum_{T\supseteq U}(-1)^{|T|-|U|}F_w(T).
\]

Thus the entire ordered factor multiset and the entire family of correlations \(F_w(T)\) determine one another. For a source of weight three, the only nontrivial correlations concern two- and three-position subsets: singletons always have value three, while all subsets of size greater than three have value zero.

**2. The long-spacing dichotomy.** As \(n\ge3k-1>3(k-1)\), at least one of the three positive clockwise spacings \(d_0,d_1,d_2\) is at least \(k\). For any offset \(1\le t<k\), the correlation \(F_w(\{0,t\})\) counts the ordered pairs of ones at clockwise distance \(t\). For \(0<a,b\) with \(a+b<k\), the correlation \(F_w(\{0,a,a+b\})\) counts the ordered triples of ones with first two successive spacings \(a,b\). In the present regime this latter count is either zero or one: an occurrence must traverse two short consecutive spacings; the remaining spacing is long.

If any three-position correlation is nonzero, its two consecutive offsets recover the **ordered** short spacings \((a,b)\), and the unique third spacing is \(n-a-b\). This is type D. Every other three-position correlation vanishes and, because no two successive short spacings sum to less than \(k\), the nonzero pair correlations at distances below \(k\) give exactly the **multiset** of short spacings. Its size is zero, one, or two, yielding respectively types A, B and C. This proves both that the displayed labels are observable and that identical labels give identical full factor multisets by the inversion formula.

**3. Counting possible labels.** Type A exists exactly when \(n\ge3k\). Every \(a\in\{1,\ldots,k-1\}\) occurs in type B. For type C, the unordered pairs \(1\le a\le b\le k-1\) with \(a+b\ge k\) number

\[
\binom{k}{2}-\left\lfloor\frac{(k-1)^2}{4}\right\rfloor.
\]

Indeed the number of unordered positive pairs with sum at most \(k-1\) is \(\lfloor(k-1)^2/4\rfloor\). For type D, the positive **ordered** pairs with sum at most \(k-1\) number \(\binom{k-1}{2}\). All labels are realizable: in B choose two remaining spacings at least \(k\) that sum to \(n-a\); in C/D take the remaining spacing \(n-a-b\), which is at least \(k\). The last assertion follows since \(a+b\le2k-2\) and \(n\ge3k-1\). Adding the four counts simplifies to the formula above. Removing the single type-A label at the predecessor establishes the sharp stabilization boundary.

**4. Counting every inverse fiber.** For B, the unique short spacing \(a\) distinguishes a first marker, and the two long ordered spacings have \(n-a-2k+1\) choices; each configuration has \(n\) possible placements. In C, the unique long spacing fixes a first marker; the unordered pair \(\{a,b\}\) has one clockwise order if \(a=b\) and two otherwise, each of which has \(n\) indexed placements. In D the ordered pair is prescribed, giving exactly \(n\) placements. In A, fix one of three marker positions as the starting point, distribute the residual \(n-3k\) among three long spacings in \(\binom{n-3k+2}{2}\) ways, and divide the resulting \(n\)-fold placements by the three choices of distinguished marker. This double-counting remains valid for periodic words, which completes the fiber formula and the proof.

## Verification

The included stdlib-only program `verify.py` uses literal cyclic binary windows, not gap-derived spectra, to group all indexed weight-three words for \(2\le k\le10\) at \(n=3k-1,3k,3k+1,3k+3\). It independently compares each observed fiber and its source multiplicity to the theoretical label. It checked **53,325** source words over **36** complete cases. Separately, **492** parameter cases for \(2\le k\le124\) verify the symbolic class counts and the identity that all predicted fibers sum to \(\binom n3\). The program prints `VERIFY_OK` on success. These finite checks test the proof's premises; they are not a substitute for the all-parameter argument above.

Reproduce with `python3 verify.py` using Python 3 and its standard library.

## Relationship to prior work

Gabrys and Milenkovic (arXiv:1804.04548, first posted 2018-04-12) study coded reconstruction from multiplicity-preserving substring spectra and repeat replacement, establishing the read-multiset information model. Marcovich and Yaakobi (arXiv:1912.11108, first posted 2019-12-23) analyze incomplete/noisy substring spectra and code constructions. Kiah, Puleo and Milenkovic (arXiv:1502.00517) study DNA sequence-profile codes and profile-count asymptotics. Those results do not explicitly state this weight-three circular, two-parameter exact count or its inverse-fiber classification. The previously known exact enumerations of circular length-three observations give a slice of the present problem at \(k=3\), not an all-read-length law. The new assertion is the precise finite-length classification, not the novelty of the resulting integer sequence alone.

## Limitations

This is a noiseless, complete, oriented factor-multiset channel, with exactly three markers and \(n\ge3k-1\). It is not a statement about reads sampled with replacement, missing reads, reverse-complement identification, or words of higher weight. It does not determine the capacity for \(n<3k-1\). A conceptually equivalent specialization of general reconstruction or flow-counting theorems may exist outside the inspected sources. No independent external mathematical audit has been performed.

## References

1. R. Gabrys and O. Milenkovic, *Unique Reconstruction of Coded Strings from Multiset Substring Spectra*, arXiv:1804.04548 (2018), https://arxiv.org/abs/1804.04548.
2. S. Marcovich and E. Yaakobi, *Reconstruction of Strings from their Substrings Spectrum*, arXiv:1912.11108 (2019), https://arxiv.org/abs/1912.11108.
3. H. Kiah, G. Puleo and O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (2015), https://arxiv.org/abs/1502.00517.
