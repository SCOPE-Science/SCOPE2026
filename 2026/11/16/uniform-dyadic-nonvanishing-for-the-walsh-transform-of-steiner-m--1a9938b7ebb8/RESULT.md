# Uniform dyadic nonvanishing for the Walsh transform of Steiner matroid bases

## Finding

Let \((X,\mathcal L)\) be any nontrivial Steiner triple system of order \(v=|X|\ge7\), and let \(\mathcal B=\binom X3\setminus\mathcal L\) be the family of triples that are *not* blocks. These are precisely the rank-three bases in the associated simple rank-three matroid. Embed each triple in \(G=\mathbb F_2^X\) by its incidence vector and use unnormalized counting convolution \(T f=\mathbf1_{\mathcal B}*f\). For every frequency subset \(S\subseteq X\), write

\[
W(S)=\sum_{B\in\mathcal B}(-1)^{|B\cap S|}.
\]

**Uniform two-adic law.** For every such design and every frequency, independently of the design isomorphism type,

\[
W(S)\equiv\begin{cases}4\pmod8,&v\equiv5,7\pmod8,\\0\pmod8,&v\equiv1,3\pmod8.\end{cases}
\]

In particular, whenever \(v\equiv5,7\pmod8\), *all* \(2^v\) multipliers have exact two-adic valuation two, \(T\) is invertible, and

\[
\operatorname{rank}T=2^v,\qquad \|T^{-1}\|_{\ell^2\to\ell^2}\le\tfrac14,\qquad \nu_2(\det T)=2^{v+1}.
\]

Here \(\nu_2\) means the exponent of two dividing a nonzero integer. The determinant statement uses the integral matrix of the counting-convolution operator on functions \(G\to\mathbb C\).

## Assumptions and scope

A Steiner triple system is a collection \(\mathcal L\subseteq\binom X3\) in which every pair of distinct points belongs to exactly one block. All systems are labelled, but the result is invariant under relabelling. The case \(v=3\) is omitted: its family \(\mathcal B\) is empty. Nontrivial orders satisfy \(v\ge7\) and \(v\equiv1,3\pmod6\). In the theorem the residue statements cover all four odd residues modulo eight, but invertibility is asserted only in the two residues \(5,7\). No claim of invertibility or singularity at *every* other admissible order is made.

For the character \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\), convolution is defined without a normalizing factor by \((\mathbf1_{\mathcal B}*f)(x)=\sum_{y\in G}\mathbf1_{\mathcal B}(y)f(x-y)\). Its Fourier eigenvalue on \(\chi_S\) is exactly \(W(S)\), not a probability-normalized transform.

## Proof

Write \(N=|\mathcal B|\), \(d_i=|\{B\in\mathcal B:i\in B\}|\) and \(c_{ij}=|\{B\in\mathcal B:\{i,j\}\subseteq B\}|\). The Steiner incidence property gives, for each point and each unordered pair,

\[
N=\binom v3-\frac{v(v-1)}6=\frac{v(v-1)(v-3)}6,\quad
 d_i=\binom{v-1}2-\frac{v-1}2=\frac{(v-1)(v-3)}2,\quad c_{ij}=v-3.
\]

For each \(B\), expand \((-1)^{|B\cap S|}=\prod_{i\in B}(1-2\mathbf1_{i\in S})\). Since every \(B\) has exactly three points, no higher-degree terms occur. Summing gives the exact integer identity

\[
W(S)=N-2\sum_{i\in S}d_i
 +4\sum_{\{i,j\}\in\binom S2}c_{ij}
 -8\left|\{B\in\mathcal B:B\subseteq S\}\right|.
\tag{1}
\]

All admissible \(v\) are odd. If \(v\equiv5\pmod8\), then \(v-1\) is divisible by four and \(v-3\) is twice an odd integer. If \(v\equiv7\pmod8\), then \(v-1\) is twice an odd integer and \(v-3\) is four times an odd integer. In *both* cases \(d_i\equiv0\pmod4\), \(c_{ij}\equiv0\pmod2\), and the displayed expression for \(N\) has exact two-adic valuation two: \(N\equiv4\pmod8\). Formula (1) therefore yields \(W(S)\equiv4\pmod8\).

