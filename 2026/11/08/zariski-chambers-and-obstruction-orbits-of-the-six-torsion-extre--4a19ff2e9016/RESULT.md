# Zariski chambers and obstruction orbits of the six-torsion extremal elliptic surface

## Finding
Let \(X\) be the unique smooth complex extremal rational elliptic surface with Kodaira fibres \(I_6+I_3+I_2+I_1\). Its Mordell--Weil group is \(\mathbb Z/6\mathbb Z\). Label the six sections \(S_j\) for \(j\in\mathbb Z/6\mathbb Z\), and label the components in each reducible fibre by \(C_{n,i}\), with \(n\in\{6,3,2\}\) and \(i\in\mathbb Z/n\mathbb Z\), so that \(S_j\) meets precisely \(C_{n,j\bmod n}\).

The **complete negative-curve set** has seventeen members: six sections of square \(-1\) and eleven multiplicative-fibre components of square \(-2\). For any subset \(T\) of these curves, let \(T\) be an *admissible support* when its intersection matrix is negative definite (also allowing the empty subset). All inadmissible supports contain one of precisely **seventy-two inclusion-minimal forbidden supports**, represented by exactly **fifteen orbits** under simultaneous cyclic translation \(j\mapsto j+1\). Their orbit sizes comprise three size-one orbits, one size-three orbit, and eleven size-six orbits. All seventy-two minimal forbidden principal matrices are singular of corank one.

The Zariski-chamber support polynomial is
\[
\boxed{Z_X(t)=1+17t+135t^2+637t^3+1929t^4+3852t^5+5039t^6+4111t^7+1836t^8+296t^9.}
\]
Hence \(X\) has exactly \(17853\) Zariski chambers, including the nef chamber. The maximal possible support size is nine, attained by exactly \(296\) chambers.

## Assumptions and scope
Everything is over \(\mathbb C\); the surface is relatively minimal, smooth, and equipped with its elliptic fibration and a chosen zero section. The fibre labels are cyclic labels, unique up to reversal. A chamber is counted by the support of the negative part of a Zariski decomposition of a big real divisor. Its cardinality is not a count of connected components of the support. The support polynomial includes the nef chamber with coefficient one in degree zero.

The following table specifies all fifteen orbit representatives. In a row, apply \(S_j\mapsto S_{j+1}\) and \(C_{n,i}\mapsto C_{n,i+1}\) simultaneously, with indices reduced modulo \(6\) or \(n\), and collect distinct resulting sets. No other forbidden minimal sets exist.

| Representative | Minimal forbidden set |
|---:|---|
| 1 | \(\{C_{6,0}, C_{6,1}, C_{6,2}, C_{6,3}, C_{6,4}, C_{6,5}\}\) |
| 2 | \(\{C_{3,0}, C_{3,1}, C_{3,2}\}\) |
| 3 | \(\{C_{2,0}, C_{2,1}\}\) |
| 4 | \(\{C_{6,0}, C_{6,1}, C_{6,5}, S_{0}\}\) |
| 5 | \(\{C_{6,0}, C_{3,0}, S_{0}\}\) |
| 6 | \(\{C_{6,0}, C_{2,0}, S_{0}\}\) |
| 7 | \(\{C_{3,0}, C_{2,0}, S_{0}\}\) |
| 8 | \(\{C_{6,0}, C_{6,1}, S_{0}, S_{1}\}\) |
| 9 | \(\{C_{3,0}, C_{3,1}, S_{0}, S_{1}\}\) |
| 10 | \(\{C_{6,0}, C_{6,1}, C_{6,2}, S_{0}, S_{2}\}\) |
| 11 | \(\{C_{6,0}, C_{6,2}, C_{6,3}, C_{6,4}, C_{6,5}, S_{0}, S_{2}\}\) |
| 12 | \(\{C_{3,0}, C_{3,2}, S_{0}, S_{2}\}\) |
| 13 | \(\{C_{2,0}, S_{0}, S_{2}\}\) |
| 14 | \(\{C_{6,0}, C_{6,1}, C_{6,2}, C_{6,3}, S_{0}, S_{3}\}\) |
| 15 | \(\{C_{3,0}, S_{0}, S_{3}\}\) |

