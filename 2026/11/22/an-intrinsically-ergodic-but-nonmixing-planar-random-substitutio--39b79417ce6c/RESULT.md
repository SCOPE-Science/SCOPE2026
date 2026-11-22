# An intrinsically ergodic but nonmixing planar random substitution with entropy \(\frac{\log 2}{3}\)

## Finding

Let \(\vartheta\) be the binary \(2\times2\) random block substitution
\[
\vartheta(a)=\left\{
\begin{pmatrix}a&a\\a&0\end{pmatrix},
\begin{pmatrix}a&a\\a&1\end{pmatrix}
\right\},\qquad a\in\{0,1\}.
\]
Let \(X_\vartheta\subset\{0,1\}^{\mathbb Z^2}\) be the shift whose finite patterns are precisely the subpatterns of some finite iterated substitution block. Then:

1. Its planar topological entropy per site is exactly \(h_{\mathrm{top}}(X_\vartheta)=\frac13\log2\).
2. The \(\mathbb Z^2\)-shift on \(X_\vartheta\) has a **unique invariant probability measure of maximal entropy** \(\mu\).
3. With respect to \(\mu\), the entire dyadic hierarchy alignment is a measurable factor onto the Haar translation action on \(\mathbb Z_2^2\). In particular, \(\mu\) is not mixing under the horizontal unit shift (indeed, that shift has a nonconstant eigenfunction with eigenvalue \(-1\)).
4. Periodic configurations are dense in \(X_\vartheta\).

The substantive conjunction is exact positive entropy, uniqueness of the maximizing invariant measure, a recoverable nonmixing dyadic phase, and dense periodic configurations in one elementary planar random substitution. The entropy identity and periodic-density property are not asserted as general new principles.

## Assumptions and scope

The substitution is applied synchronously and **independently at each parent letter**, with one free bottom-right child. Allowed substitutions at every stage are both given choices; stochastic probabilities enter only in the construction of the invariant maximizing law. Blocks are indexed by \([0,2^n-1]^2\). The shift is the full translation action of \(\mathbb Z^2\). All entropies are natural-logarithmic, area-normalized entropies.

For \(a\in\{0,1\}\), let \(W_n(a)\) be the set of size-\(2^n\) square blocks obtained after exactly \(n\) substitutions from the single symbol \(a\). By the *root* of an aligned supertile we mean its unique depth-\(n\) ancestor symbol, not its upper-left entry alone.

A dyadic alignment is \(\alpha=(\alpha_1,\alpha_2)\in\mathbb Z_2^2\): at level \(n\), the supertile boundaries lie in the cosets \(\alpha_j+2^n\mathbb Z\) of the two lattice coordinates. The sign of the shift action on \(\alpha\) depends on whether left or right translation is used, but the eigenvalue statement is unchanged.

## Proof

**1. Exact supertile count.** A block in \(W_{n+1}(a)\) splits into four aligned members of \(W_n\), whose roots are \((a,a;a,b)\), with arbitrary \(b\in\{0,1\}\). Inductively \(W_n(0)\cap W_n(1)=\varnothing\): after recovering the four subblock roots, three recover \(a\). The decomposition is unique because the four positions are fixed. If \(q_n=|W_n(a)|\), symmetry and the free root give
\[
q_0=1,\qquad q_{n+1}=2q_n^4,\qquad
q_n=2^{(4^n-1)/3}.
\]
The two-root supertile language has exactly \(2q_n\) elements at level \(n\).

**2. Entropy.** Each level-\(n\) block occurs in \(X_\vartheta\). Thus, along squares of side \(2^n\), the entropy lower bound is
\[
\lim_{n\to\infty}\frac{\log(2q_n)}{4^n}=\frac13\log2.
\]
Conversely, every \(N\times N\) legal patch has some level-\(n\) alignment: this follows first for patches of iterated supertiles, then for their closure by compactness of the finite set of alignments. Given that alignment, at most \((\lceil N/2^n\rceil+2)^2\) level-\(n\) supertiles meet the patch. Therefore its number of possibilities is at most
\[
4^n(2q_n)^{(\lceil N/2^n\rceil+2)^2}.
\]
Let \(N\to\infty\) and then \(n\to\infty\). The resulting upper bound agrees with the lower bound.

