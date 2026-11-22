# A ten-periodic exact monochromatic-rectangle minimum for five-row grids

## Finding

For a positive integer \(b\), let \(\rho(5,b)\) denote the minimum number of monochromatic axis-parallel rectangles in a red–blue colouring of the \(5\times b\) array. A rectangle is determined by two distinct rows and two distinct columns and is monochromatic when all four corners have the same colour. Write \(b=5q+r\), where \(q\ge0\) and \(0\le r\le4\). Then, **for every \(b\ge1\)**,

\[
\rho(5,b)=10q(q-1)+4qr+2\mathbf{1}_{\{b\equiv5\pmod{10}\}}.
\]

Thus the natural discrete-convexity lower bound is attained for all widths except those congruent to five modulo ten; precisely in that class, the sharp excess is two. Equivalently, the monochromatic four-cycle minimum in red–blue edge-colourings of \(K_{5,b}\) has this formula. The first values for widths one through ten are \(0,0,0,0,2,4,8,12,16,20\).

## Assumptions and scope

The rows and columns are labelled, the two colours are distinct, repeated column patterns are permitted, and rectangles of either colour are counted once each. There is no restriction on a column's numbers of red and blue entries. All variables are ordinary nonnegative integers; no asymptotic limit, statistical sampling or geometric adjacency constraint is imposed. The theorem determines the optimal **number** for every width, not the number of optimal colourings or the maximum height of a three-dimensional box-free stack.

## Proof

**1. The twenty coloured row-pair counts.** Number rows \(0,1,2,3,4\). For each unordered row pair \(\{i,j\}\) and colour \(c\in\{0,1\}\), let \(k_{ijc}\) be the number of columns whose entries in both rows equal \(c\). There are exactly twenty such slots. Any monochromatic rectangle is uniquely determined by a slot and two columns counted in it, so its total number is

\[
R=\sum_{0\le i<j\le4}\sum_{c\in\{0,1\}}\binom{k_{ijc}}{2}.
\]

A column having \(m\) entries of colour one contributes

\[
\binom m2+\binom{5-m}{2}=4+(m-2)(m-3)
\]

to \(S:=\sum_{i<j,c}k_{ijc}\). This contribution is four when \(m=2\) or \(3\), six when \(m=1\) or \(4\), and ten when \(m=0\) or \(5\). Hence \(S\ge4b=20q+4r\), with equality exactly when every column is *balanced* (two or three entries of colour one). Discrete convexity of the function \(u\mapsto\binom u2\), and its monotonicity for nonnegative integer \(u\), give the lower bound

\[
R\ge20\binom q2+4rq=10q(q-1)+4qr=:L_b.
\]

**2. A strict obstruction at odd multiples of five.** Suppose \(b\equiv5\pmod{10}\). Then \(b=5q\), with \(q\) odd and at least one, and \(L_b=20\binom q2\). If any column is not balanced, \(S\ge20q+2\). Discrete convexity now gives \(R\ge L_b+2q\ge L_b+2\).

It remains to consider balanced columns. Then \(S=20q\), and expansion about \(q\) yields the exact identity

\[
R-L_b=\frac12\sum_{i<j,c}(k_{ijc}-q)^2.
\]

If \(R-L_b\) were zero, all twenty \(k_{ijc}\) would equal \(q\). If it were one, the twenty differences from \(q\) would consist of one \(+1\), one \(-1\), and eighteen zeros. In either case, among the ten unordered row pairs there would be **at most two** for which the total \(s_{ij}:=k_{ij0}+k_{ij1}\) is odd, because \(2q\) is even.

However, let \(d_{ij}=b-s_{ij}\) be the number of columns in which rows \(i\) and \(j\) have opposite colours. For any three rows, the sum of their three pairwise Hamming distances is even: each column contributes zero or two unequal pairs. Since \(b\) is odd, this gives

\[
s_{ij}+s_{ih}+s_{jh}\equiv1\pmod2
\]

for every triple \(\{i,j,h\}\). Thus *every* one of the ten triples of five rows must contain at least one row pair with odd \(s_{ij}\). Yet any one pair belongs to only three triples, so two pairs can cover at most six triples, an impossibility. Therefore \(R\ge L_b+2\) at all odd multiples of five.

**3. Matching colourings at every width.** Describe a column by an integer mask in \(\{0,\ldots,31\}\), whose binary digit at position \(i\) is the colour in row \(i\). Use the following three finite blocks, with column order specified:

\[
\begin{aligned}
B&=(3,5,10,13,14,19,20,22,24,25),\\
C&=(3,13,22,24),\\
W&=(24,12,18,11,21).
\end{aligned}
\]

