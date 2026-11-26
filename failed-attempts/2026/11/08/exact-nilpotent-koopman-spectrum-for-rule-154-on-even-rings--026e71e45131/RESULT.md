# Exact nilpotent Koopman spectrum for Rule 154 on even rings

## Finding
Let \(n=2m\ge 2\) and let \(F_n:\{0,1\}^n\to\{0,1\}^n\) be elementary cellular automaton Rule 154 with periodic boundary conditions. Let \(K_n\) be its Koopman operator on all complex-valued functions on \(\{0,1\}^n\), defined by \((K_nf)(x)=f(F_nx)\). Put \(h=2^{\nu_2(m)}\), the greatest power of two dividing \(m\). For every integer \(t\ge0\),
\[
\operatorname{rank}(K_n^t)=2^{2m}-2^{m+1}+2^{m-\min(t,h)+1}.
\]
Consequently the algebraic multiplicity of the zero Koopman eigenvalue is exactly
\[
Z_n=2^{m+1}-2^{m-h+1},\qquad \frac{Z_n}{2^n}=2^{1-m}(1-2^{-h}).
\]
All zero-eigenvalue Jordan blocks are classified: for \(1\le j<h\) there are precisely \(2^{m-j}\) blocks of size \(j\), and there are precisely \(2^{m-h+1}\) blocks of size \(h\). No other zero-eigenvalue Jordan blocks occur. The maximum transient height is exactly \(h\).

More geometrically, write an even-ring state as two half-ring subwords, one at even sites and one at odd sites. Every configuration containing a \(1\) in **both** parity classes is periodic. A configuration supported on one parity class is periodic precisely when its nonzero half-ring word \(a\) satisfies
\[
\bigoplus_{\ell=0}^{m/h-1}a_{r+\ell h}=0\quad\text{for every }0\le r<h.
\]
The all-zero configuration is periodic. Thus every nonperiodic configuration lies on exactly one parity class, and the displayed parity conditions classify all of them.

## Assumptions and scope
Here \(\nu_2(m)\) is the exponent of two dividing the positive integer \(m\), all configuration indices are taken cyclically, \(\oplus\) is addition in \(\mathbb F_2\), and Rule 154 uses the exact Boolean update
\[
(F_nx)_i=x_{i+1}\oplus x_{i-1}(1\oplus x_i).
\]
This is the elementary rule with outputs \(1,0,0,1,1,0,1,0\) on neighborhoods \(111,110,101,100,011,010,001,000\), respectively. The Koopman operator acts on the full \(2^n\)-dimensional complex function space; all multiplicities refer to algebraic multiplicity over \(\mathbb C\). The theorem includes \(n=2\), when the two neighbors of a site coincide. No assumption is made about initial configurations beyond binary periodic-ring states.

## Proof
**Step 1: invariant decomposition.** Call a state *single-parity* if its support lies entirely in the even sites or entirely in the odd sites. Let \(U\) be the set of single-parity states and let \(C\) be its complement. For \(n=2m\), an even-supported state is sent to an odd-supported state, and vice versa, so \(F_n(U)\subseteq U\). To show \(F_n(C)\subseteq C\), write \(a_j=x_{2j}\) and \(b_j=x_{2j+1}\) for \(j\) modulo \(m\). Then
\[
(F_nx)_{2j}=b_j\oplus b_{j-1}(1\oplus a_j),\qquad
(F_nx)_{2j+1}=a_{j+1}\oplus a_j(1\oplus b_j).
\]
If every odd coordinate of \(F_nx\) vanished, then \(a_{j+1}=a_j(1\oplus b_j)\) around the cycle. Either all \(a_j=0\), or all \(a_j=1\) and all \(b_j=0\): a zero \(a_j\) propagates, and a cyclic sequence with a \(1\) can never change from \(1\) to \(0\). Likewise, if every even output coordinate vanished, either all \(b_j=0\), or all \(b_j=1\) and all \(a_j=0\). Neither situation is possible for an input in \(C\). Hence both \(U\) and \(C\) are forward invariant.

**Step 2: the complementary subsystem is a permutation.** Suppose \(F_nx=F_nx'\) with \(x\ne x'\). Since the local rule is permutive in its right neighbor, equality of \(x\) and \(x'\) at two successive sites propagates to equality everywhere. Furthermore, if \(x_i=x'_i=1\), equality of outputs at \(i\) forces \(x_{i+1}=x'_{i+1}\), providing two consecutive matches and a contradiction. Thus every coordinate-pair \((x_i,x'_i)\) is one of \(A=(0,0)\), \(B=(0,1)\), \(D=(1,0)\), and no two consecutive coordinates can both be \(A\).

A direct substitution into the local equality gives the complete directed transition graph on adjacent pair-symbols (each arrow \(PQ\to QR\) represents three successive pair-symbols):

```
AA -> AA
AB -> BA
BA -> AB, AD
AD -> DA
DA -> AB, AD
BB -> BA
BD -> DB, DD
DB -> BB, BD
DD -> DA
```

