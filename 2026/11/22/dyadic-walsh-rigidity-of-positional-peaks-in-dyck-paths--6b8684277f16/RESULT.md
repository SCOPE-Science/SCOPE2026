# Dyadic Walsh rigidity of positional peaks in Dyck paths

## Finding
For every integer \(n\ge1\), let \(\mathcal D_n\) be the Dyck paths of semilength \(n\), written as words of \(2n\) up- and down-steps. A **positional peak** is an adjacent pair of steps \(UD\), indexed by the position of its first step. For \(P\in\mathcal D_n\), let \(A(P)\subseteq[2n-1]\) be its set of positional peaks. Set
\[
K_n(x)=\#\{P\in\mathcal D_n:\mathbf1_{A(P)}=x\},\qquad x\in G_n=\mathbb F_2^{2n-1}.
\]
Let \(T_n\) be unnormalized counting convolution by \(K_n\) on real or complex functions on \(G_n\), and let \(W_n(S)=\sum_{P\in\mathcal D_n}(-1)^{|S\cap A(P)|}\) be its Walsh eigenvalue at \(S\subseteq[2n-1]\). Write \(C_m=\binom{2m}{m}/(m+1)\), \(s_2(a)\) for the number of ones in the base-two expansion of \(a\), and \(v_2(b)\) for the exponent of two in a nonzero integer \(b\).

**Theorem.** For every \(n\ge1\) and every frequency set \(S\),
\[
W_n(S)=\sum_{\substack{J\subseteq S\\\text{no two indices of }J\text{ consecutive}}}(-2)^{|J|}C_{n-|J|}.
\]
For every **odd** \(n\ge1\) and **every** \(S\subseteq[2n-1]\),
\[
\boxed{W_n(S)\equiv C_n\pmod{2^{s_2(n+1)}}},\qquad
\boxed{v_2(W_n(S))=s_2(n+1)-1=v_2(C_n).}
\]
For every **even** \(n\ge2\), the frequency \(S=[2n-1]\) satisfies \(W_n(S)=0\). Consequently \(T_n\) is invertible over \(\mathbb R\) or \(\mathbb C\) **if and only if \(n\) is odd**. For odd \(n\), all \(2^{2n-1}\) eigenvalues have the same exact two-adic valuation and
\[
v_2(\det T_n)=2^{2n-1}(s_2(n+1)-1).
\]
In particular, the inverse operator has \(\ell^2\)-norm at most \(2^{-(s_2(n+1)-1)}\). This bound is not asserted sharp in every order.

## Assumptions and scope
A Dyck path stays at nonnegative height, starts and ends at zero, and uses steps \(U=(1,1)\) and \(D=(1,-1)\). The binary coordinates record peak **step positions**, not peak heights, return positions, or up-step incidence. The group convolution is unnormalized: the kernel is a counting function and paths with the same peak profile contribute multiplicity. Every character is indexed by an arbitrary subset of the \(2n-1\) possible adjacent-step starts. The result holds for every such character, without restrictions on its support or on the heights of the path.

## Proof
**1. Exact simultaneous-peak contraction.** Fix \(J\subseteq[2n-1]\) and require a peak \(UD\) to start at each position in \(J\). Two consecutive start positions cannot both be peaks. If \(J\) has no consecutive indices, its specified two-step blocks are disjoint. Remove all these blocks, leaving a Dyck path of semilength \(n-|J|\). Conversely, given any such shorter Dyck path, insert the \(UD\) blocks into the positions prescribed by \(J\), from left to right. After accounting for earlier inserted blocks the positions are uniquely determined; two insertions at the same shortened gap retain the original ordering. Each inserted \(UD\) starts and ends at the current nonnegative height, so the reconstructed path is valid. This is a bijection, so the number of original paths satisfying all specified peaks is \(C_{n-|J|}\). The conclusion includes \(J=\varnothing\), which has \(C_n\) paths.

**2. Fourier expansion.** For any Dyck path and a set \(S\),
\[
(-1)^{|S\cap A(P)|}=\prod_{i\in S}\bigl(1-2\mathbf1_{\{i\in A(P)\}}\bigr).
\]
Expand the product, sum over all paths, and apply the simultaneous-contraction count. Terms with adjacent required peaks vanish. This proves the displayed exact formula for \(W_n(S)\). Equivalently, the coefficients of the independence polynomial of the subgraph induced by \(S\) in a \((2n-1)\)-vertex path determine the multiplier, with Catalan weights according to independent-set size.

