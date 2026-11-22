# Four-state Fourier-rank law for acyclic-orientation sink profiles of paths

## Finding
For every integer \(n\ge2\), orient all edges of the labelled path \(P_n\) on vertices \(1,\ldots,n\). Count each orientation according to the indicator of its vertex-sink set in the Boolean group \(H_n=\mathbb F_2^n\). Let \(T_n\) be unnormalized XOR convolution by this multiplicity-counting measure, and let \(R_n=\operatorname{rank}_{\mathbb C}T_n\) (equivalently the real rank). Then
\[
R_2=2,\quad R_3=5,\quad R_4=7,\quad R_5=16,
\qquad R_n=R_{n-1}+R_{n-2}+2R_{n-4}\quad(n\ge6).
\]
Equivalently,
\[
\sum_{n\ge2}R_n z^{n-2}=\frac{2+3z+4z^3}{1-z-z^2-2z^4}.
\]
This is a complete, all-order count of recoverable Walsh frequencies. In particular the nullity is exactly \(2^n-R_n\), and the surviving fraction tends to zero exponentially, at the rate \(\Theta((\rho/2)^n)\), where \(\rho\approx1.85356028\) is the positive Perron root of \(\rho^4-\rho^3-\rho^2-2=0\).

There is also an exact **frequency-by-frequency criterion**. Write any selected frequency \(S\subseteq\{1,\ldots,n\}\) as maximal consecutive nonempty runs of selected vertices. If \(S\ne\{1,\ldots,n\}\), its Walsh multiplier is nonzero if and only if **every** interior run has length not congruent to \(2\pmod4\), and **every** run touching vertex \(1\) or \(n\) has length not congruent to \(1\pmod4\). If \(S=\{1,\ldots,n\}\), the multiplier is zero precisely when \(n\equiv0\pmod4\). The empty selected set is always nonvanishing.

For example, at \(n=14\) the exact convolution rank is \(3878\) and its nullity is \(12506\) among \(16384\) Walsh characters; at \(n=20\), \(R_{20}=157406\) out of \(1048576\).

## Assumptions and scope
An edge \(\{i,i+1\}\) is oriented rightward if its direction is \(i\to i+1\), leftward otherwise. A sink has no outgoing edge; because a path has no undirected cycles, every one of its \(2^{n-1}\) orientations is acyclic. If \(f_n(x)\) counts orientations whose vertex-sink indicator is \(x\in H_n\), define \((T_n u)(x)=\sum_{y\in H_n}f_n(y)u(x+y)\). For a frequency \(S\subseteq[n]\), its unnormalized Walsh multiplier is
\[
W_n(S)=\sum_{\omega\text{ orientation of }P_n}(-1)^{|S\cap\operatorname{Sink}(\omega)|}.
\]
The Walsh basis diagonalizes \(T_n\), so its rank is exactly the number of \(S\) with \(W_n(S)\ne0\). No arbitrary edge weights, cyclic graphs, or alternative normalization are included in this claim.

## Proof
**1. Signed transfer identity.** Encode the direction of edge \(i\to i+1\) by \(b_i\in\{0,1\}\), with \(1\) rightward. Vertex \(1\) is a sink if \(b_1=0\), vertex \(n\) if \(b_{n-1}=1\), and an interior vertex \(i\) if and only if \((b_{i-1},b_i)=(1,0)\). Define
\[
J=\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
B=\begin{pmatrix}1&1\\-1&1\end{pmatrix},\qquad
L_0=(1,1),\ L_1=(-1,1),\quad U_0=(1,1)^{\mathsf T},\ U_1=(1,-1)^{\mathsf T}.
\]
If \(s_i=\mathbf1_{\{i\in S\}}\), summing over all independent edge-direction bits gives the **exact** identity
\[
W_n(S)=L_{s_1}\, M_{s_2}M_{s_3}\cdots M_{s_{n-1}}\,U_{s_n},
\qquad M_0=J,\ M_1=B.
\]
For \(n=2\), the matrix product is empty. The negative entry of \(B\) occurs precisely at the interior left-edge-rightward/right-edge-leftward bit pair \((1,0)\). This explicitly checks the endpoint and orientation conventions.

**2. Exact zero criterion.** Put \(e=(1,1)^{\mathsf T}\); then \(J=ee^{\mathsf T}\) and \(B^4=-4I\). Direct computation for exponents \(0,1,2,3\) gives
\[
e^{\mathsf T}B^k e=(2,2,0,-4),\qquad
L_1B^k e=(0,-2,-4,-4),\qquad
 e^{\mathsf T}B^k U_1=(0,-2,-4,-4),
\]
with each tuple listing values at \(k=0,1,2,3\). Also
\[
L_1B^k U_1=(-2,-2,0,4)\quad(k=0,1,2,3).
\]
All values for larger exponents are the values of the same residue class multiplied by a nonzero power of \(-4\). When at least one \(s_i\) is zero, each zero letter contributes a rank-one matrix \(J\). The resulting scalar factors are the displayed interior-run and boundary-run expressions; consecutive zeros introduce only the nonzero factor \(e^{\mathsf T}e=2\). A run bracketed by zeros has a vanishing factor exactly at length \(2\pmod4\); a run touching one endpoint but not both vanishes exactly at length \(1\pmod4\). If all letters are one, only \(L_1B^{n-2}U_1\) remains and it vanishes exactly at \(n\equiv0\pmod4\). This proves both necessity and sufficiency for the character criterion, with no cancellation between nonzero run factors.

