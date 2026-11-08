# Sharp Hausdorff isolation and entropy-zeta profiles of sparse periodic binary orbits

## Finding
Let \(q\ge2\). For the two-sided binary shift with the coordinate metric defined below, let \(P_q\) be the orbit of the periodic word consisting of one marker followed by \(q-1\) zeros. The closed hyperspace ball at observational radius \(2^{-(r+1)}\) has an exact entropy-maximizing subsystem. Writing \(m=2r+1\), its entropy is
\[
H_q(r)=\begin{cases}\log\lambda_m,&m<q,\\0,&m\ge q,\end{cases}
\qquad \lambda_m^m=\lambda_m^{m-1}+1,\quad\lambda_m>1.
\]
When \(m<q\), the maximizer is unique: the minimum-marker-spacing subshift \(Y_m\). In that case its periodic-point generating function is
\[\zeta_{Y_m}(z)=\frac1{1-z-z^m}.\]
When \(m\ge q\), the ball is the single orbit \(P_q\), whose zeta function is \(1/(1-z^q)\). The closest other nonempty invariant subshift to \(P_q\) has distance exactly \(2^{-\lfloor q/2\rfloor}\). The maximum entropy at the last nonsingleton scale is asymptotic to \(W(q)/q\) as \(q\to\infty\), where \(W\) is the principal real Lambert function. These assertions give a complete finite-resolution entropy-and-periodic-data envelope for this distinguished family of periodic subsystem points.

## Assumptions and scope
The ambient space is \(\Sigma=\{0,1\}^{\mathbb Z}\) under the left shift \(\sigma\). For distinct sequences set \(d(x,y)=2^{-\min\{|j|:x_j\ne y_j\}}\); set \(d(x,x)=0\). All hyperspace elements are nonempty compact \(\sigma\)-invariant subsets, so they are two-sided subshifts. Hausdorff distance is the maximum of the two directed point-to-set distances. For an integer \(r\ge0\), define
\[\mathcal B_r(q)=\{X:d_H(X,P_q)\le2^{-(r+1)}\},\quad m=2r+1.\]
The word \(10^{q-1}\) is repeated in both directions and its \(q\) rotations make up \(P_q\). Define \(Y_m\) by the condition that any two markers \(1\) have index separation at least \(m\); when \(m=1\), \(Y_1\) is the full binary shift. Entropy means topological entropy of the shift restricted to a subsystem. A primitive periodic orbit of length \(p\) is an orbit of least period \(p\).

## Proof
**1. A Hausdorff ball is an exact-language cylinder.** With this metric, \(d(x,y)\le2^{-(r+1)}\) if and only if \(x_j=y_j\) for all \(|j|\le r\). Compactness ensures the point-to-set distance is attained. Applying shift invariance to all translated center windows yields
\[X\in\mathcal B_r(q)\quad\Longleftrightarrow\quad \mathcal L_m(X)=\mathcal L_m(P_q),\qquad m=2r+1,\]
where \(\mathcal L_m(Z)\) is the set of length-\(m\) contiguous words occurring in the subshift \(Z\). Both inclusions are necessary because Hausdorff distance is two-sided; both are sufficient because every central word can be matched to a point of the other subsystem.

**2. The largest admissible subshift.** Let \(U_m(P_q)\) contain every bi-infinite sequence whose length-\(m\) words occur in \(P_q\). Every member of \(\mathcal B_r(q)\) lies in \(U_m(P_q)\); since \(P_q\subset U_m(P_q)\), this last subshift has precisely the required \(m\)-language and itself belongs to the ball. It is the inclusion-largest member.

If \(m<q\), the period-\(q\) pattern has either zero or exactly one marker in each length-\(m\) word, and every position of a single marker occurs. Therefore \(U_m(P_q)=Y_m\). If \(m=q\), the permitted words are precisely the length-\(q\) binary words with exactly one marker. A sequence all of whose \(q\)-windows have one marker satisfies \(x_{j+q}=x_j\), by subtracting the marker counts in consecutive windows. Such a sequence has precisely one marker per period and hence lies in \(P_q\). For \(m>q\), the same conclusion follows by restriction to length-\(q\) factors. Thus \(U_m(P_q)=P_q\) for every \(m\ge q\). The orbit has exactly \(q\) points fixed by \(\sigma^n\) whenever \(q\) divides \(n\), and zero otherwise; its zeta function is consequently \(1/(1-z^q)\).

**3. Entropy, uniqueness, and periodic zeta.** For \(m\ge1\), use \(m\) marker-gap states recording the number of zeros since the preceding marker, capped at \(m-1\). Each state advances by a zero, with the capped state remaining capped; a one is possible only from the capped state and resets to the initial state. The adjacency matrix \(A_m\) has transitions \(i\to i+1\) for \(0\le i<m-1\), a loop at \(m-1\), and a transition \(m-1\to0\). For \(m=1\) the two transitions coincide and have multiplicity two. The edge labeling is one-to-one on bi-infinite paths, since every marker resets the counter and unmarked tails have the unique saturated continuation. Thus this primitive graph presents \(Y_m\). The characteristic polynomial is \(t^m-t^{m-1}-1\), and hence its Perron eigenvalue is the unique \(\lambda_m>1\) solving that equation. Thus \(h_{\rm top}(Y_m)=\log\lambda_m\).

