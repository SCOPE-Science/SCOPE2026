# Exact dyadic gap law for the Baum–Sweet support

## Finding

Let \(b(0)=1\), and for every integer \(n\geq 1\), let \(b(n)=1\) precisely when every maximal zero-run in the ordinary binary expansion of \(n\) has even length. Put \(S=\{n\geq0:b(n)=1\}\). Define \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\).

**Exact dyadic gap multiplicities.** For every integer \(L\geq1\), list in increasing order the elements of \(S\) in \([2^{L-1},2^L)\). This list has exactly \(F_L\) elements. For every integer \(t\) with \(0\leq t\leq L-3\), put
\[
\Delta_t=\begin{cases}2^t+2,&t\text{ even},\\ 2^t+1,&t\text{ odd}.\end{cases}
\]
The complete multiset of successive differences *within that list* is obtained by taking \(F_{L-t-2}\) copies of \(\Delta_t\) for every \(t\) in this range. The contributions for \(t=0\) and \(t=1\) both have numerical value \(3\) and are added as multiplicities. The jump from the largest element of the length-\(L\) list to the smallest element of the next length list equals \(1\) when \(L\) is even and \(2\) when \(L\) is odd; additionally the initial jump from \(0\) to \(1\) is \(1\).

Consequently the exact set of all positive gaps between successive elements of \(S\) is
\[
\boxed{\{1,2\}\;\cup\;\{2^{2j+1}+1:j\geq0\}\;\cup\;\{2^{2j+2}+2:j\geq0\}.}
\]

**Dyadic limiting gap frequencies.** Let \(\varphi=(1+\sqrt5)/2\). Among consecutive pairs of \(S\) with both entries below \(2^L\), let \(P_L(g)\) be the fraction having gap \(g\). Then \(P_L(g)\) converges for every integer \(g\geq1\). The limiting frequencies are zero for \(g=1,2\), equal to \(\varphi^{-1}\) for \(g=3\), and, for each \(t\geq2\), equal to \(\varphi^{-(t+2)}\) at \(g=\Delta_t\). All other positive gaps have limiting frequency zero. These probabilities sum to one.

## Assumptions and scope

All integers and binary words use their usual *nonnegative* conventions, with no leading zeroes in a positive integer. In particular, \(0\in S\) is a separate stipulated initial element. A gap is a difference of **adjacent elements in numerical order**, not the difference of arbitrary two elements and not a gap between equal binary-symbol occurrences in a periodic extension. The frequency limit is along dyadic cutoffs \(2^L\); no arbitrary-cutoff convergence is asserted. The interval \([2^{L-1},2^L)\) is half-open. All formulas hold for every indicated positive integer \(L\), with an empty multiset when \(L\leq2\).

## Proof

**1. Unique tile representation.** A positive binary expansion is admissible exactly when it is a word of the form \(1w\), where \(w\) is a concatenation of tiles \(1\) and \(00\). Indeed, every zero-run must have even length, and such a run decomposes uniquely into pairs of zeroes; the tile alphabet \(\{1,00\}\) is prefix-free, so the decomposition is unique. A length-\(L\) admissible number is therefore a tiling of \(L-1\) positions by tiles of lengths one and two. Its count is \(F_L\), including \(F_1=F_2=1\).

**2. Successors within a fixed length.** Binary lexicographic order agrees with numeric order at fixed length. The largest admissible word of length \(L\) is \(1^L\). For any other admissible word \(x\), take the last \(00\) tile in its unique decomposition. The word has a unique factorization \(x=P\,00\,1^t\), where \(P\) is an admissible, nonempty binary prefix ending on a tile boundary and \(t\geq0\). The smallest admissible fixed-length word lexicographically larger than \(x\) must agree with \(P\), replace that last \(00\) by \(1\), and use the lexicographically smallest admissible tail of length \(t+1\). No later lexicographic change is possible, since after the final \(00\) there are only \(1\) tiles.

If \(t\) is odd, \(t+1\) is even and the smallest tail is \(0^{t+1}\); if \(t\) is even, the smallest tail is \(0^t1\). Thus the successor is respectively \(P1 0^{t+1}\) or \(P1 0^t1\). Evaluating only the changed suffix of \(t+2\) bits, the old suffix \(00 1^t\) has value \(2^t-1\), whereas the new suffix has value \(2^{t+1}\) in the odd case and \(2^{t+1}+1\) in the even case. Their difference is \(\Delta_t\) exactly as claimed.

**3. Counting all within-length gaps.** For a prescribed \(t\), the prefix \(P\) must have length \(h=L-t-2\geq1\). Its number of choices is exactly \(F_h\) by Step 1. Distinct such words \(x\) yield distinct successor gaps, so the multiset has exactly the asserted \(F_{L-t-2}\) copies. The identity \(\sum_{h=1}^{L-2}F_h=F_L-1\) shows that these account for all \(F_L-1\) within-length adjacent pairs, including the empty cases \(L=1,2\).

