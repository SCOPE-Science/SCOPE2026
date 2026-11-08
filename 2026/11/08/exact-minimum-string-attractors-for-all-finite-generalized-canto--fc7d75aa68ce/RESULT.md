# Exact minimum string attractors for all finite generalized Cantor words

## Finding

For every integer \(b\ge 3\), let \(\mu_b\) be the binary uniform morphism
\[\mu_b(1)=10^{b-2}1,\qquad \mu_b(0)=0^b,\]
and let \(C_{b,k}=\mu_b^k(1)\) for every integer \(k\ge1\). A *string attractor* of a nonempty finite word \(w\) is a set of positions meeting at least one occurrence of every distinct nonempty contiguous factor of \(w\). Its minimum cardinality is \(\gamma^*(w)\).

**Theorem.** For all \(b\ge3\) and \(k\ge1\),
\[\boxed{\gamma^*(C_{b,k})=\max\{2,k\}.}\]
For \(k=1\), a minimum attractor (in zero-based positions) is \(\{0,b-2\}\). For every \(k\ge2\), writing \(Q=b^{k-1}\), an explicit minimum attractor is
\[\boxed{\Gamma_{b,k}=\{Q-1,(b-1)Q-1\}\;\cup\;\{(b-1)Q+b^i-1:1\le i\le k-2\}.}\]
The latter set has exactly \(k\) elements. Both the optimum and its witnesses are exact for composite as well as prime bases.

## Assumptions and scope

The alphabet is \(\{0,1\}\); factors are **contiguous** and nonempty. All attractor positions are indices in \(\{0,\ldots,b^k-1\}\) using zero-based indexing; a position meets an occurrence if it lies in its closed index interval. We consider every finite morphic iterate \(C_{b,k}\), not the minimum attractor of an unspecified infinite word. The recursion is
\[C_{b,k}=C_{b,k-1}0^{(b-2)b^{k-1}}C_{b,k-1}.\]
For \(k\ge2\), put \(J=2^{k-1}\), \(Q=b^{k-1}\), \(A=Q-1\), and \(Z=(b-1)Q\). Then \(A\) is the final one in the left copy, \(Z\) is the first one in the right copy, and positions \(A+1,\ldots,Z-1\) form the unique longest zero run, of length \(G=(b-2)Q\). The second displayed attractor is \(\{A,Z-1\}\) plus \(k-2\) positions in the right copy.

## Proof

**1. Exact gap arithmetic.** Label the \(2^k\) one-positions of \(C_{b,k}\) increasingly as \(p_0,\ldots,p_{2^k-1}\). Writing \(j\) in binary and replacing every binary one digit by the base-\(b\) digit \(b-1\) gives \(p_j\). In particular, \(p_{J-1}=A\), \(p_J=Z\), and for \(1\le j<2^k\), the number of zeros strictly between the adjacent ones \(p_{j-1}\) and \(p_j\) is
\[g_j=p_j-p_{j-1}-1=(b-2)b^{\nu_2(j)}.\]
This follows by adding one to the binary expansion of \(j-1\): the trailing binary ones become zeros and the first zero becomes one. Here \(\nu_2(j)\) is the exponent of two dividing the positive integer \(j\). The central gap \(g_J=G\) is uniquely longest.

**2. Factors with at most one one.** Every all-zero factor lies in the longest zero run and can be placed to meet \(Z-1\). Every exactly-one-one factor has shape \(0^a10^d\). In an actual occurrence, at least one of \(a,d\) is at most \(b-2\), since the two adjacent gap indices at any nonendpoint one are consecutive and hence one is odd, whereas an endpoint has exterior padding zero. If \(a\le b-2\), re-place the factor at the one at \(A\), whose left gap has length \(b-2\) and right gap length \(G\); the occurrence meets \(A\). Otherwise \(a>b-2\), so \(d\le b-2\), and the factor can be placed at the one at \(Z\), with left gap \(G\) and right gap \(b-2\). Since \(a>0\), its occurrence meets \(Z-1\). The factor `1` is included in this argument.

**3. Transfer lemma for multi-one factors.** Let a factor contain at least two ones; write its consecutive internal gap indices as \(a,a+1,\ldots,c\). Among them there is a unique index \(j_0\) of maximum two-adic valuation \(r\): if two distinct indices had the same maximal valuation, an index strictly between them would have larger valuation. If \(r=k-1\), the factor traverses the central gap and meets \(A\) or \(Z-1\). Assume \(0\le r\le k-2\), and set \(t=j_0-a\), \(u=c-j_0\). The neighboring indices \(j_0\pm 2^r\), when present, have valuation greater than \(r\), so \(0\le t,u\le 2^r-1\).

The internal pattern of zero gaps to either side of \(j_0\) is determined solely by \(r,t,u\), since \(\nu_2(j_0+s)=\nu_2(s)\) for \(0<|s|<2^r\). Thus it can be translated, including its two terminal ones, to either canonical gap index
\[j_R=J+2^r\qquad\text{or}\qquad j_L=J-2^r.\]
What remains is the amount of exterior zero padding. At the right canonical placement, left padding is always sufficient: its preceding gap is identical to the original one when \(t<2^r-1\), and is the uniquely largest gap \(g_J=G\) when \(t=2^r-1\). Similarly its right padding is sufficient when \(u<2^r-1\). If \(u=2^r-1\), the next right gap there is \(g_{J+2^{r+1}}=(b-2)b^{r+1}\) for \(r\le k-3\), and is the right boundary for \(r=k-2\). If the requested padding does not fit, the actual following gap of the original factor must have valuation at least \(r+2\), or (for \(r=k-2\)) the factor must lie at the left canonical gap. In the former case the actual preceding gap at distance \(2^r\), when present, has valuation exactly \(r+1\). Consequently the left canonical placement has enough left padding as well: its preceding gap is \(g_{J-2^{r+1}}=(b-2)b^{r+1}\) when \(r\le k-3\), or the left word boundary when \(r=k-2\); its right exterior gap is the largest gap \(g_J=G\). This proves that either the right canonical placement is valid, or the left canonical placement is valid with \(u=2^r-1\).

