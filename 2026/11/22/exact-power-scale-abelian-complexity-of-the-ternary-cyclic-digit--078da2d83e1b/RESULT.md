# Exact power-scale Abelian complexity of the ternary cyclic digit-two counter

## Finding
Let \(\sigma\) be the three-uniform substitution on \(\{0,1,2\}\) defined by \(\sigma(0)=001\), \(\sigma(1)=112\), and \(\sigma(2)=220\). Its one-sided fixed point is \(s=\sigma^{\omega}(0)\). Let \(b_i=1\) precisely when \(s_i=0\), and let \(\rho_b(n)\) be the number of distinct Parikh vectors represented by contiguous length-\(n\) factors of the binary word \(b\). For every integer \(h\ge0\),
\[
\boxed{\rho_b(3^{2h})=3^{h+1}-1,\qquad \rho_b(3^{2h+1})=5\cdot3^h-1.}
\]
Equivalently, for every \(k\ge0\),
\[
\rho_b(3^k)=3^{\lceil k/2\rceil}+2\cdot3^{\lfloor k/2\rfloor}-1.
\]
The first values are \(2,4,8,14,26,44,80\) for \(k=0,\ldots,6\). The power-scale growth exponent is exactly \(1/2\), with distinct even- and odd-scale coefficients. The ternary fixed point has the digit description \(s_i\equiv \#\{\text{digits }2\text{ in the base-three expansion of }i\}\pmod 3\). Thus \(b\) indicates divisibility by three of the number of ternary digits equal to two.

## Assumptions and scope
All factors are contiguous and all words are indexed from zero. Binary Abelian equivalence at fixed length means equality of the number of ones. The substitution is prolonged at zero, and the claimed identities hold for every nonnegative integer exponent, without finite cutoff. They concern only the lengths \(3^k\); no complete formula for other lengths, and no regularity or nonregularity classification of the full complexity sequence, is asserted.

## Proof
**1. The substitution and adjacent pairs.** Each letter occurs in the fixed point. The internal factors of \(\sigma(a)=aa(a+1\bmod3)\) contain \(aa\) and \(a(a+1)\). Across the boundary of \(\sigma(aa)\) there is \((a+1)a\). Every \(aa\) occurs, so all nine ordered two-letter factors occur. Writing \(U_k(a)=\sigma^k(a)\), these blocks have common length \(Q=3^k\). The letter-count vector for \(U_k(0)\) is \(v_k=(v_{k,0},v_{k,1},v_{k,2})\), with \(v_0=(1,0,0)\) and
\[
v_{k+1}=(2I+R)v_k,\qquad (Rv)_i=v_{i-1\bmod3}.
\]
The three vectors of letter counts for \(U_k(a)\) are cyclic permutations of \(v_k\).

**2. The weighted extremum lemma.** Fix any real-valued letter weight \(w\), extended additively to words. Define \(W_k(a)=w(U_k(a))\) and let \(H_k\) be the largest weight of a length-\(3^k\) factor of \(s\). We show, for every \(k\ge0\),
\[
H_{k+1}=H_k+2\max_{a}W_k(a).\tag{1}
\]
For the upper bound, any length-\(3Q\) factor is either aligned to \(Q\)-blocks, giving weight at most \(3\max W_k\le H_k+2\max W_k\), or is unaligned. In the latter case it comprises a suffix and a prefix of total length \(Q\), together with exactly two complete \(Q\)-blocks. All ordered block-letter pairs occur in \(s\), so the concatenation of the two partial pieces is also a factor of length \(Q\) somewhere in \(s\); its weight is at most \(H_k\). The complete pieces contribute at most \(2\max W_k\).

For the matching lower bound, simultaneously maintain this induction invariant: for a maximizing letter \(c\) of \(W_k\), some maximum-weight length-\(Q\) factor occurs across or within one of \(U_k(c-1)U_k(c)\) and \(U_k(c)U_k(c+1)\), with cyclic indices. At \(k=0\), a letter attaining the maximum gives the assertion. If \(W_k(c)\ge W_k(a)\) for every \(a\), then
\[
W_{k+1}(c)-W_{k+1}(c+1)
=(W_k(c)-W_k(c+1))+(W_k(c)-W_k(c-1))\ge0,
\]
so a maximum of \(W_{k+1}\) can be selected from \(\{c-1,c\}\). Moreover,
\[
U_{k+1}(c-1)U_{k+1}(c)
=U_k(c-1)^2U_k(c)^3U_k(c+1).
\]
Extend the indicated old maximum-weight factor by exactly two complete copies of \(U_k(c)\), within this displayed block concatenation. The resulting length-\(3Q\) factor has weight \(H_k+2W_k(c)\) and lies across the level-\(k+1\) boundary. The pair is adjacent to either maximizing choice \(c-1\) or \(c\), preserving the invariant and establishing equality in (1). The argument remains valid if the original factor is wholly within one block or attains an endpoint.

**3. Recurrence for Abelian complexity.** Apply (1) with weights \(w(a)=\mathbf1_{a=0}\) and \(w(a)=-\mathbf1_{a=0}\). Write \(A_k\) and \(B_k\) for, respectively, the maximum and minimum number of ones in length-\(3^k\) factors of \(b\). Because the three letter-count vectors are cyclic permutations of \(v_k\),
\[
A_{k+1}-A_k=2\max_i v_{k,i},\qquad
B_{k+1}-B_k=2\min_i v_{k,i}.
\]
The number of ones changes by at most one when a binary window shifts by one position. Taking a finite sequence of windows from an occurrence of the minimum to an occurrence of the maximum shows that every intervening count occurs. Consequently \(\rho_b(3^k)=A_k-B_k+1\), and with \(g_k=\max_i v_{k,i}-\min_i v_{k,i}\),
\[
\rho_b(1)=2,\qquad \rho_b(3^{k+1})-\rho_b(3^k)=2g_k.\tag{2}
\]

**4. The exceptional spectral collapse.** Since \(R^3=I\) and \(J=I+R+R^2\) sends every vector to its coordinate sum times \((1,1,1)\),
\[
(2I+R)^2=4I+4R+R^2=3(I+R)+J.
\]
The centered vector \(\bar v_k=v_k-3^{k-1}(1,1,1)\) (the exponent \(k-1\) also makes sense at \(k=0\) as a rational coordinate) is annihilated by \(J\). On the centered subspace, \(I+R=-R^2\), hence
\[
\bar v_{k+2}=-3R^2\bar v_k.
\]
Cyclic permutation and addition of a constant do not change the maximum-minus-minimum spread; multiplication by \(-3\) multiplies it by three. Thus \(g_{k+2}=3g_k\) for all \(k\ge0\). Directly \(v_0=(1,0,0)\) and \(v_1=(2,1,0)\), giving \(g_0=1\), \(g_1=2\). It follows that
\[
g_{2h}=3^h,\qquad g_{2h+1}=2\cdot3^h.
\]
Substitute these identities into the telescoping sum (2):
\[
\rho_b(3^{2h})=2+2\sum_{j=0}^{h-1}(g_{2j}+g_{2j+1})
=2+6\sum_{j=0}^{h-1}3^j=3^{h+1}-1,
\]
and \(\rho_b(3^{2h+1})=\rho_b(3^{2h})+2g_{2h}=5\cdot3^h-1\). The power-scale exponent follows directly. The digit description follows from the three branches \(s_{3i}=s_i\), \(s_{3i+1}=s_i\), \(s_{3i+2}=s_i+1\pmod3\). \(\square\)

## Verification
The included `verify_direct.py` generates the substitution independently and counts zeros in every possible level-\(k\) two-block factor window for \(k=0,\ldots,6\), comparing its observed extrema and complexity to the closed formulas. The independent `verify_power3.py` builds an exact max-plus prefix-difference recurrence and checks an inductive twelve-residue affine invariant over rational coefficients, including all real scale parameters \(T\ge1\). The saved stdout files show both scripts passing. These auxiliary calculations check the proof and supply an independent exact-arithmetic derivation; the infinite conclusion follows from the four human-readable steps above, not finite sampling alone.

## Relationship to prior work
Allouche, Rampersad, Rigo, Shallit, and Stipulanti [1] study the three-letter cyclic substitution with three repeated letters before the successor, and ask about additional repetition counts. A related published extension [2] establishes nonregularity for repetition counts at least four and explicitly treats the count-three example as known. Its general weighted-factor technique is a close ancestor of Step 2; that technique is not asserted new here. The present result concerns the missing **two repeats and three-letter cycle** and gives a closed exact rational-integer formula at every power of three, using the resonant identity on the mean-zero subspace.

A related two-repeat result [3] uses **two letters**, with \(0\mapsto001\), \(1\mapsto110\), and obtains logarithmic rather than square-root power-scale Abelian complexity. That is a distinct binary fixed point: the present ternary letter \(2\mapsto220\) and its three-cycle coding are essential. Parikh-collinear morphism results [4] require a rank-one incidence matrix, whereas \(2I+R\) has full rank three. These comparisons concern mathematical statements and implications, rather than titles alone.

## Limitations
Only the geometric subsequence of lengths \(3^k\) is classified. No arbitrary-length exact complexity formula, or decision about automaticity or regularity of the full complexity sequence, follows. The weighted-factor induction resembles published methods; the novelty assessment concerns the previously untreated resonance parameter and its explicit exact formula, not a new general technique. Previously unindexed equivalents are possible, and independent scientific and historical-priority review have not occurred.

## References
[1] J.-P. Allouche, N. Rampersad, M. Rigo, J. Shallit, M. Stipulanti, *An example of an automatic sequence with non-regular abelian complexity*, arXiv:2610.03837v1 (first public 2026-10-02), https://arxiv.org/abs/2610.03837.

[2] *An infinite ternary-morphism family with nonregular binary abelian complexity*, published research record (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-infinite-ternary-morphism-family-with-nonregular-binary-abeli--f292807a24e1.

[3] *Sharp Abelian-complexity envelope for ternary digit-two parity*, published research record (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-abelian-complexity-envelope-for-ternary-digit-two-parity--ea6d16472081.

[4] M. Rigo, M. Stipulanti, M. A. Whiteland, *Automatic Abelian Complexities of Parikh-Collinear Fixed Points*, arXiv:2405.18032 (2024), https://arxiv.org/abs/2405.18032.
