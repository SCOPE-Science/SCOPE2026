# Abelian-square spectra and sharp minima for triple-plus-singleton binary words

## Finding
Let \(i,j,k\) be arbitrary nonnegative integers, and let
\[w(i,j,k)=b^i a^3 b^j a b^k,\qquad n=i+j+k+4.\]
An *Abelian square* is a nonempty factor \(uv\) with \(|u|=|v|\) and the same number of each letter in \(u\) and \(v\). Count distinct factor **contents**, not occurrences, and denote their number by \(\theta(w)\). Put \(R=\max(i,j,k)\), \(u=\min(j,k)\), and
\[
F(j,k)=\begin{cases}\lfloor u/2\rfloor+1,&j\text{ even},\\
\lceil u/2\rceil,&j\text{ odd};\end{cases}
\qquad G(i,j,k)=\max(0,1+\min(k,i-j)).
\]
Then the complete set of distinct Abelian squares is the union
\[
\begin{aligned}
\mathcal B&=\{b^{2h}:1\le h\le\lfloor R/2\rfloor\},\\
\mathcal A_2&=\{aa\}\cup\{ab^j ab^y:0\le y\le\min(j,k),\ y\equiv j\pmod 2\},\\
\mathcal A_4&=\{b^{j+y}a^3b^j ab^y:0\le y\le k,\ j+y\le i\}.
\end{aligned}
\]
The three families are disjoint by the number of \(a\)'s, apart from the duplicate \(aa\) within \(\mathcal A_2\) when \(j=0\). In particular,
\[
\boxed{\theta(w)=\left\lfloor\frac R2\right\rfloor+1+F(j,k)+G(i,j,k)-\mathbf 1_{j=0}.}
\]
Moreover, for every \(n\ge5\), the **sharp** minimum among exactly these triple-plus-singleton words of length \(n\) is
\[
\boxed{\min_{i,j,k\ge0\,;\ i+j+k=n-4}\theta(w(i,j,k))=\left\lfloor\frac{n+2}{4}\right\rfloor.}
\]
For \(n=4\), the sole word is \(a^4\) and has exactly two distinct Abelian squares, \(aa\) and \(a^4\). Reversal and swapping letters give corresponding conclusions for the mirror-image and complemented families.

## Assumptions and scope
The alphabet is the two-letter alphabet \(\{a,b\}\). All exponents in the definition are integers, with \(i,j,k\ge0\); empty powers are allowed. In particular, the displayed family can have fewer than five maximal runs. The assertion concerns contiguous **linear** factors, not circular factors or Abelian equivalence classes. There are exactly four occurrences of \(a\) in each word. The sharp minimum ranges only over words with three consecutive \(a\)'s and one additional \(a\), not over all binary words with four occurrences of \(a\).

## Proof
**Step 1: Partition by the count of \(a\).** An Abelian square has an even number of \(a\)'s, hence exactly \(0,2,\) or \(4\), since the entire word has four. The maximum constant run of \(b\)'s has length \(R\). Thus the complete zero-\(a\) family is \(\mathcal B\), containing \(\lfloor R/2\rfloor\) words.

**Step 2: Two occurrences of \(a\).** The only pairs of \(a\)'s that can occur in a factor without a third \(a\) between them are adjacent members of \(a^3\), yielding just the content \(aa\), and the last \(a\) of \(a^3\) together with the isolated \(a\). In the latter case the first \(a\) cannot be preceded by \(b\) inside the factor (its predecessor is another \(a\)), so the factor must be \(ab^j ab^y\), where \(0\le y\le k\). Write its half-length as \(h=(j+y+2)/2\). Having one \(a\) in each half is equivalent to \(h\) being integral and the second \(a\) starting in the second half: \(h\le j+1\). These are precisely the conditions \(y\equiv j\pmod2\) and \(y\le j\). Conversely, each such factor is Abelian-square because both halves contain exactly one \(a\). The resulting count is \(1+F(j,k)-\mathbf1_{j=0}\): the only duplicate is \(aa\) when \(j=y=0\).

**Step 3: Four occurrences of \(a\).** A factor containing every \(a\) is uniquely of the form \(b^x a^3b^j ab^y\), with \(0\le x\le i\), \(0\le y\le k\). The two halves must each contain exactly two \(a\)'s. Hence the midpoint is exactly between the second and third \(a\)'s in the triple. Equality of half-lengths forces \(x+2=j+2+y\), that is, \(x=j+y\). This is feasible precisely when \(0\le y\le k\) and \(j+y\le i\), giving the family \(\mathcal A_4\) of size \(G(i,j,k)\). Different \(y\)'s give different contents because their terminal \(b\)-run lengths differ. This proves the complete factor-set and count formula.

**Step 4: Uniform lower bound.** Write \(B=i+j+k=n-4\). We show \(4\theta(w)\ge B+3\); as \(\theta(w)\) is integral, it then follows that \(\theta(w)\ge\lceil(B+3)/4\rceil=\lfloor(n+2)/4\rfloor\).

