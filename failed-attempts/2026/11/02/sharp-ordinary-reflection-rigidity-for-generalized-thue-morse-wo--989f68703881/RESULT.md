# Sharp ordinary-reflection rigidity for generalized Thue–Morse words

## Finding

For integers \(b\ge2\) and \(m\ge3\), define the generalized Thue–Morse word \(\mathbf t_{b,m}=(t(j))_{j\ge0}\) by \(t(j)=s_b(j)\bmod m\), where \(s_b(j)\) is the sum of the base-\(b\) digits of \(j\). Let \(\mathcal L_n\) be its set of distinct contiguous factors of length \(n\). Let \(P(n)=|\mathcal L_n|\), and let \(R(n)\) count the equivalence classes of \(\mathcal L_n\) under ordinary reversal, where two factors are equivalent when equal or mutual reverses.

**Theorem (rigidity and exact short-length correction).** For every \(b\ge2\), \(m\ge3\), and \(n\ge3\),

\[
R(n)=P(n).
\]

Equivalently, whenever \(w\in\mathcal L_n\) and the *plain* reversal \(w^R\in\mathcal L_n\) for \(n\ge3\), then \(w=w^R\). In addition, with \(g=\gcd(m,b-1)\),

\[
R(0)=1,\quad R(1)=m,\quad
R(2)=\begin{cases}
\dfrac{m(m+1)}{2},&g=1,\\
\dfrac{m^2}{4},&g=2,\\
\dfrac{m^2}{g},&g\ge3.
\end{cases}
\]

Thus the entire ordinary-reflection profile is obtained from the known factor-complexity profile by a correction confined to length two. The binary modulus \(m=2\) is genuinely outside the rigidity theorem.

## Assumptions and scope

The base \(b\) and modulus \(m\) are arbitrary integers with \(b\ge2\), \(m\ge3\); no coprimality or aperiodicity hypothesis is imposed. All factors are factors of the **infinite**, zero-indexed, one-sided word, not only a finite substitution prefix. Letter arithmetic is in \(\mathbb Z/m\mathbb Z\). Reversal means reversing positions while **keeping each letter unchanged**, not reversing followed by a letter permutation or complement. The equality concerns ordinary reflection and distinct factors, not counting occurrences.

## Proof

**1. Carry increments.** For each \(j\ge0\), let \(h_j=\nu_b(j+1)\), the maximal exponent \(h\) with \(b^h\mid(j+1)\). Incrementing \(j\) to \(j+1\) removes exactly \(h_j\) trailing digits \(b-1\) and increments the preceding digit, so

\[
\Delta_j:=t(j+1)-t(j)\equiv1-(b-1)h_j\pmod m.\tag{1}
\]

If \(b\nmid(j+1)\), then \(h_j=0\) and \(\Delta_j=1\). Among two consecutive positive integers at least one is not divisible by \(b\), so **every two consecutive transitions contain a \(+1\) transition**.

**2. A reversible triple must be a palindrome.** Suppose \((x,y,z)\) and its reversed triple \((z,y,x)\) both occur. Write their first triple's two successive increments as \(d_1=y-x\) and \(d_2=z-y\). By step 1, one of \(d_1,d_2\) is \(+1\); likewise one of the reverse triple's increments \((-d_2,-d_1)\) is \(+1\), so one of \(d_1,d_2\) is \(-1\). Since \(m\ge3\), \(+1\ne-1\), and there are only two increments, their unordered pair is precisely \(\{+1,-1\}\). Hence \(d_1+d_2=0\) and \(x=z\).

**3. A three-step obstruction.** No three successive transitions of \(\mathbf t_{b,m}\) can include \(-1\) twice. For \(b\ge3\), a transition of value \(-1\) cannot have \(h_j=0\) by \(m\ge3\), hence its endpoint \(j+1\) must be divisible by \(b\). Among three consecutive integers at most one is divisible by \(b\). When \(b=2\), equation (1) gives \(\Delta_j\equiv1-h_j\pmod m\); the value \(-1\) implies \(h_j\equiv2\pmod m\), hence \(h_j\ge2\) and \(4\mid(j+1)\). Among three consecutive integers at most one is divisible by \(4\). This proves the obstruction uniformly.

**4. All longer reversal collisions are palindromic.** Let \(w=x_0x_1\cdots x_{n-1}\in\mathcal L_n\) with \(w^R\in\mathcal L_n\) and \(n\ge3\). Each length-three subfactor of \(w\) has its reversal in \(w^R\). Step 2 forces \(x_j=x_{j+2}\) for all \(0\le j\le n-3\), so \(w\) is two-periodic. Every two-periodic word of odd length is a palindrome. If \(n\) is even and \(w\) is nonpalindromic, then its first four letters are \(xyxy\), for distinct \(x,y\), and its reversed factor begins \(yxyx\). Put \(d=y-x\). The three transitions of \(xyxy\) are \((d,-d,d)\). Step 1 implies \(d=+1\) or \(d=-1\pmod m\). One of the two orientations \(xyxy\) or \(yxyx\) therefore has three transitions \((-1,+1,-1)\), contradicting step 3. Hence \(w\) is a palindrome in all cases, and no two distinct length-\(n\) factors coalesce under reversal for \(n\ge3\). This proves \(R(n)=P(n)\).

