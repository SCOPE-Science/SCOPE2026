# Exact three-row odd-island entropy and a quantitative planar entropy bound

## Finding
Let \(Y_3\) be the binary shift on the open strip \(\mathbb Z\times\{0,1,2\}\), with nearest-neighbor horizontal and vertical adjacency. Every **finite** connected component of occupied vertices must have odd cardinality; infinite occupied components are allowed. Its horizontal entropy per three-site column is
\[
h(Y_3)=\log\Lambda_3,\qquad 6.88017<\Lambda_3<6.88018,
\]
where \(\Lambda_3\) is the unique real root above \(6\) of
\[
P(t)=t^{11}-6t^{10}-10t^9+32t^8-30t^7-38t^6+99t^5-2t^4-49t^3+16t^2+10t-1.
\]
The finite-board counts \(F_n\), requiring every occupied component of the finite \(3\times n\) rectangle itself to be odd, start with
\[
(F_0,\ldots,F_7)=(1,6,37,251,1692,11635,79973,550440).
\]
They are exactly specified by the 19-state transfer below. In addition, if \(X_{\mathrm{odd}}\) is the full planar binary odd-island subshift, its entropy **per lattice site** obeys
\[
h(X_{\mathrm{odd}})\ge\frac14\log\Lambda_3>0.48216.
\]
This improves the previously known width-two-strip construction \(\frac13\log\Lambda_2\approx0.41735567\). No exact value of the planar entropy is asserted.

## Assumptions and scope
The strip has open, nonperiodic vertical boundary and both infinite horizontal directions. Occupied sites are symbols \(1\); only edge-sharing (not diagonal) neighbors count as connected. A finite component is one with finitely many sites, regardless of whether other components are infinite. The horizontal shift is by one complete three-site column. The planar entropy is the usual limit of logarithmic square-pattern counts divided by their area. The cited literature introduces and discusses the **multidimensional component-parity odd shift**; it must not be confused with the unrelated classical one-dimensional run-spacing odd shift.

## Proof
**1. A deterministic frontier state.** Scan columns from left to right, keeping the three occupied/empty frontier positions as a tuple of labels \(\ell_r\in\{-1,0,1,2\}\) with \(-1\) for an empty site. Equal nonnegative labels indicate that the corresponding occupied sites belong to the same connected component in the scanned region. Labels are canonically renumbered in increasing row order. For every distinct label store the parity \(p_j\in\{0,1\}\) of the number of occupied sites in that component accumulated so far. Any component detached from the current frontier has already been required to have odd cardinality.

For each next column mask \(m\in\{0,\ldots,7\}\), form one vertex for each old component and one for each newly occupied row. Union an old component to the new site in the same row whenever both are occupied, and union vertically adjacent occupied new sites. The new parity of a merged component is the XOR of all parities of its old components and one for each new occupied vertex in it. Reject the transition if an old component fails to meet the new frontier and has even parity. Retain, and canonically relabel, the new frontier components and their parities. This rule is completely deterministic for each state and mask, and is implemented in `checker.py` without a precomputed table.

Starting at the all-empty frontier, breadth-first closure under the eight masks yields exactly 19 states and 119 mask-labelled transitions. Define the integer matrix \(M\) by setting \(M_{ij}\) equal to the number of accepted column masks taking state \(i\) to state \(j\). With \(e\) the empty-state coordinate vector, every finite-board component is finalized by an additional empty column, giving the exact identity
\[
F_n=e^{\mathsf T}M^{n+1}e\qquad(n\ge0).
\]

**2. Spectral determination.** Direct exact integer elimination on the specified 19-state matrix gives
\[
\det(tI-M)=(t-1)^3(t+1)(t^4+t^3-3t-1)P(t).
\]
Every reachable state returns to the empty state by appending one or two full masks \(111\), then a zero mask. Indeed the first full column merges all active components, and a second full column flips the parity of their union, as its three added sites have odd cardinality. The empty state reaches every state by the breadth-first definition and has a zero-mask self-loop. Hence \(M\) is primitive. Moreover \((M^{20})_{ee}>6^{20}\), so its Perron eigenvalue exceeds \(6\). Exact Sturm root counting gives one real root of \(P\) on \((6,9)\), with sign change across \((6.88017,6.88018)\); all roots of the other displayed factors have absolute value smaller than \(6\). Consequently the spectral radius is exactly \(\Lambda_3\), and Perron–Frobenius implies \(\lim_{n\to\infty}F_n^{1/n}=\Lambda_3\).

