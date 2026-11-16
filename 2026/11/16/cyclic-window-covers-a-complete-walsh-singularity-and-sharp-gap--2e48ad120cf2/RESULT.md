# Cyclic window covers: a complete Walsh singularity and sharp gap law

## Finding
For integers \(n,k\ge1\), let \(H_{n,k}\) be the family of binary words \(x=(x_0,\ldots,x_{n-1})\in\mathbb F_2^n\) for which every cyclic interval of \(k\) consecutive positions contains at least one \(1\). Read indices modulo \(n\), including repetitions when \(k>n\). Define the unnormalized Walsh transform
\[
W_{n,k}(b)=\sum_{x\in H_{n,k}}(-1)^{\sum_{i=0}^{n-1}b_i x_i},\qquad b\in\mathbb F_2^n.
\]
**Theorem.** The transform vanishes at some frequency if and only if \(k\) is even and \(k+1\) divides \(n\). Furthermore
\[
\min_{b:\ W_{n,k}(b)\ne0}|W_{n,k}(b)|
=\begin{cases}2,&2\mid k\text{ and }k+1\mid n,\\1,&\text{otherwise}.\end{cases}
\]
All Walsh coefficients are even precisely in the exceptional cases, and all are odd otherwise. These are exact all-frequency assertions, for every \(n,k\ge1\).

Let \(t_i=(-1)^{b_i}\). Two concrete evaluations determine the sharp bound: for the all-negative signing, \(t_i=-1\),
\[
W_{n,k}=\begin{cases}k,&k+1\mid n,\\-1,&k+1\nmid n;\end{cases}
\]
while if \(k+1\mid n\), assigning \(t_i=+1\) to the first \(j\) consecutive positions and \(-1\) to all others yields
\[
W_{n,k}=k-2j\qquad(0\le j\le k).
\]
Consequently counting-measure convolution by \(\mathbf1_{H_{n,k}}\) is invertible precisely outside the exceptional cases, with exact \(\ell^2\) inverse norm \(1\). Its Moore–Penrose pseudoinverse has exact \(\ell^2\) norm \(1/2\) at exceptional lengths.

## Assumptions and scope
Only the binary Boolean group and unnormalized counting-measure convolution are used. Every cyclic word is rooted/labeled: rotations are different unless the underlying strings agree at all labeled positions. A length-\(k\) cyclic interval follows the periodic extension of the word, so when \(k>n\) the admissible words are exactly the nonzero words. No hypothesis on relative sizes of \(n\) and \(k\) is required.

For the graph corollary, the incidence vectors of dominating vertex sets of the \(r\)-th power \(C_n^r\), for \(n\ge3\) and \(r\ge1\), are exactly \(H_{n,2r+1}\). All their Walsh coefficients are therefore odd. The convolution operator is invertible, and the exact inverse norm is \(1\), uniformly in \(n\) and \(r\).

## Proof
**Transfer representation.** Index states by \(0,1,\ldots,k-1\), recording the number of consecutive zeros immediately preceding a position. Let \(u=(1,\ldots,1)^{\mathsf T}\) and let \(e_j\) denote the coordinate column at index \(j\). For a sign \(t\in\{+1,-1\}\), define the integer matrix \(T(t)\) by
\[
T(t)_{s,0}=t\quad(0\le s<k),\qquad
T(t)_{s,s+1}=1\quad(0\le s<k-1),
\]
with all remaining entries zero. (For \(k=1\) only the first rule applies.) A closed state walk is uniquely determined by its periodic binary word containing a \(1\), and it exists exactly when the word avoids a cyclic run of \(k\) zeros. The all-zero word has no closed walk. Thus
\[
W_{n,k}(b)=\operatorname{tr}\big(T(t_0)T(t_1)\cdots T(t_{n-1})\big)
\]
for all positive \(n,k\), including \(k>n\).

**Finite-order negative transition.** Put \(B=T(-1)\) and \(A=T(+1)\). Direct multiplication gives
\[
Bu=-e_{k-1},\quad B^ju=-e_{k-j}\ (1\le j\le k),\quad B^{k+1}u=u.
\]
The vectors \(u,Bu,\ldots,B^{k-1}u\) are a basis; hence \(B^{k+1}=I\). Moreover \(B^ku=-\sum_{i=0}^{k-1}B^iu\), so its characteristic polynomial is \(1+z+\cdots+z^k\), whose distinct complex roots are the nontrivial \((k+1)\)-st roots of unity. It follows that
\[
\operatorname{tr}(B^n)=
\begin{cases}k,&k+1\mid n,\\-1,&k+1\nmid n.\end{cases}
\]

