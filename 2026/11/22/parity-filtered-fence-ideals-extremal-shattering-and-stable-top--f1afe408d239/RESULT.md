# Parity-filtered fence ideals: extremal shattering and stable top homology

## Finding

For every integer \(m\ge1\), let \(F_m\) be the height-two zigzag (fence) poset with minimal elements \(u_0,\ldots,u_m\), maximal elements \(v_1,\ldots,v_m\), and precisely the strict relations \(u_{i-1}<v_i\) and \(u_i<v_i\) for \(1\le i\le m\). Let \(\mathcal J_m^\epsilon\), for \(\epsilon\in\{0,1\}\), be the family of lower ideals of \(F_m\) whose cardinalities are congruent to \(\epsilon\) modulo two. Boolean queries test membership of individual elements of \(F_m\). Write \(\Delta_m^\epsilon\) for the simplicial complex of shattered query supports.

Both parity classes satisfy the **sharp one-unit loss**
\[
\operatorname{VCdim}(\mathcal J_m^0)=\operatorname{VCdim}(\mathcal J_m^1)=m,
\]
whereas the class of all lower ideals has VC dimension \(m+1\).

The complete classification of shattered supports of *maximum size* \(m\) is as follows. Both parity classes shatter exactly the \(m+1\) supports
\[
T_j=\{u_0,\ldots,u_m\}\setminus\{u_j\},\qquad 0\le j\le m,
\]
except that the odd-cardinality class shatters additional supports
\[
S_{a,r}=\{v_{a+1},\ldots,v_{a+r}\}\cup
\{u_i:0\le i<a\ \text{or}\ a+r<i\le m\},
\]
precisely when \(1\le r\le2\), \(0\le a\le m-r\), \(a\le1\), and \(m-a-r\le1\). (For the even-cardinality class there are no additional maximum supports.) Consequently,
\[
[z^m]\Phi_m^0(z)=m+1,\qquad
[z^m]\Phi_m^1(z)=m+1+\binom3{m-1},
\]
where \(\Phi_m^\epsilon(z)=\sum_{S\in\Delta_m^\epsilon}z^{|S|}\) and \(\binom3k=0\) outside \(0\le k\le3\). The odd-minus-even extremal-face difference is therefore \(1,3,3,1,0,0,\ldots\).

Furthermore the integral reduced homology in the *top dimension* is exactly
\[
\widetilde H_{m-1}(\Delta_m^0;\mathbb Z)\cong\mathbb Z,\qquad
\widetilde H_{m-1}(\Delta_m^1;\mathbb Z)\cong
\begin{cases}\mathbb Z^2,&m=1,2,\\\mathbb Z,&m\ge3.\end{cases}
\]
No claim about homology in other dimensions is made.

## Assumptions and scope

The poset is finite, labelled, and has exactly the stated relations; there is no wraparound between the two endpoints. An ideal is a downward-closed subset. A query support \(S\subseteq F_m\) is shattered by \(\mathcal J_m^\epsilon\) if every trace \(B\subseteq S\) occurs as \(I\cap S\) for some ideal \(I\in\mathcal J_m^\epsilon\). The usual reduced simplicial homology convention is used, including reduced degree zero at \(m=1\). The coefficient and homology assertions concern only the *top* faces; they are not formulas for every coefficient or every homology group.

## Proof

**1. Parity of traces of ideals.** Let \(P\) be any finite poset and \(S\) an antichain. For \(B\subseteq S\), set
\[
L_B=\downarrow B,\qquad U_B=P\setminus\uparrow(S\setminus B).
\]
Every ideal with trace \(B\) on \(S\) lies in the inclusion interval \([L_B,U_B]\), and conversely every ideal in that interval has exactly this trace. The antichain property ensures \(L_B\subseteq U_B\). If the endpoints differ, a minimal element of \(U_B\setminus L_B\) can be added to \(L_B\), so the interval contains ideals of two consecutive cardinalities and therefore **both parities**. If they coincide, the unique realization has parity \(|L_B|\bmod2\). Thus the only obstructions to parity-restricted shattering are *rigid* traces \(B\) with \(L_B=U_B\) and the wrong forced parity. A support with comparable elements cannot be shattered even by unrestricted ideals, since a trace containing the greater element but not the smaller is impossible.

