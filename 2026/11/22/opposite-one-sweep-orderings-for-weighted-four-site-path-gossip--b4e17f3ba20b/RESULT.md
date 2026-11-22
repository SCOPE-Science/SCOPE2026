# Opposite one-sweep orderings for weighted four-site path gossip

## Finding
Consider a four-site path with consecutive edges labelled \(1,2,3\). For each edge \(i\), exactly one symmetric convex averaging contact of strength \(p_i\in(0,1)\) is performed, in an arbitrary chronological order \(\pi\). With \(J=\mathbf 1\mathbf 1^{\mathsf T}/4\) and full-sweep matrix \(T_\pi\), define the isotropic and worst-case squared disagreement factors
\[
F_\pi=\|T_\pi-J\|_F^2,\qquad W_\pi=\|T_\pi-J\|_2^2.
\]
For **every** triple of contact strengths strictly between zero and one, exactly the four orders \((1,3,2),(3,1,2),(2,1,3),(2,3,1)\) minimize \(F_\pi\), while exactly the two monotone orders \((1,2,3),(3,2,1)\) minimize \(W_\pi\). Both inequalities are strict between these two classes. Nevertheless, all six full-sweep matrices have identical characteristic polynomials, so their asymptotic periodic-sweep spectral factors coincide.

Writing \(p=p_1\), \(q=p_2\), \(r=p_3\), and using subscripts \(S\) (monotone/serial) and \(B\) (outer contacts together, central contact first or last), the exact isotropic penalty of a monotone sweep is
\[
F_S-F_B=4pq^2r(1-p)(1-r)>0.
\]
More strongly, if \(\chi_S,\chi_B\) are the characteristic polynomials of the squared disagreement singular values on the three-dimensional mean-zero subspace, then
\[
\boxed{\chi_S(\lambda)-\chi_B(\lambda)=4pq^2r(1-p)(1-r)\,\lambda(1-\lambda).}
\]
This identity implies \(W_S<W_B\) despite \(F_S>F_B\).

For ordinary arithmetic averaging \(p=q=r=1/2\), the two exact error pairs are
\[
(F_S,W_S)=\left(\frac9{16},\frac{9+\sqrt{17}}{32}\right),\qquad
(F_B,W_B)=\left(\frac12,\frac12\right).
\]
Thus a monotone sweep reduces the worst-case squared error by about \(18\%\) relative to the outer-contact-together schedules, while increasing isotropic squared error by \(12.5\%\) relative to those schedules.

## Assumptions and scope
The state is a vector \(x\in\mathbb R^4\). A contact on edge \(i\) replaces the two incident states by the convex combinations with self-weight \(1-p_i\) and neighbor-weight \(p_i\). Equivalently,
\[
P_i=I-p_i(e_i-e_{i+1})(e_i-e_{i+1})^{\mathsf T},\quad
T_\pi=P_{\pi_3}P_{\pi_2}P_{\pi_1}.
\]
All three contacts are mandatory and used exactly once. Their strengths are fixed and individually arbitrary in the open interval \((0,1)\). No optimization of strengths, contact multiplicities, or longer horizons is asserted. If a centered initial random state has covariance \(I-J\), its expected squared error after the sweep is exactly \(F_\pi\); \(W_\pi\) is the maximum squared error ratio over deterministic, nonzero, mean-zero initial states. Endpoint strengths zero or one are excluded because strictness may fail.

## Proof
**1. Two possible singular spectra.** Nonadjacent edge contacts commute: \(P_1P_3=P_3P_1\). Moreover, each \(P_i\) is symmetric, so reversal of any chronological order transposes its full product, preserving all singular values. Hence the two monotone orders share one Gram spectrum, and the remaining four orders share another. We may represent them by chronological schedules \(S=(1,2,3)\) and \(B=(1,3,2)\). Each \(P_i\) fixes constants and preserves the mean; consequently \(J T=T J=J\), and the squared disagreement Gram is \(G=(T-J)^{\mathsf T}(T-J)\) with a zero eigenvalue along constants.