**3. A phase extension and its maximizing law.** Let \(\widetilde X\) consist of pairs \((x,\alpha)\) with a compatible nested supertile decomposition at every level. Compactness gives a nonempty fiber over every \(x\in X_\vartheta\). The lattice shifts act on \(\alpha\in\mathbb Z_2^2\) by addition or subtraction of the lattice vector. Any invariant probability on \(\widetilde X\) has Haar phase marginal, since the integer subgroup is dense in \(\mathbb Z_2^2\). As this odometer has zero entropy, adjoining the phase does not change the measure entropy of the configuration factor.

Fix the level-one phase \(p=\alpha\bmod 2\). In each aligned \(2\times2\) square, the three equal entries determine a coarse field \(Y\in X_\vartheta\); the bottom-right entries form an unrestricted binary field \(B\). This is a coordinatewise bijection between the phase-\(p\) configurations and pairs \((Y,B)\). On the subaction by \(2\mathbb Z^2\), these two fields transform by the ordinary unit translations. With \(h\) denoting entropy per fundamental lattice site, every invariant lift \(\widetilde\nu\) satisfies
\[
4h(\widetilde\nu)=\frac14\sum_{p\in\{0,1\}^2}h(Y,B\mid p)
\le h_{\mathrm{top}}(X_\vartheta)+\log2
=4h_{\mathrm{top}}(X_\vartheta).
\]
The marginal entropy bound applies separately to every phase. The residual phase \((\alpha-p)/2\) is a zero-entropy factor of the coarse system.

There exists an invariant law attaining equality. Choose \(\alpha\) Haar-uniform and, independently, fair bits for every free bottom-right corner of every square in the nested hierarchy. A specified site is never assigned a corner bit with probability \(\lim_{n\to\infty}(3/4)^n=0\); hence each site has an almost surely well-defined symbol. This law is translation-invariant because translation permutes the Haar phase and the identically distributed independent corner variables. Its coarse field has the same law, and its level-one corner field consists of iid fair bits independent of the coarse field and the residual phase. Therefore its entropy \(h\) obeys \(4h=h+\log2\), giving \(h=\log2/3\).

**4. Uniqueness.** Let \(\widetilde\nu\) be any maximal-entropy invariant lift. Equality in the preceding entropy bound holds in each of the four phase fibers. After adjoining the zero-entropy residual phase, the conditional entropy rate of \(B\), given the entire coarse field and residual phase, is \(\log2\), its maximum. Consequently \(B\) is an iid fair binary field independent of the coarse field and residual phase. For completeness, if a finite set of corner variables \(B_F\) were not uniformly independent of some finite environment observation \(E_G\), then \(H(B_F\mid E_G)<|F|\log2\). Placing disjoint translates of \(F\cup G\) in large squares and applying conditional entropy subadditivity would reduce the limiting conditional entropy rate strictly below \(\log2\), a contradiction. The same reasoning includes finitely many digits of the residual phase in \(E_G\).

Iterate the same argument on the coarse field, which must itself have maximal entropy. It follows that, conditional on the full Haar phase, every free-corner variable at every hierarchical level is independently fair, including across levels. For a fixed finite set of physical sites, the probability that any site remains inherited after \(n\) levels tends to zero by the \((3/4)^n\) estimate. Thus these finite-dimensional distributions are uniquely determined. There is only one maximal-entropy invariant probability after projection to \(X_\vartheta\), namely \(\mu\).

**5. Almost-sure phase recovery and nonmixing.** The correct level-one phase forces every aligned \(2\times2\) square to have at least three equal symbols. For each of the other three phase offsets, the explicit level-two supertile witness test has exactly eight violating blocks among the thirty-two possible blocks of **each** root value. A violation is a fully interior \(2\times2\) square with exactly two zeros and two ones. In row-string notation, the valid root-zero four-by-four block `0000/0000/0011/0010` witnesses the offsets \( (0,1)\) and \( (1,0)\); `0000/0100/0011/0010` witnesses \( (1,1)\). Their bitwise complements serve as root-one witnesses. Thus the phase obstruction is also visible without trusting the numerical witness count. Given the root field of disjoint level-two supertiles under \(\mu\), their five internal corner bits are independent and fair. Each wrongly aligned phase therefore has a violation in each such supertile with conditional probability \(1/4\), independently across disjoint tiles. Almost surely every wrong phase fails somewhere. Hence the true parity phase is determined measurably by \(x\).