**3. The finite-board counts give the actual strip entropy.** Every finite board whose components are odd extends to \(Y_3\) by inserting only empty columns on both sides. Thus \(F_n\le L_n\), where \(L_n\) is the number of length-\(n\) words in \(Y_3\). Conversely, any \(n\)-column word occurring in \(Y_3\) has no *even* occupied connected component fully contained away from both boundary columns. On either side that contains a boundary-touching component, adjoin one fully occupied column \(111\). This merges every component reaching that side. At most one additional full column on that side changes the merged component's parity, if necessary, before it is terminated by zeros. If both sides attach to the same component, one parity adjustment suffices; if they remain disconnected they can be adjusted separately. Hence at most two columns per side produce a legal finite board. Choose a canonical such padding per word to obtain an injection into the \(3\times(n+4)\) valid boards. Therefore
\[
F_n\le L_n\le F_{n+4},
\]
so \(h(Y_3)=\lim_{n\to\infty}n^{-1}\log L_n=\log\Lambda_3\).

**4. A planar lower bound.** Embed independent copies of \(Y_3\) in the plane along successive three-row horizontal bands, separating consecutive bands by one entirely vacant row. Then connected occupied components cannot cross between distinct bands and the resulting planar configuration is valid. An \(N\times N\) square contains at least \(\lfloor N/4\rfloor\) independent three-row bands, each contributing at least \(L_N\) distinct patterns. The number of planar patterns is therefore at least \(L_N^{\lfloor N/4\rfloor}\), which yields \(h(X_{\mathrm{odd}})\ge\tfrac14\log\Lambda_3\). For the independently known width-two Perron root \(\Lambda_2\approx3.49756499717934\), exact rational enclosures give \(\Lambda_3^3>\Lambda_2^4\), proving strict improvement.

## Verification
Execute `python checker.py` with Python 3 and SymPy. The script constructs the transfer graph from the stated union-and-parity rule, checks 19 states/119 transitions, symbolically verifies the exact characteristic factorization, performs exact root isolation and a Perron lower bound, and independently enumerates every occupancy pattern on finite boards of widths one through five. It also tests all locally admissible short words for a four-column padding completion and checks the entropy-bound comparison. These finite tests support the proof but cannot establish arbitrary-length statements without the frontier-state invariant and padding argument above.

## Relationship to prior work
Antonin Callard's 2025 doctoral thesis (*Soficity of multidimensional subshifts*, Chapter 7, p. 54) describes the multidimensional odd shift and attributes its two-dimensional soficity to unpublished work by Julien Cassaigne. It does not present the 19-state, three-row exact entropy, finite-board sequence, or the explicit improved planar numerical lower bound here. Known two-row odd-island strip results give a different fifth-degree Perron equation and do not determine a three-row frontier in which separated occupied components can merge. Standard finite-width transfer/Perron–Frobenius principles are used, not claimed as new.

## Limitations
The root law concerns the open three-row strip, not the entire two-dimensional system. The planar figure is a constructive *lower bound*, not the planar entropy or a sharp upper bound. All exact matrix claims are reproducible from the standalone code but no independent expert audit or historical-priority certification is claimed. The 2010 unpublished Cassaigne construction remains a residual priority risk; the available thesis citation gives no entropy formula for it. A general finite-width transfer approach is classical, while the claim here is the specified exact three-row calculation, four-column completion, and quantitative full-plane consequence.

## References
- A. Callard, *Soficity of multidimensional subshifts*, doctoral thesis, Université de Caen Normandie, publicly defended 24 June 2025, Chapter 7 p. 54, https://www.acallard.net/publications/thesis.pdf.
- J. Cassaigne, *Odd shift*, unpublished construction (2010), cited in Callard's thesis, bibliography and Chapter 7. No specific entropy value is attributed to it.
