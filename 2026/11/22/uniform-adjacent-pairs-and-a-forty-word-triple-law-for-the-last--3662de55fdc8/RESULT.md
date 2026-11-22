# Uniform adjacent pairs and a forty-word triple law for the last nonzero decimal digits of factorials

## Finding

Let \(d_n\) be the last nonzero decimal digit of \(n!\) for \(n\ge2\). Introduce \(e_n\in\mathbb Z/4\mathbb Z\) by assigning exponents \(0,1,2,3\) to digits \(6,2,4,8\), respectively. For every \(x,y,z\in\mathbb Z/4\mathbb Z\), the limiting relative frequency of the ordered triple \((e_n,e_{n+1},e_{n+2})=(x,y,z)\) is

\[
\pi(x,y,z)=\frac{\mathbf{1}_{y=x,z=x+1}+\mathbf{1}_{y=x+1,z=x}+\mathbf{1}_{y=x-1,z=x+1}}{20}+\frac{\mathbf{1}_{y=x+2}+\mathbf{1}_{z=y}}{80}.
\]

Every equality is modulo four. Exactly \(40\) of the \(64\) possible triples occur (already for some sufficiently large \(n\)); the remaining \(24\) are prohibited for \(n\ge10\). Precisely \(12\) triples have frequency \(1/20\), four have \(1/40\), and \(24\) have \(1/80\). Every ordered adjacent pair has frequency \(1/16\). Thus adjacent digits are independent and uniform despite a highly restricted, nonuniform triple distribution. For example, \(\mathbb P(e_n=e_{n+1}=e_{n+2})=1/20\), rather than the independent-digit value \(1/16\).

For all these pair and triple statistics, the number of occurrences for indices \(2\le n<N\) equals the stated density times \(N\), plus \(O(N^{1-\delta})\), with the positive explicit exponent

\[\delta=\frac{\log(625/369)}{4\log 5}.\]

## Assumptions and scope

Here \(d_n\) is the final nonzero **single decimal digit** of the integer factorial, not a multi-digit suffix within one factorial. The statements concern ordinary natural density in consecutive index order; no averaging over factorial sizes or arbitrary progressions is assumed. The index \(n\) is at least two, with boundary conventions below used only in the proof of the digit recurrence. All exact prohibitions are asserted for \(n\ge10\); the finite initial portion is not claimed to share the same support restriction.

## Proof

**1. Exact factorial recurrence.** The standard block-of-five factorial decomposition gives, for integers \(q\ge1\), \(0\le r<5\),

\[d_{5q+r}\equiv d_q\,d_r\,2^q\pmod {10},\qquad(d_0,d_1,d_2,d_3,d_4)=(1,1,2,6,4).\]

This identity follows by grouping the integers into five-term blocks, removing matched factors of five and two, and observing that the remaining residues of a complete block contribute the displayed power of two after the smaller factorial has been extracted. It can alternatively be verified as the standard last-nonzero-factorial-digit recursion. In the multiplicative group of even final digits modulo ten, \(6\) acts as identity, and repeated multiplication by \(2\) cycles \(6,2,4,8\). Write \(\gamma=(0,0,1,0,2)\) for the exponents of \((d_0,\ldots,d_4)\); the values \(d_0=d_1=1\) act as identity on even residues. Consequently, for \(q\ge2\),

\[ e_{5q+r}=e_q+(q\bmod4)+\gamma_r\pmod4.\]

This also holds with the auxiliary exponent \(e_1:=0\) for \(q=1\), since multiplication by one and by six is identical on the relevant even residues; the actual \(d_1=1\) is not redefined.

**2. Finite state and a positivity certificate.** For \(q\ge2\), define

\[s(q)=(e_q,e_{q+1},q\bmod4)=(a,b,t)\in(\mathbb Z/4\mathbb Z)^3.\]

For the auxiliary starting index one, set \(s(1)=(0,1,1)\), which is consistent with the preceding convention. Under the child index \(5q+r\), the update \(s(q)\mapsto s(5q+r)\) is exactly

\[
T_r(a,b,t)=\begin{cases}
(a+t+\gamma_r,a+t+\gamma_{r+1},t+r),&0\le r\le3,\\
(a+t+2,b+t+1,t),&r=4,
\end{cases}
\]

