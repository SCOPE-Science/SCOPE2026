# Sharp coloured cyclic-order extension ranks and the first binary extremal census

## Finding

Let \(q\ge 1\), and let \(\mathcal K_q\) be the age of all finite **oriented total cyclic orders** equipped with an exhaustive partition into \(q\) named unary colours. The language contains one strict ternary cyclic-order relation \(C\) and the \(q\) unary predicates, with no named start point or successor. Let \(\operatorname{rk}_X(F)\) be the one-point-extension rank of a finite marked induced substructure \(F\subseteq X\), relative to the whole age \(\mathcal K_q\).

**Theorem (full relative-rank reduction and sharp extremal size).** There is an explicit gap recursion (given below) which calculates \(\operatorname{rk}_X(F)\) for **every** finite coloured cyclic order \(X\) and every marked subset \(F\). In particular, for every integer \(t\ge1\):

\[
\min\{|X|:\operatorname{rk}_X(\varnothing)\ge t\}=q\,2^{t-1}.
\]

More precisely, every cyclic word of rank at least \(t\) contains at least \(2^{t-1}\) vertices **of each colour**, and this simultaneous lower bound is attained by repeating any permutation of the \(q\) colours cyclically \(2^{t-1}\) times. Consequently the greatest possible rank at host order \(n\) is \(0\) when \(n<q\), and otherwise is

\[
1+\left\lfloor\log_2(n/q)\right\rfloor.
\]

In fact rank at least two holds exactly when each named colour occurs at least twice, independently of cyclic order. At the first nontrivial two-colour equality boundary, \(q=2\) and \(t=3\), a host of minimum order \(8\) has rank three exactly when each colour occurs four times and its cyclic word is **not** a rotation of \(00001111\). Hence precisely \(62\) of the \(\binom84=70\) balanced words on eight distinguished cyclic positions have rank three, forming exactly \(9\) isomorphism classes under orientation-preserving rotations. Their orbit sizes are \(2,4,8,8,8,8,8,8,8\).

## Assumptions and scope

For distinct vertices \(a,b,c\), \(C(a,b,c)\) holds precisely when the positive circular direction from \(a\) encounters \(b\) before \(c\); a triple with repeated entries never satisfies \(C\). A zero-, one-, or two-vertex cyclic structure has the induced empty ternary relation, and is included in the age. Each vertex satisfies exactly one of the \(q\) unary predicates. A cyclic word represents a finite such structure up to a cyclic rotation, **not** up to reversal, because its cyclic orientation is named.

The rank is defined by \(\operatorname{rk}_X(F)\ge0\) and, for integers \(s\ge0\), by \(\operatorname{rk}_X(F)\ge s+1\) when every abstract one-point extension type over the individually identified marked set \(F\) has some realization \(F\cup\{x\}\) in \(X\) with \(\operatorname{rk}_X(F\cup\{x\})\ge s\). For finite \(X\), each move increases the marked set and all ranks are finite integers. The cardinalities and rank thresholds quantify over all positive palette sizes and all finite hosts; the eight-point census is specifically for two named colours.

Write \(\Sigma\) for the named colour palette. For a finite **linear** word \(u\in\Sigma^*\), define \(\rho(u)\) recursively. It is \(0\) if any palette colour is absent; otherwise

\[
\rho(u)=1+\min_{c\in\Sigma}\ \max_{i:u_i=c}\ \min\big\{\rho(u_{<i}),\rho(u_{>i})\big\}.
\]

This is a finite recursion on length; the subscripts denote strict left and right subwords. For two distinct vertices \(x,y\) in a cyclic word \(w\), write \(A(x,y)\) for the linear colour word strictly along the positive open arc from \(x\) to \(y\).

## Proof

**1. All relative ranks.** If a marked subset \(F\) has at least two points, the one-point extensions of \(F\) in \(\mathcal K_q\) are obtained by inserting a point of an arbitrary named colour into any one of the distinct oriented gaps between consecutive points of \(F\). Once the new point is inserted, that gap splits into two linear subwords; the other gaps remain unchanged. Induction on the unmarked host size and on the proposed rank gives

\[
\operatorname{rk}_X(F)=\min_{I\text{ a cyclic gap of }F}\rho(w|_I),\qquad |F|\ge2.
\]

(The induction uses the same minimum-of-gaps formula on the child position and the monotonicity of the rank threshold in a gap.) The special cases with fewer than two marked points are important: for a singleton \(F=\{x\}\) the colour of the second vertex is the *only* extension-type datum, as the ternary relation remains empty. Accordingly,

\[
R_x=0\quad\text{if a colour is absent from }X\setminus\{x\};
\]
\[
R_x=1+\min_{c\in\Sigma}\max_{y\ne x:\,\chi(y)=c}
\min\{\rho(A(x,y)),\rho(A(y,x))\}
\quad\text{otherwise}.
\]

