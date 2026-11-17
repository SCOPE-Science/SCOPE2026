# Exact limit retractions and sharp pure-branch rates for largest-angle bisection

## Finding

Let \(\mathcal T=\{(x,y):0<y\le x\le1\}\) be the shape space of nondegenerate Euclidean triangles, where \(x\) and \(y\) are the ratios of the middle and smallest angles to the largest angle. Let \(L,R:\mathcal T\to\mathcal T\) be the two largest-angle-bisection child maps, with each child's angles resorted in decreasing order. For all initial shapes, both eventually pure branches converge to a *single, explicitly computable shape*, not merely to a fixed segment. The convergence becomes alternating geometric with the exact factor \(1/2\) after at most two \(L\)-steps or one \(R\)-step.

More precisely, define \(P_L(x,y)=(\ell(x,y),1/2)\) by
\[
\ell(x,y)=\begin{cases}
\dfrac{3x}{2(1+y)},&x\ge1/2,\ y\ge x-1/2,\\
\dfrac{3(y+1/2)}{2x+1},&x\ge1/2,\ y<x-1/2,\\
\dfrac{3}{4(x+y+1/2)},&x<1/2,\ 2x+y\ge1/2,\\
\dfrac{3(2x+y+1/2)}{3+2y},&x<1/2,\ 2x+y<1/2,
\end{cases}
\]
and \(P_R(x,y)=(1/2,r(x,y))\), where
\[
r(x,y)=\begin{cases}
\dfrac{3y}{2(1+x)},&y\le1/2,\\
\dfrac{3}{4(x+y+1/2)},&y>1/2.
\end{cases}
\]
Then for every \(z\in\mathcal T\),
\[
\lim_{n\to\infty}L^n z=P_L(z),\qquad
\lim_{n\to\infty}R^n z=P_R(z).
\]
The maps \(P_L,P_R\) are continuous piecewise-rational retractions onto the two fixed segments. They satisfy \(P_L\circ L=P_L\), \(P_R\circ R=P_R\), and \(P_L^2=P_L\), \(P_R^2=P_R\). The universal eventual factor \(1/2\), the two-step left entry, and the one-step right entry are sharp.

## Assumptions and scope

A triangle's largest, middle, and smallest angles are positive and sorted; at equal angles any consistent assignment of the two named children is allowed. The normalized shape \((x,y)\) represents the positive-angle ratio triple \((1,x,y)\). The transformations are the two sorted, renormalized triples
\[
L(x,y)=\operatorname{norm}(1/2,x,y+1/2),\qquad
R(x,y)=\operatorname{norm}(1/2,y,x+1/2),
\]
where \(\operatorname{norm}(a,b,c)\) sorts the three positive entries descending, then divides the two smaller entries by the largest.

Put
\[
F=\{(x,y)\in\mathcal T:x\ge1/2,\ y\ge x-1/2\},\qquad
G=\{(x,y)\in\mathcal T:y\le1/2\}.
\]
The theorem concerns iteration of one fixed child map, or an arbitrary finite prefix followed by repeated application of that map. It does not assert that a general mixed branch has the same limit.

## Proof

**Step 1: invariant chambers and finite entry.** Direct ordering of the left-child angle triple gives
\[
L(x,y)=\begin{cases}
\left(\dfrac{x}{y+1/2},\dfrac{1/2}{y+1/2}\right),&x\ge1/2,\ y\ge x-1/2,\\
\left(\dfrac{y+1/2}{x},\dfrac{1/2}{x}\right),&x\ge1/2,\ y<x-1/2,\\
\left(\dfrac{1/2}{y+1/2},\dfrac{x}{y+1/2}\right),&x<1/2.
\end{cases}
\]
On \(F\), the first branch maps back to \(F\): its first coordinate is at least \(1/2\) because \(2x\ge y+1/2\); its second is at least its first minus \(1/2\) because \(x\le3/4+y/2\), as follows from \(y\ge x-1/2\) and \(x\le1\). Thus \(L(F)\subseteq F\).

For \(x\ge1/2\) outside \(F\), the second branch has its image in \(F\), using \(y<x-1/2\le x/2\). For \(x<1/2\), the third branch enters \(F\) immediately exactly when \(2x+y\ge1/2\). Otherwise it enters the preceding second-branch chamber, and direct composition yields
\[
L^2(x,y)=(2x+y+1/2,\ y+1/2)\in F.
\]
This proves \(L^2(\mathcal T)\subseteq F\), including the chamber boundaries.

The right child has the exact two-branch formula
\[
R(x,y)=\begin{cases}
\left(\dfrac{1/2}{x+1/2},\dfrac{y}{x+1/2}\right),&y\le1/2,\\
\left(\dfrac{y}{x+1/2},\dfrac{1/2}{x+1/2}\right),&y>1/2.
\end{cases}
\]
In the first branch the new second coordinate is at most \(1/2\); in the second branch it is likewise at most \(1/2\) because \(x\ge y>1/2\). Hence \(R(\mathcal T)\subseteq G\), and automatically \(R(G)\subseteq G\).

**Step 2: closed-form iterates in the invariant chambers.** On \(F\), represent the initial sorted angles homogeneously by \((1,x,y)\). Each left move replaces the sorted triple \((a,b,c)\) by \((a/2+c,b,a/2)\). The middle angle \(b=x\) and the sum \(S=a+c=1+y\) remain fixed, while the leading angle satisfies \(a_{n+1}=S-a_n/2\). Solving this scalar recurrence gives
\[
A_n=\frac{2(1+y)}3+\frac{1-2y}3\left(-\frac12\right)^n,
\qquad
L^n(x,y)=\left(\frac{x}{A_n},\frac{1+y}{A_n}-1\right)
\quad(n\ge0,\ (x,y)\in F).
\]
Its limit is \((3x/[2(1+y)],1/2)\), and its deviation alternates in sign with decay factor exactly \(1/2\) unless \(y=1/2\), when the shape is already fixed.

