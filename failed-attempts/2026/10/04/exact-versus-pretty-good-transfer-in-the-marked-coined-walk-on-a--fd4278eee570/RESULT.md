# Exact versus pretty-good transfer in the marked coined walk on a star

## Finding

Consider the two-marked-vertex coined discrete-time quantum walk on the star graph used by Štefaňák and Skoupý. The star has one center and \(N\ge2\) external vertices. Two distinct leaves \(s\) and \(r\) are marked by a phase-\(\pi\) coin; the center uses the Grover diffusion coin. The source derives the exact phase
\[
\omega=\arccos\!\left(\frac{N-4}{N}\right)
\]
for the three-dimensional invariant subspace, and the exact sender-to-receiver fidelity after \(2t\) physical steps,
\[
\mathcal F_N(2t)
=
\sin^4\!\left(\frac{\omega t}{2}\right),
\qquad
t\in\mathbb Z_{\ge0}.
\]

The integer-time transport is completely classified:

\[
\boxed{\text{perfect state transfer occurs exactly for }N\in\{2,4,8\}.}
\]

The first exact physical transfer times are
\[
T_{\min}(2)=2,\qquad T_{\min}(4)=4,\qquad T_{\min}(8)=6.
\]

For every other integer \(N\ge2\), exact perfect state transfer never occurs at an integer walk time, but pretty-good state transfer does:
\[
\sup_{t\in\mathbb Z_{\ge0}}\mathcal F_N(2t)=1,
\]
and the supremum is not attained. Equivalently, for every \(\varepsilon>0\), some integer \(t\) satisfies
\[
\mathcal F_N(2t)>1-\varepsilon.
\]

Thus this marked star walk has a sharp arithmetic dichotomy: \(N=2,4,8\) give exact discrete-time transfer, whereas every other star size gives arbitrarily accurate but never exact integer-time transfer.

## Assumptions and scope

The statement concerns exactly the star-graph coined walk and marking convention of the source paper: the two marked external vertices use the phase-\(\pi\) coin, the center uses the Grover coin, and physical time is the integer number of applications of the one-step walk operator. Since sender and receiver are external leaves of a bipartite walk, nonzero receiver fidelity can occur only at even physical times.

The theorem does not claim an obstruction to perfect state transfer after modifying the coin, adding loops, changing phases, using continuous time, or using a different state-transfer protocol. It also does not claim that the first local fidelity maximum is the globally best finite-time approximation when \(N\notin\{2,4,8\}\).

## Proof

The source gives
\[
\mathcal F_N(2t)
=
\sin^4\!\left(\frac{\omega t}{2}\right),
\qquad
\cos\omega=\frac{N-4}{N}=1-\frac4N.
\]
Therefore exact perfect transfer at the even physical time \(2t\) is equivalent to
\[
\omega t=(2j+1)\pi
\]
for some integer \(j\). In particular, exact transfer forces
\[
\frac{\omega}{\pi}\in\mathbb Q.
\]

Assume \(\omega/\pi\) is rational and put \(\zeta=e^{i\omega}\). Then \(\zeta\) is a root of unity, so
\[
2\cos\omega=\zeta+\zeta^{-1}
\]
is an algebraic integer. But \(2\cos\omega=2-8/N\) is rational. Every rational algebraic integer is an integer, hence
\[
2\cos\omega\in\{-2,-1,0,1,2\}.
\]
Solving
\[
2-\frac8N\in\{-2,-1,0,1,2\}
\]
for an integer \(N\ge2\) gives only
\[
N=2,\quad N=4,\quad N=8.
\]
(The value \(-1\) would require \(N=8/3\), and \(2\) has no finite solution.)

For these three sizes,
\[
\begin{array}{c|c|c|c}
N&\cos\omega&\omega&\text{least }t\text{ with }\omega t\equiv\pi\pmod{2\pi}\\
\hline
2&-1&\pi&1\\
4&0&\pi/2&2\\
8&1/2&\pi/3&3
\end{array}
\]
so the first physical transfer times \(2t\) are \(2,4,6\).

