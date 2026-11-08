# Exact primitive-three wave census on open ladders

## Finding

For every integer \(n\ge3\), let \(L_n=P_n\square K_2\) be the labelled open ladder with rungs indexed \(1,\ldots,n\), and give its vertices the synchronous three-state Greenberg–Hastings rule. The number \(N_n\) of initial configurations whose **least** temporal period is three is characterized by

\[
N_3=6,\qquad N_4=24,\qquad N_5=90,\qquad
N_n=4N_{n-1}-N_{n-2}-2N_{n-3}\quad(n\ge6).
\]

Equivalently, the generating function and its factorization are

\[
\sum_{n\ge3}N_nz^{n-3}=\frac{6}{1-4z+z^2+2z^3}
=\frac{6}{(1-z)(1-3z-2z^2)}.
\]

The first counts, for \(3\le n\le11\), are \(6,24,90,324,1158,4128,14706,52380,186558\). Exactly \(N_n/3\) distinct temporal three-cycles occur. For \(n=1\) or \(2\), the count is zero. The exponential growth rate is

\[
\lim_{n\to\infty}N_n^{1/n}=\frac{3+\sqrt{17}}2.
\]

For a uniformly random initial configuration, the probability of immediate primitive-three periodicity equals \(N_n/9^n\), so it decreases exponentially at rate \((3+\sqrt{17})/18\) per added rung.

## Assumptions and scope

The open ladder has vertices \((i,r)\), where \(1\le i\le n\) and \(r\in\{0,1\}\). The undirected edges are \((i,0)(i,1)\) and \((i,r)(i+1,r)\) whenever both endpoints exist; there is no longitudinal wrap-around. Each vertex has state in \(\mathbb Z/3\mathbb Z\), interpreted as resting \(0\), excited \(1\), and refractory \(2\). Under one simultaneous update, \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) exactly if an adjacent vertex is in state \(1\), otherwise \(0\mapsto0\). All rungs and vertices are labelled; different temporal phases are counted separately. Only configurations already periodic at the initial time are counted, not eventual periodicity or transient basins.

## Proof

**Local reduction.** On any finite connected graph, an initial state fixed by the third iterate is either the all-resting fixed state or advances every vertex by one modulo three at each time. Indeed, a nonzero vertex in a three-periodic state must follow the forced path through its three states; a zero vertex can either remain zero throughout or follow the same full path. If a permanently zero vertex were adjacent to a cycling vertex, it would have an excited neighbor on one of the three steps and hence could not stay zero. Connectivity rules out coexistence. Thus a nontrivial configuration is a primitive three-periodic configuration exactly when every vertex has a neighbor with the successor of its initial color (modulo three). Sufficiency holds because this property persists when every color is simultaneously incremented.

**A normalized transfer.** Define \(V(C;L,R)\) to be one if the two vertices of rung \(C=(c_0,c_1)\) each have a neighbor of color \(c_r+1\pmod3\) among their vertical mate and their existing left and right rung-mates \(L,R\), and zero otherwise. The symbol \(\varnothing\) denotes an absent end rung. All colors below are modulo three. Normalize the top vertex of the current rung to color zero, and encode the previous and current rungs as

\[
L=(e,e+p),\qquad C=(0,q),\qquad (e,p,q)\in(\mathbb Z/3\mathbb Z)^3.
\]

Index the following vectors and integer matrix by these 27 triples:

