# Sharp reversal-freeness and reflection complexity of generalized Thue–Morse words

## Finding

Let \(b\ge2\) and \(m\ge3\) be integers, and let \(\mathbf t_{b,m}=(s_b(n)\bmod m)_{n\ge0}\), where \(s_b(n)\) is the sum of the base-\(b\) digits of \(n\). Write \(\mathcal L_n\) for its set of distinct length-\(n\) contiguous factors, \(\rho_{b,m}(n)=|\mathcal L_n|\), and \(r_{b,m}(n)\) for the number of equivalence classes obtained by identifying a factor with its ordinary reversal **only when that reversal also belongs to the language**. Set \(g=\gcd(b-1,m)\).

The following classification holds for every such \(b,m\):

\[
r_{b,m}(0)=1,\qquad r_{b,m}(1)=m,\qquad
r_{b,m}(2)=\begin{cases}
\tfrac12m(m+1),&g=1,\\
\tfrac14m^2,&g=2,\\
\tfrac1g m^2,&g\ge3,
\end{cases}\qquad
r_{b,m}(n)=\rho_{b,m}(n)\quad(n\ge3).
\]

More precisely, no length-\(4\) (or longer) factor has its reversal in the language. At length \(3\), the only factors whose reversal also occurs are exactly \(2m\) palindromes \((a,a+1,a)\) and \((a,a-1,a)\), for \(a\in\mathbb Z/m\mathbb Z\), when \(g\le2\); there are none when \(g\ge3\). At length \(2\), reversal pairs occur if and only if \(g\le2\). Thus the **least length** at which every factor is reversal-unpaired is \(4\) for \(g\in\{1,2\}\), and \(2\) for \(g\ge3\). Here \(\rho_{b,m}\) is the ordinary factor complexity, which is studied independently in the literature; no new explicit formula for that separate invariant is claimed.

## Assumptions and scope

All words are finite contiguous factors of the right-infinite digit-sum word; starting positions are nonnegative integers. Letters are residues in \(\mathbb Z/m\mathbb Z\). Reversal fixes the alphabet symbols: it is **not** a complemented or translated antimorphism. The base may be composite. For \(x\ge1\), define the base-\(b\) divisibility exponent \(\nu_b(x)=\max\{v\ge0:b^v\mid x\}\), even when \(b\) is composite. The empty factor is counted once at length zero. The theorem makes no assertion for \(m=2\), where \(1=-1\) in the residue alphabet and the obstruction used below fails.

## Proof

**1. Digit increments.** Adding one to a base-\(b\) numeral changes a terminal string of \(v\) digits \(b-1\) into zeros and increases the preceding digit. Therefore for every \(n\ge0\),
\[
t_{b,m}(n+1)-t_{b,m}(n)\equiv 1-(b-1)\nu_b(n+1)\pmod m.\tag{1}
\]
Among any two consecutive positive integers, at most one is divisible by \(b\); hence every pair of consecutive word increments contains an increment \(+1\).

**2. Exact adjacent-pair language.** Equation (1) shows that possible differences between consecutive letters are exactly
\[
\Delta=\{1-(b-1)v\bmod m:v\ge0\}=\{d\in\mathbb Z/m\mathbb Z:d\equiv1\pmod g\}.
\]
All differences occur: the step ending at \(n+1=b^v\) has the indicated difference. Moreover every finite factor occurs with **any** additive alphabet translate. Indeed, if a length-\(L\) factor starts at \(n\), choose \(H\) with \(n+L<b^H\) and choose \(R\ge0\) with any prescribed digit-sum residue modulo \(m\). Then for \(0\le j<L\),
\[
s_b(Rb^H+n+j)=s_b(R)+s_b(n+j),
\]
so the factor at \(Rb^H+n\) is the required translate. A number \(R\) with digit sum exactly any chosen nonnegative integer is obtained by a base-\(b\) repunit. Consequently
\[
\mathcal L_2=\{(a,a+d):a\in\mathbb Z/m\mathbb Z,\ d\in\Delta\},\qquad |\mathcal L_2|=m^2/g.
\]
A reversed two-letter factor exists precisely when \(-d\in\Delta\), or equivalently \(g\mid2\). If \(g=1\), all \(m^2\) pairs occur and the \(m\) diagonal pairs are fixed under reversal, giving \(m(m+1)/2\) reversal classes. If \(g=2\), all \(m^2/2\) pairs occur in reversal pairs, with no diagonal pairs, giving \(m^2/4\) classes. If \(g\ge3\), none has its reversal in the language, giving \(m^2/g\) classes.