The matrix determinant identity gives \(\det(I-zA_m)=1-z-z^m\). The equality between the number of period-dividing-\(n\) points of this edge shift and \(\operatorname{tr}(A_m^n)\) yields
\[\zeta_{Y_m}(z)=\exp\left(\sum_{n\ge1}\frac{\operatorname{tr}(A_m^n)}n z^n\right)=\frac1{1-z-z^m}.\]
For \(m\ge2\), the set of least periods of \(Y_m\) is exactly \(\{1\}\cup\{p\ge m\}\): the all-zero fixed point supplies period one, and a single marker repeated with spacing \(p\) supplies each \(p\ge m\), while no nonzero periodic point can have smaller period. For \(m=1\), every positive period occurs.

The mixing shift of finite type \(Y_m\) has a unique measure of maximal entropy with full support. A proper subshift \(X\subsetneq Y_m\) cannot carry this measure. Every subshift carries a measure attaining its topological entropy (expansiveness makes the measure-entropy map upper semicontinuous); uniqueness and full support therefore force \(h_{\rm top}(X)<h_{\rm top}(Y_m)\). Thus the maximum in the hyperspace ball is unique for \(m<q\). For \(m\ge q\), the ball is a singleton.

**4. Sharp distance and scaling.** The first integer \(r\) for which \(2r+1\ge q\) is \(r=\lfloor q/2\rfloor\). At the preceding level, \(r=\lfloor q/2\rfloor-1\), the member \(Y_{2r+1}\ne P_q\) lies in the ball, whereas every distinct subshift is excluded at the finer level. Since Hausdorff distances take values in \(\{2^{-k}:k\ge0\}\cup\{0\}\), the smallest positive distance from \(P_q\) is exactly \(2^{-\lfloor q/2\rfloor}\).

At the last nonsingleton level set \(m_q=2\lfloor q/2\rfloor-1=q+O(1)\). With \(h_m=\log\lambda_m\), the Perron equation becomes \((1-e^{-h_m})e^{mh_m}=1\). As \(m\to\infty\), any fixed lower bound \(h_m\ge\varepsilon>0\) would make the left-hand side diverge, so \(h_m\to0\). If \(mh_m\) stayed bounded along a subsequence, the left side would be at most \(h_m e^{mh_m}=O(1/m)\), a contradiction. Hence \(mh_m\to\infty\), and \((1-e^{-h_m})/h_m\to1\) yields \((mh_m)e^{mh_m}=m(1+o(1))\). Inverting via the increasing Lambert function gives \(h_m\sim W(m)/m\), and hence \(h_{m_q}\sim W(q)/q\). This is a one-sided pre-isolation asymptotic; the entropy at the next scale is exactly zero.

## Verification
The reproducible standard-library script `verify.py` performs cyclic-language checks for \(2\le q\le11\), word lengths through \(q+2\), and all binary periodic words of lengths through nine. It checks the gap-law root equation, independent transfer-matrix traces against exhaustive periodic-point counts for selected sizes, and the closed-language threshold. The executed script printed `VERIFY_OK checks=87555` and `VERIFY_ZETA_OK total_checks=87651`. The results are finite diagnostics; the infinite and all-size claims follow from the proof above.

## Relationship to prior work
Flores-Concha (arXiv:2610.40438v1) proves generic structural and entropy properties of compact invariant subsystems of Smale spaces. Its Section 2 introduces finite-step SFT approximations and Section 3 establishes isolation of NMC subsystems, while its entropy statements are qualitative; the explicit sharp metric isolation radius and all-resolution entropy-and-zeta profile for \(P_q\) are not given there. Pavlov and Schmieding (arXiv:2203.15159) establish qualitative isolation of periodic/NMC subshifts in the Hausdorff space; their Rauzy graph machinery is an important precursor. The entropy equation for an \(S\)-gap shift is classical and appears explicitly in Ramirez and Somers (arXiv:2501.08438); **the equation by itself is not asserted to be new**. The statement assessed here is the combined exact hyperspace-radius classification, unique maximum-entropy subsystem at each nonsingleton resolution, and periodic zeta envelope.

## Limitations
The conclusion is for the explicitly normalized coordinate ultrametric and the family of binary orbits containing one marker per period. A change in the metric normalization changes the numerical radii. It does not classify arbitrary periodic binary words or the full family of subsystem entropies inside each ball. The characterization uses known general facts about mixing shifts of finite type and known gap-shift entropy formulas; independent historical-priority confirmation remains open.

## References
1. Ángela Flores-Concha, *On generic subsystems of a Smale space*, arXiv:2610.40438v1, publicly posted 2026-10-29, https://arxiv.org/abs/2610.40438.
2. Ronnie Pavlov and Scott Schmieding, *On the structure of generic subshifts*, arXiv:2203.15159, https://arxiv.org/abs/2203.15159.
3. Cristian Ramirez and Amy Somers, *(S,w)-Gap Shifts and Their Entropy*, arXiv:2501.08438, https://arxiv.org/abs/2501.08438.
4. Douglas Lind and Brian Marcus, *An Introduction to Symbolic Dynamics and Coding*, Cambridge University Press, 1995, Chapter 4 (standard symbolic-entropy background).
