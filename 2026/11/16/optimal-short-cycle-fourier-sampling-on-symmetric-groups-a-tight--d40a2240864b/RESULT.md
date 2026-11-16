# Optimal short-cycle Fourier sampling on symmetric groups: a tight four-point exception and sharp higher-rank barriers

## Finding
Let \(n\ge4\), let \(V=\{x\in\mathbb C^n:\sum_i x_i=0\}\), and let \(R_\sigma\) be the standard unitary representation of \(S_n\) on \(V\). For \(A\in\operatorname{End}(V)\), put \(F_A(\sigma)=\operatorname{tr}(A^*R_\sigma)\). Consider **all central probability laws** \(\mu\) supported on permutations moving at most four letters. Their sampling Gram operators are defined by
\[
\langle A,G_\mu A\rangle=\mathbb E_{\sigma\sim\mu}|F_A(\sigma)|^2.
\]
The least possible squared frame-condition number \(\kappa_n=\inf_\mu\lambda_{\max}(G_\mu)/\lambda_{\min}(G_\mu)\), with singular samples assigned infinite condition number, is **attained** and equals
\[
\boxed{\kappa_n=\begin{cases}1,&n=4,\\11/8,&n=5,\\19/7,&n=6,\\\dfrac{(n-5)^2(n-2)(n^2-3n+1)}{4(n^2-5n+8)},&n\ge7.\end{cases}}
\]
An optimal law for \(n=4\) gives half its mass to all transpositions uniformly and half to all four-cycles uniformly; it is exactly tight. For \(n=5\), assign mass \(1/13\) to the identity, \(36/143\) to the double-transposition class, and \(96/143\) to the four-cycle class. For \(n=6\), assign mass \(5/19\) to double transpositions and \(14/19\) to four-cycles. For every \(n\ge7\), use only the last two classes with respective masses \((2n-7)/(n^2-3n+1)\) and \((n^2-5n+8)/(n^2-3n+1)\). Every law is uniform **inside each conjugacy class**. Thus central short-cycle observation has an exact tight exceptional dimension, two further finite-rank regimes, and a cubic stability barrier as \(n\to\infty\), with leading asymptotic \(\kappa_n\sim n^3/4\).

## Assumptions and scope
The five allowed conjugacy types are identity (id), transposition (T), three-cycle (C3), product of two disjoint transpositions (D22), and four-cycle (C4); these exhaust all permutations with at most four moved letters for \(n\ge4\). A central law is a nonnegative mixture of class-uniform laws, including zero weights. Norms on \(\operatorname{End}(V)\) are Hilbert–Schmidt. Condition numbers in this document are eigenvalue ratios (**squared singular-value** ratios), not their square roots. Haar Plancherel differs by one common scalar factor, which does not change \(\kappa_n\). Singular laws have infinite ratio.

## Proof
**Four spectral levels.** The conjugation representation of \(S_n\) on \(\operatorname{End}(V)\) is the multiplicity-free sum of scalar, standard, symmetric two-index, and skew sectors of dimensions \(1,n-1,n(n-3)/2,(n-1)(n-2)/2\). The symmetric two-index sector is the complement to the scalar and standard representations in \(\operatorname{Sym}^2V\); it is the familiar \((n-2,2)\) Johnson constituent. The skew sector \(\wedge^2V\) is irreducible. Consequently, class-uniform Gram operators are scalar on all four sectors.

For any conjugacy type having \(f\) fixed letters and \(t\) two-cycles, write the four levels as \(L_0,L_1,L_2,L_3\), in that sector order. They are
\[
L_0=\frac{(f-1)^2}{n-1},\quad L_1=\frac{f(n-f)}{(n-1)(n-2)},\quad L_3=\frac{n-f-2t}{(n-1)(n-2)},
\]
\[
L_2=\frac{2}{n(n-3)}\left(\frac{n+f+2t-2}{2}-L_0-(n-1)L_1\right).
\]
For completeness, \(\operatorname{tr}R_\sigma=f-1\) gives \(L_0\). In the standard symmetric sector, use \(B_d=P\operatorname{diag}(d)P\), where \(P=I-\mathbf1\mathbf1^T/n\) and \(\sum d_i=0\). Its squared norm is \((1-2/n)\sum|d_i|^2\), while \(\operatorname{tr}(B_d^*R_\sigma)=\sum_{\sigma(i)=i}\overline{d_i}\). Averaging over the uniform fixed-letter subset gives \(L_1\). The skew component of an orthogonal matrix has squared norm \(((n-1)-\operatorname{tr}R_\sigma^2)/2=(n-f-2t)/2\), giving \(L_3\). The symmetric component has squared norm \((n+f+2t-2)/2\), so subtracting the known scalar and standard contributions and dividing by \(n(n-3)/2\) gives \(L_2\). Complexification preserves the same spectra. This proves all four formulas for every class, without interpolation from finite data.

Substituting the five types \((f,t)=(n,0),(n-2,1),(n-3,0),(n-4,2),(n-4,0)\) yields a four-by-five rational matrix of eigenvalues. For clarity, on the four nonidentity classes:
\[
\begin{array}{c|cccc}
 &L_0&L_1&L_2&L_3\\\hline
T&(n-3)^2/(n-1)&2/(n-1)&4/[n(n-1)]&0\\
C3&(n-4)^2/(n-1)&3(n-3)/[(n-1)(n-2)]&3(n-4)/[n(n-1)(n-2)]&3/[(n-1)(n-2)]\\
D22&(n-5)^2/(n-1)&4(n-4)/[(n-1)(n-2)]&8(n^2-5n+8)/[n(n-3)(n-2)(n-1)]&0\\
C4&(n-5)^2/(n-1)&4(n-4)/[(n-1)(n-2)]&4(n^2-7n+14)/[n(n-3)(n-2)(n-1)]&4/[(n-1)(n-2)].
\end{array}
\]
The identity contributes \((n-1,0,0,0)\). The spectral levels of a mixture are the corresponding convex combinations.

