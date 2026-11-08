# A rational centralizer census for path graphical Lie algebras

## Finding

Let \(q\) be any prime power and let \(n\ge 0\). Let \(\mathfrak g_n(q)\) be the two-step graphical Lie algebra of the labeled path on vertices \(1,\ldots,n\), over \(\mathbb F_q\): it has vertex generators \(v_i\), central edge generators \(z_i\), and the only nonzero basic brackets are \([v_i,v_{i+1}]=z_i\). Define \(c_n(q)\) to be the **number of distinct subsets** \(C_{\mathfrak g_n(q)}(x)\), as \(x\) ranges through the Lie algebra. These are distinct actual centralizer subalgebras, not the number of elements with a given centralizer dimension. The exact generating function is

\[
\boxed{\sum_{n\ge0}c_n(q)u^n=
\frac{1+(1-q)u+qu^2-qu^3+u^4}
{1-qu+(q-2)u^2+u^4-u^5}.}
\]

Equivalently \(c_0(q)=c_1(q)=1\), and for every \(n\ge0\), setting all negative-index terms to zero,
\[
 c_n(q)-q c_{n-1}(q)+(q-2)c_{n-2}(q)+c_{n-4}(q)-c_{n-5}(q)
 =[u^n]\bigl(1+(1-q)u+qu^2-qu^3+u^4\bigr).
\]
In particular \(c_2(q)=q+2\), \(c_3(q)=q^2+2\), and \(c_4(q)=q^3-q^2+2q+4\). The first values at \(q=2\), for \(n=1,\ldots,10\), are \(1,4,6,12,24,45,88,170,328,635\). The count is a polynomial in \(q\) for each fixed \(n\), with nonnegative integers at all prime powers.

## Assumptions and scope

The Lie bracket is alternating and extends bilinearly, including in characteristic two; the center contains every edge generator. For \(n=0,1\), the algebra is abelian and has a single element-centralizer. For \(n\ge2\), centralizers can be identified by intersecting with the vertex span because the whole edge span is central. Fields may have arbitrary finite prime-power order, without parity restriction. The vertices are distinguished and fixed, and centralizers are counted as embedded subalgebras, not up to abstract isomorphism or automorphism conjugacy.

## Proof

Write \(x=\sum_i a_i v_i+z\), where \(z\) is central. If \(y=\sum_i b_i v_i+w\), the independent edge brackets show that \(y\) centralizes \(x\) precisely when
\[
 a_i b_{i+1}-a_{i+1}b_i=0\qquad(1\le i<n).
\]
Let \(S=\{i:a_i\ne0\}\). Each connected component \(J\) of the induced path on \(S\) forces \(b|_J\) to be a scalar multiple of \(a|_J\); every vertex in \(N(S)\setminus S\) has \(b_i=0\); all other coordinates are free. Components of \(S\) of size one contribute only free individual coordinates. Thus a centralizer is completely specified by (i) its nontrivial support runs \(J\) of size at least two, together with a line in \((\mathbb F_q^*)^{J}\) for each, and (ii) the set \(Z=N(S)\setminus S\) of forced-zero coordinates. This parametrization has **no identifications**: zero projections recover \(Z\); among the remaining coordinates, joint projections of dimension one recover exactly the nontrivial runs, and their projected lines recover the ratios. Conversely these data determine the entire vertex kernel. A run of length \(d\ge2\) admits exactly \((q-1)^{d-1}\) projective lines with no zero coordinates.

