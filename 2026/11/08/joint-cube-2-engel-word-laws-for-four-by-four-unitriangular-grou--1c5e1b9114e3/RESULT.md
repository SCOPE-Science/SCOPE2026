# Joint cube–2-Engel word laws for four-by-four unitriangular groups over finite fields

## Finding

Let \(q=p^e\) be any prime power, let \(G=\operatorname{UT}_4(\mathbb F_q)\), and choose \(X,Y\) independently and uniformly in \(G\). Write
\[
W=[[X,Y],Y],\qquad C=\{X^3=I\},\qquad Z(z)=I+zE_{14}\quad(z\in\mathbb F_q).
\]
Use the group commutator convention \([x,y]=x^{-1}y^{-1}xy\). All values of \(W\) lie in the center \(\{Z(z):z\in\mathbb F_q\}\).

Define
\[
t_q=\begin{cases}q^2+q-1,&p=2,\\3q-2,&p\ne2.\end{cases}
\]
**Complete 2-Engel word-value distribution.** For each \(z\in\mathbb F_q\),
\[
\mathbb P(W=Z(z))=
\begin{cases}
\dfrac{q^3+(q-1)t_q}{q^4},&z=0,\\[3pt]
\dfrac{q^3-t_q}{q^4},&z\ne0.
\end{cases}
\tag{1}
\]
**Complete joint cube/Engel value law.** For each \(z\in\mathbb F_q\),
\[
\mathbb P(C\ \text{and}\ W=Z(z))=
\begin{cases}
\dfrac{6q^2-8q+3}{q^4},&p=3,\ z=0,\\[3pt]
\dfrac{3(q-1)^2}{q^4},&p=3,\ z\ne0,\\[3pt]
q^{-6},&p\ne3,\ z=0,\\[3pt]
0,&p\ne3,\ z\ne0.
\end{cases}
\tag{2}
\]
In characteristic three,
\[
\mathbb P(C)=\frac{3q^2-3q+1}{q^3},\qquad
\mathbb P(W=Z(z)\mid X^3\ne I)=\frac1q\quad\text{for every }z\in\mathbb F_q.
\tag{3}
\]
Thus averaging over **non-cubic-identity elements** produces an exactly uniform central 2-Engel word value, including zero. This conditional uniformity is specific to the event \(X^3\ne I\) over characteristic-three fields. For the two events \(C\) and \(W=I\), their covariance is strictly positive:
\[
\mathbb P(C,W=I)-\mathbb P(C)\mathbb P(W=I)
=\begin{cases}
\dfrac{(q-1)^4(3q-2)}{q^7},&p=3,\\[3pt]
q^{-6}\left(1-\dfrac{q^3+(q-1)t_q}{q^4}\right),&p\ne3.
\end{cases}
\tag{4}
\]
For \(q=3^e\to\infty\), the joint zero-event probability is asymptotic to \(6/q^2\), whereas the product of marginal zero-event probabilities is asymptotic to \(3/q^2\). The ratio tends to two.

## Assumptions and scope

The group is the full group of upper unitriangular \(4\times4\) matrices over an arbitrary finite field, with prime-power order \(q\ge2\). Every group element has a unique six-tuple \((a,b,c,d,e,f)\in\mathbb F_q^6\) representing
\[
U(a,b,c,d,e,f)=
\begin{pmatrix}
1&a&d&f\\
0&1&b&e\\
0&0&1&c\\
0&0&0&1
\end{pmatrix}.
\]
All probabilities refer to independent uniform group elements, not to uniform conjugacy classes. The central value \(z\) in (1) and (2) is a specified field element. The finite-field calculations use characteristic-sensitive identities, not an assumption that \(q\) is prime. The same formula for (2) is not claimed for other nilpotent groups or other unitriangular sizes.

## Proof

