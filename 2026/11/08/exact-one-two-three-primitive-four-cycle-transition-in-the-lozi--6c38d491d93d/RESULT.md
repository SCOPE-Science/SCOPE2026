# Exact one–two–three primitive four-cycle transition in the Lozi two-saddle wedge

## Finding
Consider the classical Lozi map
\[
L_{a,b}(x,y)=\bigl(1-a|x|+y,\,bx\bigr),
\qquad a>1+b,\quad 0\le b<1.
\]
A primitive four-cycle is a set of four distinct real points cyclically permuted by the map. Write \(N_4(a,b)\) for its number of primitive four-cycles in the *entire real plane* (not just an attractor). Define
\[
R(a,b)=a^3-a^2b-a^2+ab^2-a+b^3+b^2-b-1.
\]
Then the complete census is
\[
N_4(a,b)=\begin{cases}1&R(a,b)<0,\\2&R(a,b)=0,\\3&R(a,b)>0.\end{cases}
\]
At equality one of the two cycles meets the switching line \(x=0\); every other four-cycle has strictly nonzero first coordinate at every point. The one-cycle region contains only itinerary \(+++ -\), with spaces ignored; above the transition the two additional itineraries are \(++--\) and \(+---\). Here a plus or minus denotes the sign of the first coordinate. There is a unique transition \(a=\alpha(b)>1+b\) at each \(0\le b<1\). Every strict four-cycle is hyperbolic, with one multiplier of modulus greater than one and one of modulus less than one; at \(b=0\), the latter multiplier is zero.

## Assumptions and scope
Parameters are real, \(0\le b<1\), \(a>1+b\). Every point of the real plane is included in the orbit count. An orbit passing through \(x=0\) is counted according to the continuous value of the Lozi map, independently of sign-label ambiguity at the switching line. The degenerate end \(b=0\) is allowed. No statement about global attracting basins or periods above four is made.

## Proof
Set \(x_n\) to be the first coordinate of the \(n\)-th iterate. Then \(x_{n+1}=1-a|x_n|+b x_{n-1}\). A period-four point determines one of sixteen length-four sign words; a primitive four-cycle cannot have a nonprimitive sign word. Indeed, a constant-sign branch matrix has no fourth root of unity as an eigenvalue for \(a>1+b\) and \(0\le b<1\). The two-step return for the alternating word has trace \(-a^2+2b\), determinant \(b^2\), and its characteristic polynomial at \(-1\) is \((1+b)^2-a^2<0\), so its square cannot acquire a new fixed point. This applies also when an orbit meets the switching line because either sign labels the same affine branch value there. The three primitive necklaces of binary length four are \(+++-\), \(++--\), and \(+---\). They are the only possible primitive-four itineraries, up to cyclic rotation; at switching points zero can be assigned either sign.

For a word \(s_0s_1s_2s_3\), solve the four affine equations
\[
x_{i+1}=1-a s_i x_i+b x_{i-1},\quad i\pmod4,
\]
where \(s_i=1\) for plus, \(s_i=-1\) for minus. Put
\[
D=a^4+(b^2-1)^2,\qquad C=(a^2-b^2+1)(a^2+b^2-1).
\]
Both are strictly positive under the assumptions; thus the four-step return equations have unique formal solutions for each primitive necklace. Introduce the numerators
\[
\begin{aligned}
P&=a^3-a^2b-a^2-ab^2+a-b^3-b^2+b+1,\\
Q&=a^3+a^2b+a^2+ab^2-a-b^3-b^2+b+1,\\
U&=a^3+a^2b+a^2-ab^2+a+b^3+b^2-b-1.
\end{aligned}
\]
The first-coordinate lists of the unique formal solutions are
\[
\begin{array}{c|c}
+++-&(P,\;(a-b-1)(a+b-1)(a+b+1),\;Q,\;-(a+b-1)(a^2+b^2+2b+1))/D\\
++--&(R,\;U,\;-Q,\;-P)/C\\
+---&((a-b+1)(a^2+b^2+2b+1),\;-U,\;-(a-b-1)(a-b+1)(a+b+1),\;-R)/D.
\end{array}
\]
These lists have to satisfy their sign words for the corresponding orbit to exist. Let \(t=a-b-1>0\). Direct expansion gives
\[
\begin{aligned}
P&=t^3+2(b+1)t^2+2(b+1)t+2(1-b)(b+1)^2>0,\\
Q&=t^3+4(b+1)t^2+(6b^2+10b+4)t+2(b+1)^3>0,\\
U&=t^3+4(b+1)t^2+(6b^2+10b+6)t+2(b+1)^3>0.
\end{aligned}
\]
Consequently \(+++-\) is always strict and admissible. The other two words are both strictly admissible exactly when \(R>0\) and inadmissible when \(R<0\).

