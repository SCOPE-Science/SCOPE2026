# Primitive chirality and zero-winding sectors of the ternary rotor-symbol surrogate

## Finding
Consider the cyclic, loop-free, three-symbol shift \(X=\{x\in\{0,1,2\}^{\mathbb Z}:x_i\ne x_{i+1}\}\), the three-symbol part of the no-repetition surrogate proposed for chaotic three-rotor coincidences. For a cyclic point of length \(n\), let each symbol-changing edge have increment \(+1\) if \(x_{i+1}-x_i\equiv1\pmod3\), and \(-1\) otherwise, and define its **winding** \(w=\frac13\sum_{i=0}^{n-1}\epsilon_i\in\mathbb Z\). An orbit is **primitive** when its least shift period is \(n\); its cyclic shift orbit is **achiral** when the reversed word is a rotation of the original.

For every integer \(n\ge2\), let \(T_n\), \(Z_n\), and \(A_n\) count, respectively, all primitive length-\(n\) cyclic orbits, primitive zero-winding orbits, and primitive achiral orbits. With \(\mu\) the arithmetic Möbius function, these three complete all-length censuses are
\[
T_n=\frac1n\sum_{d\mid n}\mu(n/d)\bigl(2^d+2(-1)^d\bigr),\quad
Z_n=\frac3n\sum_{\substack{d\mid n\\2\mid d}}\mu(n/d)\binom d{d/2},\quad
A_n=\frac32\sum_{\substack{d\mid n\\2\mid d}}\mu(n/d)2^{d/2}.
\]
All achiral primitive orbits have zero winding. Thus the number of **chiral zero-winding** primitive orbits is exactly \(Z_n-A_n\), while the number of chiral nonzero-winding primitive orbits is \(T_n-Z_n\). Zero winding, therefore, is not equivalent to reversal symmetry.

**Sharp onset:** for \(n=2,4,6\), \(Z_n=A_n\); the first chiral primitive zero-winding orbits occur at \(n=8\), where \((T_8,Z_8,A_8)=(30,24,18)\), so exactly six chiral zero-winding orbits exist. For odd \(n\), both zero-winding and achiral counts vanish. Through even lengths tending to infinity,
\[
\frac{A_n}{Z_n}\sim\frac12\sqrt{\frac\pi2}\,n^{3/2}2^{-n/2},
\]
so within the zero-winding sector, almost every sufficiently long primitive cyclic orbit is chiral.

## Assumptions and scope
Symbols are named, not identified under permutations. A cyclic orbit identifies rotations only, not reversals. Winding is a *combinatorial* integer on the closed walks of the three-vertex complete loop-free directed graph, not an asserted conserved physical angular momentum. The result is about all abstract periodic points in the proposed symbolic surrogate \(X\). The motivating authors explicitly caution that their surrogate adjacency matrix **does not describe actual periodic rotor trajectories**; the formulas make no claim about physical orbit existence, realization, or stability. The two-sided shift is used solely to define cyclic symbolic orbits.

## Proof
Set \(M=J-I\), the \(3\times3\) adjacency matrix of the complete directed graph without loops. Its eigenvalues are \(2,-1,-1\), so the number \(F_n\) of indexed cyclic words of length \(n\) is
\[F_n=\operatorname{tr}(M^n)=2^n+2(-1)^n.\]
Every indexed cyclic word has a unique smallest divisor period. Möbius inversion gives \(P_n=\sum_{d\mid n}\mu(n/d)F_d\) indexed primitive words, and a primitive necklace has exactly \(n\) indexed representatives, proving the formula for \(T_n=P_n/n\).

For a cyclic word, encode each directed edge by its \(+1\) or \(-1\) increment in \(\mathbb Z/3\mathbb Z\). A prescribed increment sequence and initial symbol uniquely determine the entire word; the closing condition is \(\sum\epsilon_i\equiv0\pmod3\). Zero winding is the stronger condition \(\sum\epsilon_i=0\). Hence it is possible only when \(n\) is even; then exactly \(\binom n{n/2}\) increment strings work, with three choices of initial symbol. Thus the indexed zero-winding count is \(F_n^{(0)}=3\binom n{n/2}\) if \(n\) is even and zero otherwise. Repeating a shorter cyclic word multiplies its integer winding by the repetition factor, so zero winding is preserved *and reflected* by primitive-period decomposition. Möbius inversion and division by \(n\) establish \(Z_n\).

