# The full endomorphism monoid of a finite rectangular-band power semigroup

## Finding

**Theorem.** Let \(I,J\) be nonempty finite sets with \(|I|=m\) and \(|J|=n\). Form the rectangular band \(B=I\times J\), with \((i,j)(k,\ell)=(i,\ell)\), and let \(S=\mathcal P^*(B)\), the semigroup of all nonempty subsets of \(B\) under setwise multiplication. Write \(\mathcal R=\mathcal P^*(I)\) and \(\mathcal C=\mathcal P^*(J)\). For nonempty \(X\subseteq B\), let \(r(X)\) and \(c(X)\) be its sets of first and second coordinates. Define \(e_{R,C}=R\times C\) and \(F_{R,C}=\{X\in S:r(X)=R,\ c(X)=C\}\).

Every semigroup endomorphism \(f:S\to S\) is specified *uniquely* by a pair of **arbitrary set maps**
\[
\sigma:\mathcal R\longrightarrow\mathcal R,\qquad
\tau:\mathcal C\longrightarrow\mathcal C,
\]
and independent maps
\[
\theta_{R,C}:F_{R,C}\longrightarrow F_{\sigma(R),\tau(C)}
\quad (R\in\mathcal R,\ C\in\mathcal C),
\]
subject only to \(\theta_{R,C}(e_{R,C})=e_{\sigma(R),\tau(C)}\). Every such choice gives an endomorphism. In particular neither support map need be injective or preserve the cardinality of supports, and the fiber maps need not be injective or surjective.

