# The sharp five-taxon boundary for mean-versus-half-retention phylogenetic risk

## Finding

**Theorem.** Let \(n\geq 2\), and consider nonplane, rooted, full-binary phylogenetic trees with \(n\) taxa, every edge having length one and no stem above the root. Independently, each taxon becomes extinct with common probability \(q\in(0,1)\). Let \(X_T\) denote rooted Faith phylogenetic diversity of the surviving taxa, taking \(X_T=0\) when none survives. The original phylogenetic diversity is \(2n-2\); define the **half-retention probability** as \(H_T(q)=\Pr\{X_T\geq n-1\}\).

There exist two trees \(T,U\) with the same \(n\), such that \(\mathbb E X_T>\mathbb E X_U\) but \(H_T(q)<H_U(q)\) for an interior extinction probability \(q\), **if and only if \(n\geq5\)**. Indeed, for every \(n\geq4\), let \(C_4=(((a,b),c),d)\) and \(B_4=((a,b),(c,d))\), and let \(C_{n+1}=(C_n,e_{n+1})\), \(B_{n+1}=(B_n,e_{n+1})\), where parentheses describe rooted binary joins. For every \(q\in(0,1)\):

\[
\mathbb E[X_{C_n}]-\mathbb E[X_{B_n}]=q^2(1-q)>0,
\]
\[
H_{C_n}(q)-H_{B_n}(q)
=q^{n-2}(1-q)\big((n-2)q-(n-4)\big).
\]

For every \(n\geq5\), the second difference is strictly negative precisely when \(0<q<(n-4)/(n-2)\), vanishes at the sole interior crossover \(q=(n-4)/(n-2)\), and is strictly positive above it. The crossover increases strictly to one with \(n\). For \(n=4\), it is strictly positive throughout \((0,1)\).

## Assumptions and scope

The trees are rooted and strictly binary, with precisely \(n\) leaves and \(2n-2\) unit-length edges. They need **not** be ultrametric: unit edge lengths count branches, not equal root-to-tip times. The phylogenetic-diversity score includes every edge in a root-to-surviving-leaf path. Extinctions are independent, homogeneous Bernoulli events, and probabilities refer to a fixed future time. Results do not assert the same threshold for non-unit edge lengths, correlated extinctions, unrooted phylogenetic diversity, or alternative retention targets. Both candidate trees have the same number of leaves and identical total initial phylogenetic diversity. The theorem is existential for \(n\ge5\), not a classification of every tree pair.

## Proof

**1. The four-leaf base law.** Let \(F_T(z;q)=\mathbb E[z^{X_T}]\), a probability-generating polynomial. Enumerating the \(2^4=16\) subsets of leaves, with the probability of a surviving set of size \(k\) equal to \((1-q)^kq^{4-k}\), yields

\[
F_{C_4}(z;q)-F_{B_4}(z;q)
=q^2(1-q)z(1-z)\bigl(q(1-z)^2-z^2\bigr).
\tag{1}
\]

For explicit reproducibility, the counts of subsets indexed by (number surviving, rooted diversity) are, for \(C_4\), \((0,0):1\), \((1,1):1\), \((1,2):1\), \((1,3):2\), \((2,3):1\), \((2,4):5\), \((3,5):4\), \((4,6):1\); for \(B_4\), they are \((0,0):1\), \((1,2):4\), \((2,3):2\), \((2,4):4\), \((3,5):4\), \((4,6):1\). These sum to \(16\) in each tree. Direct substitution reproduces equation (1), which can also be checked with the attached standard-library code.

**2. Common-root grafting.** For any rooted binary \(m\)-leaf tree \(T\), write \(G(T)=(T,e)\), where \(e\) is a new singleton child of a new root and both new edges have length one. For two trees \(T,U\) with the same number of leaves, their all-extinct probability is the common value \(q^m\). Conditional on at least one old leaf surviving, the newly grafted tree adds one edge when \(e\) is extinct and two edges when \(e\) survives. When no old leaves survive, the contribution from the new singleton is the same for both trees. Therefore these identical exceptional contributions cancel upon subtraction, giving the exact identity

\[
F_{G(T)}(z;q)-F_{G(U)}(z;q)
=\big(qz+(1-q)z^2\big)\big(F_T(z;q)-F_U(z;q)\big).
\tag{2}
\]

Repeatedly applying (2) to (1) gives, for all \(n\ge4\),

\[
\Delta_n(z):=F_{C_n}(z;q)-F_{B_n}(z;q)
=q^2(1-q)z^{n-3}\big(q+(1-q)z\big)^{n-4}(1-z)
\big(q(1-z)^2-z^2\big).
\tag{3}
\]

This is an exact finite polynomial identity for every \(n\), not an extrapolation from enumeration.

**3. Expected diversity.** Differentiating (3) in \(z\) and evaluating at \(z=1\) yields \(\Delta_n'(1)=q^2(1-q)\), since the other factors take value one and the differentiated \((1-z)\) contributes \(-1\) while \(q(1-z)^2-z^2\) takes value \(-1\). Because \(F_T'(1)=\mathbb E X_T\), this proves the stated strict mean inequality.