**2. Exact cubic comparison.** For either schedule, set
\[
a=\operatorname{tr}G,\quad b=\frac{(\operatorname{tr}G)^2-\operatorname{tr}(G^2)}2,
\quad c=\det(G+J).
\]
Then \(\det(\lambda I_4-G)=\lambda(\lambda^3-a\lambda^2+b\lambda-c)\). Since \(\det P_i=1-2p_i\) and the constant-direction eigenvalue of every \(T\) is one,
\[
c_S=c_B=(1-2p)^2(1-2q)^2(1-2r)^2.
\]
Expanding the displayed \(4\times4\) edge-update matrices in the trace formulas gives the two exact identities
\[
a_S-a_B=b_S-b_B=\delta,\qquad \delta=4pq^2r(1-p)(1-r)>0.
\]
The expansions, including the determinant identity, are reproduced with exact rational-polynomial arithmetic in `verify.py`; no numerical fitting is used. Therefore
\[
\chi_S(\lambda)-\chi_B(\lambda)=-\delta\lambda^2+\delta\lambda
=\delta\lambda(1-\lambda).
\]
In particular \(F_B=a_B<a_S=F_S\), giving the unique isotropic-optimal order class.

**3. Strict spectral-norm reversal.** On the mean-zero subspace each \(P_i\) is a Euclidean contraction. Equality of the norm after all three contacts would force equality at every individual contact, which in turn forces the original state to have identical values across each of the path's three edges. The only such mean-zero state is zero. Hence both Gram spectra are contained in \([0,1)\). Neither Gram is the zero matrix: a three-contact sweep cannot send both directional endpoint influences through the path, whereas every entry of \(J\) is positive. Let \(\beta=W_B\in(0,1)\) be the largest root of \(\chi_B\). For every \(\lambda\in[\beta,1)\), the monic cubic \(\chi_B(\lambda)\) is nonnegative because all its roots lie at or below \(\beta\). Therefore
\[
\chi_S(\lambda)=\chi_B(\lambda)+\delta\lambda(1-\lambda)>0
\quad (\beta\le\lambda<1).
\]
Since all the roots of \(\chi_S\) are below one, its largest root is strictly below \(\beta\), proving \(W_S<W_B\). No parameter exception occurs within the stated open cube.

**4. Common eigenvalues.** The characteristic polynomial of a product is unchanged by cyclic permutation of its three factors, and the two outer factors commute. Every permutation of three contacts can be related using these operations; thus all six transfer matrices have the same characteristic polynomial. This equality does not imply equal singular values or equal one-sweep errors.

## Verification
Run `python verify.py` after installing the two versions-compatible dependencies listed in `requirements.txt`. The checker performs exact symbolic comparisons of the trace, second elementary symmetric polynomial, determinant, and full transfer characteristic polynomial for all six orders. It independently confirms the arithmetic-average example and tests 100 explicit triples of positive strengths by floating-point linear algebra. The symbolic calculations are finite polynomial identities; the analytical eigenvalue-root comparison above, not the sample, certifies the continuum of admissible strengths.

## Relationship to prior work
Liu, Mou, Morse, Anderson and Yu's deterministic-gossip study proves order-invariance of the **transfer eigenvalues** for unweighted, ordinary pairwise averaging on trees and develops singular-value contraction metrics. The present statement requires more: it optimizes two different **one-sweep** norms across all orderings under three independently selectable (but fixed during scheduling) convex strengths. Equal-strength isotropic-optimal ordering on paths of arbitrary length has also been established separately; that specialization is not asserted to be new here. The additional conclusion is the strict opposite worst-case ordering for every positive strength triple and its explicit cubic comparison. Shi, Li, Johansson and Johansson analyze finite-time exact consensus and contact counts; those are different objectives from comparing the errors after precisely one use of each path edge.

## Limitations
The theorem is for four vertices and three once-only edge contacts; it does not claim an all-length classification, variable-strength optimization, or optimality for repeated finite horizons. It compares squared Euclidean error under common vertex scaling. It does not address asynchronous delays or arbitrary observation noise. Publication priority beyond the inspected literature is not established by a literature search alone. Independent verification has not been performed.

## References
1. J. Liu, S. Mou, A. S. Morse, B. D. O. Anderson and C. Yu, *Deterministic Gossiping*, Proceedings of the IEEE 99 (2011), 1505–1524. DOI: https://doi.org/10.1109/JPROC.2011.2159689 ; author-provided text: https://www.researchgate.net/publication/224251755_Deterministic_Gossiping .
2. G. Shi, B. Li, M. Johansson and K. H. Johansson, *Finite-time Convergent Gossiping*, 2012, https://arxiv.org/abs/1206.0992 .
