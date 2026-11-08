# Bias first destroys real-rooted acyclic sink-count laws on the eight-cycle

## Finding
For each integer \(n\ge3\), orient the \(n\) edges of the cycle \(C_n\) independently clockwise with a common probability \(p\in(0,1)\), and counterclockwise otherwise. Condition on the orientation being acyclic, and let \(S_{n,p}\) be the number of sinks (vertices of outdegree zero). The probability-generating polynomial \(\mathbb E[z^{S_{n,p}}]\) has exclusively real zeros for **every** \(p\in(0,1)\) when \(3\le n\le7\). At \(n=8\), the choice \(p=1/10\) gives a conjugate pair of nonreal zeros. Therefore \(C_8\) is the smallest cycle where this natural directional-bias deformation of the acyclic sink-count law loses real-rootedness. This does **not** assert the smallest graph among all graph families, nor classify all biases or larger cycles.

## Assumptions and scope
The cycle is a simple undirected labeled cycle on \(n\ge3\) vertices, equipped with a fixed clockwise traversal. Edge directions are independent *before* conditioning. Exactly two orientations of \(C_n\) are cyclic: the consistently clockwise and consistently counterclockwise orientations, with total probability \(p^n+(1-p)^n<1\). Define \(u=p(1-p)\), so \(0<u\le1/4\). Real-rootedness refers to the zeros in the complex variable \(z\) of the conditional probability-generating polynomial; normalization by a nonzero constant does not affect its zeros.

## Proof
Let \(T_{n,p}\) denote the number of sinks *without* conditioning, and let \(G_{n,p}(z)=\mathbb E[z^{T_{n,p}}]\). For each sink indicator \(I_v\), the elementary identity \(z^{I_v}=1+(z-1)I_v\) yields
\[
G_{n,p}(z)=\sum_{A\subseteq V(C_n)}(z-1)^{|A|}\Pr(\text{every vertex in }A\text{ is a sink}).
\]
Adjacent vertices cannot both be sinks. When \(A\) is an independent \(k\)-set, the \(2k\) incident directed edges are distinct and forced, with one clockwise and one counterclockwise edge per sink. Its event probability is \(u^k\). For \(0\le k\le\lfloor n/2\rfloor\), there are
\[
a_{n,k}=\frac{n}{n-k}\binom{n-k}{k}
\]
independent \(k\)-sets of \(C_n\); the \(k=0\) term is one. Thus the *exact, all-parameter* formula is
\[
G_{n,p}(z)=\sum_{k=0}^{\lfloor n/2\rfloor}a_{n,k}u^k(z-1)^k.\tag{1}
\]
The only orientations without a sink are the two consistently oriented directed cycles. They are also exactly the cyclic orientations. Consequently
\[
\mathbb E[z^{S_{n,p}}]=\frac{G_{n,p}(z)-G_{n,p}(0)}{1-G_{n,p}(0)},\qquad G_{n,p}(0)=p^n+(1-p)^n.\tag{2}
\]
The numerator is divisible by \(z\). Put \(Q_n(z;u)=[G_{n,p}(z)-G_{n,p}(0)]/z\). Its nonzero factor, whose real-rootedness we must test, depends on \(p\) only through \(u\).

Direct finite algebra in (1) gives the complete small-cycle list:
\[
\begin{aligned}
Q_3/u&=3,\\
Q_4/u&=2(uz-2u+2),\\
Q_5/u&=5(uz-2u+1),\\
Q_6/u&=2u^2z^2+(-6u^2+9u)z+(6u^2-18u+6),\\
Q_7/u&=7\bigl(u^2z^2+(-3u^2+2u)z+(3u^2-4u+1)\bigr).
\end{aligned}\tag{3}
\]
The polynomials \(Q_3,Q_4,Q_5\) are constant or linear. For \(Q_6\) and \(Q_7\), the quadratic discriminants (including the displayed positive factors \(u\) in (3)) are, respectively,
\[
\Delta_6=-3u^4(4u^2-12u-11)>0,\qquad
\Delta_7=-49u^5(3u-4)>0\tag{4}
\]
for all \(0<u\le1/4\). All coefficients of \(Q_n\) are nonnegative because they are probabilities of positive sink counts, and the constant and leading coefficients are strictly positive. Therefore any real zeros of these nonconstant factors are negative. Equations (3)–(4) establish real-rootedness for all \(3\le n\le7\) and all admissible biases.