**3. Reversible triples must be palindromes.** Let a length-three factor have successive differences \((x,y)\). Both the factor and its reversed word can occur only if each of \((x,y)\) and \((-y,-x)\) is a legal consecutive-increment pair. By step 1, each such pair includes \(+1\); thus \((x,y)\) includes both \(+1\) and \(-1\). Since \(m\ge3\), these residues are distinct. Therefore \((x,y)=(1,-1)\) or \((-1,1)\), and the factor is necessarily palindromic. Such a triple exists exactly when \(-1\in\Delta\), i.e. \(g\mid2\). To see existence in both orientations, choose a positive integer \(v\) with \((b-1)v\equiv2\pmod m\); around the step ending at \(b^v\), the consecutive three increments include \((1,-1,1)\), since the two neighboring positive integers are not divisible by \(b\). Translating letters as in step 2 realizes all \(2m\) displayed palindromes. A word of length three cannot have adjacent increments both zero, by step 1, so there are no other palindromes.

**4. No reversible four-letter factor.** If a four-letter factor had its reversal in the language, then both its overlapping length-three subfactors would also have their reversals in the language. By step 3, each such subfactor would be palindromic, and hence the four-letter word must alternate \((a,c,a,c)\). The absence of \((0,0)\) consecutive increments rules out \(a=c\). The two orientations of an alternating four-letter word have increment patterns \((1,-1,1)\) and \((-1,1,-1)\), by step 3. Its reversed word would force the latter pattern to occur. We show \((-1,1,-1)\) is impossible. Both steps with increment \(-1\) require \(\nu_b(N)>0\) at positive integers \(N\) distance two apart, by (1) and \(m\ge3\). For \(b\ge3\), two integers distance two apart cannot both be divisible by \(b\). For \(b=2\), two even integers distance two apart have valuations such that one is exactly \(1\), and its increment \(1-(b-1)\cdot1=0\), not \(-1\) modulo \(m\ge3\). Both cases contradict the pattern. Thus no four-letter factor can coexist with its reversal.

**5. All longer lengths and reflection counts.** If a length-\(n\) word with \(n\ge4\) and its reverse both occurred, their length-four subfactors at the corresponding endpoints would form a forbidden reversed pair. Therefore all factors of length at least four are reversal-unpaired. By step 3, the length-three reversible factors are palindromes only, so identifying reversals never merges two *distinct* length-three factors. It follows that \(r_{b,m}(n)=\rho_{b,m}(n)\) for all \(n\ge3\). Length-one factors exhaust the residue alphabet by the translation argument, and the empty word gives \(r_{b,m}(0)=1\). This proves every statement.

## Verification

The standalone standard-library program `verify.py` implements an exact symbolic length-two-through-four factor-language enumerator from base-\(b\) divisibility signatures, independently checks realizability by actual digit-sum indices and compares its predictions against direct 100000-symbol prefixes. Execute `python3 verify.py`. A completed run reported `VERIFICATION_OK`, comprising 1406 base/modulus pairs for the symbolic small-language checks, 24843 constructive digit-index witnesses and direct factor checks for 20 parameter pairs. These finite checks are supporting reproducibility; the infinite theorem is established by the preceding argument.

## Relationship to prior work

Allouche, Campbell, Li, Shallit and Stipulanti (2024) introduce reflection complexity and, in their discussion of generalized Thue–Morse sequences, note the special case \(b=2,m=3\): reflection complexity agrees with ordinary factor complexity from length three. **That special case is not claimed as new.** The present proof establishes the uniform statement for every base \(b\ge2\) and alphabet modulus \(m\ge3\), plus the exact gcd-controlled short-factor counts and sharp reversal-freeness thresholds. Starosta (2011) develops generalized Thue–Morse factor languages, palindromes and symmetry under the **dihedral antimorphisms that combine reversal with symbol transformations**; these are distinct from ordinary reversal without a symbol map. Fleischer and Shallit (2019) study reversal avoidance more generally, not this complete digit-sum family. Later work by Blažek, Dvořáková and Pelantová (2026) studies generalized reflection complexity for binary sequences and group actions, not the present \(m\ge3\) ordinary-reversal classification.

## Limitations

The result does not supply a new closed expression for the separately studied ordinary factor complexity \(\rho_{b,m}(n)\), though it determines reflection complexity in terms of that invariant for every \(n\ge3\). It does not address \(m=2\), generalized group-relative reversal, or factor frequencies. Computational tests cannot establish originality; potentially unindexed literature may overlap the uniform assertion. The result has not undergone independent scientific audit.

## References

- J.-P. Allouche, C. Campbell, S. Li, J. Shallit and M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302 (first posted 2024-06-13), https://arxiv.org/abs/2406.09302.
- Š. Starosta, *Generalized Thue–Morse words and palindromic richness*, arXiv:1104.2476 (2011), https://arxiv.org/abs/1104.2476.
- L. Fleischer and J. Shallit, *Words Avoiding Reversed Factors, Revisited*, arXiv:1911.11704 (2019), https://arxiv.org/abs/1911.11704.
- O. Blažek, L. Dvořáková and E. Pelantová, *Generalized reflection complexity*, arXiv:2610.14637 (2026), https://arxiv.org/abs/2610.14637.