Set
\[
T(r,c)=\sum_{a=0}^{r}\sum_{b=0}^{c}(-1)^{a+b}
\binom{r}{a}\binom{c}{b}2^{(r-a)(c-b)}.
\]
Then \(|F_{R,C}|=T(|R|,|C|)\) and the exact order of the full endomorphism monoid is
\[
\boxed{\displaystyle
|\operatorname{End}(S)|=
\sum_{\sigma:\mathcal R\to\mathcal R}
\sum_{\tau:\mathcal C\to\mathcal C}
\prod_{R\in\mathcal R}\prod_{C\in\mathcal C}
T(|\sigma(R)|,|\tau(C)|)^{T(|R|,|C|)-1}.}
\]
The formula holds for all \(m,n\ge1\). In particular, if \(m=1\) then \(S\) is a right-zero semigroup on \(2^n-1\) elements and \(|\operatorname{End}(S)|=(2^n-1)^{2^n-1}\); the dual formula holds if \(n=1\). For \(m=n=2\),
\[
\boxed{|\operatorname{End}(S)|=648+81\cdot7^6=9\,530\,217.}
\]
The composition law is the ordinary composition of the two support maps, together with \((\theta'\circ\theta)_{R,C}=\theta'_{\sigma(R),\tau(C)}\circ\theta_{R,C}\). Consequently, the idempotent endomorphisms are exactly the data satisfying \(\sigma^2=\sigma\), \(\tau^2=\tau\) and \(\theta_{\sigma(R),\tau(C)}\circ\theta_{R,C}=\theta_{R,C}\) for every \(R,C\).

## Assumptions and scope

The sets \(I,J\) are finite and nonempty. There is no empty subset in \(S\); this matters because adjoining the empty set changes the endomorphism monoid. There is no assumed zero, identity, cancellation, cardinality preservation, injectivity, or surjectivity of an endomorphism. The idempotent characterization concerns idempotency as a function under composition, not idempotence of its values.

## Proof

**1. Multiplication and squares.** For nonempty subsets \(X,Y\subseteq B\), every pair of a row occurring in \(X\) and a column occurring in \(Y\) is realized by multiplying a corresponding element of \(X\) with an element of \(Y\). Therefore
\[
XY=e_{r(X),c(Y)},\qquad X^2=e_{r(X),c(X)}.
\]
It follows that the idempotents in \(S\) are precisely the nonempty rectangles \(e_{R,C}\), and those rectangles form a rectangular band under \(e_{R,C}e_{U,V}=e_{R,V}\).

**2. The action on rectangles.** Every endomorphism preserves idempotents, so \(f(e_{R,C})\) is a rectangle. Write \(f(e_{R,C})=e_{a(R,C),b(R,C)}\). For arbitrary \(R,U\in\mathcal R\) and \(C,V\in\mathcal C\), preservation of \(e_{R,C}e_{U,V}=e_{R,V}\) gives
\[
a(R,V)=a(R,C),\qquad b(R,V)=b(U,V).
\]
Thus \(a(R,C)\) depends only on \(R\), and \(b(R,C)\) only on \(C\). They are unique functions \(\sigma:\mathcal R\to\mathcal R\) and \(\tau:\mathcal C\to\mathcal C\), with no injectivity restrictions.

**3. The action on each fiber.** For \(X\in F_{R,C}\), the square identity gives
\[
f(X)^2=f(X^2)=f(e_{R,C})=e_{\sigma(R),\tau(C)}.
\]
The square of any nonempty subset is exactly the rectangle of its row and column supports. Hence \(f(X)\in F_{\sigma(R),\tau(C)}\), and the image of the source rectangle is forced to be its corresponding target rectangle. This proves necessity and uniqueness of all fiber data.

**4. Converse.** Conversely, choose arbitrary support maps and fiber maps with the stated sole compatibility condition. For any \(X,Y\in S\),
\[
f(XY)=f(e_{r(X),c(Y)})=e_{\sigma(r(X)),\tau(c(Y))}
=f(X)f(Y).
\]
This proves sufficiency for every possible map, including all singular ones. Composition yields exactly the formula in the finding. Squaring that composition law yields the claimed characterization of idempotent endomorphisms.

**5. Counting.** A subset in \(F_{R,C}\) is an \(|R|\)-by-\(|C|\) zero-one matrix with no all-zero row or column. Inclusion-exclusion over rows and columns gives \(T(r,c)\). For fixed support functions \(\sigma,\tau\), the source rectangle in each fiber has a forced image, whereas each of its \(T(|R|,|C|)-1\) other elements has exactly \(T(|\sigma(R)|,|\tau(C)|)\) independently chosen images. Multiplication of these independent choices and summation over all pairs of support maps yields the asserted formula.

**6. Boundary cases and a small exact count.** If \(m=1\), each nonempty subset is already a rectangle and multiplication is right projection; therefore every function on \(2^n-1\) elements is a homomorphism. The case \(n=1\) is dual. For \(m=n=2\), there are three nonempty row supports and three nonempty column supports. All nine rectangles have singleton fibers except the full-support pair, which has \(T(2,2)=7\) elements (one rectangle and six nonrectangular subsets). There are \(3^3\cdot3^3=729\) support-map pairs. Exactly \(3^2\cdot3^2=81\) send both full supports to full supports, allowing \(7^6\) choices for the six nonrectangles; the other \(648\) pairs allow only one choice. Hence the count is \(648+81\cdot7^6=9\,530\,217\).

## Verification

The standalone file `CHECK.py` computes all subsets and all pair products for \((m,n)=(1,1),(1,3),(2,2),(2,3),(3,2)\), independently enumerates every support fiber and checks its inclusion-exclusion size, constructs deterministic pseudorandom endomorphisms using arbitrary support/fiber maps and exhaustively tests every multiplication identity, and enumerates all \(729\) support-map pairs in the \(2\)-by-\(2\) example. Run `python3 CHECK.py`; the accompanying `CHECK_OUTPUT.txt` records its output ending in `VERIFY_OK`. This finite verification is not an exhaustive test for arbitrary \(m,n\); the universal conclusion rests on the symbolic proof above.

## Relationship to prior work

The 2026 work *On the automorphisms of the power semigroups of a numerical semigroup* (arXiv:2604.26901) studies invertible maps in the cancellative numerical-semigroup setting. *Kobayashi's problem for power semigroups of inverse semigroups* (arXiv:2610.29525) treats isomorphism reconstruction for inverse semigroups; a rectangular band with two nontrivial factors is not inverse. Kudryavtseva's *The structure of automorphism groups of semigroup inflations* (arXiv:math/0511669) studies automorphism groups of inflations, not arbitrary endomorphisms. Earlier work on the same rectangular-band power semigroups characterizes their **automorphisms**, in which the support actions and fibers must be bijective; its results are not claimed here. The present theorem characterizes the entire endomorphism monoid, including collapsing support maps, arbitrary singular fiber maps, exact total counts and all endomorphism retractions. The open problems in *Lyapin's notebook* (arXiv:2604.04763) motivate systematic study of powers of semigroups; no general reconstruction problem is claimed solved here.

## Limitations

The theorem is restricted to the **nonempty-subset** power semigroup of a **finite rectangular band**. It does not classify endomorphisms of the full powerset with the empty set, arbitrary finite bands, arbitrary semigroups, or inverse semigroups. The enumeration formula is finite but involves sums over all functions on nonempty support sets; no closed asymptotic is established. Exhaustive endomorphism enumeration for general dimensions was not attempted. Bibliographic coverage is necessarily limited to the inspected primary sources and available research records; priority beyond those comparisons is not certified.

## References

- *On the automorphisms of the power semigroups of a numerical semigroup*, arXiv:2604.26901 (2026), https://arxiv.org/abs/2604.26901.
- *Kobayashi's problem for power semigroups of inverse semigroups*, arXiv:2610.29525 (2026), https://arxiv.org/abs/2610.29525.
- G. Kudryavtseva, *The structure of automorphism groups of semigroup inflations*, arXiv:math/0511669 (2005), https://arxiv.org/abs/math/0511669.
- *Lyapin's notebook*, arXiv:2604.04763 (2026), https://arxiv.org/abs/2604.04763.