For \(n=8\) and \(p=1/10\), we have \(u=9/100\), and expansion of (1) yields
\[
Q_8(z;9/100)=\frac{6561z^3+556956z^2+6389766z+21523356}{50000000}.\tag{5}
\]
The discriminant of the integer cubic in the numerator of (5) is exactly
\[
-548120008099593420688656<0.\tag{6}
\]
A real cubic with negative discriminant has one real root and two nonreal conjugate roots. By (2), multiplication by \(z\) and division by the positive conditioning probability add a single zero root and preserve those nonreal roots. This supplies the eight-cycle witness, and (3)–(4) exclude every smaller cycle. \(\square\)

## Verification
Run `python3 verify.py` from the directory containing the files. The standard-library checker independently enumerates all \(2^n\) edge-direction words for \(3\le n\le10\) at three exact rational biases and tests equation (1), no-sink mass and normalization. It also reproduces the rational cubic (5), its *integer* discriminant (6), and sample positive discriminants at \(n=6,7\). The executable reports `VERIFY_OK 81 exact checks`. The universal statement for all real biases and the sharp cutoff follows from symbolic identities (1)–(6), not from the finite enumeration.

## Relationship to prior work
Hwang, Jung, Lee, Oh and Yu (first public preprint October 24, 2019) develop acyclic orientation polynomials and sink enumerators. Wentzel-Larsen and Anhøj (October 1, 2019) address crossings and longest runs in independent Bernoulli sequences, mostly in the linear rather than circular setting. Alexandersson and Leite (first public preprint October 30, 2026), Proposition 3.21, **prove real-rootedness of the uniform-acyclic sink polynomial for every cycle** and, in Section 4, real-rootedness of the all-orientations sink polynomial for claw-free graphs. Thus the unbiased case and those general results are prior work, **not** new claims here. The new distinction is a common, independent clockwise bias *before conditioning on acyclicity*, and the sharp first loss of real-rootedness at \(n=8\); the inspected statements neither assert nor imply stability under that biased conditional measure. The derivation also uses standard cycle independent-set counting; the formula for that count alone is not new.

## Limitations
This result applies only to simple cycles under a common preconditioning directional bias. It does not determine the complete interval of biases causing nonreal zeros for \(n=8\), nor describe every larger cycle, nor imply a general weighted graph classification. Historical priority has not been independently certified. The accessible 2005 Inoue–Aki circular-run article abstract describes broader run generating functions but was not available in complete text for a statement-by-statement comparison; its possible overlapping consequences remain a specific risk. No independent mathematical audit has been performed.

## References
- T. Wentzel-Larsen and J. Anhøj, *Joint distribution for number of crossings and longest run in independent Bernoulli observations*, PLOS ONE 14(10), e0223233, October 1, 2019. DOI: https://doi.org/10.1371/journal.pone.0223233.
- B.-H. Hwang, W.-S. Jung, K.-J. Lee, J. Oh, and S.-H. Yu, *Acyclic orientation polynomials and the sink theorem for chromatic symmetric functions*, arXiv:1910.10920, first public October 24, 2019. https://arxiv.org/abs/1910.10920.
- P. Alexandersson and L. S. M. Leite, *Sink polynomials of line graphs and weighted matching polynomials*, arXiv:2610.41502, first public October 30, 2026, especially Proposition 3.21 and Theorem 4.3. https://arxiv.org/abs/2610.41502.
- K. Inoue and S. Aki, *Joint distributions of numbers of success runs of specified lengths in linear and circular sequences*, Ann. Inst. Stat. Math. 57 (2005), 353–368. https://doi.org/10.1007/BF02507029.