**1. Commutator coordinates.** Write \(X=U(a,b,c,d,e,f)\) and \(Y=U(A,B,C,D,E,F)\). Direct multiplication yields
\[
U(a,b,c,d,e,f)U(A,B,C,D,E,F)
=U(a+A,b+B,c+C,d+D+aB,e+E+bC,f+F+aE+dC).
\]
Using \([x,y]=x^{-1}y^{-1}xy\) twice, or tracking the lower central series of \(G\), gives
\[
[[X,Y],Y]=Z\bigl(aBC-2bAC+cAB\bigr).\tag{5}
\]
In particular all six second-and-higher-superdiagonal coordinates of the pair are irrelevant to \(W\); for any fixed first-superdiagonal coordinates of \(X,Y\), there are \(q^6\) corresponding ordered pairs in \(G^2\). The six first-superdiagonal coordinates are jointly uniform in \(\mathbb F_q^6\).

**2. Unconditional fibers.** For fixed \((A,B,C)\), the value in (5) is the linear functional on \((a,b,c)\) with coefficient vector \((BC,-2AC,AB)\). It has \(q^3\) preimages of zero and none of nonzero outputs when that coefficient vector is zero; otherwise, every field element has exactly \(q^2\) preimages. The zero coefficient vector occurs for \(t_q\) triples: in odd characteristic these are precisely the triples with at most one nonzero coordinate, giving \(3q-2\); in characteristic two the alternatives are \(B=0\) (\(q^2\) triples) and \(B\ne0,A=C=0\) (\(q-1\) triples), giving \(q^2+q-1\). Counting six-coordinate pairs gives (1): the zero fiber has size \(t_q q^3+(q^3-t_q)q^2\), and each nonzero fiber has size \((q^3-t_q)q^2\), out of \(q^6\).

**3. Cube word.** The group has order \(q^6=p^{6e}\). If \(p\ne3\), the only group element satisfying \(X^3=I\) is \(I\); its Engel output with any \(Y\) is \(I\). This gives the last two lines of (2). If \(p=3\), write \(X=I+N\). Because \(N^4=0\), the binomial theorem in characteristic three gives \(X^3=I+N^3=I+abcE_{14}\), so
\[
C\ \Longleftrightarrow\ abc=0.
\]
There are \(N_0=q^3-(q-1)^3=3q^2-3q+1\) such triples \((a,b,c)\), and \(\mathbb P(C)=N_0/q^3\).

**4. Joint fibers in characteristic three.** The coefficient \(-2\) in (5) equals \(1\) in characteristic three, so the central value becomes \(aBC+bAC+cAB\). Classify \((A,B,C)\) by its number of nonzero coordinates:

- At most one nonzero: \(3q-2\) triples, with central output zero for all \(N_0\) cube-identity first triples.
- Exactly two nonzero: \(3(q-1)^2\) triples. The central output is a fixed nonzero scalar times the missing first coordinate. For output zero, the cube restriction permits \(q^2\) first triples; for each prescribed nonzero output it permits \(2q-1\) first triples (at least one of the remaining two coordinates vanishes).
- All three nonzero: \((q-1)^3\) triples. Rescale \(u=a/A,\ v=b/B,\ w=c/C\). The word value is \(ABC(u+v+w)\), while \(C\) becomes \(uvw=0\). On \(u+v+w=s\), the union of the three coordinate lines has \(3q-2\) points for \(s=0\), and \(3q-3\) points for \(s\ne0\), by inclusion-exclusion (the three pairwise intersections coalesce only for \(s=0\)).

Consequently the number of six-coordinate pairs with \(C\) and \(W=I\) is
\[
(3q-2)N_0+3(q-1)^2q^2+(q-1)^3(3q-2)
=q^2(6q^2-8q+3).
\]
For each given nonzero central value, the number is
\[
3(q-1)^2(2q-1)+(q-1)^3(3q-3)=3q^2(q-1)^2.
\]
Division by \(q^6\) proves the first two lines of (2).

**5. Conditional uniformity, covariance and boundaries.** Subtracting the joint fibers from (1), in characteristic three the probability of \(X^3\ne I\) together with **each** fixed central value is exactly
\[
\frac{(q-1)^3}{q^4}.
\]
As \(\mathbb P(X^3\ne I)=(q-1)^3/q^3\), division proves the uniform law (3). The displayed covariance (4) is an exact subtraction of products of marginals. In characteristic three its numerator factors as \((q-1)^4(3q-2)\), strictly positive; in other characteristics the factor \(1-\mathbb P(W=I)\) is strictly positive because (5) can be nonzero. The asymptotic statement follows by comparing leading polynomial terms in the three probabilities.

