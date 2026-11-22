# Exact dyadic pair correlations of the Baum–Sweet support

## Finding

Let \(b(0)=1\). For every integer \(n\geq1\), set \(b(n)=1\) if and only if every maximal run of zeroes in the ordinary base-two representation of \(n\) has even length. Set \(b(n)=0\) otherwise. For integers \(m\geq1\) and \(0\leq r<m\), define the (non-cyclic) dyadic two-point incidence count
\[
C_{m,r}=\sum_{n=0}^{2^m-2^r-1}b(n)b(n+2^r).
\]
Let \(F_0=0,F_1=1,F_{j+2}=F_{j+1}+F_j\) be the Fibonacci numbers. Then, **for every** indicated \((m,r)\),
\[
\boxed{C_{m,r}=F_{r+1}\left\lfloor\frac{m-r+1}{2}\right\rfloor.}
\]
More strongly, write \(T_r\) for the integers whose *exactly* \(r\)-digit, zero-padded binary word is a concatenation of tiles \(1\) and \(00\) (with \(T_0=\{0\}\)). The complete set of starting indices counted by \(C_{m,r}\) is
\[
\boxed{\left\{(2^{2t}-1)2^r+s:\ 0\le t\le\left\lfloor\frac{m-r-1}{2}\right\rfloor,\ s\in T_r\right\}.}
\]
Every representation in this set is unique. In particular \(|T_r|=F_{r+1}\). For fixed \(r\), the pair count grows only linearly with \(m\), whereas the support count below \(2^m\) is \(F_{m+2}\). At the macroscopic lag \(2^{m-1}\), exactly \(F_m\) pairs occur, and \(F_m/F_{m+2}\to\varphi^{-2}\), where \(\varphi=(1+\sqrt5)/2\). The count includes **all pairs** of support elements at separation \(2^r\), not only adjacent support elements.

## Assumptions and scope

The representation of a positive integer has no leading zeros, while \(b(0)=1\) by convention. In constructing \(T_r\), however, leading zeros **are included** as part of the fixed-width suffix and must occur in even runs. The empty word is the sole element of \(T_0\). Both indices in a counted pair must lie in the half-open dyadic interval \([0,2^m)\); there is no wraparound. The lag is exactly the power of two \(2^r\), not an arbitrary integer shift. Each index \(n\) represents one ordered forward pair \((n,n+2^r)\); no cyclic or multiplicity normalization is used.

## Proof

**1. Binary support language.** The positive support indices have exactly the binary expansions \(1(1\mid00)^*\). A fixed-width word with all zero runs even is uniquely tiled by \(1\) and \(00\), including pairs of leading zeros. Thus if \(a_r=|T_r|\), then \(a_0=a_1=1\) and \(a_r=a_{r-1}+a_{r-2}\) for \(r\ge2\), giving \(a_r=F_{r+1}\).

**2. Separate the shifted bit.** Fix \(m\ge1\), \(0\le r<m\) and a starting index \(n\) satisfying \(n+2^r<2^m\). There are unique integers \(a\ge0\) and \(0\le s<2^r\) with \(n=a2^r+s\). Then \(n+2^r=(a+1)2^r+s\). Write \(S\) for the fixed-width \(r\)-digit binary expansion of \(s\), and \(h\) for the number of leading zero digits of \(S\), taking \(h=r\) when \(S\) is all zeros.

**3. Carry rigidity.** Suppose both \(n\) and \(n+2^r\) are in the support. We prove \(a=2^j-1\) for some **even** \(j\ge0\). If \(a>0\) is not an all-ones binary number, uniquely write its ordinary binary representation as \(U0^e1^j\), where \(U\) is nonempty and ends in \(1\), \(e\ge1\), and \(j\ge0\) counts trailing ones. Adding one changes this portion to \(U0^{e-1}10^j\).

If \(j\ge1\), the old block of \(e\) zeros is bounded by ones inside the original high part, while the new block of \(e-1\) zeros is bounded by ones inside the incremented high part. Both numbers would therefore require \(e\) and \(e-1\) to be even, an impossibility. If \(j=0\), the new block of \(e-1\) zeros lies between two ones, forcing \(e\) odd. Its final one is followed by the \(h\) leading zeros of \(S\). Admissibility of the incremented number forces \(h\) even (whether the suffix eventually contains a one or ends in zeros). But the original number has a terminal (or followed-by-one) block of \(e+h\) zeros, which is odd, again impossible. Hence \(a\) is zero or all ones: \(a=2^j-1\).

For such an \(a\), the two high parts are respectively \(1^j\) (if \(j=0\), empty) and \(10^j\). Since the incremented integer is positive, the zero block \(0^{j+h}\) following its initial one must have even length. Admissibility of the original integer also forces \(h\) even when \(j>0\); when \(j=0\), all non-leading zeros in \(S\) must be even and \(h\) is forced even by the incremented integer. Thus \(j\) is even and \(S\) has only even zero runs. Equivalently \(j=2t\) and \(s\in T_r\). (If \(S\) has other zero runs, they are internal to \(S\) and must also be even.)

