# Exact dyadic Walsh valuations for equivalence-relation supports

## Finding
Let \(n\ge2\), let \(E_n=\binom{[n]}2\), and let \(P_n\subseteq\mathbb F_2^{E_n}\) be the indicator vectors of the equivalence relations on \([n]\): the coordinate indexed by \(\{i,j\}\) equals one when \(i\) and \(j\) belong to the same block of the corresponding set partition. For a frequency graph \(H\subseteq E_n\), write \(m=|H|\) and set
\[
W_n(H)=\sum_{x\in P_n}(-1)^{\sum_{e\in H}x_e}.
\]
Write \(B_j\) for the \(j\)-th Bell number. Uniformly in the shape of \(H\),
\[
\boxed{W_n(H)\equiv B_n-2mB_{n-1}+4\binom m2B_{n-2}\pmod8.}
\]
Furthermore, the following complete first dyadic classification holds, with \(\nu_2(z)\) the exponent of two dividing a nonzero integer \(z\):

| \(n\bmod12\) | Frequency graph \(H\) | Assertion |
|---|---|---|
| \(0,1,3,4,6,7,9,10\) | all \(H\) | \(W_n(H)\) is odd; \(\nu_2(W_n(H))=0\). |
| \(5,8\) | \(m\) even | \(\nu_2(W_n(H))=2\). |
| \(5,8\) | \(m\) odd | \(\nu_2(W_n(H))=1\). |
| \(11\) | \(m\) even | \(\nu_2(W_n(H))=1\). |
| \(11\) | \(m\) odd | \(\nu_2(W_n(H))=2\). |
| \(2\) | \(m\) even | \(\nu_2(W_n(H))=1\). |
| \(2\) | \(m\) odd | \(W_n(H)\equiv0\pmod8\); no nonvanishing claim. |

Thus, for every \(n\ge3\) satisfying \(n\not\equiv2\pmod{12}\), convolution by the indicator of \(P_n\) on \(\ell^2(\mathbb F_2^{E_n})\) is invertible. For \(n\equiv2\pmod{12}\), at least half the Fourier multipliers are nonzero, so its rank is at least \(2^{\binom n2-1}\). The exceptional case \(n=2\) has rank one. In each nonexceptional even-Bell residue class \(5,8,11\pmod{12}\), the inverse convolution norm is at most \(1/2\) in \(\ell^2\); no optimality of this bound for every \(n\) is asserted.

## Assumptions and scope
The Boolean vector space has one coordinate per **unordered pair** of distinct vertices, and the transform is unnormalized. Set partitions are unordered collections of nonempty blocks, and each partition determines a unique equivalence-relation incidence vector. The edge set \(H\) is an arbitrary simple graph on the fixed labelled vertex set \([n]\), including isolated vertices. The graph's number of edges is \(m\). The dyadic valuations are asserted exactly only where the displayed congruence rules out zero. No signed or weighted partitions are introduced beyond the Walsh character itself.

## Proof
**Exact character expansion.** For a partition \(\pi\) let \(I_e(\pi)\) be one when the endpoints of edge \(e\) share a block, and zero otherwise. The character is
\[
(-1)^{\sum_{e\in H}I_e(\pi)}=\prod_{e\in H}(1-2I_e(\pi)).
\]
Expanding and interchanging finite sums yields the stronger identity
\[
\boxed{W_n(H)=\sum_{F\subseteq H}(-2)^{|F|}B_{c(F)},}
\]
where \(c(F)\) counts connected components of the spanning graph \(([n],F)\), isolated vertices included. Indeed, requiring \(I_e(\pi)=1\) for all \(e\in F\) identifies all vertices in each component of \(F\); the resulting partition choices are exactly the \(B_{c(F)}\) partitions of those components. When \(|F|=0,1,2\), the component counts are respectively \(n,n-1,n-2\), since any two distinct simple edges are independent identifications. All terms with \(|F|\ge3\) are divisible by eight, proving the displayed universal congruence.

**Bell numbers modulo eight, proved without a period assumption.** Let \(S(n,k)\) be Stirling numbers of the second kind, with \(S(0,0)=1\), and put
\[
a_r(n)=\sum_{\substack{k\ge0\\ k\equiv r\ (\mathrm{mod}\ 8)}}S(n,k)\pmod8,\qquad 0\le r<8.
\]
The recurrence \(S(n+1,k)=kS(n,k)+S(n,k-1)\) gives a linear operator \(M\) on \((\mathbb Z/8\mathbb Z)^8\), defined by \((Mv)_r=rv_r+v_{r-1}\) with subscripts modulo eight. If \(e_0=(1,0,\ldots,0)\), then \(a(n)=M^ne_0\) and \(B_n\equiv\sum_ra_r(n)\pmod8\). Finite modular matrix multiplication gives
\[
M^{24}e_0-e_0=4(e_0+e_4)\pmod8.
\]
The six successive iterates of \(e_0+e_4\) modulo two have supports \(\{0,4\}\), \(\{1,5\}\), \(\{1,2,5,6\}\), \(\{1,2,3,5,6,7\}\), \(\{0,1,2,4,5,6\}\), \(\{2,3,6,7\}\); the next iterate returns to \(\{0,4\}\). Every support has even cardinality. Hence for every \(n\ge0\),
\[
B_{n+24}-B_n\equiv\sum_r\bigl(M^n4(e_0+e_4)\bigr)_r=0\pmod8.
\]
The 24 initial residues, calculated from the Stirling recurrence, are
\[
(1,1,2,5,7,4,3,5,4,3,7,2,5,5,2,1,3,4,7,1,4,7,3,2).
\]
These are also the historically known residues of the Bell sequence modulo eight; the argument above supplies a complete independent finite-state proof of their period.