On \(G\), each right move replaces \((a,b,c)\) by \((a/2+b,a/2,c)\). The smallest angle \(c=y\) and sum \(S=a+b=1+x\) remain fixed. The same scalar recurrence yields
\[
B_n=\frac{2(1+x)}3+\frac{1-2x}3\left(-\frac12\right)^n,
\qquad
R^n(x,y)=\left(\frac{1+x}{B_n}-1,\frac{y}{B_n}\right)
\quad(n\ge0,\ (x,y)\in G).
\]
Its limit is \((1/2,3y/[2(1+x)])\), with the same alternating factor unless \(x=1/2\). Positivity of the actual sorted angle triples guarantees positive denominators and preservation of the displayed chamber ordering for every iterate.

**Step 3: evaluate the entry transients.** Apply the stable-chamber limit formula after zero, one, or two left steps, according to the four chambers in Step 1. The corresponding first coordinates are, respectively,
\[
\frac{3x}{2(1+y)},\quad
\frac{3(y+1/2)}{2x+1},\quad
\frac{3}{4(x+y+1/2)},\quad
\frac{3(2x+y+1/2)}{3+2y}.
\]
For the right branch, applying the stable formula directly when \(y\le1/2\) or after one right step when \(y>1/2\) produces the two displayed expressions for \(r\). Since each chamber formula is an actual pointwise limit of continuous iterates, the projection maps are continuous across their common boundaries; direct substitution also verifies boundary agreement. Their images are the fixed sets
\[
C_L=\{(u,1/2):1/2\le u\le1\},\quad
C_R=\{(1/2,v):0<v\le1/2\}.
\]
On these segments the corresponding child map is the identity. This proves idempotence and the orbit-invariance identities.

**Step 4: sharpness and arbitrary finite prefixes.** The shape \((1/10,1/10)\) lies outside \(F\), and its first left child still lies outside \(F\); thus the two-step bound cannot be reduced to one. The shape \((4/5,3/5)\) lies outside \(G\), so the one-step bound cannot be reduced to zero. The nonfixed stable-chamber shape \((3/4,1/4)\) has a nonzero \((-1/2)^n\) coefficient for both child maps; thus no smaller universal exponential factor works. More precisely, for any nonfixed initial point already in its stable chamber, the ratio of successive nonzero coordinate errors tends to \(-1/2\). A finite prefix \(w\) followed by only \(L\) or only \(R\) has limit \(P_L(wz)\) or \(P_R(wz)\), respectively, with the same eventual rate and finite entry bounds.

## Verification

Run `python3 verify.py` with only the Python standard library. Its independently implemented sorted-angle child maps and exact rational arithmetic check 743 initial shapes, including four rational grids. For each it verifies finite chamber entry, one-step invariance of both projections, idempotence, all iterates through step 12 against the closed forms, the projections against their post-entry formulas, and the codomain inequalities. Separate rational witnesses establish the optimal entry transients and nontrivial geometric decay. Actual execution output was:

`PASS: 743 exact-rational initial states; both projection identities, entry thresholds, iterates 0..12, and sharpness witnesses`

The infinite statements are proved algebraically above; finite checks do not replace that proof. No external proof certification has been performed.

## Relationship to prior work

Michaud's November 4, 2026 preprint supplies these piecewise projective child maps, identifies their respective fixed segments (Proposition 3), and proves that pure iterates approach the segments (Proposition 7); it does not identify the individual limiting fixed point, entry times, or exact oscillatory convergence rate. Its infinite-itinerary classification is credited, not claimed here. The new pointwise limit retractions refine its qualitative pure-branch theorem.

Ismailescu, Kim, Kim, and Lee (2019) established regularity and size decay for largest-angle bisection; Michaud and Korotov (July 2026) extended regularity to largest-angle \(n\)-section. Neither states these pointwise pure-branch formulas. A closely related subsequently published mixed-child contraction result gives a sharp \(3/4\) factor for unlike consecutive children and full-tree concentration, but does not determine the exceptional pure-child endpoint or its rate. That result is mathematically complementary, not stronger coverage of this claim.

## Limitations

The result concerns planar largest-angle bisection, the two precisely defined labelled child maps, and eventually constant symbol itineraries; no claims about arbitrary infinite alternations, adaptive mesh conformity, random branches, Euclidean diameter decay, or area-weighted sampling are made. Sharpness is for a universal *eventual* exponential rate and chamber-entry time, not for a uniform one-step bound from all starts. Historical priority outside inspected literature is not independently established. No independent audit has been performed.

## References

1. J. Michaud, *Largest-Angle Bisection and Statistical Regularization of Triangle Shapes*, arXiv:2611.06492v1, first posted November 4, 2026, https://arxiv.org/abs/2611.06492 . In particular Proposition 1, Proposition 3 and Proposition 7.
2. D. Ismailescu, J. Kim, K. Kim, and J. Lee, *The largest angle bisection procedure*, arXiv:1908.02749v1, first posted August 6, 2019, https://arxiv.org/abs/1908.02749 .
3. J. Michaud and S. Korotov, *On Triangulations Generated by the Largest-Angle \(n\)-Section Algorithm*, arXiv:2607.25457v1, first posted July 28, 2026, https://arxiv.org/abs/2607.25457 .
4. *Sharp mixed-child contraction and exponential shape concentration for largest-angle bisection*, published November 8, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-mixed-child-contraction-and-exponential-shape-concentratio--30fda51bbc9b .