If \(j=0\), the formula reduces to \(\theta=\lfloor R/2\rfloor+\min(i,k)+2\), with \(R=\max(i,k)\). Since \(4\lfloor R/2\rfloor\ge2R-2\), one has \(4\theta\ge2R+4\min(i,k)+6\ge i+k+3=B+3\).

If \(j>0\) and \(k>0\), set \(q=\min(j,k)\ge1\). In either parity, \(F(j,k)\ge q/2\). Since \(4\lfloor R/2\rfloor\ge 2R-2\) and \(G\ge0\), the count formula gives \(4\theta\ge2R+2q+2\). Furthermore, \(i\le R\) and \(j+k=\max(j,k)+q\le R+q\), so \(B\le2R+q\). Therefore \(4\theta\ge B+q+2\ge B+3\).

Finally, if \(j>0\) and \(k=0\), then \(q=0\), \(R=\max(i,j)\), and \(G=\mathbf1_{i\ge j}\). If \(j\) is even, \(F=1\), so \(\theta\ge\lfloor R/2\rfloor+2\), yielding \(4\theta\ge 2R+6\ge i+j+3\). If \(j\) is odd and \(i<j\), then \(\theta=(j+1)/2\) and \(i+j\le2j-1\), so \(4\theta=2j+2\ge i+j+3\). If \(j\) is odd and \(i\ge j\), then \(\theta=\lfloor i/2\rfloor+2\), so \(4\theta\ge2i+6\ge i+j+3\). All cases are covered.

**Step 5: Equality for every length.** For \(n=4q+r\), \(0\le r\le3\), use the following nonnegative parameters, for the specified ranges:

| Residue | Range | \((i,j,k)\) | Exact value |
|---|---|---|---|
| \(r=0\) | \(q\ge2\) | \((2q-3,2q-1,0)\) | \(q\) |
| \(r=1\) | \(q\ge1\) | \((2q-2,2q-1,0)\) | \(q\) |
| \(r=2\) | \(q\ge1\) | \((2q-1,2q-1,0)\) | \(q+1\) |
| \(r=3\) | \(q\ge1\) | \((2q-2,2q+1,0)\) | \(q+1\) |

Each row has \(i+j+k+4=n\), and direct substitution in the proved count formula gives the listed value, equal to \(\lfloor(n+2)/4\rfloor\). The remaining case \(n=4\) is \(w=a^4\), whose two squares are explicit. This proves sharpness for the complete parameter range.

## Verification
The standalone Python 3 program `verify.py` independently enumerates literal factors of each of \(19^3=6859\) parameter triples with \(0\le i,j,k\le18\). It checks equality of the **sets** with the three displayed families, the closed count formula, and the lower bound. A second enumeration over all parameter triples at each \(4\le n\le40\) checks the restricted minimum and constructive witnesses. The direct program passed those tests. These experiments are corroboration, while the parameter-free proof above establishes the statements for all nonnegative integers.

## Relationship to prior work
Fazekas, Mammoliti, Mercaş and Simpson (first public version 2026-04-25, arXiv:2604.23188) determine minimum counts with at most three occurrences of one letter, give a construction for larger fixed weights, and leave general fixed-weight minima open. Their Theorem 12 treats a special effective **four-run** construction and supplies equality examples but not the complete factor sets or lower bound for arbitrary five-run triple-plus-singleton words. A previously available exact four-run classification also covers the \(k=0\) boundary of the present family; neither four-run statement logically covers the genuine five-run cases \(i,j,k>0\). The new contribution is the exhaustive all-parameter factor-set formula across that additional run and the corresponding sharp restricted lower bound, not the already-known existence of four-run witnesses. The original fixed-weight-four minimum over *all* words remains unresolved by this theorem.

## Limitations
The theorem does not prove \(M(4,n)\) for unrestricted four-\(a\) words: words whose \(a\)-run composition is \((2,2)\), \((2,1,1)\), or \((1,1,1,1)\) are outside the family. It also does not classify all restricted minimizers, only their sharp minimum and explicit witnesses. It is not an independent historical-priority certification; equivalent unindexed results remain possible.

## References
- Szilárd Zsolt Fazekas, Adam Mammoliti, Robert Mercaş, and Jamie Simpson, *Binary Words Containing Few Abelian Squares*, arXiv:2604.23188 (first public version 2026-04-25). https://arxiv.org/abs/2604.23188
- Gabriele Fici and Aleksi Saarela, *On The Minimum Number of Abelian Squares in a Word*, Dagstuhl Reports 4 (2014), cited in arXiv:2604.23188.
- Gabriele Fici and Svetlana Puzynina, *Abelian combinatorics on words: a survey*, Computer Science Review 47 (2023), 100532, cited in arXiv:2604.23188.