For \(1\le r\le k-2\), the right canonical factor spans its left one
\[p_{j_R-1}=Z+b^r-1\in\Gamma_{b,k}.\]
For \(r=0\), provided \(k\ge3\), that factor spans its right one \(p_{j_R}=Z+b-1\), the member of \(\Gamma_{b,k}\) with \(i=1\). In the exceptional left placement, \(u=2^r-1\) makes the final one precisely \(p_{J-1}=A\). Hence every multi-one factor meets the displayed attractor for \(k\ge3\).

For \(k=2\), a factor with at least three ones necessarily contains the unique central gap and meets \(A\) or \(Z-1\). A factor with exactly two ones and an internal noncentral gap must be of the form \(0^a10^{b-2}10^d\): it occurs either in the left copy (with \(a=0\), meeting \(A\)) or in the right copy (with \(d=0\)); in the latter case, if \(a>0\) the occurrence meets \(Z-1\), and if \(a=0\) the same factor also occurs in the left copy. This establishes the upper bound \(\gamma^*(C_{b,k})\le k\) for \(k\ge2\). For \(k=1\) the explicit two-point set intersects every factor of \(10^{b-2}1\).

**4. Matching lower bound.** A factor \(F\) imposes a *support*: the union of index sets of all occurrences of \(F\). Supports of pairwise disjoint factors require distinct positions in any attractor. For \(k=1\), `0` and `1` have disjoint nonempty supports. For \(k=2\), the factors `1` and \(0^G\) have disjoint nonempty supports; the latter occurs solely inside the central largest gap.

For \(k\ge3\), put \(h=(b-2)b^{k-2}+1\) and use the following \(k\) factors:
\[F_-=10^h,\qquad F_+=0^h1,\qquad F_r=10^{(b-2)b^r}1\quad(1\le r\le k-2).\]
The length-\(h\) zero run in \(F_-\) or \(F_+\) exists only in the central largest zero gap. The former is supported on the central left one and its first \(h\) zeros; the latter is supported on the central right one and its last \(h\) zeros. These supports are disjoint because \(2h\le G\) for \(b\ge3,k\ge3\). For \(r\ge1\), the gap occurrence in \(F_r\) must have index of two-adic valuation \(r\), hence an even gap index. Two distinct even gap indices cannot be consecutive; therefore the supports of all \(F_r\) are pairwise disjoint. Moreover neither endpoint of the central largest gap belongs to an \(F_r\) support, because its neighboring gap indices \(J-1,J+1\) are odd, so those supports are disjoint from the supports of \(F_-\) and \(F_+\). Thus any attractor needs at least \(k\) positions. Together with the upper construction, this proves the theorem for every stated base and depth.

## Verification

The accompanying standard-library Python verifier constructs \(C_{b,k}\) independently, enumerates **all** distinct factors and the union of every factor's occurrence positions, checks that every factor has an occurrence meeting \(\Gamma_{b,k}\), and checks that the specified lower-bound witnesses have nonempty pairwise disjoint occurrence supports. Run `python3 VERIFY.py` in the same directory. The recorded diagnostic output was `VERIFY_OK cases=23 factors=264990`, with bases from three through nine and depths selected so that the largest length was \(729\). This finite verification checks the implementations and boundary cases; the proof above is the infinite justification.

## Relationship to prior work

Restivo, Romana and Sciortino (2022) study string attractors and infinite words, including finite-prefix profiles. Cassaigne, Gheeraert, Restivo, Romana, Sciortino and Stipulanti (2023 preprint/2024 journal) establish logarithmic-order attractor-profile behavior in a ternary Cantor-related infinite word (their Example 13, after alphabet complementation); they do not give the exact \(\gamma^*(C_{b,k})\) at every morphic iterate nor these explicit all-base optimal sets. Schaeffer and Shallit (2020) give decision and structural methods for string attractors of automatic sequences, rather than this exact family formula. The present theorem refines the qualitative logarithmic-scale picture to an exact finite-iterate optimum for all integer bases. Bibliographic completeness is not claimed; a separately unpublished equivalent is possible.

## Limitations

The theorem concerns precisely the finite words \(C_{b,k}\), not all arbitrary-length prefixes of the infinite fixed point, all Cantor-like morphisms, or arbitrary factors. The exhibited minimum attractor need not be unique. The direct verifier uses exhaustive finite factor enumeration and makes no claim of machine certification of all infinite cases. Independent external scientific validation is not claimed.

## References

1. A. Restivo, G. Romana and M. Sciortino, *String Attractors and Infinite Words*, arXiv:2206.00376 (first public 2022-06-01). https://arxiv.org/abs/2206.00376
2. J. Cassaigne, F. Gheeraert, A. Restivo, G. Romana, M. Sciortino and M. Stipulanti, *New string attractor-based complexities for infinite words* (2023 preprint; later journal version), especially Example 13 and Theorem 22. https://orbi.uliege.be/bitstream/2268/309672/1/String_attractors__journal_version_%20%282%29.pdf
3. L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840 (2020). https://arxiv.org/abs/2012.06840
