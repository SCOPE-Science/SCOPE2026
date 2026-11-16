# Cycle independent sets: a modulo-three Fourier invertibility law with sharp spectral gaps

## Finding

For an integer \(n\ge3\), let \(C_n\) be the simple cycle with cyclically ordered vertices \(0,1,\ldots,n-1\), and let \(A_n\subseteq\mathbb F_2^n\) consist of all incidence vectors of vertex-independent sets of \(C_n\), including the empty set. Define the unnormalized Walsh multiplier
\[
W_n(b)=\sum_{x\in A_n}(-1)^{\sum_{j=0}^{n-1}b_jx_j},\qquad b\in\mathbb F_2^n.
\]
Then \(W_n(b)\neq0\) for every \(b\) if and only if \(3\nmid n\). Moreover, the **smallest positive magnitude** of a Walsh multiplier is exactly
\[
\min_{b:W_n(b)\ne0}|W_n(b)|=
\begin{cases}1,&3\nmid n,\\2,&3\mid n.\end{cases}
\]
For \(3\mid n\), the Fourier kernel has at least
\[
3\cdot4^{\lfloor(n-3)/6\rfloor}
\]
distinct frequencies, and for \(3\nmid n\) it is empty.

Let \(T_n\) denote **unnormalized** convolution by \(\mathbf1_{A_n}\) on \(\ell^2(\mathbb F_2^n)\). Its maximum singular value is the Lucas number \(L_n=|A_n|\). Thus
\[
\|T_n^{-1}\|_{2\to2}=1,\quad\kappa_2(T_n)=L_n \qquad(3\nmid n),
\]
while
\[
\|T_n^\dagger\|_{2\to2}=\tfrac12,\quad
\kappa_2^+(T_n)=L_n/2 \qquad(3\mid n),
\]
where \(T_n^\dagger\) is the Moore–Penrose pseudoinverse, and \(\kappa_2^+\) is the ratio of the largest to the smallest **positive** singular value.

## Assumptions and scope

All statements hold for every integer \(n\ge3\). Independent sets include the empty set. Fourier and convolution are taken on the entire Boolean vertex-coordinate group, not on the independent-set subset itself. The Walsh transform is unnormalized, and convolution means \((T_n f)(x)=\sum_{y\in\mathbb F_2^n}\mathbf1_{A_n}(y)f(x+y)\). Spectral norms are on the corresponding full-dimensional complex \(\ell^2\) space, with either normalized or counting inner product, which give the same operator norms. The Lucas numbers satisfy \(L_1=1\), \(L_2=3\), and \(L_{n+2}=L_{n+1}+L_n\).

## Proof

**1. Signed hard-core transfer identity.** Given \(b\in\mathbb F_2^n\), put \(s_j=(-1)^{b_j}\). For \(s\in\{1,-1\}\), set
\[
M(s)=\begin{pmatrix}1&1\\s&0\end{pmatrix}.
\]
The entry of \(M(s_j)\) indexed by the two successive occupation states \(u,v\in\{0,1\}\) equals \(s_j^u\) if \(uv=0\), and vanishes otherwise. Consequently, expanding the trace over cyclic occupation states proves exactly
\[
W_n(b)=\operatorname{tr}\bigl(M(s_0)M(s_1)\cdots M(s_{n-1})\bigr).
\]
This identity is valid for arbitrary independent choices of the signs, and is not merely a uniform-activity specialization.

**2. Zero-free lengths by arithmetic parity.** Reducing signs modulo two gives \(W_n(b)\equiv |A_n|\pmod2\) for every \(b\). The total number of independent sets on a cycle is
\[
|A_n|=L_n=\operatorname{tr}\bigl(M(1)^n\bigr).
\]
The matrix \(M(1)\) is invertible modulo two and satisfies \(M(1)^3\equiv I\pmod2\); its traces at exponents \(1,2,3\) are respectively \(1,3,4\), of parities \(1,1,0\). Hence \(L_n\) is odd precisely when \(3\nmid n\). In these lengths every Walsh multiplier is odd and therefore nonzero. When \(3\mid n\), every multiplier is even.

**3. A zero in every multiple of three.** Write a sign word as a sequence of \(+\) and \(-\) representing \(1\) and \(-1\). Direct multiplication gives
\[
M(-1)^3=-I,\qquad
M(-1)M(-1)M(1)=
\begin{pmatrix}1&0\\-2&-1\end{pmatrix},
\]
whose trace is zero. For any \(n=3k\), choose the length-\(n\) sign word \(--+\) followed by \(k-1\) copies of \(---\). Its transfer product is \((-1)^{k-1}\) times the displayed trace-zero matrix; thus its Walsh multiplier vanishes. This proves the exact invertibility dichotomy.

