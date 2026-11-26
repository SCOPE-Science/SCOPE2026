# Three sequential transitions are enough to reverse an optimal block order

## Finding

In an irreversible continuous-time chain \(0\to1\to2\to3\), let a block specify a fixed duration and three strictly positive constant transition rates. The objective is to maximize absorption by the end of a prescribed finite multiset of blocks, each used once, with initial state \(0\). Blocks \(A,B,C\), all of duration \(\log 2\), with rate triples
\[
A=(4,1,2),\qquad B=(1,4,3),\qquad C=(8,1,2)
\]
give opposite strict preferences for the adjacent pair \(A,B\) with and without the prefix \(C\):
\[
 F(AB)-F(BA)=\frac{245}{768},\qquad F(CAB)-F(CBA)=-\frac{59245}{1376256}.
\]
Moreover, \(AB\) is the unique optimum for the two-block instance and \(CBA\) is the unique optimum for the three-block instance. Thus a fixed pair comparator cannot capture all strict swap preferences, and sorting by a fixed total order of individual blocks (including a fixed tie-break) cannot optimize all instances. Three is the smallest number of sequential transitions for either obstruction. The two-transition sorting rule below is a specialization of established affine composition ordering and is not claimed as new.

## Exact calculation

For \(r=(r_0,r_1,r_2)\), let \(G\) be the \(3\times3\) transient column generator: \(G_{jj}=-r_j\), \(G_{j+1,j}=r_j\) for \(j=0,1\), and other entries zero. Stage \(3\) is absorbing; probability lost from the transient coordinates is the completion probability. The three rates in each block of the example are distinct. For \(I\) the identity, the spectral projector at eigenvalue \(-r_j\) is \(\prod_{i\ne j}(G+r_i I)/(r_i-r_j)\), as is seen by evaluating this polynomial on the three eigenvalues. At time \(\log 2\) the projector's multiplier is \(2^{-r_j}\). It follows that the transient matrices are
\[
 R_A=\frac1{48}\begin{pmatrix}3&0&0\\28&24&0\\10&12&12\end{pmatrix},\quad
 R_B=\frac1{48}\begin{pmatrix}24&0&0\\7&3&0\\8&12&6\end{pmatrix},\quad
 R_C=\frac1{1792}\begin{pmatrix}7&0&0\\1016&896&0\\428&448&448\end{pmatrix}.
\]
For chronological blocks \(w_1,\ldots,w_k\), the absorption probability is \(1-\mathbf 1^\mathsf T R_{w_k}\cdots R_{w_1} e_0\), where \(\mathbf 1\) is the three-vector of ones and \(e_0=(1,0,0)^\mathsf T\). For \(AB,BA\) the numerators over \(768\) are \(569,324\), respectively. For the three-block instance the complete enumeration is:

| Chronological order | Numerator over \(1376256\) |
|---|---:|
| ABC | 1231672 |
| ACB | 1198687 |
| BAC | 902392 |
| BCA | 938120 |
| CAB | 1218287 |
| CBA | 1277532 |

In particular, the two unique optima require opposite relative orders for the same unchanged pair. This rules out an instance-independent deterministic ordering of individual blocks, but not a method which resolves ties using the whole instance or which optimizes over full states or schedules.

## Why one or two transitions cannot show the obstruction

For one transition, absorption is \(1-\exp(-\sum_i p_i t_i)\), independent of order. For two transitions, write \(p_i,q_i>0\) for the block rates, \(t_i>0\) for its duration, \(a_i=\exp(-p_i t_i)\), \(b_i=\exp(-q_i t_i)\), and set
\[
 J_i=\int_0^{t_i}e^{-p_i u-q_i(t_i-u)}\,du>0.
\]
The transient column coordinates \((x_0,x_1)\) update to \((a_i x_0,p_iJ_i x_0+b_i x_1)\). The first coordinate is always positive. Consequently \(z=x_1/x_0\) evolves under the strictly increasing affine map \(L_i(z)=s_i z+d_i\), where \(s_i=b_i/a_i>0\) and \(d_i=p_iJ_i/a_i>0\). Completion at the end is \(1-(\prod_i a_i)(1+z)\); it is maximized by minimizing the final \(z\).

The affine comparison is
\[
 L_j(L_i(z))-L_i(L_j(z))=d_j(1-s_i)-d_i(1-s_j),\qquad
 \frac{1-s_i}{d_i}=\frac{q_i}{p_i}-1.
\]
The latter equality uses \(a_i-b_i=(q_i-p_i)J_i\), valid also at equal rates. Thus decreasing \(p_i/q_i\) orders all pairs optimally; a strict inversion has a strictly improving adjacent swap, since every suffix map is strictly increasing. Equal ratios commute and can be ordered arbitrarily. This is the affine comparison and adjacent-exchange result of Kawase, Makino and Seimi, *Optimal Composition Ordering Problems for Piecewise Linear Functions*, arXiv:1601.05480, Sec. 3, Lemmas 8–10 and Eq. (6), applied after the transient normalization. Their maximum formulation also gives the minimum formulation by conjugation with \(z\mapsto-z\).

Kubo, Makino and Sakamoto, *Composition Orderings for Linear Functions and Matrix Multiplication Orderings*, arXiv:2402.10451, Theorems 3 and 4, prove a tractability result for simultaneously triangularizable \(2\times2\) matrices of nonnegative determinant and a hardness result for general nonnegative triangular matrices of dimension at least three. That broader hardness theorem does not establish an obstruction for this restricted class of positive-rate serial Markov propagators with a fixed initial vector and absorption objective. Conversely, the counterexample here makes no computational-hardness claim. Bak, Salamon and Andresen, DOI `10.1021/jp021800u`, study reversible consecutive chemical reactions with continuous temperature choice and an intermediate-yield objective rather than fixed-block absorption.

## Verification and scope

The displayed matrices and finite enumeration can be reproduced with `python3 verify.py` using exact rational arithmetic. The all-block one- and two-transition assertions follow from the given algebra, not from finite sampling. The result uses fixed durations, positive piecewise-constant rates, a serial irreversible memoryless chain, and no feedback or mortality. It is an ordering obstruction in an abstract Markov model, not a no-algorithm result and not an empirical development prediction. Classical affine ordering and first-order kinetics are established background; the contribution is the explicit smallest-stage obstruction in this restricted class.
