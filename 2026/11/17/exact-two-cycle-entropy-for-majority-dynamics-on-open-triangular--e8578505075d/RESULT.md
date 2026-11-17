# Exact two-cycle entropy for majority dynamics on open triangular strips

## Finding

For each integer \(n\ge2\), let \(G_n=P_n\square K_3\) be the labelled open strip of \(n\) triangles, with edges between corresponding vertices of neighboring triangles. Apply synchronous binary open-neighbor majority: at each vertex take the strict majority of neighboring bits, retaining the existing bit in a tie. Let \(F_n\) be the global update, \(P_n=\#\operatorname{Fix}(F_n^2)\) and \(Q_n=\#\operatorname{Fix}(F_n)\). Define

\[
\begin{aligned}
D_P(z)&=(1-z^2)(1-2z+z^2-3z^3)(1-4z+z^2-3z^3+9z^4),\\
N_P(z)&=22-70z+58z^2-166z^3+340z^4-94z^5+276z^6-342z^7-216z^8,\\
D_Q(z)&=(1-3z)(1-z-z^3),\\
N_Q(z)&=4-8z+2z^2-6z^3.
\end{aligned}
\]

Then the **exact all-length generating functions** are

\[
\boxed{\sum_{n\ge2}P_nz^{n-2}=\frac{N_P(z)}{D_P(z)},\qquad
\sum_{n\ge2}Q_nz^{n-2}=\frac{N_Q(z)}{D_Q(z)}.}
\]

Every trajectory eventually has temporal period one or two, and the exact number of distinct primitive two-cycle orbits is \(C_n=(P_n-Q_n)/2\). In particular:

| Number of triangles | Fixed configurations \(Q_n\) | Initially periodic configurations \(P_n\) | Primitive two-cycle orbits \(C_n\) |
|---:|---:|---:|---:|
| 2 | 4 | 22 | 9 |
| 3 | 8 | 62 | 27 |
| 4 | 22 | 232 | 105 |
| 5 | 62 | 800 | 369 |
| 6 | 178 | 3028 | 1425 |
| 7 | 524 | 11414 | 5445 |

Let \(\lambda=3.778651974588\ldots\) be the unique root of \(x^4-4x^3+x^2-3x+9\) in \((3.5,4)\). Its remaining roots and all other relevant roots have smaller modulus. Consequently

\[
\boxed{P_n\sim 1.03597111082\ldots\,\lambda^n,\qquad
Q_n\sim\frac4{17}\,3^n,\qquad
C_n\sim0.51798555541\ldots\,\lambda^n.}
\]

Thus, among *initially periodic* configurations, the fixed-state fraction tends to zero exponentially, even though both fixed states and primitive two-cycles grow exponentially with strip length. Under a uniformly random initial state, the probability of being periodic at time zero is asymptotic to \(1.03597111082\ldots(\lambda/8)^n\).

## Assumptions and scope

The graph is the simple Cartesian product of a path with \(n\) labelled ordered columns and a three-vertex complete graph, with vertex set \(\{0,\ldots,n-1\}\times\{0,1,2\}\). Vertices in the same column form a triangle, and corresponding rows in neighboring columns are adjacent. The two boundary columns have degree three; all interior vertices have degree four. For a vertex of degree four a two-to-two neighbor tie preserves its old bit. The graph is open along its length, not cyclic. The counts concern every labelled binary initial configuration, not spatial equivalence classes and not configurations which enter an orbit only after a transient.

## Proof

**Period restriction.** Encode bits as spins \(\sigma_v\in\{-1,1\}\), let \(A\) be the symmetric adjacency matrix of \(G_n\), and set \(W=A+\tfrac12 I\). Because every neighbor spin sum is an integer and has odd parity at boundary vertices, the tie-retaining update agrees exactly with \(\sigma_{t+1}=\operatorname{sgn}(W\sigma_t)\), with no zero coordinates. Put \(E_t=-\sigma_t^{\mathsf T}W\sigma_{t-1}\). Symmetry yields

\[
E_t-E_{t+1}=(\sigma_{t+1}-\sigma_{t-1})^{\mathsf T}W\sigma_t\ge0.
\]

Whenever \(\sigma_{t+1}\ne\sigma_{t-1}\), at least one summand is strictly positive because each coordinate of \(W\sigma_t\) is nonzero and \(\sigma_{t+1}\) has its sign. This energy takes values in a finite set, so eventually \(\sigma_{t+1}=\sigma_{t-1}\). The only possible recurrent primitive periods are one and two.

**Exact paired-column transfer.** A column of a pair \((x,y)\), with \(y=F_n(x)\) and \(x=F_n(y)\), is a symbol \(a\in\{0,\ldots,63\}\). Its three low bits are the \(x\)-column and three high bits the \(y\)-column. Define \(B(a,b)\in\{0,1\}\) as the conjunction of all six binary update equalities at the left boundary using \(a\) for the present column and \(b\) for its single neighbor. Define \(H(a,b,c)\) by the same six equalities at an interior column \(b\), using \(a,c\) for its left/right neighbors. In both tests the six equalities mean the three site updates \(F_n(x)=y\) and the three updates \(F_n(y)=x\); they use neighbor counts three at a boundary and four in the interior. Their explicit complete bitwise definitions appear in `verify.py`.

Index a transfer state by an ordered pair of column symbols \((a,b)\). Let \(T_P\) be the \(4096\times4096\) integer matrix with

\[
(T_P)_{(a,b),(b',c)}=\mathbf1_{b=b'}H(a,b,c),\quad
(v_P)_{(a,b)}=B(a,b),\quad(w_P)_{(a,b)}=B(b,a).
\]

There is a bijection between compatible length-\(n\) column sequences and transfer paths, including the second boundary, giving \(P_n=v_PT_P^{n-2}w_P\). A fixed-state transfer \((v_Q,T_Q,w_Q)\) uses one three-bit time slice per column, hence has \(64\) ordered-pair states and satisfies \(Q_n=v_QT_Q^{n-2}w_Q\).

**Finite exhaustive identities supplying an all-length proof.** Direct exhaustive integer evaluations of the fully defined local Boolean tests give \(9812\) transfer arcs and initial vector support \(200\) for \(T_P\), and \(182\) arcs and initial support \(16\) for \(T_Q\). With

\[
\begin{aligned}
p(z)&=(z^2-1)(z^3-2z^2+z-3)(z^4-4z^3+z^2-3z+9),\\
q(z)&=(z-3)(z^3-z^2-1),
\end{aligned}
\]

all \(4096\) coordinates of \(v_Pp(T_P)\) and all \(64\) coordinates of \(v_Qq(T_Q)\) are **exactly zero over the integers**. The supplied independent, finite source listing `verify.py` constructs every transfer edge from bit counts, computes the relevant vector powers and asserts the complete zero-vector identities, not merely a few scalar sequence terms. These checked finite identities imply the corresponding scalar recurrences for *every* \(n\ge2\).

The same finite computation gives

\[
\begin{aligned}
(P_2,\ldots,P_{10})&=(22,62,232,800,3028,11414,43096,162746,614878),\\
(Q_2,Q_3,Q_4,Q_5)&=(4,8,22,62).
\end{aligned}
\]

A recurrence of order nine (respectively four) and these exact initial values uniquely imply the rational functions displayed in the Finding; multiplying the series by their stated denominators gives precisely \(N_P\) and \(N_Q\). The primitive-orbit formula follows by pairing two states per primitive two-cycle.

**Asymptotics.** The quartic has two positive roots, one in \((1,1.5)\) and \(\lambda\in(3.5,4)\). Its other two roots are nonreal conjugates of modulus less than \(\sqrt{9/3.5}\), by their product and the derivative sign analysis. The cubic \(z^3-2z^2+z-3\) has a unique positive real root in \((2,3)\) and a complex-conjugate pair of modulus less than \(\sqrt{3/2}\); its derivative confirms uniqueness. The remaining poles arise from \(z=\pm1\). Thus \(\lambda\) is the unique dominant root. Its pole is simple and its coefficient is nonzero, yielding

\[
 P_n\sim c\lambda^n,\qquad
 c=-\frac{N_P(1/\lambda)}{\lambda D_P'(1/\lambda)}
 =1.03597111082\ldots>0.
\]

For fixed states, \(D_Q(z)=(1-3z)(1-z-z^3)\), with all roots of the second factor corresponding to exponential bases smaller than three. Its pole residue yields \(Q_n\sim(4/17)3^n\). Since \(\lambda>3\), the stated two-cycle entropy and probability limits follow.

## Verification

Run `python3 verify.py`, using Python 3 with no third-party packages. This checks the complete nine-step \(4096\)-coordinate transfer annihilator, four-step \(64\)-coordinate fixed-state annihilator, initial term tables, and exact generating-function numerators. The recorded output is `verification-output.txt`. For a distinct microscopic check, compile `direct.cpp` with `g++ -O3 -std=c++17 direct.cpp -o direct` and run `./direct`. It independently iterates each of the \(2^{3n}\) labelled configurations for all \(2\le n\le7\), compares one-step and two-step fixed sets, and also records numbers of flipping sites. This exhausts \(2^{6}+2^{9}+2^{12}+2^{15}+2^{18}+2^{21}=2{,}396{,}736\) configurations. Its actual output appears in `direct-output.txt`. This direct finite enumeration corroborates the exact transfer certificate; the all-length conclusion rests on the latter's finite integer annihilators.

## Relationship to prior work

Goles and Olivos established eventual period at most two in symmetric threshold networks. Benjamini, Chan, O'Donnell, Tamuz and Tan (2014) treat convergence and consensus on general and random graphs, and Kaaser, Mallmann-Trenn and Natale (2015) analyze convergence-time bounds. Those theorems do not determine a strip-specific count of initially periodic states. The published exact majority census on open two-row ladders \(P_n\square K_2\) has different local degree and a Lucas–Fibonacci law, and the published three-row *cyclic* triangular-cylinder result \(C_n\square K_3\) counts only fixed states. Neither statement directly implies the present exact open three-row two-cycle population or its quartic entropy root. The method of finite transfer matrices and the general period-two restriction are background, not claimed as new.

## Limitations

The result counts initial fixed and initial two-step recurrent states, not all attraction basins, transient-depth populations or their probabilities from random nonrecurrent initial states. It assumes a precisely specified open Cartesian graph and deterministic tie retention. The finite transfer identities are fully enumerated in ordinary integer code but have not undergone independent formal proof or external audit. Searches do not exclude unindexed earlier equivalent exact enumerations, and a few inaccessible historical works have not been inspected at full-text level. The date assigned to the archival research source is the verified 2014 public preprint date; earlier general threshold literature is cited by publication year without inventing a first-public day.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189; DOI `10.1016/0012-365X(80)90121-1`.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:`1405.2486v1`, first posted 2014-05-11, https://arxiv.org/abs/1405.2486.
3. D. Kaaser, F. Mallmann-Trenn and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:`1508.03519v1`, first posted 2015-08-14, https://arxiv.org/abs/1508.03519.