Conversely, for any \(t\ge0\) and \(s\in T_r\), both the binary strings with high parts \(1^{2t}\) and \(10^{2t}\) followed by \(S\) have only even zero runs. The exceptional all-zero initial index \(t=s=0\) is admissible by convention. Therefore precisely these pairs occur.

**4. Cutoff and count.** The incremented integer is \(2^{2t+r}+s\), so the strict upper bound \(2^{2t+r}+s<2^m\) is equivalent to \(2t+r<m\). Hence \(0\le t\le\lfloor(m-r-1)/2\rfloor\), providing exactly \(\lfloor(m-r+1)/2\rfloor\) distinct choices. Their residue \(s\bmod2^r\) and high quotient are unique. Multiplication by \(|T_r|=F_{r+1}\) proves both statements.

**5. Scale comparison.** A positive support number of exactly \(j\) binary digits has \(F_j\) choices, by the same tile decomposition after its first \(1\). Summing over \(1\le j\le m\), and including \(0\), gives \(F_{m+2}\) support indices below \(2^m\). The conclusions for fixed \(r\) and for \(r=m-1\) follow immediately from the formula and the standard Fibonacci ratio limit.

## Verification

Run `python3 checks/direct_check.py` and `python3 checks/carry_automaton.py` using Python 3 and only the standard library. The first program enumerates the Baum–Sweet definition directly, constructs the claimed pair sets via independent tile recursion, and verifies equality of **full sets** for all \(1\le m\le15\) and \(0\le r<m\). The second uses low-to-high binary addition with carry and two independent zero-run-parity states; it verifies \(1{,}830\) counts for all \(1\le m\le60\). Both programs were executed successfully. Finite checks are corroborative; the unrestricted theorem follows from the proof above.

## Relationship to prior work

The support language and its recurrence have been known since the original Baum–Sweet construction; OEIS A060142 records the equivalent support-closure rules \(0\in S\), \(n\in S\implies 2n+1,4n\in S\). Adamczewski–Rivoal study the associated generating function and rational approximations, not this two-point count; Mérai–Winterhof study pseudorandomness and correlation *measures*, giving Baum–Sweet well-distribution bounds but no exact support-pair incidence at prescribed dyadic lags. Kimberling's 2000 paper studies a distinct, though superficially related, closure system.

Two publicly available Baum–Sweet return-gap studies establish **consecutive** support gaps and their Fibonacci multiplicities, including the exact dyadic prefix histogram. The present formula counts **nonconsecutive pairs too**. Indeed for \(r\ge2\), \(2^r\) does not belong to the documented adjacent-gap spectrum, yet \(C_{m,r}>0\) for every \(m>r\). An adjacent-gap histogram does not determine how sums of successive gaps line up, so those statements do not imply the present pair count. Searches for dyadic pair-incidence, autocorrelation, carry equivalences, and the Fibonacci-times-floor formula yielded no equivalent statement in the checked indexed records or inspected sources; this is not a claim of exhaustive historical priority.

## Limitations

This is a deterministic, unnormalized two-point incidence enumeration, not a probabilistic independence theorem or a general autocorrelation formula for all shifts. The support has zero natural density, and the displayed scale comparison uses dyadic intervals. Historical search cannot rule out unindexed or unpublished equivalent pair-count calculations. The original 1976 work was verified bibliographically but not fully available in this inspection; it is not characterized as excluding the present result. The day-verified historical anchor is OEIS A060142's March 5, 2001 entry; earlier work exists, but its exact first-public calendar date was not established here. Independent mathematical audit has not been performed.

## References

1. L. E. Baum and M. M. Sweet, *Continued Fractions of Algebraic Power Series in Characteristic 2*, Annals of Mathematics 103 (1976), 593–610, https://doi.org/10.2307/1970953 .
2. C. Kimberling, OEIS A060142, original entry dated March 5, 2001, https://oeis.org/A060142 .
3. B. Adamczewski and T. Rivoal, *Irrationality measures for some automatic real numbers*, Section 2.4, https://adamczewski.perso.math.cnrs.fr/IMAN.pdf .
4. L. Mérai and A. Winterhof, *On the pseudorandomness of automatic sequences*, arXiv:1710.03026 (October 9, 2017), https://arxiv.org/abs/1710.03026 .
5. C. Kimberling, *A Self-Generating Set and the Golden Mean*, J. Integer Sequences 3 (2000), Article 00.2.8, https://cs.uwaterloo.ca/journals/JIS/VOL3/goldentext.html .
6. *Exact dyadic gap law for the Baum–Sweet support*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-dyadic-gap-law-for-the-baum-sweet-support--98bde352d9b4 .
7. *The complete return-gap law for the Baum–Sweet sequence*, public mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-the-complete-return-gap-law-for-the-baum-sweet-sequence--34910b02e3eb .
