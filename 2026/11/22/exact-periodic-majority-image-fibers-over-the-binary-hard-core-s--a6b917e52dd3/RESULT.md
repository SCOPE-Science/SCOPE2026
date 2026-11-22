# Exact periodic majority-image fibers over the binary hard-core shift

## Finding

Let \(n\ge1\) and let \(\mathcal X_n\) be the set of indexed binary cyclic words \(x=(x_i)_{i\in\mathbb Z/n\mathbb Z}\) satisfying \(x_ix_{i+1}=0\) at every cyclic index. Apply one simultaneous three-neighbor majority update
\[
\Phi_n(x)_i=\mathbf1\{x_{i-1}+x_i+x_{i+1}\ge2\},
\]
with repeated residues used literally when \(n=1,2\). For a received word \(y\), write \(p_n(y)=|\{x\in\mathcal X_n:\Phi_n(x)=y\}|\).

**Exact fiber law.** If \(y\ne0^n\), list its cyclic successive-one gaps, each a positive integer, as \(g_1,\ldots,g_k\) with sum \(n\) (a lone one has gap \(n\)). Define \(c_0=1\), \(c_1=c_2=0\), and
\[
c_t=\sum_{j=3}^t c_{t-j}\quad(t\ge3),\qquad
\sum_{t\ge0}c_tz^t=\frac{1-z}{1-z-z^3}.
\]
Then for every nonzero word and every positive ring length,
\[
\boxed{p_n(y)=\prod_{j=1}^k c_{g_j-2}},
\]
where a factor with a negative subscript is defined to be zero. In particular, the attainable nonzero outputs have *every* cyclic one-gap in \(\{2\}\cup\{5,6,7,\ldots\}\). Moreover, nonzero output words have a **unique** allowed predecessor exactly when all their gaps lie in \(\{2,5,6,7\}\).

The all-zero word always occurs; its inverse fiber is \(b_n\), where \(b_1=b_2=1\), \(b_3=4\) and \(b_n=b_{n-1}+b_{n-3}\) for \(n\ge4\). It has one predecessor precisely at \(n=1,2\).