Here the symbol \(D\) represents \((1,0)\), not \((1,1)\). Besides the trivial loop at \(AA\), the only strongly connected components containing directed cycles are \(\{AB,BA,AD,DA\}\) and \(\{BD,DB\}\). Every closed nontrivial walk therefore alternates between two symbol classes: in the first component one entire site parity is \(A\), and in the second component the pair-symbols alternate \(B,D\). In either case both \(x\) and \(x'\) are single-parity configurations. In particular distinct states in \(C\) cannot have the same image. Since \(F_n\) maps finite \(C\) into itself and is injective there, its restriction to \(C\) is a permutation: every state in \(C\) is periodic.

**Step 3: exact linear dynamics on the single-parity subsystem.** On half-ring words of length \(m\), let \(S\) be cyclic shift and \(L=I+S\) over \(\mathbb F_2\). The displayed update in Step 1 shows that \(F_n\) swaps the two parity supports and applies either \(L\) or \(S^{-1}L\). Hence \(F_n^t\), restricted to either parity-supported subspace, is a cyclic shift composed with \(L^t\). In the polynomial realization \(\mathbb F_2[z]/(z^m-1)\), \(L\) acts by \(1+z\). Write \(m=hr\), with \(r\) odd. In characteristic two, \(z^m-1=(z^r-1)^h\), and \(z+1\) has exact multiplicity \(h\) in this polynomial. The Euclidean algorithm therefore gives
\[
\dim_{\mathbb F_2}\operatorname{im}(L^t)=m-\min(t,h).
\]
The stable image \(W=\operatorname{im}(L^h)\) consists exactly of words satisfying the parity equations in the Finding: indeed \(L^h=I+S^h\), and on each of the \(h\) length-\(r\) cyclic residue classes its image is the even-parity hyperplane. The restriction of \(F_n\) to the union of the two copies of \(W\) is bijective, so these and only these single-parity states are periodic.

**Step 4: Koopman power ranks and Jordan blocks.** For a map \(F\) of a finite set, the rank of pullback by \(F^t\) equals \(\#\operatorname{im}(F^t)\). The two parity-supported images intersect exactly in the zero configuration. Thus
\[
\#\operatorname{im}(F_n^t)=\#C+2\cdot 2^{m-\min(t,h)}-1.
\]
Since \(\#C=2^{2m}-2^{m+1}+1\), this is the asserted rank formula. The stable rank counts periodic states, so the remaining \(Z_n\) states give the algebraic multiplicity of eigenvalue zero in the Koopman matrix of a finite functional graph. If \(R_t=\operatorname{rank}(K_n^t)\), the number of zero-Jordan blocks of size at least \(t\) is \(R_{t-1}-R_t\). For \(1\le t\le h\) this difference is \(2^{m-t+1}\), and it vanishes for \(t>h\). Taking successive differences yields precisely the stated block multiplicities. The last positive difference occurs at \(t=h\), proving sharpness of the maximum transient height.

## Verification
The standalone `verify.py` uses state-graph pruning to classify periodic states independently of the formula, tests the precise single-parity parity-check criterion, computes ranks of successive images directly, and verifies the \(\mathbb F_2\) linear-algebra ranks for half-rings. It also reconstructs the nine-node collision graph from all local binary assignments. The test covers every binary state for even ring sizes \(2,4,6,8,10,12,14,16\); its computational results are finite confirmations, not substitutes for the proof. Run `python3 verify.py` from the extracted package.

## Relationship to prior work
Zhu and Richard, *Elementary cellular automata: spectral properties of Koopman operator for finite periodic realizations* (arXiv:2610.10967v1, 7 October 2026), §4.2–4.3, report that Rule 154 has a very small zero-eigenvalue ratio for even rings and that it appears to decrease with ring length; they do not provide an exact formula or the nilpotent Jordan filtration. Their general functional-graph/Koopman spectral connection is used here, not claimed as new. Nobe and Yura (2007) analyze the reversible Rule 154 **on odd rings**, proving linearization and orbit-period properties for that regime. The explicit even-ring transient decomposition, all-size power-rank formula and zero-Jordan block census are different conclusions. Earlier finite-length tables do not themselves prove these formulas.

## Limitations
The theorem covers finite periodic **even** rings and the zero-eigenvalue Jordan structure; it does not classify multiplicities of nonzero roots of unity or infinite-lattice Koopman spectra. Literature access was incomplete for Chua et al., *More Isles of Eden* (2007), which studies basin/isles structure and mentions Rule 154, so an unrecognized equivalent even-ring result in that source remains a historical-priority risk. No independent mathematical audit has been performed.

## References
1. Q. Zhu and S. Richard, *Elementary cellular automata: spectral properties of Koopman operator for finite periodic realizations*, arXiv:2610.10967v1 (7 October 2026), https://arxiv.org/html/2610.10967 .
2. A. Nobe and F. Yura, *Linearizable cellular automata*, Journal of Physics A 40 (2007), 7159–7174, DOI: 10.1088/1751-8113/40/26/004.
3. L. O. Chua, K. Karacs, V. I. Sbitnev, J. Guan and J. Shin, *A Nonlinear Dynamics Perspective of Wolfram's New Kind of Science. Part VIII: More Isles of Eden*, International Journal of Bifurcation and Chaos 17 (2007), 3741–3894, DOI: 10.1142/S0218127407019901.