**Dyadic classification.** For \(n\not\equiv2\pmod3\), the table gives odd \(B_n\), and \(W_n(H)\equiv B_n\pmod2\), hence \(\nu_2(W_n(H))=0\). In the eight remaining residue classes modulo 24, substitute the three Bell residues into the universal formula. In the order \((m\text{ even},m\text{ odd})\), the resulting \(W_n(H)\bmod8\) pairs are
\[
\begin{array}{c|cccccccc}
n\bmod24&2&5&8&11&14&17&20&23\\\hline
(W_{\rm even},W_{\rm odd})&(2,0)&(4,6)&(4,2)&(2,4)&(2,0)&(4,6)&(4,2)&(2,4).
\end{array}
\]
For the even-frequency entries this calculation uses only \(m\bmod2\): the \(4\binom m2B_{n-2}\) term compensates for the change from \(m\) to \(m+2\) modulo eight. All nonzero residues immediately give the exact valuations stated. Fourier diagonalization of convolution on a finite Boolean group identifies the rank with the number of nonzero multipliers. The Fourier multipliers with even \(m\) form exactly half of all \(2^{\binom n2}\) characters when \(n\ge2\); this proves the rank bound in the exceptional class. For invertible convolution, its \(\ell^2\) inverse norm is the reciprocal of the least absolute multiplier, giving the claimed upper bound.

## Verification
Run `python verify_equivalence_walsh.py` with Python 3.9 or newer. The checker verifies the eight-state matrix identity and the 24 Bell residues, checks the modular class table for 70 representative indices, independently enumerates all set partitions for \(2\le n\le7\) and runs exact-integer Walsh butterflies on all \(2^{\binom n2}\) frequencies (2,131,018 coefficients in total), and compares 1,026 additional eight-vertex signed partition sums computed by an unrelated first-block recurrence. These computations are finite corroboration; the arbitrary-\(n\) theorem rests on the combinatorial and modular-matrix proof above.

## Relationship to prior work
Duncan and Peele (2009) and Hertz and Mélot (2014 preprint, 2016 journal) develop **unsigned** graphical Bell numbers and deletion–contraction, rather than signed character sums of the entire equivalence-relation support. Lunnon, Pleasants and Stephens (1979) established Bell-number congruences; Bell-number residues and the period itself are prior knowledge, not a novel part of this finding. The new assertion is the shape-independent Walsh congruence together with its all-frequency dyadic valuations and full-rank classification across 11 of the 12 congruence classes. The inclusion–exclusion method is elementary, so an equivalent earlier signed graph-partition specialization remains a residual priority risk.

## Limitations
This theorem does **not** prove nonvanishing at odd-edge frequencies for \(n\equiv2\pmod{12}\); the case \(n=2\) actually has a vanishing multiplier. It does not determine arbitrary integer Walsh coefficients or the optimal inverse norm for all dimensions, nor does it assert a necessary-and-sufficient condition for invertibility in the unresolved class. The original 1979 congruence paper's full text was not accessible during the comparison, but its historical result was independently reconstructed for the modulus used here. Independent mathematical audit has not been performed.

## References
1. B. Duncan and R. Peele, *Bell and Stirling Numbers for Graphs*, Journal of Integer Sequences **12** (2009), Article 09.7.1, first published 13 October 2009. https://cs.uwaterloo.ca/journals/JIS/VOL12/Peele/peele5.pdf
2. A. Hertz and H. Mélot, *Counting the number of non-equivalent vertex colorings of a graph*, institutional full text available since 3 February 2014; Discrete Applied Mathematics **203** (2016), 62–71. https://orbi.umons.ac.be/handle/20.500.12907/10001
3. W. F. Lunnon, P. A. B. Pleasants, and N. M. Stephens, *Arithmetic properties of Bell numbers to a composite modulus I*, Acta Arithmetica **35** (1979), 1–16, DOI: 10.4064/aa-35-1-1-16. https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/35/11/102216/arithmetic-properties-of-bell-numbers-to-a-composite-modulus-i
