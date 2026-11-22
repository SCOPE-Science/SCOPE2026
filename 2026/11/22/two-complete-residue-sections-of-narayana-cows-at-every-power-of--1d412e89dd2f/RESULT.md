# Two complete residue sections of Narayana cows at every power of two

## Finding

Let the Narayana-cows numbers be normalized by \(a_0=a_1=a_2=1\) and \(a_{n+3}=a_{n+2}+a_n\) for all \(n\ge0\). For every integer \(k\ge1\), as \(t\) runs through \(0,1,\ldots,2^{k-1}-1\), the values
\[
 a_{7t+2}\pmod{2^k} \quad\text{and}\quad a_{7t+3}\pmod{2^k}
\]
run **exactly once through all odd residues and exactly once through all even residues**, respectively. Thus the union of these two index progressions selects precisely one representative of *each* residue modulo \(2^k\), within the least complete sequence period \(7\cdot2^{k-1}\).

In fact the two selections satisfy the stronger exact metric identity
\[
 \nu_2\bigl(a_{7t+j}-a_{7s+j}\bigr)=1+\nu_2(t-s)
 \qquad(j\in\{2,3\},\quad s,t\ge0,\quad s\ne t).
\]
Here \(\nu_2\) denotes the usual valuation of a nonzero integer. Among all seven index residue classes \(j\pmod7\), these are exactly the two for which this identity holds for all distinct nonnegative \(s,t\). Consequently both maps admit unique extensions from \(\mathbb Z_{\ge0}\) to scaled isometric bijections of \(\mathbb Z_2\) onto the indicated parity cosets of \(\mathbb Z_2\).

## Assumptions and scope

The recurrence is indexed from \(a_0=1\); several sources use the shifted normalization \(u_0=0,u_1=0,u_2=1\), related by \(a_n=u_{n+2}\). Congruences and the representative count concern every positive integer exponent \(k\), not merely large exponents. The term *least period* means the least positive \(L\) satisfying \(a_{n+L}\equiv a_n\pmod{2^k}\) for every \(n\ge0\). An isometry into a parity coset means its difference valuations are shifted upward by one. The classification of index classes is relative to this specific two-adic scaled-isometry property, not to every conceivable regularity property of the seven classes.

## Proof

**1. Explicit companion matrices.** Put
\[
 M=\begin{pmatrix}0&1&0\\0&0&1\\1&0&1\end{pmatrix},\qquad
 v=\begin{pmatrix}1\\1\\1\end{pmatrix},\qquad e=(1,0,0).
\]
Then \(a_n=eM^nv\). Direct integer multiplication gives
\[
 M^7=I+2B,\quad B=\begin{pmatrix}1&1&2\\2&1&3\\3&2&4\end{pmatrix},
\qquad M^{14}=I+4C,\quad
 C=B+B^2=\begin{pmatrix}10&7&15\\15&10&22\\22&15&32\end{pmatrix}.
\]
For each \(r\ge0\), define an integer matrix \(D_r\) by \(M^{7\cdot 2^r}=I+2^{r+1}D_r\). We have \(D_0=B\), \(D_1=C\), and squaring yields
\[
 D_{r+1}=D_r+2^r D_r^2\quad (r\ge0).
\]
Hence \(D_r\equiv C\pmod2\) for every \(r\ge1\).

**2. The parity certificates.** Exact integer arithmetic gives the following table for \(0\le j\le6\):

| \(j\) | \(a_j\) | \(eBM^jv\pmod2\) | \(eCM^jv\pmod2\) |
|---:|---:|---:|---:|
| 0 | 1 | 0 | 0 |
| 1 | 1 | 0 | 1 |
| 2 | 1 | 1 | 1 |
| 3 | 2 | 1 | 1 |
| 4 | 3 | 1 | 0 |
| 5 | 4 | 0 | 1 |
| 6 | 6 | 1 | 0 |

In particular, \(eD_rM^jv\) is odd for both \(j=2,3\), for every \(r\ge0\).

**3. Exact differences for all index pairs.** Fix \(j\in\{2,3\}\) and \(t>s\ge0\). Write \(t-s=2^rq\) with \(q\) odd. Since \(M^{7\cdot2^r}=I+2^{r+1}D_r\), the binomial expansion yields
\[
 M^{7(t-s)}-I\equiv 2^{r+1}qD_r\pmod{2^{r+2}}.
\]
This congruence also holds when \(r=0\), as all omitted terms contain \(2^{2r+2}\). Since \(M^{7s}\equiv I\pmod2\), multiplication by \(eM^{7s}\) on the left and \(M^jv\) on the right gives
\[
 a_{7t+j}-a_{7s+j}\equiv
 2^{r+1}q\,eD_rM^jv\pmod{2^{r+2}}.
\]
The coefficient is odd by Step 2. Therefore the difference has valuation exactly \(r+1\), proving the displayed identity. Reversing \(s,t\) only changes sign.