For an empty marked set, a one-point extension specifies only a colour, so

\[
R_{\varnothing}=0\quad\text{if some colour is absent from }X;
\]
\[
R_{\varnothing}=1+\min_{c\in\Sigma}\max_{x:\,\chi(x)=c}R_x
\quad\text{otherwise}.
\]

We have \(R_x=\operatorname{rk}_X(\{x\})\) and \(R_{\varnothing}=\operatorname{rk}_X(\varnothing)\). These equations prove the claimed exact computation for every marked subset, including the low-cardinality boundary where a naïve circular-gap formula would be wrong.

**2. Letter-multiplicity lemma.** For every integer \(s\ge0\), if \(\rho(u)\ge s\), then every colour occurs at least \(2^s-1\) times in \(u\). The case \(s=0\) is empty. At a positive rank, fix a colour \(c\); some occurrence of \(c\) has left and right subwords both of rank at least \(s-1\). By induction each subword has at least \(2^{s-1}-1\) occurrences of \(c\), giving \(2^s-1\) including the pivot.

Conversely, if \(\pi\) is any linear permutation of all \(q\) named colours, then

\[
\rho\big(\pi^{\,2^s-1}\big)\ge s.
\]

This follows by induction: take the occurrence of any challenged colour in the central copy of \(\pi\), leaving \(2^{s-1}-1\) complete copies of \(\pi\) on each side. Since inserting extra letters cannot decrease a relative extension rank (or by direct induction from the definition of \(\rho\)), every contiguous linear subword of a periodic repetition of \(\pi\) of length at least \(q(2^s-1)\) has \(\rho\ge s\). Its first \(q(2^s-1)\) letters are repetitions of a cyclic rotation of \(\pi\), itself a full-colour permutation.

**3. Sharp lower bound, including colours separately.** If \(\operatorname{rk}_X(\varnothing)\ge1\), every colour occurs at least once, giving the asserted \(2^0\) lower bound. For \(t\ge2\), fix an arbitrary colour \(c\). From the empty-rank definition there is a first marked point \(x\) of colour \(c\) with \(R_x\ge t-1\). From the singleton-rank definition, challenging colour \(c\) again yields a *different* point \(y\) of colour \(c\) with \(\rho(A(x,y)),\rho(A(y,x))\ge t-2\). By Step 2, each of the two disjoint open arcs contains at least \(2^{t-2}-1\) points of colour \(c\). Including \(x,y\), there are at least \(2^{t-1}\) points of colour \(c\). As \(c\) was arbitrary, \(|X|\ge q2^{t-1}\).

**4. Periodic equality construction.** Let \(X\) be the cyclic word \(\pi^{\,2^{t-1}}\), where \(\pi\) permutes the \(q\) distinct colours. Rank at least one is immediate. For \(t\ge2\), take *any* first point \(x\), with colour \(c\). Set \(r=2^{t-2}\). For any challenged second colour \(d\), choose the corresponding occurrence \(y\) in the length-\(q\) period beginning exactly \(qr\) positions after \(x\). Its offset within that period is some \(\delta\in\{0,\ldots,q-1\}\). The two open arcs from \(x\) to \(y\) and back have lengths \(qr+\delta-1\) and \(qr-\delta-1\), both at least \(q(r-1)\). Each is a segment of the periodic colour word, hence by Step 2 has linear rank at least \(t-2\). Thus \(R_x\ge t-1\) for every first point and \(R_\varnothing\ge t\). This meets the lower bound. For arbitrary larger orders, add points without changing the cyclic order of the witness; rank monotonicity under induced superstructures gives the maximum-rank formula.

**5. Eight-point binary equality census.** For \(q=2,t=3\), Step 3 forces four occurrences of each colour. A binary word with four zeros and four ones is therefore the only kind of possible eight-point witness. A direct complete classification of these balanced necklaces is given in the reproducible checker and the following certificate. The ten canonical rotations are:

```
00001111  -- does not achieve rank 3
00010111  00011011  00011101
00100111  00101011  00101101
00110011  00110101  01010101
```

For each of the nine positive representatives, the following certificate gives for both possible first colours a first-point index and one feasible second-point index of **each** challenged colour; indices are zero-based in the displayed word. The notation \( (i;j_0,j_1)\) signifies first point at position \(i\), with second point at \(j_d\) when the second challenge is colour \(d\).