**6. Normalization.** Summing (1) over \(q\) central values gives one. Summing (2) over all central values gives \(1/q^6\) for \(p\ne3\), and \((3q^2-3q+1)/q^3\) for \(p=3\), precisely the cube-identity probabilities. No probabilistic independence is assumed at any step.

## Verification

The standalone file `verify_word_joint.py` implements finite-field arithmetic over prime fields and extensions \(\mathbb F_4,\mathbb F_8,\mathbb F_9\). It exhaustively enumerates six first-superdiagonal coordinates and independently compares (1), (2) and conditional uniformity against the exact polynomial values for field orders \(2,3,4,5,7,8,9\). There are \(931748\) such six-coordinate pairs. A separate group-law implementation directly computes matrix products, inverses, two nested commutators and cubes for all \(4096\) ordered group pairs over \(\mathbb F_2\), all \(531441\) pairs over \(\mathbb F_3\), and \(6000\) reproducibly sampled pairs over each of the five larger tested fields. In total \(565537\) pairs are tested by direct group operations. The program's recorded output is in `verification_output.txt`.

These finite checks verify the implementation and boundary cases but are not an infinite proof. The arbitrary prime-power claim is established by the symbolic field-uniform counting in the preceding section.

## Relationship to prior work

Putignano and Vannacci (2026, originally public October 16) compare cube-word and 2-Engel probabilities in **arbitrary finite groups**, proving a universal positive lower comparison. They do not give this group's exact joint word-value law or its characteristic-three conditional uniformity. This comparison motivates studying a concrete class-three test family.

Gritschacher and Villarreal (2021, Lemma 4.2) **already derive the trilinear threefold-commutator form for** \(\operatorname{UT}_4(\mathbb F_p)\) **over prime fields**. The central polynomial in (5), specialized to repeated second and third arguments, is therefore not claimed as new. Their theorem concerns coset-poset homotopy and does not state exact word-value fibers, the cube joint distribution, or the conditional uniformity. In particular this work does not claim to invent the structural commutator formula.

Erfanian and Farrokhi (2013) study the 2-Engel degree and its upper/lower bounds in finite groups, giving examples (including degree \(13/16\) in one group of order \(64\)). Rostamyari, Moghaddam and Khoshtarash (2022) also study the probability of a random ordered pair being 2-Engel; their accessible abstract states bounds, while their complete article was not accessible for comparison. This work does not claim \(13/16\) as a new numeric constant; it derives a complete prime-power word-value and two-word joint law for the specified family. We do not assert whether their order-\(64\) example is isomorphic to \(\operatorname{UT}_4(\mathbb F_2)\) without an identification.

## Limitations

The theorem is a count for one natural class-three matrix-group family, not a universal comparison bound for groups. The proof is elementary once the group law is written out, and the 2021 trilinear expression is a strong precursor; possible unlocated implicit derivations of the joint formula from earlier word-map literature remain a historical-priority risk. No independence of verification, peer review, or formal certification is claimed. No statements are made about \(\operatorname{UT}_n\) for \(n\ne4\), nonuniform sampling, or the full joint distribution of multiple noncentral words.

## References

1. L. Putignano and M. Vannacci, *Comparing word probabilities in finite groups*, arXiv:2610.23100v1 (first posted 2026-10-16), revised v2 (2026-10-19). https://arxiv.org/abs/2610.23100
2. S. Gritschacher and B. Villarreal, *On families of nilpotent subgroups and associated coset posets*, arXiv:2104.06869v2 (2021), especially Lemma 4.2 and Theorem 4.1. https://arxiv.org/abs/2104.06869
3. A. Erfanian and M. Farrokhi D. G., *On the probability of being a 2-Engel group*, *International Journal of Group Theory* 2(4) (2013), 31–38. https://www.researchgate.net/publication/288650599_On_the_probability_of_being_a_2-Engel_group
4. M. A. Rostamyari, M. R. Moghaddam and R. Khoshtarash, *The probability that a pair of group elements is 2-Engel*, *Asian-European Journal of Mathematics* 15(5) (2022), article 2250088, https://doi.org/10.1142/S1793557122500887 (abstract inspected; complete text inaccessible).