**4. Exponentially many distinct zero frequencies.** The three cyclic rotations of the three-letter word \(--+\) yield three distinct trace-zero transfer products. Direct integer multiplication also shows that each of the four distinct six-letter words
\[
+--+--,\qquad -+--+-,\qquad --+--+,\qquad ------
\]
has transfer product exactly \(I\). If \(n=3+6j\), concatenate any of the three trace-zero words with any sequence of \(j\) of the four six-letter identity words. If \(n=6+6j\), insert \(---\) after the first three-letter trace-zero word and then concatenate \(j\) identity words. Each product remains trace-zero, and all \(3\cdot4^j\) displayed sign assignments are different. This establishes the claimed lower bound for every multiple of three.

**5. Sharp nonzero magnitude and convolution norms.** The matrix \(M(-1)\) has eigenvalues \(\exp(\pm i\pi/3)\). At the uniform all-negative frequency this gives
\[
W_n(1,\ldots,1)=\operatorname{tr}(M(-1)^n)=2\cos(n\pi/3).
\]
Its magnitude is \(1\) for \(3\nmid n\) and \(2\) for \(3\mid n\). Combined with the established oddness or evenness of all multipliers, this attains the smallest possible positive magnitude in each case. Every coefficient satisfies \(|W_n(b)|\le |A_n|=L_n\), and equality holds at \(b=0\). Finally, the Walsh characters form an orthogonal eigenbasis for \(T_n\) with eigenvalues \(W_n(b)\), so the asserted norms, condition numbers, and pseudoinverse statements follow.

## Verification

The included standalone Python checker computes each multiplier by two independent transfer-state algorithms and, for \(3\le n\le9\), by a third explicit independent-set enumeration. It exhaustively checks every \(2^n\) sign assignment for \(3\le n\le16\), checks the least positive magnitude and the zero/nonzero dichotomy, verifies the four identity-block multiplications exactly, and checks explicit witnesses through \(n=101\). The zero counts obtained for \(n=3,6,9,12,15\) are \(3,18,111,696,4413\), respectively; no zero occurs at any other tested length. Run `python3 checker.py` using Python 3 standard library only. All finite tests support, but are not needed to infer, the general theorem; the proof above establishes it for all lengths.

## Relationship to prior work

Scott and Sokal (2003, revised 2004), Section 3.2, Examples 3.2–3.3, develop cycle independence polynomials and the uniform-activity transfer trace, including the uniform negative-fugacity evaluation used in Step 5. The multivariate independent-set partition function is also classical. The claim here is distinct: it quantifies over **every nonuniform Boolean Walsh frequency**, classifies full-group convolution invertibility, determines sharp positive spectral gaps, and constructs exponentially many singular frequencies. Those conclusions do not follow from the cited uniform-activity formula alone. Adamaszek (2011) studies homotopy of independence complexes of cycle powers, including the periodic homotopy type of ordinary cycle independence complexes; these topological statements do not determine arbitrary sign-weighted Fourier multipliers. Related Fourier restriction results for graph-independent coordinate supports concern principal sampling matrices, not the full-group convolution operator studied here. This is a bounded historical comparison, not a proof that no earlier equivalent result exists.

## Limitations

The theorem does not determine the exact number of vanishing frequencies at divisible-by-three lengths, the distribution of all nonzero multipliers, or endpoint \(\ell^1\)/\(\ell^\infty\) pseudoinverse norms. The exponentially large nullspace lower bound is not asserted to be sharp. The results do not apply automatically to non-cycle graphs or nonbinary characters. Independent mathematical validation and exhaustive historical-priority verification have not been performed.

## References

1. A. D. Scott and A. D. Sokal, *The Repulsive Lattice Gas, the Independent-Set Polynomial, and the Lovász Local Lemma*, arXiv:cond-mat/0309352, first public version September 15, 2003; especially Section 3.2, Examples 3.2–3.3 and the multivariate partition function.
2. M. Adamaszek, *Splittings of Independence Complexes and the Powers of Cycles*, arXiv:1106.6250, first public version June 30, 2011; especially Sections 1 and 3, on the cycle independence-complex recurrence.