| Canonical word | First colour 0 | First colour 1 |
|---|---|---|
| `00010111` | `(1;4,5)` | `(6;1,3)` |
| `00011011` | `(1;5,4)` | `(4;0,7)` |
| `00011101` | `(1;6,4)` | `(4;0,7)` |
| `00100111` | `(1;4,5)` | `(6;1,2)` |
| `00101011` | `(0;3,4)` | `(2;5,6)` |
| `00101101` | `(0;3,4)` | `(2;6,5)` |
| `00110011` | `(0;4,3)` | `(2;5,6)` |
| `00110101` | `(0;4,3)` | `(2;6,5)` |
| `01010101` | `(0;4,3)` | `(1;4,5)` |

For every displayed pair of indices the two resulting oriented open arcs both contain both colours (this can be checked directly by reading the word cyclically). Each arc therefore has \(\rho\ge1\), making the empty rank at least three. In the excluded two-run word, after any first point of colour \(c\), every possible second point of the same colour leaves a monochromatic open arc, so rank three fails. There are exactly ten balanced necklaces: Burnside's lemma gives \( (70+2+6+2)/8=10\) (the nontrivial rotations with fixed balanced words contribute \(2,6,2\)). Exactly eight of the \(70\) balanced labelled words are rotations of the excluded word, leaving \(62\). Rotating the nine positive representatives yields orbit sizes \(8\) seven times, \(4\) once, and \(2\) once. Their total is \(62\), so the certificate is exhaustive.

## Verification

The accompanying `checker.py` uses two independently structured evaluators: (i) the original one-point extension game recursively on *every marked subset* of each finite cyclic host, and (ii) the gap/min–max identities from Step 1. It compares all marked ranks, not only the empty rank, for all words over one colour through length eleven, all two-colour words through length eight, and all three-colour words through length six (\(1{,}616\) complete host words in total). Periodic equality constructions are also evaluated directly at all tested palette/threshold pairs with host size at most sixteen. An independent full game enumeration of the binary balanced eight-point stratum verifies the \(62\) labelled witnesses, \(9\) cyclic isomorphism classes and orbit sizes. Run `python3 checker.py` with the Python 3 standard library.

The proofs in Steps 1–5 establish the infinite parameter assertions and the finite census, respectively; bounded computation is corroboration and does not certify an arbitrary unexamined host.

## Relationship to prior work

López-Callejas and Navarro-Castillo (2026) define the one-point-extension rank and calculate it for ordinary finite linear orders, but do not state a coloured **cyclic** relative-rank formula or the colourwise bound above. Their finite linear-order result has a different small-marked-set geometry; a cyclic order cannot be replaced by a linear order without choosing a parameter, and the null/one-point cases are essential.

The coloured linear-word gap recursion is a useful ingredient in the present proof, but a linear word with two ends does not have the two-arc condition imposed by a ternary cyclic order. The new circular reduction, per-colour minimum-host law and nontrivial binary eight-point orbit census are not claims about linear words.

The published exact finite-uncoloured cyclic-order **first-order quantifier-rank** cutoff (published-finding corpus, November 2026) is a different invariant: it compares two cyclic orders by an Ehrenfeucht–Fraïssé game, while the present rank challenges all one-point extensions **inside one fixed host**. It supplies a matching uncoloured scale but neither the coloured relative-rank recursion nor the sharp colourwise law. Mwesigye and Truss (2018) treat first-order equivalence of coloured *linear* orders, likewise not this invariant or circular host class. Snowden (2026) lists cyclic orders and coloured linear orders as separate canonical Fraïssé examples, but does not calculate this rank.

## Limitations

The theorem assumes finite **total oriented** cyclic orders and an exhaustive partition into named colours. It does not treat partial cyclic orders, named successor, a chosen start point, reversal-identified cycles, or infinite host ranks. The full relative-rank algorithm may require exponential time if evaluated by naive enumeration. The eight-point classification is for exactly two colours; no enumeration of all minimum-host types at arbitrary palette sizes or rank levels is claimed. Historical priority is supported by the specific comparisons listed but is not exhaustively established; independent mathematical validation has not been performed.

## References

- C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461v1, first publicly submitted 2026-04-15, Sections 2, 6 and 7. https://arxiv.org/html/2604.14461v1
- F. Mwesigye and J. K. Truss, *On Optimal Representatives of Finite Coloured Linear Orders*, *Order* 36 (2019), 107–117, first published online 2018-05-02, doi:10.1007/s11083-018-9458-3. https://link.springer.com/content/pdf/10.1007/s11083-018-9458-3.pdf
- A. Snowden, *Oligomorphic Groups and Tensor Categories: A Summary*, ICM 2026, Section 4.3, doi:10.1137/25M1806223. https://epubs.siam.org/doi/10.1137/25M1806223
- *Sharp quantifier-rank cutoff and three-variable completeness for finite cyclic orders*, published scientific result, 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-quantifier-rank-cutoff-and-three-variable-completeness-for--5fa0dcc54b96
