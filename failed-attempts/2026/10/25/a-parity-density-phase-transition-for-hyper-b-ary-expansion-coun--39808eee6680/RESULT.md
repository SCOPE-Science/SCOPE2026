# A parity-density phase transition for hyper-\(b\)-ary expansion counts

## Finding
For an integer \(b\ge2\), let \(h_b(n)\) be the number of finite expansions
\[
n=\sum_{j\ge0} d_j b^j,\qquad 0\le d_j\le b,
\]
with integer digits, only finitely many nonzero. Define the exact block count
\[
A_b(L)=\#\{0\le n<b^L:h_b(n)\equiv1\pmod2\},\qquad L\in\mathbb Z_{\ge0}.
\]
Then
\[
A_b(0)=1,\quad A_b(1)=b,\quad
A_b(L)=(b-1)A_b(L-1)+2A_b(L-2)-1\quad(L\ge2),
\]
and consequently
\[
\boxed{\sum_{L\ge0}A_b(L)t^L=\frac{1-2t^2}{(1-t)\bigl(1-(b-1)t-2t^2\bigr)}.}
\]
Let
\[
\Delta_b=\sqrt{(b-1)^2+8},\qquad
\lambda_{b,\pm}=\frac{b-1\pm\Delta_b}{2},\qquad
\theta_b=\log_b\lambda_{b,+}.
\]
Writing \(N_b(X)=\#\{0\le n<X:h_b(n)\text{ is odd}\}\) for real \(X\ge1\), the binary case has
\[
\boxed{N_2(X)=\tfrac23X+O(1)},
\]
whereas every integer \(b\ge3\) has \(0<\theta_b<1\) and
\[
\boxed{N_b(X)=\Theta_b(X^{\theta_b})\quad(X\to\infty).}
\]
In particular, the odd-value set has natural density \(2/3\) at \(b=2\), but natural density zero for every \(b\ge3\). For \(b=3\) the block counts start \(1,3,7,19,51,139\); for \(b=4\) they start \(1,4,13,46,163,580\).

## Assumptions and scope
All bases \(b\) are ordinary integers at least \(2\); all digit expansions have finite support, so \(h_b(n)\) is a finite positive integer for every nonnegative integer \(n\). Put \(h_b(-1)=0\) as a boundary convention, not as a representation count. The statement concerns the parity of the *number* of such representations, not parity of digits, summands, or values of \(n\). The ordinary base-\(b\) expansion makes \(h_b(n)\ge1\). No primality condition on \(b\) is imposed.

## Proof
**1. Exact digit recurrence.** In an expansion of \(bn\), the final digit is either \(0\) or \(b\), so
\[
h_b(bn)=h_b(n)+h_b(n-1)\qquad(n\ge0).
\]
For \(1\le r<b\), the final digit of an expansion of \(bn+r\) is necessarily \(r\), and hence
\[
h_b(bn+r)=h_b(n)\qquad(n\ge0,\ 1\le r<b).
\]
These identities hold at \(n=0\) using \(h_b(-1)=0\).

**2. Four-state parity automaton.** For \(n\ge0\), use the parity state \((a,c)=(h_b(n),h_b(n-1))\bmod2\). Appending a base-\(b\) digit \(r\), thus replacing \(n\) by \(bn+r\), acts as
\[
r=0:(a,c)\mapsto(a+c,c),\qquad
r=1:(a,c)\mapsto(a,a+c),\qquad
2\le r<b:(a,c)\mapsto(a,a).
\]
All pairs are over \(\mathbb F_2\). The state \((0,0)\) is absorbing. The other three states, denoted \(10,11,01\), evolve under the exact count matrix
\[
M_b=\begin{pmatrix}
1&1&0\\
b-1&b-2&1\\
0&1&1
\end{pmatrix}.
\]
Indeed, from state \(10\), one digit leads to \(10\) and \(b-1\) digits lead to \(11\); from \(11\), digits \(0\) and \(1\) lead to \(01\) and \(10\), while the remaining \(b-2\) digits lead to \(11\); from \(01\), digits \(0\) and \(1\) lead to \(11\) and \(01\), while the remaining \(b-2\) lead to the absorbing state. Reading all \(L\)-digit words including leading zeros from the start state \(10\) enumerates each integer in \([0,b^L)\) exactly once because the leading-zero transition fixes \(10\).

Let \((x_L,y_L,z_L)^\mathsf T=M_b^L(1,0,0)^\mathsf T\) record the numbers ending in states \(10,11,01\). Those having odd \(h_b(n)\) are exactly \(10\) and \(11\); thus \(A_b(L)=x_L+y_L\). Matrix multiplication gives
\[
x_{L+1}=x_L+y_L,\qquad
 y_{L+1}=(b-1)x_L+(b-2)y_L+z_L,\qquad
 z_{L+1}=y_L+z_L.
\]
Hence \(x_L-z_L=1\) for every \(L\), since this difference is invariant and initially one. For \(L\ge1\), \(x_L=A_b(L-1)\), so
\[
A_b(L+1)=(b-1)A_b(L)+2A_b(L-1)-1.
\]
The initial counts are \(A_b(0)=1\) and \(A_b(1)=b\). Summing the recurrence as a formal power series yields the displayed rational generating function; no convergence assumption is required.

**3. Exact spectral solution and the sparse-base law.** The homogeneous characteristic polynomial is \(u^2-(b-1)u-2\). The constant particular solution of the inhomogeneous recurrence is \(1/b\). Thus for every integer \(L\ge0\),
\[
A_b(L)=\frac1b+c_{b,+}\lambda_{b,+}^L+c_{b,-}\lambda_{b,-}^L,
\]
where the initial values give
\[
c_{b,+}=\frac{(b-1)(b+3+\Delta_b)}{2b\Delta_b}>0,
\qquad
c_{b,-}=\frac{(b-1)(\Delta_b-b-3)}{2b\Delta_b}.
\]
For \(b\ge3\), \(2<\lambda_{b,+}<b\) (the upper inequality follows by squaring \(\Delta_b<b+1\), equivalent to \(b>2\)). Also \(\lambda_{b,+}\lambda_{b,-}=-2\), so \(|\lambda_{b,-}|<1\). Therefore \(A_b(L)\sim c_{b,+}\lambda_{b,+}^L\). If \(b^L\le X<b^{L+1}\), monotonicity yields \(A_b(L)\le N_b(X)\le A_b(L+1)\). Since \(\lambda_{b,+}=b^{\theta_b}\), these bounds prove \(N_b(X)=\Theta_b(X^{\theta_b})\) and density zero.

**4. The binary boundary.** The same exact spectral solution at \(b=2\) yields
\[
A_2(L)=\frac23\,2^L+\frac12-\frac{(-1)^L}{6}.
\]
For arbitrary prefixes, let \(s_2(0)=0\), \(s_2(n+1)=h_2(n)\), and use the classical identities \(s_2(2n)=s_2(n)\), \(s_2(2n+1)=s_2(n)+s_2(n+1)\). Induction on \(n\) proves \(s_2(n)\) is even precisely when \(3\mid n\): for \(n=0,1\) the assertion holds, the even-index recurrence preserves divisibility by \(3\), and the odd-index recurrence reduces the three residue classes \(n\bmod3\) to exactly the desired parity pattern. Therefore \(h_2(n)\) is odd if and only if \(n\not\equiv2\pmod3\). Counting these residues below any real \(X\) gives \(N_2(X)=\tfrac23 X+O(1)\).

## Verification
The standalone Python program `verify.py` performs independent finite calculations by multiplying the actual restricted-partition generating product in \(\mathbb F_2[x]\) and comparing against the parity-state matrix and scalar recurrence for every base \(2\le b\le10\) and levels \(0\le L\le6\) with \(b^L\le10^6\). It separately checks individual coefficient parity against the integer generalized-Stern recurrence, checks matrix/recurrence equality through level \(100\), and checks the binary residue criterion through index \(50000\). The finite computations are corroboration; the preceding proof establishes all bases, lengths, and asymptotic claims.

## Relationship to prior work
Defant's 2015 preprint arXiv:1506.07824 defines the generalized Stern sequence and determines pointwise bounds and maximum-order growth; Coons and Spiegelhofer's 2015 preprint arXiv:1511.08267 gives a related maximal-order treatment. Neither inspected paper classifies the parity frequency of representation counts. Dilcher and Ericksen (2015) study hyperbinary Stern polynomials, rather than base-uniform parity densities. Wakhare and collaborators (2018) treat polynomial and matrix variants with related expansion interpretations, but no equivalent parity-density theorem was located in the inspected text.

There is **exact numerical overlap** with existing tables: for \(b=3\), \(A_3(L)\) is OEIS A052948 shifted by one index (its listed interpretation is a constrained walk); for \(b=4\), \(A_4(L)\) is OEIS A180144 (its listed interpretation is a chess-move count). Thus those individual numerical sequences and their rational generating functions were already known. The finding is the universal connection to odd hyper-\(b\)-ary expansion counts, the base-uniform proof, and the sharp dichotomy between binary positive density and all larger bases having a specific sublinear growth exponent; it does not claim novelty for the pre-existing numeric tables or the classical binary residue criterion. Earlier binary Stern residue-distribution results concern base \(2\) only, not the generalized family \(b\ge3\).

## Limitations
Originality is assessed against the full texts and indexes described, not established by an exhaustive theorem-priority search; unindexed equivalent work could exist. The asymptotic constants depend on fixed \(b\) and the result does not give a joint uniform estimate as \(b\) and \(X\) vary. The calculations do not establish the infinite theorem independently of the proof. This is a parity theorem: it does not describe the full distribution of \(h_b(n)\) modulo higher prime powers.

## References
1. C. Defant, *Upper Bounds for Stern's Diatomic Sequence and Related Sequences*, arXiv:1506.07824v1, first public 2015-06-25; Electronic Journal of Combinatorics 23(4), P4.8 (2016). https://arxiv.org/pdf/1506.07824
2. M. Coons and L. Spiegelhofer, *The Maximal Order of Hyper-(b-ary)-Expansions*, arXiv:1511.08267v1, first public 2015-11-26. https://arxiv.org/pdf/1511.08267
3. K. Dilcher and L. Ericksen, *Hyperbinary Expansions and Stern Polynomials*, Electronic Journal of Combinatorics 22(2), P2.24 (2015). https://doi.org/10.37236/4822
4. T. Wakhare et al., *Hyper b-ary Expansions and Stern Polynomials*, arXiv:1810.11096v1 (2018). https://arxiv.org/pdf/1810.11096
5. OEIS A052948, constrained-walk interpretation and generating function. https://oeis.org/A052948
6. OEIS A180144, chess-move interpretation and generating function. https://oeis.org/A180144
