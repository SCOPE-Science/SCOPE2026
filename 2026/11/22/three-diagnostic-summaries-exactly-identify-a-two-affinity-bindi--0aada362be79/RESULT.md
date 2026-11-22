# Three diagnostic summaries exactly identify a two-affinity binding mixture

## Finding
For an equilibrium mixture of two noninteracting one-site ligand-binding classes, the unique location and value of the minimum local Hill slope, together with the half-saturation concentration, determine **both dissociation constants and the class proportion uniquely**. Every positive minimum location, every minimum slope strictly between zero and one, and every positive half-saturation concentration occur, with no further feasibility restriction. None of the three possible pairs of these summaries identifies all three physical parameters.

Explicitly, write the measured summaries as \(m>0\) (minimum-slope concentration), \(0<h<1\) (minimum slope), and \(z>0\) (half-saturation concentration). Put
\[
r=2/h-1,\qquad c=rm,\qquad P=\frac{zm(z+rm)}{m+rz},\qquad d=\frac{rP}{m}.\]
The two distinct dissociation constants, ordered \(0<a<b\), and the fraction \(w\) of class \(a\) are exactly
\[
a=\frac{2P}{c+d+\sqrt{(c+d)^2-4P}},\qquad
b=\frac{c+d+\sqrt{(c+d)^2-4P}}2,\qquad
w=\frac{c-a}{b-a}.\]
The radical is always strictly real and these formulae always yield \(0<w<1\).

## Assumptions and scope
For every \(a,b\in\mathbb R\) and \(w\in\mathbb R\) satisfying \(0<a<b\) and \(0<w<1\), assume a normalized, noiseless, equilibrium binding curve with two independent monomer classes:
\[
F(x)=w\frac{x}{a+x}+(1-w)\frac{x}{b+x},\qquad x>0.
\]
The weight \(w\) is the proportion of sites belonging to the **lower dissociation constant** class. Both classes are noncooperative and saturate at one; this is a mixture of *classes*, not a model of two interacting sites on each protein. Define the local Hill *slope function*, not a single logistic-fit coefficient, by
\[
H(x)=\frac{d}{d\log x}\log\!\frac{F(x)}{1-F(x)}.
\]
Let \(m\) denote the unique minimizing concentration of \(H\), \(h=H(m)\), and \(z\) the unique concentration where \(F(z)=1/2\). No measurement error, unknown baseline, unknown saturation or time kinetics are included. Concentrations share common units.

## Proof
**1. Rational reduction.** Define
\[
c=wb+(1-w)a,\quad d=wa+(1-w)b,\quad P=ab.
\]
Then \(c+d=a+b\) and
\[
cd-P=w(1-w)(b-a)^2>0.
\]
Direct common-denominator reduction yields
\[
\frac{F(x)}{1-F(x)}=\frac{x(x+c)}{P+dx}.
\]
Differentiating its log odds gives
\[
H(x)=1-\frac{(cd-P)x}{(x+c)(P+dx)},\quad
H'(x)=-\frac{(cd-P)(cP-dx^2)}{(x+c)^2(P+dx)^2}.
\]
Thus \(H\) strictly decreases on \((0,\sqrt{cP/d})\), strictly increases thereafter, approaches one at both endpoints, and possesses exactly one strict global minimum at
\[
m=\sqrt{\frac{cP}{d}}.
\]
Evaluating the minimum yields
\[
h=\frac{2\sqrt P}{\sqrt P+\sqrt{cd}},\qquad 0<h<1.
\]
Since \(F\) increases strictly from zero to one, its half-saturation point is unique and satisfies
\[
z(z+c)=P+dz.
\]
**2. Exact inverse.** Given any \(m>0\), \(0<h<1\), \(z>0\), set \(r=2/h-1>1\). The minimum-depth equation forces \(cd=r^2P\). The minimum-location equation forces \(c=rm\) and \(d=rP/m\). The midpoint equation now forces
\[
P=\frac{zm(z+rm)}{m+rz}>0.
\]
The positive roots of \(t^2-(c+d)t+P=0\) satisfy \(0<a<b\): indeed \(cd=r^2P>P\) implies \((c+d)^2\ge4cd>4P\). Moreover, the quadratic is negative at \(t=c\), since its value there is \(P-cd<0\), so \(a<c<b\). Consequently \(w=(c-a)/(b-a)\) lies strictly between zero and one and obeys \(c=wb+(1-w)a\) and \(d=wa+(1-w)b\). The constructed model has the prescribed \(m,h,z\) by the forward equations. Conversely, those equations force all reconstruction steps, proving injectivity. This proves a bijection onto the entire stated open data region.