**3. Four-state automaton.** Ignore nonzero scalar multiples of a nonzero intermediate row in the transfer. After the left endpoint, the row has one of four projective representatives
\[
E=(1,1),\qquad Z=(0,1),\qquad G=(-1,1),\qquad X=(1,0).
\]
Right multiplication by \(B\) sends \(E\to Z\to G\to X\to E\), always with nonzero scalar. Right multiplication by \(J\) sends \(E,Z,X\to E\), but kills \(G\). The first selected bit starts in \(G\) if selected and in \(E\) otherwise, hence the initial state-count row is \(v=(1,0,1,0)\). The interior zero/one letters give the unweighted transition-count matrix
\[
Q=\begin{pmatrix}
1&1&0&0\\
1&0&1&0\\
0&0&0&1\\
2&0&0&0
\end{pmatrix},
\]
with rows and columns ordered \(E,Z,G,X\). At the final vertex, exactly one of its two selected-bit choices gives a nonzero dot product from \(E\) or \(G\), while both choices survive from \(Z\) or \(X\). Thus the terminal survival column is \(t=(1,2,1,2)^{\mathsf T}\), and
\[
R_n=vQ^{n-2}t\quad(n\ge2).
\]
This counts all character bits, not the number of distinct sink profiles.

**4. Recurrence and asymptotics.** Direct matrix algebra gives \(\det(\lambda I-Q)=\lambda^4-\lambda^3-\lambda^2-2\). Cayley–Hamilton therefore implies \(R_n=R_{n-1}+R_{n-2}+2R_{n-4}\) for \(n\ge6\), and multiplying the first four values by the recurrence produces the stated rational generating function. The directed transition graph of \(Q\) is strongly connected (the cycle \(E\to Z\to G\to X\to E\) includes every state) and aperiodic (the loop \(E\to E\)); hence \(Q\) is primitive. Perron–Frobenius gives \(R_n\sim c\rho^n\) with \(c>0\). Since \(1<\rho<2\), the rank fraction decays exponentially.

## Verification
The self-contained `verify.py` uses Python 3 standard library only. It independently enumerates every orientation of \(P_n\), computes its exact sink mask, performs an integer fast Walsh transform, and checks **every** frequency against the transfer formula and the run criterion for \(2\le n\le14\). It checks rank and nullity against the four-state recurrence at each of those orders. A separate independent-set inclusion-exclusion summation checks the same Walsh multipliers for \(2\le n\le8\). An independent four-state count agrees with the recurrence for \(2\le n\le200\). All assertions pass. These finite checks corroborate, but do not replace, the all-order matrix proof.

To reproduce, run `python3 verify.py`. No nonstandard packages or external data files are needed.

## Relationship to prior work
Gebhard and Sagan (1999 public preprint) study sinks in acyclic orientations and the classical unique-sink counting theory. Hwang, Jung, Lee, Oh and Yu (2019 public preprint) establish the multivariate acyclic-orientation polynomial, which determines positionwise sink-count data in principle; its path examples do not state the exact Boolean Fourier rank or the four-state nonvanishing classification. Alexandersson and Leite (2026 public preprint) derive a weighted independence-polynomial expression for sinks of arbitrary orientations and count aggregate sinks on paths; their displayed specializations do not establish the number of nonzero **positionwise** evaluations at \(\pm1\), or the rank growth constant. A related earlier result for all degree-at-most-two graphs proves that paths are Fourier-singular because they have leaves, but does not determine how many frequencies survive. The present result addresses this distinct quantitative gap, not the older noninvertibility criterion.

## Limitations
The exact rank and run test apply only to the **multiplicity-weighted sink profiles** of every orientation of a path. They do not give the complete magnitudes of the nonzero eigenvalues, their sharp least magnitude, endpoint range-projection norms, arbitrary tree shape results, or a theorem about non-path graph families. No independent external audit or priority adjudication has occurred; the historical-priority comparison is bounded by the cited works and searched records.

## References
1. D. D. Gebhard and B. E. Sagan, *Sinks in Acyclic Orientations of Graphs*, first publicly posted 1999-07-12, arXiv:math/9907078, https://arxiv.org/abs/math/9907078 .
2. B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh and S.-H. Yu, *Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions*, first publicly posted 2019-10-24, arXiv:1910.10920, https://arxiv.org/abs/1910.10920 .
3. P. Alexandersson and L. S. M. Leite, *Sink polynomials of line graphs and weighted matching polynomials*, first publicly posted 2026-10-30, arXiv:2610.41502, https://arxiv.org/abs/2610.41502 .