**4. Boundaries and exact spectrum.** The maximum admissible length-\(L\) number is \(2^L-1\). The minimum length-\(L+1\) admissible number is \(2^L\) if \(L\) is even (binary \(1 0^L\)), and \(2^L+1\) if \(L\) is odd (binary \(1 0^{L-1}1\)). The boundary gaps are therefore \(1\) and \(2\) respectively, occurring infinitely often. Every \(t\geq0\) occurs in Step 3 by taking \(L=t+3\) and \(P=1\). Since \(\Delta_0=\Delta_1=3\), the distinct interior values are precisely \(2^{2j+1}+1\) and \(2^{2j+2}+2\) for \(j\geq0\). This proves both inclusions in the spectrum formula.

**5. Frequencies.** Through all positive binary lengths at most \(L\), the number of admissible positive elements is \(\sum_{\ell=1}^L F_\ell=F_{L+2}-1\). Including zero, the number of available adjacent gaps below \(2^L\) is therefore \(F_{L+2}-1\). For any fixed \(t\geq0\), Step 3 gives exactly
\[
\sum_{\ell=t+3}^{L}F_{\ell-t-2}=F_{L-t}-1
\]
internal gaps from that tile-tail type once \(L\geq t+3\). By the Fibonacci ratio limit \(F_{k+1}/F_k\to\varphi\), its normalized contribution tends to \(\varphi^{-(t+2)}\). The numerical gap \(3\) collects two types \(t=0,1\); the identity \(\varphi^{-2}+\varphi^{-3}=\varphi^{-1}\) gives its mass. Boundaries \(1,2\) occur only \(O(L)\) times against \(F_{L+2}-1\) total pairs, so each has limiting mass zero. Finally \(\sum_{t\geq0}\varphi^{-(t+2)}=1\), proving that the stated distribution has total mass one.

## Verification

The attached standalone `verify.py` recomputes admissibility directly from integer binary zero-runs and independently generates admissible words by their \(1\)/\(00\) tilings. It checks the complete predicted gap multiset at every length \(1\leq L\leq20\), direct membership completeness through \(L=16\), and the exact set of gaps produced by all indices below \(2^{18}\). Run `python3 verify.py` in the directory containing the script. The successful stdout begins `VERIFY_OK` and reports \(6765\) admissible indices below \(2^{18}\). These finite checks corroborate the theorem; the infinite quantifiers are justified by the proof, not by the finite enumerations.

## Relationship to prior work

Baum and Sweet introduced the sequence in the context of algebraic power series in characteristic two (1976). OEIS A086747 records its binary zero-run definition and recurrences. OEIS A060142 (first entered March 5, 2001) independently lists the ordered set \(S\) as the smallest set containing zero and closed under \(x\mapsto2x+1\) and \(x\mapsto4x\); it also records its encoding by compositions into odd parts. Those are equivalent membership descriptions, not direct enumerations of the full adjacent-gap multiset, its exact infinite spectrum, or its limiting dyadic frequencies. The related 2000 article *A Self-Generating Set and the Golden Mean* studies a different closure \(x\mapsto2x\), \(x\mapsto4x-1\). The present theorem uses a rightmost-tile successor argument to obtain the additional return-gap statistics; it does not assert novelty for the underlying automatic sequence, Fibonacci layer counts, or the membership representations.

## Limitations

The historical-priority assessment is limited to inspected accessible records and source passages; it is not a proof of uniqueness in the literature. In particular, a first-difference sequence or return-gap characterization could appear under the alternative A060142/odd-part-composition terminology. The original 1976 article was verified bibliographically but its full text was not inspected; its available abstract/landing material does not support a claim about complete gap statistics. The result concerns only consecutive ones, dyadic layer counts, and their dyadic limiting law; no claim is made about arbitrary pair distances, ordinary asymptotic density of \(S\), or limiting distributions at all cutoffs.

## References

1. L. E. Baum and M. M. Sweet, *Continued fractions of algebraic power series in characteristic 2*, Annals of Mathematics 103 (1976), 593–610. DOI: https://doi.org/10.2307/1970953 .
2. OEIS, *A060142: Ordered set defined by closure under \(2x+1\) and \(4x\)*, https://oeis.org/A060142 (record originated March 5, 2001).
3. OEIS, *A086747: Baum–Sweet sequence*, https://oeis.org/A086747 .
4. C. Kimberling, *A Self-Generating Set and the Golden Mean*, Journal of Integer Sequences 3 (2000), Article 00.2.8, https://cs.uwaterloo.ca/journals/JIS/VOL3/goldentext.html .