**2. Size bound and the common supports.** The comparability graph of \(F_m\) is the path \(u_0-v_1-u_1-\cdots-v_m-u_m\), so an antichain has at most \(m+1\) elements. The only antichain of that size is the set of all minima: choosing any maximum forces omission of at least two minima, and, more generally, \(r\ge1\) selected maxima require omission of at least \(r+1\) distinct incident minima. On the all-minima support the empty trace has the unique empty ideal (even parity), whereas a singleton-minimum trace has the unique singleton ideal (odd parity), so neither parity class shatters it. Thus the parity VC dimensions are at most \(m\). For each \(T_j\), every trace \(B\subseteq T_j\) is realized by the two ideals \(B\) and \(B\cup\{u_j\}\); they have opposite parities. Hence every \(T_j\) is shattered by both parity classes, proving the asserted dimensions and common maximum faces. All proper subsets of the set of minima are also shattered; this will yield a boundary sphere.

**3. Classification of size-\(m\) antichains.** A size-\(m\) antichain containing \(r\ge1\) maxima must omit exactly \(r+1\) of the \(m+1\) minima. Regard the chosen maxima as \(r\) edges in the path on the minima, with \(v_i\) joining \(u_{i-1}\) to \(u_i\). Any \(r\) path edges touch at least \(r+1\) vertices, with equality exactly when the chosen edges are consecutive. Hence every size-\(m\) antichain is either some \(T_j\), or one and only one \(S_{a,r}\) with \(1\le r\le m\), \(0\le a\le m-r\).

**4. All rigid traces on \(S_{a,r}\).** A trace selects a subset \(E\) of the queried maxima \(v_{a+1},\ldots,v_{a+r}\) and a subset \(T\) of the queried minima outside \(u_a,\ldots,u_{a+r}\). The interval from Step 1 collapses to one ideal exactly when the following two conditions both hold:

- The selected edges \(E\) cover all \(r+1\) unqueried internal minima \(u_a,\ldots,u_{a+r}\). Equivalently, the first and last of the \(r\) edges belong to \(E\), and no two consecutive edges are omitted. Otherwise an uncovered internal minimum can be toggled without changing the trace.
- Every unqueried maximum outside the interval is prohibited by an excluded queried minimum. Equivalently, \(T\) contains no consecutive minima on either exterior side and contains no minimum adjacent to the central interval (\(u_{a-1}\) or \(u_{a+r+1}\), when present). Otherwise at least one unqueried maximum is optional; all external minima are themselves queried.

When these conditions hold the unique ideal consists of the \(r+1\) internal minima, the selected maxima \(E\), and the selected external minima \(T\). Its cardinality is
\[
(r+1)+|E|+|T|.
\]
This establishes necessity and sufficiency of the rigidity test, not just a list of examples.

**5. Parity classification and enumeration.** Choosing all \(r\) central maxima and no exterior minima is always rigid and has odd size \(2r+1\). Hence no \(S_{a,r}\) is shattered by the even class. For the odd class, if \(r\ge3\), remove one non-end central maximum from this rigid trace: all internal minima remain covered and the new unique ideal has even size \(2r\). Thus \(r\le2\) is necessary. For \(r=1,2\), both end edges are mandatory, so \(E\) must be the whole central interval. A nonempty allowed \(T\) produces an even-size rigid ideal if and only if some exterior side has at least two queried minima: take one not adjacent to the central interval. Thus the odd class shatters \(S_{a,r}\) exactly when \(r\in\{1,2\}\) and both exterior lengths \(a\) and \(m-a-r\) are at most one. There are \(1,3,3,1\) additional maximum supports for \(m=1,2,3,4\), respectively, and none afterward; these are precisely \(\binom3{m-1}\). This proves the complete asserted maximum-support classification.

