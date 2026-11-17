# Every lattice-polygon prism has a real-rooted Ehrhart numerator

## Finding
Let \(P\subset\mathbb R^2\) be any two-dimensional convex lattice polygon, and let \(m\ge1\) be any integer. The three-dimensional lattice prism \(Q=P\times[0,m]\) has an Ehrhart \(h^*\)-polynomial with **only real, strictly negative roots**, where roots are counted with multiplicity. This holds even if the Ehrhart \(h^*\)-polynomial of \(P\) has nonreal roots. At height \(m=1\), the exceptional family with one interior and three boundary lattice points yields the repeated factor \((1+2t)^2\); no assertion of simplicity is made for other prism parameters.

Writing \(I=\#(\operatorname{int}P\cap\mathbb Z^2)\), \(B=\#(\partial P\cap\mathbb Z^2)\), and \(a=I+B-3\), the exact formula is
\[
h^*_{Q}(t)=1+\big((m+1)a+3m-1\big)t
+\big((2m-1)a+(2m+1)I\big)t^2+(m-1)I t^3.
\]
In particular, taking a **single unit lattice segment** repairs every non-real-rooted planar Ehrhart numerator: \(h^*_P\) may have two nonreal zeros, but \(h^*_{P\times[0,1]}\) never does.

## Assumptions and scope
A lattice polygon is the convex hull of finitely many integer points and has nonempty Euclidean interior. The lattice is standard. \(I\ge0\) and \(B\ge3\) are integers. For a \(d\)-polytope \(X\), its Ehrhart numerator is defined by
\[
\sum_{n\ge0}\#(nX\cap\mathbb Z^d)t^n=\frac{h_X^*(t)}{(1-t)^{d+1}}.
\]
The claim concerns **Cartesian products**, not the convex-hull join, direct/free sum, or a section of a prism. Integral height \(m\ge1\) is essential to the lattice-polytope setting. The constant numerator is real-rooted by convention (the present positive-dimensional prisms actually have nonconstant numerator).

## Proof
**1. Planar numerator and its possible exceptional roots.** Pick's theorem and the two-dimensional Ehrhart formula give
\[
\#(nP\cap\mathbb Z^2)=\big(I+B/2-1\big)n^2+(B/2)n+1,
\qquad h_P^*(t)=1+(I+B-3)t+It^2.
\]
Set \(a=I+B-3\). All coefficients are nonnegative. The quadratic has nonreal roots precisely when \(a^2<4I\). For \(B\ge4\), \(a\ge I+1\) implies \(a^2-4I\ge (I-1)^2\ge0\). For \(B=3\), \(a=I\), and \(I^2-4I<0\) exactly at \(I=1,2,3\). Thus **the only planar nonreal numerator cases are** \((B,I)=(3,1),(3,2),(3,3)\), in which \(h_P^*=1+It+It^2\). This covers also the constant and linear base cases.

**2. Exact prism transform.** Since every lattice point of \(nQ\) consists of a lattice point of \(nP\) and one of the \(mn+1\) integer heights,
\[
\#(nQ\cap\mathbb Z^3)=(mn+1)\#(nP\cap\mathbb Z^2).
\]
Apply \(F(t)\mapsto F(t)+mtF'(t)\) to \(F(t)=h_P^*(t)/(1-t)^3\). Multiplying by \((1-t)^4\) yields
\[
 h_Q^*(t)=\big(1+(3m-1)t\big)h_P^*(t)+mt(1-t)(h_P^*)'(t).
\]
Expansion gives exactly the four displayed coefficients. They are nonnegative because \(I\ge0\), \(a\ge0\), and \(m\ge1\).

**3. Bases already having real roots.** The segment \([0,m]\) has \(h^*(t)=1+(m-1)t\), with only nonpositive real roots (or no roots at \(m=1\)). Wagner's theorem on the real-zero-preserving Ehrhart/Hadamard product, stated for lattice Cartesian products in Liu's Theorem 2.2(i) [3], gives real-rootedness of \(h_{P\times[0,m]}^*\) whenever \(h_P^*\) is real-rooted. Step 1 has exhausted this class, which includes all \(B\ge4\) and all \(B=3\) except \(I=1,2,3\).

**4. The three nonreal bases, checked without a product closure hypothesis.** Write \(k=I\in\{1,2,3\}\) and \(q=m-1\ge0\). Step 2 gives
\[
 h_Q^*(t)=1+\big((k+3)q+2k+2\big)t+4k(q+1)t^2+kqt^3.
\]
For a cubic \(d+ct+bt^2+at^3\), its discriminant is \(b^2c^2-4ac^3-4b^3d-27a^2d^2+18abcd\). Substitution and exact polynomial expansion yield
\[
\begin{aligned}
\Delta_1(q)&=288q^3+549q^2+288q,\\
\Delta_2(q)&=600q^4+2832q^3+4180q^2+2304q+256,\\
\Delta_3(q)&=2592q^4+10800q^3+16317q^2+10560q+2304.
\end{aligned}
\]
For \(q>0\), the polynomial has degree three and all three discriminants are strictly positive; hence all three zeros are distinct and real. When \(q=0\), the cubic coefficient vanishes, so use the quadratic directly: its discriminant is \(4(k-1)^2\ge0\), and for \(k=1\) its numerator equals \((1+2t)^2\). Therefore every exceptional prism numerator has only real zeros as well.

**5. Signs and quantifiers.** For every allowed \(P,m\), the numerator has constant coefficient one and all nonconstant coefficients nonnegative, so it has no real root at \(t\ge0\). Together with the real-rootedness established in Steps 3–4, all its roots are strictly negative. All planar lattice polygons and all positive integral heights are covered. \(\square\)

## Verification
The accompanying standalone `prism_verify.py` reconstructs the three discriminants **as polynomials in \(q\) using integer polynomial arithmetic**, checks their coefficient identities, and independently compares the derived prism numerator with lattice-point counts from Pick's formula. It also tests 117,600 exact coefficient/count pairs across many interior counts, boundary counts, heights, and dilations, along with real-root discriminant inequalities. The infinite theorem follows from the displayed derivation and the cited product-preservation theorem; the finite numerical grid is supplementary only. Run the file with `python3 prism_verify.py` from this directory.

## Relationship to prior work
Nill [1] proves that lattice polytopes of sufficiently large width (in each fixed dimension) have real-rooted Ehrhart numerators, but a Cartesian prism has lattice width at most the width of its polygonal base. The theorem here applies even to bases of width two or three and therefore is not implied by a large-width hypothesis. Ferroni and Higashitani [2] and Liu [3, Theorem 2.2(i)] state Wagner's sufficient criterion that **two already real-rooted factors** have a real-rooted product. This does not cover the three polygonal classes \(h_P^*=1+kt+kt^2\) with \(k\in\{1,2,3\}\), since those inputs are nonreal-rooted. The exact formula and their discriminant calculation fill that gap. A separately published lattice-segment preservation result [5] guarantees ordinary log-concavity given log-concavity of the base, but does not assert real-rootedness or treat the exceptional roots. A different prism-slice real-rootedness conjecture [6] concerns intersections of rectangular prisms with hyperplanes, rather than products with arbitrary lattice polygons.

## Limitations
The result is three-dimensional and requires an honest Cartesian product of a two-dimensional lattice polygon with a positive integral segment. It neither proves real-rootedness for arbitrary three-dimensional lattice polytopes nor generalizes to arbitrary higher-dimensional bases. The proof cites Wagner's established root-preservation theorem for already-real-rooted factors and verifies the only exceptional planar factors directly. The derivation does not establish simplicity for every possible prism numerator. Searches do not establish absolute historical priority; equivalent results under alternative Ehrhart-series terminology are possible.

## References
1. B. Nill, “Lattice polytopes of large width have real-rooted Ehrhart \(h^*\)-polynomials,” arXiv:2608.03635 (first public version 2026-08-04), https://arxiv.org/abs/2608.03635.
2. L. Ferroni and A. Higashitani, “Examples and counterexamples in Ehrhart theory,” arXiv:2307.10852 (first public 2023-07-20), https://arxiv.org/abs/2307.10852; EMS Surveys in Mathematical Sciences (2024).
3. F. Liu, “Ehrhart Properties under Operations on Lattice Polytopes,” arXiv:2610.06338 (first public 2026-10-05), Theorem 2.2(i), https://arxiv.org/abs/2610.06338.
4. D. G. Wagner, “Total positivity of Hadamard products,” Journal of Mathematical Analysis and Applications 163 (1992), 459–483, Theorem 0.2.
5. “Lattice-segment factors preserve Ehrhart \(h^*\)-log-concavity,” https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-lattice-segment-factors-preserve-ehrhart-h-log-concavity--5724d44ac8d4.
6. L. Ferroni and D. McGinnis, “Lattice points in slices of prisms,” arXiv:2202.11808, https://arxiv.org/abs/2202.11808.