**3. Sharp insufficiency of any pair.** Holding any two entries of \((m,h,z)\) fixed and varying the remaining entry through its allowed open interval gives infinitely many distinct models by the established bijection. Thus no pair among these three summaries identifies the model. This statement concerns these specific summaries, not arbitrary encodings of data.

## Verification
For the exact example \((a,b,w)=(1,9,1/4)\), the intermediate quantities are \((c,d,P)=(3,7,9)\), giving
\[
m=\sqrt{27/7},\qquad h=\frac6{3+\sqrt{21}},\qquad z=2+\sqrt{13}.
\]
Substitution in the displayed inverse recovers \((1,9,1/4)\). A standalone Python 3 standard-library script, `CHECK.py`, checks the inversion and global minimum against deterministic random models, independently selected feasible summary triples, and the exact benchmark, reporting 22,503 passed assertions. These finite diagnostics are not a substitute for the proof of the universal quantifiers above; they only detect implementation/algebra errors in sampled cases.

## Relationship to prior work
Abeliovich (2005) gives the general weighted mixture binding isotherm, the local Hill-slope expression and the important warning that a slope below one does not distinguish a mixture from negative molecular cooperativity. Those forward facts are **prior work**, not the finding claimed here. Prinz (2009), Ravera et al. (2015), and later Middendorf and Aldrich (online December 2016) study related binding curves and identifiability, often for two binding sites on one protein and/or full-curve inference. The distinct statement proved here is a **global bijection from exactly three named scalar diagnostics of a two-class, arbitrarily weighted monomer mixture**, plus the entire feasible diagnostic region and the precise insufficiency of each diagnostic pair. The inspected work did not state or imply this three-summary characterization without additional derivation. More general identifiability results based on complete binding curves do not by themselves prove that these particular three compressed summaries always suffice.

## Limitations
The theorem is exact only for known normalization and perfect equilibrium responses. It cannot on its own discriminate heterogeneous classes from alternative cooperative molecular mechanisms generating the same curve. The minimum local slope may be difficult to estimate under noise or for nearly equal affinities, where \(h\) approaches one and the inverse is ill-conditioned. The claim is structural identifiability, not stable inference, data-fitting superiority, or experimental validation. A broader unindexed historical result could cover the three-summary inverse, and an independent scientific audit has not been performed.

## References
1. H. Abeliovich, “An Empirical Extremum Principle for the Hill Coefficient in Ligand-Protein Interactions Showing Negative Cooperativity,” *Biophysical Journal* **89** (2005), 76–79, https://doi.org/10.1529/biophysj.105.060194 (online 2005-04-15).
2. H. Prinz, “Hill coefficients, dose–response curves and allosteric mechanisms,” *Journal of Chemical Biology* **3** (2010), 37–44, https://doi.org/10.1007/s12154-009-0029-3 (online 2009-09-25).
3. S. Ravera et al., “Beyond non-integer Hill coefficients: A novel approach to analyzing binding data, applied to Na+-driven transporters,” *Journal of General Physiology* **145** (2015), 555–563, https://doi.org/10.1085/jgp.201511365.
4. T. R. Middendorf and R. W. Aldrich, “The structure of binding curves and practical identifiability of equilibrium ligand-binding parameters,” *Journal of General Physiology* **149** (2017), 121–147, https://doi.org/10.1085/jgp.201611703 (first online 2016-12-19; supplementary historical comparison).