Now take any other integer \(N\ge2\). The algebraic-integer argument proves
\[
\frac{\omega}{\pi}\notin\mathbb Q.
\]
An irrational rotation is dense on the circle, so the sequence
\[
t\omega\pmod{2\pi},
\qquad t=0,1,2,\ldots,
\]
comes arbitrarily close to \(\pi\). Hence
\[
\sin^4\!\left(\frac{\omega t}{2}\right)
\]
comes arbitrarily close to \(1\). It can never equal \(1\), because equality would imply the rationality of \(\omega/\pi\), already excluded. This is precisely pretty-good, but not perfect, state transfer for the sender and receiver states of this walk.

## Verification

`verify_star_transfer.py` reconstructs the source's \(3\times3\) effective two-step evolution matrix and checks its unitary evolution against
\[
\mathcal F_N(2t)=\sin^4(\omega t/2)
\]
for many sizes and times. It checks exact unit fidelity at the predicted first times for \(N=2,4,8\), verifies the rational-angle candidate calculation, and searches long integer-time windows for high-fidelity witnesses at representative nonexceptional sizes.

For example, the source's plotted \(N=100\) first local maximum at \(22\) physical steps has fidelity strictly below one; the exact arithmetic theorem explains why no integer time can ever attain one for that size, even though later times can approach one arbitrarily closely.

The finite replay is supplementary. The all-\(N\) classification follows from the root-of-unity algebraic-integer argument and density of irrational rotations.

## Relationship to prior work

Štefaňák and Skoupý derive the exact star-graph eigenphase and fidelity formula used above. Their text says that setting the continuous phase condition \(\omega t=\pi\) gives the receiver state, then chooses the physical transfer time as the closest integer to \(2\pi/\omega\) and describes the result there as “(almost) perfect” state transfer. In contrast, the abstract and conclusion use the phrase “perfect state transfer” for arbitrary \(N\).

The arithmetic classification above separates those two notions at genuinely discrete integer times. It shows that the source's exact formula reaches unit fidelity only for \(N=2,4,8\), while all other sizes have pretty-good state transfer. The later complete-bipartite extension states that same-part dynamics reduces to the star walk “where perfect state transfer is achieved”; it does not state the finite-size exception set.

Chan and Zhan later developed a general theory of pretty-good state transfer for a class of discrete-time quantum walks in terms of spectral and number-theoretic conditions. That broader theory provides important context, but the inspected material did not state this marked-search-star classification. Because model equivalences among discrete-time walk formalisms can be subtle, this later theory remains a residual coverage risk rather than being treated as a novelty proof.

Targeted semantic and web searches for the star model together with the exceptional sizes \(2,4,8\), rational eigenphase, root-of-unity conditions, and pretty-good transfer did not locate the displayed classification.

## Limitations

The result is an arithmetic sharpening of an explicit source formula, not a new quantum-walk construction. The proof uses the exact marked-star invariant subspace and does not automatically extend to the complete graph with self-loops or to the Szegedy model discussed in the same paper.

Pretty-good transfer is qualitative here: density proves arbitrarily high fidelity but gives no optimized hitting-time bound as a function of the requested error. Quantitative Diophantine estimates would be a separate problem.

A later general theory of pretty-good discrete-time state transfer may imply the classification after a nontrivial identification of the marked-search walk with its framework. No such explicit implication for this star model was located in the inspected literature, so broad priority is not claimed.

## References

1. M. Štefaňák and S. Skoupý, “Perfect state transfer by means of discrete-time quantum walk search algorithms on highly symmetric graphs,” *Physical Review A* 94, 022301 (2016), arXiv:1608.00498, DOI: 10.1103/PhysRevA.94.022301.
2. M. Štefaňák and S. Skoupý, “Perfect state transfer by means of discrete-time quantum walk on complete bipartite graphs,” *Quantum Information Processing* 16, 72 (2017), arXiv:1610.03633, DOI: 10.1007/s11128-017-1516-z.
3. A. Chan and H. Zhan, “Pretty good state transfer in discrete-time quantum walks,” *Journal of Physics A: Mathematical and Theoretical* 56, 165305 (2023), DOI: 10.1088/1751-8121/acc4f5.