\[
\begin{aligned}
 a_{e,p,q}&=V\big((e,e+p);\varnothing,(0,q)\big),\\
 b_{e,p,q}&=V\big((0,q);(e,e+p),\varnothing\big),\\
 M_{(e,p,q),(e',p',q')}&=\sum_{x,d\in\mathbb Z/3\mathbb Z}
 V\big((0,q);(e,e+p),(x,x+d)\big)
 \mathbf1\{(e',p',q')=(-x,q,d)\}.
\end{aligned}
\]

Here \(a\) is a row vector, \(b\) a column vector, and \(M\) a nonnegative integer matrix. The new state arises by shifting the next rung's top color \(x\) to zero. A global addition of one common color leaves validity invariant and has exactly three choices. Consequently, the precise count including both free ends is

\[
N_n=3aM^{n-2}b\qquad(n\ge2).
\]

**Finite structural identity.** A complete 27-component calculation, directly using the displayed definitions, gives

\[
M^3b=4M^2b-Mb-2b.
\]

For transparency, the 27 triples fall into the following five classes according to the four integer entries \((b,Mb,M^2b,M^3b)\). Triples are written as the three digits \(e,p,q\):

| Triples | Values \((b,Mb,M^2b,M^3b)\) |
|---|---|
| 000, 020, 200, 210 | (0, 0, 0, 0) |
| 001, 002, 011, 012, 022, 101, 121, 202, 211, 212, 221, 222 | (0, 0, 1, 4) |
| 010, 110, 120, 220 | (0, 1, 2, 7) |
| 021, 102, 111, 112, 122, 201 | (1, 2, 6, 20) |
| 100 | (1, 3, 7, 23) |

This exhibits and proves the identity componentwise, without numerical interpolation or reliance on a finite sequence prefix. Moreover, direct multiplication gives \(3ab=0\), \(3aMb=6\), \(3aM^2b=24\), and \(3aM^3b=90\). Multiplication of the matrix identity by \(3aM^{n-5}\) yields the claimed recurrence for all \(n\ge5\), hence in particular for every \(n\ge6\) with the three stated initial values. Standard generating-function algebra now yields the rational expression.

**Primitive periods and growth.** A nonfixed state satisfying the local reduction has exactly three successive configurations before returning, so division by three counts its distinct cycles. The transfer gives no such states on \(L_2=C_4\), and the single rung also has none. For \(n\ge3\), the recurrence and its positive transfer interpretation give \(N_n>0\). The factorization of the denominator has simple reciprocal roots \(1\), \((3+\sqrt{17})/2\), and \((3-\sqrt{17})/2\); its largest positive root has nonzero positive coefficient, establishing the exponential limit and the stated uniform-random initial probability.

## Verification

The standalone standard-library script `verify_transfer.py` reconstructs all 27 states and verifies all components of the cubic identity exactly, and checks the recurrence through \(n=71\). The independent script `verify_direct.py` uses the original vertex-wise update rather than the normalized transfer, iterates all \(597861\) ternary configurations for \(2\le n\le6\) through three updates, and compares the count of nonfixed three-periodic states with a distinct unnormalized 81-state color-pair transfer through \(n=30\). Both scripts passed from the included files; text outputs are bundled. These are finite and exact tests; the unrestricted conclusion follows from the 27-component matrix identity and local reduction, not from extrapolating enumerated lengths.

## Relationship to prior work

Durrett and Steif (1991), Section 5, Lemma 6, use initial 'clocks' to characterize eventual three-periodic behavior in finite boxes; this does not enumerate initial primitive-three states on open two-rail strips. Gravner, Lyu and Sivakoff (2016), Sections 1–2, develop universal-cover comparisons and asymptotic activity criteria on arbitrary graphs; those results provide the dynamical foundation but do not state the rational ladder census or its cubic recurrence. The earlier Greenberg–Greene–Hastings (1980) paper gives a winding-number characterization of two-dimensional periodic patterns; its full text was inaccessible in this check, and any equivalent enumeration within it is an unresolved priority risk. No covering claim was found among searched published mathematical records or the accessible relevant historical results. A generic finite-width transfer algorithm would not itself imply the unexpectedly low-degree rational denominator without the explicit 27-state reduction and identity.

## Limitations

The theorem counts only immediate primitive temporal period three, not periodic states of other primitive periods or states that enter three-cycles after a transient. The ladder is open at both longitudinal ends and has two rows; adding wrap-around edges changes the boundary vectors and generally the census. All claims are unconditional for every stated \(n\), but originality remains subject to independent expert literature verification, especially the unavailable 1980 full text and possible alternative descriptions as directed cyclic-dominating colorings. No independent audit has been performed.

## References

1. R. Durrett and J. E. Steif, *Some rigorous results for the Greenberg–Hastings Model*, Journal of Theoretical Probability 4 (1991), 669–690, DOI: 10.1007/BF01259549. Available author PDF: https://sites.math.duke.edu/~rtd/reprints/paper66.pdf.
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, public preprint submitted March 22, 1993, https://arxiv.org/abs/patt-sol/9303002.
3. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, preprint submitted October 24, 2016, https://arxiv.org/abs/1610.07320.
4. J. M. Greenberg, C. Greene, and S. P. Hastings, *A combinatorial problem arising in the study of reaction-diffusion equations*, SIAM J. Algebraic Discrete Methods 1 (1980), 34–42, DOI: 10.1137/0601006 (abstract inspected; full text unavailable).
