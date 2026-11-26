# The second-largest gap of \(\Phi_{35p}\) and its multiplicity

## Finding

Let \(p>35\) be prime, and write \(p=35q+r\), with \(1\le r<35\) and \(\gcd(r,35)=1\). A gap of a polynomial means the difference between successive exponents in its nonzero coefficient support. The largest gap of \(\Phi_{35p}\) is \(24\), occurring \(2q\) times. The **second-largest distinct** gap is
\[
s_r=24-\min(r,35-r).
\]
Its exact multiplicity is \(a_rq+b_r\), with the following parameters:

| \(r\) | \(a_r\) | \(b_r\) |
|:--|--:|--:|
| 1, 2, 3, 4, 6 | 8 | 0 |
| 8 | 10 | 2 |
| 9, 11, 12, 13 | 8 | 2 |
| 16, 17 | 10 | 4 |
| 18, 19 | 10 | 6 |
| 22, 23, 24, 26 | 8 | 6 |
| 27 | 10 | 8 |
| 29, 31, 32, 33, 34 | 8 | 8 |

In particular, the length is unchanged under \(r\mapsto 35-r\), but its frequency at a fixed quotient need not be. The classification is for the first ternary family with smallest prime factor larger than three: \(35=5\cdot7\). It concerns a feature below the known maximum, which by itself does not identify the next gap or its frequency.

## Proof

We recall the specialized gap count reduction to make the finite certificate explicit. The affine gap-frequency law used in this reduction is a known general method (see below), not an originality claim of this result.

Write \(C_e=[X^e]\Phi_{35}(X)\) for \(0\le e\le24\). In order from the constant term the coefficients are

`[1,-1,0,0,0,1,-1,1,-1,0,1,-1,1,-1,1,0,-1,1,-1,1,0,0,0,-1,1]`.

Indeed, \(\Phi_{35}(X)=(1-X^{35})(1-X)/((1-X^5)(1-X^7))\). Its formal reciprocal is \((1+X+X^2+X^3+X^4)(1-X^7)/(1-X^{35})\). Thus its coefficients are \(h(n)\) for \(n\ge0\), with the period-35 function \(h\) equal to \(1\) on residues \(0,\dots,4\), \(-1\) on residues \(7,\dots,11\), and zero elsewhere.

For any integer \(u=35q+r\), \(q\ge1\), \(r\) a unit, set \(F_u(X)=\Phi_{35}(X^u)/\Phi_{35}(X)\). This is an integer polynomial since every primitive 35th root stays primitive upon raising to the \(u\)-th power, and divisor and dividend are monic over the integers. Its degree is \(24(u-1)\); for prime \(u=p>35\) it equals \(\Phi_{35p}\). For \(0\le j\le23\), the coefficient at degree \(ju+t\) within block \(j\) equals
\[
w_{j,r}(t)=\sum_{e=0}^{j}C_e h((j-e)r+t).
\]
The block length is \(u\) except at \(j=23\), where it is \(u-23\). Hence each block is a prefix of a periodic word of period 35. The full-length blocks have nonempty support because every period word in these residue cases has a nonzero entry (checked below); the last block has the monic leading term.

Let \(B_g(r)\) count ordinary support gaps of length \(g\) for \(F_{35+r}\). Let \(A_g(r)\) be the sum, over these 24 period words, of their cyclic support-gap counts of length \(g\), retaining the wraparound gap. Incrementing \(q\) increases each block length by 35, leaves its first nonzero offset fixed, and moves its last nonzero offset by exactly 35. The support indices strictly after the old last nonzero offset up to and including its translate by 35 run through one full cycle of nonzero residues; the new internal gaps have exactly the cyclic histogram. The cross-block gap is unchanged because its left tail distance and its right initial offset are both unchanged. This reasoning also applies to the truncated last block. Consequently the gap histogram of \(F_{35q+r}\) is \(B_g(r)+(q-1)A_g(r)\) for every length \(g\).

It remains to extract the largest and second-largest entries of the support of this histogram. This is a finite exact calculation over all 24 units. For clarity, for each \(r\) the following checks suffice:

1. Form the 24 period words from the formula above and check all have nonempty cyclic support. Sort their nonzero positions; take the consecutive differences and the wraparound difference to form \(A_g(r)\).
2. Form the coefficient list \(f_n\) of \(F_{35+r}\) using \(f_n=[X^n]\Phi_{35}(X^{35+r})-\sum_{1\le e\le\min(24,n)}C_e f_{n-e}\). Take the ordinary consecutive differences of nonzero indices to form \(B_g(r)\).
3. Check \(A_{24}=B_{24}=2\); that neither histogram has a gap strictly between \(s_r\) and 24; and that \(A_{s_r}=a_r\) and \(B_{s_r}=a_r+b_r\) for the table above. By the maximum-gap theorem there are no gaps larger than 24 for the prime multipliers in the claim. Every \(a_r>0\) and \(b_r\ge0\), so the second gap occurs already at the base and thus for every \(q\ge1\).

The accompanying `word_gaps_verify.py` performs the finite checks with exact integers. These checks and the gap count reduction, together with the known maximum-gap theorem for prime multipliers, complete the second-gap classification.

## Reproducibility and scope

With the accompanying `gap_spectrum_35.csv` in the same directory, run `python3 word_gaps_verify.py` using the Python standard library. The whole CSV is auxiliary: the theorem extracts the two upper gap lengths and their frequencies. Additional checks at \(q=1,2,3\) compare exact coefficient recurrence and periodic-word constructions and reconcile their histograms. Those tests do not substitute for the periodic insertion argument for arbitrary \(q\).

The result concerns exactly consecutive nonzero exponents, not the two largest frequency counts, coefficients of large magnitude, or a theorem about the second gap at an arbitrary fixed ternary base. In particular it makes no claim to a uniform second-gap expression for other values of \(m\).

## Relationship to known results

- A. Al-Kateeb, M. Ambrosino, H. Hong and E. Lee, [*Maximum gap in cyclotomic polynomials*](https://arxiv.org/abs/1911.11667), Theorem 1, already gives the maximum length \(\varphi(m)\) at odd squarefree bases and prime multipliers exceeding \(m\). Here \(\varphi(35)=24\).
- A. Al-Kateeb and A. Dagher, [*On the number of terms of some families of the ternary cyclotomic polynomials*](https://arxiv.org/abs/2207.07393v1), Theorem 4, Lemma 1 and Theorem 5, give the coefficient-block formula and the repetition and truncation used in the periodic reduction. Their explicit term-count applications concern families with smallest prime factor three.
- [*Exact affine gap spectra for cyclotomic prime extensions, including every \(\Phi_{15p}\)*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-exact-affine-gap-spectra-for-cyclotomic-prime-extensions-includi--351556961373/RESULT.md) and [*Universal affine gap profiles of cyclotomic substitution quotients*](https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-universal-affine-gap-profiles-of-cyclotomic-substitution-quotien--0500051e2451/RESULT.md) give the affine count method in broader settings, with detailed examples for base 15. We use the method at base 35 to determine the explicit second gap and its multiplicity. The simple distance-to-zero expression above is not automatic at other bases: for base 15, the second gap at residue 7 is 3 rather than \(8-7\).
- A. Cafure and E. Cesaratto, [*Gaps in binary cyclotomic polynomials*](https://arxiv.org/abs/2507.19381), Theorems 1.1–1.2, treats the second gap and some exact frequencies for the binary family. It does not establish the comparison for base 35.