## Proof
**1. The curve inventory.** The fibre configuration and group \(\mathbb Z/6\mathbb Z\) are established in the Miranda--Persson classification, as recorded in Schütt--Shioda, Section 9.5. For a rational elliptic surface, the canonical divisor is numerically \(-F\), where \(F\) is a fibre, and \(\chi(\mathcal O_X)=1\). If an irreducible curve \(D\) has negative square, adjunction gives \(2p_a(D)-2=D^2-F\cdot D\). If \(F\cdot D\ge1\), the inequality \(p_a(D)\ge0\) forces \(F\cdot D=1\), \(D^2=-1\), and \(p_a(D)=0\); thus \(D\) is a section. Otherwise \(F\cdot D=0\), so \(D\) is vertical and is a component of a reducible fibre (irreducible whole fibres have square zero). Each component of the three reducible fibres has square \(-2\). The six Mordell--Weil elements therefore account for every negative curve, exactly \(6+3+2+6=17\).

**2. All intersections.** In the fibre \(I_n\), the components \(C_{n,0},\ldots,C_{n,n-1}\) form a cycle with adjacent intersection one, except that the two components of \(I_2\) meet twice. Different fibres are disjoint. Each section has square \(-1\). To find how the sections intersect, note that the component-group homomorphism is injective on torsion and use the explicit height formula of Schütt--Shioda, Section 11.8. An order-six generator must meet indices \((1,1,1)\) in the three fibres \(I_6,I_3,I_2\), up to reversal: only these indices have local self-corrections adding to \(2\) and component-group order six. Therefore \(S_j\) meets \(C_{n,j\bmod n}\). For \(j=1,\ldots,5\),
\[
\sum_{n\in\{6,3,2\}} \frac{(j\bmod n)(n-(j\bmod n))}{n}=2,
\]
so the height-zero identity \(0=2+2(S_j\cdot S_0)-2\) gives \(S_j\cdot S_0=0\). For any distinct nonzero \(i,j\in\{1,\ldots,5\}\),
\[
\sum_{n\in\{6,3,2\}}\frac{\min(i\bmod n,j\bmod n)\bigl(n-\max(i\bmod n,j\bmod n)\bigr)}{n}=1.
\]
The mixed height-zero formula \(0=1-(S_i\cdot S_j)-1\) gives \(S_i\cdot S_j=0\). Thus all sections are pairwise disjoint.

**3. Exact negative-definiteness criterion.** Put \(A=-(D_i\cdot D_j)_{0\le i,j<17}\), ordering the fibre components by \(I_6,I_3,I_2\), followed by the sections \(S_0,\ldots,S_5\). The diagonal of \(A\) consists of eleven \(2\)'s and six \(1\)'s. Its only nonzero off-diagonal entries are \(-1\) between adjacent components of the \(I_6\) and \(I_3\) cycles, \(-2\) between the two \(I_2\) components, and \(-1\) between \(S_j\) and each \(C_{n,j\bmod n}\). The complete integer matrix is reconstructed without external files by the attached verifier.

Every subset of the seventeen indices has been examined in increasing integer bit-mask order. The empty matrix is declared positive definite. A nonempty principal matrix can be positive definite only if every one-element deletion is positive definite; when the latter condition holds, positive definiteness is equivalent to positivity of its determinant by the Schur-complement criterion. Exact fraction-free integer elimination supplies the determinant. Hence the classification is exhaustive for all \(2^{17}=131072\) subsets, not a statistical sample. It yields precisely \(72\) inclusion-minimal bad subsets. The determinant of each minimal bad principal matrix is zero, and one deletion is positive definite, so each is singular of corank exactly one.

