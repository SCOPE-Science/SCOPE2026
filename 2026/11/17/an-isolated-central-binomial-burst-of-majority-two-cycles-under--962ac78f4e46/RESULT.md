# An isolated central-binomial burst of majority two-cycles under matching-edge restoration

## Finding
Let \(n=2q+1\) be odd with \(q\ge1\). Choose labelled shore sets \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), and let
\[
G_{n,k}=K_{n,n}\setminus\{a_ib_i:1\le i\le k\},\qquad 0\le k\le n.
\]
Under synchronous binary open-neighbor majority with retention of the current bit on a tie, let \(C_2(n,k)\) be the number of distinct primitive temporal two-cycle orbits (labelled states; no quotient by spatial symmetries). Then
\[
\boxed{C_2(n,k)=1+3\binom{2q}{q}\,\mathbf1_{\{k=n-1\}}.}
\]
Thus the same graph family has exactly one primitive two-cycle at every deletion level except \(k=n-1\). At that unique level it has \(3\binom{n-1}{(n-1)/2}+1\) primitive two-cycles. Starting from the crown graph \(k=n\), restoring one deleted matching edge creates exponentially many cycles; restoring a second matching edge destroys all the additional cycles. The exceptional population grows as \(3\cdot4^q/\sqrt{\pi q}\) as \(q\to\infty\).

## Assumptions and scope
The graph is simple and loopless. At each simultaneous update, a vertex takes opinion \(1\) if strictly more than half of its neighbors hold \(1\), takes opinion \(0\) if strictly fewer than half do, and retains its own bit if the neighbor count ties. The matched pairs with missing edges are indexed by \(1,\ldots,k\); the remaining \(r=n-k\) pairs have their edges present. A periodic *state* \(x\) is a configuration satisfying \(F^2(x)=x\); a primitive two-cycle consists of two nonfixed states \(x,F(x)\). All enumeration is on labelled vertices. The result is an exact census of existing primitive periodic orbits, **not** of their attraction basins or entry times. The restriction to odd \(n\) is essential to the proof.

## Proof
**1. Reduction to four missing-pair types and uniform unmatched groups.** Write \(n=2q+1\), and let \(A_t,B_t\) be the numbers of ones in each shore at a given time. For each missing matched edge, let \((a_i,b_i)\in\{0,1\}^2\) be its two endpoint bits. This pair has degree \(2q\) at each endpoint; an unmatched vertex has degree \(2q+1\). Hence
\[
 a_i'=\operatorname{maj}_{2q}(B_t-b_i;a_i),\quad
 b_i'=\operatorname{maj}_{2q}(A_t-a_i;b_i),
\]
where \(\operatorname{maj}_{2q}(s;z)\) equals \(0\), \(1\), or \(z\) according as \(s<q\), \(s>q\), or \(s=q\). Any unmatched vertex of shore \(A\) updates to \(\mathbf1_{\{B_t\ge q+1\}}\), and likewise on shore \(B\). If \(r\ge1\), all unmatched vertices in a given shore are uniform after a single step; therefore they are already uniform in every configuration fixed by \(F^2\). Denote these two uniform bits by \(X,Y\), and let \(t_{00},t_{01},t_{10},t_{11}\) count the four types among the \(k\) missing pairs. Then
\[
 \sum_{a,b\in\{0,1\}}t_{ab}=k,\qquad
 A_t=t_{10}+t_{11}+rX,\quad B_t=t_{01}+t_{11}+rY.
\]
For \(r=0\), omit \(X,Y\). The correspondence records the actual pair type at each labelled index, not just totals, so there is no spurious inference of state periodicity from coincident counts.

**2. Four exact threshold regimes.** Classify an integer shore count \(s\) as \(L\) if \(s\le q-1\), \(M\) if \(s=q\), \(P\) if \(s=q+1\), and \(H\) if \(s\ge q+2\). For a matched endpoint with old bit \(z\) and its omitted partner's old bit \(w\), the update conditioned on the opposite shore's level is exactly
\[
 h_L(z,w)=0,\qquad h_M(z,w)=z(1-w),\qquad
 h_P(z,w)=1-w(1-z),\qquad h_H(z,w)=1.
\]
Thus, with current levels \(\ell_A,\ell_B\), the deterministic transition on a pair type is
\[
 T_{\ell_A,\ell_B}(a,b)=
 \bigl(h_{\ell_B}(a,b),h_{\ell_A}(b,a)\bigr).
\]
An unmatched shore bit becomes \(X'=\mathbf1_{\{\ell_B\in\{P,H\}\}}\), \(Y'=\mathbf1_{\{\ell_A\in\{P,H\}\}}\). Therefore each proposed two-step level sequence, support set of occupied pair types, and unmatched bits gives *linear integer constraints* on the type counts and \(q,r\). A labelled initial state is two-periodic precisely when the two consecutive pair-type transitions return every occupied type to itself and the unmatched bits return; it is fixed if the first transition already returns every occupied type and both unmatched bits.

