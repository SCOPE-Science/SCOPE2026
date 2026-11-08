# Sharp Abelian-complexity envelope for ternary digit-two parity

## Finding

Let \(\tau(0)=001\) and \(\tau(1)=110\). Its infinite fixed point beginning in \(0\) is \(x=\tau^\omega(0)\). Write \(\rho_x(n)\) for the number of distinct Parikh vectors among all contiguous length-\(n\) factors of \(x\). For every integer \(k\ge0\),

\[
\rho_x(3^k)=2k+2,
\qquad
\max_{1\le n\le3^k}\rho_x(n)=2k+2.
\]

Consequently, for every integer \(n\ge1\),

\[
\rho_x(n)\le2\lceil\log_3 n\rceil+2,
\qquad
\limsup_{n\to\infty}\frac{\rho_x(n)}{\log_3 n}=2.
\]

In digit terms, \(x_i\) is the parity of the number of digits equal to \(2\) in the base-three expansion of the nonnegative integer \(i\).

## Assumptions and scope

The alphabet is \(\{0,1\}\). A factor is a **contiguous** subword of the one-sided infinite fixed point, not a scattered subsequence. Its Parikh vector records the counts of zeros and ones, so the two counts determine one another at fixed length. All logarithms in the asserted asymptotic coefficient have base \(3\). The morphism is prolonged at \(0\), so its fixed point exists. There is no restriction to a finite prefix in the theorem.

## Proof

**1. The supertile prefix extrema.** Put \(U_k=\tau^k(0)\), of length \(L=3^k\). Give every zero signed weight \(+1\) and every one weight \(-1\); write \(W_k\) for the resulting signed sequence. Because the two images are complements,

\[
W_{k+1}=W_k\,W_k\,(-W_k).
\]

The total signed weight of each \(W_k\) is \(1\): this is true for \(W_0=(+1)\), and the displayed concatenation preserves total weight \(1\). Define inclusive-prefix endpoints

\[
P_k(j)=\sum_{i=0}^{j-1}W_k(i)\quad(0\le j\le L),
\qquad M_k=\max_{0\le j\le L}P_k(j),\qquad
m_k=\min_{0\le j\le L}P_k(j).
\]

The prefix sums of \(W_{k+1}\), on its three consecutive supertiles, take the forms \(P_k(j)\), \(1+P_k(j)\), and \(2-P_k(j)\). Thus

\[
M_{k+1}=\max\{1+M_k,2-m_k\},\qquad
m_{k+1}=\min\{m_k,2-M_k\}.
\]

Starting at \((M_0,m_0)=(1,0)\), induction gives, for **all** \(k\ge0\),

\[
M_k=k+1,\qquad m_k=\min\{0,2-k\}.
\]

In particular the extrema arise from an exact infinite recurrence, not extrapolation of finite computations.

**2. All factors through the geometric scale.** The fixed point satisfies \(x=\tau^k(x)\). Therefore it decomposes into aligned blocks of length \(L=3^k\), each with signed contents either \(W_k\) or \(-W_k\). Every factor of any length \(n\le L\) lies in one such block or crosses one boundary between two adjacent blocks.

A factor within one block has signed sum of absolute value at most \(M_k-m_k\). A factor crossing a boundary starts at offset \(a\) of the first supertile and ends at offset \(b\) of the second, with \(0\le b\le a\le L\). If the two aligned blocks have the same sign, its signed sum has absolute value

\[
|1-P_k(a)+P_k(b)|\le1+M_k-m_k.
\]

If the signs are opposite, its signed sum has absolute value at most

\[
|1-P_k(a)-P_k(b)|
\le \max\{|1-2m_k|,|1-2M_k|\}.
\]

For \(k\ge1\), substitution of the exact prefix extrema shows that all three bounds do not exceed \(2k+1\). For \(k=0\), only \(n=1\) is possible and the same bound is immediate. Hence every factor of length \(n\le3^k\) has signed sum in the integer interval \([-2k-1,2k+1]\).

A signed sum \(S\) for a length-\(n\) binary factor corresponds to exactly \((n-S)/2\) ones, and \(S\equiv n\pmod2\). The indicated interval contains at most \(2k+2\) integers of any fixed parity, giving

\[
\rho_x(n)\le2k+2\qquad(1\le n\le3^k).
\]

**3. Both extremal Parikh counts at the scale.** The length-two factor \(01\) occurs in \(x\), so the block pair \(U_k\tau^k(1)=U_k\overline{U_k}\) occurs in \(x\). Select \(a\in[0,L]\) with \(P_k(a)=M_k=k+1\). The length-\(L\) factor using the last \(L-a\) symbols of the first supertile and first \(a\) symbols of the second has signed sum