After recovering that phase, decimate to the coarse field and repeat. Induction recovers every binary digit of \(\alpha\) almost surely, producing a measurable factor from \((X_\vartheta,\mu)\) onto the Haar \(\mathbb Z_2^2\) translation system. The function \((-1)^{\alpha_1\bmod2}\), pulled back to configurations, is nonconstant and changes sign under the horizontal unit shift. A mixing transformation cannot have such an eigenfunction, so \(\mu\) is not mixing.

**6. Dense periodic configurations.** Fix any \(W_n(a)\) block and repeat it periodically in both lattice directions, with spatial period \(2^n\). Four copies form an allowed \((n+1)\)-supertile with four child roots equal to \(a\); repeating gives compatible higher ancestors at every stage. Thus this periodic configuration belongs to \(X_\vartheta\). Every legal finite pattern occurs inside some \(W_n(a)\), and therefore occurs in a periodic point. Periodic points are dense.

## Verification

Run `python3 verify.py` with standard Python 3. The independent reverse-decimation test examines all \(2^{16}\) binary \(4\times4\) blocks and obtains precisely \(64\) correctly aligned level-two supertiles. Forward construction gives \(|W_1(a)|=2\) and \(|W_2(a)|=32\) with disjoint root classes. For each root and each wrong alignment, exactly \(8\) of the \(32\) level-two blocks exhibit an interior forbidden two-and-two square. The script also checks periodic extension at two additional levels for all level-one and level-two supertiles. The all-level counting and entropy/uniqueness claims are established by the arguments above rather than by finite enumeration.

## Relationship to prior work

Felipe, Miro and Silvestre (first published 18 September 2026) study two-dimensional random substitution subshifts and prove general results including agreement of inflation-block and topological entropies for primitive block substitutions, as well as a periodic-point density-or-absence dichotomy. Those general entropy and periodicity principles are used as context, not presented as new. The paper's accessible abstract does not specify the present free-corner rule or a unique maximal-entropy law with a recoverable odometer factor; full text remained inaccessible for direct theorem-by-theorem comparison.

Gohlke and Mitchell (2026) classify maximal-entropy measures for **one-dimensional** recognisable random substitution systems. Their one-dimensional hypotheses do not directly cover this planar variable-inheritance construction. The present measure-uniqueness proof instead uses exact hierarchical entropy splitting. Mijares, Miro and Silvestre (2026) study diffraction for a different constant-shape random-substitution family where one letter substitutes to a homogeneous block; that source does not supply the specified two-letter free-corner classification.

## Limitations

The theorem concerns the exact binary rule above, not every primitive planar random substitution. Nonmixing is established for the unique measure of maximal entropy; it is not asserted for all invariant measures. The hierarchy is recovered almost surely, not uniquely for all configurations (constant periodic points can admit multiple alignments). The available abstract of the directly relevant 2026 general study does not exclude an unindexed equivalent special example in its unavailable full text; priority therefore remains provisional. No external independent proof audit has been performed.

## References

1. B. C. L. Felipe, E. D. P. Miro and L. S. Silvestre, *Dynamics and entropy of dynamical systems arising from two-dimensional random substitutions*, Acta Crystallographica A **82** (2026), 428–440, first published 2026-09-18, DOI: `10.1107/S2053273326008351`, https://pubmed.ncbi.nlm.nih.gov/42755358/ .
2. P. Gohlke and A. Mitchell, *A Classification of Intrinsic Ergodicity for Recognisable Random Substitution Systems*, Communications in Mathematical Physics **407** (2026), article 78, DOI: `10.1007/s00220-026-05602-8`, https://link.springer.com/article/10.1007/s00220-026-05602-8 .
3. J. R. Mijares, E. D. P. Miro and L. S. Silvestre, *On the diffraction spectrum of two-dimensional random substitutions*, first published 2026-10-06, DOI: `10.1107/S2053273326009587`, https://onlinelibrary.wiley.com/doi/abs/10.1107/S2053273326009587 .
