# Parity transition in wheel acyclic-orientation Fourier recovery

## Finding

Let \(n\ge3\), and let \(G_n=K_1\vee C_n\) be the wheel with hub \(h\), labelled rim vertices \(v_0,\dots,v_{n-1}\), and rim indices modulo \(n\). Encode each orientation by \(x=(s,r)\in\mathbb F_2^{2n}\): the spoke coordinate \(s_i=0\) denotes \(h\to v_i\), and \(s_i=1\) denotes \(v_i\to h\); the rim coordinate \(r_i=0\) denotes \(v_i\to v_{i+1}\), while \(r_i=1\) denotes the reverse direction. Let \(f_n(x)=1\) for an acyclic orientation, \(0\) otherwise. For character frequencies \(a,b\in\mathbb F_2^n\), use the **unnormalized** transform

\[
\widehat f_n(a,b)=\sum_{s,r\in\mathbb F_2^n}f_n(s,r)(-1)^{\sum_i(a_i s_i+b_i r_i)}.
\]

Set \(D_0=I_2\), \(D_1=\operatorname{diag}(1,-1)\), and

\[
L_0=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad L_1=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

**Theorem (all coefficients and parity transition).** Every coefficient has an \(O(n)\)-step exact evaluation in the unit-cost integer-arithmetic model (with intermediate integers of \(O(n)\) bits)

\[
\boxed{\widehat f_n(a,b)=\operatorname{tr}\left(\prod_{i=0}^{n-1}D_{a_i}L_{b_i}\right)-\left(1+(-1)^{\sum_i a_i}\right)\left(1+(-1)^{\sum_i b_i}\right).}
\]

Convolution \(T_n:g\mapsto f_n*g\) on \(\mathbb C^{\mathbb F_2^{2n}}\) has the following sharp parity behaviour.

- For every **even** \(n\ge4\), \(\widehat f_n(a,b)\) is nonzero **if and only if** \(\sum_i(a_i+b_i)\) is even. Thus
  \[\boxed{\operatorname{rank}T_n=2^{2n-1},\qquad \min_{\widehat f_n\ne0}|\widehat f_n|=2,\qquad \kappa_2(T_n|_{\mathrm{ran}T_n})=\frac{3^n-3}{2}.}\]
  The range is exactly the functions invariant under the global reversal translation \(x\mapsto x+\mathbf1\); the averaging projection \(g(x)\mapsto(g(x)+g(x+\mathbf1))/2\) has optimal \(\ell^1\) and \(\ell^\infty\) operator norms equal to one.
- For every **odd** \(n\ge3\), in addition to all odd-weight zero coefficients, each frequency having \(b_i=1\) for every rim coordinate and \(\sum_i a_i\) odd is zero. These are \(2^{n-1}\) **distinct even-weight frequencies**, yielding
  \[\boxed{\operatorname{rank}T_n\le2^{2n-1}-2^{n-1}.}\]

The total number \(3^n-3\) of acyclic wheel orientations is a known prerequisite, not a newly claimed enumeration. No exact rank for odd \(n\) is asserted.

## Assumptions and scope

The wheel is finite, simple and has a **fixed labelled hub** and cyclically labelled rim; \(n=3\) gives the complete graph on four vertices. A directed cycle is any consistently oriented simple cycle. The group for convolution is the full Boolean edge-orientation cube \(\mathbb F_2^{2n}\), and every Fourier coefficient is unnormalized. The stated condition ratio takes the largest divided by the smallest *positive* singular value of convolution (equivalently, restriction to its range), not a condition number for the singular full operator. The conclusion concerns arbitrary complex-valued functions on the orientation cube.

## Proof

**1. Local acyclicity criterion.** If consecutive spoke bits are \(s_i=0,s_{i+1}=1\), then \(r_i=0\) would form a directed triangle \(h\to v_i\to v_{i+1}\to h\); therefore \(r_i=1\). If the spoke bits are \(1,0\), the required rim direction is \(r_i=0\). If the spoke bits agree, either rim direction is locally possible. When both spoke values occur, these local triangle exclusions are sufficient: the fixed edges at every transition point from a spoke-\(1\) run into a spoke-\(0\) run point from \(1\) to \(0\), so neither a directed full rim cycle nor any longer hub-containing directed cycle is possible. When all spokes are equal, every rim edge is free, but the two coherently directed rim cycles must be removed. This spoke/rim criterion is already implicit in the wheel treatment of Savage–Squire–West (1993) and is not itself claimed as new.

**2. Signed transfer matrix.** The signed sum over the admissible direction(s) of rim edge \(i\), conditional on the consecutive spoke bits \(u,v\), is

\[
L_{b_i}(u,v)=\begin{cases}2,&b_i=0,\ u=v,\\0,&b_i=1,\ u=v,\\ (-1)^{b_i},&u=0,\ v=1,\\1,&u=1,\ v=0.\end{cases}
\]

This is precisely the displayed pair \(L_0,L_1\). Multiplying by \((-1)^{a_i u}\) at spoke \(i\) supplies \(D_{a_i}\). Summing over all cyclic spoke strings yields \(\operatorname{tr}\prod_iD_{a_i}L_{b_i}\). The four excluded configurations have both constant spokes and directed rim cycles. Their signed sum is

\[
\sum_{c,d\in\mathbb F_2}(-1)^{c\sum_i a_i+d\sum_i b_i}=(1+(-1)^{\sum_i a_i})(1+(-1)^{\sum_i b_i}).
\]

Subtracting proves the all-frequency formula. At frequency zero, \(L_0\) has eigenvalues three and one, so \(\widehat f_n(0,0)=\operatorname{tr}(L_0^n)-4=3^n-3\), as required.

**3. The reversal parity obstruction and even-wheel exactness.** Global reversal sends \((s,r)\) to \((s,r)+\mathbf1\) and preserves acyclicity. Hence \(\widehat f_n(a,b)=0\) whenever the total frequency weight is odd. When the weight is even, the summands in the Fourier transform coincide in pairs under reversal; each pair contributes \(2\) or \(-2\). Therefore

\[
\widehat f_n(a,b)\equiv|\mathcal A(G_n)|=3^n-3\pmod4.
\]

For even \(n\), \(3^n-3\equiv2\pmod4\), so **every even-weight coefficient is nonzero**. There are exactly \(2^{2n-1}\) such characters. To attain the least possible nonzero magnitude, take every rim frequency \(b_i=1\). Write \(J=L_1\), \(Z=D_1\); then \(J^2=-I\) and \((ZJ)^2=I\). If \(n\equiv0\pmod4\), choose all \(a_i=0\), giving \(\operatorname{tr}(J^n)=2\). If \(n\equiv2\pmod4\), choose \(a_0=a_1=1\) and the others zero, giving \(\operatorname{tr}((ZJ)^2J^{n-2})=2\). In both cases both frequency sums are even, so the excluded-cycle correction equals four. Consequently \(\widehat f_n(a,b)=-2\). No nonzero magnitude can be smaller by the congruence above; none can exceed \(\widehat f_n(0,0)=3^n-3\) by the triangle inequality. The exact rank and condition ratio follow. The Fourier support characterizes precisely the reversal-invariant functions; translation averaging is a norm-one projection onto this range, and every nonzero projection has norm at least one.

**4. Extra odd-wheel zeros.** Suppose \(n\) is odd, all \(b_i=1\), and \(\sum_i a_i\) is odd. Every \(D_{a_i}J\) is off-diagonal. The product of an odd number of such matrices remains off-diagonal, so its trace is zero. The correction term also vanishes because the spoke-frequency sum is odd. The total character weight is even, since \(n\) and \(\sum_i a_i\) are both odd. Thus these zeros are **additional** to those forced by reversal symmetry; there are exactly \(2^{n-1}\) choices of such spoke frequencies. Subtraction from the baseline possible \(2^{2n-1}\) nonzero frequencies gives the odd-rim rank upper bound.

## Verification

Two standalone Python 3 programs reproduce the formulas with integer arithmetic. `verify_wheel_direct.py` enumerates all \(4^n\) edge-orientation configurations, independently checks acyclicity by topological elimination, and applies a full unnormalized Walsh–Hadamard transform. `verify_wheel_transfer.py` instead multiplies two-by-two integer matrices for each frequency and verifies Parseval's identity, all even-rim nonvanishing congruences, the sharp magnitude-two witnesses, and the odd-rim witness family. Both were executed for every \(3\le n\le8\) and returned their success markers. Direct rank counts for \(n=3,4,5,6,7,8\) were \(16,128,346,2048,6252,32768\), respectively. A separate per-frequency comparison of both methods was performed for \(3\le n\le7\). All-length claims follow from the proof, not from finite computation.

## Relationship to prior work

Savage, Squire and West (1993) describe the exact admissible rim-orientation fibres of any spoke assignment on the wheel, and establish the known count \(3^n-3\). Those statements directly supply the combinatorial input to Step 1. Their paper studies Gray codes and Hamiltonicity of acyclic-orientation flip graphs, not the signed edge-orientation Walsh transform, and does not state the spectrum, sharp magnitude-two witness or the odd/even spectral transition. The even-rim nonvanishing is an elementary consequence of the known count combined with global reversal; it is not proposed as an independent deep theorem.

Gebhard and Sagan (arXiv:math/9907078v1, first public 1999-07-12) treat acyclic-orientation counts with specified sinks via chromatic and symmetric-function identities; these do not provide the individual signed edge-orientation frequencies. A later exact wheel-orientation flip-degree distribution gives a different statistic. The claimed addition is the complete explicit signed Fourier evaluation in a linear number of integer transfer steps per frequency and the sharp all-even spectral recovery versus explicit additional odd-rim blind characters. Searches and inspections cannot exclude unindexed equivalent calculations.

## Limitations

Only ordinary acyclic **edge orientations** of finite simple wheels are studied, with their specified Boolean edge-coordinate encoding. No result about the whole Fourier-rank sequence for odd rim lengths, larger joins, arbitrary graphs, noisy inverse recovery or a general graph-theoretic Fourier theorem is asserted. The exact small-size computations are checks, not proofs beyond their finite ranges. Historical priority is provisional despite inspected primary texts; the underlying local combinatorial representation is known. No independent mathematical audit has been performed.

## References

1. C. D. Savage, M. B. Squire and D. B. West, *Gray Code Results for Acyclic Orientations*, Congressus Numerantium 96 (1993), 185–204. Author-hosted full text: https://dwest.web.illinois.edu/pubs/aograph.pdf .
2. D. D. Gebhard and B. E. Sagan, *Sinks in Acyclic Orientations of Graphs*, arXiv:math/9907078v1, submitted 1999-07-12. https://arxiv.org/abs/math/9907078 .
3. *Degree distribution of the wheel acyclic-orientation flip graph*, publicly indexed mathematical record (2026-11-01), https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-degree-distribution-of-the-wheel-acyclic-orientation-flip-graph--00ad365d2ac5 .