**Matching lower bounds.** For any positive numbers \(L_2,L_3\) and \(p\in[0,1]\), \(\min(L_2,L_3)\le pL_2+(1-p)L_3\). Thus any classwise inequality \(L_j\ge K[pL_2+(1-p)L_3]\) extends to every mixture and implies \(\kappa_n\ge K\).

For \(n=5\), take \(j=1\), \(K=11/8\), \(p=5/11\). The five classwise differences, ordered id,T,C3,D22,C4, are exactly \((0,3/8,9/32,0,0)\). For \(n=6\), take \(j=1\), \(K=19/7\), \(p=9/19\); the five differences are \((0,8/35,6/35,0,0)\). Both lower bounds are therefore universal.

For \(n\ge7\), take \(j=0\),
\[
p=\frac{n(n-3)}{2(n^2-3n+1)},\quad K=\frac{(n-5)^2(n-2)(n^2-3n+1)}{4(n^2-5n+8)}.
\]
The differences for id,T,C3,D22,C4 are
\[
n-1,\quad\frac{(n-3)(n^2-3n-2)}{2(n^2-5n+8)},\quad\frac{n^3-6n^2+4n+13}{4(n^2-5n+8)},\quad0,\quad0.
\]
All are nonnegative for every integer \(n\ge7\), completing the lower bound for every admissible central law.

**Attainment.** For \(n=4\), averaging T and C4 at equal masses makes all four levels exactly \(1/3\), so the ratio is one. For \(n=5\), the indicated three-class mixture has four levels \((4/13,4/13,32/143,32/143)\), giving \(11/8\). For \(n=6\), the indicated D22/C4 mixture has \(L_2=L_3=14/95\), \(L_1=2/5\), and \(L_0=1/5\), giving \(19/7\). For \(n\ge7\), the indicated D22/C4 weights make
\[
L_2=L_3=\frac{4(n^2-5n+8)}{(n-1)(n-2)(n^2-3n+1)},\quad L_0=\frac{(n-5)^2}{n-1},\quad L_1=\frac{4(n-4)}{(n-1)(n-2)}.
\]
Here \(L_0\) is largest and \(L_2=L_3\) smallest by the elementary inequalities \((n-5)^2(n-2)\ge4(n-4)\) and \(L_1\ge L_2\) for integers \(n\ge7\). The ratio equals \(K\). All specified optimal laws are nonsingular.

## Verification
The companion script `check.py` directly enumerates each of the five permutation classes for \(n=4,5,6\), constructs the complete Fourier-block Gram matrix in ambient coordinates, and compares every eigenvalue and multiplicity against the four-sector formulas. It independently verifies the three exceptional optimal witnesses and checks their predicted ratios. It also evaluates the general rational witness formulas at all integers \(7\le n\le100\). The analytic proof above, especially its classwise rational dual inequalities, establishes the infinite claims; the finite script is corroboration, not an exhaustive proof.

## Relationship to prior work
Chen–DeJong–Halverson–Shuman (2021) develop interpretable Parseval representation-theoretic frames for ranking data. Beck–Ghandehari (2022) characterize compatible Frobenius–Schur frames for inverse-closed Cayley generating sets; their frame construction is not this restricted point-evaluation minimax problem. Previously available exact classwise standard-block spectra and a general two-statistic conjugacy-class formula already cover the four constituent eigenvalues for a *single* class; no originality is asserted for those ingredients. The contribution assessed here is the distinct **global weighted minimax design over every central law supported on all five short-motion types**, with sharp four-regime optima, rational certificates, and an exceptional exactly tight law at dimension four. Searches compared class mixing, alternative language about central sampling, and stronger classwise Fourier-spectrum theorems.

## Limitations
Only conjugacy-invariant sampling probability laws and support consisting of permutations moving at most four labels are optimized. Noncentral weights, other supports, individual row selection, and sampling-cost constraints are not addressed. The optimal laws given are witnesses, not a complete classification of all possible optimizers. Some related research records supplied only summaries and were therefore treated as priority risks rather than certified full-text exclusions. Historical novelty is provisional pending independent comparison.

## References
- Y. Chen, J. DeJong, T. Halverson, D. I. Shuman, *Signal Processing on the Permutahedron: Tight Spectral Frames for Ranked Data Analysis*, arXiv:2103.04150 (first submitted 2021-03-06), Journal of Fourier Analysis and Applications 27 (2021).
- K. Beck, M. Ghandehari, *Frames for Graph Signals on the Symmetric Group: A Representation Theoretic Approach*, arXiv:2203.03036 (first submitted 2022-03-06), EUSIPCO 2022.
- Earlier public mathematical records titled *Four-level three-cycle sampling spectrum for the symmetric-group standard Fourier block* and *Two-statistic Fourier sampling law for symmetric-group conjugacy classes* (2026). Their classwise formulas are acknowledged as prior ingredients; the present weighted minimax statement is compared separately.
