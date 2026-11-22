# Exact optimal 2-limited packing partitions of cyclic prisms

## Finding
For each integer \(n\geq3\), let \(Y_n=C_n\square K_2\) have vertex set \(\{(i,r):i\in\mathbb Z/n\mathbb Z,\ r\in\{0,1\}\}\) with horizontal cycle edges and vertical rung edges. A \(2\)-limited packing partition is a partition into color classes such that each closed vertex neighborhood contains at most two vertices of each color. Let \(\chi_{\times2}\) be the minimum number of classes.

The exact optimal palette size is
\[
\chi_{\times2}(Y_n)=\begin{cases}2,&n\text{ even},\\3,&n\text{ odd}.\end{cases}
\]
For even \(n\), the number of optimal partitions **without named colors** is \(3\) when \(4\mid n\) and \(1\) when \(n\equiv2\pmod4\). All two-color optimizers are described explicitly in the proof below.

For odd \(n\), let \(b_n\) denote the number of optimum partitions without named colors. Define
\[
\begin{aligned}
D(z)={}&(1-z)^6(1+z)^2(1+z^2)(1+2z-z^2)\\
&\cdot(1+z+z^3)^2(1-4z^2+5z^4+z^6)^2\\
&\cdot(1-6z+7z^2-6z^3+2z^4)\\
&\cdot(1+3z+4z^2+3z^3+2z^4)^2.
\end{aligned}
\]
Then for every odd integer \(n\geq3\),
\[
\boxed{b_n=\frac16[z^n]\left(-z\frac{D'(z)}{D(z)}\right).}
\]
In particular, \(b_3=15\), \(b_5=405\), \(b_7=9429\), and \(b_9=216579\). The corresponding numbers of named three-colorings are \(90,2430,56574,1299474\). This is an exact rational generating-function prescription at every odd circumference, not a finite-size extrapolation.

## Assumptions and scope
Graphs are finite, simple, and labelled by their canonical column and layer coordinates; \(n\ge3\) ensures that the two cycle neighbors of each vertex are distinct. A color class \(S\) is \(2\)-limited precisely when \(|S\cap N[v]|\le2\) for every vertex \(v\). Colors in a named palette are distinguishable; a partition into \(k\) nonempty classes has exactly \(k!\) names. In counting optimum partitions, automorphism-equivalent vertex subsets are **not** identified; only color names are forgotten.

## Proof
**Two colors and the parity obstruction.** For a named two-color assignment, write \(s_{i,r}\in\{+1,-1\}\) according to the color. Since every closed neighborhood has four vertices, the condition that neither class appear more than twice is equivalent to exactly two vertices of each color in every closed neighborhood. Hence
\[
s_{i-1,r}+s_{i+1,r}+s_{i,r}+s_{i,1-r}=0.
\]
Set \(t_i=s_{i,0}+s_{i,1}\) and \(d_i=s_{i,0}-s_{i,1}\). Adding and subtracting the two row equations yields
\[
t_{i-1}+2t_i+t_{i+1}=0,\qquad d_{i-1}+d_{i+1}=0.
\]
The first recurrence has solutions \(t_i=(-1)^i(a+bi)\); cyclicity forces \(b=0\) and forces \(a=0\) when \(n\) is odd. The second has \(d_{i+2}=-d_i\) and has a nonzero cyclic solution only when \(4\mid n\). For odd \(n\), both sequences vanish, impossible for a pair of signs. For even \(n\), if \(t\ne0\), all columns have the same color on both layers, with alternating colors across consecutive columns: exactly two named assignments. Otherwise \(t=0\), the two layers have opposite colors, and the \(d\)-recurrence permits precisely four assignments when \(4\mid n\), none otherwise. Mixed modes do not exist because a nonzero cyclic \(t\) has magnitude \(2\) in every column, forcing \(d=0\). Thus the named optimum counts are \(2\) or \(6\), and the unnamed optimum counts are \(1\) or \(3\). For odd \(n\), a proper three-coloring of the base cycle, used identically on both layers, is a valid three-color partition: the rung gives two occurrences of the current color and each horizontal neighbor gives at most two occurrences of another color. The lower and upper bounds establish the stated optimum sizes.

**All optimal three-colorings for odd \(n\).** A column is an ordered pair \(u=(u_0,u_1)\in\{0,1,2\}^2\), giving nine possible columns. Define an explicit \(81\)-by-\(81\) matrix \(M\), whose rows and columns are indexed by ordered pairs of columns. Put
\[
M_{(u,v),(v',w)}=\begin{cases}
1,&v=v'\text{ and every color occurs at most twice in }\{u_r,v_r,v_{1-r},w_r\}\text{ for }r=0,1,\\
0,&\text{otherwise}.
\end{cases}
\]
These four values form the closed neighborhood of vertex \((i,r)\) when three consecutive columns are \(u,v,w\). Consequently a closed walk of length \(n\) in this de Bruijn transfer corresponds bijectively to a named, closed-neighborhood-capacity-two coloring of the labelled cyclic prism, giving the exact count \(a_n=\operatorname{tr}(M^n)\) for all \(n\ge3\).

The following **finite integer matrix identity** is established by the exact certificate in `VERIFY.py` (which constructs all \(81\) states and \(342\) permitted transitions, computes traces of powers one through \(81\), and applies Newton's identities to reconstruct the complete characteristic polynomial):
\[
\begin{aligned}
\det(xI-M)={}&x^{39}(x-1)^6(x+1)^2(x^2+1)(x^2+2x-1)\\
&\cdot(x^3+x^2+1)^2(x^6+5x^4-4x^2+1)^2\\
&\cdot(x^4-6x^3+7x^2-6x+2)\\
&\cdot(x^4+3x^3+4x^2+3x+2)^2.
\end{aligned}
\]
By polynomial reciprocity, \(\det(I-zM)=D(z)\) as displayed above. The standard formal identity \(-z\frac{d}{dz}\log\det(I-zM)=\sum_{n\ge1}\operatorname{tr}(M^n)z^n\) follows by expanding \(\log(1-z\lambda)\) for each eigenvalue \(\lambda\), with algebraic multiplicity. Thus \([z^n](-zD'/D)=a_n\). At odd \(n\), no two-color assignment exists, so every valid named three-coloring uses all three colors, and exactly six such assignments represent each partition. Division by six gives the announced formula for \(b_n\). The first coefficients follow by exact integer expansion, not numerical approximation.

## Verification
`VERIFY.py` is a self-contained Python 3 exact-arithmetic certificate. It reconstructs the matrix directly from the local four-vertex condition, obtains all \(81\) traces and characteristic coefficients via Newton's identities, and compares them with the fully multiplied claimed factorization. It also independently enumerates named colorings at \(n=3,4,5\) and two-color assignments through \(n=10\). `BRUTE.cpp` independently enumerates all direct graph colorings with three colors through \(n=7\) and two colors through \(n=10\), without relying on transfer matrices. Successful output is `PRISM_2LP_CERTIFICATE_OK` and `PRISM_2LP_BRUTE_OK`. The exact scripts, not merely these output strings, are the reproducible finite proof evidence.

## Relationship to prior work
Ahmadi, Soltankhah and Samadi introduced and studied the \(2\)-limited packing partition number and proved an exact result for trees together with general bounds; their 2023 manuscript does not give the prism optimum spectrum or the counting function. Earlier work of Lisitsyna (2013) and Lisitsyna–Avgustinovich (2016) studies **perfect colorings** of prisms, which additionally require each fixed color to see identical neighbor-color multisets. This does not cover the current family: in \(Y_3\), the three columns \((0,0),(1,2),(1,2)\) form a valid three-color \(2\)-limited packing partition, but the two vertices of color \(0\) have distinct neighbor-color multisets \(\{0,1,1\}\) and \(\{0,2,2\}\). Thus a classification confined to perfect colorings cannot imply the present complete optimizer counts. Nearby coloring and packing-prism results use different local conditions and objectives, as described in `AUDIT.json`.

## Limitations
The exact 81-state certificate is finite symbolic computation, not a hand-derived simplification of the characteristic polynomial. The theorem counts all optimal partitions but does not give a closed geometric classification of the exponentially many three-color optimizers for odd \(n\). It concerns exactly two layer rows and capacity two, not other cylinders or general \(k\)-limited packings. Priority comparisons include accessible full text of the main 2023 source and the 2013 perfect-coloring paper; the 2016 follow-up was accessible by its abstract and bibliographic record, but its full text was not retrieved. Unindexed prior calculations may exist. Independent mathematical review has not been performed.

## References
1. A. S. Ahmadi, N. Soltankhah, B. Samadi, *Limited packings: related vertex partitions and duality issues*, arXiv:2308.16837, initially posted 2023-08-31. https://arxiv.org/abs/2308.16837
2. M. A. Lisitsyna, *Perfect 3-colorings of prism and Möbius ladder graphs*, Diskretnyi Analiz i Issledovanie Operatsii **20** (2013), 28–36. https://www.mathnet.ru/links/b2975877364d31df7cfe8e93ccc05e68/da716.pdf
3. M. A. Lisitsyna and S. V. Avgustinovich, *Perfect colorings of the prism graph*, Siberian Electronic Mathematical Reports **13** (2016), 1116–1128. https://doi.org/10.17377/semi.2016.13.088