**6. Exact top homology.** The \(m+1\) common top faces \(T_j\) form the boundary of an abstract \(m\)-simplex on \(u_0,\ldots,u_m\). There is no \(m\)-dimensional face because the VC dimension equals \(m\). For the even class, these are all the top faces, so its top reduced homology is \(\mathbb Z\). For the odd class, the same is true when \(m\ge5\). When \(m=4\), the sole extra top face \(\{u_0,v_2,v_3,u_4\}\) contains a codimension-one face with a maximum that belongs to no other top face, so it cannot participate in a top cycle. When \(m=3\), the three extras are \(\{u_0,v_2,u_3\}\), \(\{u_0,v_2,v_3\}\), and \(\{v_1,v_2,u_3\}\). In a top cycle, the coefficient of the second is zero by the unique edge \(\{u_0,v_3\}\), the coefficient of the third is zero by \(\{v_1,u_3\}\), and then the coefficient of the first is zero by \(\{u_0,v_2\}\). Thus the boundary-sphere generator is the entire top homology. For \(m=2\), the odd complex in top degree is the triangle on the three minima together with a three-edge path joining two of those minima through the two maxima: a connected graph with five vertices and six edges, hence \(H_1\cong\mathbb Z^2\). For \(m=1\), the odd complex consists of three isolated vertices, so \(\widetilde H_0\cong\mathbb Z^2\). Since the complexes have no cells above dimension \(m-1\), no quotient by higher boundaries occurs in top homology. This proves the integral statements.

## Verification

The standalone standard-library script `CHECK.py` independently enumerates ideals as bitmasks, constructs all size-\(m\) antichains, and tests each possible trace directly without using the rigidity lemma. It matches every predicted even/odd maximum face for \(1\le m\le8\) (328 antichain/parity comparisons). It checks that the unique size-\(m+1\) antichain is not shattered and computes top boundary-matrix ranks modulo a prime for \(1\le m\le5\), agreeing with the integral rank formulas. Run `python3 CHECK.py` in this package. These finite checks corroborate, but do not replace, the all-order proof above.

## Relationship to prior work

Fence ideal lattices and their cardinality-rank polynomials are classical. Oğuz and Ravichandran (2021) establish unimodality and interlacing properties of rank polynomials, and Elizalde and Sagan (2022) study partial rank symmetry and circular fences. Those results count ideals by total size and do not, from their stated theorems, determine the complete Boolean traces on a specified query support or distinguish top-dimensional parity-shattered faces. The distinct general fact that all ideals shatter precisely antichains is elementary background and is not a novelty claim. The present contribution is the **parity-specific rigid-trace classification**, the exact top-support formula, and the integral top-homology distinction for this connected incidence-poset family. This is not an unconditional claim of bibliographic priority; equivalent unindexed formulations may exist.

## Limitations

The theorem concerns odd-length, height-two alternating fences and parity modulo two. It does not determine every lower-degree face number, lower homology groups, Littlestone dimension, or arbitrary fence segment lengths. Finite enumeration is not offered as a proof beyond its checked range. A second independent mathematical assessment has not been performed, and a literature search cannot certify worldwide novelty.

## References

1. E. Kantarcı Oğuz and M. Ravichandran, *Rank Polynomials of Fence Posets are Unimodal*, first publicly posted 2021-12-01, arXiv:2112.00518, https://arxiv.org/abs/2112.00518 .
2. S. Elizalde and B. E. Sagan, *Partial Rank Symmetry of Distributive Lattices for Fences*, first publicly posted 2022-01-09, arXiv:2201.03044, https://arxiv.org/abs/2201.03044 .