**4. Orbit certification and chamber counts.** Translation by the six-torsion generator preserves every intersection and permutes the indices as above. Taking the cyclic orbit of each table row produces exactly \(72\) distinct supports, in orbit-size distribution \(3\cdot1+1\cdot3+11\cdot6\). An independent mask-avoidance pass over all \(131072\) subsets proves that a support is positive definite if and only if it contains none of the \(72\) forbidden supports. The coefficient of \(t^r\) is then the count of admissible subsets of cardinality \(r\). The displayed polynomial is the resulting complete count.

Finally, Bauer--Funke--Neumann, Proposition 1.1, identifies non-nef Zariski chambers with the nonempty negative-definite supports of negative curves; the empty support supplies the nef chamber. The numerical support polynomial therefore equals the Zariski-chamber polynomial. A negative-definite subspace of \(\operatorname{NS}(X)_\mathbb R\) has dimension at most nine (the rational elliptic surface has signature \((1,9)\)), agreeing with the verified top degree.

## Verification
Run \(\texttt{python3 verify_chambers.py}\) with a standard Python 3 installation. The standalone code reconstructs all \(17\) curves, all their intersections, and the fifteen orbit prototypes; it checks all \(131072\) masks. The first method performs exact Bareiss determinant tests with hereditary positive-definiteness pruning, and the second tests explicit forbidden-orbit avoidance on every mask. It asserts equality of the two classifications and every polynomial coefficient. The reproduced program output is \(\texttt{verify_chambers.out}\).

The exact computation is a finite proof of the support census conditional on the mathematically established intersection matrix. The geometric argument supplies that matrix and shows it includes all negative curves. The verifier is not a computer-formalized proof of the geometric lemmas.

## Relationship to prior work
Schütt--Shioda, *Elliptic Surfaces* (arXiv:0907.0298, Section 9.5 and Section 11) supply the fibre/Mordell--Weil classification and height formulas. Jarvis--Lang--Ricks, *Integral Models of Extremal Rational Elliptic Surfaces* (arXiv:0908.1831, Section 1.I and Appendix A), supply models and the same fibre configuration. Neither cited section provides this chamber census or the minimal forbidden-support hypergraph. Bauer--Funke--Neumann (arXiv:0912.0958, Proposition 1.1) supplies the general bijection between chambers and negative-definite configurations. Bauer--Schmitz (arXiv:1204.4373, Section 1) supplies a general counting algorithm, applied there to different surfaces. General computability is prior work; this specific seventeen-curve support classification, its fifteen symmetry orbits, and its evaluated polynomial are the present claim.

## Limitations
The calculation concerns the unique complex fibre type \(I_6+I_3+I_2+I_1\) and the support-size statistic; it does not classify shapes of the chamber cones, volume polynomials, or walls under birational modifications. It does not assert a corresponding statement in residue characteristics two or three, where the fibre configuration degenerates. It does not claim an exhaustive search of unindexed historical tables, so historical priority remains provisional. The exact verifier is exhaustive only after the geometric negative-curve inventory has been proved.

## References
1. M. Schütt and T. Shioda, *Elliptic Surfaces*, arXiv:0907.0298 (first public version July 2, 2009), Sections 7, 9, 11. https://arxiv.org/abs/0907.0298
2. T. J. Jarvis, W. E. Lang, and J. R. Ricks, *Integral Models of Extremal Rational Elliptic Surfaces*, arXiv:0908.1831 (August 13, 2009), Section 1.I and Appendix A. https://arxiv.org/abs/0908.1831
3. T. Bauer, M. Funke, and S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958 (December 4, 2009), Proposition 1.1. https://arxiv.org/abs/0912.0958
4. T. Bauer and D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373 (April 19, 2012), Section 1. https://arxiv.org/abs/1204.4373