with every coordinate modulo four. Let \(M\) be the \(64\)-square integer matrix counting these five transitions from each state. Direct finite enumeration using `verify.py` checks two exact universal identities: every state has precisely five incoming edges, and **every entry of \(M^4\) lies between 4 and 16 inclusive**. The program enumerates each of the \(5^4\) labeled paths from each of the \(64\) starting states, and independently verifies every target count, so this is a finite, exhaustive certificate rather than a sampling assertion. Row and column sums are five. It follows that \(P=M/5\) has the uniform stationary distribution on all \(64\) states. By strict positivity of \(P^4\) and the minorization \(P^4(s,t)\ge4/625\), every initial state distribution converges to uniform in total variation at rate at most

\[\left(1-64\cdot\frac4{625}\right)^{\lfloor L/4\rfloor}=\left(\frac{369}{625}\right)^{\lfloor L/4\rfloor}.\]

**3. From digit-tree mixing to natural density.** Every block \(5^L q\le n<5^L(q+1)\), for fixed \(q\ge1\), is obtained by appending \(L\) unrestricted base-five digits to the state at \(q\). Its empirical state law is \(P^L\) applied to this single starting state, so it differs from uniform by at most the displayed geometric rate. Decompose an arbitrary initial interval \(2\le n<N\) into at most four such full five-adic blocks at each length \(5^L\), plus bounded initial exceptions. Summing the errors \(5^L(369/625)^{\lfloor L/4\rfloor}\) over the decomposition yields \(O(N^{1-\delta})\) with the stated \(\delta\). The same reasoning applies to an observable determined by the state and the final base-five digit.

**4. Exact word law.** For a state \((a,b,t)\), its final-digit child index \(5q+r\) determines three adjacent exponents as follows:

\[
\begin{array}{c|c}
r&(e_{5q+r},e_{5q+r+1},e_{5q+r+2})\\\hline
0&(u,u,u+1)\\
1&(u,u+1,u)\\
2&(u,u-1,u+1)\\
3&(u,u+2,v)\\
4&(u,v,v)
\end{array}
\]

In each row, \(u\) is uniform modulo four when the state is uniform; in the last two rows, \(u,v\) are jointly independent uniform residues. Each row has limiting weight \(1/5\), by the child-digit proportions. The five rows therefore give exactly the displayed \(\pi\), as well as a uniform \(1/16\) distribution on consecutive pairs. An exact count of the sixty-four entries of the displayed expression gives \(12\) of weight \(1/20\), four of \(1/40\), \(24\) of \(1/80\), and \(24\) zeros. The finite-state table also shows that none of these zero-weight triples occurs once the block recursion applies, i.e. for \(n\ge10\). Because every state has positive stationary frequency, every permitted triple actually occurs infinitely often.

## Verification

Run `python3 verify.py` in the directory containing this document. The standard-library-only script exhausts the full 64-state five-letter transition graph and every 4-step path, verifies the triple formula and all 64 frequencies, tests the exact factorial recursion against independent full integer factorials through index 500, and checks 59,988 consecutive integer-factorial triples against the state-derived formula. It prints the exact minima/maxima and frequency counts. Finite checks do not replace the recurrence and mixing proof for arbitrarily large indices.

## Relationship to prior work

Lipka (2018) characterizes base-dependent automaticity of last-nonzero-factorial-digit sequences. Sobolewski (2018) constructs uniform morphisms and calculates frequencies of **multiple trailing positions within one factorial**; these are one-index marginals, not joint laws across the three factorials at indices \(n,n+1,n+2\). Dresden's article describes the familiar block structure of individual factorial digits. The present exact ordered three-index distribution, twenty-four forbidden words, and uniform adjacent-pair law are not stated by those inspected results. The standard factorial digit recurrence, not its discovery, is used here.

## Limitations

The result is restricted to decimal last nonzero digits and consecutive indices, rather than arbitrary bases or lags. The finite-state certificate in `verify.py` is computational, with all inputs and loops explicit; an independent proof of the matrix's four-step positivity could replace it. The literature comparison does not exclude unindexed equivalent results. The proof's asymptotic rate is a deliberately nonoptimal effective bound.

## References

- E. Lipka, *Automaticity of the Sequence of the Last Nonzero Digits of \(n!\) in a Fixed Base*, first public preprint 2018-06-07, arXiv:1806.02560v1, https://arxiv.org/abs/1806.02560 .
- B. Sobolewski, *On the Last Nonzero Digits of \(n!\) in a Given Base*, first public preprint 2018-09-18, arXiv:1809.06947v1, https://arxiv.org/abs/1809.06947 .
- G. P. Dresden, *Two Irrational Numbers That Give the Last Non-Zero Digits of \(n!\) and \(n^n\)*, arXiv:1904.10274v1, https://arxiv.org/abs/1904.10274 (revised presentation of earlier work).