**3. Exhaustive symbolic classification.** The included programs `exact_certificate.py`, `two_restorations_certificate.py`, and `crown_check.py` enumerate every pair of four-level shore categories at times zero and one and all supports of the four matched-pair types. They reject candidate regimes that fail the exact two-step return test. For each remaining regime they impose its exact linear inequalities, positivity of every occupied type, zero counts for other types, \(q\ge1\), and the correct sum condition. The cases are analyzed with rational Fourier–Motzkin elimination, which preserves existence over the reals; therefore each resulting contradiction also excludes every integer profile. No floating-point optimization, bounded-size extrapolation, or unexamined dynamical type is used in the certificate. Integer parameter restrictions are retained through inequalities; the surviving real profiles are then explicitly identified and realized for every admissible integer \(q\).

The exact classifications obtained are:

| Restored edges \(r\) | Candidate two-step regime/support systems | Real-feasible systems | Nonfixed periodic states |
| --- | ---: | ---: | --- |
| \(r=0\) | 172 | 2 | The two shore-opposite uniform configurations. |
| \(r=1\) | 296 | 8 | Two shore-opposite uniform configurations and six families each containing \(\binom{2q}{q}\) labelled states. |
| \(r\ge2\) | 488 | 4 | The two shore-opposite uniform configurations; the four systems include separate descriptions for \(k=0\) and \(k>0\). |

For \(r=1\), the six nonuniform families have \((X,Y)=(1,0)\) and respective occupied types \(\{00,10\},\{01,10\},\{10,11\}\), or \((X,Y)=(0,1)\) and types \(\{00,01\},\{01,10\},\{01,11\}\). In every case both occupied type counts are **exactly** \(q\): the certificate separately disproves both inequalities \(t<q\) and \(t>q\) in each candidate family (12 exact exclusion checks). Conversely, substituting any of these six half-and-half assignments into the displayed update equations verifies a genuine two-cycle for all \(q\ge1\). There are \(\binom{2q}{q}\) ways to choose the indices of either type, and the two uniform shore-opposite states also form a genuine two-cycle for every \(r\). In the \(r=0\) and \(r\ge2\) cases, the exact surviving supports force all matched pairs to share the shore-opposite type, so the two uniform configurations are the only primitive two-periodic states.

There are consequently \(2\) primitive-two-periodic states when \(r\ne1\), and \(6\binom{2q}{q}+2\) when \(r=1\). Dividing by two states per temporal orbit proves the formula.

## Verification
Reproduction with Python 3, standard library only: run `python3 exact_certificate.py`, `python3 two_restorations_certificate.py`, `python3 crown_check.py` and `python3 direct_verification.py` in the same directory. The first three programs implement exact integer Fourier–Motzkin elimination, with no numerical feasibility oracle. They report, respectively, 296 candidate systems with eight feasible; 488 candidates with four feasible; and 172 candidates with two feasible. The first also verifies 12 exclusions that force the six half-and-half profiles. The independently written direct vertex-bit implementation checks 22 graph instances and all 1,186,048 labelled configurations in those instances, including all deletion levels for sizes 3, 5, 7 and selected levels for size 9. The supplied output files give exact replay results. The proof for all odd orders is the symbolic constraint elimination and explicit construction; the vertex experiments are additional cross-checks.

## Relationship to prior work
The classical Goles–Olivos theorem gives the eventual period-at-most-two property for finite symmetric threshold networks, but that property alone does not count their orbits. Kuhlman, Mortveit, Murrugarra, and Kumar (2011) present a broader bi-threshold theory, including a translated proof of the Goles–Olivos theorem; the graph constructions and theorem statements inspected there do not give a matching-deletion orbit census. Benjamini, Chan, O'Donnell, Tamuz, and Tan (2014) study majority dynamics on unimodular and random graphs and likewise do not furnish the present special-graph classification. The new calculation isolates a discontinuous dependence on precisely one restored matching edge that is not determined by general period restrictions.

## Limitations
Only odd equal shore orders \(n\ge3\) and deletion of a **matching** are treated. The result counts pre-existing primitive two-cycle orbits, not transient lengths, attraction probabilities, fixed points, or arbitrary edge-deletion patterns. Historical priority is qualified by possible unindexed earlier graph-family enumerations and by the inability to inspect the original Goles–Olivos articles in full. The exact algebraic certificate and its interpretation have had no independent mathematical audit.

## References
1. C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974 (first arXiv submission 2011-08-15), §§3–4 and Appendix A. https://arxiv.org/abs/1108.2974
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486 (first arXiv submission 2014-05-11). https://arxiv.org/abs/1405.2486
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189. DOI: 10.1016/0012-365X(80)90121-1.