If instead \(v\equiv1\pmod8\), then \(v-1\) is divisible by eight and \(v-3\) is twice an odd integer. If \(v\equiv3\pmod8\), then \(v-1\) is twice an odd integer and \(v-3\) is divisible by eight. In either case \(N\equiv0\pmod8\), \(d_i\equiv0\pmod4\) and \(c_{ij}\equiv0\pmod2\), hence (1) gives \(W(S)\equiv0\pmod8\). This proves the full residue assertion.

The Walsh characters diagonalize convolution on \(G\). When all \(W(S)\equiv4\pmod8\), they are nonzero integers and satisfy \(|W(S)|\ge4\); the rank and Hilbert-space inverse-norm conclusions follow immediately. As the integer matrix of \(T\) has determinant \(\prod_{S\subseteq X}W(S)\), additivity of the two-adic valuation gives \(\nu_2(\det T)=\sum_{S\subseteq X}2=2^{v+1}\). These arguments are exact in every admissible order; they use no finite extrapolation.

## Verification

The accompanying standalone Python program `verify.py` constructs and independently validates five explicit designs: the seven-point projective system, the nine-point affine-plane system, a cyclic thirteen-point system, and two nonisomorphic fifteen-point constructions (projective and Bose). It enumerates the base indicators, calculates every Walsh coefficient by integer fast Walsh transform, and independently checks each coefficient against the exact subset-incidence identity (1). It checks all point-pair incidences, Parseval identities, and the predicted residues. The arithmetic identities, not finite checks, prove the infinite statement.

The verified ranks in those five cases are respectively \(128\), \(272\), \(8192\), \(32768\), \(32768\). The two order-fifteen systems have different absolute multiplier histograms but both have full rank. The order-nine system has 240 zeros, showing that the divisible-by-eight branch can be genuinely singular. More elementarily, at frequency \(S\) consisting of any two points the identity simplifies to

\[
W(S)=\frac{(v-3)(v-9)(v-4)}6,
\]

which vanishes at \(v=9\) for *every* nine-point Steiner triple system.

Replay with Python 3 (standard library): `python verify.py`. The complete output of the execution used for this report is embedded as `verification_output.txt`.

## Relationship to prior work

Kirkman's existence theorem and the incidence parameters of Steiner triple systems are classical; Cameron's design-theory encyclopaedia describes the existence and diversity of these systems. Ghorbani and Khosrovshahi study signed Steiner triple systems in the distinct sense of assigning signs *to blocks* subject to pairwise signed incidence requirements; their existence results do not state the point-character Walsh nonvanishing law above. Work on Steiner-design base polytopes studies geometric asymmetry, while Fourier-labeled Steiner frames address a different Fourier object. The general elementary expansion of Boolean characters is standard; the new mathematical claim assessed here is its uniform two-adic consequence and complete Fourier invertibility for the *complementary rank-three base families of every Steiner triple system* at the indicated orders.

## Limitations

The result gives congruences, not exact multipliers or their multiplicity distributions in arbitrary designs. For \(v\equiv1,3\pmod8\), divisibility by eight does not decide nonvanishing. The sharpness of the Hilbert inverse bound \(1/4\) is not asserted uniformly. The historical-priority comparison is bounded; it does not establish that no earlier result stated an equivalent criterion. No independent mathematical audit has been performed.

## References

1. P. J. Cameron, *Encyclopaedia of Design Theory: Steiner triple systems*, online reference page dated 26 October 2002, https://webspace.maths.qmul.ac.uk/p.j.cameron/design/encyc/sts/m/ .
2. E. Ghorbani and G. B. Khosrovshahi, *Simple signed Steiner triple systems*, arXiv:1105.2896, initial public preprint 14 May 2011, https://arxiv.org/abs/1105.2896 .
3. C. J. Colbourn, J. H. Dinitz and A. Rosa, *Bicoloring Steiner Triple Systems*, Electronic Journal of Combinatorics 6 (1999), R25, https://www.combinatorics.org/ojs/index.php/eljc/article/view/v6i1r25 .
