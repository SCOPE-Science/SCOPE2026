# The first row-anisotropy-induced nonreal hard-core zeros on an open ladder

## Finding
Let \(L_n=P_n\square K_2\) be the open two-row ladder with \(n\) rungs. Assign fugacity \(z\) to each upper vertex and \(tz\) to each lower vertex, where the *fixed row bias* \(t>0\) is constant along the ladder. Let \(P_n(z;t)\) denote its hard-core grand partition polynomial (the weighted independent-set polynomial). Then, for **every** \(t>0\), all zeros of \(P_n(\cdot;t)\) are simple and strictly negative for \(1\le n\le4\).

For five rungs, let \(v_*\) be the **unique positive real root** of
\[
G(v)=196v^7+1176v^6+22624v^5+56308v^4-31960v^3-299061v^2-419112v-179024,
\]
and define
\[
T=\frac{2+v_*+\sqrt{v_*(v_*+4)}}{2}=4.01178730250454\ldots.
\]
Then the zero geometry of the degree-five polynomial \(P_5(\cdot;t)\) is completely determined by the ratio \(t\):

- If \(T^{-1}<t<T\), it has five distinct strictly negative real zeros.
- If \(t=T^{-1}\) or \(t=T\), it has one negative double zero and three distinct simple negative zeros.
- If \(0<t<T^{-1}\) or \(t>T\), it has exactly three simple negative real zeros and one nonreal conjugate pair.

In particular, **five rungs are necessary and sufficient** for nonreal partition zeros under homogeneous-by-row positive anisotropy. The two critical ratios are reciprocal under row exchange. This is a finite-volume complex-fugacity effect; no positive-fugacity phase transition is asserted.

## Assumptions and scope
All horizontal and vertical nearest-neighbor pairs in \(L_n\) exclude simultaneous occupation, with no diagonal interactions. The two fugacity factors on each rung are \(z\) and \(tz\), and \(t>0\) is held fixed while \(z\) varies in the complex plane. The graph has free, not periodic, length boundaries. The theorem classifies \(1\le n\le5\); it does not assert an all-length classification for \(n>5\), and does not cover independently varying fugacities from rung to rung.

For an independent vertex set \(S\subseteq V(L_n)\), define its weight as \(z^{|S|}t^{|S\cap B|}\), where \(B\) is the lower rail, and sum over all independent sets. The resulting degree is exactly \(n\) when \(t>0\), with constant coefficient one and all other coefficients strictly positive.

## Proof

**1. An exact three-state transfer and reciprocity.** Let \(E_n,U_n,D_n\) be the partial partition polynomials for configurations whose rightmost rung is respectively empty, occupied above, or occupied below. The allowed predecessor states give
\[
\begin{aligned}
E_{n+1}&=E_n+U_n+D_n,\\
U_{n+1}&=z(E_n+D_n),\\
D_{n+1}&=tz(E_n+U_n),
\end{aligned}
\qquad(E_0,U_0,D_0)=(1,0,0).
\]
Thus \(P_n=E_n+U_n+D_n\). Swapping the rails gives the exact root-preserving identity \(P_n(z;t)=P_n(tz;t^{-1})\). The explicit polynomials for the nontrivial lengths are
\[
\begin{aligned}
P_2&=1+2(1+t)z+2tz^2,\\
P_3&=1+3(1+t)z+(t^2+6t+1)z^2+t(1+t)z^3,\\
P_4&=1+4(1+t)z+(3t^2+12t+3)z^2+6t(1+t)z^3+2t^2z^4,\\
P_5&=1+5(1+t)z+(6t^2+20t+6)z^2+(t^3+18t^2+18t+1)z^3\\
&\quad +(2t^3+12t^2+2t)z^4+t^2(1+t)z^5.
\end{aligned}
\]
Here \(P_1=1+(1+t)z\).

**2. Exact discriminant certificates.** Write \(y=t+t^{-1}\), so \(y\ge2\) for \(t>0\). Direct polynomial resultant expansion of the displayed coefficients, with the conventional discriminant sign \(\prod_{i<j}(r_i-r_j)^2\) times the appropriate positive leading-coefficient power, gives
\[
\begin{aligned}
\operatorname{Disc}_z(P_2)&=4(t^2+1),\\
\operatorname{Disc}_z(P_3)&=t^3(5y^3+81y-54),\\
\operatorname{Disc}_z(P_4)&=16t^6 J(y),\\
\operatorname{Disc}_z(P_5)&=-t^{10}H(y),
\end{aligned}
\]
where
\[
J(y)=27y^4-54y^3+117y^2-108y+20
\]
and
\[
H(y)=196y^7-1568y^6+24976y^5-154252y^4+344136y^3-415301y^2+263692y-54228.
\]
For \(v=y-2=(t-1)^2/t\ge0\),
\[
J(2+v)=27v^4+162v^3+441v^2+576v+272>0,
\]
while \(5y^3+81y-54>0\) for \(y\ge2\). Hence the discriminants of lengths two through four never vanish for positive \(t\).