Encode the coordinate support as bits \(s_i=\mathbf1_{i\in S}\), augmented by boundary bits \(s_0=s_{n+1}=0\). At each position record an output symbol \(B\), \(Z\), or \(F\): \(B\) when \(s_i=1\) and at least one neighbor bit is one, \(Z\) when \(s_i=0\) and at least one neighbor bit is one, and \(F\) otherwise. These output words are precisely the possible canonical run/zero descriptions just established. Give an output word weight \((q-1)^{\#\{i:2\le i\le n,\ y_{i-1}=y_i=B\}}\), one factor for each continuation of a nontrivial run. Its weight is exactly the number of centralizers with that description.

For completeness we construct the deterministic seven-state automaton recognizing these output words, thus counting each realized word once even when multiple support patterns produce it. Reading from left to right, a state is a subset of the four bit-pairs \((s_{i-1},s_i)\), containing all pairs compatible with the outputs read. Starting from \(\{(0,0),(0,1)\}\), appending a symbol entails choosing \(s_{i+1}\in\{0,1\}\), testing the displayed three-bit output rule, and retaining \((s_i,s_{i+1})\). The seven reachable states in order are
\[
\begin{aligned}
&\{00,01\},\quad\{00,10\},\quad\{11\},\quad\{01\},\\
&\{00\},\quad\{10,11\},\quad\{10\}.
\end{aligned}
\]
The accepted states (allowing the required right boundary bit \(s_{n+1}=0\)) are those with indices \(0,1,4,5,6\). The transition matrix \(M\), with each row/column in the stated state order and weights as above, is
\[
 M=\begin{pmatrix}
0&1&1&1&0&0&0\\
1&0&0&0&1&0&0\\
0&0&0&0&0&q-1&0\\
0&0&1&0&0&0&1\\
0&0&0&1&1&0&0\\
1&0&0&0&0&q-1&0\\
1&0&0&0&0&0&0
\end{pmatrix}.
\]
A transition labeled \(B\) from states \(2\) or \(5\) continues a \(B\)-run, so and only so receives weight \(q-1\); all other allowed transitions receive weight one. Here the output symbol \(B\) is equivalent to entering state \(2\) or \(5\), which makes the weighting state-local. Let \(e_0\) be the first standard row vector and let \(h=(1,1,0,0,1,1,1)^{\mathsf T}\). The exact count is \(c_n(q)=e_0M^nh\), including the empty word at \(n=0\). Elementary elimination in \((I-uM)t=h\) gives
\[
 e_0(I-uM)^{-1}h=
\frac{1+(1-q)u+qu^2-qu^3+u^4}
{1-qu+(q-2)u^2+u^4-u^5},
\]
proving the claim. This is a deterministic-language enumeration, not a count of support strings with multiplicity.

## Verification

Run `python verify.py` with Python 3 and no third-party packages. The checker enumerates the **actual centralizer row spaces** of every graph-Lie vertex coefficient vector, by finite-field row-reduction of the edge-determinant coefficient matrix, for all \(n\le8\) at \(q=2\), all \(n\le7\) at \(q=3\), all \(n\le6\) at \(q=4\), and all \(n\le5\) at \(q=5\). The four-element field uses the independent binary-polynomial multiplication table. It compares these subspace counts with the recurrence coefficients. Independently, it enumerates all binary supports, constructs their canonical run/zero descriptions, counts each description once with its finite-field projective-line weight, and compares these counts through \(n=17\) at six field orders. This is a finite consistency check; the proof for every \(n\) and \(q\) is the preceding classification and automaton calculation. Successful execution prints `VERIFY_OK`.

## Relationship to prior work

Rossmann's 2021 preprint (published 2022) introduces the graphical groups and Lie algebras, identifies their centralizers with kernels of edge-commutator maps, and derives conjugacy-class *size* and orbit enumerations via specialized adjacency modules. The present invariant instead counts **how many distinct centralizer subspaces occur**; counting coefficient vectors or centralizer dimensions does not answer that question because many vectors have exactly the same kernel. Godoy Molina and Lagos (2023) study graph-labeled two-step Lie algebras and their ideals/derivations, not this distinct-centralizer census. Existing exact all-graph adjoint rank distributions similarly distinguish element counts by kernel dimension, not equality of kernels. The finite-state quotient and rational function here are the new, narrower contribution. Published comparisons of class-two graphical-group character ranks, filiform adjoint spectra, and centralizers of Kronecker associative path algebras concern different invariants. Searches for synonymous formulations did not identify this exact generating function; comprehensive priority verification remains open.

## Limitations

The rational form is proved only for paths with individually independent central edge brackets; reusing an edge label or adding graph chords changes the kernel-equivalence structure. Counts are for distinct embedded Lie subalgebras, not isomorphism classes or a lattice-isomorphism theorem. A relevant earlier paper could encode the same finite-state count implicitly, so publication priority requires independent assessment. All computerized enumerations are finite checks and are not substitutes for the automaton proof.

## References

1. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564v1, publicly posted July 12, 2021; *Bull. Lond. Math. Soc.* 54 (2022), 1923–1943, DOI 10.1112/blms.12665. See Section 2.4 and Lemma 3.2.
2. M. Godoy Molina and D. Lagos, *Lie algebras associated with labeled directed graphs*, arXiv:2308.00272v1, first public August 1, 2023; see Sections 2–5.
3. A. Shamsaki, A. Erfanian, and M. Parvizi, *On the commutativity degree of a finite-dimensional Lie algebra*, arXiv:2406.10064v1, publicly posted June 14, 2024.