**3. Binary valuation.** Legendre's formula gives the standard identity
\[
v_2(C_m)=s_2(m+1)-1\qquad(m\ge0).
\]
Indeed, \(v_2(\binom{2m}{m})=s_2(m)\), while adding one to \(m\) changes its binary digit sum by \(1-v_2(m+1)\). Put \(N=n+1\). The binary digit-sum inequality \(s_2(a+b)\le s_2(a)+s_2(b)\) implies, for every \(2\le k\le n\),
\[
s_2(N)\le s_2(N-k)+s_2(k)\le s_2(N-k)+k-1.
\]
If \(n\) is odd, then \(N\) is even; hence \(s_2(N)\le s_2(N-1)\), and the same strict inequality \(s_2(N)<1+s_2(N-1)\) holds for \(k=1\). Thus in all cases \(1\le k\le n\),
\[
k+v_2(C_{n-k})=k+s_2(N-k)-1\ge s_2(N).
\]
Every nonempty summand in the formula from Step 2 is divisible by \(2^{s_2(n+1)}\). The empty summand is \(C_n\), which has valuation exactly \(s_2(n+1)-1\). Therefore every \(W_n(S)\) has the stated congruence and exact valuation. In particular, it never vanishes for odd \(n\).

**4. Exact even-order cancellation.** Let \(N(n,r)\) be the number of Dyck paths of semilength \(n\) with exactly \(r\) peaks. A first-return decomposition gives the bivariate series \(F=1+zF(F-1+t)\), where \(z\) records semilength and \(t\) records the number of peaks. Setting \(Y=F-1\) and applying the formal Lagrange coefficient formula to \(Y=z(1+Y)(t+Y)\) gives
\[
N(n,r)=\frac1n\binom nr\binom n{r-1}\quad(1\le r\le n).
\]
This is invariant under \(r\mapsto n+1-r\). If \(n\) is even, paired peak counts have opposite signs in the alternating sum; therefore
\[
W_n([2n-1])=\sum_{r=1}^{n}(-1)^rN(n,r)=0.
\]
Since Walsh characters diagonalize convolution on \(\mathbb F_2^{2n-1}\), Steps 3 and 4 give the complete invertibility classification. In odd orders, all \(2^{2n-1}\) multipliers are nonzero and have the same valuation, giving the determinant assertion. The inverse norm bound follows because a nonzero integer with valuation \(v\) has absolute value at least \(2^v\).

## Verification
The standalone exact-integer program `verify.py` independently constructs each Dyck path and its positional peak mask, accumulates the kernel, and computes its entire unnormalized Walsh transform. It checks the contraction-based formula at **every character** through semilength eight (a total of 43,690 characters), and computes every Walsh value for semilengths nine and ten (655,360 additional characters), sampling 2,048 character formulas in each. It checks the asserted exact valuation at every character of odd semilength at most nine and the all-selected cancellation for even semilengths at most ten. At semilength six it checks the simultaneous-contraction count for **every admissible forced-peak set**. As a separate arithmetic sanity check, it tests the binary digit-sum strict inequality for odd semilengths up to 499. The program returns `PASS` with only integer arithmetic. Finite tests corroborate, but do not replace, the unrestricted proof above.

For illustration, the exact zero-frequency counts at semilengths \(1,2,\ldots,10\) are
\[
0,\ 4,\ 0,\ 31,\ 0,\ 363,\ 0,\ 2305,\ 0,\ 27698.
\]
The group dimensions here are \(2n-1\), not \(n\).

## Relationship to prior work
Classical Narayana enumeration already gives the all-selected character's cancellation for even semilengths; that observation alone is not presented as new. The 2002 work of Mansour and the 2003 work of Eu, Liu and Yeh study peaks selected by **height**, not independent signs at arbitrary **step positions**. Adin and Roichman's 2004 paper identifies positional Dyck peaks with descent data of pattern-avoiding permutations and develops a multivariate inverse-descent generating function, but does not provide the congruence for every full positional peak character, nor the binary Fourier invertibility theorem stated here. The positional contraction formula is an elementary and independently proved ingredient; the new contribution assessed here is its uniform, exact two-adic consequence for every signed character at odd semilength, together with the sharp parity classification of invertibility.

## Limitations
The theorem does not determine all individual Fourier multipliers in a simpler closed numerical form than the independent-set sum, or the full nullity in even semilengths. It does not assert a sharp positive spectral gap for all odd semilengths, and it does not apply to height-marked peaks, restricted-height Dyck paths or other lattice-path ensembles. Bibliographic discovery is not a proof of historical priority; an unindexed earlier equivalent multivariate signed-peak identity is a residual risk. No independent mathematical audit has been performed.

## References
- T. Mansour, *Counting Peaks at Height \(k\) in a Dyck Path*, Journal of Integer Sequences 5 (2002), Article 02.1.1, arXiv:math/0203222 (first posted 2002-03-21). https://arxiv.org/abs/math/0203222
- S.-P. Eu, S.-C. Liu and Y.-N. Yeh, *Dyck Paths with Peaks Avoiding or Restricted to a Given Set*, Studies in Applied Mathematics 111 (2003), 453–465. https://doi.org/10.1111/1467-9590.t01-1-00042
- R. M. Adin and Y. Roichman, *Equidistribution and Sign-Balance on 321-Avoiding Permutations*, Séminaire Lotharingien de Combinatoire 51 (2004), B51d. https://www.mat.univie.ac.at/~slc/s/s51adin.pdf