At \(t=1\) the three-state transfer reduces to the second-order relation \(P_n(z;1)=(1+z)P_{n-1}(z;1)+zP_{n-2}(z;1)\), with \(P_0=1\), \(P_1=1+2z\). To establish real-rootedness without an unproved stability assumption, direct rational sign brackets give one root each in the following pairwise disjoint negative intervals (for \(n=1,2,3,4,5\) respectively):
\[
\begin{array}{l}
(-3/5,-2/5);\\
(-2,-3/2),\ (-2/5,-1/5);\\
(-16/5,-3),\ (-4/5,-3/5),\ (-1/4,-1/5);\\
(-4,-39/10),\ (-3/2,-13/10),\ (-9/20,-2/5),\ (-11/50,-1/5);\\
(-5,-4),\ (-5/2,-2),\ (-1,-1/2),\ (-2/5,-3/10),\ (-1/4,-1/5).
\end{array}
\]
The signs at each pair of endpoints differ by exact rational arithmetic (reproduced by the attached verifier). The degree bounds therefore force all \(n\) zeros to be simple negative real ones at \(t=1\). Since polynomial roots vary continuously as a multiset, positive discriminant and no collision for every \(t>0\) imply that the simple-negative root property persists for \(1\le n\le4\).

**3. One and only one five-rung collision.** Substitution into the fifth discriminant gives precisely \(H(2+v)=G(v)\), the seventh-degree polynomial in the finding. Its coefficients in descending degree have four positive signs followed by four negative signs; Descartes' rule permits **at most one positive root, counted with multiplicity**. Since \(G(0)=-179024<0\) and its leading coefficient is positive, there is exactly one, and it is simple. On \(t\ge1\), \(v=t+t^{-1}-2\) increases strictly from zero to infinity. Thus there is exactly one collision ratio \(T>1\), defined by \(G(v_*)=0\). Reciprocal row exchange gives the only other positive collision \(T^{-1}\).

At \(t=1\), all five roots are simple negative by the rational brackets. Until the first collision they stay distinct and real. At \(t=T\), the discriminant has a simple zero in \(t\) because \(G\) has a simple positive root and \(d(t+t^{-1})/dt>0\) at \(T>1\). A simple zero of the discriminant entails exactly one ordinary double root, with no other simultaneous collisions or higher multiplicity. The discriminant changes from positive to negative, and the two colliding real roots become a nonreal conjugate pair. For every \(t>T\), there are no further collision ratios. All remaining real roots are strictly negative, as the coefficients are positive. Reciprocal row exchange completes the classification for \(t<1\). This proves the theorem.

## Verification
The included `verify.py` (Python 3 with SymPy) independently enumerates all legal occupation patterns on lengths \(1\) through \(5\) at four exact rational activity ratios, checks the transfer-polynomial coefficients, the row-exchange identity, all exact discriminant identities and positive-coefficient certificates, Descartes' unique positive root via exact real-root counting, and all 15 disjoint rational sign brackets. It prints `ALL_EXACT_CHECKS_PASSED` when its tests pass. Symbolic computation checks the large displayed identities; the proof relies on the identities, sign arguments and root continuity, not on floating-point zero plots. The approximate value of \(T\) is informational only.

## Relationship to prior work
Wang and Zhu (arXiv:1008.2605, submitted 2010-08-16) prove a general real-rootedness/interlacing criterion for certain scalar second-order recurrences and examine independence polynomials of concatenated graphs. Their criterion applies to the row-symmetric \(t=1\) baseline, but not to the three-state row-biased transfer above; a claim of real-rootedness for all positive \(t\) would in fact be false at five rungs. Leake and Ryder (arXiv:1610.00805, first public 2016-10-04) characterize same-phase stability through claw-freeness for independently varied vertex weights, which does not determine the sharp **two-parameter homogeneous-by-row** zero collision or the minimal length. Zhu and Lu (arXiv:1507.05754, first public 2015-07-21) study unimodality and log-concavity of composite and multipartite independence polynomials, not this discriminant transition. The claim is an explicit restricted-family threshold, not a new general stability theorem.

## Limitations
The classification ends at length five and says nothing about further bands of nonreal zeros or limiting zero curves for longer strips. It concerns the zeros in *complex shared fugacity* \(z\), not a singularity on the physically positive fugacity axis. The previous literature comparison is based on inspected accessible primary documents and search; an older unindexed exact computation for the same small row-biased ladder remains a residual priority risk. No independent mathematical audit has been performed.

## References
1. Y. Wang and B.-X. Zhu, *On the unimodality of independence polynomials of some graphs*, arXiv:1008.2605 (first submitted 2010-08-16), https://arxiv.org/html/1008.2605v1.
2. J. Leake and N. Ryder, *Generalizations of the Matching Polynomial to the Multivariate Independence Polynomial*, arXiv:1610.00805 (first submitted 2016-10-04), https://arxiv.org/html/1610.00805v4.
3. B.-X. Zhu and Q. Lu, *Unimodality of the independence polynomials of some composite graphs*, arXiv:1507.05754 (first submitted 2015-07-21), https://arxiv.org/html/1507.05754v1.