\[
(1-P_k(a))-P_k(a)=1-2(k+1)=-(2k+1).
\]

An endpoint choice \(a=L\) merely gives the whole second supertile, so is allowed. The factor language of \(x\) is closed under exchanging zeros and ones: if a factor occurs in \(\tau^j(0)\), its complement occurs in \(\tau^j(1)\), which occurs in \(\tau^j(x)=x\) because \(1\) occurs in \(x\). Thus signed sum \(+(2k+1)\) also occurs among length-\(L\) factors.

As a length-\(L\) window slides one position, its number of ones changes by at most one. A finite chain of such windows between two occurrences of the opposite extreme counts consequently realizes every intervening integer count. The two extremes differ by \(2k+1\) in the number of ones, giving exactly \(2k+2\) distinct Parikh vectors. With Step 2 this proves both displayed geometric-scale identities.

**4. Asymptotic coefficient.** For any \(n\ge1\), take \(k=\lceil\log_3 n\rceil\) in Step 2. This proves the global upper envelope. The subsequence \(n=3^k\) has \(\rho_x(n)=2k+2\); upper and lower bounds together give the stated limsup coefficient.

Finally, reading the substitution in ternary positions gives \(x_{3i}=x_i\), \(x_{3i+1}=x_i\), and \(x_{3i+2}=1-x_i\), establishing the digit-parity description by induction on the number of base-three digits.

## Verification

The accompanying standalone `verify.py` independently constructs the morphic fixed-point prefix and the ternary digit-parity sequence, checks that they agree at all \(3^{11}\) inspected indices, and verifies the supertile prefix-extrema equations through \(k=8\). Using sliding sums in the prefix, it observes the asserted endpoint values and exact Parikh-type counts for \(0\le k\le7\), and the proposed upper inequality for all \(1\le n\le300\). The script terminates with `VERIFY_OK` on success. These are finite consistency checks; the four proof steps above establish the infinite statement.

## Relationship to prior work

Allouche, Rampersad, Rigo, Shallit, and Stipulanti (2026), *An example of an automatic sequence with non-regular abelian complexity*, study a different alphabet and parameter in the morphism family \(a\mapsto a^r(a+1)\) and explicitly propose studying other parameters in their Remark 4. The present binary map is the \(r=2\), two-letter case, not their three-letter \(r=3\) construction.

Blanchet-Sadri, Fox, and Rampersad's earlier classification gives an \(O(\log n)\) bound for uniform binary morphisms in the appropriate positive-excess case and discusses the lower-growth question, but does not give this exact two-unit coefficient and sharp value at every power of three. Here the morphism length is \(3\), the image zero-count difference is \(1\), and the length-three maximum is \(3\) (since \(000\) occurs), giving positive excess \(3-2=1\).

Blanchet-Sadri, Seita, and Wise (2016) study general algorithmic computation of Abelian complexity for binary uniform morphic words. A paper-specific identical evaluation could not be excluded from inaccessible full text. No claim is made that the general computability or asymptotic upper bound is new.

## Limitations

The exact identity is for the special lengths \(3^k\), and the accompanying upper envelope is for all lengths; no closed formula for \(\rho_x(n)\) at arbitrary \(n\) is asserted. The result concerns precisely the indicated binary substitution, not all morphisms of the 2026 family. Originality is assessed against accessible mathematical literature and indexed results and remains subject to an independent historical-priority check. No independent scientific audit has been performed.

## References

1. J.-P. Allouche, N. Rampersad, M. Rigo, J. Shallit, and M. Stipulanti, *An example of an automatic sequence with non-regular abelian complexity*, arXiv:2610.03837, first posted 2026-10-02, https://arxiv.org/abs/2610.03837 (particularly Remark 4).
2. F. Blanchet-Sadri, N. Fox, and N. Rampersad, *On the asymptotic abelian complexity of morphic words*, Advances in Applied Mathematics 61 (2014), 46–84, https://doi.org/10.1016/j.aam.2014.08.005; accessible related 2013 lecture material https://sites.math.rutgers.edu/~nhf12/research/DLT2013-AbelianAsymptoticComplexities.pdf.
3. F. Blanchet-Sadri, D. Seita, and D. Wise, *Computing abelian complexity of binary uniform morphic words*, Theoretical Computer Science 640 (2016), 41–51, https://doi.org/10.1016/j.tcs.2016.05.046.
4. M. A. Whiteland, *Asymptotic Abelian Complexities of Certain Morphic Binary Words*, Journal of Automata, Languages and Combinatorics 24 (2019), 89–114, https://www.utupub.fi/bitstream/10024/172354/1/final_version_for_personal_use.pdf.