At \(R=0\), the \(++--\) formal orbit has its first position on \(x=0\), while the \(+---\) orbit has its fourth position on \(x=0\). Their positive and negative positions match after one cyclic rotation. For instance, the equality of their relevant first-coordinate expressions follows from the exact identity
\[
U D-(a-b+1)(a^2+b^2+2b+1)C=2a(a^2b+b^2-1)R.
\]
Hence the two formal solutions are the same physical primitive four-cycle at this collision. No other sign word can contribute a primitive four-cycle, by the exhaustive binary-necklace enumeration and uniqueness of the formal solutions. The three resulting counts follow, including the border point.

The transition is unique because
\[
R(1+b+t,b)=t^3+2(b+1)t^2+2b(b+1)t+2(b-1)(b+1)^2.
\]
For each \(0\le b<1\) this is strictly increasing for \(t>0\), negative at \(t=0\), and tends to positive infinity.

Finally, on a strict orbit the branch derivatives are \(J_+=\begin{pmatrix}-a&1\\b&0\end{pmatrix}\), \(J_-=\begin{pmatrix}a&1\\b&0\end{pmatrix}\). For each primitive-four word the fourth-return determinant is \(b^4\), and the traces are \(-a^4+2b^2\), \(a^4+2b^2\), and \(-a^4+2b^2\), respectively. Since
\[
a^4-2b^2>1+b^4,
\]
the characteristic roots have one modulus greater than one and another smaller than one. This includes \(b=0\), with one zero multiplier. No smooth return derivative is assigned to the cycle meeting \(x=0\).

## Verification
The companion standalone Python checker reproduces the three formal orbit formulas by symbolic linear algebra, verifies the root polynomial and collision identity exactly, and independently enumerates all sixteen sign words over twenty rational parameter pairs using exact arithmetic. It returns the correct one-versus-three classification in every test. The equality case is established algebraically in the proof by the exact collision identity, not inferred from floating-point computations. Finite tests do not establish the universal census, which follows from the full necklace and sign analysis above.

## Relationship to prior work
The two-dimensional Lozi family and its border-collision phenomena are classical. Sushko, Avrutin and Gardini study analytical boundaries of large *stable* periodicity regions with prescribed rotation numbers; those regions do not provide the complete count of primitive four-cycles throughout the two-saddle region here. Ou establishes general symbolic uniqueness and rational parameter dependence for Lozi formal periodic points; the present proof uses the same standard affine-itinerary mechanism, but additionally establishes the exact global \(1\)-to-\(2\)-to-\(3\) census in the specified parameter wedge and explicitly counts the switching collision. Prior work on the border-collision normal form establishes a general upper bound of three isolated strict four-cycles, which does not imply this exact Lozi parameter-phase diagram. The originating papers' ideas are acknowledged, not claimed as new.

## Limitations
The result is confined to \(a>1+b\) and \(0\le b<1\). It counts cycles in the entire plane; the three regular cycles are not attractors. The borderline \(R=0\) cycle is nondifferentiable and has no ordinary fourth-return Jacobian. A detailed independent literature audit has not been performed. In particular, the fully published text of Sushko, Avrutin and Gardini could not be inspected beyond its available bibliographic and abstract material, leaving residual publication-priority risk in alternative symbolic formulations.

## References
Sushko, Avrutin and Gardini, *Lozi map embedded into the 2D border collision normal form*, Journal of Difference Equations and Applications (first published online 26 April 2023), https://doi.org/10.1080/10236198.2023.2205960 .

Ou, *Critical points in higher dimensions, I: Reverse order of periodic orbit creations in the Lozi family*, arXiv:2203.02326 (4 March 2022), https://arxiv.org/abs/2203.02326 .

Lozi, *Survey of Recent Applications of the Chaotic Lozi Map*, Algorithms 16 (2023), 491, https://www.mdpi.com/1999-4893/16/10/491 .