**4. Exact residue transversals.** Since \(M^7\equiv I\pmod2\), all values on each progression have the same parity as its initial term: \(a_2=1\) and \(a_3=2\). If \(0\le s<t<2^{k-1}\), then \(\nu_2(t-s)<k-1\), and Step 3 shows \(a_{7t+j}\not\equiv a_{7s+j}\pmod{2^k}\). There are \(2^{k-1}\) values and exactly \(2^{k-1}\) residues of the given parity, so each progression is a bijection onto the relevant parity coset. These are complementary; their union is a complete set of residues.

**5. Sharpness of the two index classes.** If \(j\notin\{2,3\}\), at least one of the two indicated parity entries in Step 2 is zero. If \(eBM^jv\) is even, take \((s,t)=(0,1)\); then \(a_{7+j}-a_j\) is divisible by four, contradicting the required valuation one. Otherwise \(eCM^jv\) is even; take \((s,t)=(0,2)\); then \(a_{14+j}-a_j\) is divisible by eight, contradicting the required valuation two. Thus exactly the two stated classes satisfy the unrestricted identity.

**6. Least period and 2-adic extension.** The seven terms \((a_0,\ldots,a_6)\pmod2=(1,1,1,0,1,0,0)\) have least period seven, so any period modulo \(2^k\) is a multiple of seven. The formula for \(M^{7\cdot2^{k-1}}\) makes \(7\cdot2^{k-1}\) a period modulo \(2^k\). Conversely, if \(7h\) is a period, comparison at index two and Step 3 with \(s=0,t=h\) force \(1+\nu_2(h)\ge k\). This proves that \(7\cdot2^{k-1}\) is the least period. Finally the exact difference identity implies that each progression map extends continuously to \(\mathbb Z_2\), retaining the same metric and parity. Its induced map on the finite quotient modulo \(2^k\) is bijective for every \(k\); compatibility of inverse residue classes proves surjectivity and uniqueness on the full two-adic parity coset.

## Verification

The self-contained Python file `check.py` uses only integer operations. It independently reconstructs the companion matrices and seven-row parity certificates, checks the exact metric for multiple progressions, verifies that both residue sections contain every required parity class exactly once for every \(1\le k\le12\), and checks the claimed least period directly at those levels. Run `python3 check.py` and expect `CHECK_OK`. These finite checks are reproducibility evidence; the unrestricted theorem follows from Steps 1–6, not from extrapolation.

## Relationship to prior work

Kirthi's 2015 Narayana-sequence study concerns modular periods and correlation statistics, especially at prime moduli; it does not state either exact two-adic scalar permutation. The OEIS Narayana period table gives period lengths but not the values or their complete parity-residue sections. Related explicit two-adic valuation results determine divisibility layers of another standard indexing, not the unit residues of these two sections. A published exact-zero count for a shifted Narayana recurrence covers one zero residue per period on an associated nonsingular branch; its matrix method overlaps the method here but the zero-fiber statement does not determine a complete residue permutation or the second, complementary parity section. The known full-state functional-graph classification for this cubic companion map determines state cycles, not coordinatewise modular residue bijections. The distinction is between periods/zero counts/valuations of individual coefficients and the *full exact scalar residue transversals* proved here.

## Limitations

The result does not determine the complete multiplicities of all residues across the entire length-\(7\cdot2^{k-1}\) period; other five index classes may contribute additional representations. A complete inventory of historical recurrence-distribution papers is not claimed; a stronger unindexed theorem may cover this statement. The isometric lifting mechanism shares classical tools with existing work, and an independent mathematical audit has not been performed. The first date recorded as a precise day is that of the explicitly inspected 2015 archival research source; the Narayana recurrence itself is centuries old and older literature includes publications with year-only metadata.

## References

1. K. Kirthi, *Narayana Sequences for Cryptographic Applications*, arXiv:1509.05745v1 (first posted 2015-09-17), https://arxiv.org/abs/1509.05745 .
2. OEIS A000930, *Narayana's cows sequence*, https://oeis.org/A000930 .
3. OEIS A271953, *Periods of A000930 modulo \(n\)*, https://oeis.org/A271953 .
4. J.-P. Allouche and T. Johnson, *Narayana's Cows and Delayed Morphisms*, 1996, freely available at https://oeis.org/A000930/a000930.pdf .
5. R. Guadalupe, *On the 3-adic valuation of the Narayana numbers*, arXiv:2112.06187 (2021), https://arxiv.org/abs/2112.06187 .