**Parity.** Since \(T(+1)\equiv T(-1)\pmod2\), the transfer representation gives \(W_{n,k}(b)\equiv\operatorname{tr}(B^n)\pmod2\) for every frequency. In particular, all coefficients are even exactly when \(k\) is even and \(k+1\mid n\); all are odd in every other case. In nonresonant cases the all-negative signing gives \(-1\), proving both invertibility and the sharp positive gap \(1\).

**Resonant signed-reflection identity.** Write \(N=k+1\). Since \(B^N=I\) and
\[
A=B+2u e_0^{\mathsf T},\qquad e_0^{\mathsf T}B^{-1}=-e_{k-1}^{\mathsf T},
\]
we have \(AB^{-1}=I-2u e_{k-1}^{\mathsf T}\). Set
\[
E_i=(B^iu)(e_{k-1}^{\mathsf T}B^{-i}),\qquad 0\le i<k.
\]
The displayed formula for \(B^ju\), its \(N\)-periodicity, and the cases of positive and negative differences give, for \(0\le i,h<k\),
\[
e_{k-1}^{\mathsf T}B^{h-i}u=\delta_{ih}-\delta_{h,i+1},
\]
where the second Kronecker term is zero when \(i+1\ge k\). Put \(u_i=B^iu\), a basis of the state space. The rank-one map \(E_i\) therefore sends \(u_i\) to itself, sends \(u_{i+1}\) to \(-u_i\) when \(i+1<k\), and kills every other basis vector. Thus the reflection \(I-2E_i\) has, in this basis, an upper triangular matrix with diagonal \(-1\) at index \(i\), diagonal \(+1\) elsewhere, and a possible entry \(+2\) in position \((i,i+1)\). The ordered identity
\[
A^jB^{-j}=\prod_{i=0}^{j-1}(I-2E_i)
\]
shows that the product is upper triangular with exactly \(j\) diagonal entries \(-1\) and \(k-j\) entries \(+1\). Consequently
\[
\operatorname{tr}(A^jB^{-j})=k-2j\qquad(0\le j\le k).
\]
When \(N\mid n\), the cyclic sign assignment with the first \(j\) signs positive has transfer trace \(\operatorname{tr}(A^jB^{n-j})=k-2j\). For odd \(k\), choose \(j=(k-1)/2\) and obtain \(1\); since every coefficient is odd, no zero exists. For even \(k\), choose \(j=k/2\) and obtain a zero, then \(j=k/2-1\) and obtain \(2\). All coefficients are even in that case, so the positive gap is exactly \(2\).

Finally, Walsh characters simultaneously diagonalize convolution on \(\mathbb F_2^n\), with eigenvalues \(W_{n,k}(b)\). Taking reciprocals of the smallest nonzero absolute eigenvalues proves the exact inverse and pseudoinverse norm assertions. This completes the proof.

## Verification
Run `python3 verify.py` from the directory containing the supplied standalone checker. It performs exact all-frequency Walsh enumeration for \(1\le n\le14\) and \(1\le k\le10\), as well as exact integer transfer-matrix identities for \(1\le k\le23\), three full resonant cycles, and off-resonance traces. The expected final marker is `CYCLIC_WINDOW_FOURIER_EXACT_PASS`. No floating-point arithmetic or external library is used. These finite checks corroborate but do not substitute for the all-parameter proof above.

## Relationship to prior work
Alikhani and Peng studied the enumerative domination polynomial of ordinary cycles and its three-term recurrence (2009). Bernini, Bilotta, Pinzani, and Vajnovszki studied generalized Fibonacci words avoiding long constant runs and their Gray codes (2013). These motivate the natural constrained-word family and its enumeration; the cited results do not supply an arbitrary-frequency cyclic Walsh singularity criterion or the resonant rank-one-reflection identity. The previously known ordinary-cycle independent-set Walsh result is the special case \(k=2\), and is not claimed as original. The new content is the uniform classification across every forbidden run length, including the odd-run zero-free regime and all even-run resonances, and the sharp spectral gaps.

## Limitations
The theorem does not count all vanishing frequencies in singular cases, nor determine any endpoint \(\ell^1\) inverse or projection norms. It concerns cyclic windows with a single forbidden all-zero factor and binary signs, not arbitrary forbidden patterns or nonbinary alphabets. Literature comparison is bounded; an earlier equivalent formula in signed transfer-matrix or restricted-word literature is a residual historical-priority possibility. Independent mathematical validation has not been performed.

## References
1. S. Alikhani and Y.-H. Peng, *Dominating Sets and Domination Polynomials of Cycles*, arXiv:0905.3268v1, first public 2009-05-20, https://arxiv.org/html/0905.3268v1.
2. A. Bernini, S. Bilotta, R. Pinzani, V. Vajnovszki, *A trace partitioned Gray code for q-ary generalized Fibonacci strings*, arXiv:1308.3619v1, first public 2013-08-16, https://arxiv.org/abs/1308.3619.