**Exact image and unique-decoding counts.** Set
\[
A(z)=z^2+\frac{z^5}{1-z},\qquad B(z)=z^2+z^5+z^6+z^7.
\]
If \(I_n\) is the number of distinct outputs and \(U_n\) is the number of those outputs with exactly one predecessor in \(\mathcal X_n\), then
\[
\boxed{\sum_{n\ge1}I_nz^n=\frac{z}{1-z}+\frac{zA'(z)}{1-A(z)}},\qquad
\boxed{\sum_{n\ge1}U_nz^n=z+z^2+\frac{zB'(z)}{1-B(z)}}.
\]
For \(n=1,\ldots,10\), the image counts are \(1,3,1,3,6,9,15,19,28,38\); the unique-decoding counts are \(1,3,0,2,5,8,14,10,18,17\). These are *indexed cyclic* output counts, not necklace counts.

Let \(r,s\in(0,1)\) be the unique positive solutions of \(A(r)=B(s)=1\) respectively (that is, each equation applies to its named function). Then \(r\approx0.692871630044598\), \(s\approx0.729610770140541\), and
\[
I_n\sim r^{-n},\qquad U_n\sim s^{-n},\qquad
\frac{U_n}{I_n}\sim(r/s)^n\approx(0.9496455623)^n.
\]
Thus the proportion of distinct outputs that are uniquely invertible tends exponentially to zero, although unique output words themselves grow exponentially.

## Assumptions and scope

All words are ordered/indexed with periodic boundary conditions. The source constraint is cyclic avoidance of adjacent ones, including the wraparound pair. The majority map is a single synchronous update, not an asynchronous or iterative process. The predecessor count refers only to the restricted source \(\mathcal X_n\); unrestricted-predecessor counts can differ. For rings of size one and two, repeated neighborhood indices are evaluated with their multiplicities, not collapsed to sets. Generating functions are formal at the origin. The value of \(c_t\) for \(t<0\) is zero by convention.

## Proof

**1. Majority equals a gap detector under the hard-core constraint.** In any \(x\in\mathcal X_n\), no two adjacent sites are one. If a neighborhood has a majority of ones, the only possibility is \((x_{i-1},x_i,x_{i+1})=(1,0,1)\). The converse holds. This remains valid for \(n=1,2\) with the original repeated cyclic indices. Hence the received ones are exactly the midpoints of cyclic successive input ones separated by distance two. All cyclic successive input-one gaps are at least two.

**2. Local-to-global inverse fiber bijection.** Let \(y\ne0^n\) have consecutive output ones at positions \(i,j\), with forward cyclic gap \(g\). Every source predecessor must have ones at \(i-1,i+1,j-1,j+1\), counting coincidences only for equal residue positions. When \(g=1\), this forces adjacent ones; when \(g=3\), the forced sites \(i+1,i+2\) are adjacent; and when \(g=4\), the forced sites \(i+1,i+3\) necessarily create an additional output one at \(i+2\). Thus gaps one, three and four cannot occur. Gap two is feasible and determines its source segment uniquely: its central forced-one site is shared. For \(g\ge5\), the forced input ones inside the gap lie at offsets one and \(g-1\) from \(i\), separated by \(g-2\). Any intervening source ones must split that separation into gaps at least three: a gap of one violates hard-core admissibility and a gap of two generates an output one not present between \(i\) and \(j\). Conversely, any ordered decomposition of \(g-2\) into parts at least three gives a valid source segment, with no extra received one in this output gap. Segments from different output gaps meet only at the forced source ones straddling received ones; these are compatible, and the two forced ones on either side of each received one always have the required input gap two. Therefore the segments can be selected independently and glued uniquely around the indexed circle, including when there is just one output one. This gives the product formula and the exact allowed gap set.

**3. Composition recurrence and uniqueness.** The number of ordered decompositions of an integer \(t\) into parts at least three (including the empty decomposition when \(t=0\)) is \(c_t\). Its generating series is
\[
\frac{1}{1-\sum_{j\ge3}z^j}=\frac{1-z}{1-z-z^3}.
\]
Thus \(c_0=1\), \(c_1=c_2=0\), \(c_3=c_4=c_5=1\), and \(c_t\ge2\) for every \(t\ge6\) (use both \((t)\) and \((3,t-3)\) for \(t\ge6\)). The nonzero output has one predecessor precisely when every gap \(g\) has \(c_{g-2}=1\), which means \(g\in\{2,5,6,7\}\).

**4. Zero-output fiber.** The output is all zero precisely when no pair of successive source ones is two positions apart. Thus source-one gaps, when there are ones, are all at least three. Equivalently, the source avoids the cyclic patterns `11` and `101`. Encode the distance since the last source one by three states (zero, one, at least two); appending zero moves them respectively to (one, at least two, at least two), while appending one is allowed only from the third state and moves to zero. The transition matrix is
\[
T=\begin{pmatrix}0&1&0\\0&0&1\\1&0&1\end{pmatrix}.
\]
Every indexed periodic source gives exactly one closed labeled walk and vice versa, including the all-zero source. Therefore \(b_n=\mathrm{tr}(T^n)\). Since \(\det(tI-T)=t^3-t^2-1\), Cayley–Hamilton gives \(b_n=b_{n-1}+b_{n-3}\) with initial values \(1,1,4\). For \(n\ge3\), there is the all-zero input and at least one single-one input, so \(b_n>1\).

**5. Cycle-composition counting.** A cyclic indexed binary output with \(k\ge1\) ones and ordered successive-one gap sizes in an allowed set with gap polynomial \(G(z)\) is counted exactly by
\[
\frac nk[z^n]G(z)^k.
\]
Indeed there are \(n\) choices of a designated starting one, and each output has exactly \(k\) choices of designation. Summing over \(k\ge1\) yields \(n[z^n]\sum_{k\ge1}G(z)^k/k=[z^n]zG'(z)/(1-G(z))\). For all attainable nonzero outputs, take \(G=A\); for uniquely invertible nonzero outputs, take \(G=B\). Add the all-zero output to the first series and add it at \(n=1,2\) only to the second. This proves both rational identities at every length.

**6. Asymptotics.** Both \(A\) and \(B\) have nonnegative coefficients and allowed gap lengths with greatest common divisor one. Their unique positive radii \(r,s\) satisfying \(G=1\) are strictly within the first other singularities (\(r<1\); \(B\) is a polynomial). If \(|z|=r\) and \(A(z)=1\), the triangle inequality forces all terms of positive coefficient to have the same phase, hence \(z=r\); similarly \(z=s\) for \(B\). Both roots are simple because \(G'(r),G'(s)>0\). Near either root, \(zG'(z)/(1-G(z))\) has principal part \(1/(1-z/r)\) (using the corresponding root), so its coefficient is the reciprocal-root exponential with leading constant one and an exponentially smaller remainder. The extra all-zero terms do not affect the leading rates. The displayed numerical values are roots of the exact rational equations, not experimental extrapolations.

## Verification

The standalone Python standard-library file `verify.py` independently enumerates every cyclic hard-core input and every possible output at lengths one through fifteen. It checks the full inverse-fiber formula for every output, the zero-output recurrence, the rational-series counts by independent gap-composition dynamic programming, and small composition values. It has been run from the delivered artifact contents. The exhaustive tests cover finite lengths only; the all-length theorem is proved by the constructive gap bijection and cycle-marking identity in the preceding steps.

## Relationship to prior work

Jen (1989, Section 4, Case e, pages 441–442) presents a general inverse-counting treatment of elementary Rule 232 over **unrestricted** binary sources, using coupled recurrences; that formula does not state the predecessor-fiber product for cyclic sources avoiding `11` nor the restricted image and singleton spectra. Salo (2022) develops cellular automata on subshifts and de Bruijn representations in a more general setting, without this evaluated restricted majority image. Published studies titled *The exact first-image subshift and entropy of binary majority cellular automaton* (2026) and *Exact cyclic image counts and spectral growth for elementary majority cellular automaton Rule 232* (2026) classify the **unrestricted-source** image language or cyclic output counts, not the hard-core-source fibers. The mathematical distinction is genuine: the present output set has smaller growth rate, and its inverse fibers use an entirely different gap-composition factor. Generic automaton methods are prior art, not claimed as new. Direct comparison with the relevant full texts and semantic-index searches did not identify an equivalent formula under the imposed source restriction.

## Limitations

The proof is restricted to the radius-one majority rule, binary indexed cycles and the cyclic hard-core source constraint. It is neither an arbitrary-input preimage theorem nor a claim about image complexity for all cellular automata or about multistep dynamics. This is a self-review, without an independent audit; priority may depend on specialized subshift publications not located in the consulted record. Finite numerical checks are supporting evidence, not an infinite proof.

## References

1. V. Salo, *On von Neumann regularity of cellular automata*, arXiv:2209.13373, first public 2022-09-27, https://arxiv.org/abs/2209.13373, especially Section 2 and the discussion of de Bruijn automata.
2. E. Jen, *Enumeration of Preimages in Cellular Automata*, *Complex Systems* 3 (1989), 421–456, https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf, especially pages 441–442.
3. *The exact first-image subshift and entropy of binary majority cellular automaton*, published online 2026-10-26, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-the-exact-first-image-subshift-and-entropy-of-binary-majority-ce--9a5867630f75, section Finding/Proof.
4. *Exact cyclic image counts and spectral growth for elementary majority cellular automaton Rule 232*, published online 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-cyclic-image-counts-and-spectral-growth-for-elementary-maj--da4a182e6a5a, section Finding/Relationship to prior work.
5. Wolfram Atlas, *Rule 232 - Rule properties*, https://atlas.wolfram.com/01/01/232/01_01_1_232.html (rule identification).