**4. Half-retention probability.** Set \(m=n-4\) and

\[
A(z)=\big(q+(1-q)z\big)^m
\big(q-3qz+(3q-1)z^2+(1-q)z^3\big).
\]

Equation (3) becomes \(\Delta_n(z)=q^2(1-q)z^{n-3}A(z)\). Therefore the half-retention probability difference, the sum of coefficients of \(z^j\) for \(j\ge n-1\), equals \(q^2(1-q)\) times the sum of coefficients of \(A(z)\) of degree at least two. Since \(A(1)=0\), that sum is the negative of its constant and linear coefficients. Those coefficients are

\[
[z^0]A=q^{m+1},\qquad
[z^1]A=-3q^{m+1}+m(1-q)q^m.
\]

Thus

\[
H_{C_n}-H_{B_n}
=-q^2(1-q)q^m\big(m(1-q)-2q\big)
=q^{n-2}(1-q)\big((n-2)q-(n-4)\big).
\]

The factors \(q^{n-2}(1-q)\) are strictly positive for \(0<q<1\). For \(n=4\) the remaining factor is \(2q>0\). For every \(n\ge5\) it is strictly increasing affine in \(q\) with one interior zero \((n-4)/(n-2)\); the sequence of zeros is \(1-2/(n-2)\), strictly increasing and tending to one.

**5. Sharpness below five taxa.** Up to isomorphism, there is exactly one rooted full-binary tree with two leaves, one with three, and two with four: the four-leaf caterpillar and balanced fork above. Trees with one leaf are also unique when that trivial case is admitted. At four leaves, equation (3) shows that the caterpillar has higher mean and higher half-retention probability for every \(q\in(0,1)\). Hence no discordance is possible through four leaves. At five leaves and \(0<q<1/3\), the constructed pair has the opposite half-retention ordering. This proves the sharp minimum.

## Verification

The attached \(\texttt{verify.py}\) uses only the Python standard library. It independently reconstructs the descendant-leaf edge masks and enumerates every surviving subset, expands exact polynomial weights over the integers, checks the entire four-leaf generating-function difference, verifies the claimed expectation and half-retention polynomials for each leaf count from four through eleven, and confirms the small-tree shape counts. Run \(\texttt{python3 verify.py}\). It successfully returned all checks passed. This finite replay supports the calculation; the all-\(n\) proof is equations (1)–(3) and the coefficient argument, not the finite replay.

## Relationship to prior work

Faller, Pardi and Steel (arXiv:0708.0425, publicly available August 2, 2007; journal publication 2008) introduce the exact future-phylogenetic-diversity distribution under independent extinction and explicitly distinguish maximizing its expectation from minimizing a loss-tail probability. They give a general exact distribution algorithm in Section 4 and an asymptotic normal result. This theorem does **not** claim to introduce their probability model, root-PD edge indicators, exact distribution recursion, or the general distinction between mean and risk. Its specific contribution is the sharp smallest leaf count and an all-size closed-form half-retention crossover for a motivated family of equal-size tree shapes.

Steel, Mimoto and Mooers (2007) examine the expected contribution of individual species to future phylogenetic diversity; that expected-value score does not give the half-retention comparison of whole tree shapes here. Earlier analytical comparisons of the same four-leaf tree rotation concern mean and variance of future PD; their variance comparison neither implies nor specifies this exact half-retention threshold. The family of unit-edge trees is intentionally a discrete shape model; it should not be mistaken for equal-height phylogenetic time trees.

## Limitations

Historical originality is assessed only against the sources inspected and the accessible records; the general distribution algorithm makes the present finite calculations in principle computable, but its published statement does not supply the claimed sharp threshold or all-size formula. This comparison is not an independently validated priority claim. No ecological data, fitted extinction rates, or population correlations are inferred. A 50% retention threshold is a policy-relevant mathematical benchmark, not a universal ecological objective. The result is restricted to strictly positive interior extinction probabilities and rooted unit-edge full-binary shapes; it does not describe all possible shape comparisons.

## References

1. B. Faller, F. Pardi and M. Steel, “Distribution of phylogenetic diversity under random extinction,” arXiv:0708.0425 (first public version August 2, 2007), *Journal of Theoretical Biology* 251 (2008), 286–296. DOI: https://doi.org/10.1016/j.jtbi.2007.11.034. Author-hosted full text: https://www.math.canterbury.ac.nz/~m.steel/Non_UC/files/research/arxiv-1.pdf.
2. M. Steel, A. Mimoto and A. Ø. Mooers, “Hedging Our Bets: The Expected Contribution of Species to Future Phylogenetic Diversity,” *Evolutionary Bioinformatics* 3 (2007), 237–244. DOI: https://doi.org/10.1177/117693430700300024. Full text: https://journals.sagepub.com/doi/10.1177/117693430700300024.
3. D. P. Faith, “Phylogenetic diversity, functional trait diversity and extinction: avoiding tipping points and worst-case losses,” *Philosophical Transactions of the Royal Society B* 370 (2015), 20140011. DOI: https://doi.org/10.1098/rstb.2014.0011. Relevant contextual work on loss-sensitive objectives.