All their columns are balanced. Direct substitution into the twenty-slot definition gives three finite identities: (a) the ten columns of \(B\) visit **each** coloured row-pair slot exactly twice; (b) the four columns of \(C\), which all occur in \(B\), visit sixteen different slots, each once; and (c) the five columns of \(W\) have slot counts \(0,1,2\) with respective multiplicities \(2,16,2\). All identities are checked independently by the included standalone `verify.py`.

Write \(b=10t+s\), with \(0\le s\le9\). Concatenate columns as follows:

- For \(s=0,1,2,3,4\), concatenate \(t\) complete copies of \(B\) and the first \(s\) columns of \(C\). Every slot has load \(2t\) or \(2t+1\), with exactly \(4s\) of the latter.
- For \(s=5\), concatenate \(t\) copies of \(B\) and the five columns of \(W\). Slot loads are \(2t,2t+1,2t+2\) with multiplicities \(2,16,2\), so the rectangle count exceeds \(L_b\) by exactly two.
- For \(s=6,7,8,9\), begin with \(t+1\) complete copies of \(B\) and remove the first \(10-s\) columns of \(C\) from one copy. Because these columns use disjoint slots, precisely \(4(10-s)\) slot loads drop from \(2t+2\) to \(2t+1\), and every other load remains \(2t+2\).

For \(s\ne5\), these load distributions attain the convexity bound \(L_b\). For \(s=5\), the displayed construction attains \(L_b+2\), which the obstruction in step 2 shows is best possible. This proves the theorem for every positive integer \(b\).

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter; there are no third-party dependencies. The script enumerates all twenty slots directly, verifies the exact block identities for \(B,C,W\), checks the ten-triangle parity hitting argument for sets of at most two exceptional row pairs, and compares direct four-corner rectangle enumeration against the formula on the explicit constructions for widths \(1\) through \(120\). The universal lower bound and every-width construction are supplied in the mathematical proof; the finite replay corroborates only its finite ingredients and sampled constructed widths.

## Relationship to prior work

Alm and Miller (arXiv:2611.19635v1, first public on 14 November 2026) define \(\rho(a,b)\), obtain small exact entries through dimension eight, and pose the determination of \(\rho(a,b)\) and the equality cases for its convexity bound as Problem 4. Their relevant table includes \(\rho(5,5)=2\), \(\rho(5,6)=4\), \(\rho(5,7)=8\), and \(\rho(5,8)=12\), consistent with the present formula but not implying its all-width periodic defect or constructions.

Cooper, Fenner, and Purewal (arXiv:0810.3019v1, Proposition 7.3) show how the exact minimum for fixed dimensions can be *expressed* as a finite integer quadratic optimization over column-type multiplicities. That general formulation does not evaluate its optimum symbolically for all widths with five rows; the closed formula and proof here give such an evaluation. Fenner, Gasarch, Glover, and Purewal (arXiv:1005.3750) classify which rectangles are avoidable, not the number forced at each width. Chang, Zhu, and Lin (2017) likewise study existence thresholds for monochromatic subrectangles of several shapes, not this all-width multiplicity. Existing diagonal numerical entries, e.g. OEIS A399620, are compatible with the theorem but cannot give the unrestricted width-five statement.

## Limitations

The proof treats exactly five rows and two colours. It neither classifies every optimal colouring nor determines exact minimum rectangle counts for other fixed heights; it does not settle when the layer bound for a three-dimensional box-free grid is attainable. Priority is qualified by the possibility of older, differently indexed supersaturation work. No independent mathematical audit has been performed.

## References

1. Jeremy F. Alm and Alex Miller, *Constructive and computational methods for extremal and near-extremal box colorings*, arXiv:2611.19635v1 (public 2026-11-14), especially Sections 3, 5, 8, and Appendix A. https://arxiv.org/pdf/2611.19635v1
2. Joshua Cooper, Stephen Fenner, and Semmy Purewal, *Monochromatic Boxes in Colored Grids*, arXiv:0810.3019v1, especially Section 7 and Proposition 7.3. https://arxiv.org/pdf/0810.3019
3. Stephen Fenner, William Gasarch, Charles Glover, and Semmy Purewal, *Rectangle Free Coloring of Grids*, arXiv:1005.3750, especially Sections 2 and 5. https://arxiv.org/pdf/1005.3750
4. Yi-Wu Chang, Jun-Yan Zhu, and Zi-Xuan Lin, *The Existence of (s,t)-Monochromatic-rectangles in a 2-colored Checkerboard*, IOSR Journal of Mathematics 13(2), 64–78 (2017), DOI:10.9790/5728-1302016478. https://www.iosrjournals.org/iosr-jm/papers/Vol13-issue2/Version-1/J1302016478.pdf
5. OEIS A399620, diagonal values for two-colour monochromatic rectangle minima. https://oeis.org/A399620