**5. All short factors and exact correction.** Every letter \(a\in\mathbb Z/m\mathbb Z\) occurs: choose a nonnegative integer with digit sum congruent to \(a\). By (1), every consecutive-pair increment belongs to the residue class \(1\pmod g\), with \(g=\gcd(m,b-1)\). Conversely, choose any \(a,d\in\mathbb Z/m\mathbb Z\) with \(d\equiv1\pmod g\). The linear congruence \((b-1)h\equiv1-d\pmod m\) has a nonnegative integer solution \(h\). Choose \(s\in\{0,\dots,m-1\}\) with \(s\equiv a-h(b-1)\pmod m\), and choose the base-\(b\) integer \(L=\sum_{r=0}^{s-1}b^r\) (with \(L=0\) when \(s=0\)). Set

\[
N=b^h(bL+1)-1.
\]

Its base-\(b\) expansion ends with \(h\) digits \(b-1\), preceded by zero; thus \(s_b(N)=s_b(L)+h(b-1)\), while \(s_b(N+1)=s_b(L)+1\). Consequently \((t(N),t(N+1))=(a,a+d)\). This proves the *exact* pair language:

\[
\mathcal L_2=\{(a,a+d):a\in\mathbb Z/m\mathbb Z,\ d\equiv1\pmod g\},\qquad |\mathcal L_2|=m^2/g.
\]

Its reversed pair also occurs exactly when \(-d\equiv1\pmod g\), equivalent to \(g\mid2\). When \(g=1\), every pair and its reverse occur; exactly \(m\) of the \(m^2\) pairs are fixed, giving \(m(m+1)/2\) classes. When \(g=2\), every permitted increment is odd, so none is zero; all \(m^2/2\) pairs are grouped in free reversal pairs, giving \(m^2/4\) classes. When \(g\ge3\), no pair has its reverse in the language, giving \(m^2/g\) classes. The empty word gives \(R(0)=1\) and all letters give \(R(1)=m\).

**6. Sharpness at alphabet size two.** In the classical binary Thue–Morse word \(\mathbf t_{2,2}\), both \(011\) and \(110\) occur, are distinct, and are mutual reverses. Therefore the universal statement for \(m\ge3\) cannot simply be extended to \(m=2\). \(\square\)

## Verification

The included `verify.py` enumerates all permissible length-two pairs and reconstructs explicit witnesses for \(2\le b\le10\), \(3\le m\le10\). It independently compares the first \(18{,}000\) digits from the digit-sum definition against the length-\(b\) morphism \(a\mapsto a(a+1)\cdots(a+b-1)\) for \(2\le b\le7\), \(3\le m\le8\), and checks ordinary-reversal collision absence at lengths \(3\) through \(12\). The standalone checker returned `VERIFY_OK 3477 finite assertions` when run as `python3 verify.py`. The proof above establishes all bases, moduli and factor lengths; these finite checks are consistency tests, not an infinite exhaustive proof.

## Relationship to prior work

Allouche, Campbell, Li, Shallit and Stipulanti introduced reflection complexity and, in Section 7 of their June 2024 preprint [1], explicitly asked for generalized Thue–Morse analogues. They already report equality for \(b=2,m=3\) and conjectural-looking numerical behavior for \(b=2,m>4\); that previously stated case is not claimed as new here. The result above proves the assertion for **all** \(b\ge2,m\ge3\), including the unaddressed \(m=4\) threshold and arbitrary bases, and gives the exceptional length-two correction.

Starosta [2] determined the factor complexity and the language symmetries under *letter-complementing* antimorphisms \(k\mapsto x-k\). Those are not the ordinary letter-preserving reversal for \(m\ge3\), so the factor-complexity formula and dihedral richness do not themselves supply the present collision exclusion. Allouche and Shallit [3] proved that ordinary palindromes of length at least four are absent for \(m\ge3\), but palindrome absence alone does not exclude the presence of two distinct mutually reversed factors. The relevant 2026 generalized-reflection study [4] uses other alphabet actions; its accessible discussion did not yield the present plain-reversal formula.

## Limitations

The equality \(R(n)=P(n)\) gives reflection complexity **in terms of** the previously known factor-complexity function; this note does not reprove or newly claim that earlier factor-complexity formula. The result is specific to integer digit sums modulo \(m\) and ordinary reversal. The existing base-two, modulus-three case is published prior work. Exhaustive searches cannot establish absolute uniqueness, and an unindexed equivalent formulation in the broader automatic-word literature remains possible. No external independent verification is asserted.

## References

[1] J.-P. Allouche, J. M. Campbell, S. Li, J. Shallit and M. Stipulanti, *The reflection complexity of sequences over finite alphabets*, arXiv:2406.09302 (first posted 2024-06-13), especially Section 7. https://arxiv.org/abs/2406.09302

[2] Š. Starosta, *Generalized Thue–Morse words and palindromic richness*, Kybernetika 48 (2012), 361–370; arXiv:1104.2476. https://dml.cz/dmlcz/142943

[3] J.-P. Allouche and J. Shallit, *Sums of Digits, Overlaps, and Palindromes*, Discrete Mathematics and Theoretical Computer Science 4 (2000), 1–10. https://dmtcs.episciences.org/en/articles/282/download

[4] *Generalized reflection complexity*, arXiv:2610.14637 (2026), cited for related, distinct group-action formulations. https://arxiv.org/abs/2610.14637