Consider literal reversal of symbol order. A reversal-invariant cyclic orbit contains a word fixed by some dihedral reflection. If \(n\) is odd, every axis passes through the midpoint of an edge and would identify that edge's two endpoints, which is impossible in this shift. For even \(n\), the \(n/2\) edge-axis reflections similarly fix no words, while each of the \(n/2\) vertex-axis reflections fixes exactly \(3\cdot2^{n/2}\) indexed cyclic words: choose the first vertex color (three options), choose successive colors along the half-cycle (two options per edge), and reflect the path. Under period reduction, a word fixed by the specific axis \(i\mapsto-i\) descends to a word fixed by that axis modulo its least divisor period. Möbius inversion therefore gives the number \(R_n=3\sum_{d\mid n,\,2\mid d}\mu(n/d)2^{d/2}\) of *primitive indexed* words fixed by a specified vertex reflection. A primitive word cannot be fixed by two distinct reflections (their product would be a nonidentity rotation). Thus the number of primitive indexed words fixed by some reflection is \((n/2)R_n\). Dividing by \(n\) yields \(A_n=R_n/2\).

Reversing a closed walk reverses the sign of every directed increment, and rotating does not alter their sum. Hence achirality forces \(w=-w\), or \(w=0\). Direct substitutions give the census at lengths \(2,4,6,8\) and the sharp first occurrence at eight. For even \(n\to\infty\), the leading divisor terms yield \(A_n=(3/2)2^{n/2}(1+o(1))\) and \(Z_n=(3/n)\binom n{n/2}(1+o(1))=3\sqrt{2/\pi}\,2^nn^{-3/2}(1+o(1))\). Their quotient is the stated asymptotic. Proper-divisor terms are exponentially smaller than the top terms, including at small prime divisor two. This completes the proof.

## Verification
Run the standalone Python 3 standard-library checker `check.py`. It enumerates every admissible indexed cyclic word for lengths \(2\) through \(12\), obtains distinct primitive rotation classes, identifies reversal-symmetric classes, computes signed winding, and independently compares all three resulting counts with the closed formulas. The checker makes only finite confirmations; the proof above establishes all \(n\ge2\). At \(n=8\), all three exact class counts are also reported.

## Relationship to prior work
Krishnaswami and Rameshan (2026, Section 6, especially their adjacency matrix (26)) propose the no-zero, no-repeated-pair grammar for a surrogate of globally chaotic three-rotor coincidence codes and establish its word-complexity interpretation; they neither enumerate all abstract primitive cyclic paths by winding and literal reversal nor assert that all those paths are realized by physical rotor trajectories. The present calculation adds a joint primitive-period/chirality/zero-winding census and identifies the sharp first zero-winding chiral length. The generic tools of Möbius inversion, dihedral Burnside counting, and three-coloring are classical and are not claimed as new. Comparisons against nearby rotor-symbol, ternary-word symmetry, and winding-sector classifications found no direct all-length triple census; a pre-existing equivalent in classical necklace literature cannot be excluded.

## Limitations
This is a combinatorial theorem for the full three-symbol adjacency surrogate, not a theorem about invariant sets, periods or trajectories of the physical three-rotor Hamiltonian system. Literal symbolic reversal is not a substitute for a proof of physical time-reversal correspondence. Historical originality is provisional within the searched literature. The finite checker cannot certify the infinite theorem; the complete argument is analytic/combinatorial. No independent mathematical audit has been performed.

## References
1. G. S. Krishnaswami and A. Rameshan, *Symbol sequences from three-rotor coincidences and their word-complexity* (2026), arXiv:2606.25766, first public June 24, 2026. https://arxiv.org/abs/2606.25766 ; full author-supplied text: https://www.researchgate.net/publication/408047853_Symbol_sequences_from_three-rotor_coincidences_and_their_word-complexity . See Section 6, equation (26), and its explicit caveat on physical periodic orbits.
2. Classical tools: Möbius inversion for primitive periodic points; Burnside's lemma for dihedral actions; the transfer matrix of proper colorings of a cycle. These methods are standard background, not priority claims.
